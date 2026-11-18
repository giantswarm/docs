---
linkTitle: add base
title: "'kubectl gs gitops add base' command reference"
diataxis_content_type: reference
description: Reference documentation on how to add a new base to create clusters in a GitOps repository.
weight: 20
menu:
  principal:
    parent: kubectlgs-gitops
last_review_date: 2026-11-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I add an base to a GitOps repository?
aliases:
  - /vintage/use-the-api/kubectl-gs/gitops/add-base/
---

This command adds a new base to the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/reference/kubectl-gs/gitops/init" >}}))

## Description

The structure created by this command is presented below.

```nohighlight
bases
└── clusters
    └── PROVIDER
        └── template
            ├── cluster.yaml
            ├── cluster_config.yaml
            └── kustomization.yaml
```

`cluster.yaml` deploys the cluster's `release-<provider>` chart, such as `release-aws`, with a Flux `OCIRepository` and
`HelmRelease`. The chart version is the Giant Swarm release, set by the `${release}` variable, which
[`add workload-cluster`]({{< relref "/reference/kubectl-gs/gitops/add-wc" >}}) sets with its `--release` flag.
`cluster_config.yaml` holds the default values, and `kustomization.yaml` turns it into the `${cluster_name}-config`
ConfigMap that the `HelmRelease` reads.

**Note:** this needs kubectl-gs v6.0.0 or newer. Older versions generate an App CR for the cluster.

## Usage

Basic command syntax: `kubectl gs gitops add base FLAGS`.

### Flags

- `--provider` -- Installation infrastructure provider, supported values: `capa`, `capz`, `vsphere` (required)
- `--region` -- AWS or Azure region where the cluster will be created (required for `capz`)
- `--azure-subscription-id` -- Azure subscription ID (required for `capz`)

{{% kubectl_gs_gitops_common_flags %}}

### Examples

```nohighlight
kubectl gs gitops add base --provider capa --dry-run
```

Output:

```nohighlight

## CREATE ##
./bases
./bases/clusters
./bases/clusters/capa
./bases/clusters/capa/template
./bases/clusters/capa/template/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name:  ${cluster_name}-config
    namespace: org-${organization}
generatorOptions:
  disableNameSuffixHash: true
kind: Kustomization
resources:
  - cluster.yaml

./bases/clusters/capa/template/cluster.yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  labels:
    giantswarm.io/cluster: ${cluster_name}
  name: ${cluster_name}
  namespace: org-${organization}
spec:
  interval: 10m0s
  provider: generic
  ref:
    tag: ${release}
  timeout: 1m0s
  url: oci://gsoci.azurecr.io/charts/giantswarm/release-aws
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  labels:
    giantswarm.io/cluster: ${cluster_name}
  name: ${cluster_name}
  namespace: org-${organization}
spec:
  chartRef:
    kind: OCIRepository
    name: ${cluster_name}
    namespace: org-${organization}
  install:
    remediation:
      remediateLastFailure: false
      retries: 10
  interval: 5m0s
  releaseName: ${cluster_name}
  serviceAccountName: automation
  storageNamespace: org-${organization}
  targetNamespace: org-${organization}
  timeout: 10m0s
  upgrade:
    remediation:
      remediateLastFailure: true
      retries: 10
      strategy: rollback
  valuesFrom:
  - kind: ConfigMap
    name: ${cluster_name}-config
    valuesKey: values

./bases/clusters/capa/template/cluster_config.yaml
global:
  connectivity:
    network: {}
    topology: {}
  controlPlane: {}
  metadata:
    name: ${cluster_name}
    organization: ${organization}
    preventDeletion: false
  nodePools:
    nodepool0: {}
  providerSpecific: {}


## METADATA ##
./.gitops-metadata.yaml
# This file is managed by `kubectl gs gitops`. Do not edit it by hand.
# It records which version of the repository structure each part of this
# repository was generated with, so that `kubectl gs gitops check` can tell
# you when the repository has fallen behind.
apiVersion: gitops.giantswarm.io/v1alpha1
generatedWith: kubectl-gs/6.0.3
kind: RepositoryMetadata
layers:
- generatedWith: kubectl-gs/6.0.3
  kind: cluster-base
  path: bases/clusters/capa/template
  structureVersion: 2
structureVersion: 2
```

Remove the `--dry-run` flag and re-run it to apply the changes.
