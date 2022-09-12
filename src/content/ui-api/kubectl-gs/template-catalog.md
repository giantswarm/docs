---
linkTitle: template catalog
title: "'kubectl gs template catalog' command reference"
description: Reference documentation on how to create a manifest for a Catalog using 'kubectl gs'.
weight: 80
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-catalog/
last_review_date: 2021-07-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an catalog manifest for the Management API?
  - How can I add catalog level values or secrets for the apps deployed from this catalog?
---

The `template catalog` command allows to create an [app catalog]({{< relref "/app-platform" >}}) manifest. The resulting manifest is meant to be applied to the Management Cluster, for example via `kubectl apply`.

The resulting manifest will define a [`Catalog`]({{< relref "/ui-api/management-api/crd/catalogs.application.giantswarm.io.md" >}}) resource (API group/version `application.giantswarm.io/v1alpha1`).

**Note:** The `Catalog` CRD is namespace scoped and replaces the [AppCatalog]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}})
CRD which is cluster scoped. This is to improve multi-tenancy support when used with the [Management API]({{< relref "/ui-api/management-api/overview/index.md" >}}).

The Catalog CRD supports having a related `ConfigMap` and/or `Secret` resource with values YAML. These values are merged with the rest of the [configuration]({{< relref "/app-platform/app-configuration/index.md" >}}) when Apps are deployed from this App Catalog.

## Usage

The command to execute is `kubectl gs template catalog`.

It supports the following required flags:

- `--name` - Catalog name.
- `--namespace` - Namespace where the catalog will be created.
- `--description` - Description of the purpose of the catalog.
- `--url` - URL where the helm repository lives. Can be defined multiple times if you want to utilize repository mirroring.
- `--type` - Label containing a type of the helm repository. Defaults to `helm`. Can be defined multiple times.
- `--logo` - URL of the catalog logo image.
- `--visibility` - Defaults to `public` in which case the catalog appears in the web UI. Any other value will hide the catalog.

Example command:

```nohighlight
kubectl gs template catalog \
  --name example-catalog \
  --namespace example-org \
  --description "An example Catalog" \
  --url https://example.github.io/my-app-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

Example command with multiple repositories defined:

```nohighlight
kubectl gs template catalog \
  --name example-catalog \
  --namespace example-org \
  --description "An example Catalog" \
  --type helm \
  --url https://example.github.io/my-app-catalog/ \
  --type helm-mirror \
  --url https://example.com/my-app-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

It also supports the following optional flags:

- `--configmap`: Path to the values configmap YAML file.
- `--secret`: Path to the secrets YAML file.

## Output

As a result, the command will produce a YAML document comprising up to three parts:

- the Catalog resource
- a ConfigMap if specified
- a Secret if specified

The following example illustrates the output generated:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: Catalog
metadata:
  name: example-catalog
  namespace: example-org
  labels:
    application.giantswarm.io/catalog-visibility: public
spec:
  description: An example App Catalog
  logoURL: https://example.com/logos/example-logo.png
  storage:
    URL: https://example.github.io/my-app-catalog/
    type: helm
  repositories:
    - URL: https://example.github.io/my-app-catalog/
      type: helm
  title: example-catalog
```
