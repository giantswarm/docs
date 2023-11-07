---
linkTitle: Cluster autoscaler
title: Advanced cluster autoscaler configuration
description: Here we describe how you can customize the configuration of the managed cluster autoscaler service in your workload clusters.
weight: 90
menu:
  main:
    parent: advanced-cluster-management
user_questions:
  - Where can I find the ConfigMap to configure cluster-autoscaler?
  - What cluster-autoscaler options can I configure?
last_review_date: 2023-11-07
aliases:
  - /guides/advanced-cluster-autoscaler-configuration/
  - /guides/cluster-autoscaler/
  - /advanced/cluster-autoscaler/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

Your Giant Swarm installation comes with a default configuration for the [cluster-autoscaler addon](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)

You can override these defaults in a ConfigMap named `cluster-autoscaler-user-values`.

## Where is the user values ConfigMap

The following examples assume the cluster you are trying to configure has an id of `123ab`

You will find the `cluster-autoscaler-user-values` ConfigMap on the Control Plane in the `123ab` namespace:

```nohighlight
$ kubectl -n 123ab get cm cluster-autoscaler-user-values --context=control-plane
NAME                                   DATA      AGE
cluster-autoscaler-user-values         0         11m
```

-----

__Warning:__

Please do not edit any other cluster-autoscaler related ConfigMaps.

Only the user values ConfigMap is safe to edit.

-----

On cluster creation the user values ConfigMap is empty (or might not exist yet) and the following defaults will be applied to the final cluster-autoscaler deployment. To customize any of the configuration options, you just need to add the respective line(s) in the data field of the user ConfigMap.

## How to set configuration options using the user values ConfigMap

On the Control Plane, create or edit a ConfigMap named `cluster-autoscaler-user-values`
in the workload cluster namespace:

```yaml
# On the Control Plane, in the abc12 namespace

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
      scaleDownUtilizationThreshold: 0.30
```

## Configuration Reference

The following sections explain some of the configuration options and what their
defaults are. They show only the 'data' field of the ConfigMap for brevity.

The most recent source of truth for these values can be found in
the [values.yaml](https://github.com/giantswarm/cluster-autoscaler-app/blob/v1.1.4/helm/cluster-autoscaler-app/values.yaml) file of the cluster-autoscaler-app

### Scale down utilization threshold

The `scaleDownUtilizationThreshold` defines the proportion between requested resources and capacity, which under the value cluster-autoscaler will trigger the scaling down action.

Our default value is 65%, which means in order to scale down, one of the nodes has to have less utilization (CPU/memory) than this threshold.

```yaml
# 9.0.1 and greater
data:
  values: |
    configmap:
      scaleDownUtilizationThreshold: 0.65

# 9.0.0 and below
data:
  scaleDownUtilizationThreshold: 0.65
```

### Scan Interval

Define what interval is used to review the state for taking a decision to scale up/down. Our default value is 10 seconds.

```yaml
data:
  values: |
    configmap:
      scanInterval: "100s"
```

### Skip system pods

By default, the cluster-autoscaler will never delete nodes which run pods of the `kube-system` namespace (except `daemonset` pods). It can be modified by setting following property to `"false"`.

```yaml
data:
  values: |
    configmap:
      skipNodesWithSystemPods: "false"
```

### Skip pods with local storage

The cluster-autoscaler configuration by default deletes nodes with pods using local storage (`hostPath` or `emptyDir`). In case you want to disable this action, you need to set the following property to `"true"`.

```yaml
data:
  values: |
    configmap:
      skipNodesWithLocalStorage: "true"
```

### Balance similar node groups

> Added in release v17.0.0

The cluster-autoscaler configuration by default doesn't differentiate between node groups when scaling. In case you want to enable this action, you need to set the following property to `"true"`.

```yaml
data:
  values: |
    configmap:
      balanceSimilarNodeGroups: "true"
```

## Further reading

- [cluster-autoscaler Github repository](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)
- [Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
