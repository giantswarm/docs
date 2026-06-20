---
title: Meta-tools and tool discovery
linkTitle: Meta-tools
description: The small set of meta-tools Muster exposes to AI agents, how lazy discovery keeps the context window lean, and the prefixes that group external, core, and workflow tools.
weight: 30
menu:
  principal:
    parent: overview-ai-agents
    identifier: overview-ai-agents-meta-tools
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - What are Muster's meta-tools?
  - How does Muster keep my AI agent's context small?
  - What do the x_, core_, and workflow_ tool prefixes mean?
---

A single management cluster can expose hundreds of MCP tools—one per Kubernetes operation, per cluster, plus everything from any other server behind the gateway. Loading them all into an AI assistant's context window at startup is wasteful. It pollutes the context and inflates the token cost of every interaction, most of it for tools the assistant never uses.

Muster avoids this with **meta-tool indirection**. Instead of exposing every underlying tool, it exposes a small, fixed set of meta-tools. The assistant uses these to discover and invoke the full set of capabilities on demand.

## The meta-tool surface

Muster exposes 11 meta-tools:

| Meta-tool | Purpose |
|---|---|
| `list_tools` | Discover all available tools |
| `filter_tools` | Discover tools cheaply: filter by name, description, or labels, rank by a natural-language query, and get a bounded, summarized page |
| `describe_tool` | Get the authoritative full description and schema for a specific tool |
| `call_tool` | Execute any tool by name |
| `list_core_tools` | List Muster's built-in tools only |
| `list_resources` / `get_resource` / `describe_resource` | Access MCP resources |
| `list_prompts` / `get_prompt` / `describe_prompt` | Access MCP prompts |

The assistant sees only these meta-tools in its MCP configuration—not the 100+ underlying tools. It discovers what it needs via `list_tools` or `filter_tools`, inspects a candidate with `describe_tool`, and runs it with `call_tool`. Because the configuration never names individual tools, adding or removing a downstream MCP server changes what `list_tools` returns without any change to the assistant's setup.

## Discovering tools with `filter_tools`

`filter_tools` is the cheap, scalable way to find tools across a large catalog. It returns a bounded page of one-line summaries instead of every full description and schema. The agent spends context only on plausible candidates, then calls `describe_tool` for the authoritative detail of the one it picks.

It accepts several ways to narrow the catalog, which you can combine:

- **`pattern`**: glob match against tool names (supports `*`). Case-insensitive unless you set `case_sensitive: true`.
- **`description_filter`**: case-insensitive substring match against tool descriptions.
- **`query`**: a natural-language query. When set, matching tools are relevance-ranked with Okapi BM25 over each tool's name and summary, returned best-first with a `score`, and non-matching tools are dropped.
- **`labels`**: a facet of `key=value` pairs. A tool must carry every requested label to match, for example `{"category": "observability"}`. Labels come from a workflow's `metadata.labels` and are propagated onto its `workflow_<name>` tool.

The response is a bounded summary page:

- **`limit`**: maximum tools returned in this page. Defaults to **5**. Raise it to page through more matches.
- **`offset`**: number of matching tools to skip before this page. Defaults to `0`.
- **`total`**: the number of tools matching the filters across the whole catalog.
- **`truncated`**: `true` when more matches exist beyond the current page, the signal to page further or refine the query.
- **`summary`**: a one-line, length-capped excerpt returned per tool instead of the full description.
- **`include_schema`**: defaults to `false`. When `true`, each entry carries its full description and input schema instead of the one-line summary, which costs much more context.

`describe_tool` stays the authoritative source for a tool's full description and input schema. Use `filter_tools` to shortlist, then `describe_tool` on the chosen tool before you call it.

## Tool naming

Every tool reachable through `call_tool` falls into one of three families, distinguished by prefix:

- **`x_<server>_<tool>`**: a tool from an external MCP server, prefixed with the server name to avoid conflicts. For example `x_kubernetes_get_pods` or `x_prometheus_query`.
- **`core_<area>_<tool>`**: one of Muster's built-in tools, such as service and workflow management (`core_service_*`, `core_workflow_*`).
- **`workflow_<name>`**: a dynamically generated tool for a [workflow]({{< relref "/overview/ai-agents/architecture" >}}#workflows-cut-agent-token-cost). Authoring a workflow registers a matching `workflow_<name>` tool that the agent can discover and call like any other.

## Lazy discovery keeps context lean

Several mechanisms work together so that an agent pays context cost only for the tools it actually uses:

- **Filter-based discovery.** Rather than parsing every tool definition, an agent narrows the list with `filter_tools` by name pattern, labels, or a ranked natural-language `query`, and gets back a short page of summaries. It pulls full schemas only for the candidate it chooses, via `describe_tool`.
- **AutoStart control.** A downstream MCP server can be defined but not started until it's needed. Muster won't spin up the process or load its tool definitions for a server that isn't relevant to the current task.
- **Dynamic registration.** When a server starts—manually, or as part of a workflow—its tools are discovered, prefixed, and registered immediately. The agent's next `list_tools` call reflects the new capabilities, no IDE restart required.
- **Prerequisite encapsulation.** Complex setups such as port forwarding or authentication are encapsulated so that the relevant tools only become available once their prerequisites are satisfied.

The combined effect: an assistant interacting with Muster carries a tiny, stable tool surface. The cost of any given task scales with what that task touches—not with the size of the whole platform.

To see these meta-tools in action from your IDE, follow [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
