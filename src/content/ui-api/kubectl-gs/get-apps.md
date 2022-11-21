---
linkTitle: get apps
title: "'kubectl gs get apps' command reference"
description: Reference documentation on how to list apps and get details for a single app using 'kubectl gs'.
weight: 30
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-apps/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I list apps using kubectl?
  - How can I inspect apps using kubectl?
last_review_date: 2021-01-01
---

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, an [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}})
custom resource in this case, or list several of them.

## Usage

### Get a list of apps {#list}

Simply execute

```nohighlight
kubectl gs get apps -n NAMESPACE
```

To list some information on all apps available to you in the specified namespace.
Your apps are stored in a namespace in the management cluster with the same
name as your cluster ID, e.g. `ab12c`.

Here is some example output:

```nohighlight
NAME                 VERSION   LAST DEPLOYED   STATUS     NOTES
cert-exporter        1.6.1     11m             deployed
```

Here is an example output when the deployment of a new version failed.

```nohighlight
NAME                 VERSION   LAST DEPLOYED   STATUS     NOTES
cert-exporter        1.6.1     11m             deployed   Deployment failed for `1.7.0` with `not-installed`: `pulling chart <TARBALL-URL> failed`
```

The `VERSION`, `LAST DEPLOYED` and `STATUS` columns always contain the actual, current status of the deployment. The `NOTES` column contains information on the status of the last attempted deployment. Taking the above example output version `1.6.1` of `cert-exporter` was successfully deployed. At some point App was updated to use version `1.7.0` which is the current desired state. However, the deployment for version `1.7.0` failed to deploy because the chart tarball failed to pull. Therefore the actual status of our App is that version `1.6.1` is still deployed and the status of the last attempted deployment is visible in the `NOTES` column. If all is well, the `NOTES` column is empty for the given App.

### Get a specific app

When used with an app name as additional argument, the command will show details for a single app.

```nohighlight
kubectl gs get apps -n NAMESPACE APP_NAME
```

Note: As an alternative to `get apps`, `get app` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `NAME`: Name of the app.
- `VERSION`: Version of the app.
- `LAST DEPLOYED`: When the app was last deployed.
- `STATUS`: Status of the app.
- `NOTES`: Notes on the last attempted deployment in case there was an error, empty otherwise.

Note: The `NOTES` column is available since `v2.11.0`.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get apps` command. Use `kubectl gs get apps --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get apps` is no different.

#### YAML output {#yaml}

To inspect a cluster's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for app `coredns`. It would return the [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) resource.

```nohighlight
kubectl gs get apps -n ab12c coredns --output yaml
```

When applied without an app name, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get apps -n ab12c --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: app.application.giantswarm.io/v1alpha1
  kind: App
...
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
