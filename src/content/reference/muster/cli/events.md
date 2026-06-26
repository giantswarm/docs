---
linkTitle: events
title: "'muster events' command reference"
diataxis_content_type: reference
description: Reference for the 'muster events' command, which lists and filters events for Muster resources.
weight: 130
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I see events for Muster resources?
  - How do I follow Muster events live?
last_review_date: 2026-06-21
---

`muster events` lists and filters events for Muster resources, in both Kubernetes and filesystem modes. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster events [flags]
```

## Flags {#flags}

| Name | Description |
|---|---|
| `--resource-type` | Filter by resource type: `mcpserver` or `workflow` |
| `--resource-name` | Filter by resource name |
| `--namespace` | Filter by namespace |
| `--type` | Filter by event type: `Normal` or `Warning` |
| `--since` | Show events after this time, for example `1h`, `30m`, or an absolute timestamp |
| `--until` | Show events before this time |
| `--limit` | Maximum number of events. Defaults to `50` |
| `--follow`, `-f` | Stream new events as they occur |

`events` also accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster events
muster events --resource-type mcpserver
muster events --type Warning --since 1h
```

## Related

- [`muster check`]({{< relref "/reference/muster/cli/check" >}}) - Check that a resource is available.
- [Troubleshooting]({{< relref "/tutorials/ai-agents/troubleshooting" >}}) - Diagnose connection problems.
