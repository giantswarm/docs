---
linkTitle: show release
title: "'gsctl show release' command reference"
description: The 'gsctl show release' command displays details of a workload cluster release.
weight: 220
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/show-release/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I inspeact a workload cluster release using gsctl?
---

# `gsctl show release`

The `gsctl show release` command displays details of a workload cluster release.

## Usage

```nohighlight
gsctl show release 11.5.1
```

## Output details

Example output for workload cluster release v11.5.1 for AWS:

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

- **Version:** version of this workload cluster release.
- **Created:** date and time of workload cluster release creation.
- **Active:** wether this release is active or deprecated. Creating clusters with deprecated workload cluster releases is not recommended.
- **Components:** included component versions in this release.
- **Changelog:** link to release notes for this workload cluster release.

## Related

- [`gsctl list releases`]({{< relref "/ui-api/gsctl/list-releases" >}})
- [`gsctl upgrade cluster`]({{< relref "/ui-api/gsctl/upgrade-cluster" >}})
- [`gsctl create cluster`]({{< relref "/ui-api/gsctl/create-cluster" >}})
