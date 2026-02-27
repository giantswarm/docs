---
linkTitle: Set up your AI agent
title: Set up your AI agent for Kubernetes operations
description: Learn how to use Muster and mcp-kubernetes to interact with your Giant Swarm management clusters through AI assistants like GitHub Copilot or Cursor.
weight: 80
menu:
  principal:
    parent: getting-started
    identifier: getting-started-ai-agent-setup
last_review_date: 2026-02-27
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I use AI assistants with my Kubernetes clusters?
  - How do I set up Muster with VS Code or Cursor?
  - What is mcp-kubernetes?
  - How do I authenticate with Muster?
---

The Giant Swarm platform is ready to be used by AI agents. Its integration lets you query Kubernetes resources across all your management clusters using plain language—directly from your IDE. Instead of switching between terminals and dashboards, you can ask your AI assistant things like "are there any pods in CrashLoopBackOff on any cluster?" and get answers grounded in live cluster state.

## How it works

Two components work together to make this possible:

**mcp-kubernetes** runs on each management cluster and exposes Kubernetes resources—pods, deployments, services, logs, events, and more—through a secure, OAuth-protected API using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/).

**Muster** is a central aggregator that connects all your mcp-kubernetes instances into a single endpoint. Instead of configuring your AI assistant to talk to a separate MCP server for each cluster, you point it at Muster and get unified access to all clusters at once.

The `muster` CLI runs locally as a lightweight agent that bridges your AI assistant (via stdio) with the Muster aggregator (via HTTPS):

```text
AI Assistant (VS Code / Cursor)
      │ stdio (MCP protocol)
      ▼
muster agent (local CLI process)
      │ HTTPS
      ▼
Muster aggregator (management cluster)
      │
      ├── mcp-kubernetes (cluster A)
      ├── mcp-kubernetes (cluster B)
      └── mcp-kubernetes (cluster C)
```

The agent handles authentication transparently, so your AI assistant never needs to manage tokens or cluster credentials directly.

## Before you start

You'll need:

- Access to a Giant Swarm installation with mcp-kubernetes and Muster deployed. Ask your Giant Swarm account engineer for your Muster endpoint URL—it looks like `https://muster.<management-cluster>.<base-domain>/mcp`.
- Ensure `dex` is configured in your management clusters with a supported identity provider. Contact Giant Swarm support if not.
- VS Code with the GitHub Copilot extension, or Cursor.

## Step 1: Install Muster

Download the `muster` binary from the [GitHub releases page](https://github.com/giantswarm/muster/releases). It's a single binary with no additional dependencies—just put it somewhere on your `PATH`.

## Step 2: Configure your context

A context tells Muster which aggregator endpoint to connect to. Add one with the endpoint URL your account engineer provided, then activate it:

```bash
muster context add my-platform --endpoint https://muster.<management-cluster>.<base-domain>/mcp
muster context use my-platform

You can verify the context is set correctly:

```bash
muster context show my-platform
```

## Step 3: Authenticate

Run the login command, which opens your browser for SSO authentication:

```bash
muster auth login
```

After you authenticate, check that everything is connected:

```bash
muster auth status
```

You should see all your MCP servers listed as `Connected`. The output looks something like this:

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

## Step 4: Configure your code editor

### VS Code (GitHub Copilot)

Create or edit `.vscode/mcp.json` in your workspace (or your user-level MCP settings) and add:

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

The agent uses the active context you set in Step 2, so no endpoint flag is needed here. The first time Copilot connects, if you haven't authenticated yet, the agent exposes a single tool called `authenticate_muster`. Copilot calls this tool automatically, which opens your browser for SSO login. After authentication succeeds, the full set of Kubernetes tools becomes available—no restart needed.

### Cursor

Create or edit `~/.cursor/mcp.json` (for global settings) or `.cursor/mcp.json` in your project directory, and add:

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

The agent uses the active context you set in Step 2. Make sure MCP is enabled in Cursor's settings. After saving the configuration, you can toggle the MCP server off and on from Cursor's MCP settings panel to pick up the changes.

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

Muster uses a meta-tool architecture—instead of exposing hundreds of individual tools (one per Kubernetes operation per cluster), it exposes a small set of meta-tools (including `list_tools`, `call_tool`, `filter_tools`, and `describe_tool`) that your AI assistant uses automatically. You don't need to know the tool names—just describe what you want in plain language.

## Session management

- **Token expiry:** Access tokens expire every 30 minutes, but the agent refreshes them automatically in the background.
- **Session duration:** Your overall session lasts approximately 30 days (the default) before you need to log in again. This can vary by installation.
- **Re-authentication:** If your session expires, the agent automatically detects it and initiates re-authentication by opening your browser.

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
Failed to list resources: failed to list networkpolicies: networkpolicies.networking.k8s.io is forbidden: User "fernando@example.com" cannot list resource "networkpolicies" in API group "networking.k8s.io" in the namespace "kube-system"
```

Make sure the user has the correct group attached in the identity provider (Azure AD, GitHub, and similar) which is bound to a role in the cluster to perform those actions.

### A cluster shows as disconnected in `muster auth status`

The mcp-kubernetes instance on that cluster may be temporarily unavailable. Other clusters aren't affected. If the issue persists, contact Giant Swarm support.

### Tools aren't showing up in your editor

1. Verify authentication: `muster auth status`
2. Check that the MCP server is enabled in your editor's MCP settings.
3. Restart the MCP server from your editor's MCP panel.
