---
title: AWS Cluster scaling
description: How to configure and manage the scaling of your AWS workload clusters on Giant Swarm.
weight: 20
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

Instead, `Karpenter` is a recommended addon that relies on the Kubernetes events to scale up or down the number of nodes in the cluster. It's select from a suite of instance types defined in a special `Provisioner` resources to match the workload requirements and can be configured to use spot instances to save costs. It's faster and more efficient than the cluster autoscaler, but does not operate well with base on-demand instances.

## How both work together

In most of the cases the advise is to have both controllers, cluster autoscaler and `Karpenter`, to be able to offer spot instances and faster scaling options, meanwhile cluster autoscaler manages a base on-demand capacity as fallback.

To avoid collisions between both, the cluster autoscaler is configured to have a lower priority than `Karpenter`, so it will react only after a pod is on `Pending` for a while (default 5 minutes).

## Configuration

### `Karpenter`

Our recommendation for the autoscaling configuration is to set two different profiles. One will target `Spot` compute and the other `On-Demand` instances. The `Spot` profile will have a higher weight to be prioritized over the `On-Demand` profile. And the `on-demand` profile will ensure that the cluster has a base capacity to handle the main workloads.

First, let's dive into what a `Provisioner` custom resource is to understand how to configure it. There are a set of parameters to help you define how the nodes should be provisioned:

- **labels**: Used to select which nodes should be managed by the provisioner.
- **limits**: Lets you set limits on the total CPU and Memory that can be used by the node pool, effectively stopping further node provisioning when those limits have been reached.
- **provider**: Define the launch template, node pool and the AWS tags for the nodes.
- **requirements**: An array of requirements defining the conditions to be met by the provisioner.

Let's see an example of a `Provisioner` configuration:

```yaml
apiVersion: karpenter.sh/v1alpha5
  kind: Provisioner
  metadata:
    name: spot-provisioner-west-1a-pool1
  spec:
    consolidation:
      enabled: true
    labels:
      cluster: mycluster
      managed-by: karpenter
      nodepool: pool1
      role: worker
    limits:
      resources:
        cpu: 4k
        memory: 4000Gi
    provider:
      launchTemplate: mycluster-pool1
      subnetSelector:
        giantswarm.io/machine-deployment: pool1
      tags:
        Name: mycluster-karpenter-spot-worker
        cluster: mycluster
        giantswarm.io/cluster: mycluster
        managed-by: karpenter
        nodepool: pool1
    requirements:
    - key: karpenter.k8s.aws/instance-family
      operator: In
      values:
      - m7i
      - ...
    - key: karpenter.k8s.aws/instance-size
      operator: In
      values:
      - 4xlarge
      - ...
    - key: topology.kubernetes.io/zone
      operator: In
      values:
      - eu-west-1a
    - key: karpenter.sh/capacity-type
      operator: In
      values:
      - spot
    weight: 10
```

Notice there is a `weight` parameter that defines the priority of the provisioner. The higher the weight, the higher the priority. Select it conveniently to prioritize the `Spot` instances over the `On-Demand` instances or other provisioners.

Also, you can see `consolidation` is enabled. This feature allows `Karpenter` to consolidate workloads on fewer nodes, reducing costs.

Now, let's see an `On-Demand` provisioner to complete the configuration example:

```yaml
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: ondemand-provisioner-west-1c-pool2
spec:
  consolidation:
    enabled: true
  labels:
    cluster: mycluster
    managed-by: karpenter
    nodepool: pool2
    role: worker
  limits:
    resources:
      cpu: 4k
      memory: 4000Gi
  provider:
    launchTemplate: mycluster-pool2
    subnetSelector:
      giantswarm.io/machine-deployment: pool2
    tags:
      Name: mycluster-karpenter-ondemand-worker
      cluster: mycluster
      giantswarm.io/cluster: mycluster
      managed-by: karpenter
      nodepool: pool2
  requirements:
  - key: karpenter.k8s.aws/instance-family
    operator: In
    values:
    - m7i
    - ...
  - key: karpenter.k8s.aws/instance-size
    operator: In
    values:
    - 4xlarge
  - key: topology.kubernetes.io/zone
    operator: In
    values:
    - eu-west-1c
  - key: karpenter.sh/capacity-type
    operator: In
    values:
    - on-demand
  weight: 2
```

As you see, the `weight` is lower than the `Spot` provisioner making the `Karpenter` controller to prioritize the `Spot` instances over the `On-Demand` instances. Also the `capacity-type` is set to `on-demand` to ensure the provisioner will use only on-demand instances.

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
