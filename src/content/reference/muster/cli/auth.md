---
linkTitle: auth
title: "'muster auth' command reference"
description: Reference for the 'muster auth' command, which authenticates the Muster CLI to a remote OAuth-protected aggregator.
weight: 50
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I log in to a remote Muster?
  - How do I check my Muster authentication status?
  - How do I log out of Muster?
last_review_date: 2026-06-21
---

`muster auth` manages authentication to a remote, OAuth-protected aggregator. Use it to log in, check your current identity and token status, and log out. For how OAuth works in Muster, see the [security overview]({{< relref "/overview/ai-agents/security" >}}).

## Usage

```nohighlight
muster auth <subcommand> [flags]
```

## Subcommands {#subcommands}

| Subcommand | Description |
|---|---|
| `login` | Authenticate to a Muster aggregator using OAuth |
| `status` | Show authentication status |
| `whoami` | Show the current authenticated identity |
| `logout` | Clear stored authentication tokens |

## Flags {#flags}

These flags apply to every `auth` subcommand:

| Name | Description |
|---|---|
| `--endpoint` | Endpoint URL to authenticate to |
| `--context` | Use a named context. Reads `MUSTER_CONTEXT` when unset |
| `--config-path` | Configuration directory. Defaults to `~/.config/muster` |
| `--quiet`, `-q` | Suppress non-essential output |

### `login` flags {#login-flags}

| Name | Description |
|---|---|
| `--all` | Log in to the aggregator and every pending MCP server behind it |
| `--server` | Name of an aggregator-managed MCP server to authenticate to |
| `--silent` | Attempt silent re-auth using OIDC `prompt=none`. Needs IdP support, not available with Dex |

### `logout` flags {#logout-flags}

| Name | Description |
|---|---|
| `--all` | Clear all stored tokens |
| `--yes`, `-y` | Skip the confirmation prompt for `--all` |
| `--server`, `-s` | Name of an MCP server to disconnect |

## Examples {#examples}

Log in to a remote aggregator and to every MCP server that still needs authentication:

```nohighlight
muster auth login \
  --endpoint https://muster.<management-cluster>.<base-domain>/mcp --all
```

Authenticate to one downstream MCP server after the aggregator is connected:

```nohighlight
muster auth login --server kubernetes
```

## Related

- [Access control]({{< relref "/tutorials/ai-agents/access-control" >}}) - How identity maps to cluster permissions.
- [`muster context`]({{< relref "/reference/muster/cli/context" >}}) - Manage the endpoints you authenticate to.
