---
linkTitle: get clusters
title: "'kubectl gs get clusters' command reference"
description: Reference documentation on how to list clusters and get details for a single cluster using 'kubectl gs'.
weight: 20
menu:
  main:
    parent: uiapi-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `kubectl gs get clusters`

{{% kgs_alias_assumption %}}

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a cluster in this case, or list several of them.

## Usage

### Get a list of clusters {#list}

Simply execute

```nohighlight
kgs get clusters
```

to list some information on all clusters available to you in the current installation.

Here is some example output:

```nohighlight
ID      CREATED                         CONDITION   RELEASE   ORGANIZATION   DESCRIPTION
3i99p   2020-09-29 11:51:52 +0000 UTC   CREATED     12.1.4    giantswarm     ced0ps kong pm
```

### Get specific cluster

When used with a cluster ID as additional argument, the command will show details for a single cluster. Example:

```nohighlight
kgs get clusters ab12c
```

Note: As an alternative to `get clusters`, `get cluster` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `ID`: Unique identifier of the cluster.
- `CREATED`: Date and time of the Cluster CR creation.
- `CONDITION`: Latest condition reported for the cluster. Either of:
    - `CREATING`: The cluster is currently being created.
    - `CREATED`: Cluster creation is finished.
    - `UPDATING`: The cluster is currently being updated, e. g. during an upgrade.
    - `UPDATED`: The cluster update is finished.
    - `DELETING`: The cluster is being deleted.
- `RELEASE`: Workload cluster release version of the cluster.
- `ORGANIZATION`: Organization owning the cluster.
- `DESCRIPTION`: User friendly description for the cluster.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get clusters` command. Use `kgs get clusters --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kgs get clusters` is no different.

#### YAML output {#yaml}

To inspect a cluster's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for cluster `ab12c`. It would return the [Cluster]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) resource.

```nohighlight
kgs get clusters ab12c --output yaml
```

When applied without a cluster ID argument, the output will be a list of resources. Example:

```nohighlight
$ kgs get clusters --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: cluster.x-k8s.io/v1alpha3
  kind: Cluster
...
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
