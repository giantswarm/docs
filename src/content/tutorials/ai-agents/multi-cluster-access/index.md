---
title: Give agents multi-cluster access
linkTitle: Multi-cluster access
description: Expose an entire fleet of management clusters through one central Muster, with the instance-selection argument contract and RFC 8693 token exchange for cross-cluster single sign-on.
weight: 40
mermaid: true
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-multi-cluster-access
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I give AI agents access to multiple management clusters?
  - How does cross-cluster single sign-on work in Muster?
  - What value do I pass to select a cluster?
---

A customer running several management clusters doesn't want a separate connection per cluster. A **central** Muster aggregates the `mcp-kubernetes` (and `mcp-prometheus`) servers on each management cluster and gives every user one endpoint and one login for the whole fleet.

<!-- vale off -->
{{< mermaid >}}
flowchart LR
  user["SRE / developer"]
  central["Central Muster<br/>(management cluster)"]
  mcpA["mcp-kubernetes<br/>(MC A)"]
  mcpB["mcp-kubernetes<br/>(MC B)"]
  mcpC["mcp-kubernetes<br/>(MC C)"]

  user -- "one SSO login,<br/>one endpoint" --> central
  central --> mcpA
  central --> mcpB
  central --> mcpC
{{< /mermaid >}}
<!-- vale on -->

This guide assumes the central Muster and the per-cluster `mcp-kubernetes` servers are already deployed. It covers how to wire them together so an agent can reach the whole fleet.

## Two deployment shapes

- **Single management cluster:** Muster with `mcp-kubernetes` and `mcp-prometheus` on one cluster. The simplest setup, and nothing here about instance selection or token exchange applies.
- **Multiple management clusters:** a central Muster that bridges single sign-on to the `mcp-kubernetes` servers on remote clusters. The rest of this page is about this shape.

## Register each cluster as a family member

Register each cluster's `mcp-kubernetes` as a remote [`MCPServer`]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) and put them all in one **family** so their tools appear once, with an argument that selects the target cluster:

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: cluster-a-mcp-kubernetes
  namespace: muster
spec:
  type: streamable-http
  url: "https://mcp-kubernetes.cluster-a.<base-domain>/mcp"
  autoStart: true
  family:
    name: kubernetes
    instanceArg: management_cluster
  auth:
    type: oauth
    tokenExchange:
      enabled: true
      dexTokenEndpoint: "https://dex.cluster-a.<base-domain>/token"
      connectorId: "central-dex"
      clientCredentialsSecretRef:
        name: cluster-a-token-exchange-credentials
```

Every cluster's server shares `family.name: kubernetes` and `instanceArg: management_cluster`, so all their tools collapse to one set (`x_kubernetes_list`, `x_kubernetes_logs`, and the rest).

Register each cluster's `mcp-prometheus` the same way, in its own `prometheus` family, so metrics tools are fleet-wide too:

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: MCPServer
metadata:
  name: cluster-a-mcp-prometheus
  namespace: muster
spec:
  type: streamable-http
  url: "https://mcp-prometheus.cluster-a.<base-domain>/mcp"
  autoStart: true
  family:
    name: prometheus
    instanceArg: management_cluster
  auth:
    type: oauth
    tokenExchange:
      enabled: true
      dexTokenEndpoint: "https://dex.cluster-a.<base-domain>/token"
      connectorId: "central-dex"
      clientCredentialsSecretRef:
        name: cluster-a-token-exchange-credentials   # reuse the kubernetes credentials
```

The Prometheus servers collapse to `x_prometheus_*` tools (such as `x_prometheus_query`), selected by the same `management_cluster` argument. A single token-exchange secret per cluster covers both servers, so an agent that authenticates once reaches each cluster's Kubernetes API and its metrics.

## The instance-selection contract

The value an agent passes for `management_cluster` is the **full MCP server name**, not the bare cluster name. For a server named `cluster-a-mcp-kubernetes`, the correct argument is:

```text
management_cluster: cluster-a-mcp-kubernetes
```

This trips up agents in practice: a model often guesses the bare cluster name first and gets a wrong-argument error, then retries. The same rule applies to the `prometheus` family, where the value is the full Prometheus server name (`<cluster>-mcp-prometheus`). If you write [workflows]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}) for a fleet, document this contract in the workflow's argument description, and have the workflow take the full server name. Naming servers consistently (always `<cluster>-mcp-kubernetes` and `<cluster>-mcp-prometheus`) makes the value predictable.

## Cross-cluster single sign-on with token exchange

When remote clusters run their own identity provider, the user's central token isn't valid on them directly. Muster uses **RFC 8693 token exchange**: it exchanges the user's central token for one the remote cluster's identity provider issues. The user authenticates once and reaches every cluster.

The `tokenExchange` block on each remote server's `auth` configures this:

- `enabled: true` turns it on.
- `dexTokenEndpoint`: the remote identity provider's token endpoint. This can differ from the issuer when access goes through a proxy.
- `expectedIssuer`: the issuer expected in the exchanged token. Set it when the endpoint differs from the issuer (a proxy); otherwise Muster derives it from the endpoint.
- `connectorId`: the connector on the remote identity provider that trusts the central one.
- `clientCredentialsSecretRef`: a reference to a Kubernetes secret holding the client ID and secret for authenticating to the remote token endpoint.

The remote identity provider must be configured with a connector that trusts the central one. After login, the central Muster waits for token exchange to complete, and `muster auth status` shows each server's mode:

```text
MCP Servers
  cluster-a-mcp-kubernetes   Connected [SSO: Exchanged]
  cluster-b-mcp-kubernetes   Connected [SSO: Exchanged]
```

Where a remote server trusts the **same** issuer as the central Muster, you don't need exchange at all—set `forwardToken: true` instead and Muster reuses the user's token. See [RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}) for the difference.

## Operational notes from production

A few details surface only when you run this at scale:

- **`mcp-kubernetes` needs to read kubeconfig secrets** for the clusters it serves, in the relevant namespaces on each management cluster. An interim approach grants cluster-wide secret access; per-namespace RBAC automation is the longer-term direction.
- **Large tokens overflow default ingress buffers.** Enterprise tokens carrying many group claims can exceed the default nginx header buffer. The `mcp-kubernetes` ingress needs a raised `large_client_header_buffers` to accept them. See [RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}#large-tokens) for the symptom and fix.

## Related

- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): the `family` and `auth` fields in full.
- [Map RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}): mapping identity to cluster permissions.
- [Architecture]({{< relref "/overview/ai-agents/architecture" >}}): how fleet-wide aggregation fits together.
