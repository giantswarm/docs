---
linkTitle: create
title: "'muster create' command reference"
diataxis_content_type: reference
description: Reference for the 'muster create' command, which creates Muster Workflow and MCPServer definitions.
weight: 80
menu:
  principal:
    parent: reference-muster-cli
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I create an MCP server definition with the Muster CLI?
  - How do I create a Muster workflow from the command line?
last_review_date: 2026-06-21
---

`muster create` creates a resource definition. The aggregator must be running, or `--endpoint` must point at a remote one.

## Usage

```nohighlight
muster create <resource-type> <name> [flags]
```

## Resource types {#types}

| Type | Description |
|---|---|
| `workflow` | A `Workflow` definition |
| `mcpserver` | An `MCPServer` definition: `stdio`, `streamable-http`, or `sse` |

## Flags {#flags}

For `mcpserver`, these flags map to fields on the [`MCPServer`]({{< relref "/reference/muster/crds" >}}#mcpserver) resource:

| Name | Description |
|---|---|
| `--type` | Server type: `stdio`, `streamable-http`, or `sse` |
| `--command` | Executable for a `stdio` server |
| `--args` | Command-line arguments for a `stdio` server |
| `--url` | Endpoint URL for a `streamable-http` or `sse` server |
| `--tool-prefix` | Prefix prepended to the server's tool names |
| `--timeout` | Connection timeout in seconds. Defaults to `30` |
| `--autoStart` | Start the server automatically when Muster initializes |
| `--env` | Environment variable, as `KEY=VALUE`. Repeat for several |
| `--description` | Human-readable description |

`create` also accepts the [common flags]({{< relref "/reference/muster" >}}#common-flags).

## Examples {#examples}

```nohighlight
muster create mcpserver my-stdio-server \
  --type=stdio --command=npx --args="@modelcontextprotocol/server-git" --autoStart=true

muster create mcpserver my-http-server \
  --type=streamable-http --url=https://api.example.com/mcp --timeout=30

muster create workflow example-workflow
```

For the full set of `MCPServer` and `Workflow` fields, including authentication and control flow, see [custom resources]({{< relref "/reference/muster/crds" >}}). To author a workflow the code-grounded way, see [Author a Muster workflow]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}).

## Related

- [Managing MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) - The full `MCPServer` workflow.
- [Custom resources]({{< relref "/reference/muster/crds" >}}) - The resource schemas.
