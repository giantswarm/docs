---
title: Deploy Muster
linkTitle: Deploy Muster
description: Install the CRD and application Helm charts for Muster on a management cluster, and run the aggregator in custom-resource discovery mode.
weight: 70
menu:
  principal:
    parent: tutorials-ai-agents-self-hosting
    identifier: tutorials-ai-agents-deploy-muster
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
last_review_date: 2026-06-20
user_questions:
  - How do I deploy Muster on a management cluster?
  - Which Helm charts does Muster need?
  - How does Muster read MCPServer and Workflow resources?
---

{{% notice note %}}
**Applies to self-hosted Muster only.** Follow this guide when you operate your own Muster. On the managed Giant Swarm platform, Muster is already deployed for you.
{{% /notice %}}

Muster ships as two Helm charts: `muster-crds`, which installs the `MCPServer` and `Workflow` CustomResourceDefinitions, and `muster`, which runs the aggregator itself. This guide installs both and explains the custom-resource discovery mode the aggregator runs in on a cluster.

For the concepts behind the aggregator, see the [architecture overview]({{< relref "/overview/ai-agents/architecture" >}}). To protect the deployed endpoint with single sign-on, continue to [set up OAuth]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}).

## Prerequisites

- A management cluster you can deploy to, with the Giant Swarm app platform or Helm available.
- An ingress controller or Gateway API implementation to expose the aggregator. Production OAuth needs HTTPS.
- An OIDC provider (Dex on a Giant Swarm cluster) if you plan to protect the endpoint, covered in [OAuth setup]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}).

## Install the CRDs first

The application chart no longer renders the CRDs. It expects them to exist, so always reconcile `muster-crds` before `muster`. Installing the application first risks the reconciler starting against missing or stale CRDs.

```bash
helm upgrade --install muster-crds \
  oci://gsoci.azurecr.io/giantswarm/muster-crds \
  --namespace muster --create-namespace
```

The CRDs carry `helm.sh/resource-policy: keep`, so a later `helm uninstall muster-crds` leaves them, and every `MCPServer` and `Workflow` resource, in place. Removing them is a deliberate, destructive step that also deletes the dependent resources.

## Install the application

```bash
helm upgrade --install muster \
  oci://gsoci.azurecr.io/giantswarm/muster \
  --namespace muster
```

The image comes from `gsoci.azurecr.io/giantswarm/muster`. On a Giant Swarm management cluster, deploy both charts through the app platform with an `App` resource managed by your GitOps pipeline, rather than running Helm by hand. The ordering rule is the same: the CRD chart lands first.

## How the aggregator finds resources

The chart renders a `config.yaml` and runs `muster serve --config-path=/etc/muster`. Two settings drive discovery:

```yaml
namespace: muster
kubernetes: true
```

With `kubernetes: true`, the aggregator watches the cluster for `MCPServer` and `Workflow` resources in `namespace` and reconciles them live. You add a downstream server by applying an [`MCPServer`]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}) resource, and a workflow by applying a [`Workflow`]({{< relref "/tutorials/ai-agents/authoring-workflows" >}}). No restart is needed. `namespace` defaults to the release namespace, so this configuration watches the `muster` namespace.

## Configure the aggregator endpoint

The aggregator's HTTP server is configured under `muster.aggregator` in the values:

```yaml
muster:
  aggregator:
    port: 8090
    transport: "streamable-http"
```

- `port`: the port the aggregator listens on. The chart's `Service` targets the same port.
- `transport`: the MCP transport. `streamable-http` is the default and the right choice for remote clients. `sse` is also supported.

The aggregator binds to `0.0.0.0` inside the pod and serves the MCP endpoint at `/mcp` and a health check at `/health`.

## Expose the endpoint

By default the `Service` is `ClusterIP` and the aggregator is reachable only inside the cluster. To let IDEs and the developer portal connect, expose it with either Ingress or Gateway API.

```yaml
ingress:
  enabled: true
  className: "nginx"
  hosts:
    - host: muster.<management-cluster>.<base-domain>
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: muster-tls
      hosts:
        - muster.<management-cluster>.<base-domain>
```

For Gateway API, set `gatewayAPI.enabled: true` with a `parentRefs` entry and `hostnames`. On Envoy Gateway, also enable `gatewayAPI.backendTrafficPolicy` with `timeout: "0s"`, because the default fifteen-second backend timeout kills the long-lived streaming connections MCP relies on.

Tokens from enterprise single sign-on can carry many group claims and overflow the default ingress header buffers. Raise `large_client_header_buffers` on the ingress that fronts Muster. The [OAuth setup]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}) guide covers the symptom and fix.

## Verify the deployment

```bash
kubectl get pods -n muster
kubectl logs -n muster -l app.kubernetes.io/name=muster -f
```

Once the pod is ready, check the health endpoint through a port-forward:

```bash
kubectl port-forward -n muster svc/muster 8090:8090
curl http://localhost:8090/health
```

A protected deployment rejects unauthenticated MCP calls, which is expected. The `/health` endpoint stays open so probes and load balancers can reach it.

## Next steps

- [Set up OAuth]({{< relref "/tutorials/ai-agents/self-hosting/oauth-setup" >}}): protect the endpoint and proxy authentication to downstream servers.
- [Manage MCP servers]({{< relref "/tutorials/ai-agents/managing-mcp-servers" >}}): register the downstream servers Muster aggregates.
- [Multi-cluster token exchange]({{< relref "/tutorials/ai-agents/self-hosting/multi-mc-token-exchange" >}}): bridge single sign-on to remote management clusters.
