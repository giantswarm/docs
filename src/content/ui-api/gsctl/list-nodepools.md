---
title: "'gsctl list nodepools' command reference"
description: "The 'gsctl list nodepools' command shows all node pools of a cluster."
weight: 44
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl list nodepools`

The `gsctl list nodepools` command lists all [node pools](/basics/nodepools/) of a cluster.

## Usage

Execute the command with the cluster ID as the only argument. Example:

```nohighlight
gsctl list nodepools 3if4
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl list nodepools "Cluster name"
```

## Output

The result will be a table of all node pools of a specific cluster with the following details in columns:

- `ID`:              Node pool identifier (unique within the cluster)
- `NAME`:            Name specified for the node pool, usually indicating the purpose
- `AZ`:              Availability zone letters used by the node pool, separated by comma
- `INSTANCE TYPE`:   EC2 instance type used for worker nodes
- `ALIKE`:           Whether similar instance types are used within this node pool (e. g. if `m5.xlarge` is defined also `m4.xlarge` is possible)
- `ON-DEMAND-BASE`:  Number of on-demand instances that this node pool needs to have until spot instances are used
- `SPOT-PERCENTAGE`: Percentage of spot instances used once the on-demand base capacity is fulfilled. A number of 40 would mean that 40% will be spot and 60% will be on-demand instances.
- `NODES MIN/MAX`:   The minimum and maximum number of worker nodes in this pool
- `NODES DESIRED`:   Current desired number of nodes as determined by the autoscaler
- `NODES READY`:     Number of nodes that are in the Ready state in kubernetes
- `SPOT INSTANCES`:  Number of nodes using spot instances
- `CPUS`:            Sum of CPU cores in nodes that are in state Ready
- `RAM (GB)`:        Sum of memory in GB of all nodes that are in state Ready

## Argument reference

- `--output` or `-o`: Using this flag with the value `json`, the output can be printed in JSON format. This is convenient for use in automation. The default output format is `table`.

## Related

- [`gsctl create nodepool`](/reference/gsctl/create-nodepool/) - Add a node pool to a cluster
- [`gsctl show nodepool`](/reference/gsctl/show-nodepool/) - Show details for a node pool
- [`gsctl update nodepool`](/reference/gsctl/update-nodepool/) - Modify a node pool
- [`gsctl delete nodepool`](/reference/gsctl/delete-nodepool/) - Delete a node pool
