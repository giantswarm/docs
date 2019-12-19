+++
title = "gsctl Command Reference: show nodepool"
description = "The 'gsctl show nodepool' command shows details on a node pool."
date = "2019-12-19"
type = "page"
weight = 44
+++

# `gsctl show nodepool`

The `gsctl show nodepool` command shows details on a [node pool](/basics/nodepools/).

## Usage

The command is called with the cluster and node pool ID as the only argument,
separated by a slash.

Example:

```nohighlight
gsctl show nodepool f01r4/op1dl
```

Here, `f01r4` is the cluster ID and `op1dl` is the node pool ID.

## Output

Example

```nohighlight
ID:                    op1dl
Name:                  First test node pool
Node instance type:    m4.xlarge - 16 GB RAM, 4 CPUs each
Availability zones:    A
Node scaling:          Pinned to 2
Nodes desired:         3
Nodes in state Ready:  3
CPUs:                  12
RAM:                   48 GB
```

Description of output rows:

- **ID**:                    The node pool ID.
- **Name**:                  Name assigned to the node pool.
- **Node instance type**:    The AWS EC2 instance type used for each worker node, plus the memory and CPU amount per node.
- **Availability zones**:    The availability zone(s) assigned to this node pool, abbreviated to one letter. Note that it is not guaranteed that all shown availability zones have worker nodes at all times.
- **Node scaling**:          Current scaling setting of the node pool. When the lower and upper end of the scaling range are the same number, the pool size is "Pinned" at  certain number of worker nodes. Otherwise the node pool uses the Kubernetes autoscaler to set the amount of worker nodes within the configured range.
- **Nodes desired**:         The expected number of nodes. With auto-scaling active, this is the number determined by the autoscaler.
- **Nodes in state Ready**:  The current number of worker nodes which are in state `Ready`.
- **CPUs**:                  The total number of CPU cores in this node pool.
- **RAM**:                   The total amount of memory in this node pool.

## Related

- [`gsctl create nodepool`](/reference/gsctl/create-nodepool/) - Add a node pool to a cluster
- [`gsctl list nodepools`](/reference/gsctl/list-nodepools/) - List all node pools of a cluster
- [`gsctl update nodepool`](/reference/gsctl/update-nodepool/) - Modify a node pool
- [`gsctl delete nodepool`](/reference/gsctl/delete-nodepool/) - Delete a node pool
