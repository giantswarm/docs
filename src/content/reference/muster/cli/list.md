---
linkTitle: list
title: "'muster list' command reference"
diataxis_content_type: reference
description: Reference for the 'muster list' command, which lists Muster services, MCP servers, workflows, executions, and MCP primitives.
weight: 60
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I list Muster services and workflows?
  - How do I list the tools behind Muster?
last_review_date: 2026-06-21
---

`muster list` lists resources in the Muster environment. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster list <resource-type> [flags]
```

## Resource types {#types}

The trailing `(s)` means both singular and plural work, for example `service` or `services`.

| Type | Description |
|---|---|
| `service(s)` | All services with their status |
| `mcpserver(s)` | All MCP server definitions |
| `workflow(s)` | All workflow definitions |
| `workflow-execution(s)` | Workflow execution history |
| `tool(s)` | All MCP tools from the aggregated servers |
| `resource(s)` | All MCP resources from the aggregated servers |
| `prompt(s)` | All MCP prompts from the aggregated servers |

## Flags {#flags}

These flags filter the MCP primitives (`tool`, `resource`, `prompt`):

| Name | Description |
|---|---|
| `--filter` | Filter by name pattern. Wildcards `*` and `?` are supported |
| `--description` | Filter by description content, as a case-insensitive substring |
| `--server` | Filter by server-name prefix |

For `mcpserver`:

| Name | Description |
|---|---|
| `--all` | Show all servers, including unreachable ones |
| `--verbose` | Show detailed error information for failed or unreachable servers |

`list` also accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags), including `--output`.

## Examples {#examples}

```nohighlight
muster list mcpserver
muster list workflow
muster list tool --filter 'x_kubernetes_*'
```

## Related

- [`muster get`]({{< relref "/reference/muster/cli/get" >}}) - Get details for a single resource.
- [`muster check`]({{< relref "/reference/muster/cli/check" >}}) - Check that a resource is available.
