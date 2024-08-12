---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-azure/releases/azure-azure-25.0.0/
changes_categories:
- Workload cluster releases for Azure
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/azure/v25.0.0
  version: azure-25.0.0
  version_tag: azure-25.0.0
date: '2024-06-27T18:00:00'
description: Release notes for Azure workload cluster release azure-25.0.0, published
  on 27 June 2024, 18:00.
title: Workload cluster release azure-25.0.0 for Azure
---

We are happy to announce the first release for Azure that uses the new release framework.

## Migration to new releases flow

In order to consume the new flow, the following two fields need to be manually adapted:

* In ConfigMap `<cluster name>-userconfig` set `.Values.global.release` to the release version, e.g. `25.0.0`.
* In App `<cluster name>` remove the `spec.version` field. In case of GitOps, Flux might complain that the app manifest is invalid as the `spec.version` field is mandatory. In that case, edit the live App CR and set `spec.version` to an empty string. That will unblock Flux and allow it reconcile successfully.

And if you want to use `kubectl-gs` to create a cluster, you'd need to now specify the release version, e.g.:

```bash
kubectl-gs template cluster --provider capz --organization my-org --name cluster_name --region westeurope --azure-subscription-id AZURE_ID --release 25.0.0
```