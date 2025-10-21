---
title: AWS Cluster scaling
description: How to configure and manage the scaling of your AWS workload clusters on Giant Swarm.
weight: 20
aliases:
  - /vintage/getting-started/sizing-multi-tenancy
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-clusters-scaling
last_review_date: 2025-01-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I scale my workload clusters on Giant Swarm using `Karpenter` and cluster autoscaler?
---

At Giant Swarm, your workload clusters run with [cluster autoscaler](https://github.com/kubernetes/autoscaler) and [`Karpenter`](https://karpenter.sh/) to reach optimal scaling for your workloads and keeping the costs at minimum. This tutorial will guide you through the configuration and management of both.

The cluster autoscaler is running by default in all your cluster and it is responsible for scaling the number of nodes on the different node pools. It's triggered by not schedule pods, pods in `Pending` state, making the controller increase the number of desired nodes in the node pool. Indeed it modifies the `AutoScalingGroup` to reflect the new desired capacity.

Instead, `Karpenter` is a recommended add-on that relies on the Kubernetes events to scale up or down the number of nodes in the cluster. It's select from a suite of instance types defined in a special `Provisioner` resources to match the workload requirements and can be configured to use spot instances to save costs. It's faster and more efficient than the cluster autoscaler, but it's harder to configure and manage.

## How both work together

In most of the cases the advise is to have both controllers, cluster autoscaler and `Karpenter`, to be able to offer spot instances and faster scaling options, meanwhile cluster autoscaler manages a base on-demand capacity as fallback.

To avoid collisions between both, the cluster autoscaler is configured to have a lower priority than `Karpenter`, so it will react only after a pod is on `Pending` for a while (default 5 minutes).

## Configuration

### Karpenter

You can learn more about the Karpenter configuration in the [node pools configuration page]({{< ref "/tutorials/fleet-management/cluster-management/node-pools" >}}).

### Cluster autoscaler

The cluster autoscaler is automatically configured in the workload cluster. The settings when running together with `Karpenter` makes the cluster autoscaler to only take action after a pod is not reconciled for five minutes.

When checking the flags provided to the controller, you see:

```yaml
  containers:
  - args:
    - --scan-interval=30s
    - --skip-nodes-with-system-pods=false
    - --skip-nodes-with-local-storage=false
    - --new-pod-scale-up-delay=300s
    - --scale-down-utilization-threshold=0.7
    - --scale-down-unneeded-time=5m0s
```

You can learn more about those values in the [cluster autoscaler configuration page]({{< ref "/tutorials/fleet-management/cluster-management/cluster-autoscaler" >}}).
