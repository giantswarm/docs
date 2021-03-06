---
linkTitle: template appcatalog
title: "'kubectl gs template appcatalog' command reference"
description: Reference documentation on how to create a manifest for an AppCatalog using 'kubectl gs'.
weight: 80
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-appcatalog/
last_review_date: 2021-06-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I create an appcatalog manifest for the Management API?
---

# `kubectl gs template appcatalog`

In order to create an [App Catalog]({{< relref "/app-platform" >}}) using custom resources, `kubectl-gs` will help you create manifests for the resource type:

- [`AppCatalog`]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}}) (API group/version `application.giantswarm.io/v1alpha1`) - holds the base AppCatalog specification.

## Usage

The command to execute is `kubectl gs template appcatalog`.

It supports the following flags:

- `--name` - Catalog name.
- `--description` - Description of the purpose of the catalog.
- `--url` - URL where the helm repository lives.
- `--owner` - organization, owning workload cluster. Must be configured with existing organization in installation.
- `--logo` - URL of the catalog logo image.

Example command:

```nohighlight
kubectl gs template template appcatalog \
  --name example-catalog \
  --description "An example App Catalog" \
  --url https://example.github.io/my-app-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

## Output

As a result, the command will produce a YAML document comprising three parts:

- a ConfigMap
- a Secret
- the AppCatalog resource

The following example illustrates the output generated:

```yaml
apiVersion: v1
data:
  values: ""
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: example-catalog558rf
  namespace: default
---
apiVersion: v1
kind: Secret
metadata:
  creationTimestamp: null
  name: example-catalog558rf
  namespace: default
---
apiVersion: application.giantswarm.io/v1alpha1
kind: AppCatalog
metadata:
  creationTimestamp: null
  labels:
    app-operator.giantswarm.io/version: 1.0.0
    application.giantswarm.io/catalog-type: awesome
  name: example-catalog
spec:
  config:
    configMap:
      name: example-catalog558rf
      namespace: default
    secret:
      name: example-catalog558rf
      namespace: default
  description: An example App Catalog
  logoURL: https://example.com/logos/example-logo.png
  storage:
    URL: https://example.github.io/my-app-catalog/
    type: helm
  title: example-catalog
```
