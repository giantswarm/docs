---
linkTitle: get appcatalogs
title: "'kubectl gs get appcatalogs' command reference"
description: Reference documentation on how to list appcatalogs and get details for a single appcatalog using 'kubectl gs'.
weight: 20
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-appcatalogs/
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I list appcatalogs using kubectl?
  - How can I inspect appcatalogs using kubectl?
---

# `kubectl gs get appcatalogs`

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, an [AppCatalog]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}})
custom resource in this case, or list several of them.

## Usage

### Get a list of app catalogs {#list}

Simply execute

```nohighlight
kubectl gs get appcatalogs
```

to list some information on all available public app catalogs.

Here is some example output:

```nohighlight
NAME                    CATALOG URL                                                   AGE
giantswarm              https://giantswarm.github.io/giantswarm-catalog/              280d
giantswarm-playground   https://giantswarm.github.io/giantswarm-playground-catalog/   280d
```

### Get a specific app catalog

When used with an app catalog name as additional argument, the command will show
the latest available version of each app in the catalog according to
[semantic versioning](https://semver.org/).

Example:

```nohighlight
kubectl gs get appcatalogs giantswarm
```

```nohighlight
kubectl gs get appcatalogs giantswarm
CATALOG      APP NAME                       APP VERSION   VERSION            AGE
giantswarm   cert-manager-app               1.3.1         2.7.0              25h
```

Note: As an alternative to `get appcatalogs`, `get appcatalog` will also work.

## Output {#columns}

The standard tabular output format for app catalogs features these columns:

- `NAME`: Name of the app catalog.
- `URL`: URL for the Helm chart repository.
- `CREATED`: How long ago the appcatalog was created.

When viewing the available apps within an app catalog the output format features
these columns:

- `CATALOG`: Name of the app catalog.
- `APP NAME`: Name of the app.
- `APP VERSION`: Upstream version of the app.
- `VERSION`: Latest version of the app.
- `CREATED`: How long ago the app release was created.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get appcatalogs` command. Use `kubectl gs get appcatalogs --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get appcatalogs` is no different.

#### YAML output {#yaml}

To inspect a cluster's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for cluster `ab12c`. It would return the [AppCatalog]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}}) resource.

```nohighlight
kubectl gs get appcatalogs giantswarm --output yaml
```

When applied without an app catalog name, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get appcatalogs --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: appcatalog.application.giantswarm.io/v1alpha1
  kind: AppCatalog
...
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
