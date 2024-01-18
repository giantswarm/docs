---
linkTitle: get nodepools
title: "'kubectl gs get nodepools' command reference"
description: Reference documentation on how to list node pools and get details for a single node pool using 'kubectl gs'.
weight: 50
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-nodepools/
  - /ui-api/kubectl-gs/get-nodepools/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I list node pools in a cluster using kubectl?
  - How can I inspect node pools using kubectl?
last_review_date: 2024-01-18
---

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a node pool in this case, or list several of them.

**Note:** Currently this command can only be used with vintage installations. We [intend](https://github.com/giantswarm/roadmap/issues/1519) to make it available for CAPI installations, to.

## Usage

### Get a list of node pools {#list}

Simply execute

```nohighlight
kubectl gs get nodepools
```

to list some information on all node pools available to you in the current installation.

Here is some example output:

```nohighlight
NAME    CLUSTER NAME   AGE  CONDITION   NODES MIN/MAX   NODES DESIRED   NODES READY   DESCRIPTION
ab12c   s921a          1d   READY       3/10            5               3             Production node pool
```

### Get specific node pool

When used with a node pool name as additional argument, the command will show details for a single node pool. Example:

```nohighlight
kubectl gs get nodepool ab12c
```

Note: As an alternative to `get nodepools`, `get nodepool` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `NAME`: Unique identifier of the node pool.
- `CLUSTER NAME`: Unique identifier of the cluster that the node pool belongs to.
- `AGE`: How long ago was the node pool created.
- `CONDITION`: Latest condition reported for the node pool. (Azure only)
- `NODES MIN/MAX`: Node pool autoscaler settings (if supported).
- `NODES DESIRED`: The total number of nodes that the node pool should have.
- `NODES READY`: The number of nodes in the node pool that are actually ready.
- `DESCRIPTION`: User friendly description for the node pool.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get nodepools` command. Use `kubectl gs get nodepools --help` for a full list.

### `--cluster-name/-c` {#flags-output}

If present, list the node pools that belong to this given workload cluster.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kubectl gs get nodepools` is no different.
Similar to other `get` subcommands, you can specify the output format of `kubectl gs get nodepools` using the `--output` flag.

#### YAML output {#yaml}

To inspect a node pool's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for node pool `ab12c`. On AWS that would be the [MachineDeployment]({{< relref "/use-the-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) resource printed. On Azure, it would return the [MachinePool]({{< relref "/use-the-api/management-api/crd/machinepools.exp.cluster.x-k8s.io.md" >}}) resource.

```nohighlight
kubectl gs get nodepool ab12c --output yaml
```

When applied without a node pool name argument, the output will be a list of resources. Example:

```nohighlight
$ kubectl gs get nodepools --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: cluster.x-k8s.io/v1beta1
  kind: MachineDeployment
...
```

## Related

- [`kubectl gs login`]({{< relref "/use-the-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
