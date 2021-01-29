---
title: "'gsctl list releases' command reference"
description: The 'gsctl list releases' command shows all workload cluster releases available in an installation.
weight: 45
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl list releases`

The `gsctl list releases` command shows all workload cluster releases available in an installation.

## Workload cluster releases {#definition}

Workload cluster releases are software bundles that constitute the software running in a cluster.
They are identified by their semantic version number in the `MAJOR.MINOR.PATCH` format.
Check our detailed explanation of [workload cluster releases](/reference/workload-cluster-release-versions/) to learn more.

A workload cluster release provides _components_, of which Kubernetes is an important one.
For each workload cluster release the contained components are listed with their specific
version.

An installation usually supports several workload cluster releases at the same time, which allows
to select a specific workload cluster release when creating a cluster.

## Usage and output

The command has no specific flags. Simply run it like this:

```nohighlight
gsctl list releases
```

The resulting output is a list of all workload cluster releases, like in the following example
(in this case showing one item only):

```yaml
---
Version: 0.3.0
Created: 2017 Oct 27, 16:21 UTC
Active: true
Components:
  calico: 2.6.2
  docker: 1.12.6
  etcd: 3.2.7
  flannel: 0.9.0
  kubedns: 1.14.5
  kubernetes: 1.8.1
  nginx-ingress-controller: 0.9.0
  vault: 0.7.3
Changelog:
  calico: Calico version updated.
  docker: Docker version updated.
  etcd: Etcd version updated.
  flannel: Flannel version updated.
  kubedns: KubeDNS version updated.
  kubernetes: Kubernetes version updated.
  nginx-ingress-controller: Nginx-ingress-controller version updated.
  vault: Vault version updated.
```

The output is formatted as YAML, to allow both user-friendly and
machine-readable output of hierarchical information.

Output details:

- **Version:** semantic version number identifying the release
- **Created:** Date/time the workload cluster release has been created
- **Active:** `true` if the workload cluster release is usable for new cluster or upgrades.
  `false` will indicate workload cluster releases that are no longer usable for new clusters or
  upgrades, but which may still be running on older clusters.
- **Components:** List of components provided by the release, each with their
  version number
- **Changelog:** List of changes in components compared to the previous
  workload cluster release. Note that only a subset of all components may have changed.

## Related

- [`gsctl create cluster`](../create-cluster/)
- [`gsctl show cluster`](../show-cluster/)
- [API: Get releases](/api/#operation/getReleases)
