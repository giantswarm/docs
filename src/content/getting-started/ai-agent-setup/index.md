---
linkTitle: Set up your AI agent
title: Set up your AI agent for Kubernetes operations
diataxis_content_type: how-to-guide
description: Learn how to use Muster and mcp-kubernetes to interact with your Giant Swarm management clusters through AI assistants like Claude Code, Cursor, or GitHub Copilot.
weight: 80
menu:
  principal:
    parent: getting-started
    identifier: getting-started-ai-agent-setup
last_review_date: 2026-07-23
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How do I use AI assistants with my Kubernetes clusters?
  - How do I set up Muster with Claude Code, Cursor, or VS Code?
  - What is mcp-kubernetes?
  - How do I authenticate with Muster?
---

The Giant Swarm platform is ready to be used by AI agents. Its integration lets you query Kubernetes resources across all your management clusters using plain language—directly from your IDE. Instead of switching between terminals and dashboards, you can ask your AI assistant things like "are there any pods in CrashLoopBackOff on any cluster?" and get answers grounded in live cluster state.

## How it works

Two components work together: **mcp-kubernetes** runs on each management cluster and exposes its Kubernetes resources through a secure, OAuth-protected [MCP](https://modelcontextprotocol.io/) API, and **Muster** is a central aggregator that connects all those instances into a single endpoint. You point your AI assistant at Muster and get unified access to every cluster at once.

Modern AI assistants—Claude Code, Cursor, and VS Code with GitHub Copilot—support remote, OAuth-protected MCP servers natively. You point your editor straight at the Muster endpoint over HTTPS, and it runs the SSO login itself—nothing to install or keep running locally. That direct connection is the recommended setup. For a client that can only speak stdio, or has no built-in OAuth flow, the `muster` CLI provides an optional local bridge (`muster agent`).

For the full picture—how the aggregator works, the supported deployment shapes, and how it stays secure—see the [Muster architecture]({{< relref "/overview/ai-agents/architecture" >}}) and [security]({{< relref "/overview/ai-agents/security" >}}) explanations. If you'd rather ask questions in the browser, the [developer portal AI chat]({{< relref "/overview/developer-portal/ai-chat" >}}) uses the same aggregator.

## Before you start

You'll need:

- Access to a Giant Swarm installation with mcp-kubernetes and Muster deployed. Ask your Giant Swarm account engineer for your Muster endpoint URL—it looks like `https://muster.<management-cluster>.<base-domain>/mcp`.
- Ensure `dex` is configured in your management clusters with a supported identity provider. Contact Giant Swarm support if not.
- An MCP-capable client: Claude Code, Cursor, or VS Code with the GitHub Copilot extension.

## Connect your editor directly

This is the recommended setup. Point your editor at the Muster endpoint your account engineer gave you—it looks like `https://muster.<management-cluster>.<base-domain>/mcp`. The first time the editor connects, it opens your browser for SSO login. After you authenticate, the full set of Kubernetes tools becomes available with no restart. Your editor refreshes tokens in the background, so you stay connected. See [AI agent security]({{< relref "/overview/ai-agents/security" >}}#agent-to-muster-authentication) for session duration and single sign-on.

### Claude Code

Register the endpoint as an HTTP MCP server:

```bash
claude mcp add --transport http muster https://muster.<management-cluster>.<base-domain>/mcp
```

Then run `/mcp` in your session to complete the browser OAuth login. Alternatively, commit a project-level `.mcp.json` so your team shares the configuration:

```json
{
  "mcpServers": {
    "muster": {
      "type": "http",
      "url": "https://muster.<management-cluster>.<base-domain>/mcp"
    }
  }
}
```

### Cursor

Create or edit `~/.cursor/mcp.json` (for global settings) or `.cursor/mcp.json` in your project directory, and add:

```json
{
  "mcpServers": {
    "muster": {
      "url": "https://muster.<management-cluster>.<base-domain>/mcp"
    }
  }
}
```

Make sure MCP is enabled in Cursor's settings. Cursor opens your browser to authenticate on first connect.

### VS Code (GitHub Copilot)

Create or edit `.vscode/mcp.json` in your workspace (or your user-level MCP settings) and add:

```json
{
  "servers": {
    "muster": {
      "type": "http",
      "url": "https://muster.<management-cluster>.<base-domain>/mcp"
    }
  }
}
```

VS Code opens your browser for SSO the first time Copilot connects. After authentication the Kubernetes tools become available—no restart needed.

## Verify and manage with the muster CLI (optional)

The direct connection above needs only your editor. Install the `muster` CLI when you want a terminal view of what you can reach, the `auth` and `context` commands, or the local bridge described below.

### Install the CLI

Download the `muster` binary and put it somewhere on your `PATH`. See [Installing the Muster CLI]({{< relref "/reference/muster/installation" >}}) for the full instructions.

### Point it at your endpoint

A context tells the CLI which aggregator endpoint to use. Add one with the endpoint URL your account engineer provided, then activate it:

```bash
muster context add my-platform --endpoint https://muster.<management-cluster>.<base-domain>/mcp
muster context use my-platform
```

### Check what you can reach

```bash
muster auth login
muster auth status
```

`muster auth status` shows the aggregator and each downstream server's state:

```text
Muster Aggregator
  Endpoint:  https://muster.<management-cluster>.<base-domain>/mcp
  Status:    Authenticated
  Expires:   in 18 minutes
  Session:   ~29 days remaining (auto-refresh)

MCP Servers
  cluster-a-mcp-kubernetes   Connected [SSO: Forwarded]
  cluster-b-mcp-kubernetes   Connected [SSO: Exchanged]
  cluster-c-mcp-kubernetes   Connected [SSO: Exchanged]
```

## Connect through the local bridge (fallback)

For an editor that can't connect to a remote, OAuth-protected MCP server directly, bridge it with `muster agent`. This needs the CLI installed and a context set, as above. The bridge uses the active context, so no endpoint flag is needed in the editor config.

### Claude Code through the bridge

```bash
claude mcp add muster -- muster agent --mcp-server
```

### Cursor through the bridge

```json
{
  "mcpServers": {
    "muster": {
      "command": "muster",
      "args": ["agent", "--mcp-server"]
    }
  }
}
```

Make sure MCP is enabled in Cursor's settings. After saving the configuration, you can toggle the MCP server off and on from Cursor's MCP settings panel to pick up the changes.

### VS Code through the bridge

```json
{
  "servers": {
    "muster": {
      "type": "stdio",
      "command": "muster",
      "args": ["agent", "--mcp-server"]
    }
  },
  "inputs": []
}
```

The first time your editor connects through the bridge, if you haven't authenticated yet, the agent exposes a single tool called `authenticate_muster`. Your assistant calls it automatically, which opens your browser for SSO login. After authentication succeeds, the full set of Kubernetes tools becomes available—no restart needed.

## Connect from other MCP tools

The Muster endpoint is a standard remote, OAuth-protected MCP server, so it works with any client that supports remote MCP and OAuth—not just code editors. Point the client at the same `https://muster.<management-cluster>.<base-domain>/mcp` URL and complete the browser SSO login.

- **Claude.ai (web) and Claude Desktop**: open Settings -> Connectors, add a custom connector with the endpoint URL, and complete the browser OAuth login. Custom connectors are available on Pro, Max, Team, and Enterprise plans; on Team and Enterprise an organization owner has to add the connector before members can use it.
- **ChatGPT**: in Connectors (developer mode, available on Business, Enterprise, and Pro), add the MCP server URL and authenticate. The tools then become available to the model.
- **Any other MCP client**: use the same endpoint URL. For a client that only speaks stdio or has no built-in OAuth flow, bridge it with [`muster agent`](#connect-through-the-local-bridge-fallback) or a generic stdio bridge such as [`mcp-remote`](https://github.com/geelen/mcp-remote).

## What you can ask

Once everything's configured, your AI assistant has live access to Kubernetes resources across all your management clusters. You interact with it through natural language.

**Cluster overview:**

- "List all pods in the monitoring namespace on cluster A."
- "What's the status of all deployments across all clusters?"
- "Are there any pods in CrashLoopBackOff on any cluster?"

**Troubleshooting:**

- "Show logs for the failing pod in the kube-system namespace on cluster B."
- "What events have occurred in the last hour on cluster C?"
- "Why is the ingress-controller pod restarting?"

**Resource inspection:**

- "List all services of type LoadBalancer across all clusters."
- "What are the resource requests and limits for pods in the default namespace?"
- "What Helm releases are installed on cluster A?"

You don't need to know any tool names—just describe what you want in plain language, and your assistant selects the right tools automatically. See [Meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) for how Muster keeps the assistant's context lean.

## Troubleshooting

These are the first checks for IDE setup. For deeper, platform-side failure modes—single sign-on loops, `MCPServer` states, or workflows an agent can't find—see [Troubleshoot AI agent access]({{< relref "/tutorials/ai-agents/troubleshooting" >}}).

### `authenticate_muster` keeps reappearing in your IDE

Your session has likely expired. Run `muster auth login` in a terminal to re-authenticate, then restart the MCP server in your IDE.

### An agent hits a "forbidden" error

A `forbidden` message in the agent output is a Kubernetes RBAC issue, not a Muster problem. The user authenticated fine, but their identity-provider groups aren't bound to a role that allows the action. See [Map RBAC and single sign-on]({{< relref "/tutorials/ai-agents/access-control" >}}#when-an-agent-hits-a-forbidden-error) to fix it.

### A cluster shows as disconnected in `muster auth status`

The mcp-kubernetes instance on that cluster may be temporarily unavailable. Other clusters aren't affected. If the issue persists, contact Giant Swarm support.

### Tools aren't showing up in your editor

1. Verify authentication: `muster auth status`
2. Check that the MCP server is enabled in your editor's MCP settings.
3. Restart the MCP server from your editor's MCP panel.

## Learn more

- [AI agents overview]({{< relref "/overview/ai-agents" >}}): what AI agents on the platform are and the pieces involved.
- [Architecture]({{< relref "/overview/ai-agents/architecture" >}}): how the central aggregator gives you unified access to your whole fleet.
- [Security]({{< relref "/overview/ai-agents/security" >}}): OAuth 2.1, per-user tool visibility, and how single sign-on works across clusters.
- [Developer portal AI chat]({{< relref "/overview/developer-portal/ai-chat" >}}): ask the same questions in the browser instead of your IDE.
- [Muster CLI reference]({{< relref "/reference/muster/cli" >}}): every `muster` command, including `context` and `auth`.
