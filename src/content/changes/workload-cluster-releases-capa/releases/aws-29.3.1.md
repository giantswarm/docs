---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-capa/releases/capa-aws-29.3.1/
changes_categories:
- Workload cluster releases for CAPA
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/capa/v29.3.1
  version: aws-29.3.1
  version_tag: aws-29.3.1
date: '2024-09-30T12:00:00'
description: Release notes for CAPA workload cluster release aws-29.3.1, published
  on 30 September 2024, 12:00.
title: Workload cluster release aws-29.3.1 for CAPA
---

## Changes compared to v29.3.0

This release does not contain any changes to components or apps, but makes use of an cluster-aws chart which allows custom tags applied to EC2 instances only using the `global.providerSpecific.additionalNodeTags` property.

Expose the maxHealthyPercentage property to allow setting the maximum percentage of healthy machines in the Auto Scaling Group during upgrades.