---
linkTitle: template app
title: "'kubectl gs template app' command reference"
description: Reference documentation on how to create a manifest for an App using 'kubectl gs'.
weight: 70
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /use-the-api/kubectl-gs
  - /reference/kubectl-gs/template-app/
  - /ui-api/kubectl-gs/template-app/
last_review_date: 2024-01-18
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an app manifest for the Management API?
  - How can I add labels and annotations to the target namespace of an app?
---

The `template app` command allows to create a manifest for an app to be installed in a workload cluster. The resulting manifest is meant to be applied to the management cluster, for example via `kubectl apply`.

The resulting manifest of the `template app` defines an [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) resource (API group/version `application.giantswarm.io/v1alpha1`).

## Usage

The command to execute is `kubectl gs template app`.

It supports the following required flags:

- `--name`: Name of the app in the catalog. This is also the name of the App CR unless `--app-name` is set.
- `--target-namespace`: Namespace where the app will be deployed.
- `--catalog`: Catalog name where the app package is stored. `Catalog` CR for this catalog must exist in the cluster.
- `--cluster-name`: Name of the cluster the app will be deployed to.
- `--version`: Version of the app to be installed. The version package must exist in the `Catalog` storage.

It also supports older flag variations to maintain backward compatibility:

- `--namespace` - replaced by `--target-namespace`.
- `--cluster` - replaced by `--cluster-name`.

These older flag variations are marked as deprecated and will be removed in the next major version of `kubectl gs`.

The example command

```nohighlight
kubectl gs template app \
  --catalog giantswarm-playground \
  --name keda \
  --target-namespace default \
  --cluster-name 2hr7z  \
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
- `--namespace-annotations`: Additional annotations to be appended to the metadata of the target namespace (through [`spec.namespaceConfig.annotations`]({{< relref "/vintage/getting-started/app-platform/namespace-configuration/index.md" >}}) of [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR) in form `key=value`. To specify multiple annotations, either separate annotation pairs with commata (,) or specify the flag multiple times.
- `--namespace-labels`: Additional labels to be appended to the metadata of the target namespace (through [`spec.namespaceConfig.labels`]({{< relref "/vintage/getting-started/app-platform/namespace-configuration/index.md" >}}) of [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR) in form `key=value`. To specify multiple labels, either separate label pairs with commata (,) or specify the flag multiple times.
- `--in-cluster`: Creates in-cluster app by setting `.spec.kubeConfig.inCluster` field of the [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR to `true`. This is necessary for installing collection of apps, for example [Security Pack]({{< relref "/vintage/platform-overview/security" >}}).

Only required fields are templated. Other fields are are set by the
[defaulting webhook]({{< relref "/vintage/getting-started/app-platform/defaulting-validation" >}}).

This is enabled for the Giant Swarm releases shown below. For older releases you can set the `--defaulting-enabled` flag to false.

- AWS >= v14.0.0
- Azure >= v13.1.0
- KVM >= v13.1.0
