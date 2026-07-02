---
linkTitle: Muster CLI
title: Muster CLI and resource reference
description: Reference for the Muster command-line interface, the meta-tools it exposes to AI agents, and the MCPServer and Workflow custom resources.
weight: 40
layout: single
menu:
  principal:
    identifier: reference-muster
    parent: reference
last_review_date: 2026-06-21
user_questions:
  - Which commands does the Muster CLI offer?
  - What meta-tools does Muster expose to AI agents?
  - What fields do the MCPServer and Workflow custom resources support?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
---

`muster` is the command-line interface for [Muster]({{< relref "/overview/ai-agents/introduction" >}}), the MCP gateway that gives AI agents unified, secure access to your fleet. This section documents the CLI commands, the meta-tools Muster exposes to agents, and the custom resources you author to extend it.

For a conceptual overview, start with [AI agents on the platform]({{< relref "/overview/ai-agents" >}}). To connect your IDE, follow [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).

## Reference pages {#pages}

| Page | Description |
|---|---|
| [Meta-tools]({{< relref "/reference/muster/meta-tools" >}}) | The meta-tools Muster exposes to agents, plus the `core_*` tool catalog |
| [Custom resources]({{< relref "/reference/muster/crds" >}}) | The `MCPServer` and `Workflow` schemas |

## CLI commands {#commands}

| Command | Description |
|---|---|
| [`serve`]({{< relref "/reference/muster/cli/serve" >}}) | Start the aggregator server |
| [`standalone`]({{< relref "/reference/muster/cli/standalone" >}}) | Run the aggregator and agent in one process |
| [`agent`]({{< relref "/reference/muster/cli/agent" >}}) | Connect to the aggregator as a client, or bridge it over stdio |
| [`context`]({{< relref "/reference/muster/cli/context" >}}) | Manage named endpoint contexts |
| [`auth`]({{< relref "/reference/muster/cli/auth" >}}) | Authenticate to a remote aggregator |
| [`list`]({{< relref "/reference/muster/cli/list" >}}) | List resources |
| [`get`]({{< relref "/reference/muster/cli/get" >}}) | Get details for one resource |
| [`create`]({{< relref "/reference/muster/cli/create" >}}) | Create a workflow or MCP server definition |
| [`call`]({{< relref "/reference/muster/cli/call" >}}) | Call an MCP tool by name |
| [`start`]({{< relref "/reference/muster/cli/start" >}}) | Start a service or run a workflow |
| [`stop`]({{< relref "/reference/muster/cli/stop" >}}) | Stop a service |
| [`check`]({{< relref "/reference/muster/cli/check" >}}) | Check that a resource is available |
| [`events`]({{< relref "/reference/muster/cli/events" >}}) | List resource events |
| [`version`]({{< relref "/reference/muster/cli/version" >}}) | Print CLI and server version |
| [`self-update`]({{< relref "/reference/muster/cli/self-update" >}}) | Update the CLI from GitHub |

## Common flags {#common-flags}

The client commands that talk to a running aggregator (`list`, `get`, `create`, `call`, `start`, `stop`, `check`, `events`) share these flags:

| Name | Description |
|---|---|
| `--output`, `-o` | Output format: `table` (default), `wide`, `json`, or `yaml` |
| `--no-headers` | Suppress the header row in table output |
| `--quiet`, `-q` | Suppress non-essential output |
| `--debug` | Enable debug logging, showing MCP protocol messages |
| `--config-path` | Configuration directory. Defaults to `~/.config/muster` |
| `--endpoint` | Remote aggregator endpoint URL. Reads `MUSTER_ENDPOINT` when unset |
| `--context` | Use a named context. Reads `MUSTER_CONTEXT` when unset |
| `--auth` | Authentication mode: `auto` (default), `prompt`, or `none`. Reads `MUSTER_AUTH_MODE` when unset |

Most of these commands need a running aggregator. Start one with [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}), or point `--endpoint` at a remote one.

## Configuration {#config}

Muster reads its configuration from `~/.config/muster` by default. Override the directory with `--config-path`:

```nohighlight
~/.config/muster/
├── config.yaml      # aggregator port, host, transport, namespace
├── mcpservers/      # MCPServer definitions
└── workflows/       # Workflow definitions
```

In Kubernetes mode, Muster reads `MCPServer` and `Workflow` custom resources from the cluster instead. See [Deploy Muster]({{< relref "/tutorials/ai-agents/self-hosting/deploy-muster" >}}).

## Contributing {#contributing}

See the [GitHub project](https://github.com/giantswarm/muster) for source code, issues, and pull requests.
