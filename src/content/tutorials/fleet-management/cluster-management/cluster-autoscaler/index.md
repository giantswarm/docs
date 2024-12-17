---
linkTitle: Cluster autoscaler
title: Advanced cluster autoscaler configuration
description: Here we describe how you can customize the configuration of the managed cluster autoscaler service in your workload clusters.
weight: 90
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-clusters-cluster-autoscaler
user_questions:
  - Where can I find the ConfigMap to configure cluster-autoscaler?
  - What cluster-autoscaler options can I configure?
last_review_date: 2024-12-13
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

In Giant Swarm platform, your workload clusters come with default autoscaling functionality. Today, it's supported by {{/*% autoscaling_supported_versions*/%}}, but our goal is to bring this feature to all supported providers.

The cluster autoscaler runs in the workload cluster and is responsible for scaling the number of nodes in the cluster. The configuration though is managed in the management cluster though. The autoscaling controller has a default configuration for the [cluster-autoscaler addon](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler). To configure the `cluster-autoscaler` further, you need to access the platform API. [Learn how to access the platform API]({{< relref "/getting-started/access-to-platform-api" >}}).

To extend the configuration, you need to override these defaults using a `ConfigMap` with the convention name `cluster-autoscaler-user-values`.

## Where is the user values ConfigMap

The following examples assume the cluster you are trying to configure has an id of `myclustername`.

You will find the `ConfigMap` named `myclustername-cluster-autoscaler-user-values` in the organization namespace of your cluster:

```text
$ kubectl -n org-company get cm myclustername-cluster-autoscaler-user-values
NAME                                       DATA      AGE
myclustername-cluster-autoscaler-user-values         0         11m
```

## How to set configuration options using the user values ConfigMap

On the platform API, create or edit a ConfigMap named `myclustername-cluster-autoscaler-user-values`
in the workload cluster namespace:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  labels:
    app: cluster-autoscaler
  name: myclustername-cluster-autoscaler-user-values
  namespace: myorg
data:
  values: |
    configmap:
      scaleDownUtilizationThreshold: 0.30
```

## Configuration reference

The following sections explain some of the configuration options and what their defaults are. They show only the `data` field of the ConfigMap for brevity.

The most recent source of truth for these values can be found in the [values.yaml](https://github.com/giantswarm/cluster-autoscaler-app/blob/v1.30.3-gs1/helm/cluster-autoscaler-app/values.yaml) file of the `cluster-autoscaler-app`.

### Scale down utilization threshold

The `scaleDownUtilizationThreshold` defines the proportion between requested resources and capacity. Once utilization drops below this value, cluster autoscaler will consider a node as removable.

Our default value is 70%, which means in order to scale down, one of the nodes has to have less utilization (CPU/memory) than this threshold. You can adjust this value to your needs as shown below:

```yaml
data:
  values: |
    configmap:
      scaleDownUtilizationThreshold: 0.65
```

### Scan interval

Defines what interval is used to review the state for taking a decision to scale up/down. Our default value is 10 seconds.

```yaml
data:
  values: |
    configmap:
      scanInterval: "100s"
```

### Skip system pods

By default, the cluster autoscaler will never delete nodes which run pods of the `kube-system` namespace (except `daemonset` pods). This rule can be deactivated by setting the following property to false.

```yaml
data:
  values: |
    configmap:
      skipNodesWithSystemPods: "false"
```

### Skip pods with local storage

The cluster autoscaler by default deletes nodes with pods using local storage (`hostPath` or `emptyDir`). In case you want to protect these nodes from removal, you can to set the following property to true.

```yaml
data:
  values: |
    configmap:
      skipNodesWithLocalStorage: "true"
```

### Balance similar node groups

The cluster autoscaler by default doesn't differentiate between node groups when scaling. In case you want to enable considering node groups, you need to set the following property to true.

```yaml
data:
  values: |
    configmap:
      balanceSimilarNodeGroups: "true"
```

Read [the Kubernetes autoscaler FAQ](https://github.com/kubernetes/autoscaler/blob/master/cluster-autoscaler/FAQ.md) to learn more about the cluster autoscaler and its configuration options.
