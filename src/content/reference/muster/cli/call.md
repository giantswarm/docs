---
linkTitle: call
title: "'muster call' command reference"
diataxis_content_type: reference
description: Reference for the 'muster call' command, which invokes any MCP tool behind the Muster aggregator by name.
weight: 90
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I call an MCP tool from the Muster CLI?
  - How do I run a Muster workflow tool by name?
last_review_date: 2026-06-21
---

`muster call` invokes any MCP tool by name, including the `core_*` tools, the `x_*` tools from aggregated servers, and the `workflow_*` tools. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster call <tool-name> [--arg=value ...]
```

Pass arguments as `--key=value` or `--key value` flags. To pass a structured argument, use `--json` with a JSON object instead.

## Flags {#flags}

| Name | Description |
|---|---|
| `--json` | Pass the tool arguments as a single JSON object |

Any other `--key=value` flag is forwarded to the tool as an argument. `call` also accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster call core_service_list
muster call core_service_status --name=prometheus
muster call workflow_deploy --environment=production --replicas=3
muster call core_mcpserver_list --output json
```

## Related

- [Meta-tools]({{< relref "/reference/muster/meta-tools" >}}) - The tool families and the `core_*` catalog.
- [`muster start`]({{< relref "/reference/muster/cli/start" >}}) - Run a workflow by name.
