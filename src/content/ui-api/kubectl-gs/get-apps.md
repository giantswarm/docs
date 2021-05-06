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
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I list apps using kubectl?
  - How can I inspect apps using kubectl?
---

# `kubectl gs get apps`

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, an [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}})
custom resource in this case, or list several of them.

## Usage

### Get a list of apps {#list}

Simply execute

```nohighlight
kubectl gs get apps -n ab12c
```

to list some information on all Apps available to you in the current namespace.
Your Apps are stored in a namespace in the management cluster with the same
name as your cluster ID.

Here is some example output:

```nohighlight
NAME                 VERSION   LAST DEPLOYED   STATUS
cert-exporter        1.6.1     11m             deployed
```

### Get specific app

When used with an App name as additional argument, the command will show details for a single App. Example:

```nohighlight
kubectl gs get apps -n ab12c cert-exporter
```

Note: As an alternative to `get apps`, `get app` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `NAME`: Name of the App.
- `VERSION`: Version of the App.
- `LAST DEPLOYED`: When the App was last deployed.
- `STATUS`: Status of the App.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get apps` command. Use `kubectl gs get apps --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get apps` is no different.

#### YAML output {#yaml}

To inspect a cluster's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for App `coredns`. It would return the [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) resource.

```nohighlight
kubectl gs get apps -n ab12c coredns --output yaml
```

When applied without an App name, the output will be a list of resources. Example:

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
