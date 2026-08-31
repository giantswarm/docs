---
title: Agent Platform architecture
diataxis_content_type: explanation
linkTitle: Architecture
description: How a tool call travels through the Agent Platform, from the TLS edge through agentgateway to Muster and the MCP servers, and where agents fit into the same path.
weight: 20
mermaid: true
menu:
  principal:
    parent: overview-agent-platform
    identifier: overview-agent-platform-architecture
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How is the Agent Platform structured?
  - What is agentgateway and where does it sit?
  - How does Muster give access to multiple clusters?
  - Why do workflows reduce AI agent cost?
aliases:
  - /overview/ai-agents/architecture/
---

The Agent Platform has one topology: a TLS-terminating edge Gateway, **agentgateway** as the MCP data plane behind it, and **Muster** as the authentication and aggregation point in front of the MCP servers. Every tool call travels the same path, whether it comes from your IDE, the developer portal, chat, or an agent running on the cluster.

## The request path

<!-- vale off -->
{{< mermaid >}}
flowchart LR
  client["MCP client<br/>(IDE, portal, chat, agent)"]
  edge["Edge Gateway<br/>TLS termination, public hostname"]
  agw["agentgateway<br/>/mcp — observability and<br/>policy choke point"]
  muster["Muster<br/>OAuth enforcement,<br/>MCP aggregation"]
  servers["MCP servers<br/>(mcp-kubernetes, mcp-prometheus, …)"]

  client -- "HTTPS /mcp" --> edge
  edge --> agw
  agw --> muster
  muster --> servers
{{< /mermaid >}}
<!-- vale on -->

Each hop has one job:

- **The edge Gateway** terminates TLS and owns the public hostname. It's a standard Kubernetes Gateway API gateway—on Giant Swarm installations the cluster's shared Envoy Gateway, on your own cluster either an existing Gateway or one the platform chart creates.
- **agentgateway** is the MCP data plane. Every `/mcp` request passes through it, which makes it the single choke point where tool calls become observable (protocol, tool name, session, latency) and where policy can be applied. It forwards the caller's bearer token to Muster without consuming it.
- **Muster** is the authentication enforcement point. It acts as an OAuth resource server: an unauthenticated request gets a `401` response with a `WWW-Authenticate` header pointing at the standard OAuth discovery metadata, which is how MCP clients find out where to sign in—no manual configuration. Authenticated requests reach the aggregator, which fans out to the MCP servers behind it and handles their credentials on the user's behalf.
- **The MCP servers** do the actual work: `mcp-kubernetes` and `mcp-prometheus` on each management cluster, plus any other servers you put behind the gateway.

OAuth sign-in, token, and discovery endpoints are served by Muster directly. Only MCP traffic flows through agentgateway.

## The aggregator

Muster hosts all the aggregation logic, manages the lifecycle of downstream MCP server connections, monitors their health, and exposes a [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}) interface using the MCP HTTP and SSE transports.

Modern AI assistants—Claude Code, Cursor, VS Code with GitHub Copilot, the developer portal chat, and other MCP-capable tools—support remote, OAuth-protected MCP servers natively. You point them straight at the platform's MCP URL and they handle the [OAuth flow]({{< relref "/overview/agent-platform/security" >}}) themselves:

```json
{
  "mcpServers": {
    "muster": {
      "url": "https://muster.<management-cluster>.<base-domain>/mcp"
    }
  }
}
```

All aggregation, downstream authentication, and tool management live server-side, where they can be operated and updated centrally—there is nothing to keep running on your machine.

## The optional local bridge

Some MCP clients can't connect to a remote, OAuth-protected server directly—they only speak stdio, or lack a built-in OAuth flow. For those, `muster agent` is a thin local bridge: it converts stdio to HTTPS and performs OAuth on the client's behalf. It holds no business logic, so it stays a single lightweight binary. If your assistant supports remote MCP with OAuth—most now do—you don't need it.

## Conflict-free tool names

The aggregator resolves tool-name conflicts by prefixing external tools with their server name, so `get_pods` from the Kubernetes server becomes `x_kubernetes_get_pods` and `query` from Prometheus becomes `x_prometheus_query`. Tool registries update dynamically as servers start, stop, or change—the assistant's next discovery call reflects the new capabilities without any IDE restart.

## The agent plane

Agents that run *on* the platform are Kubernetes resources, managed by the runtime controller and surfaced through the developer portal and chat channels. Architecturally they're ordinary MCP clients: an agent reaches its tools through the same Muster endpoint as everyone else, carrying the identity of the human it acts for. The human's own token is the only credential on the agent path, so downstream systems and audit logs see the human. There is no separate, privileged tool path for agents.

The [platform integration]({{< relref "/overview/agent-platform/platform-integration" >}}) page covers what that means for RBAC and auditing; the [security]({{< relref "/overview/agent-platform/security" >}}) page covers the token handling.

## Supporting services

- **Valkey** stores Muster's OAuth session state, so tokens survive a Muster restart.
- **The avatar service** renders each agent's identifying icon deterministically from its name, reused by every surface (portal, chat).

## Fleet-wide aggregation

For a customer operating several management clusters, a **central** Muster instance aggregates the `mcp-kubernetes` and `mcp-prometheus` servers on each management cluster, giving SREs a single MCP endpoint for the entire fleet:

<!-- vale off -->
{{< mermaid >}}
flowchart LR
  user["SRE / developer"]
  central["Central Muster<br/>(management cluster)"]
  mcpA["mcp-kubernetes + mcp-prometheus<br/>(MC A)"]
  mcpB["mcp-kubernetes + mcp-prometheus<br/>(MC B)"]
  mcpC["mcp-kubernetes + mcp-prometheus<br/>(MC C)"]

  user -- "one SSO login,<br/>one endpoint" --> central
  central --> mcpA
  central --> mcpB
  central --> mcpC
{{< /mermaid >}}
<!-- vale on -->

The user authenticates once through their enterprise identity provider. Muster bridges that identity to each remote cluster. It reuses the same token where the issuer is trusted, or exchanges it for one valid on the remote cluster where the issuer differs. The [Security]({{< relref "/overview/agent-platform/security" >}}) page covers this token handling in detail.

Two deployment shapes are supported:

- **Single management cluster**: the platform with `mcp-kubernetes` and `mcp-prometheus` on one management cluster. The simplest setup.
- **Multiple management clusters**: a central Muster that bridges SSO to the `mcp-kubernetes` and `mcp-prometheus` servers on remote management clusters. Required when a customer runs more than one management cluster.

## Workflows cut agent token cost

Muster can package a multi-step operation—authenticate, port-forward, query, correlate—as a single named **workflow** that an agent invokes with one call. It's not just convenient. It makes the AI assistant dramatically cheaper, because one workflow call replaces the whole discover-query-correlate loop the agent would otherwise run itself.

One internal lab trial measured this directly on four real management-cluster alerts, with the same agent, model, and prompt, differing only in whether the agent was given the raw aggregated tools or the matching workflow tool. The numbers below are illustrative of the *shape* of the saving rather than a guarantee—the ratios hold across a range of investigations, but the absolute figures depend on the model and its pricing:

| Metric | Raw aggregated tools | Workflow tool | Reduction |
|---|--:|--:|--:|
| Cost | $4.32 | $1.57 | 2.8x |
| Messages | 334 | 71 | 4.7x |
| Cache-read input tokens | 11.0M | 1.1M | 9.6x |
| Tool-call invocations | 68 | 4 | 17x |

Cache-read input tokens dominate the bill, so the 10x reduction there is the real cost lever, and it holds regardless of the per-token price. The savings scale with how much investigation an alert needs.

The trade-off is scope: a workflow only checks what it was authored to check. For a first responder handling the specific alert that paged, that focus is a feature. For open-ended "what's broken here?" exploration, an agent with the raw tools surfaces more adjacent context at higher cost. Both modes run through the same gateway—see [meta-tools]({{< relref "/overview/agent-platform/meta-tools" >}}) for how an agent reaches each one.
