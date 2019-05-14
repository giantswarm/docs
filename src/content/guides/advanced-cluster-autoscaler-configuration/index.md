+++
title = "Advanced Cluster Autoscaler Configuration"
description = "Here we describe how you can customize the configuration of the managed Cluster Autoscaler service in your clusters"
date = "2019-05-09"
type = "page"
weight = 40
tags = ["tutorial"]
+++

# Advanced Cluster Autoscaler Configuration

The [Cluster Autoscaler addon](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) running inside your cluster has additional configuration options and features that can be customized.

You can customize some of these configuration options on a per cluster basis through a ConfigMap inside your clusters. The ConfigMap is named `cluster-autoscaler-user-values` and is located in the `kube-system` namespace.

__Note:__ This feature is only available in more recent cluster versions. To find out if your cluster version supports customization through the ConfigMap, you can check if the above-mentioned ConfigMap is present.

```nohighlight
$ kubectl -n kube-system get cm cluster-autoscaler-user-values
NAME                                   DATA      AGE
cluster-autoscaler-user-values                    0         11m
```

On cluster creation the ConfigMap is empty and below-mentioned defaults will be applied to the final Cluster Autoscaler deployment. To customize any of the configuration options, you just need to add the respective line(s) in the data field of the user ConfigMap.

__Warning:__ Please do not edit any of the other Cluster Autoscaler related resources. Only the user ConfigMap is safe to edit.

## Scale down utilization threshold

The `scaleDownUtilizationThreshold` defines the proportion between requested resources and capacity, which under the value Cluster Autoscaler will trigger the scaling down action.

```yaml
data:
  scaleDownUtilizationThreshold: 0.65
```

Our default value is 65%, which means in order to scale down, one of the nodes has to have less utilization (CPU/memory) than this threshold.

# Scan Interval

Define what interval is used to review the state for taking a decision to scale up/down. Our default value is 10 seconds.

```yaml
data:
  scanInterval: "100s"
```

## Skip system pods

By default, the Cluster Autoscaler will never delete nodes which run pods of the `kube-system` namespace (except `daemonset` pods). It can be modified by setting following property to `"false"`.

```yaml
data:
  skipNodesWithSystemPods: "false"
```

## Skip pods with local storage

The Cluster Autoscaler configuration by default deletes nodes with pods using local storage (`hostPath` or `emptyDir`). In case you want to disable this action, you need to set the following property to `"true"`.

```yaml
data:
  skipNodesWithLocalStorage: "true"
```

## Further reading

- [Cluster Autoscaler Github repository](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler)
- [Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md)
