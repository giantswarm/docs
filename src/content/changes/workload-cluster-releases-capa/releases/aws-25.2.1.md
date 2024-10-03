---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-capa/releases/capa-aws-25.2.1/
changes_categories:
- Workload cluster releases for CAPA
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/capa/v25.2.1
  version: aws-25.2.1
  version_tag: aws-25.2.1
date: '2024-09-19T12:00:00'
description: Release notes for CAPA workload cluster release aws-25.2.1, published
  on 19 September 2024, 12:00.
title: Workload cluster release aws-25.2.1 for CAPA
---

This release introduces several changes that are required for Vintage to CAPA migration use-cases.

Most notable change is that now `auditd` is *disabled* by default. If you actively use this feature, please add the following field `global.components.auditd.enabled` set to `true` in the Cluster App user values before the upgrade.

## Changes compared to v25.2.0

### Components

- cluster-aws from v1.3.0 to v1.3.2

### cluster-aws [v1.3.0...v1.3.2](https://github.com/giantswarm/cluster-aws/compare/v1.3.0...v1.3.2)

#### Added

- Chart: Add `global.connectivity.network.pods.nodeCidrMaskSize` to schema.
- Chart: Allow to enable `auditd` through `global.components.auditd.enabled`.
- Chart: Support multiple service account issuers.

#### Changed

- Chart: Update `cluster` to v1.0.1.
  - Allow to enable `auditd` service through `global.components.auditd.enabled`.
  - Support multiple service account issuers.
  - Allow configuring kube-controller-manager `--node-cidr-mask-size` flag.