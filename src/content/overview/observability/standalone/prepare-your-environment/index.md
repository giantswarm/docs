---
title: Prepare your environment for the standalone Observability Platform
linkTitle: Prepare your environment
diataxis_content_type: reference
description: Kubernetes cluster, network, and object storage requirements for the standalone Giant Swarm Observability Platform.
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
  - What do I need before I install the standalone Observability Platform?
  - What does the standalone Observability Platform need to run in my cluster?
  - Which object storage does the standalone Observability Platform support?
  - Which network endpoints does the standalone Observability Platform need to reach?
  - How big a cluster does the standalone Observability Platform need?
---

The standalone Observability Platform runs Mimir, Loki, Tempo, and Grafana in a Kubernetes cluster you own. It stores all data in object storage you own.

This page lists what the cluster and the object storage need before the install. Each requirement links to a setup guide in the [observability-platform repository](https://github.com/giantswarm/observability-platform).

## Responsibility boundary

The diagram shows what you provide in blue, the Giant Swarm Observability Platform in orange, and the network paths between them.

<!-- vale off -->
{{< mermaid >}}
%%{init: {"themeCSS": ".edgeLabel, .edgeLabel p, .edgeLabel rect { background-color: transparent !important; fill: none !important; color: #000 !important; } .edgeLabel foreignObject { overflow: visible; } .edgeLabel foreignObject div { transform: translateY(-11px); } [id*=L_grafana_operator] path, [id*=L_api_operator] path, path[id*=L_grafana_operator], path[id*=L_api_operator] { marker-end: none !important; }"}}%%
flowchart LR
  clients["External clients<br/>(agents, collectors, users)"]
  registries["Giant Swarm Registries<br/>gsoci.azurecr.io<br/>docker.io"]

  subgraph customer["Customer-provided"]
    dns["DNS record<br/>observability.#lt;domain#gt;"]
    oidc["OIDC issuer<br/>(JWKS URI)"]
    storage["Object storage<br/>(Amazon S3, Azure Blob Storage)"]
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

- **Kubernetes cluster**: a conformant cluster that can host the Observability Platform. Any managed or self-managed distribution works. Giant Swarm has verified the platform on Kubernetes 1.36 and Amazon EKS 1.36.
- **Release namespace `monitoring`**. The platform installs into the `monitoring` namespace only.

### Access and tools

- **`cluster-admin`** on the Kubernetes cluster. The install creates custom resource definitions and cluster-wide RBAC.
- **[`kubectl`](https://kubernetes.io/docs/tasks/tools/)** and **[`helm`](https://helm.sh/docs/intro/install/)**, pointed at the right cluster.

### Cluster capacity

The platform ships one sizing profile, tuned for a small cluster. These values are the minimum cluster size.

- **Nodes**: 3, one per availability zone.
- **CPU**: 4 vCPU per node, 12 vCPU in total.
- **Memory**: 16 GiB per node, 48 GiB in total.
- **Node disk**: 50 GiB per node.

At rest, the platform requests 5.2 vCPU and 36.9 GiB of memory. The remaining capacity absorbs ingest and query load.

### Cluster add-ons

- **Default StorageClass** backed by a working CSI driver. Mimir, Loki, and Tempo store data on persistent volumes. Use `volumeBindingMode: WaitForFirstConsumer` on a multi-zone cluster. A volume then lands in the zone of the pod that uses it. See [EKS_CLUSTER.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EKS_CLUSTER.md) and [Provider guidance](#provider-guidance).
- **Metrics server**. The platform scales Mimir and Loki components with HorizontalPodAutoscalers. These need the `metrics.k8s.io` API. If it's missing, install [metrics-server](https://github.com/kubernetes-sigs/metrics-server). See [EKS_CLUSTER.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EKS_CLUSTER.md).
- **DNS service**. Mimir discovers its components through the cluster DNS service. The chart expects a Service named `kube-dns` in `kube-system`. On a cluster where the Service has another name, set `mimir.global.dnsService` to that name.

Check that a default StorageClass exists. One class must show `(default)` next to its name:

```sh
kubectl get storageclass
```

Check that the metrics API serves. The command prints CPU and memory per node:

```sh
kubectl top nodes
```

Check that each HorizontalPodAutoscaler reads its metrics after the install. No target must show `<unknown>`:

```sh
kubectl get hpa -n monitoring
```

### Network access

Allow egress to these hosts from the cluster nodes. See the [observability-platform README](https://github.com/giantswarm/observability-platform/blob/main/README.md).

- **`gsoci.azurecr.io`**, for container images.
- **`docker.io`**, for container images.
- **`giantswarm.github.io/giantswarm-catalog`**, for Helm charts.
- **`giantswarm.github.io/control-plane-catalog`**, for Helm charts.
- **Object storage endpoint**, over HTTPS on port 443. Mimir, Loki, and Tempo reach it.
- **OIDC issuer JWKS URI**, over HTTPS, with the [External API](#external-api-optional) enabled. The Envoy Gateway pods fetch it.

A registry cache or proxy in front of these hosts works too.

### Object storage

The platform supports Amazon S3 and Azure Blob Storage. See [OBJECT_STORAGE.md](https://github.com/giantswarm/observability-platform/blob/main/doc/OBJECT_STORAGE.md).

- **Buckets**: five private buckets. On Azure Blob Storage, a bucket is a container in a storage account.
    - `mimir-blocks`, for metrics.
    - `mimir-alertmanager`, for Alertmanager state.
    - `mimir-ruler`, for recording and alerting rules.
    - `loki`, for logs.
    - `tempo`, for traces.
- **Bucket names**: you can pick other names. Set them under `global.objectStorage.buckets` at install time.
- **Public access**: disabled.
- **Transport**: HTTPS only.
- **Minimum TLS version**: 1.2.
- **Redundancy**: zone-redundant, if your data needs to survive a zone outage.
- **Credentials** with read and write access to the five buckets.

### Release namespace, Secret, and Helm values

The platform reads object storage settings from two places:

- **Secret**: holds the credentials.
- **Helm values** under `global.objectStorage`: hold the account and bucket names.

Inside the `monitoring` namespace, in which the platform lives:

- **Secret name**: `observability-platform-object-storage`. Keep the name and the key names exactly as written.
- **Secret key on Azure Blob Storage**: `AZURE_STORAGE_KEY`, holding the storage account key.

Example for Azure Blob Storage:

```sh
kubectl create secret generic observability-platform-object-storage \
  --namespace monitoring \
  --from-literal=AZURE_STORAGE_KEY=<storage-account-key>
```

**Warning**: Static credentials are long-lived. Rotate them in your object storage service, then update the Secret and restart the Mimir, Loki, and Tempo pods.

Set the account and bucket names in your values file. Example for Azure Blob Storage:

```yaml
global:
  objectStorage:
    azure:
      accountName: <storage-account>
    buckets:
      mimirBlocks: mimir-blocks
      mimirAlertmanager: mimir-alertmanager
      mimirRuler: mimir-ruler
      loki: loki
      tempo: tempo
```

The bucket names above are the defaults. With these names, only `accountName` is required.

### Grafana access

The chart creates no Ingress and no TLS certificate for Grafana. Exposing Grafana to your users is your responsibility. Giant Swarm recommends it. Without it, users reach Grafana through `kubectl port-forward` only. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).

- **Ingress controller or Gateway API implementation**.
- **DNS name** for Grafana.
- **TLS certificate** for that name.

### External API (optional)

The Observability Platform API accepts metrics, logs, and traces from outside the cluster. It's disabled by default. Without it, the platform observes only the cluster it runs in. Enable it when agents, collectors, or users outside the cluster send or query data. See [EXTERNAL_API.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EXTERNAL_API.md).

- **[Envoy Gateway](https://gateway.envoyproxy.io/)** installed in the cluster. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **Gateway with an HTTPS listener** that accepts routes from the `monitoring` namespace. Set `parentRefs` on every API component (`loki`, `mimir`, `tempo`, and `basicAuth`) to that Gateway and listener. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **Base domain**. The API answers at `observability.<domain>`.
- **DNS record** for `observability.<domain>`, pointing at the Gateway. See [GATEWAY.md](https://github.com/giantswarm/observability-platform/blob/main/doc/GATEWAY.md).
- **OIDC issuer**, at least one. Every request carries a JWT from that issuer.
- **Tenant header**. Every request carries an `X-Scope-OrgID` header with the tenant name.

## Provider guidance {#provider-guidance}

{{< tabs >}}
{{< tab title="Amazon EKS" active="true" >}}

See [EKS_CLUSTER.md](https://github.com/giantswarm/observability-platform/blob/main/doc/EKS_CLUSTER.md).

- **Nodes**: 3 × `m6i.xlarge` or `t3.xlarge`, one per availability zone.
- **CSI driver**: install the `aws-ebs-csi-driver` add-on. Its IAM role needs the `AmazonEBSCSIDriverPolicy` policy.
- **StorageClass**: create a `gp3` class with provisioner `ebs.csi.aws.com` and mark it as default. The built-in `gp2` class isn't the default on EKS 1.30 and later.
- **Metrics server**: install the `metrics-server` add-on.
- **DNS service**: `kube-dns`. No change needed.

Create the `gp3` StorageClass:

```sh
kubectl apply -f - <<'EOF'
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: gp3
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: ebs.csi.aws.com
parameters:
  type: gp3
  encrypted: "true"
volumeBindingMode: WaitForFirstConsumer
allowVolumeExpansion: true
EOF
```

{{< /tab >}}
{{< tab title="Azure AKS" >}}

- **Nodes**: 3 × `Standard_D4s_v5`, spread over zones 1, 2, and 3.
- **CSI driver**: the Azure Disk CSI driver ships with AKS. No change needed.
- **StorageClass**: the built-in `default` class is the default. It uses zone-redundant Standard SSD (`StandardSSD_ZRS`) with `WaitForFirstConsumer`. Use `managed-csi-premium` for Premium SSD.
- **Metrics server**: ships with AKS. No change needed.
- **DNS service**: `kube-dns`. No change needed.

Create a node pool across three zones:

```sh
az aks nodepool add \
  --resource-group <resource-group> \
  --cluster-name <cluster> \
  --name observability \
  --node-count 3 \
  --node-vm-size Standard_D4s_v5 \
  --zones 1 2 3
```

{{< /tab >}}
{{< /tabs >}}

## Known limitations

- **Grafana client certificate**: Grafana organizations, datasources, and dashboards need a Grafana client certificate Secret named `grafana-tls` in `monitoring`. The chart doesn't provide it yet. Until it does, these resources aren't reconciled.

## Next steps

Install the platform with the [observability-platform chart](https://github.com/giantswarm/observability-platform).

If you need help with the setup, contact your Giant Swarm account engineer. For sharing any secret with us, read [Sharing secrets with our team]({{< relref "/overview/security/sharing-secrets" >}}) first.
