---
linkTitle: get catalogs
title: "'kubectl gs get catalogs' command reference"
description: Reference documentation on how to list catalogs and get details for a single catalog using 'kubectl gs'.
weight: 20
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-catalogs/
  - /ui-api/kubectl-gs/get-catalogs/
last_review_date: 2024-01-18
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I list catalogs using kubectl?
  - How can I inspect catalogs using kubectl?
---

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a [Catalog]({{< relref "/vintage/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
custom resource in this case, or list several of them.

The Catalog CRD is namespace scoped and replaces the [AppCatalog]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}})
CRD which is cluster scoped. This is to improve multi-tenancy support when used with the [Management API]({{< relref "/vintage/platform-overview/management-api" >}}).

## Usage

### Get a list of catalogs {#list}

Simply execute

```nohighlight
kubectl gs get catalogs
```

to list some information on all available public catalogs.

Here is some example output:

```nohighlight
NAME                    NAMESPACE   CATALOG URL                                                   AGE
giantswarm              default     https://giantswarm.github.io/giantswarm-catalog/              1d
giantswarm-playground   default     https://giantswarm.github.io/giantswarm-playground-catalog/   1d
```

### Get a specific catalog

When used with a catalog name as an additional argument, the command will show
the latest available version of each app in the catalog according to
[semantic versioning](https://semver.org/).

Example:

```nohighlight
kubectl gs get catalogs giantswarm
```

```nohighlight
kubectl gs get catalogs giantswarm
CATALOG      APP NAME                       APP VERSION   VERSION            AGE
giantswarm   cert-manager-app               1.3.1         2.7.0              25h
```

Note: As an alternative to `get catalogs`, `get catalog` will also work.

## Output {#columns}

The standard tabular output format for catalogs features these columns:

- `NAME`: Name of the app catalog.
- `URL`: URL for the Helm chart repository.
- `AGE`: How long ago was the catalog created.

When viewing the available apps within a catalog the output format features
these columns:

- `CATALOG`: Name of the app catalog.
- `APP NAME`: Name of the app.
- `APP VERSION`: Upstream version of the app.
- `VERSION`: Latest version of the app.
- `AGE`: How long ago was the app release created.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get catalogs` command. Use `kubectl gs get catalogs --help` for a full list.

### `--all-namespaces/-A` {#flags-all-namespaces}

`kubectl` commonly allows to list resources for all namespaces for all `get` subcommands. `kubectl gs get catalogs` is no different.
However by default we hide internal catalogs in the `giantswarm` namespace.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get catalogs` is no different.

#### YAML output {#yaml}

To inspect a catalogs main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for catalog `giantswarm`. It would return the [Catalog]({{< relref "/vintage/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}}) resource.

```nohighlight
kubectl gs get catalogs giantswarm --output yaml
```

When applied without a catalog name, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get catalogs --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: catalog.application.giantswarm.io/v1alpha1
  kind: Catalog
...
```

## Related

- [`kubectl gs login`]({{< relref "/vintage/use-the-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
