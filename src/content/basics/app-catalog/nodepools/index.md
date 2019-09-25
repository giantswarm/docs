---
title: Node Pools
description: A general description of the node pool concept, the benefits, and some details you should be aware of.
date: 2019-09-25
weight: 15
type: page
categories: ["basics"]
---

# Node Pools

Node pools are a new concept introduced in October 2019 with release {{% first_aws_nodepools_version %}} for AWS.

Prior the introduction of node pools, a cluster could only comprise one type of worker node. The cluster would have
to be scaled as a whole, and the availability zone distribution would apply to all worker nodes of a cluster. This
would mean that every worker node would have to be big enough to run the largest possible workload, in terms of
memory and CPU resources required. At the same time, all worker nodes in the cluster would have to use the same
availability zone distribution, even if some workloads wouldn't require the increased availability that would come
with using more availability zones.

Node pools are independent groups of worker nodes belonging to a cluster, where all nodes within a pool share a
common configuration. You can combine any sort of node pool within one cluster. Node pools can differ regarding

- EC 2 instance type
- Availability zone distribution
- Scaling configuration (number of nodes)

A node pool is identified by a unique ID that is generated on creation and by a name that you can pick as a cluster
administrator.


```
Content outline:

- Main purposes:
    - Offer different types of worker nodes, suited to different types of needs
    - Adjust scaling more flexibly
    - Adjust AZ placement more flexibly
- API changes (v5 instead of v5)
- Cluster definition changes
- Clusters can exist without any node pools and thus without any workloads.
- How to schedule workloads to certain node pools:
  - Use the unique node pool ID which is present as a node label as a selector
  - Alternatively use other labels, e. g. the EC2 instance type.
- Lifecycle:
  - Deleting a node pool
    - never affects the cluster owning the node pool.
    - means that nodes will be cordoned, drained, removed.
    - Whether workloads can be rescheduled depends on the remaining node pools and selectors.
- Mininum size for support: 3 worker nodes
- Consequences for maximum cluster size (IP range)
```
