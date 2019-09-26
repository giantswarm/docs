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

### Lifecycle

Node pools can be created when creating a cluster

- via the Giant Swarm web interface ("happa")
- via the CLI command [`gsctl create cluster`](/reference/gsctl/create-ckuster/)

or any time after the cluster has been created

- via the Giant Swarm web interface
- via the CLI command [`gsctl add nodepool`](/reference/gsctl/add-nodepool/)

These tools also support modification (renaming, changing scaling settings) of node pools
and their deletion.

Once a node pool has been created, as soon as the workers are available, they will
join the cluster and appear in your `kubectl get nodes` listing. You can identify the
nodes' node pool using the `giantswarm.io/machine-deployment` label.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.giantswarm\.io/machine-deployment}{"\t"}{.metadata.name}{"\n"}{end}' | sort
```

### Node pool deletion

When a node pool gets deleted,

- nodes in the pool will be cordoned (marked as unschedulable) and drained, resulting in Pods being unassigned from the nodes and containers being stopped.
- Then the actual nodes (EC2 instanced) will be removed.

If you are deleting a node pool running critical workloads, we recommend to take some
precautions:

- Make sure there is at least one node pool providing enough nodes to pick
up the workloads.
- Double-check any taints and node selectors of your workloads to make sure they can land on different nodes.
- For most control, cordon all of the node pool's nodes and then drain them manually, one by one.

Then pay close attention to the workloads being rescheduled on other nodes once nodes are drained.

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
