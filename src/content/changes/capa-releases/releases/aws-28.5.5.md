---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/workload-cluster-releases-capa/releases/aws-28.5.5/
changes_categories:
- CAPA releases
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/capa/v28.5.5
  version: aws-28.5.5
  version_tag: aws-28.5.5
date: '2025-06-27T09:08:48'
description: Release notes for CAPA workload cluster release aws-28.5.5, published
  on 27 June 2025, 09:08.
title: Workload cluster release aws-28.5.5 for CAPA
---

Upgrade cluster-aws to handle IMDS Hop Limit and patch kubernetes version.

## Changes compared to v28.5.4

### Components

- cluster-aws from v1.3.10 to v1.3.11

### cluster-aws [v1.3.10...v1.3.11](https://github.com/giantswarm/cluster-aws/compare/v1.3.10...v1.3.11)

#### Changed

- Reduce IMDS Response Hop Limit to 2 if pod networking is in ENI mode to increase security.
