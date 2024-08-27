---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-azure/releases/azure-azure-28.0.0/
changes_categories:
- Workload cluster releases for Azure
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/azure/v28.0.0
  version: azure-28.0.0
  version_tag: azure-28.0.0
date: '2024-08-12T18:00:00'
description: Release notes for Azure workload cluster release azure-28.0.0, published
  on 12 August 2024, 18:00.
title: Workload cluster release azure-28.0.0 for Azure
---

## Changes compared to v27.0.0

### Components

- Kubernetes from v1.27.16 to v1.28.12

### Apps

- azure-cloud-controller-manager from v1.27.18-gs1 to v1.28.10-gs1
- azure-cloud-node-manager from v1.27.18-gs1 to v1.28.10-gs1

### azure-cloud-controller-manager [v1.27.18-gs1...v1.28.10-gs1](https://github.com/giantswarm/azure-cloud-controller-manager-app/compare/v1.27.18-gs1...v1.28.10-gs1)

#### Changed

- Chart: Update to upstream v1.28.10. ([#82](https://github.com/giantswarm/azure-cloud-controller-manager-app/pull/82))

### azure-cloud-node-manager [v1.27.18-gs1...v1.28.10-gs1](https://github.com/giantswarm/azure-cloud-node-manager-app/compare/v1.27.18-gs1...v1.28.10-gs1)

#### Changed

- Chart: Update to upstream v1.28.10. ([#71](https://github.com/giantswarm/azure-cloud-node-manager-app/pull/71))