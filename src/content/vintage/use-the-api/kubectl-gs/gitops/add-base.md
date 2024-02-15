---
linkTitle: add base
title: "'kubectl gs gitops add base' command reference"
description: Reference documentation on how to add a new base to create clusters in a GitOps repository.
weight: 20
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2024-01-18
aliases:
  - /reference/kubectl-gs/gitops/add-org
  - /ui-api/kubectl-gs/gitops/add-org
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I add an base to a GitOps repository?
---

This command adds a new base to the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/init" >}}))

## Description

The structure created by this command is presented below.

```nohighlight
bases
└── clusters
    └── capa
        └── template
            ├── cluster.yaml
            ├── cluster_config.yaml
            ├── default_apps.yaml
            ├── default_apps_config.yaml
            └── kustomization.yaml
```

## Usage

Basic command syntax: `kubectl gs gitops add base FLAGS`.

### Flags

- `--provider` -- Installation infrastructure provider, supported values: capa, gcp, openstack

{{% kubectl_gs_gitops_common_flags %}}

### Examples

```nohighlight
kubectl gs gitops add base --provider gcp --dry-run
```

Output:

```nohighlight

## CREATE ##
./bases
./bases/clusters
./bases/clusters/gcp
./bases/clusters/gcp/template
./bases/clusters/gcp/template/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
    - values=cluster_config.yaml
    name:  ${cluster_name}-config
    namespace: org-${organization}
  - files:
    - values=default_apps_config.yaml
    name:  ${cluster_name}-default-apps-config
    namespace: org-${organization}
generatorOptions:
  disableNameSuffixHash: true
kind: Kustomization
resources:
  - cluster.yaml
  - default_apps.yaml

./bases/clusters/gcp/template/cluster.yaml
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
  name: cluster-gcp
  namespace: org-${organization}
  userConfig:
    configMap:
      name: ${cluster_name}-config
      namespace: org-${organization}
  version: ${cluster_release}

./bases/clusters/gcp/template/cluster_config.yaml
clusterName: ${cluster_name}
controlPlane:
  containerdVolume: {}
  etcdVolume: {}
  kubeletVolume: {}
  replicas: 3
  rootVolume: {}
  serviceAccount: {}
gcp: {}
machineDeployments:
- containerdVolume: {}
  kubeletVolume: {}
  name: machine-pool0
  rootVolume: {}
  serviceAccount: {}
organization: ${organization}

./bases/clusters/gcp/template/default_apps.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
    giantswarm.io/cluster: ${cluster_name}
    giantswarm.io/managed-by: cluster
  name: ${cluster_name}-default-apps
  namespace: org-${organization}
spec:
  catalog: cluster
  config:
    configMap:
      name: ${cluster_name}-cluster-values
      namespace: org-${organization}
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
  name: default-apps-gcp
  namespace: org-${organization}
  userConfig:
    configMap:
      name: ${cluster_name}-default-apps-config
      namespace: org-${organization}
  version: ${default_apps_release}

./bases/clusters/gcp/template/default_apps_config.yaml
clusterName: ${cluster_name}
organization: ${organization}

```

Remove the `--dry-run` flag and re-run it to apply the changes.
