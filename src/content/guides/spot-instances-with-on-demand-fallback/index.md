---
title: Using on-demand instances as fall-back when spot instances are unavailable on AWS
description: When using spot instances in a node pool on AWS, it can happen that the node pool cannot be scaled up as not enough spot instances are available. This guide shows you how to configure cluster-autoscaler in a way to provide on-demand instances as a back-up automatically.
date: "2020-07-01"
type: page
weight: 120
tags: ["tutorial"]
---

# Using on-demand instances as fall-back when spot instances are unavailable

As of release v{{% first_aws_spotinstances_version %}} on AWS, node pools can use [spot instances](/basics/nodepools/#on-demand-spot). Users can select for each node pool which percentage of nodes should be covered by spot instances and by on-demand instances respectively. And users can define a base amount of on-demand instances that will be used, to ensure at least a certain amount of worker nodes are available at any time.

However, it is still possible that the node pool is in need of more worker nodes and there are just no spot instances available matching the request, based on the availability zone and the instance type(s). In this case the node pool cannot be scaled up. As a result, workloads will likely remain unscheduled.

To ensure enough capacity in a cluster, this guide presents a solution where

- two node pools exist: one configured to only use spot instances, the other one to only use on-demand instances.
- cluster-autoscaler is configured to scale up the spot node pool first, and only if that fails, scale up the on-demand node pool.

Credit where credit is due: this solution has been proposed [in a blog post by Nir Forer](https://blog.doit-intl.com/running-eks-workloads-on-spot-instances-with-on-demand-instances-fallback-14bef39ce689). We adapt it here to match exactly the situation of Giant Swarm tenant clusters on AWS.

**Note:** This guide has been written for release v11.4.0 with [cluster-autoscaler](https://github.com/kubernetes/autoscaler) v1.16.5, provided via our [cluster-autoscaler-app](https://github.com/giantswarm/cluster-autoscaler-app) version [v1.16.0](https://github.com/giantswarm/cluster-autoscaler-app/releases/tag/v1.16.0).

## Cluster set-up

First, create a cluster with at least version 11.x.x for the purpose of this tutorial.

Next, create two node pools.

1. Name: Spot,
   Enable spot instances: yes,
   Spot instance percentage: 100 percent,
   Scaling range: min=1

2. Name: On-Demand,
   Instance type: the same as selected for the "Spot" node pool,
   Enable spot instances: no,
   Scaling range: min=1

If it is important to you that the nodes in both node pools run in the same availability zone(s), you have to select the matching zones manually for each node pool.

Make sure there are no other node pools in the cluster.

Finally, once you have create the cluster and the two node pools, take note of their IDs. You will need them in the next steps.

## Autoscaler expander configuration

First we create a ConfigMap manifest to provide configuration for the cluster-autoscaler's `priority` expander. This expander decides which node pool to scale up, based on a defined priority value.

Let's assume that our Spot node pool has the ID `sp0ti` and the on-demand node pool has ID `0ndmd`. We apply these two node pool ID in the ConfigMap as shown below:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-autoscaler-priority-expander
  namespace: kube-system
data:
  priorities: |-
    10:
      - .*0ndmd.*
    20:
      - .*sp0ti.*
```

The `.data.priorities` part defines a map of priority values and regular expressions to select the Auto Scaling Group (ASG) associated with the node pool. Since with Giant Swarm the node pool ID is part of the respective ASG name, we have to apply the IDs here.

Now this ConfigMap must be deployed in the (tenant) cluster with your two node pools.

If you are not authenticated with the cluster's Kubernetes API yet, create a key pair via the web UI or via [`gsctl create kubeconfig`](/reference/gsctl/create-kubeconfig/).

With the above manifest edited according to your IDs and stored as `expander-cm.yaml`, use this command:

```nohighlight
kubectl apply -f ./expander-cm.yaml
```

## Autoscaler app configuration

Now we have to tell cluster-autoscaler to actually use the `priority` expander, which we have provided configuration for in the previous step. As you can see in the default `values.yaml` of the cluster-autoscaler-app ([here for v1.1.4 of the app](https://github.com/giantswarm/cluster-autoscaler-app/blob/v1.1.4/helm/cluster-autoscaler-app/values.yaml#L12)), normally the `least-waste` expander would be used, which optimizes for highest possible node utilization.

To switch the expander, we provide a user ConfigMap as described in our guide on [advanced cluster autoscaler configuration](/guides/advanced-cluster-autoscaler-configuration/).

In contrast to the previous step, this is not done in the tenant cluster, but in the control plane instead. So this step requires write access to the [Control Plane Kubernetes API](/basics/api/#cp-k8s-api). Please contact your Giant Swarm Solution Engineer in case you need assistance.

The user ConfigMap has to reside in the namespace named after the (tenant) cluster ID, so make sure to adapt `.metadata.labels.namespace` to your cluster ID.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: cluster-autoscaler
  name: cluster-autoscaler-user-values
  namespace: abc12
data:
  values: |
    configmap:
      expander: priority
```

Save this manifest to e. g. `cluster-autoscaler-user-values.yaml` and apply it using

```nohighlight
kubectl apply -f ./cluster-autoscaler-user-values.yaml
```

## Test and observe

Back to the tenant cluster, let's deploy some workloads. Here is a simple deployment manifest we can use for the purpose.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx
  namespace: default
spec:
  replicas: 10
  revisionHistoryLimit: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        imagePullPolicy: Always
        name: nginx
        resources:
          requests:
            cpu: "1"
            memory: 1Gi
      restartPolicy: Always
```

This would try to create 10 pods, where each one would request 1 CPU and 1 GiB of memory.

Once you apply this to the tenant cluster, watch the autoscaler logs using this command:

```nohighlight
kubectl -n kube-system logs -l app=cluster-autoscaler -f
```

The logs should show that cluster-autoscaler is registering the two Auto scaling Groups (ASGs) belonging to our node pools, similar to this:

```nohighlight
I0701 11:10:16.028372       1 auto_scaling_groups.go:138] Registering ASG cluster-cp983-tcnp-sp0ti-NodePoolAutoScalingGroup-139WETDOF86WA
I0701 11:10:16.028394       1 auto_scaling_groups.go:138] Registering ASG cluster-cp983-tcnp-0ndmd-NodePoolAutoScalingGroup-1B8IU42LTSOYU
```

When the deployment has been scaled up, some line like this should appear:

```nohighlight
I0701 11:16:47.077234       1 priority.go:167] priority expander: cluster-cp983-tcnp-sp0ti-NodePoolAutoScalingGroup-139WETDOF86WA chosen as the highest available
```

## Final notes

Keep in mind that the configuration for the cluster-autoscaler priority expander contains your node pool IDs. So once you decide to create new node pools, make sure to update the configuration.
