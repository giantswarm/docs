---
linkTitle: Installation
title: Installing the Muster CLI
diataxis_content_type: how-to-guide
description: How to install the muster command-line interface and keep it up to date.
weight: 5
menu:
  principal:
    parent: reference-muster
    identifier: reference-muster-installation
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-07-23
user_questions:
  - How do I install the Muster CLI?
  - Where can I download the muster binary?
  - How do I keep the Muster CLI up to date?
---

`muster` is a single, self-contained binary with no additional dependencies. This page explains how to install it and keep it current. For what the CLI does and which commands it offers, see the [Muster CLI reference]({{< relref "/reference/muster" >}}).

You only need the CLI for a terminal view of your fleet, the `auth` and `context` commands, or the local bridge (`muster agent`). Modern AI assistants connect to the Muster endpoint directly over HTTPS with nothing to install — see [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).

## Download the binary {#download}

Download the build for your operating system and architecture from the [latest Muster release](https://github.com/giantswarm/muster/releases/latest), then move the binary into a directory on your `PATH`.

On Linux or macOS, once you have unpacked the downloaded archive:

```bash
sudo mv muster /usr/local/bin/muster
chmod +x /usr/local/bin/muster
```

Verify that the CLI is working:

```bash
muster version
```

You should see the CLI version and, if a running aggregator is reachable, the server version.

## Keep it up to date {#update}

Update the installed CLI in place to the latest GitHub release:

```bash
muster self-update
```

See [`muster self-update`]({{< relref "/reference/muster/cli/self-update" >}}) for details.

## Next steps {#next-steps}

- [Point the CLI at your endpoint]({{< relref "/reference/muster/cli/context" >}}) with a named context.
- [Authenticate]({{< relref "/reference/muster/cli/auth" >}}) to a remote aggregator.
- [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) to connect your IDE.
