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

Starting with release version 35, cluster charts are published under a new naming scheme: `release-<provider>` (for example `release-aws`) instead of `cluster-<provider>` (for example `cluster-aws`). This change simplifies cluster upgrades and enables automation through standard Flux/Helm patterns.

## What changed

With `release-<provider>` charts, upgrading a cluster is straightforward: change the version on the App CR and the upgrade happens. There is no need to manually update a ConfigMap or coordinate multiple resources.

This means you can use Flux to automate cluster upgrades by simply bumping `.spec.version` in your GitOps repository.

### Provider mapping

| Provider | Previous chart | New chart |
|----------|---------------|-----------|
| AWS | `cluster-aws` | `release-aws` |
| Azure | `cluster-azure` | `release-azure` |
| vSphere | `cluster-vsphere` | `release-vsphere` |
| Cloud Director | `cluster-cloud-director` | `release-cloud-director` |
| Elastic Kubernetes Service (EKS) | `cluster-eks` | `release-eks` |

## New clusters

For new clusters created with release version 35 or later, [`kubectl-gs template cluster`]({{< relref "/reference/kubectl-gs/template-cluster" >}}) automatically uses `release-<provider>` chart names. No manual steps are required.

## Migrating existing clusters

Existing clusters using `cluster-<provider>` charts continue to work without any changes. Migration is **optional** but recommended if you want to use Flux-based automated upgrades.

To migrate an existing cluster:

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
  version: "35.0.0"        # set to the target release version
  catalog: cluster
  # ... rest of spec unchanged
```

### 2. Remove the version override from the ConfigMap

If your user ConfigMap contains a `global.release.version` override, you should remove it since the value is now included in the chart:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-cluster-userconfig
  namespace: org-myorg
data:
  values: |
    # global.release.version is no longer needed here
```

If you keep the ConfigMap value, it takes precedence over the chart default. This can result in undesired behavior if the value is not updated regularly.

### 3. Verify

After applying the changes, verify that the App CR is reconciled:

```bash
kubectl get app my-cluster -n org-myorg -o yaml
```

Confirm that:

- `.spec.name` is `release-<provider>`
- `.spec.version` matches the target release version
- `.status.release.status` shows the deployment progressing

## Automating upgrades with flux

Once a cluster uses `release-<provider>` charts, you can automate upgrades by updating `.spec.version` in your GitOps repository. For example, changing the version from `35.0.0` to `35.1.0` triggers an upgrade to the new release.
