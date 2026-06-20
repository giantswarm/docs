---
title: Muster architecture
linkTitle: Architecture
description: How the central Muster aggregator exposes one OAuth-protected MCP endpoint, aggregates per-cluster mcp-kubernetes servers across a fleet, and why workflows cut agent token cost.
weight: 20
mermaid: true
menu:
  principal:
    parent: overview-ai-agents
    identifier: overview-ai-agents-architecture
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How is Muster structured?
  - How does Muster give access to multiple clusters?
  - Why do workflows reduce AI agent cost?
---

Muster runs as a central **aggregator**, the `muster serve` process, that holds all the logic and exposes a single, OAuth-protected MCP endpoint. Your AI assistant connects straight to that endpoint over HTTPS.

## The aggregator

{{< mermaid >}}
flowchart TB
  client["AI assistant<br/>(VS Code / Cursor / portal chat)"]
  serve["muster serve<br/>(aggregator, management cluster)"]
  k8sA["mcp-kubernetes + mcp-prometheus<br/>(management cluster A)"]
  k8sB["mcp-kubernetes + mcp-prometheus<br/>(management cluster B)"]
  other["other MCP servers<br/>(Grafana, Teleport)"]

  client -- "HTTPS (MCP, OAuth)" --> serve
  serve --> k8sA
  serve --> k8sB
  serve --> other
{{< /mermaid >}}

`muster serve` is the central component, typically running on a management cluster. It hosts all business logic, manages the lifecycle of downstream MCP server processes, monitors their health, and exposes a [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) interface over HTTPS, using the MCP HTTP and SSE transports.

Modern AI assistants—VS Code with GitHub Copilot, Cursor, and the developer portal chat—support remote, OAuth-protected MCP servers natively. You point them straight at the aggregator's URL and they handle the [OAuth flow]({{< relref "/overview/ai-agents/security" >}}) themselves:

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

## Fleet-wide aggregation

For a customer operating several management clusters, a **central** Muster instance aggregates the `mcp-kubernetes` and `mcp-prometheus` servers on each management cluster, giving SREs a single MCP endpoint for the entire fleet:

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

The user authenticates once through their enterprise identity provider. Muster bridges that identity to each remote cluster—reusing the same token where the issuer is trusted, or exchanging it for one valid on the remote cluster where the issuer differs. The [Security]({{< relref "/overview/ai-agents/security" >}}) page covers this token handling in detail.

Two deployment shapes are supported:

- **Single management cluster**: Muster with `mcp-kubernetes` and `mcp-prometheus` on one management cluster. The simplest setup.
- **Multiple management clusters**: a central Muster that bridges SSO to the `mcp-kubernetes` and `mcp-prometheus` servers on remote management clusters. Required when a customer runs more than one management cluster.

## Workflows cut agent token cost

Muster can package a multi-step operation—authenticate, port-forward, query, correlate—as a single named **workflow** that an agent invokes with one call. It's not just convenient. It makes the AI assistant dramatically cheaper, because one workflow call replaces the whole discover-query-correlate loop the agent would otherwise run itself.

A paired A/B trial measured this directly on four real management-cluster alerts, using the same agent, model, and prompt, differing only in whether the agent was given the raw aggregated tools or the matching workflow tool:

| Metric | Raw aggregated tools | Workflow tool | Reduction |
|---|--:|--:|--:|
| Total cost (USD) | $4.32 | $1.57 | 2.8x |
| Messages | 334 | 71 | 4.7x |
| Cache-read input tokens | 11.0M | 1.1M | 9.6x |
| Tool-call invocations | 68 | 4 | 17x |

Cache-read input tokens dominate the bill, so the 10x reduction there is the real cost lever. The savings scale with how much investigation an alert needs.

The trade-off is scope: a workflow only checks what it was authored to check. For a first responder handling the specific alert that paged, that focus is a feature. For open-ended "what's broken here?" exploration, an agent with the raw tools surfaces more adjacent context at higher cost. Both modes run through the same gateway—see [meta-tools]({{< relref "/overview/ai-agents/meta-tools" >}}) for how an agent reaches each one.
