---
linkTitle: get releases
title: "'kubectl gs get releases' command reference"
description: Reference documentation on how to list releases and get details for a single release using 'kubectl gs'.
weight: 50
menu:
  principal:
    parent: reference-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I list releases in a cluster using kubectl?
  - How can I inspect releases using kubectl?
last_review_date: 2026-06-08
aliases:
  - /vintage/use-the-api/kubectl-gs/get-releases/
---

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
VERSION      STATUS       AGE   KUBERNETES   FLATCAR    CILIUM   COREDNS   OBSERVABILITY BUNDLE   SECURITY BUNDLE
aws-34.3.0   ACTIVE       24d   1.34.7       4593.2.1   1.4.3    1.30.0    2.8.0                  1.17.1
aws-34.4.0   ACTIVE       3d    1.34.7       4593.2.2   1.4.3    1.30.0    2.8.0                  1.17.1
eks-34.0.0   DEPRECATED   103d  1.34.4       4459.2.3   1.3.4    1.29.1    2.5.0                  1.16.1
eks-34.0.1   ACTIVE       48d   1.34.4       4459.2.3   1.3.4    1.30.0    2.5.0                  1.16.1
```

### Get specific release

When used with a release version as additional argument, the command will show details for a single release. Example:

```nohighlight
kubectl gs get releases aws-34.4.0
```

Note: As an alternative to `get releases`, `get release` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `VERSION`: Unique identifier of the release.
- `STATUS`: The state of the release. Possible states are:
    - `ACTIVE`: A stable release, fully supported.
    - `PREVIEW`: A preview for testing purposes only, not yet considered stable.
    - `WIP`: Work in progress, a release in development.
    - `DEPRECATED`: Has been replaced by a successor release. No longer recommended.
- `AGE`: How long ago was the release created.
- `KUBERNETES`: The version of Kubernetes provided by this release.
- `FLATCAR`: The version of Flatcar Container Linux provided by this release.
- `CILIUM`: The version of Cilium provided by this release.
- `COREDNS`: The version of CoreDNS provided by this release.
- `OBSERVABILITY BUNDLE`: The version of the observability bundle provided by this release.
- `SECURITY BUNDLE`: The version of the security bundle provided by this release.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get releases` command. Use `kubectl gs get releases --help` for a full list.

### `--active-only` {#flags-active-only}

If present, list only the releases that are currently marked as active.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get releases` is no different.
Similar to other `get` subcommands, you can specify the output format of `kubectl gs get releases` using the `--output` flag.

#### YAML output {#yaml}

To inspect a release's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for release `aws-34.4.0`.

```nohighlight
kubectl gs get releases aws-34.4.0 --output yaml
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

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
