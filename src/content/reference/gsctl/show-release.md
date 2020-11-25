---
title: "gsctl Command Reference: show release"
description: "The 'gsctl show release' command displays details of a tenant cluster release."
date: 2020-11-25
type: page
weight: 52
---

# `gsctl show release`

The `gsctl show release` command displays details of a tenant cluster release.

## Usage

```nohighlight
gsctl show release 11.5.1
```

## Output details

Example output for tenant cluster release v11.5.1 for AWS:

```nohighlight
---
Version: 11.5.1
Created: 2020 Aug 04, 12:34 UTC
Active: true
Components:
  app-operator: 1.0.0
  aws-cni: 1.6.0
  aws-operator: 8.7.5
  calico: 3.15.1
  cert-operator: 0.1.0
  cluster-operator: 2.3.2
  containerlinux: 2512.2.1
  etcd: 3.4.9
  kubernetes: 1.16.13
  cert-exporter: 1.2.3
  cert-manager: 0.9.0
  chart-operator: 0.12.4
  cluster-autoscaler: 1.16.5
  coredns: 1.6.5
  external-dns: 0.7.2
  kiam: 3.5.0
  kube-state-metrics: 1.9.5
  metrics-server: 0.3.3
  net-exporter: 1.9.0
  node-exporter: 0.18.1
Changelog:
  See release notes: https://github.com/giantswarm/releases/tree/master/aws/v11.5.1
```

The output lines in detail:

- **Version:** version of this tenant cluster release.
- **Created:** date and time of tenant cluster release creation.
- **Active:** wether this release is active or deprecated. Creating clusters with deprecated tenant cluster releases is not recommended.
- **Components:** included component versions in this release.
- **Changelog:** link to release notes for this tenant cluster release.

## Related

- [`gsctl list releases`](../list-releases/)
- [`gsctl upgrade cluster`](../upgrade-cluster/)
- [`gsctl create cluster`](../create-cluster/)
