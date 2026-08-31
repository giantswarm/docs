---
title: Integration with SSO, cluster management, and observability
diataxis_content_type: explanation
linkTitle: Platform integration
description: How the Agent Platform rides on your existing single sign-on, applies Kubernetes RBAC to every agent action, and plugs into the platform's observability stack.
weight: 50
menu:
  principal:
    parent: overview-agent-platform
    identifier: overview-agent-platform-integration
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How does the Agent Platform integrate with my identity provider?
  - Does Kubernetes RBAC apply to AI agents?
  - Who shows up in the audit log when an agent acts?
  - What observability does the Agent Platform ship?
---

The Agent Platform doesn't bring its own identity system, its own permission model, or its own monitoring stack. It rides on the ones your platform already has: your OIDC identity provider, Kubernetes RBAC, and the Prometheus and OpenTelemetry tooling you already operate. This page explains all three integration points.

## Single sign-on

The platform uses **one OIDC identity provider per installation**. On Giant Swarm clusters that's [Dex]({{< relref "/overview/architecture/authentication" >}}), federating to your upstream provider (GitHub, Entra ID, and others)—but the contract is plain OIDC, so any compliant provider works. On a self-hosted install you point the chart's identity configuration at your own issuer.

Sign in once and every surface rides the same identity:

- **MCP clients** (Claude Code, Cursor, VS Code) authenticate to Muster through the standard OAuth flow against that provider.
- **The developer portal** signs you in through the same provider and forwards your identity when it talks to Muster and the agent runtime.
- **Chat channels** link your chat account to your platform identity with a one-time browser sign-in; from then on, agents you talk to act with your identity.

The important property: the platform never mints its own identity tokens. Your identity provider is the sole authority—Muster signs nothing, and everything downstream validates tokens against the provider that issued them. The [security]({{< relref "/overview/agent-platform/security" >}}) and [authentication]({{< relref "/overview/agent-platform/authentication" >}}) pages cover the token mechanics in depth.

## Cluster management

Agents read and change cluster state through `mcp-kubernetes`, and the credential that arrives at the Kubernetes API is **your own token**:

- **Management clusters.** Muster forwards your token to `mcp-kubernetes`, which passes it to the API server's native OIDC authentication. Kubernetes RBAC evaluates *you*, with the same roles and bindings that apply when you use `kubectl`, and the audit log records *you*. There's no impersonation and no platform-minted token on this path.
- **Fleets (hub and spoke).** When a central Muster reaches a remote management cluster with its own identity provider, it uses standards-based token exchange ([RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693)) to obtain a token that cluster accepts—still representing you, still evaluated by that cluster's RBAC.
- **Workload clusters.** Access currently uses the cluster's admin kubeconfig with user impersonation: `mcp-kubernetes` impersonates your user and groups, so RBAC still evaluates you, and the audit log records the impersonated identity. This is an interim mechanism until workload clusters accept the platform's OIDC tokens directly.

The consequence for governance: **an agent can't do anything the human it acts for couldn't do**. Granting or revoking an engineer's Kubernetes permissions immediately grants or revokes what agents acting for them can do—there's no second permission system to keep in sync. See [Map RBAC and SSO]({{< relref "/tutorials/agent-platform/access-control" >}}) for wiring identity-provider groups to cluster permissions.

## Observability

The platform components ship with the same observability conventions as the rest of the Giant Swarm platform:

- **Metrics.** Every component exposes Prometheus metrics with ServiceMonitors: Muster (gateway health, per-server tool dispatch volume, outcomes, and latency, workflow executions), the agent runtime controller, and the supporting services.
- **Dashboard.** The Muster chart ships the **Muster / MCP Gateway** Grafana dashboard: MCP server fleet state, tool-call volume and latency per downstream server, and workflow execution statistics.
- **Alerts.** The chart ships alert rules for MCP servers that are genuinely broken: `MusterMCPServerFailed` (a server stuck in the `Failed` state) and `MusterMCPServerFlapping` (repeated failure transitions). A server in the `Auth Required` state isn't alerted on: it's a healthy state that means no user session is currently signed in to that server, not an outage.
- **Traces.** agentgateway and the agent runtime export OTLP traces, so every MCP call that crosses the gateway is visible with protocol, tool name, session, and latency.

The developer portal's MCP usage view reads the same dispatch metrics, so operators and users look at one set of numbers.

## Related pages

- [Agent Platform architecture]({{< relref "/overview/agent-platform/architecture" >}}) - The request path these integrations attach to.
- [Security]({{< relref "/overview/agent-platform/security" >}}) - The OAuth model, per-user tool visibility, and sign-out.
- [Authentication deep dive]({{< relref "/overview/agent-platform/authentication" >}}) - Every token on the path, end to end.
- [Observability overview]({{< relref "/overview/observability" >}}) - The platform's monitoring stack these components plug into.
