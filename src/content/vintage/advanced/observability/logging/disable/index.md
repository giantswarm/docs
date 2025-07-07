---
linkTitle: Disable managed logging
title: Disable managed logging for a workload cluster
description: This article explains how to turn off all managed logging for an entire workload cluster.
weight: 50
menu:
  main:
    identifier: advanced-observability-logging-disable
    parent: advanced-observability-logging
user_questions:
  - How can I disable logging on my cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-02-28
---

In this article you will learn how you can disable managed logging for your cluster (i.e. logs of components to ensure the observability of the cluster).

## Introduction to logging

The managed logging stack allows Giant Swarm to provide 24/7 support based on your workload cluster logs. Currently, this component is pre-installed on workload clusters for the following implementations:

- {{% impl_title "vintage_aws" %}}, release v19.2.0 or newer

Logs of components deployed in the `kube-system` and `giantswarm` namespaces, as well as Kubernetes and node audit logs are collected by managed `promtail` pods and sent to a Loki instance running in your management cluster. You can access its logs by [accessing to the managed Grafana]({{< relref "/getting-started/observe-your-clusters-and-apps" >}}).

## Why would I like to disable logging?

You might create clusters where you do not need support from our operations team, for instance because you might just want to try something new for a while, or you are running a playground cluster where you know what you are doing.
You may also have storage or cost constraints and therefore would like to turn logging off.

## Implications

When you turn off logging on a workload cluster, Giant Swarm will not be able to provide detailed investigation on that cluster, as we will not have logging data over time to read from.

## How to disable logging?

To disable logging for a cluster you need to label the Cluster CR with:

```yaml
giantswarm.io/logging: "false"
```

You can achieve this by running the following command:

```nohighlight
$ kubectl label clusters.cluster.x-k8s.io myclustername giantswarm.io/logging=false --overwrite
cluster.cluster.x-k8s.io/myclustername labeled
```

Below is an example of a Cluster CR with logging disabled:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  annotations:
    cluster.giantswarm.io/description: Playground test Cluster
  labels:
    giantswarm.io/cluster: myclustername
    giantswarm.io/logging: "false"
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
  name: nzr5z
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSCluster
    name: myclustername:
    namespace: default
```
