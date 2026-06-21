---
linkTitle: start
title: "'muster start' command reference"
description: Reference for the 'muster start' command, which starts a Muster service or runs a workflow.
weight: 100
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I start a Muster service?
  - How do I run a Muster workflow from the command line?
last_review_date: 2026-06-21
---

`muster start` starts a service or runs a workflow. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster start <resource-type> <name> [parameters]
```

## Resource types {#types}

| Type | Description |
|---|---|
| `service` | Start a service by name |
| `workflow` | Run a workflow, with optional parameters as flags |

Workflow parameters are passed as `--key=value` flags and validated against the workflow's [argument schema]({{< relref "/reference/muster/crds" >}}#workflow).

## Flags {#flags}

`start` accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags). For workflows, additional `--key=value` flags supply the workflow arguments.

## Examples {#examples}

```nohighlight
muster start service prometheus
muster start workflow deploy-app --environment=production --replicas=3
```

## Related

- [`muster stop`]({{< relref "/reference/muster/cli/stop" >}}) - Stop a running service.
- [`muster call`]({{< relref "/reference/muster/cli/call" >}}) - Run a workflow as a `workflow_<name>` tool.
- [Author a Muster workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}) - Write workflows.
