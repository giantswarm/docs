---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/workload-cluster-releases-capa/releases/aws-25.5.2/
changes_categories:
- CAPA releases
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/capa/v25.5.2
  version: aws-25.5.2
  version_tag: aws-25.5.2
date: '2025-02-26T12:00:00'
description: Release notes for CAPA workload cluster release aws-25.5.2, published
  on 26 February 2025, 12:00.
title: Workload cluster release aws-25.5.2 for CAPA
---

## Changes compared to v25.5.1

### Components

- cluster-aws from v1.3.8 to v1.3.9

### cluster-aws [v1.3.8...v1.3.9](https://github.com/giantswarm/cluster-aws/compare/v1.3.8...v1.3.9)

#### Added

- Add ingress rule in nodes Security Group to allow access to the Cilium Relay when using ENI mode.
