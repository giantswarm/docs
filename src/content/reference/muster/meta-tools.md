---
linkTitle: Meta-tools
title: Muster meta-tools reference
diataxis_content_type: reference
description: Reference for the meta-tools Muster exposes to AI agents, the filter_tools discovery arguments and response shape, and the catalog of built-in tools.
weight: 20
menu:
  principal:
    parent: reference-muster
    identifier: reference-muster-meta-tools
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - What meta-tools does Muster expose?
  - What arguments does filter_tools take?
  - Which built-in core tools does Muster provide?
last_review_date: 2026-06-21
---

Muster exposes a small, fixed set of meta-tools to an AI agent instead of the hundreds of underlying tools behind the gateway. The agent discovers what it needs on demand and pays context cost only for the tools it uses. For the concept and the reasoning, see [Meta-tools and tool discovery]({{< relref "/overview/ai-agents/meta-tools" >}}). This page is the field-level reference, verified against Muster `v0.10.0`.

## The meta-tools {#meta-tools}

Muster exposes 11 meta-tools:

| Meta-tool | Purpose |
|---|---|
| `list_tools` | List all available tools from connected MCP servers |
| `filter_tools` | Discover tools cheaply, with a bounded, summarized page |
| `describe_tool` | Get the full description and input schema for one tool |
| `call_tool` | Execute a tool by name with the given arguments |
| `list_core_tools` | List Muster's built-in tools only |
| `list_resources` | List all available MCP resources |
| `describe_resource` | Get details about one MCP resource |
| `get_resource` | Retrieve a resource's contents |
| `list_prompts` | List all available MCP prompts |
| `describe_prompt` | Get details about one MCP prompt |
| `get_prompt` | Get a prompt with the given arguments |

The agent sees only these meta-tools in its MCP configuration. It shortlists candidates with `filter_tools`, inspects the chosen one with `describe_tool`, and runs it with `call_tool`.

## Discovering tools with `filter_tools` {#filter-tools}

`filter_tools` is the discovery tier. It returns a bounded page of one-line summaries rather than every full description and schema, so the agent spends context only on plausible candidates.

### Arguments {#filter-tools-args}

| Argument | Type | Default | Description |
|---|---|---|---|
| `pattern` | string | | Glob match against tool names. Supports `*`. Case-insensitive unless `case_sensitive` is set |
| `description_filter` | string | | Case-insensitive substring match against tool descriptions |
| `query` | string | | Natural-language query. When set, matches are relevance-ranked with Okapi BM25 over each tool's name and summary, returned best-first with a `score`, and non-matches are dropped |
| `labels` | object | | Label facets as `key=value` pairs. A tool must carry every requested label to match. Labels come from a workflow's `metadata.labels` |
| `case_sensitive` | boolean | `false` | Whether pattern matching is case-sensitive |
| `include_schema` | boolean | `false` | When `true`, each entry carries its full description and input schema instead of a one-line summary. This costs much more context |
| `limit` | number | `5` | Maximum tools returned in this page. Raise it to page through more matches |
| `offset` | number | `0` | Number of matching tools to skip before this page |

### Response {#filter-tools-response}

The response is a bounded summary page:

```json
{
  "filters": { "...": "the filter arguments applied" },
  "total": 12,
  "truncated": true,
  "tools": [
    {
      "name": "x_prometheus_query",
      "summary": "Run a PromQL query against a managed cluster.",
      "score": 4.21,
      "labels": { "category": "observability" }
    }
  ],
  "total_tools": 213,
  "filtered_count": 5
}
```

| Field | Description |
|---|---|
| `total` | Number of tools matching the filters across the whole catalog |
| `truncated` | `true` when more matches exist beyond this page, the signal to page further or refine the query |
| `tools` | The current page. Each entry has `name`, plus `summary` (or `description` when `include_schema` is set), `score` when ranked by a query, `labels` when present, and `inputSchema` when `include_schema` is `true` |
| `total_tools` | The size of the full catalog. Retained for backward compatibility |
| `filtered_count` | The current page size, equal to `len(tools)`. Deprecated: prefer `total` for the match count |

`describe_tool` stays the authoritative source for a tool's full description and input schema. Use `filter_tools` to shortlist, then `describe_tool` on the chosen tool before you call it.

## Tool naming {#naming}

Every tool reachable through `call_tool` falls into one of three families, distinguished by prefix:

- **`x_<server>_<tool>`**: a tool from an external MCP server, prefixed with the server name to avoid conflicts, for example `x_kubernetes_get_pods`.
- **`core_<area>_<tool>`**: one of Muster's built-in tools.
- **`workflow_<name>`**: a tool generated from a [`Workflow`]({{< relref "/reference/muster/crds" >}}#workflow) resource.

When an `MCPServer` declares a `family`, its tools are exposed under the family name (`<prefix>_<family>_<tool>`) with a required argument that selects which instance handles the call. See [`MCPServer`]({{< relref "/reference/muster/crds" >}}#mcpserver).

## Built-in tool catalog {#core-tools}

Muster's `core_*` tools manage the resources it owns. List them at runtime with `list_core_tools`, or `muster list tool --filter 'core_*'`. The catalog as of `v0.10.0`:

| Area | Tools |
|---|---|
| Authentication | `core_auth_login`, `core_auth_logout` |
| Configuration | `core_config_get` |
| MCP servers | `core_mcpserver_list`, `core_mcpserver_get`, `core_mcpserver_create`, `core_mcpserver_update`, `core_mcpserver_delete`, `core_mcpserver_validate` |
| Services | `core_service_list`, `core_service_status`, `core_service_start`, `core_service_stop`, `core_service_restart` |
| Workflows | `core_workflow_list`, `core_workflow_get`, `core_workflow_create`, `core_workflow_update`, `core_workflow_delete`, `core_workflow_validate`, `core_workflow_available`, `core_workflow_run`, `core_workflow_execution_list`, `core_workflow_execution_get` |
| Events | `core_events` |

## Related

- [Meta-tools and tool discovery]({{< relref "/overview/ai-agents/meta-tools" >}}) - The concept and the token-cost rationale.
- [Custom resources]({{< relref "/reference/muster/crds" >}}) - The `MCPServer` and `Workflow` schemas these tools manage.
- [`muster call`]({{< relref "/reference/muster/cli/call" >}}) - Call any of these tools from the CLI.
