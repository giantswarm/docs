---
linkTitle: version
title: "'muster version' command reference"
diataxis_content_type: reference
description: Reference for the 'muster version' command, which prints the Muster CLI and server version.
weight: 140
menu:
  principal:
    identifier: agent-platform-reference-muster-cli-version
    parent: agent-platform-reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I check which version of Muster I'm running?
last_review_date: 2026-06-21
aliases:
  - /reference/muster/cli/version/
---

`muster version` prints the CLI version. When the aggregator server is reachable, it also prints the server version.

## Usage

```nohighlight
muster version
```

## Related

- [`muster self-update`]({{< relref "/agent-platform/reference/muster/cli/self-update" >}}) - Update the CLI to the latest release.
