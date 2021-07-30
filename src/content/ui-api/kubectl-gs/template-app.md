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
last_review_date: 2021-06-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I create an app manifest for the Management API?
---

# `kubectl gs template app`

In order to create an App using custom resources, `kubectl gs` will help you create manifests for the resource type:

- [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API group/version `application.giantswarm.io/v1alpha1`) - holds the base App specification.

## Usage

The command to execute is `kubectl gs template app`.

It supports the following required flags:

- `--name`: Name of the app in the catalog. This is also the name of the App CR unless `--app-name` is set.
- `--namespace`: Namespace where the app will be deployed.
- `--catalog`: Catalog name where the app package is stored. `Catalog` CR for this catalog must exist in the cluster.
- `--cluster`: Name of the cluster the app will be deployed to.
- `--version`: Version of the app to be installed. The version package must exist in the `Catalog` storage.

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

- `--app-name`: Name of the App CR, otherwise uses the same value as `--name`. This can be set when you want to change the name or install multiple instances of an app.
- `--defaulting-enabled`: Only include fields that differ from the default value (default true). When false, a much longer template is created.
- `--user-configmap`: Path to the user values configmap YAML file.
- `--user-secret`: Path to the user secrets YAML file.

Only required fields are templated. Other fields are are set by the
[defaulting webhook]({{< relref "/app-platform/defaulting-validation" >}}).

This is enabled for the Giant Swarm releases shown below. For older releases you can set the `--defaulting-enabled` flag to false.

- AWS >= v14.0.0
- Azure >= v13.1.0
- KVM >= v13.1.0
