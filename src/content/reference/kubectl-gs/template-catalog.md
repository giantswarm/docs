---
linkTitle: template catalog
title: "'kubectl gs template catalog' command reference"
description: Reference documentation on how to create a manifest for a Catalog using 'kubectl gs'.
weight: 80
menu:
  principal:
    parent: reference-kubectlgs
last_review_date: 2024-11-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an catalog manifest for the platform API?
  - How can I add catalog level values or secrets for the apps deployed from this catalog?
aliases:
  - /vintage/use-the-api/kubectl-gs/template-catalog/
---

The `template catalog` command allows to create an [app catalog]({{< relref "/vintage/getting-started/app-platform" >}}) manifest. The resulting manifest is meant to be applied to the management cluster, for example via `kubectl apply`.

The resulting manifest will define a [`Catalog`]({{< relref "/reference/platform-api/crd/catalogs.application.giantswarm.io.md" >}}) resource (API group/version `application.giantswarm.io/v1alpha1`).

**Note:** The `Catalog` CRD is namespace scoped and replaces the [AppCatalog]({{< relref "/reference/platform-api/crd/appcatalogs.application.giantswarm.io.md" >}})
CRD which is cluster scoped. This is to improve multi-tenancy support when used with the [platform API]({{< relref "/overview/architecture/#platform-api" >}}).

The Catalog CRD supports having a related `ConfigMap` and/or `Secret` resource with values YAML. These values serve as a base for the rest of the [configuration]({{< relref "/vintage/getting-started/app-platform/app-configuration/index.md" >}}) when Apps are deployed from this App Catalog.

## Usage

The command to execute is `kubectl gs template catalog`.

It supports the following required flags:

- `--name` - Catalog name.
- `--target-namespace` - Namespace where the catalog will be created.
- `--description` - Description of the purpose of the catalog.
- `--url` - URL where the helm repository lives. Can be defined multiple times if you want to utilize repository mirroring.
- `--type` - Label containing a type of the helm repository. Defaults to `helm`. Can be defined multiple times.
- `--logo` - URL of the catalog logo image.
- `--visibility` - Defaults to `public` in which case the catalog appears in the web UI. Any other value will hide the catalog.

It also supports an older flag variation to maintain backward compatibility:

- `--namespace` - replaced by `--target-namespace`.

This older flag variation is marked as deprecated and will be removed in the next major version of `kubectl gs`.

Example command:

```nohighlight
kubectl gs template catalog \
  --name example-catalog \
  --target-namespace example-org \
  --description "An example Catalog" \
  --url https://example.github.io/my-app-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

Example command with multiple repositories defined:

```nohighlight
kubectl gs template catalog \
  --name example-catalog \
  --target-namespace example-org \
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
