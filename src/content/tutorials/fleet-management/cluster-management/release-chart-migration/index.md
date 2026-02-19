---
title: Migrating to release charts
description: How to migrate existing clusters from cluster-provider to release-provider charts for automated upgrades via Flux.
weight: 15
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-release-chart-migration
last_review_date: 2026-02-19
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - What are release charts?
  - How do I migrate from cluster-aws to release-aws?
  - How do automated cluster upgrades work with Flux?
  - What is the difference between cluster-provider and release-provider charts?
---

Starting with release version 35, cluster charts are published under a new naming scheme: `release-<provider>` (for example `release-aws`) instead of `cluster-<provider>` (for example `cluster-aws`). This enables automated cluster upgrades through standard Flux/Helm patterns.

## Why release charts

With the previous `cluster-<provider>` charts, upgrading a cluster required coordinating multiple pieces:

1. Updating `global.release.version` in the user ConfigMap
2. The [App Admission Controller](https://github.com/giantswarm/app-admission-controller) mutating webhook detecting the change and updating the App CR's `.spec.version`
3. The chart doing a runtime lookup of the Release CR

This flow made it difficult to use standard Flux automation because Flux manages upgrades by changing `.spec.version` on an App CR, but the mutating webhook would overwrite that field.

With `release-<provider>` charts:

- The App CR's **`.spec.version` is the actual release version** (for example `35.0.0`), not the internal chart version (for example `7.2.5`)
- **Standard Flux/Helm upgrade patterns work**: bumping `.spec.version` from `35.0.0` to `35.1.0` triggers an upgrade
- **No mutating webhook interference**: the App Admission Controller only intercepts charts named `cluster-*`, so `release-*` charts pass through unmodified
- **No ConfigMap version override needed**: the release version is baked into the chart's `values.yaml` as `global.release.version`

## How it works

When a new release (for example `v35.0.0`) is created in the [releases repository](https://github.com/giantswarm/releases), an automated CI pipeline:

1. Pulls the original `cluster-aws:7.2.5` chart from the OCI registry
2. Renames it to `release-aws`
3. Sets the chart version to `35.0.0`
4. Injects `global.release.version: "35.0.0"` into `values.yaml`
5. Publishes `release-aws:35.0.0` to the registry

The result is a chart that is functionally identical to the original `cluster-aws` chart but versioned to match the release and self-contained (no external ConfigMap needed for version resolution).

### Provider mapping

| Provider | Previous chart | New chart |
|----------|---------------|-----------|
| AWS | `cluster-aws` | `release-aws` |
| Azure | `cluster-azure` | `release-azure` |
| vSphere | `cluster-vsphere` | `release-vsphere` |
| Cloud Director | `cluster-cloud-director` | `release-cloud-director` |
| Elastic Kubernetes Service (EKS) | `cluster-eks` | `release-eks` |

## New clusters

For new clusters created with release version 35 or later, [`kubectl-gs template cluster`]({{< relref "/reference/kubectl-gs/template-cluster" >}}) automatically uses `release-<provider>` chart names with the release version set in `.spec.version`. No manual steps are required.

## Migrating existing clusters

Existing clusters using `cluster-<provider>` charts continue to work without any changes. Migration is **optional** but recommended if you want to use Flux-based automated upgrades.

To migrate an existing cluster to use the new chart naming:

### 1. Update the App CR

Change the App CR's `.spec.name` and `.spec.version` fields:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: my-cluster        # metadata.name stays the same
  namespace: org-myorg
spec:
  name: release-aws        # was: cluster-aws
  version: "35.0.0"        # was: "" (empty, set by webhook)
  catalog: cluster
  # ... rest of spec unchanged
```

### 2. Remove the version override from the ConfigMap (optional)

If your user ConfigMap contains a `global.release.version` override, you can remove it since the value is now baked into the chart:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-cluster-userconfig
  namespace: org-myorg
data:
  values: |
    # global.release.version is no longer needed here
    # (it's already set in the release chart's values.yaml)
```

If you keep the ConfigMap value, it takes precedence over the chart default. This is harmless as long as the version matches.

### 3. Verify the upgrade

After applying the changes, verify that the App CR is reconciled:

```bash
kubectl get app my-cluster -n org-myorg -o yaml
```

Confirm that:

- `.spec.name` is `release-<provider>`
- `.spec.version` matches the target release version
- `.status.release.status` shows the deployment progressing

## Automating upgrades with flux

Once a cluster uses `release-<provider>` charts, you can automate upgrades with Flux by updating `.spec.version` in your GitOps repository. For example, changing the App CR's version from `35.0.0` to `35.1.0` triggers an upgrade to the new release.

This works because each release version corresponds to a published chart version in the registry, and Flux can manage the App CR's `.spec.version` field directly without the mutating webhook interfering.
