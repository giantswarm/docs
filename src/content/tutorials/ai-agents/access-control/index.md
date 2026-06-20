---
title: Map RBAC and single sign-on
linkTitle: RBAC and SSO
description: Connect identity-provider groups to Kubernetes RBAC so AI agents act with each user's own permissions, and handle large tokens and group limits.
weight: 50
menu:
  principal:
    parent: tutorials-ai-agents
    identifier: tutorials-ai-agents-access-control
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do AI agents inherit my cluster permissions?
  - Why does my agent get a forbidden error from a cluster?
  - Why do users with many groups fail to authenticate?
---

An AI agent acting through Muster has exactly the permissions of the person driving it—no more. Authorization isn't something Muster grants; it flows from the user's identity-provider groups through to each cluster's Kubernetes RBAC. This guide explains how that chain works and how to keep it healthy.

## The permission chain

Three layers combine to decide what an agent can do:

1. **Identity provider:** the user authenticates through enterprise single sign-on. Their token carries group claims.
2. **Muster:** keys all per-user state on the OAuth `sub` (subject) claim and forwards or exchanges the user's token to each downstream server. Muster never widens access—it can't let an agent do something the user's token doesn't permit.
3. **Kubernetes RBAC:** each cluster binds identity-provider groups to roles. A tool call the user isn't permitted to make is rejected by the cluster itself.

Because Muster keys visibility on identity, each user only sees tools from servers they've personally authenticated with. This is **per-user tool visibility**: a cluster a user can't reach simply doesn't appear in their tool list. See the [security model]({{< relref "/overview/ai-agents/security" >}}) for the mechanics.

## Bind identity-provider groups to cluster roles

For an agent to do anything useful on a cluster, the user's groups must be bound to a Kubernetes role there. This is standard OIDC RBAC: a `ClusterRoleBinding` (or `RoleBinding`) whose subject is the group from the identity provider.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: platform-team-view
subjects:
  - kind: Group
    name: "platform-team"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: view
  apiGroup: rbac.authorization.k8s.io
```

Manage these bindings through your usual GitOps pipeline, the same as any other cluster RBAC. The group name must match exactly what the identity provider puts in the token.

## Forward or exchange the token

Muster needs the user's token to reach a downstream server in a form the cluster's OIDC accepts:

- **Token forwarding** (`auth.forwardToken: true`): reuse the user's token where the downstream server trusts the same issuer. For Kubernetes OIDC, add the audience the cluster expects with `requiredAudiences` so the forwarded token is accepted:

```yaml
spec:
  auth:
    type: oauth
    forwardToken: true
    requiredAudiences:
      - "dex-k8s-authenticator"
```

- **Token exchange** (`auth.tokenExchange`): for remote clusters with their own identity provider, exchange the central token for one the remote provider issues. See [multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}#cross-cluster-single-sign-on-with-token-exchange).

## When an agent hits a forbidden error

A message like this in the agent output means RBAC, not a Muster bug:

```text
networkpolicies.networking.k8s.io is forbidden: User "<user>" cannot list
resource "networkpolicies" in API group "networking.k8s.io" in the namespace
"kube-system"
```

The user authenticated fine, but their groups aren't bound to a role that allows the action. Fix it by binding the right identity-provider group to an appropriate role on that cluster. The agent picks up the new permission on its next call—no reconnect needed.

## Large tokens {#large-tokens}

Enterprise tokens that carry many group claims can break two limits:

- **Ingress header buffers.** A token with many groups can exceed the default nginx header buffer, and the request is rejected before it reaches the server. Raise `large_client_header_buffers` on the `mcp-kubernetes` ingress to accept large tokens.
- **Group count.** Users in a very large number of groups were once rejected outright. The OAuth layer now truncates excessive groups to a configurable limit instead of rejecting the request, so heavily-grouped users can still authenticate. If a user belongs to more groups than the limit, make sure the groups that matter for cluster RBAC are within it.

If a user can authenticate from a small account but fails from a heavily-grouped one, suspect these limits first.

## Related

- [Security model]({{< relref "/overview/ai-agents/security" >}}): per-user visibility, token forwarding, and exchange.
- [Multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}): cross-cluster single sign-on.
- [Troubleshooting]({{< relref "/tutorials/ai-agents/troubleshooting" >}}): authentication loops and missing tools.
