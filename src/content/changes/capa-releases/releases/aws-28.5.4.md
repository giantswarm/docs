---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/workload-cluster-releases-capa/releases/aws-28.5.4/
changes_categories:
- CAPA releases
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/capa/v28.5.4
  version: aws-28.5.4
  version_tag: aws-28.5.4
date: '2025-03-19T12:00:00'
description: Release notes for CAPA workload cluster release aws-28.5.4, published
  on 19 March 2025, 12:00.
title: Workload cluster release aws-28.5.4 for CAPA
---

## Changes compared to v28.5.3

### Components

- cluster-aws from v1.3.9 to v1.3.10

### cluster-aws [v1.3.9...v1.3.10](https://github.com/giantswarm/cluster-aws/compare/v1.3.9...v1.3.10)

#### Added

- Add ingress rule in nodes Security Group to allow access for monitoring Chart Operator, EBS CSI Controller, Cilium Operator and Node Exporter.
