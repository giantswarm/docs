---
title: Author a Muster workflow
linkTitle: Author a workflow
description: Write a Muster Workflow resource that packages a multi-step operation into one named tool an AI agent can discover and call, grounded in the fields the engine actually implements.
weight: 10
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-authoring-workflows
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I author a Muster workflow?
  - What fields does a Muster Workflow support?
  - Why doesn't my AI agent find my workflow?
  - How do I keep a workflow's token cost low?
---

A workflow packages a multi-step operation into a single named tool. You write it as a `Workflow` custom resource, and Muster registers it as a `workflow_<name>` tool that an agent discovers and calls with one request. Muster runs the steps server-side and returns one shaped result. That's the whole value: it collapses what would otherwise be many agent round-trips, each paying prompt tokens both ways, into a single call. A paired trial measured a 10x reduction in cache-read tokens when an agent used a workflow instead of the raw tools. See [why workflows cut agent cost]({{< relref "/overview/ai-agents/architecture" >}}#workflows-cut-agent-token-cost).

This guide documents what the engine implements. Write against these fields and your workflow behaves predictably. For the complete field-by-field schema of the `Workflow` resource, see the [Muster resource reference]({{< relref "/reference/muster" >}}).

## The execution model

A workflow is an ordered list of steps that Muster runs server-side, returning one JSON document. Top-level steps run **sequentially**, but a step isn't always a single tool call. Each top-level step is exactly one of a plain `tool` call, a `forEach` loop, or a `parallel` group. A workflow-level `onFailure` block can run best-effort cleanup when a step fails. Design every workflow around one fact: it collapses many agent round-trips into a single call, and its response cost is the sum over everything it returns.

Every step's result is **always** available to later steps and the response projection through `{{ .results.<id>.<field> }}`. That holds regardless of any flag. You separately control what the *agent* sees back. The per-step `output` flag picks which step results land in the returned document. The workflow-level `spec.output` projection replaces that document with a shape you define.

> Control flow (`forEach`, `parallel`, `onFailure`, and template conditions) requires Muster 0.8.0 or later. Plain sequential `tool` steps work on every version.

## A complete example

This read-only workflow lists not-running pods and crash-loop events on a management cluster, then returns both as one digest:

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: Workflow
metadata:
  name: pod-health
  namespace: muster
spec:
  description: >-
    Pod health digest for a management cluster. Answers "check the pods in
    <mc>" and "are any pods failing on <mc>?". Lists not-running pods and
    BackOff events in one pass. Stop when the result is empty: no not-running
    pods and no BackOff events means the cluster is healthy, so write a
    one-line "all pods healthy" summary and stop. If a pod is crash-looping,
    you may make one follow-up call to read its logs with tailLines 30.
  args:
    management_cluster:
      type: string
      required: true
      description: The full MCP server name, for example my-cluster-mcp-kubernetes.
  steps:
    - id: not_running
      tool: x_kubernetes_list
      args:
        management_cluster: "{{ .input.management_cluster }}"
        resourceType: pods
        allNamespaces: true
        fieldSelector: "status.phase!=Running"
        output: slim
        limit: 25
      output: true
    - id: backoff_events
      tool: x_kubernetes_list
      args:
        management_cluster: "{{ .input.management_cluster }}"
        resourceType: events
        allNamespaces: true
        fieldSelector: "reason=BackOff"
        fullOutput: true
        limit: 10
      output: true
      allowFailure: true
```

The sections below explain why each field is there.

## The fields that matter

### `spec.description` is the only text the agent sees

When an agent lists tools, the **only** workflow text it gets is `spec.description` (maximum 1000 characters). The step-level `description` fields are stored on the resource but never reach the agent, so a directive placed there does nothing. Put everything you want the agent to know in `spec.description`.

Three blocks belong in most descriptions:

- A **stop-when-healthy rule**: the explicit conditions that mean no follow-up is needed, plus a directive to write a one-line summary and stop. Without it, an agent treats a clean result as an invitation to keep exploring, and cost balloons.
- A **pinned follow-up rule**: the one extra call the agent may make (for example, reading logs with `tailLines: 30`), so it drills the right thing instead of improvising.
- An **event-noise hint**: which objects are relevant, so the agent ignores unrelated events.

### The description also controls discoverability

An agent finds a workflow through the `filter_tools` meta-tool, whose description filter is a **case-insensitive substring match** over `spec.description`. There's no stemming, ranking, or synonym matching. So the description must literally contain the terms an agent searches by.

A workflow described only as `"check the pods in <mc>"` is invisible to a search for `"pod health"`, because that phrase isn't a substring of the description, and the agent falls back to raw tools. Lead the description with **both** the topic keyword (`pod health`, `cluster health`, `failing pods`) **and** the natural question phrasing. The 1000-character budget is large enough for both.

### `args` define and validate the inputs

Each entry in `spec.args` is typed (`string`, `integer`, `boolean`, `number`, `object`, or `array`), can be `required`, and can carry a `default` and a `description`. Muster validates and defaults the inputs before the first step runs. A missing required argument fails execution immediately. Extra arguments that aren't in the schema are tolerated.

### `output: true` selects what the agent sees

Every step result is recorded. Later steps and the response projection can read it through `{{ .results.<id>.<field> }}`, with or without a flag. The per-step `output` flag controls one thing: whether the step's data lands in the document the agent receives. Without it, Muster emits only `{id, tool, status}` for the step and drops the data before the response. Set `output: true` on every step whose data the agent must read. The last step's result is merged into the top level even when you set no flag.

The step-level `output` boolean differs from the `output: slim` argument inside `args`. That argument is a tool's own response knob. In the earlier example, `not_running` sets both. `output: slim` trims the Kubernetes payload, and step-level `output: true` returns the trimmed result.

`store: true` is deprecated. It's the older name for `output: true` and still works. Muster logs a deprecation warning for each step that uses it. Referencing a step result no longer needs it, so prefer `output`. When a step sets neither, `output` wins if present, and `store` is the fallback. The warning fires on the create or validate path and on the CRD reconciler.

### Shape the response with `spec.output`

For the tightest response, declare a workflow-level `spec.output` projection. It's a templated map, rendered once after every step completes. It **replaces** the default `{execution_id, workflow, status, input, steps[], ...}` envelope with the shape you define. It reads `.input`, `.results`, and `.vars`. Every step result is available to it, no matter how you flag the step.

```yaml
spec:
  steps:
    - id: not_running
      tool: x_kubernetes_list
      args: { management_cluster: "{{ .input.management_cluster }}", resourceType: pods, fieldSelector: "status.phase!=Running", output: slim, limit: 25 }
    - id: backoff_events
      tool: x_kubernetes_list
      args: { management_cluster: "{{ .input.management_cluster }}", resourceType: events, fieldSelector: "reason=BackOff", fullOutput: true, limit: 10 }
      allowFailure: true
  output:
    not_running_pods: "{{ .results.not_running.items }}"
    backoff_count: "{{ len .results.backoff_events.items }}"
    cluster: "{{ .input.management_cluster }}"
```

The projection **preserves JSON types**. A leaf's type comes from the value it evaluates to, not from how the rendered text looks. A single bare reference like `{{ .results.not_running.items }}` keeps its real type, so an array stays an array. A `{{ len ... }}` leaf is a number. A leaf that mixes literal text with an action, such as `"cluster {{ .input.management_cluster }}"`, renders to a string. Values whose form matters survive without coercion, including leading zeros, versions, and IDs like `08` and `1.20`.

When `spec.output` is declared, the per-step `output` and `store` flags no longer affect the returned document. The projection defines it in full. Muster logs a one-line warning naming any flags it made inert. Drop those flags, or drop the projection. The projection is the strongest token lever a workflow has, since it returns a small, shaped payload instead of the full step envelope.

### `allowFailure: true` for legitimately optional steps

By default, a single step error fails the whole workflow and flips its result to an error, which sends the agent chasing the failure with expensive discovery calls. Set `allowFailure: true` on steps that may legitimately fail or return nothing. Examples are a resource type not every cluster uses, an optional backend such as the metrics server (`x_prometheus_*`), or a list that depends on RBAC that might be scoped differently. In the earlier example, the events list is marked optional so a cluster without recent crash-loop events still returns a clean digest.

A workflow can mix servers in one digest, for example correlating Kubernetes state with an `x_prometheus_query` step, so a single call returns both the failing pods and the matching metrics. Mark the metrics step `allowFailure: true` so a cluster without `mcp-prometheus` deployed still returns the Kubernetes half.

## Control flow

Beyond plain `tool` steps, a top-level step can be a loop or a concurrent group, and the workflow can declare cleanup. These need Muster 0.8.0 or later. A step sets **exactly one** of `tool`, `forEach`, or `parallel`. Setting none or more than one is rejected at apply time.

### `forEach` loops

`forEach` runs a flat body of sub-steps once per item of a list, sequentially. Use it instead of hand-copying the same step per element:

```yaml
- id: per_cluster
  forEach:
    items: "{{ .input.clusters }}"   # must resolve to an array
    as: cluster                       # the item is {{ .vars.cluster }}
    steps:
      - id: status
        tool: x_kubernetes_list
        args:
          management_cluster: "{{ .vars.cluster }}"
          resourceType: pods
          output: slim
          limit: 25
        output: true
```

- `items` must be a reference that resolves to an array. A scalar, or a string built from a richer template, is rejected at runtime.
- The current item is bound to `{{ .vars.<as> }}` (default `item`) and its zero-based index to `{{ .vars.<as>_index }}`.
- After the loop, `{{ .results.<subStepID> }}` holds the last iteration's result; every iteration stays addressable as `{{ .results.<subStepID>_<index> }}`, for example `status_0` and `status_1`.
- `allowFailure: true` on the `forEach` step tolerates a failing iteration.

A loop multiplies cost: the per-step budget caps below apply to **every** iteration, so a loop over a large list is the easiest way to blow the token budget.

### `parallel` groups

`parallel` runs its sub-steps concurrently and joins before the next top-level step, so total latency is the **max** over the group rather than the sum. It's the right tool for fanning out independent reads:

```yaml
- id: fan_out
  parallel:
    - id: nodes
      tool: x_kubernetes_list
      args: { management_cluster: "{{ .input.management_cluster }}", resourceType: nodes, output: slim }
      output: true
    - id: events
      tool: x_kubernetes_list
      args: { management_cluster: "{{ .input.management_cluster }}", resourceType: events, fullOutput: true, limit: 10 }
      output: true
```

- Each sub-step sees a snapshot of the results as they were **before** the group started, so siblings can't read each other's output. A sub-step that needs another sub-step's result must be a later top-level step.
- Sub-step results merge back into the workflow after the join, so later steps reference them normally; flag the ones you want in the response with `output: true`.
- Only latency is parallelized; response **size** is still the sum, so the per-step caps still apply.

### `onFailure` cleanup

A workflow-level `onFailure` block lists sub-steps that run best-effort when the workflow fails on a step that isn't marked `allowFailure`. Each handler can read `{{ .results.<id> }}` from any step that ran before the failure, so a rollback can reference what it must undo:

```yaml
spec:
  steps:
    - id: backup
      tool: postgres_backup
      output: true
    - id: migrate
      tool: postgres_migrate
  onFailure:
    - id: restore
      tool: postgres_restore
      args:
        backup_name: "{{ .results.backup.backup_name }}"
```

`onFailure` is workflow-level only. There's no per-step failure handler. For read-only health digests you seldom need it, and `allowFailure` already covers the case where a resource might not exist. It earns its place in imperative pipelines such as deploy, migrate, and rollback.

## Templating

Step arguments are Go templates resolved server-side per step. Rendering uses `missingkey=error`, so referencing an undefined key **fails the step** rather than rendering an empty string. Four roots are in scope:

- `{{ .input.<arg> }}`: a workflow argument. It's always `.input.<arg>`, never a bare `{{ .<arg> }}`. The bare form fails with a missing-key error.
- `{{ .results.<stepID>.<field> }}`: a field from any prior step, available regardless of that step's `output` flag. Nested map navigation and array indexing both work (`{{ (index .results.list.items 0).name }}`).
- `{{ .vars.<name> }}`: a `forEach` loop variable: the loop item `{{ .vars.<as> }}` and its index `{{ .vars.<as>_index }}`. There's no other way to set `.vars`.
- `{{ .context.<x> }}`: another name for `.results`.

A template that's a **single bare access** (`{{ .input.port }}`) preserves the original type, so an integer stays an integer. Any richer template—string concatenation such as `"{{ .input.host }}:{{ .input.port }}"`, or one using a [sprig](https://masterminds.github.io/sprig/) function—renders to a string. Keep that in mind for tools that type-check their arguments. The full sprig function set is available.

## Conditions

A step can carry an optional `condition` that skips it (status `skipped`, not failed) when the condition is false. A condition selects its source with **exactly one** of `template`, `tool`, or `fromStep`.

The cheapest form is a boolean Go-template gate, evaluated in-process with no tool call. It's also the only way to express compound logic, since there are no `and`/`or` operators—write the boolean expression with sprig functions:

```yaml
- id: prod_only
  tool: x_security_run_checks
  args:
    management_cluster: "{{ .input.management_cluster }}"
  condition:
    template: '{{ eq .input.env "production" }}'
```

Alternatively, run a tool or reference a prior stored step and test the outcome. A `tool` or `fromStep` condition must declare `expect` or `expectNot`:

```yaml
- id: production_only
  tool: x_security_run_checks
  args:
    management_cluster: "{{ .input.management_cluster }}"
  condition:
    fromStep: detect_environment
    expect:
      jsonPath:
        "type": "production"
```

The `jsonPath` uses the same path navigator as step arguments and templates. It accepts two interchangeable forms. The first is a dotted or bracketed path over the result object, with array indexing. Paths like `data.field`, `items[0].name`, and plain dotted paths all work. The second is a Go-template expression that exposes the condition result as `.result`, alongside the usual roots. An example is `"{{ (index .result.items 0).name }}"`. For the read-only health digests that agents call most, conditions are seldom needed. Prefer `allowFailure` for the case where a resource might not exist.

## Budget for cost

Total response size is the **sum** over everything the workflow runs, including each `forEach` iteration and every `parallel` sub-step. An unbounded step is what eventually produces a multi-million-token outlier even when the typical run is small. Latency is the sum for sequential steps but the max within a `parallel` group. Cap every list, get, and log step:

- Set `limit:` on every list. Ten events is plenty; more just feeds noise.
- Set `tailLines: 30` on any log fetch. The default is 100 and the maximum is 1000—enough to blow the prompt window on a healthy system.
- Set `output: slim` on lists to strip verbose fields.

## Know the `mcp-kubernetes` output knobs

These bite every workflow that reads Kubernetes:

- `output:` and `fullOutput:` are independent. `output:` strips verbose fields; `fullOutput:` switches off the per-kind summary. For **events** you must set `fullOutput: true`, otherwise `reason`, `message`, `type`, and `count` are dropped.
- On older `mcp-kubernetes` (before `v0.1.86`), `output:` and `fullOutput:` are **list-only**. A single `output:` on a get-style call there flips the whole workflow to an error. From `v0.1.86` onward, `output:` is accepted on read tools too.
- `fieldSelector: reason=BackOff` on events is the **authoritative** crash-loop signal. Filtering on `status.phase!=Running` misses it, and a summary view reports crash-loopers as `Running`. Never gate pod health on phase or summary alone.

## What the engine doesn't support

These look plausible but are rejected at apply time or ignored. Avoid them:

| Looks plausible | Reality |
|---|---|
| `{{ .<arg> }}` | Always `{{ .input.<arg> }}`; the bare form fails. |
| `outputs:` on a step | Removed from the schema; use the `output` flag, or `spec.output` to shape the response. |
| `spec.name`, custom annotations to steer the agent | Not part of the schema; pruned or ignored. |
| Directives on a step's `description` | Never reach the agent; move them to `spec.description`. |
| `and`/`or` in a condition | One source per condition; compose logic in a `template`. |
| `forEach` or `parallel` nested inside a sub-step | Sub-steps are plain tool calls only; control flow doesn't nest. |
| `parallel` siblings reading each other's results | Each sibling sees a pre-group snapshot; sequence them as top-level steps instead. |
| Per-step `onFailure` | `onFailure` is workflow-level only. |

## Apply and iterate

Iterate live, then promote to your GitOps pipeline:

1. Apply the resource directly while you're shaping it. Muster's reconciler reloads it within seconds, with no restart of the agent or the consuming app:

   ```bash
   kubectl apply -f pod-health.yaml
   ```

2. Confirm it's valid and see the tools it references:

   ```bash
   kubectl get workflow pod-health -o yaml
   ```

   The `status.valid` field and any `status.validationErrors` tell you whether the spec passed structural validation.

3. Verify the **raw** workflow output over a direct Muster session before spending agent tokens. Because agent runs vary, run a scenario several times and compare.
4. Once the YAML is validated, fold it into the GitOps repository that manages your clusters so it ships the same way as the rest of your platform configuration.

## Related

- [Muster resource reference]({{< relref "/reference/muster" >}}): the complete field-by-field schema for the `Workflow` resource.
- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): the servers whose tools your workflow steps call.
- [Meta-tools and discovery]({{< relref "/overview/ai-agents/meta-tools" >}}): how an agent finds and invokes a `workflow_<name>` tool.
- [Troubleshooting]({{< relref "/tutorials/ai-agents/troubleshooting" >}}): when a workflow runs but the agent never picks it.
