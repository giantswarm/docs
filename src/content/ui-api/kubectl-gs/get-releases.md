---
linkTitle: get releases
title: "'kubectl gs get releases' command reference"
description: Reference documentation on how to list releases and get details for a single release using 'kubectl gs'.
weight: 50
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-releases/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I list releases in a cluster using kubectl?
  - How can I inspect releases using kubectl?
last_review_date: 2021-10-04
---

# `kubectl gs get releases`

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a release in this case, or list several of them.

## Usage

### Get a list of releases {#list}

Execute

```nohighlight
kubectl gs get releases
```

to list some information on all releases available to you in the current installation.

Here is some example output:

```nohighlight
VERSION          STATUS     CREATED                         KUBERNETES  CONTAINER LINUX   COREDNS   CALICO
v14.2.1          active     2021-06-29 13:41:00 +0000 UTC   1.19.9      2765.2.3          1.6.5     3.15.3
v14.2.2          active     2021-06-29 13:41:00 +0000 UTC   1.19.9      2605.12.0         1.6.5     3.15.3
v15.0.0          inactive   2021-07-09 11:54:44 +0000 UTC   1.20.8      2765.2.6          1.6.5     3.15.3
v15.1.0          inactive   2021-08-04 15:54:57 +0000 UTC   1.20.9      2765.2.6          1.8.3     3.15.5
v15.1.1          inactive   2021-08-24 15:05:20 +0000 UTC   1.20.9      2765.2.6          1.8.3     3.15.5
v15.2.0          active     2021-08-23 13:02:03 +0000 UTC   1.20.9      2765.2.6          1.8.3     3.15.5
v15.2.1          active     2021-08-26 15:55:59 +0000 UTC   1.20.9      2765.2.6          1.8.3     3.15.5
```

### Get specific release

When used with a release version as additional argument, the command will show details for a single release. Example:

```nohighlight
kubectl gs get releases v15.2.1
```

Note: As an alternative to `get releases`, `get release` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `VERSION`: Unique identifier of the release.
- `STATUS`: Indication of if the release is currently active.
- `CREATED`: Date and time of the release CR creation.
- `KUBERNETES`: The version of Kubernetes provided by this release
- `CONTAINER LINUX`: The version of container linux provided by this release
- `COREDNS`: The version of CoreDNS provided by this release
- `CALICO`: The version of Calico provided by this release

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get releases` command. Use `kubectl gs get releases --help` for a full list.

### `--active-only` {#flags-active-only}

If present, list only the releases that are currently marked as active.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get releases` is no different.
Similar to other `get` subcommands, you can specify the output format of `kubectl gs get releases` using the `--output` flag.

#### YAML output {#yaml}

To inspect a release's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for release `v15.2.1`.

```nohighlight
kubectl gs get releases v15.2.1 --output yaml
```

When applied without a release version argument, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get releases --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: release.giantswarm.io/v1alpha1
  kind: Release
...
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
