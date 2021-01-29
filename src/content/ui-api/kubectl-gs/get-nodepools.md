---
linkTitle: get nodepools
title: "'kubectl gs get nodepools' command reference"
description: Reference documentation on how to list node pools and get details for a single node pool using 'kubectl gs'.
weight: 30
menu:
  main:
    parent: uiapi-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `kubectl gs get nodepools`

{{% kgs_alias_assumption %}}

Like with all `get` commands in `kubectl`, this command can be used to get details on one item, a node pool in this case, or list several of them.

## Usage

### Get a list of node pools {#list}

Simply execute

```nohighlight
kgs get nodepools
```

to list some information on all node pools available to you in the current installation.

Here is some example output:

```nohighlight
ID      CLUSTER ID   CREATED                         CONDITION   NODES MIN/MAX   NODES DESIRED   NODES READY   DESCRIPTION
ab12c   s921a        2021-01-02 15:04:32 +0000 UTC   READY       3/10            5               3             Production node pool
```

### Get specific node pool

When used with a node pool ID as additional argument, the command will show details for a single node pool. Example:

```nohighlight
kgs get nodepool ab12c
```

Note: As an alternative to `get nodepools`, `get nodepool` will also work.

## Output {#columns}

The standard tabular output format features these columns:

- `ID`: Unique identifier of the node pool.
- `CLUSTER ID`: Unique identifier of the cluster that the node pool belongs to.
- `CREATED`: Date and time of the node pool CR creation.
- `CONDITION`: Latest condition reported for the node pool. (Azure only)
- `NODES MIN/MAX`: Node pool autoscaler settings (if supported).
- `NODES DESIRED`: The total number of nodes that the node pool should have.
- `NODES READY`: The number of nodes in the node pool that are actually ready.
- `DESCRIPTION`: User friendly description for the node pool.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `get nodepools` command. Use `kgs get nodepools --help` for a full list.

### `--cluster-id/-c` {#flags-output}

If present, list the node pools that belong to this given workload cluster.

### `--output/-o` {#flags-output}

`kubectl` commonly allows to specify the output format for all `get` subcommands. `kgs get nodepools` is no different.
Similar to other `get` subcommands, you can specify the output format of `kgs get nodepools` using the `--output` flag.

#### YAML output {#yaml}

To inspect a node pool's main custom resource in YAML notation, add the `--output yaml` flag (or `-o yaml` in short) to the command.

The following example command would print the main resource for node pool `ab12c`. On AWS that would be the [MachineDeployment](/reference/cp-k8s-api/machinedeployments.cluster.x-k8s.io/) resource printed. On Azure, it would return the [MachinePool](/reference/cp-k8s-api/machinepools.exp.cluster.x-k8s.io/) resource.

```nohighlight
kgs get nodepool ab12c --output yaml
```

When applied without a node pool ID argument, the output will be a list of resources. Example:

```nohighlight
$ kgs get nodepools --output yaml
apiVersion: v1
kind: List
items:
- apiVersion: cluster.x-k8s.io/v1alpha2
  kind: MachineDeployment
...
```

## Related

- [`kubectl gs login`]({{< relref "/ui-api/kubectl-gs/login" >}}) - Ensure an authenticated kubectl context.
