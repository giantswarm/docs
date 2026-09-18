---
linkTitle: check
title: "'muster check' command reference"
diataxis_content_type: reference
description: Reference for the 'muster check' command, which checks whether a Muster MCP server or workflow is available.
weight: 120
menu:
  principal:
    identifier: agent-platform-reference-muster-cli-check
    parent: agent-platform-reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I check that a Muster workflow is available?
  - How do I check an MCP server's status?
last_review_date: 2026-06-21
aliases:
  - /reference/muster/cli/check/
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

`check` accepts the [common flags]({{< relref "/agent-platform/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster check mcpserver prometheus
muster check workflow my-deployment
```

## Related

- [`muster list`]({{< relref "/agent-platform/reference/muster/cli/list" >}}) - List resources.
- [Troubleshooting]({{< relref "/agent-platform/tutorials/troubleshooting" >}}) - When a workflow's tools are missing.
