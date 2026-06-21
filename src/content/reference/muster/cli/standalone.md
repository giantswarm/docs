---
linkTitle: standalone
title: "'muster standalone' command reference"
description: Reference for the 'muster standalone' command, which runs the Muster aggregator and the agent together in a single process.
weight: 20
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I run Muster as a single-process MCP server?
  - What does 'muster standalone' do?
last_review_date: 2026-06-21
---

`muster standalone` starts the aggregator server and the agent in one process. It's the simplest way to expose Muster to a stdio-only client without running [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}) and [`muster agent`]({{< relref "/reference/muster/cli/agent" >}}) separately.

## Usage

```nohighlight
muster standalone [flags]
```

## Flags {#flags}

Standalone accepts the flags of both [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}) and [`muster agent`]({{< relref "/reference/muster/cli/agent" >}}). The `--silent` flag defaults to `true` here, so the aggregator's console logging doesn't interfere with the stdio MCP stream.

## Related

- [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}) - Start the aggregator on its own.
- [`muster agent`]({{< relref "/reference/muster/cli/agent" >}}) - Connect to a running aggregator.
