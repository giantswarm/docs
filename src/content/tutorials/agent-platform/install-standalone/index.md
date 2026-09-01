---
title: Install the Agent Platform on your own cluster
diataxis_content_type: how-to-guide
linkTitle: Install standalone
description: Install the whole Agent Platform with one Helm chart on any conformant Kubernetes cluster, wire it to your OIDC identity provider, and verify the install.
weight: 65
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-install-standalone
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-08-31
user_questions:
  - How do I install the Agent Platform on my own cluster?
  - Why does the Agent Platform chart require Helm 4?
  - What goes into the agent-platform-idp secret?
  - How do I upgrade the Agent Platform's CRDs?
---

The [`agent-platform-standalone`](https://github.com/giantswarm/agent-platform-standalone) Helm chart installs the whole Agent Platform—Muster, agentgateway, the agent runtime, the developer portal, and their supporting services—on any conformant Kubernetes cluster with a plain `helm install`. No GitOps controller is required.

This guide is the whole-platform track. If you only want the MCP gateway without the runtime and portal, follow [Self-hosting Muster]({{< relref "/tutorials/agent-platform/self-hosting" >}}) instead.

## Prerequisites

- A conformant Kubernetes cluster. The chart's defaults deliberately need nothing outside Kubernetes conformance.
- **Helm 4.** This is a hard requirement for `helm install`: under Helm 3 the chart's dependency archives alone exceed the 1 MiB cap on the Helm release Secret, so Helm 3 can't store the release at all. Rendering and linting work on both majors—only the install needs Helm 4.
- The [Gateway API](https://gateway-api.sigs.k8s.io/) v1 CRDs plus an implementation. If your cluster already runs a public Gateway, the platform's routes attach to it. If not, the chart's own agentgateway can act as the TLS edge.
- An OIDC identity provider, with a client registered for the platform (see below).
- DNS for `*.<your domain>` pointing at the Gateway, and a TLS certificate for that wildcard. TLS and DNS stay outside the chart.

## Register the OAuth client

The platform uses one OIDC client, shared by its surfaces. Register a confidential client (for example, named `agent-platform`) at your identity provider with these redirect URIs—hostnames derive from your domain:

| Surface | Redirect URI |
|---|---|
| Muster | `https://muster.<domain>/oauth/callback` |
| Developer portal | `https://backstage.<domain>/api/auth/oidc-agent-platform/handler/frame` |
| Agent runtime UI | `https://kagent.<domain>/oauth2/callback` |

## Create the identity secret

The chart reads all sensitive values from one Secret in the release namespace, named by `global.identity.existingSecret` (default `agent-platform-idp`):

| Key | Purpose |
|---|---|
| `dex-client-secret` | The OAuth client secret of the platform's client at your identity provider |
| `registration-token` | Bearer token MCP clients present to Muster's dynamic client registration endpoint |
| `oauth-encryption-key` | Encrypts Muster's stored tokens at rest (`openssl rand -base64 32`) |
| `valkey-password` | Shared by Muster and the bundled Valkey session store |
| `backstage-session-secret` | The developer portal's cookie signing key |

```sh
kubectl create namespace agent-platform
kubectl -n agent-platform create secret generic agent-platform-idp \
  --from-literal=dex-client-secret=<client secret> \
  --from-literal=registration-token=$(openssl rand -base64 32) \
  --from-literal=oauth-encryption-key=$(openssl rand -base64 32) \
  --from-literal=valkey-password=$(openssl rand -base64 32) \
  --from-literal=backstage-session-secret=$(openssl rand -base64 32)
```

If your identity provider serves a certificate from a private CA, also create a Secret holding that CA (key `ca.crt`) and reference it via `global.identity.ca.secretName`.

## Write your values

The chart's input contract is small: a domain, an identity provider, a public Gateway, and the component toggles.

```yaml
global:
  domain: agents.example.com
  identity:
    issuerUrl: https://your-idp.example.com
    clientId: agent-platform
    existingSecret: agent-platform-idp
  gatewayApi:
    # Your cluster's existing public Gateway. Alternatively, let the chart's
    # agentgateway be the TLS edge - see below.
    parentRefs:
      - name: public-gateway
        namespace: gateway-system

# The platform topology: client -> agentgateway /mcp -> Muster.
ingress:
  mode: agentgateway-muster

components:
  muster:
    enabled: true
  valkey:
    enabled: true
  agentgateway:
    enabled: true
  agent-platform-mcps:
    enabled: true
  kagent:
    enabled: true
    controllerRoute:
      enabled: true
  backstage:
    enabled: true

agent-platform-mcps:
  agentgateway:
    viaMuster: true

# The Muster chart reads its own OIDC keys; they must match global.identity
# (the render fails otherwise).
muster:
  muster:
    oauth:
      server:
        baseUrl: https://muster.agents.example.com
        dex:
          issuerUrl: https://your-idp.example.com
          clientId: agent-platform
        existingSecret: agent-platform-idp
        # Accept ID tokens carrying the cross-client audience the developer
        # portal requests by default (Dex-specific; see the note below).
        trustedAudiences:
          - dex-k8s-authenticator

valkey:
  valkey:
    auth:
      usersExistingSecret: agent-platform-idp
      aclUsers:
        default:
          # The ACL init reads each user's password from the key this names;
          # the identity secret carries no key named `default`.
          passwordKey: valkey-password
```

Two variations worth knowing:

- **No existing Gateway?** Drop `global.gatewayApi.parentRefs` and set `gatewayApi.gateway.create: true` plus `gatewayApi.gateway.tls.secretName: <your wildcard certificate Secret>`. The chart's agentgateway then terminates TLS itself and exposes a `LoadBalancer` Service.
- **Identity providers other than Dex.** The `trustedAudiences` entry and the portal's default extra scopes are Dex's cross-client mechanism. On providers that reject unknown scopes (Keycloak, Entra ID), set `components.backstage.extraScopes: []` and omit `trustedAudiences`.

Every component is toggled with `components.<name>.enabled`; the full knob list is in the chart's [values file](https://github.com/giantswarm/agent-platform-standalone/blob/main/helm/agent-platform-standalone/values.yaml), which documents each key in place.

## Install

The published chart package includes its dependencies, so a single command installs the platform:

```sh
helm install agent-platform \
  oci://gsoci.azurecr.io/charts/giantswarm/agent-platform-standalone \
  --namespace agent-platform --create-namespace \
  -f values.yaml
```

## Verify

First, every Deployment in the release namespace (and the agent runtime namespace) becomes ready:

```sh
kubectl -n agent-platform get deployments
kubectl -n kagent get deployments
```

Then confirm the platform's front door behaves like an OAuth resource server. An unauthenticated request to the MCP endpoint must return `401` *with* a `WWW-Authenticate` header carrying the discovery pointer—that header is how MCP clients find your identity provider, so its presence is the real health check:

```sh
curl -si -X POST https://muster.<domain>/mcp | grep -i www-authenticate
```

Expect `resource_metadata="https://muster.<domain>/.well-known/oauth-protected-resource"` in the response. Now point an MCP client at `https://muster.<domain>/mcp` and sign in.

One first-install wrinkle: the developer portal probes the identity provider for a short window at startup and then serves `503` until restarted. If the portal doesn't come up although everything else is ready, run `kubectl -n agent-platform rollout restart deployment backstage`.

## Upgrades

Three things to know before your first `helm upgrade`:

- **CRDs.** Helm installs CRDs but never upgrades them. Before upgrading to a release that bumps a component, apply the new chart's CRDs first—one line, harmless for unchanged CRDs:

  ```sh
  helm show crds oci://gsoci.azurecr.io/charts/giantswarm/agent-platform-standalone | kubectl apply --server-side -f -
  ```

- **PostgreSQL needs two revisions.** The agent runtime uses a bundled single-container PostgreSQL by default (demo grade). For a real database, enable `components.cloudnative-pg.enabled: true` first, then set `postgres.enabled: true` in a second `helm upgrade`: the operator's CRDs must exist before the `Cluster` resource can be rendered.
- **Kyverno fail-closed.** On a cluster whose Kyverno admission fails closed, a first install can be rejected before Kyverno has loaded the policies this release ships. Running `helm upgrade` once more resolves it.

## Related

- [Self-hosting Muster]({{< relref "/tutorials/agent-platform/self-hosting" >}}) - The gateway-only track.
- [Agent Platform architecture]({{< relref "/overview/agent-platform/architecture" >}}) - What you just installed.
- [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) - Connect your IDE to the new endpoint.
