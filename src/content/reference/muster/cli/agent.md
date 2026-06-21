---
linkTitle: agent
title: "'muster agent' command reference"
description: Reference for the 'muster agent' command, which connects to the Muster aggregator as a client or bridges it to a stdio-only IDE.
weight: 30
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I connect my IDE to Muster?
  - What does 'muster agent --mcp-server' do?
  - How do I explore Muster tools interactively?
last_review_date: 2026-06-21
---

`muster agent` connects to a running aggregator as an MCP client. Modern IDEs and the developer portal chat connect to the aggregator URL directly over remote, OAuth-protected MCP, so `muster agent` is an optional local bridge. Use it for clients that can only speak stdio, or to explore tools by hand.

The aggregator must be running first. Start it with [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}).

## Usage

```nohighlight
muster agent [flags]
```

The command runs in one of three modes:

- **Normal** (default): connects, lists tools, and waits for tool-update notifications.
- **REPL** (`--repl`): an interactive prompt to list and run tools, resources, and prompts.
- **MCP server** (`--mcp-server`): runs an MCP server over stdio that an IDE configures as its MCP endpoint. This is the local-bridge mode for stdio-only clients.

## Flags {#flags}

| Name | Description |
|---|---|
| `--endpoint` | Aggregator MCP endpoint URL. Reads the configured context when unset |
| `--context` | Use a named context. Reads `MUSTER_CONTEXT` when unset |
| `--transport` | Transport for the connection: `streamable-http` (default) or `sse` |
| `--repl` | Start the interactive prompt |
| `--mcp-server` | Run as an MCP server over stdio, for stdio-only IDEs |
| `--timeout` | How long to wait for notifications. Defaults to `5m` |
| `--auth` | Authentication mode: `auto` (default), `prompt`, or `none`. Reads `MUSTER_AUTH_MODE` when unset |
| `--disable-auto-sso` | Don't authenticate to remote MCP servers automatically after Muster auth |
| `--silent` | Attempt silent re-auth using OIDC `prompt=none`. Needs IdP support, not available with Dex |
| `--verbose` | Enable verbose logging, including keepalive messages |
| `--json-rpc` | Log full JSON-RPC messages |
| `--no-color` | Disable colored output |
| `--config-path` | Configuration directory. Defaults to `~/.config/muster` |

## Related

- [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) - Connect an IDE to Muster.
- [`muster serve`]({{< relref "/reference/muster/cli/serve" >}}) - Start the aggregator.
- [`muster auth`]({{< relref "/reference/muster/cli/auth" >}}) - Authenticate to a remote aggregator.
