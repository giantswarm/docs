---
linkTitle: get
title: "'muster get' command reference"
diataxis_content_type: reference
description: Reference for the 'muster get' command, which retrieves details about a single Muster resource.
weight: 70
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I inspect a single Muster resource?
  - How do I see a workflow execution's result?
last_review_date: 2026-06-21
---

`muster get` retrieves details about one resource. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster get <type> <name|uri|id> [flags]
```

## Resource types {#types}

| Type | Identified by | Description |
|---|---|---|
| `service` | name | Detailed status of a service |
| `mcpserver` | name | MCP server details and configuration |
| `workflow` | name | Workflow definition and details |
| `workflow-execution` | execution ID | Workflow execution details and results |
| `tool` | name | MCP tool details, including its input schema |
| `resource` | URI | MCP resource metadata |
| `prompt` | name | MCP prompt details, including its arguments |

## Flags {#flags}

`get` accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags). Use `--output yaml` or `--output json` to inspect the full resource.

## Examples {#examples}

```nohighlight
muster get service prometheus
muster get workflow auth-flow
muster get workflow-execution abc123-def456-789
muster get mcpserver kubernetes --output yaml
muster get tool core_service_list
```

## Related

- [`muster list`]({{< relref "/reference/muster/cli/list" >}}) - List resources.
- [Custom resources]({{< relref "/reference/muster/crds" >}}) - The `MCPServer` and `Workflow` schemas.
