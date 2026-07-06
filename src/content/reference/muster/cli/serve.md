---
linkTitle: serve
title: "'muster serve' command reference"
diataxis_content_type: reference
description: Reference for the 'muster serve' command, which starts the Muster aggregator server that AI agents and other Muster commands connect to.
weight: 10
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I start the Muster aggregator server?
  - How do I enable OAuth protection for Muster?
last_review_date: 2026-06-21
---

`muster serve` starts the aggregator server. It connects the configured MCP servers, exposes their tools behind one unified MCP endpoint, and keeps that endpoint available for IDEs, the developer portal chat, and the other `muster` commands.

## Usage

```nohighlight
muster serve [flags]
```

With no flags, Muster loads its configuration from `~/.config/muster`, starts the MCP servers and services marked for autostart, and prints a summary with the connection details.

To connect an IDE that can't reach the endpoint directly, bridge it with [`muster agent --mcp-server`]({{< relref "/reference/muster/cli/agent" >}}). IDEs that support remote, OAuth-protected MCP connect straight to the aggregator URL instead.

## Flags {#flags}

| Name | Description |
|---|---|
| `--config-path` | Configuration directory. Defaults to `~/.config/muster` |
| `--debug` | Enable general debug logging |
| `--silent` | Disable console log output. Does not silence OTLP export |
| `--yolo` | Disable the denylist for destructive tool calls. Use with caution |
| `--enable-events` | Enable Kubernetes event emission (alpha) |
| `--extra-ca-file` | PEM file whose certificates are appended to the system trust pool at startup |

### OAuth protection {#oauth}

These flags turn Muster into an OAuth 2.1 protected resource and enable the MCP client proxy for authenticating to remote MCP servers. Full setup needs a configuration file. See [Set up OAuth for Muster]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}).

| Name | Description |
|---|---|
| `--oauth-server` | Enable OAuth 2.1 protection for the Muster server |
| `--oauth-server-base-url` | Base URL of the Muster server for OAuth, for example `https://muster.<management-cluster>.<base-domain>` |
| `--oauth-mcp-client` | Enable the OAuth MCP client proxy for remote MCP server authentication |
| `--oauth-mcp-client-public-url` | Publicly accessible URL of the Muster server for OAuth callbacks |
| `--oauth-mcp-client-id` | OAuth client identifier. Auto-derived from the public URL when empty |

## Related

- [`muster standalone`]({{< relref "/reference/muster/cli/standalone" >}}) - Run the aggregator and agent in one process.
- [`muster agent`]({{< relref "/reference/muster/cli/agent" >}}) - Connect to a running aggregator.
- [Muster architecture]({{< relref "/overview/ai-agents/architecture" >}}) - How the aggregator works.
