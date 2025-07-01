---
linkTitle: get clusters
title: "'kubectl gs get clusters' command reference"
description: Reference documentation on how to list clusters and get details for a single cluster using 'kubectl gs'.
weight: 40
menu:
  principal:
    parent: reference-kubectlgs
user_questions:
  - How can I list clusters using kubectl?
  - How can I inspect clusters using kubectl?
last_review_date: 2024-11-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /vintage/use-the-api/kubectl-gs/get-clusters/
---

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a cluster in this case, or list several of them.

## Usage

### Get a list of clusters {#list}

Simply execute

```nohighlight
kubectl gs get clusters
```

to list some information on all clusters available to you in the current installation. Use `--all-namespace` (if you have the permission to do so) or specify a namespace using the `--namespace` flag.

For a Cluster API management cluster, the result looks like this:

```nohighlight
NAMESPACE                   NAME         AGE    CONDITION   RELEASE   SERVICE PRIORITY   ORGANIZATION            DESCRIPTION
org-giantswarm-production   operations   270d   READY       28.1.0    highest            giantswarm-production   Operations Cluster
org-giantswarm              gazelle      296d   READY       25.0.0    highest            giantswarm              Management Cluster
```

Here is some example output from a vintage management cluster:

```nohighlight
NAME    AGE  CONDITION   RELEASE   SERVICE PRIORITY   ORGANIZATION   DESCRIPTION
3i99p   1d   CREATED     12.1.4    highest            giantswarm     ced0ps kong pm
```

### Get specific cluster

When used with a cluster name as additional argument, the command will show details for a single cluster. Example:

```nohighlight
kubectl gs get clusters ab12c
```

Note: As an alternative to `get clusters`, `get cluster` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `NAME`: Unique identifier of the cluster.
- `AGE`: How long ago was the cluster created.
- `CONDITION`: Latest condition reported for the cluster. Either of:
    - `CREATING`: The cluster is currently being created.
    - `CREATED`: Cluster creation is finished (on vintage only).
    - `UPDATING`: The cluster is currently being updated, e. g. during an upgrade.
    - `UPDATED`: The cluster update is finished.
    - `DELETING`: The cluster is being deleted.
    - `READY`: The cluster is running (on Cluster API only).
- `RELEASE`: Workload cluster release version of the cluster. Only on vintage management clusters.
- `SERVICE PRIORITY`: [Service priority]({{< relref "/vintage/advanced/cluster-management/labelling-workload-clusters#service-priority" >}}) of the cluster.
- `ORGANIZATION`: Organization owning the cluster.
- `DESCRIPTION`: User-friendly description for the cluster.

The columns `CLUSTER VERSION` and `PREINSTALLED APPS VERSION` shown on Cluster API are currently not used.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get clusters` command. Use `kubectl gs get clusters --help` for a full list.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get clusters` is no different.

#### YAML output {#yaml}

To inspect a cluster's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for cluster `ab12c`. It would return the [Cluster](https://doc.crds.dev/github.com/kubernetes-sigs/cluster-api/cluster.x-k8s.io/Cluster/v1beta1) resource.

```nohighlight
kubectl gs get clusters ab12c --output yaml
```

When applied without a cluster name argument, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get clusters --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: cluster.x-k8s.io/v1beta1
  kind: Cluster
...
```

## Related

- [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
