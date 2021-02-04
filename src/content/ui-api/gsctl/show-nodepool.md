---
linkTitle: show nodepool
title: "'gsctl show nodepool' command reference"
description: The 'gsctl show nodepool' command shows details on a node pool.
weight: 210
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/show-nodepool/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl show nodepool`

The `gsctl show nodepool` command shows details on a [node pool]({{< relref "/advanced/node-pools" >}}).

## Usage

The command is called with the cluster and node pool ID as the only argument,
separated by a slash.

Example:

```nohighlight
gsctl show nodepool f01r4/op1dl
```

Here, `f01r4` is the cluster ID and `op1dl` is the node pool ID.

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl show nodepool "Cluster name"/op1dl
```

## Output

Example

```nohighlight
ID:                                            op1dl
Name:                                          General purpose node pool
Node instance type:                            m4.xlarge - 16 GB RAM, 4 CPUs each
Alike instances types:                         true
Availability zones:                            A
On-demand base capacity:                       0
Spot percentage above base capacity:           40
Node scaling:                                  Autoscaling between 2 and 10
Nodes desired:                                 3
Nodes in state Ready:                          3
Spot instances:                                1
CPUs:                                          12
RAM:                                           48 GB
```

Description of output rows:

- **ID**:                                  The node pool ID.
- **Name**:                                Name assigned to the node pool.
- **Node instance type**:                  The AWS EC2 instance type used for each worker node, plus the memory and CPU amount per node.
- **VM Size**:                             The Azure VM size used for each worker node, plus the memory and CPU amount per node.
- **Alike instance types**:                Whether similar instance types are used within this node pool (eg if m5.xlarge is defined also m4.xlarge is possible)
- **Availability zones**:                  The availability zone(s) assigned to this node pool, abbreviated to one letter. Note that it is not guaranteed that all shown availability zones have worker nodes at all times.
- **On-demand base capacity**:             Number of on-demand instances that this node pool needs to have until spot instances are used
- **Spot percentage above base capacity**: Percentage of spot instances used once the on-demand base capacity is fullfilled. A number of 40 would mean that 60% will be on-demand and 40% will be spot instances.
- **Node scaling**:                        Current scaling setting of the node pool. When the lower and upper end of the scaling range are the same number, the pool size is "Pinned" at  certain number of worker nodes. Otherwise the node pool uses the Kubernetes autoscaler to set the amount of worker nodes within the configured range.
- **Nodes desired**:                       The expected number of nodes. With auto-scaling active, this is the number determined by the autoscaler.
- **Nodes in state Ready**:                The current number of worker nodes which are in state `Ready`.
- **Spot instances**:                      The current number of worker nodes using spot instances.
- **CPUs**:                                The total number of CPU cores in this node pool.
- **RAM**:                                 The total amount of memory in this node pool.

## Related

- [`gsctl create nodepool`]({{< relref "/ui-api/gsctl/create-nodepool" >}}) - Add a node pool to a cluster
- [`gsctl list nodepools`]({{< relref "/ui-api/gsctl/list-nodepools" >}}) - List all node pools of a cluster
- [`gsctl update nodepool`]({{< relref "/ui-api/gsctl/update-nodepool" >}}) - Modify a node pool
- [`gsctl delete nodepool`]({{< relref "/ui-api/gsctl/delete-nodepool" >}}) - Delete a node pool
