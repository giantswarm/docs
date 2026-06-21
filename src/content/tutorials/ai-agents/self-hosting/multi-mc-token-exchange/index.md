---
title: Multi-cluster token exchange
linkTitle: Multi-cluster token exchange
description: Compare the single-cluster and central deployment shapes, set up RFC 8693 token exchange to remote management clusters, and grant the kubeconfig access each needs.
weight: 90
menu:
  principal:
    parent: tutorials-ai-agents-self-hosting
    identifier: tutorials-ai-agents-multi-mc-token-exchange
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I give Muster access to multiple management clusters?
  - How does cross-cluster single sign-on work for AI agents?
  - What RBAC does mcp-kubernetes need to read kubeconfig secrets?
---

{{% notice note %}}
**Applies to self-hosted Muster only.** Follow this guide when you operate your own central Muster across several management clusters. On the managed Giant Swarm platform, multi-cluster wiring is handled for you.
{{% /notice %}}

A customer with more than one management cluster wants a single endpoint and a single login for the whole fleet. This guide covers the two deployment shapes, sets up the RFC 8693 token exchange that bridges single sign-on to remote clusters, and grants the cluster access each `mcp-kubernetes` needs.

It builds on [multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}), which covers the `MCPServer` family wiring. This page is about the operational setup: secrets, identity-provider trust, and RBAC.

## Two deployment shapes

- **Scenario 1, single cluster:** one management cluster runs Muster alongside its `mcp-kubernetes` and `mcp-prometheus`. The user's token is already valid on that cluster, so nothing here about token exchange applies. This is the simpler shape and a good place to start.
- **Scenario 2, central cluster:** a central Muster aggregates the `mcp-kubernetes` servers on several remote management clusters. Each remote cluster runs its own Dex, so the central token isn't valid there directly. Muster exchanges it. The rest of this page is about this shape.

## How the exchange works

When a remote cluster runs its own identity provider, Muster uses RFC 8693 token exchange to turn the user's central token into one the remote provider issues:

1. The user signs in once against the central Muster through enterprise single sign-on.
2. For each remote server marked for exchange, Muster posts the user's token to that cluster's Dex token endpoint.
3. The remote Dex, which trusts the central Dex through a connector, issues a token valid on the remote cluster.
4. Muster caches the exchanged token and uses it for that user's calls, re-exchanging it only as it nears expiry.

The user authenticates once and reaches every cluster. `muster auth status` shows `[SSO: Exchanged]` next to each remote server.

## Set up the remote identity provider

Each remote cluster's Dex needs a connector that trusts the central cluster's Dex. The connector's ID is the `connectorId` you reference from the `MCPServer`. This is the trust anchor: without it, the remote Dex rejects the exchange. Configure it through the remote cluster's usual GitOps pipeline.

## Create the token-exchange credentials

The exchange authenticates to the remote Dex as a confidential client. Create a secret per remote cluster holding that client's credentials, in the namespace where Muster runs:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: cluster-a-token-exchange-credentials
  namespace: muster
type: Opaque
stringData:
  client-id: muster-token-exchange
  client-secret: <secret-value>
```

The keys default to `client-id` and `client-secret`. Register a matching client on the remote Dex.

## Wire it on the MCPServer

Reference the secret from each remote server's `auth.tokenExchange` block. The full family wiring lives in [multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}#cross-cluster-single-sign-on-with-token-exchange). The exchange-specific fields are:

```yaml
spec:
  auth:
    type: oauth
    tokenExchange:
      enabled: true
      dexTokenEndpoint: "https://dex.cluster-a.<base-domain>/token"
      connectorId: "central-dex"
      clientCredentialsSecretRef:
        name: cluster-a-token-exchange-credentials
```

- `dexTokenEndpoint`: the remote Dex token endpoint. It can differ from the issuer when access goes through a proxy.
- `expectedIssuer`: set this to the remote Dex issuer when the endpoint differs from it. Otherwise Muster derives the issuer from the endpoint.
- `connectorId`: the connector on the remote Dex that trusts the central one.
- `scopes`: defaults to `openid profile email groups`. For a token the remote Kubernetes API accepts, the exchanged token needs the right audience. Add the Dex cross-client scope, such as `audience:server:client_id:dex-k8s-authenticator`, so the audience isn't the exchange client alone.

One secret per cluster covers both that cluster's `mcp-kubernetes` and `mcp-prometheus`, so reuse it across the family members.

## Grant kubeconfig access on each cluster

Token exchange gets a user authenticated to a remote cluster, but `mcp-kubernetes` still needs the kubeconfig for the clusters it serves. It reads those from Kubernetes secrets in the organization namespaces on each management cluster, so its service account needs `get` on secrets there.

An interim approach grants cluster-wide secret access. Per-namespace RBAC automation is the longer-term direction. If you run the central Muster's own token broker against target secrets in other namespaces, the application chart's `rbac.additionalSecretNamespaces` adds a `Role` and `RoleBinding` granting `get` on secrets in each listed namespace.

## Operational notes

- **Large tokens overflow ingress buffers.** Tokens that carry many group claims can exceed the default nginx header buffer on the `mcp-kubernetes` ingress. Raise `large_client_header_buffers`, as the [OAuth setup]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}) guide describes.
- **A remote cluster can fail on its own.** A single cluster reporting `Disconnected` doesn't take the fleet down. Other clusters keep working while you fix the one. See [troubleshooting]({{< relref "/tutorials/ai-agents/troubleshooting" >}}#a-cluster-shows-as-disconnected).

## Related

- [Multi-cluster access]({{< relref "/tutorials/ai-agents/multi-cluster-access" >}}): the `MCPServer` family and instance-selection contract.
- [Deploy Muster]({{< relref "/tutorials/ai-agents/self-hosting/deploy-muster" >}}): install the central aggregator.
- [Set up OAuth]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}): the central single sign-on this exchange extends.
- [Map RBAC and SSO]({{< relref "/tutorials/ai-agents/access-control" >}}): how identity maps to cluster permissions.
