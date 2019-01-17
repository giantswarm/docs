+++
title = "Cluster Size and Autoscaling"
description = "This article explains options you have for defining the size of a Kubernetes cluster with Giant Swarm, and automatically scaling it"
date = "2019-01-17"
weight = 45
type = "page"
categories = ["basics"]
+++

# Cluster Size and Autoscaling

Starting with release version X.X.X (TODO) for AWS, you can leverage the benefits of the [Kubernetes autoscaling components](https://github.com/kubernetes/autoscaler) to define the number of worker nodes in a cluster based on demand.

On Giant Swarm installations on Azure, on bare-metal, and on AWS prior to version X.X.X (TODO), the cluster size would be defined statically.

**Note:** the number of master nodes cannot be changed

## Setting scaling limits

With the autoscaler taking control over the number of worker nodes, you only define the bounds or limits in which the cluster size can vary. This is possible both during cluster creation as well as after creation.

To enforce an exact cluster size and **effectively disable the autoscaler**, simply set the minimum and maximum worker node count to the same value. This is also the recommended way in case you want to control the number of worker nodes through some external tooling via the Giant Swarm API.

## Minimal and default cluster size

When creating a cluster without specifying the number of worker nodes, **three** worker nodes will be created. This is also the minimal number supported by Giant Swarm. On AWS starting with release version X.X.X (TODO), when not specified, the maximum number of worker nodes is also set to **three**.

Technically, while you may be able to create and run smaller clusters successfully, we don't encourage this due to reduced resilience. We explicitly deactivate all sorts of alerts for clusters with less than three worker nodes and won't get notified in case of any problems.

Also note that we don't support scaling a cluster to zero worker nodes.

## See also

- [Recommendations and Best Practices regarding cluster size](/guides/recommendations-and-best-practices/#cluster-sizing)
- [Creating clusters with gsct](/reference/gsctl/create-cluster/)
- [Scaling clusters with gsctl](/reference/gsctl/scale-cluster/)
- [Inspecting clusters with gsctl](/reference/gsctl/show-cluster/)
- [API: Create cluster](/api/#operation/addCluster)
- [API: Modify cluster](/api/#operation/modifyCluster)
- [API: Get cluster details](/api/#operation/getCluster)
- [API: Get cluster status](/api/#operation/getClusterStatus)
