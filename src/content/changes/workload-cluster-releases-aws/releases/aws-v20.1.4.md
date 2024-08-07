---
# Generated by scripts/aggregate-changelogs. WARNING: Manual edits to this files will be overwritten.
aliases:
- /changes/tenant-cluster-releases-aws/releases/aws-v20.1.4/
changes_categories:
- Workload cluster releases for AWS
changes_entry:
  repository: giantswarm/releases
  url: https://github.com/giantswarm/releases/tree/master/aws/v20.1.4
  version: 20.1.4
  version_tag: v20.1.4
date: '2024-07-09T07:58:07'
description: Release notes for AWS workload cluster release v20.1.4, published on
  09 July 2024, 07:58.
title: Workload cluster release v20.1.4 for AWS
---

This patch release fixes an issue with cert-manager acme-http01-solver-image argument and improves container security.

## Change details

### cert-manager [3.7.9](https://github.com/giantswarm/cert-manager-app/releases/tag/v3.7.9)

#### Fix
- Remove quotes from acme-http01-solver-image argument. The quotes are used when looking up the image which causes an error.

#### Update
- Improves container security by setting `runAsGroup` and `runAsUser` greater than zero for all deployments.

### security-bundle [1.6.7](https://github.com/giantswarm/security-bundle/releases/tag/v1.6.7)

#### Changed
- Update `kyverno` (app) to v0.17.13.
- Update `trivy-operator` (app) to v0.8.1.
- Update `starboard-exporter` (app) to v0.7.10.
