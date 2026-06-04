---
title: Matching app deployments with metrics
linkTitle: Metrics matching
description: To display metrics about app workloads, we match them via labels and fall back to resource names. On this page you learn in detail how this works and what labels you can apply to enable metrics in the portal.
weight: 50
menu:
  principal:
    parent: overview-developer-portal-deployments
    identifier: overview-developer-portal-deployments-metricsmatching
last_review_date: 2026-03-13
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I need to label workloads so that I see metrics in the developer portal?
---

The developer portal shows deployment data from two sources: Kubernetes custom resources (HelmRelease and App CRs) and Mimir metrics (workload replica counts, CPU/memory usage). This document explains how we match and merge these data sources.

## Matching parameters

To find Mimir metrics for a deployment, we need three identifiers:

| Parameter | Description | Mimir label |
|-----------|-------------|-------------|
| **Cluster name** | The cluster where the workload runs | `cluster_id` |
| **Namespace** | The namespace where the workload pods run | `namespace` |
| **Name prefix** | The name prefix for matching workload names | `deployment`, `statefulset`, `daemonset`, or `pod` |

These are derived differently for HelmRelease and App CRs.

### Cluster name

Identifies *which* cluster the workload runs on. Mimir stores metrics from multiple clusters, distinguished by `cluster_id`.

**HelmRelease CRs:**

- If the HelmRelease has no `spec.kubeConfig`, it targets the management cluster. The cluster name is the installation name (that is, the cluster the CR was fetched from).
- Otherwise, the cluster name comes from the `giantswarm.io/cluster` label.

**App CRs:**

- If `spec.kubeConfig.inCluster` is `true`, or `spec.kubeConfig.secret.name` equals `{installation}-kubeconfig`, the app targets the management cluster. The cluster name is the installation name.
- Otherwise, the cluster name comes from the `giantswarm.io/cluster` label.

### Workload namespace

The namespace where the workload pods actually run. This is **not** the same as the CR's own namespace.

**HelmRelease CRs:**

- `spec.targetNamespace` (the namespace where Helm installs resources)
- Falls back to the CR's own `metadata.namespace`

**App CRs:**

- `spec.namespace` (the target deployment namespace, for example `kube-system`)
- Falls back to the CR's own `metadata.namespace`

For example, an App CR in namespace `org-team-tinkerers` can deploy workloads to `kube-system`.

### Name prefix

The prefix used to match workload names via regex (`prefix.*`).

**HelmRelease CRs:**

- `spec.releaseName` (the Helm release name)
- Falls back to the CR's `metadata.name`

**App CRs:**

- `spec.name` (the Helm chart/release name, for example `cert-manager-app`)
- Falls back to the CR's `metadata.name`

For App CRs, `spec.name` is critical because `metadata.name` is typically prefixed with the cluster name (for example `cicddev-cert-manager`) and does not match the actual workload names.

## Metrics queries

### Resource usage

Uses `pod=~"{prefix}-.*"` to match by pod name:

| Metric | Source | Purpose |
|--------|--------|---------|
| `container_cpu_usage_seconds_total` | cAdvisor | CPU usage |
| `container_memory_working_set_bytes` | cAdvisor | Memory usage |
| `kube_pod_container_resource_requests` | kube-state-metrics | CPU/memory requests |
| `kube_pod_container_resource_limits` | kube-state-metrics | CPU/memory limits |

### Workload status

Uses label regex matches based on the name prefix like `deployment=~"prefix.*"` to find metrics provided by kube-state-metrics about matching deployments etc.

**Desired replicas:**

- `kube_deployment_spec_replicas{deployment=~"prefix.*", ...}`
- `kube_statefulset_replicas{statefulset=~"prefix.*", ...}`
- `kube_daemonset_status_desired_number_scheduled{daemonset=~"prefix.*", ...}`

**Ready replicas:**

- `kube_deployment_status_replicas_ready{deployment=~"prefix.*", ...}`
- `kube_statefulset_status_replicas_ready{statefulset=~"prefix.*", ...}`
- `kube_daemonset_status_number_ready{daemonset=~"prefix.*", ...}`

## Examples

### HelmRelease: `mimir`

| Field | Value |
|-------|-------|
| CR name | `mimir` |
| `spec.releaseName` | `mimir` |
| `spec.targetNamespace` | `mimir` |
| `giantswarm.io/cluster` | `graveler` |
| **Resolved `cluster_id`** | `graveler` |
| **Resolved namespace** | `mimir` |
| **Resolved prefix** | `mimir` |

Matches: Deployments `mimir-distributor`, `mimir-gateway`, etc. StatefulSets `mimir-ingester`, `mimir-compactor`, etc.

### App CR: `cicddev-cert-manager`

| Field | Value |
|-------|-------|
| CR `metadata.name` | `cicddev-cert-manager` |
| CR `metadata.namespace` | `org-team-tinkerers` |
| `spec.name` | `cert-manager-app` |
| `spec.namespace` | `kube-system` |
| `giantswarm.io/cluster` | `cicddev` |
| **Resolved `cluster_id`** | `cicddev` |
| **Resolved namespace** | `kube-system` |
| **Resolved prefix** | `cert-manager-app` |

Matches: Deployments `cert-manager-app`, `cert-manager-app-cainjector`, `cert-manager-app-webhook`.

### App CR: `cicddev-alloy-logs`

| Field | Value |
|-------|-------|
| CR `metadata.name` | `cicddev-alloy-logs` |
| `spec.name` | `alloy` |
| `spec.namespace` | `kube-system` |
| `giantswarm.io/cluster` | `cicddev` |
| **Resolved `cluster_id`** | `cicddev` |
| **Resolved namespace** | `kube-system` |
| **Resolved prefix** | `alloy` |

Matches: DaemonSet `alloy-logs`, but also DaemonSet/Deployment `alloy-events` (belonging to a different App CR). This is a known limitation of the prefix-based matching approach.

## Known limitations

- **Prefix over-matching**: When `spec.name` is generic (for example `alloy`), the `prefix.*` regex may match workloads belonging to sibling App CRs (for example `alloy-logs` and `alloy-events` both match `alloy.*`).
- **List page deduplication by exact name**: The deployments list page matches CRDs to Mimir workloads by exact chart name or CR name. If the chart name differs from the primary workload name (unusual but possible), the match fails and both appear as separate entries.
