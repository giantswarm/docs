---
title: Prepare your environment for the standalone observability platform
linkTitle: Prepare your environment
diataxis_content_type: reference
description: The infrastructure you provide before you install the standalone observability platform, from the Kubernetes cluster and object storage to the Gateway, OIDC issuer, and network access.
weight: 10
mermaid: true
menu:
  principal:
    identifier: overview-observability-standalone-prepare-your-environment
    parent: overview-observability-standalone
last_review_date: 2026-10-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What do I need before I install the standalone observability platform?
  - Which object storage does the standalone observability platform support?
  - Does the standalone observability platform support S3?
  - What does the observability-platform chart install, and what do I provide?
  - Which network endpoints does the standalone observability platform need to reach?
  - How big a cluster does the standalone observability platform need?
---

The standalone observability platform runs on your own Kubernetes cluster. One Helm chart installs Mimir, Loki, Tempo, Grafana, the observability-operator, and the observability platform API. You provide the infrastructure around it.

This page lists that infrastructure. Each requirement links to a setup guide in the [observability-platform repository](https://github.com/giantswarm/observability-platform).

## Responsibility boundary

The diagram shows what you provide in blue, the Giant Swarm Observability Platform in orange, and the network paths between them.

<!-- vale off -->
{{< mermaid >}}
---
config:
  layout: dagre
---
%%{init: {"themeCSS": ".edgeLabel, .edgeLabel p, .edgeLabel rect { background-color: transparent !important; fill: none !important; color: #000 !important; } .edgeLabel foreignObject { overflow: visible; } .edgeLabel foreignObject div { transform: translateY(-11px); } [id*=L_grafana_operator] path, [id*=L_api_operator] path, path[id*=L_grafana_operator], path[id*=L_api_operator] { marker-end: none !important; }"}}%%
flowchart LR
  clients["External clients<br/>(agents, collectors, users)"]
  registries["Giant Swarm Registries<br/>gsoci.azurecr.io<br/>docker.io"]

  subgraph customer["Customer-provided"]
    dns["DNS record<br/>observability.#lt;domain#gt;"]
    oidc["OIDC issuer<br/>(JWKS URI)"]
    storage["Object storage<br/>(Azure Blob Storage)"]
    subgraph cluster["Kubernetes cluster"]
      gateway["Envoy Gateway<br/>HTTPS listener, TLS certificate"]
      subgraph chart["Giant Swarm Observability Platform<br/>(monitoring namespace)"]
        grafana["Grafana"]
        hl["Grafana"]
        api["observability-platform-api"]
        operator["observability-operator"]
        spacer["Mimir, Loki, Tempo"]
        backends["Mimir, Loki, Tempo"]
      end
    end
  end

  clients -- "HTTPS" --> dns
  dns --> gateway
  gateway -- "Grafana Route" --> grafana
  gateway -- "Ingest and Query" --> api
  gateway -- "JWKS Fetch" --> oidc
  grafana <--> operator
  api <--> operator
  operator --> backends
  api --> backends
  backends -- "Object Storage Egress" --> storage
  backends ~~~ registries
  operator ~~~ spacer
  gateway ~~~ hl
  hl ~~~ operator
  spacer ~~~ oidc
  cluster -- "Image and Chart Pulls" --> registries

  classDef customerNode fill:#bfdbfe,stroke:#2563eb,color:#1e3a8a
  classDef gsNode fill:#F17130,stroke:#c4571f,color:#ffffff
  classDef hidden fill:none,stroke:none,color:transparent
  class dns,oidc,storage,gateway customerNode
  class api,backends,grafana,operator,registries gsNode
  class spacer,hl hidden
  style customer fill:#eff6ff,stroke:#2563eb,color:#1e3a8a
  style cluster fill:#dbeafe,stroke:#2563eb,color:#1e3a8a
  style chart fill:#fde3d6,stroke:#F17130,color:#7c2d12
{{< /mermaid >}}
<!-- vale on -->

## Requirements

### Kubernetes cluster

- **Default StorageClass** with dynamic provisioning. Mimir, Loki, and Tempo store data on persistent volumes. See [EKS_CLUSTER.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EKS_CLUSTER.md).
- **metrics-server**. The Loki, Mimir, and Tempo HorizontalPodAutoscalers read from the metrics API. Without it, they stay at their minimum replicas. See [EKS_CLUSTER.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EKS_CLUSTER.md).
- **Release namespace `monitoring`**. The chart installs into `monitoring` only. The render fails in any other namespace.

### Object storage

Azure Blob Storage is the supported backend. S3 and S3-compatible storage are coming soon, tracked in [giantswarm/giantswarm#38467](https://github.com/giantswarm/giantswarm/issues/38467). See [OBJECT_STORAGE.md](https://github.com/giantswarm/observability-platform/blob/main/doc/OBJECT_STORAGE.md).

- **Storage account**: `StorageV2`, `Standard_LRS` (default) or `Standard_ZRS`, `Hot` access tier, minimum TLS 1.2, HTTPS only, blob public access disabled, shared key access enabled.
- **Containers**: `mimir-blocks`, `mimir-alertmanager`, `mimir-ruler`, `loki`, and `tempo`.
- **Secret**: `observability-platform-object-storage` in the `monitoring` namespace, with the account key under the key `AZURE_STORAGE_KEY`.

### Gateway

- **Envoy Gateway**. It brings the Gateway API CRDs. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **Gateway with an HTTPS listener** named `https`, for `observability.<domain>`. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **DNS record** for `observability.<domain>`, pointing to the Gateway load balancer. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **TLS certificate**: cert-manager with `--enable-gateway-api`, or a `kubernetes.io/tls` Secret. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).

### OIDC issuer

- **Issuer URL** and **JWKS URI**. The observability platform API validates every request's JWT against the issuer. Envoy fetches the JWKS, so the JWKS URI must be reachable from the Envoy pods. See [EXTERNAL_API.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EXTERNAL_API.md).

### Grafana exposure

- **Route and TLS for Grafana**. The chart creates no ingress and no certificate for Grafana. You attach the Grafana route to your Gateway's HTTPS listener. See [EXTERNAL_API.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EXTERNAL_API.md).

### Network access

The cluster reaches these endpoints. See the [observability-platform README](https://github.com/giantswarm/observability-platform/blob/main/README.md).

- The object storage endpoint, for example `https://<account>.blob.core.windows.net`.
- The OIDC JWKS URI.
- `gsoci.azurecr.io`, for container images and charts.
- `docker.io`, for container images.
- The Giant Swarm Helm catalogs.

## Validated reference setup

Giant Swarm validates the platform on the setup below. The values are examples, not minimums.

{{< tabs >}}
{{< tab title="EKS" active="true" >}}

- EKS 1.36.
- Three `t3.xlarge` nodes across three availability zones.
- `gp3` default StorageClass with `volumeBindingMode: WaitForFirstConsumer`.
- Measured platform requests: 4.2 vCPU and 26.4 GiB memory across 29 pods.

{{< /tab >}}
{{< /tabs >}}

## Next steps

With your environment ready, install the platform with the [observability-platform chart](https://github.com/giantswarm/observability-platform).
