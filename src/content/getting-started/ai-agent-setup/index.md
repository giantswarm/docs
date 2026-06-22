---
linkTitle: Set up your AI agent
title: Set up your AI agent for Kubernetes operations
description: Learn how to use Muster and mcp-kubernetes to interact with your Giant Swarm management clusters through AI assistants like Claude Code, Cursor, or GitHub Copilot.
weight: 80
mermaid: true
menu:
  principal:
    parent: getting-started
    identifier: getting-started-ai-agent-setup
last_review_date: 2026-02-27
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

Two components work together to make this possible:

- **mcp-kubernetes** runs on each management cluster and exposes Kubernetes resources—pods, deployments, services, logs, events, and more—through a secure, OAuth-protected API using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

- **Muster** is a central aggregator that connects all your mcp-kubernetes instances into a single endpoint. Instead of configuring your AI assistant to talk to a separate MCP server for each cluster, you point it at Muster and get unified access to all clusters at once.

Modern AI assistants—Claude Code, Cursor, and VS Code with GitHub Copilot—support remote, OAuth-protected MCP servers natively. You point your editor straight at the Muster endpoint over HTTPS, and it runs the SSO login flow itself, with nothing to install or keep running locally:

{{< mermaid >}}
flowchart TB
  client["AI assistant<br/>(Claude Code / Cursor / VS Code)"]
  muster["Muster aggregator<br/>(management cluster)"]
  k8sA["mcp-kubernetes (cluster A)"]
  k8sB["mcp-kubernetes (cluster B)"]
  k8sC["mcp-kubernetes (cluster C)"]
  client -- "HTTPS (MCP, OAuth)" --> muster
  muster --> k8sA
  muster --> k8sB
  muster --> k8sC
{{< /mermaid >}}

That direct connection is the recommended setup, and Muster handles authentication to each cluster on your behalf so your assistant never juggles tokens or credentials directly. For a client that can't reach a remote, OAuth-protected MCP server—one that only speaks stdio, or has no built-in OAuth flow—the `muster` CLI provides an optional local bridge (`muster agent`) that converts stdio to HTTPS and performs the login for you.

For the bigger picture—what Muster is, how the aggregator works, and how it stays secure—see the [AI agents overview]({{< relref "/overview/ai-agents" >}}). If you'd rather ask questions in the browser instead of your IDE, the [developer portal AI chat]({{< relref "/overview/developer-portal/ai-chat" >}}) is powered by the same Muster aggregator.

## Before you start

You'll need:

- Access to a Giant Swarm installation with mcp-kubernetes and Muster deployed. Ask your Giant Swarm account engineer for your Muster endpoint URL—it looks like `https://muster.<management-cluster>.<base-domain>/mcp`.
- Ensure `dex` is configured in your management clusters with a supported identity provider. Contact Giant Swarm support if not.
- An MCP-capable client: Claude Code, Cursor, or VS Code with the GitHub Copilot extension.

## Connect your editor directly

This is the recommended setup. Point your editor at the Muster endpoint your account engineer gave you—it looks like `https://muster.<management-cluster>.<base-domain>/mcp`. The first time the editor connects, it opens your browser for SSO login. After you authenticate, the full set of Kubernetes tools becomes available with no restart.

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

Download the `muster` binary from the [GitHub releases page](https://github.com/giantswarm/muster/releases). It's a single binary with no additional dependencies—just put it somewhere on your `PATH`.

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

Muster uses a meta-tool architecture. Instead of exposing hundreds of individual tools (one per Kubernetes operation per cluster), it exposes a small set of meta-tools that your AI assistant uses automatically. These include `list_tools`, `call_tool`, `filter_tools`, and `describe_tool`. You don't need to know the tool names—just describe what you want in plain language. See [Meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) for how this keeps the assistant's context lean.

## Session management

- **Token expiry:** Access tokens expire every 30 minutes, but your editor (or the local bridge) refreshes them automatically in the background.
- **Session duration:** Your overall session lasts approximately 30 days (the default) before you need to log in again. This can vary by installation.
- **Re-authentication:** If your session expires, your editor (or the bridge) detects it and re-authenticates by opening your browser.

## CLI quick reference

| Command | Purpose |
|---|---|
| `muster auth login` | Authenticate via SSO |
| `muster auth status` | Check connectivity to all MCP servers |
| `muster auth whoami` | Show the currently authenticated identity |
| `muster auth logout` | Clear stored tokens |
| `muster context add` | Register a new Muster endpoint |
| `muster context use` | Switch active context |
| `muster context current` | Show the name of the active context |
| `muster context show <name>` | Show a specific context's configuration |
| `muster context list` | List all contexts |

## Troubleshooting

### `authenticate_muster` keeps reappearing in your IDE

Your session has likely expired. Run `muster auth login` in a terminal to re-authenticate, then restart the MCP server in your IDE.

### Lack of permissions on the cluster

You may encounter a message like this in the agent output:

```text
Failed to list resources: failed to list networkpolicies: networkpolicies.networking.k8s.io is forbidden: User "<user>" cannot list resource "networkpolicies" in API group "networking.k8s.io" in the namespace "kube-system"
```

Make sure the user has the correct group attached in the identity provider (Azure AD, GitHub, and similar) which is bound to a role in the cluster to perform those actions.

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
