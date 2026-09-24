---
linkTitle: CLI commands
title: Muster CLI command reference
description: Per-command reference for the Muster command-line interface, covering the aggregator server, the agent bridge, authentication, and resource management.
weight: 10
layout: single
menu:
  principal:
    identifier: agent-platform-reference-muster-cli
    parent: agent-platform-reference-muster
last_review_date: 2026-06-21
user_questions:
  - Which commands does the Muster CLI offer?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
aliases:
  - /reference/muster/cli/
---

The `muster` binary groups its commands into a few areas: running the aggregator, connecting to it, authenticating, and managing resources. Each command has its own page below.

## Server and bridge {#server}

| Command | Description |
|---|---|
| [`serve`]({{< relref "/agent-platform/reference/muster/cli/serve" >}}) | Start the aggregator server that other commands and IDEs connect to |
| [`standalone`]({{< relref "/agent-platform/reference/muster/cli/standalone" >}}) | Run the aggregator and agent together in a single process |
| [`agent`]({{< relref "/agent-platform/reference/muster/cli/agent" >}}) | Connect to the aggregator as a client, or bridge it to a stdio-only IDE |

## Connection and authentication {#connection}

| Command | Description |
|---|---|
| [`context`]({{< relref "/agent-platform/reference/muster/cli/context" >}}) | Manage named contexts, each pointing at a Muster endpoint |
| [`auth`]({{< relref "/agent-platform/reference/muster/cli/auth" >}}) | Log in to, inspect, and log out of a remote aggregator |

## Resources {#resources}

| Command | Description |
|---|---|
| [`list`]({{< relref "/agent-platform/reference/muster/cli/list" >}}) | List services, MCP servers, workflows, executions, tools, resources, or prompts |
| [`get`]({{< relref "/agent-platform/reference/muster/cli/get" >}}) | Get details for a single resource |
| [`create`]({{< relref "/agent-platform/reference/muster/cli/create" >}}) | Create a `Workflow` or `MCPServer` definition |
| [`call`]({{< relref "/agent-platform/reference/muster/cli/call" >}}) | Call any MCP tool by name |
| [`start`]({{< relref "/agent-platform/reference/muster/cli/start" >}}) | Start a service or run a workflow |
| [`stop`]({{< relref "/agent-platform/reference/muster/cli/stop" >}}) | Stop a running service |
| [`check`]({{< relref "/agent-platform/reference/muster/cli/check" >}}) | Check that an MCP server or workflow is available |
| [`events`]({{< relref "/agent-platform/reference/muster/cli/events" >}}) | List and filter resource events |

## Utility {#utility}

| Command | Description |
|---|---|
| [`version`]({{< relref "/agent-platform/reference/muster/cli/version" >}}) | Print the CLI version and, if reachable, the server version |
| [`self-update`]({{< relref "/agent-platform/reference/muster/cli/self-update" >}}) | Update the CLI to the latest GitHub release |

The flags shared by the resource commands are documented under [common flags]({{< relref "/agent-platform/reference/muster" >}}#common-flags).
