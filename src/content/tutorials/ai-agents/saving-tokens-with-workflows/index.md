---
title: Save agent tokens with workflows
linkTitle: Save tokens with workflows
description: Why a Muster workflow makes an AI agent dramatically cheaper, with the measured before-and-after numbers and the design rules that maximize the saving.
weight: 15
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-saving-tokens-with-workflows
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - Why do workflows make my AI agent cheaper?
  - How much do Muster workflows reduce token cost?
  - How do I design a workflow to minimize agent token cost?
---

A workflow doesn't just save you clicks. It makes your AI agent dramatically cheaper to run. One `workflow_<name>` call runs every step server-side and returns one condensed document, so the agent pays for a single call and a single response instead of many round-trips. This guide makes the economic case with measured numbers, then gives you the design rules that maximize the saving. For the field-by-field mechanics of writing the resource, see [Author a workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}).

## Where the tokens go

When an agent investigates a problem with the raw aggregated tools, it runs a discover-query-correlate loop itself. It finds the right tool and reads its schema. Then it lists pods and events, queries a metric, and reads a log. It reasons over the results to decide what to call next. Every one of those is a separate tool call, and every tool call is a round-trip.

The expensive part isn't the answer. It's the conversation. Each round-trip re-sends the whole transcript so far—the system prompt, every prior tool result, every reasoning step—back to the model as input. As the investigation grows, each new call carries more context than the last. That's why **cache-read input tokens dominate the bill**: the same growing transcript is read over and over. A loop that takes dozens of calls reads millions of cached tokens before it reaches a conclusion.

## What a workflow changes

A workflow collapses that loop into one server-side call. The agent invokes `call_tool(name="workflow_<name>", arguments={...})` once. Muster walks the steps itself, calls the same underlying tools, shapes the combined output, and returns one document. The agent pays for exactly one call and one response. The round-trips that re-read the transcript never happen, because there's no back-and-forth to re-read.

Picture the same alert triage both ways:

- **Raw tools**: discover the Kubernetes tools, read a schema, list not-running pods, list crash-loop events, query a metric, read a log, correlate—each a round-trip that re-sends a growing transcript.
- **Workflow**: one `call_tool(name="workflow_alert-triage", arguments={management_cluster: "<mc>"})`. Muster runs every step server-side and returns a single digest.

## The measured saving

The figures below come from one internal lab trial. Treat them as illustrative of the *shape* of the saving, not as a guarantee: the ratios hold across a range of investigations, but the absolute numbers depend on the model, its pricing, and how much work each alert needs.

The trial was a paired A/B run: the same agent, model, and prompt against four real management-cluster alerts. The only difference was the tool surface—one variant could use the raw aggregated tools (`x_kubernetes_*` and `x_prometheus_*`) but no workflow, the other could only call the matching `workflow_*` tool. Aggregated across the four alerts:

| Metric | Raw aggregated tools | Workflow tool | Reduction |
|---|--:|--:|--:|
| Cost | $4.32 | $1.57 | 2.8x |
| Messages | 334 | 71 | 4.7x |
| Cache-read input tokens | 11.0M | 1.1M | 9.6x |
| Tool-call invocations | 68 | 4 | 17x |

Read the tool-call row first: 68 calls became four, one per alert. That's the mechanism in a single number—the entire discover-query-correlate loop became one delegated call. The cache-read row is where the durable saving lives: those tokens drive the dollar cost, and they fell by about 10x regardless of the per-token price.

The saving scales with how much investigation an alert needs. The most exploratory alert saw a 4.7x message reduction at the high end of the run, and the most static one around 2.9x. Heavy, open-ended triage saves the most, while near-static checks save the least.

## Design rules that maximize the saving

A workflow saves tokens by default, but a few choices decide whether you capture a 3x win or a 10x one.

### Shape a tight response

The agent pays for everything the workflow returns, so the returned document is the single biggest token lever you control. By default a workflow returns a full envelope: `execution_id`, `workflow`, `status`, `input`, and a `steps[]` array carrying every step's payload. That array grows with every step, every `forEach` iteration, and every `parallel` sub-step. One unbounded step produces a multi-million-token outlier even when the typical run is small.

The strongest fix is a workflow-level `spec.output` projection. It's a templated map, rendered once after every step completes, that **replaces** the default envelope with the exact shape you define. Instead of the whole `steps[]` array, the agent receives one small digest:

```yaml
spec:
  output:
    not_running_pods: "{{ .results.not_running.items }}"
    backoff_count: "{{ len .results.backoff_events.items }}"
    cluster: "{{ .input.management_cluster }}"
```

The projection can read every step result through `{{ .results.<id>.<field> }}`, so you pull just the fields that matter and drop everything else. The projection preserves JSON types, so a bare reference stays an array and a `{{ len ... }}` leaf stays a number. When you declare it, the per-step flags below no longer shape the returned document, and Muster logs a one-line warning naming any flag it made inert. See [shape the response with `spec.output`]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}#shape-the-response-with-specoutput) for the full schema.

Without a projection, the per-step `output` flag is the next lever. Set `output: true` only on the steps whose data the agent actually needs to read. A step without it still runs, and later steps can still read its result, but Muster keeps only its status in the returned document and drops the payload. `store: true` is the deprecated, older name for `output: true`: it still works but logs a warning, so prefer `output`.

Then cap whatever does land in the response:

- Set `limit:` on every list. Ten events is plenty, and more just feeds noise.
- Set `tailLines: 30` on any log fetch. The default is 100 and the maximum is 1000, enough to swamp the prompt window on a healthy system.
- Set `output: slim` on lists to strip verbose fields. That's the tool's own response knob, separate from the step-level `output` flag.

### Fan out server-side, not in the agent

When a check spans several clusters or several resource types, do the fan-out inside the workflow so it stays one agent call:

- Use `forEach` to repeat a step over a list argument. Looping over `{{ .input.clusters }}` keeps the whole fleet check in one call instead of one agent round-trip per cluster.
- Use `parallel` to run independent reads concurrently. Latency becomes the max over the group rather than the sum, while the result still returns as one document.

Both keep the saving intact: the agent still makes a single call no matter how many underlying tools run. Remember that the per-step caps described earlier apply to every iteration, so a loop over a large list is the easiest way to undo the win. The full mechanics are in [Authoring workflows]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}#control-flow).

### Skip the expensive step unless it's needed

The cheapest step is the one that never runs. A step's `condition` reads a prior result and decides whether to run the step or skip it. A skipped step costs nothing: no tool call, and no output in the response. Use it to gate the costly part of a workflow on a cheap signal:

- A `template` condition gates on an input or a prior field without any tool call, for example `'{{ eq .input.env "production" }}'`.
- A `jsonPath` condition checks a value at a dotted path in an earlier step's result, for example running a deep drill-down only when a quick list already shows something not running.

A `jsonPath` condition is a **gate**, not a way to trim what a step returns. It decides whether the step runs, not how the response is shaped. The path navigates into an earlier step's result, for example `data.field`. So pair a cheap, capped first step with an expensive second step gated on it, and the expensive half runs only when the cheap half found something worth the tokens. See [conditions]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}#conditions) for the full schema.

### Keep the description lean and stop-aware

Only `spec.description` reaches the agent at call time, and it does double duty for cost. Two directives matter most:

- A **stop-when-healthy rule**: state the exact conditions that mean no follow-up is needed, plus an instruction to write a one-line summary and stop. Without it, an agent reads a clean result as an invitation to keep exploring with raw tools, and the saving evaporates.
- **Discoverable wording**: an agent finds a workflow through a case-insensitive substring match over the description, with no stemming or synonyms. If the description doesn't literally contain the terms the agent searches by, the agent never finds the workflow and falls back to the expensive raw-tool loop. Lead with both the topic keyword and the natural question phrasing.

A few hundred characters of description are far cheaper than the dozen extra calls they prevent.

## The honest trade-off

A workflow is cheaper precisely because it only checks what it was authored to check. For a first responder handling the specific alert that paged, that focus is a feature. For open-ended "what's broken here?" exploration, an agent with the raw tools surfaces more adjacent context at higher cost. In the trial, one alert showed this directly. The workflow correctly reported its alert wasn't firing, while the free-roaming agent dug further and found two unrelated apps broken at about three times the cost. Build workflows for the focused, repeatable questions, and leave the raw tools available for genuine exploration. Both run through the same gateway.

## Related

- [Author a workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}): the field-by-field guide to writing the resource.
- [Muster architecture]({{< relref "/overview/ai-agents/architecture" >}}#workflows-cut-agent-token-cost): where this saving fits in the bigger picture.
- [Meta-tools and discovery]({{< relref "/overview/ai-agents/meta-tools" >}}): how an agent finds and invokes a `workflow_<name>` tool.
- [Give agents multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}): the fleet setup that makes `forEach` fan-out worthwhile.
