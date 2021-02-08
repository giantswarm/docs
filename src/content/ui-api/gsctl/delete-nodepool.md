---
linkTitle: delete nodepool
title: "'gsctl delete nodepool' command reference"
description: Explanation of the 'gsctl delete nodepool' command, which deletes a node pool.
weight: 100
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/delete-nodepool/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl delete nodepool`

The `gsctl delete nodepool` command deletes a [node pool]({{< relref "/advanced/node-pools" >}}).

Deleting a node pool means that all worker nodes in the pool will be drained,
cordoned and then terminated.

In case you are running production workloads on the node pool you want to delete,
make sure that there is at least one other node pool with capacity to
schedule the workloads. Also check whether label selectors, taints and
tolerations will allow scheduling on other pool's worker nodes. The best
way to observe this is by manually cordoning and draining the pool's
worker nodes and checking workload's node assignments, before issuing
the `delete nodepool` command.

**Note:** Data stored outside of persistent volumes will be lost and there is
no way to undo this.

## Usage

The command is called with the cluster and node pool ID as the only argument,
separated by a slash.

Example:

```nohighlight
gsctl delete nodepool f01r4/op1dl
```

Here, `f01r4` is the cluster ID and `op1dl` is the node pool ID.

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl delete nodepool "Cluster name"/op1dl
```

A confirmation will be required to finally delete the node pool. To suppress this
confirmation, add the `--force` option.

## Related

- [`gsctl create nodepool`]({{< relref "/ui-api/gsctl/create-nodepool" >}}) - Add a node pool to a cluster
- [`gsctl list nodepools`]({{< relref "/ui-api/gsctl/list-nodepools" >}}) - List all node pools of a cluster
- [`gsctl show nodepool`]({{< relref "/ui-api/gsctl/show-nodepool" >}}) - Show details for a node pool
- [`gsctl update nodepool`]({{< relref "/ui-api/gsctl/update-nodepool" >}}) - Modify a node pool
