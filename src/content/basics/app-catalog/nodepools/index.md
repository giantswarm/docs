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

## Advantages

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

## Lifecycle

Node pools can be created when creating a cluster

- via the Giant Swarm web interface ("happa")
- via the CLI command [`gsctl create cluster`](/reference/gsctl/create-ckuster/)

or any time after the cluster has been created

- via the Giant Swarm web interface
- via the CLI command [`gsctl add nodepool`](/reference/gsctl/add-nodepool/)

These tools also support modification of node pools and their deletion.

Once a node pool has been created, as soon as the workers are available, they will
join the cluster and appear in your `kubectl get nodes` listing. You can identify the
nodes' node pool using the `giantswarm.io/machine-deployment` label.

```nohighlight
kubectl get nodes \
  -o=jsonpath='{range .items[*]}{.metadata.labels.giantswarm\.io/machine-deployment}{"\t"}{.metadata.name}{"\n"}{end}' | sort
```

Some details of a node pool can be modified after creation:

- The node pool name
- The scaling range (min(max)

Settings like the instance type or the availability zone assignment cannot be change after creation.

## Assigning workloads to node pools

Knowing the node pool ID of the pool to use, you can use the `nodeSelector` method of assigning pods to the node pool.

Assuming that the node pool ID is `a1b2c`, your `nodeSelector` should look like this (for example):

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
  nodeSelector:
    giantswarm.io/machine-deployment: a1b2c
```

## Node pool deletion

You can delete a node pool at any time using the Giant Swarm API and user interfaces. When a node pool gets deleted,

- nodes in the pool will be cordoned (marked as unschedulable) and drained, resulting in Pods being unassigned from the nodes and containers being stopped.
- Then the actual nodes (EC2 instanced) will be removed.

If you are deleting a node pool running critical workloads, we recommend to take some
precautions:

- Make sure there is at least one node pool providing enough nodes to pick
up the workloads.
- Double-check any taints and node selectors of your workloads to make sure they can land on different nodes.
- For most control, cordon all of the node pool's nodes and then drain them manually, one by one.

Then pay close attention to the workloads being rescheduled on other nodes once nodes are drained.

## Node pools and the Giant Swarm API

Handling clusters with node pools requires an API schema different from the one used for clusters
with homogeneous worker nodes. We introduced a new API version path `v5` for this reason.

Using the v5 API endpoints, you can

- Create a new cluster
- Add a node pool to a cluster
- Rename a cluster
- Modify a node pool (for renaming or changing scaling settings)
- Delete a node pool

## Node pools and the cluster definition YAML format

Just as the Giant Swarm API schema for v4 (without node pools) and v5 (with node pools) clusters are different, the [cluster definition format](/reference/cluster-definition/) is different for both versions.

The new definition schema for v5 allows for defining cluster and node pool details in one file,
to be submitted for creation via the [`gsctl create cluster`](/reference/gsctl/create-cluster/) command.

## Support

Please note that we do not monitor node pools with less than three worker nodes and do not provide any proactive support for those.

Also please note that we do not monitor a cluster without any node pools.

```
TODO

- Consequences for maximum cluster size (IP range)
```

### Further reading

- [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/) from the official Kubernetes documentation
