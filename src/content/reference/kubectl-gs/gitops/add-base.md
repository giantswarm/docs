---
linkTitle: add base
title: "'kubectl gs gitops add base' command reference"
description: Reference documentation on how to add a new base to create clusters in a GitOps repository.
weight: 20
menu:
  principal:
    parent: kubectlgs-gitops
last_review_date: 2026-06-08
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
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: ${cluster_name}
  namespace: org-${organization}
spec:
  catalog: cluster
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: cluster-aws
  namespace: org-${organization}
  userConfig:
    configMap:
      name: ${cluster_name}-config
      namespace: org-${organization}
  version: ""

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
  release:
    version: ${release}
```

Remove the `--dry-run` flag and re-run it to apply the changes.
