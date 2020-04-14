---
title: "gsctl Command Reference: list nodepools"
description: "The 'gsctl list nodepools' command shows all node pools of a cluster."
date: "2020-03-11"
type: page
weight: 44
---

# `gsctl list nodepools`

The `gsctl list nodepools` command lists all [node pools](/basics/nodepools/) of a cluster.

## Usage

Execute the command with the cluster ID as the only argument. Example:

```nohighlight
$ gsctl list nodepools 3if4
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
$ gsctl list nodepools "Cluster name"
```

## Output

The result will be a table of all node pools of a specific cluster with the following details in columns:

- `ID`:             Node pool identifier (unique within the cluster)
- `NAME`:           Name specified for the node pool, usually indicating the purpose
- `AZ`:             Availability zone letters used by the node pool, separated by comma
- `INSTANCE TYPE`:  EC2 instance type used for worker nodes
- `NODES MIN/MAX`:  The minimum and maximum number of worker nodes in this pool
- `NODES DESIRED`:  Current desired number of nodes as determined by the autoscaler
- `NODES READY`:    Number of nodes that are in the Ready state in kubernetes
- `CPUS`:           Sum of CPU cores in nodes that are in state Ready
- `RAM (GB)`:       Sum of memory in GB of all nodes that are in state Ready

## Related

- [`gsctl create nodepool`](/reference/gsctl/create-nodepool/) - Add a node pool to a cluster
- [`gsctl show nodepool`](/reference/gsctl/show-nodepool/) - Show details for a node pool
- [`gsctl update nodepool`](/reference/gsctl/update-nodepool/) - Modify a node pool
- [`gsctl delete nodepool`](/reference/gsctl/delete-nodepool/) - Delete a node pool
