---
linkTitle: Cluster size and autoscaling
title: Cluster size and autoscaling
description: This article explains options you have for defining the size of a Kubernetes cluster with Giant Swarm, and automatically scaling it
weight: 30
menu:
  main:
    parent: kubernetes
last_review_date: 2020-10-07
aliases:
  - /basics/cluster-size-autoscaling/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Cluster size and autoscaling

{{< platform_support_table aws="ga=v6.3.0" azure="ga=v13.1.0" >}}

## Introduction

Giant Swarm workload clusters on AWS and Azure provide the [Kubernetes cluster autoscaler](https://github.com/kubernetes/autoscaler) by default, to set the number of worker nodes in a cluster dynamically, based on demand.

On KVM installations, the cluster size is defined statically.

## Setting scaling limits

With the autoscaler taking control over the number of worker nodes, you only define the bounds or limits in which the cluster size can vary. This is possible both during cluster creation as well as after creation.

To enforce an exact cluster size and **effectively disable the autoscaler**, simply set the minimum and maximum worker node count to the same value. This is also the recommended way to control the number of worker nodes through external tooling via the Giant Swarm REST API.

## How the autoscaler works

When relying on the autoscaler to determine the number of worker nodes in your cluster, you may benefit from a deeper understanding of how the autoscaler decides when to increase or decrease the number of worker nodes. We recommend reading the [Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) for details. This document only highlights a few important aspects.

Whenever pods cannot be scheduled due to insufficient resources in the cluster, the autoscaler adds a worker node.

To decide whether a cluster can be scaled down, the autoscaler periodically calculates the **utilization** of a node based on CPU and memory requests of all running pods, compared to the node's total capacity.

**Note:** This means that your pods MUST be configured with CPU and memory requests in order to inform the autoscaler about the actual node utilization.
Pods without CPU and memory requests won't count towards the utilization as calculated by the autoscaler and won't trigger any scaling.

The current utilization is compared to a configurable _utilization threshold_, which is set {{% autoscaler_utilization_threshold %}} by default.
If the utilization is below the threshold, the autoscaler decides to remove the node.

## Minimal and default cluster size

When creating a cluster without specifying the number of worker nodes, {{% default_cluster_size_worker_nodes %}} worker nodes will be created. On supported AWS and Azure workload clusters, when not specified, the maximum number of worker nodes is also set to {{% default_cluster_size_max_worker_nodes %}}.

Technically, while you may be able to create and run smaller clusters successfully, we don't encourage this due to reduced resilience.

## Minimal worker node instance type

Relying on autoscaling may have an effect on the instance type you should use for your cluster. This is the result of the way the autoscaler decides when to remove a node, as described above.

With the services required to run a cluster, like DNS, kube-proxy, ingress and others, each node has a baseline utilization, even before you start your first workloads. Hence the minimal worker node instance types on AWS are those with the `.xlarge` suffix, providing 4 CPU cores. The default instance type for worker nodes is `{{% default_aws_instance_type %}}`.

For automatic down-scaling to work, utilization threshold and instance type have to fit together.
The default worker nodes instance type for AWS (`{{% default_aws_instance_type %}}`) and the default utilization threshold ({{% autoscaler_utilization_threshold %}}) are adjusted so that down-scaling should work as expected.

If you decide to run larger instance types, you may ask the Giant Swarm support team to adjust the utilization threshold of a particular cluster for you.

## Ingress controller replicas with autoscaling

With AWS and workload cluster release {{% first_aws_autoscaling_version %}}, the amount of Ingress Controller (IC) replicas is fixed to the minimum number of worker nodes when creating the cluster. This can mean two things:

- When scaling up a cluster from an initially low minimum number of worker nodes, there might not be enough IC replicas to fullfill all your requests.

- When scaling down a cluster from an initially high minimum number of workers, there may be several IC pods per worker node, using more resources than necessary.

When in doubt, please run load tests against your autoscaling cluster, in order to make sure you have the proper amount of IC replicas running.
Also feel free to contact the Giant Swarm support team to clarify any questions on this topic.

We plan to improve this behaviour in a release by scaling the IC using the Horizontal Pod Autoscaler (HPA), to better adapt the number of ICs to the load.
This would as a consequence lead to the worker node count being adapted to the demand for IC pods.
In workload clusters without autoscaling support, the number of Ingress Controller replicas scales linearly with the number of worker nodes.

## Further restrictions

- Scaling a cluster to zero worker nodes is currently not supported.
- The number of master nodes cannot be changed as of now.

## See also

- [Cluster Autoscaler advanced configuration]({{< relref "/advanced/cluster-autoscaler" >}})
- [Recommendations and Best Practices regarding cluster size]({{< relref "/kubernetes/best-practices#cluster-sizing" >}})
- [`gsctl create cluster`]({{< relref "/ui-api/gsctl/create-cluster" >}}): Creating a cluster
- [`gsctl scale cluster`]({{< relref "/ui-api/gsctl/scale-cluster" >}}): Scaling a cluster
- [`gsctl show cluster`]({{< relref "/ui-api/gsctl/show-cluster" >}}): Inspecting a cluster
- [API: Create cluster](/api/#operation/addCluster)
- [API: Modify cluster](/api/#operation/modifyCluster)
- [API: Get cluster details](/api/#operation/getCluster)
- [API: Get cluster status](/api/#operation/getClusterStatus)
- [Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
