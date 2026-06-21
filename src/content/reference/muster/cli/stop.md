---
linkTitle: stop
title: "'muster stop' command reference"
description: Reference for the 'muster stop' command, which stops a running Muster service.
weight: 110
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I stop a Muster service?
last_review_date: 2026-06-21
---

`muster stop` stops a running service. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster stop service <name>
```

## Resource types {#types}

| Type | Description |
|---|---|
| `service` | Stop a service by name |

## Flags {#flags}

`stop` accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster stop service prometheus
```

## Related

- [`muster start`]({{< relref "/reference/muster/cli/start" >}}) - Start a service or run a workflow.
