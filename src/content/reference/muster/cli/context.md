---
linkTitle: context
title: "'muster context' command reference"
description: Reference for the 'muster context' command, which manages named contexts that each point at a Muster endpoint.
weight: 40
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I switch between Muster endpoints?
  - How do I add a Muster context?
last_review_date: 2026-06-21
---

`muster context` manages named contexts. Each context points at a Muster endpoint, so you can switch between a local aggregator and one or more remote management clusters without retyping URLs. Running `muster context` with no subcommand lists the contexts.

## Usage

```nohighlight
muster context [subcommand]
```

## Subcommands {#subcommands}

| Subcommand | Aliases | Description |
|---|---|---|
| `list` | `ls` | List all configured contexts |
| `current` | | Show the name of the active context |
| `use <name>` | `switch` | Switch the active context |
| `add <name> --endpoint <url>` | | Add a new context |
| `update <name> --endpoint <url>` | `set` | Change an existing context's endpoint |
| `rename <old-name> <new-name>` | | Rename a context |
| `show <name>` | `describe`, `get` | Show details for one context |
| `delete <name>` | `rm`, `remove` | Delete a context |

## Flags {#flags}

| Subcommand | Name | Description |
|---|---|---|
| `add` | `--endpoint` | Endpoint URL for the context (required) |
| `add` | `--use` | Set as the active context after adding |
| `update` | `--endpoint` | New endpoint URL (required) |
| `show` | `--output`, `-o` | Output format: `text` (default), `json`, or `yaml` |
| `delete` | `--force`, `-f` | Skip the confirmation prompt |
| (all) | `--quiet`, `-q` | Suppress non-essential output |

## Examples {#examples}

Add a context for a remote management cluster and make it active:

```nohighlight
muster context add prod \
  --endpoint https://muster.<management-cluster>.<base-domain>/mcp --use
```

Switch back to a local aggregator:

```nohighlight
muster context use local
```

## Related

- [`muster auth`]({{< relref "/reference/muster/cli/auth" >}}) - Authenticate to the endpoint behind a context.
