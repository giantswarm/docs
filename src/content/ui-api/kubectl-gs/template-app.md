---
linkTitle: template app
title: "'kubectl gs template app' command reference"
description: Reference documentation on how to create a manifest for an App using 'kubectl gs'.
weight: 70
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-app/
last_review_date: 2021-06-22
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
---

# `kubectl gs template app`

In order to create an App using custom resources, `kubectl gs` will help you create manifests for the resource type:

- [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API group/version `application.giantswarm.io/v1alpha1`) - holds the base App specification.

## Usage

The command to execute is `kubectl gs template app`.

It supports the following required flags:

- `--name`: App name.
- `--namespace`: Namespace where the app will be deployed.
- `--catalog`: Catalog name where the app package is stored. `AppCatalog` CR for this catalog must exist in the cluster.
- `--cluster`: Cluster ID where app will be installed.
- `--version`: Version of the app to be installed. The version package must exit in the `AppCatalog` storage.

The example command

```nohighlight
kubectl gs template app \
  --catalog giantswarm-playground \
  --name keda \
  --namespace default \
  --cluster 2hr7z  \
  --version 0.1.0
```

produces the following output:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: keda
  namespace: 2hr7z
spec:
  catalog: giantswarm-playground
  kubeConfig:
    inCluster: false
  name: keda
  namespace: default
  version: 0.1.0
```

It also supports the following optional flags:

- `--defaulting-enabled`: Only include fields that differ from the default value (default true). When false, a much longer template is created.
- `--user-configmap`: Path to the user values configmap YAML file.
- `--user-secret`: Path to the user secrets YAML file.

Only required fields are templated. Other fields are are set by the
[defaulting webhook]({{< relref "/app-platform/defaulting-validation" >}}).

This is enabled for Giant Swarm releases. For older releases you can set the `--defaulting-enabled` flag to false.

- AWS >= v14.0.0
- Azure >= v13.1.0
- KVM >= v13.1.0
