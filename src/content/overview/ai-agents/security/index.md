---
title: AI agent security and SSO
linkTitle: Security
description: How Muster secures AI agent access with OAuth 2.1, per-user tool visibility keyed on identity, and single sign-on across clusters via token forwarding and exchange.
weight: 40
mermaid: true
menu:
  principal:
    parent: overview-ai-agents
    identifier: overview-ai-agents-security
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How does Muster authenticate AI agents?
  - Can AI agents only see the tools I'm allowed to use?
  - How does single sign-on work across clusters?
---

Muster treats authentication as a first-class concern at two levels: protecting access to the gateway itself, and handling authentication to the downstream MCP servers on a user's behalf. Both are built on OAuth 2.1.

## Agent-to-Muster authentication

The aggregator requires the OAuth 2.1 authorization code flow with PKCE. The first time your AI assistant connects—or when you run `muster auth login` from the CLI—your browser opens for SSO against your enterprise identity provider. Tokens are stored locally with restricted file permissions. Access tokens are short-lived—30 minutes by default—and your MCP client refreshes them automatically in the background, so you stay connected without re-authenticating.

Because authentication uses the OAuth 2.1 flow, an assistant that supports remote MCP servers natively can connect straight to the aggregator's HTTPS URL. Examples include VS Code and Cursor. They run this flow themselves, with no local bridge process. Production deployments require HTTPS for all OAuth endpoints.

## Muster-to-downstream authentication

The downstream MCP servers behind Muster (such as `mcp-kubernetes` and `mcp-prometheus` on each cluster) are themselves protected. Muster acts as an OAuth proxy on your behalf:

{{< mermaid >}}
flowchart TB
  s1["1. Assistant invokes a tool that needs server X"]
  s2["2. Muster forwards the request to server X"]
  s3["3. Server X replies 401 (authentication required)"]
  s4["4. Muster returns an authorization URL to the assistant"]
  s5["5. User authenticates in the browser"]
  s6["6. Muster retries the request with the acquired token"]
  s7["7. Server X returns the result"]
  s1 --> s2 --> s3 --> s4 --> s5 --> s6 --> s7
{{< /mermaid >}}

When a downstream server returns a `401`, Muster detects the challenge and hands back an "authentication required" response with an authorization URL. Once you authenticate in the browser, it exchanges the code for tokens scoped to your session. Subsequent calls to that server carry the token automatically.

## Per-user tool visibility

Per-user state is keyed by the OAuth `sub` (subject) claim extracted from each authenticated request. There is no separate session-ID layer. The access token itself identifies the user.

A direct benefit is **per-user tool visibility**: each user only sees tools from the MCP servers they have personally authenticated with. If you haven't authenticated to a given cluster—or your identity provider doesn't grant you access to it—its tools simply don't appear in your `list_tools` results. Cluster-level authorization is still enforced by each cluster's own Kubernetes RBAC. A tool call you aren't permitted to make is rejected by the cluster, not allowed by the gateway.

## Single sign-on across clusters

When several downstream servers trust the same identity provider, Muster provides SSO so you authenticate once and reach the whole fleet. It uses two mechanisms depending on the trust relationship:

- **Token forwarding**: reuse the same access token across servers that trust the same issuer. The latest valid token is resolved per request.
- **RFC 8693 token exchange**: exchange a local ID token for one valid on a remote identity provider. This is what enables cross-cluster SSO: authenticating to remote management clusters and their workload clusters through a central management cluster.

After login, the CLI waits for SSO-configured servers to finish connecting. `muster auth status` distinguishes servers still completing SSO setup ("SSO Pending") from those that genuinely need a manual login, so you get an accurate picture of what you can reach:

```text
MCP Servers
  cluster-a-mcp-kubernetes   Connected [SSO: Forwarded]
  cluster-b-mcp-kubernetes   Connected [SSO: Exchanged]
  cluster-c-mcp-kubernetes   Connected [SSO: Exchanged]
```

## Signing out

Muster offers three distinct logout operations for different needs:

- **Per-device logout** (`muster auth logout`): revokes the entire token family for the current device. Your other devices are unaffected.
- **Per-server disconnect**: clears the downstream token for a single server and drops its cached capabilities, leaving your other connections intact.
- **Sign out everywhere**: clears all downstream tokens and cached capabilities for your identity across every device.

Per-device isolation comes from OAuth refresh-token families, not a custom session layer—so revoking one device never disturbs the others.

For the hands-on login flow and an RBAC troubleshooting guide, see [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}).
