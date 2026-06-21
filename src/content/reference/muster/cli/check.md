---
linkTitle: check
title: "'muster check' command reference"
description: Reference for the 'muster check' command, which checks whether a Muster MCP server or workflow is available.
weight: 120
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I check that a Muster workflow is available?
  - How do I check an MCP server's status?
last_review_date: 2026-06-21
---

`muster check` reports whether a resource is available and properly configured. For a workflow, "available" means every tool the workflow references is present in your session. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster check <resource-type> <name>
```

## Resource types {#types}

| Type | Description |
|---|---|
| `mcpserver` | Check an MCP server's status |
| `workflow` | Check that a workflow is available, with all required tools present |

## Flags {#flags}

`check` accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster check mcpserver prometheus
muster check workflow my-deployment
```

## Related

- [`muster list`]({{< relref "/reference/muster/cli/list" >}}) - List resources.
- [Troubleshooting]({{< relref "/tutorials/ai-agents/troubleshooting" >}}) - When a workflow's tools are missing.
