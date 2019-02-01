+++
title = "Cluster Size and Autoscaling"
description = "This article explains options you have for defining the size of a Kubernetes cluster with Giant Swarm, and automatically scaling it"
date = "2019-01-17"
weight = 45
type = "page"
categories = ["basics"]
+++

# Cluster Size and Autoscaling

Starting with release version 6.3.0 for AWS, you can leverage the benefits of the [Kubernetes autoscaler](https://github.com/kubernetes/autoscaler) to define the number of worker nodes in a cluster based on demand.
The autoscaler is provided with every cluster of version >= 6.3.0 on AWS.

On Giant Swarm installations on Azure, on bare-metal, and on AWS prior to version 6.3.0, the cluster size would be defined statically.

## Setting scaling limits

With the autoscaler taking control over the number of worker nodes, you only define the bounds or limits in which the cluster size can vary. This is possible both during cluster creation as well as after creation.

To enforce an exact cluster size and **effectively disable the autoscaler**, simply set the minimum and maximum worker node count to the same value. This is also the recommended way in case you want to control the number of worker nodes through some external tooling via the Giant Swarm API.

## Minimal and default cluster size

When creating a cluster without specifying the number of worker nodes, **three** worker nodes will be created. This is also the minimal number supported by Giant Swarm. On AWS starting with release version 6.3.0, when not specified, the maximum number of worker nodes is also set to **three**.

Technically, while you may be able to create and run smaller clusters successfully, we don't encourage this due to reduced resilience. We explicitly deactivate all sorts of alerts for clusters with less than three worker nodes and won't get notified in case of any problems.

## Minimal worker node instance type

Relying on autoscaling may have an effect on the instance type you should use for your cluster.
To explain this more detail, it is helpful to explain how the autoscaler determines whether a node is needed or not.

The autoscaler periodically calculates the utilization of a node based on CPU and memory requests, compared to the node's total capacity.
The utilization is compared to a configurable _utilization threshold_, which is {{% autoscaler_utilization_threshold %}} by default.
If the utilization is below the threshold, the autoscaler decides to remove the node.
If it's above, it will keep the node.

With the services required to run a cluster, like DNS, kube-proxy, ingress and others, each node has a baseline utilization, even before you start your first workloads.
With small instance types, e. g. only 2 CPU cores, the utilization of an otherwise empty node can already be above {{% autoscaler_utilization_threshold %}}.
Using such a small instance type with the default utilization threshold of {{% autoscaler_utilization_threshold %}} would result in a cluster that would never get scaled down, effectively running unused worker nodes.

For down-scaling to work, utilization threshold and instance type have to fit together.
You yourself can select an appropriate instance type when creating a cluster.
We recommend to use types with at least 4 CPU cores for autoscaling clusters.
In addition, the Giant Swarm support team can also customize the utilization threshold for you. Setting the value to e. g. 60% could cause the autoscaler to remove a node with higher utilization.

## Further restrictions

- Scaling a cluster to zero worker nodes is currently not supported.
- The number of master nodes cannot be changed as of now.

## See also

- [Recommendations and Best Practices regarding cluster size](/guides/recommendations-and-best-practices/#cluster-sizing)
- [`gsctl create cluster`](/reference/gsctl/create-cluster/): Creating a cluster
- [`gsctl create cluster`](/reference/gsctl/scale-cluster/): Scaling a cluster
- [`gsctl show cluster`](/reference/gsctl/show-cluster/): Inspecting a cluster
- [API: Create cluster](/api/#operation/addCluster)
- [API: Modify cluster](/api/#operation/modifyCluster)
- [API: Get cluster details](/api/#operation/getCluster)
- [API: Get cluster status](/api/#operation/getClusterStatus)
- [Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
