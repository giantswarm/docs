---
title: Install the Agent Platform on your own cluster
diataxis_content_type: how-to-guide
linkTitle: Install on your own cluster
description: Install the whole Agent Platform with one Helm chart on any conformant Kubernetes cluster, wire it to your OIDC identity provider, and operate it from day two on.
weight: 65
menu:
  principal:
    parent: tutorials-agent-platform
    identifier: tutorials-agent-platform-install
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-09-08
user_questions:
  - How do I install the Agent Platform on my own cluster?
  - Why does the Agent Platform chart need Helm 4?
  - What goes into the agent-platform-idp secret?
  - How do I change the Agent Platform's values after the install?
  - How do I install the Agent Platform on a cluster that already runs Flux?
  - How do I uninstall the Agent Platform?
aliases:
  - /tutorials/agent-platform/install-standalone/
---

The [`agent-platform`](https://github.com/giantswarm/agent-platform) Helm chart installs the whole Agent Platform on any conformant Kubernetes cluster with one `helm install`. That's Muster, agentgateway, the agent runtime, the developer portal, and their supporting services. The chart is an app-of-apps. It renders one Flux `HelmRelease` per component and brings the Flux engine that reconciles them where the cluster has none, so you don't need a GitOps controller first. On a cluster that already runs Flux, you install the same chart through that Flux instead (see [Clusters that run Flux](#clusters-that-run-flux)).

This guide is the whole-platform track. If you only want the MCP gateway without the runtime and portal, follow [Self-hosting Muster]({{< relref "/tutorials/agent-platform/self-hosting" >}}) instead.

## Prerequisites

- A conformant Kubernetes cluster, version 1.33 or later.
- **Helm 4.** Its `--wait` waits on the component `HelmRelease` resources, so `helm install --wait` returns when the platform runs. Helm 3 renders the chart, but its `--wait` returns before the components are ready, and the install isn't verified with it.
- The [Gateway API](https://gateway-api.sigs.k8s.io/) v1 CRDs. This is the one cluster prerequisite the chart doesn't bring; the install step below applies them. If your cluster already runs a public Gateway, the platform's routes attach to it. If not, the chart's own agentgateway can act as the TLS edge.
- An OIDC identity provider, with a client registered for the platform (see below).
- DNS for `*.<your domain>` pointing at the Gateway, and a TLS certificate for that wildcard. TLS and DNS stay outside the chart.
- Flux is optional. Without it, the chart brings its own engine (the Flux Operator with one `FluxInstance` running source-controller and helm-controller). It refuses to install that engine next to a Flux the cluster already runs; use the [Flux path](#clusters-that-run-flux) there.

## Register the OAuth client

The platform uses one OIDC client, shared by its surfaces. Register a confidential client (for example, named `agent-platform`) at your identity provider with these redirect URIs—hostnames derive from your domain:

| Surface | Redirect URI |
|---|---|
| Muster | `https://muster.<domain>/oauth/callback` |
| Developer portal | `https://backstage.<domain>/api/auth/oidc-agent-platform/handler/frame` |
| Agent runtime UI (if you expose it) | `https://kagent.<domain>/oauth2/callback` |

## Create the identity secret

The chart reads all sensitive values from one Secret in the release namespace, named by `global.identity.existingSecret`:

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

The chart's input contract is small: a domain, an identity provider, a public Gateway, and the component toggles. Nothing about Flux.

```yaml
global:
  domain: agents.example.com
  identity:
    issuerUrl: https://your-idp.example.com
    clientId: agent-platform
    existingSecret: agent-platform-idp
  gatewayApi:
    # Your cluster's existing public Gateway; every route attaches to it.
    # Alternatively, let the chart's agentgateway be the TLS edge - see below.
    parentRefs:
      - name: public-gateway
        namespace: gateway-system

# The platform topology: client -> agentgateway /mcp -> Muster.
ingress:
  mode: agentgateway-muster

# Pick your components. Muster, the avatar service, and the connectivity
# wiring are always on; everything else is a toggle.
components:
  agentgateway:
    enabled: true
  kagent:
    enabled: true
  agent-manager:
    enabled: true
  backstage:
    enabled: true
  mcp-kubernetes:
    enabled: true

kagent:
  controllerRoute:
    enabled: true  # the portal reaches the agent runtime through this route

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

A few variations worth knowing:

- **No existing Gateway?** Drop `global.gatewayApi.parentRefs` and set `gatewayApi.gateway.create: true` plus `gatewayApi.gateway.tls.secretName: <your wildcard certificate Secret>`. The chart's agentgateway then terminates TLS itself and exposes a `LoadBalancer` Service.
- **No Cilium?** Set `mcp-kubernetes.ciliumNetworkPolicy.enabled: false`. Everything else follows the cluster on its own: the chart detects Kyverno, the network-policy flavor, and the monitoring CRDs at install time and renders only what the cluster serves.
- **Identity providers other than Dex.** The `trustedAudiences` entry and the portal's default extra scopes are Dex's cross-client mechanism. On providers that reject unknown scopes (Keycloak, Entra ID), set `backstage.extraScopes: []`, omit `trustedAudiences`, and set `mcp-kubernetes.kubernetesAudience` to the audience your Kubernetes API server accepts.
- **Want your own model backend?** Turn on `components.model-manager` and point it at an Ollama, Lemonade, LM Studio, or KServe endpoint; the chart's [README](https://github.com/giantswarm/agent-platform#model-manager-and-agent-manager) has the details.

Every component is toggled with `components.<name>.enabled`. The full knob list is in the chart's [values file](https://github.com/giantswarm/agent-platform/blob/main/helm/agent-platform/values.yaml), which documents each key in place.

## Install

Apply the Gateway API CRDs, then install the chart:

```sh
kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.5.0/standard-install.yaml
helm install agent-platform \
  oci://gsoci.azurecr.io/charts/giantswarm/agent-platform \
  --namespace agent-platform --create-namespace \
  -f values.yaml --wait --timeout 10m
```

The command returns when the platform runs: with `--wait`, Helm waits for the component `HelmRelease` resources to become ready, which takes a few minutes with these components. This is the last Helm command you run besides `helm uninstall`. The release manages itself from here on, as described in [Change values and upgrade](#change-values-and-upgrade).

## Verify

First, every `HelmRelease` the chart rendered is ready, and every Deployment in the release namespace (and the agent runtime namespace) becomes ready:

```sh
kubectl -n agent-platform get helmreleases
kubectl -n agent-platform get deployments
kubectl -n kagent get deployments
```

Then confirm the platform's front door behaves like an OAuth resource server. An unauthenticated request to the MCP endpoint must return `401` *with* a `WWW-Authenticate` header carrying the discovery pointer. That header is how MCP clients find your identity provider, so its presence is the real health check:

```sh
curl -si -X POST https://muster.<domain>/mcp | grep -i www-authenticate
```

Expect `resource_metadata="https://muster.<domain>/.well-known/oauth-protected-resource"` in the response. Now point an MCP client at `https://muster.<domain>/mcp` and sign in.

One first-install wrinkle: the developer portal probes the identity provider for a short window at startup and then serves `503` until restarted. If the portal doesn't come up although everything else is ready, run `kubectl -n agent-platform rollout restart deployment backstage`.

## Change values and upgrade

The release manages itself. The engine the chart brought also holds the chart: the release renders its own `OCIRepository` and `HelmRelease`, and the bundled helm-controller adopts the release right after the install. From then on:

- **The chart rolls forward on its own** inside its major version, and every component rolls forward inside its `components.<name>.versionRange`. Component CRDs travel with their component (Flux upgrades them together with the app), and the Flux Operator keeps Flux and its CRDs current, so there is no manual CRD step. To freeze what you run, pin the ranges in your values file; the chart's [`examples/customer-bom.yaml`](https://github.com/giantswarm/agent-platform/blob/main/helm/agent-platform/examples/customer-bom.yaml) shows the shape.
- **`helm upgrade` and `helm rollback` are refused** by an admission policy the chart renders, with the reason in Helm's error output and no release revision written. Change values by rewriting the Secret `agent-platform-values` in the release namespace with your complete values file; helm-controller applies it within seconds:

    ```sh
    kubectl -n agent-platform create secret generic agent-platform-values \
      --from-file=values.yaml=values.yaml --dry-run=client -o yaml \
      | kubectl apply --server-side --force-conflicts -f -
    ```

    The Secret *is* the values of the release, so always write the whole file—a partial file reverts everything it omits to the chart defaults.

- **The next major is a deliberate step.** Set `gitops.self.versionRange` (for example `">=4.0.0 <5.0.0"`) in the values file, read the operator actions in the chart's [UPGRADE.md](https://github.com/giantswarm/agent-platform/blob/main/UPGRADE.md), and rewrite the Secret the same way.

If you'd rather keep the Helm CLI as your day-two tool, set `gitops.self.enabled: false` in the values file before the install and keep it there. `helm upgrade -f values.yaml` then stays the way to change values and to move the chart itself, while the components keep following their version ranges.

## Clusters that run Flux

A cluster that already runs Flux installs the chart through that Flux, with the bundled engine off. Nothing of the engine reaches the cluster, and that Flux holds the chart's `HelmRelease`, so day two is the usual GitOps change to its values. Leaving `components.flux.enabled` at its default on such a cluster fails the render with `this cluster runs Flux; set components.flux.enabled=false or install the chart through it`.

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: agent-platform
  namespace: flux-system
spec:
  interval: 1h
  url: oci://gsoci.azurecr.io/charts/giantswarm/agent-platform
  ref:
    semver: ">=3.0.0 <4.0.0"   # or a pinned tag
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: agent-platform
  namespace: flux-system
spec:
  interval: 10m
  chartRef:
    kind: OCIRepository
    name: agent-platform
  install:
    createNamespace: true
    crds: Skip   # the chart's only CRDs are the engine's, which stays off here
  upgrade:
    crds: Skip
  values:
    components:
      flux:
        enabled: false               # this cluster runs Flux
    gitops:
      namespace: flux-system         # the Flux objects the chart renders land here
      targetNamespace: agent-platform  # the workloads land here
    # ...the rest of your values file
```

## Uninstall

```sh
helm uninstall agent-platform --namespace agent-platform --wait --timeout 5m
```

The chart's pre-delete hooks tear the platform down in order: the platform `HelmRelease` resources first, then the `FluxInstance`, and the Flux Operator removes Flux and its CRDs last. Every `HelmRelease` object in the cluster goes with those CRDs, the agents' included. Their workloads and `Agent` objects stay behind, orphaned, and the `kagent` namespace is kept, so a reinstall finds the agents where it left them. The components' CRDs stay too (Helm never deletes CRDs), and a reinstall is clean. There's no way to uninstall the platform and keep the agents running. To keep the agents, leave the platform installed.

On a cluster that runs its own Flux, delete the `HelmRelease` you created instead, and that Flux uninstalls the release.

## Related

- [Self-hosting Muster]({{< relref "/tutorials/agent-platform/self-hosting" >}}) - The gateway-only track.
- [Agent Platform architecture]({{< relref "/overview/agent-platform/architecture" >}}) - What you just installed.
- [Enable Agent Platform features in Backstage]({{< relref "/tutorials/agent-platform/enable-portal-features" >}}) - The portal side of the configuration.
- [Set up your AI agent]({{< relref "/getting-started/ai-agent-setup" >}}) - Connect your IDE to the new endpoint.
