---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-cloud-director/releases/cloud-director-cloud-director-29.1.0/
changes_categories:
- Workload cluster releases for CLOUD-DIRECTOR
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/cloud-director/v29.1.0
  version: cloud-director-29.1.0
  version_tag: cloud-director-29.1.0
date: '2024-11-25T12:00:00'
description: Release notes for CLOUD-DIRECTOR workload cluster release cloud-director-29.1.0,
  published on 25 November 2024, 12:00.
title: Workload cluster release cloud-director-29.1.0 for CLOUD-DIRECTOR
---

## Changes compared to v29.0.0

### Apps

- cert-exporter from v2.9.2 to v2.9.3
- observability-bundle from v1.6.2 to v1.8.0

### cert-exporter [v2.9.2...v2.9.3](https://github.com/giantswarm/cert-exporter/compare/v2.9.2...v2.9.3)

#### Changed

- Chart: Enable `global.podSecurityStandards.enforced`. ([#420](https://github.com/giantswarm/cert-exporter/pull/420))

### observability-bundle [v1.6.2...v1.8.0](https://github.com/giantswarm/observability-bundle/compare/v1.6.2...v1.8.0)

#### Changed

- Upgrade `prometheus-agent` from v0.6.9 to v0.7.0.
  - Adds extraArgs to be able to use nice features like wal truncation
- upgrade `kube-prometheus-stack` from 61.0.0 to 65.1.1
  - prometheus-operator CRDs from 0.73.0 to 0.75.0
  - prometheus-operator from 0.75.0 to 0.77.1
  - prometheus upgraded from 2.53.0 to 2.54.1
  - grafana from 8.2.0 to 8.5.0
  - thanos ruler upgraded from 0.35.1 to 0.36.1
  - prometheus-node-exporter upgraded from 1.8.1 to 1.8.2
- Add missing depends on annotation on alloy-metrics and alloy-logs to make sure they are deployed after the prometheus-operator-crds.
- Upgrade `alloyLogs` to v0.6.1
  - Allow passing PodLogs via helm chart values
  - Upgrade to Alloy v1.4.2 which fixes a bug with component reload/evaluation and keeping Alloy up-to-date
  - Fixes an issue with CiliumNetworkPolicy preventing Alloy to run in clustering mode