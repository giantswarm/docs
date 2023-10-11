---
linkTitle: Disable logging
title: Disable Logging
description: This article explains how to turn off all logging for an entire workload cluster.
weight: 50
menu:
  main:
    identifier: getting-started-observability-logging-disable
    parent: getting-started-observability-logging
user_questions:
  - How can I disable logging on my cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2023-10-11
aliases:
  - /ui-api/observability/logging/disable
  - /observability/logging/disable
---

In this article you will learn how you can disable logging for your cluster.

## Introduction to logging

Since releases 19.1.0, cluster created on the Giant Swarm platform benefits from our logging stack which allow us to provide you with 24/7 support to ensure best quality of service.
Hence we are able to follow components lifecycle and to debug incidents more efficiently.

/!\ Disclaimer: the logging is enabled by default in 19.1.0.

Each components logs deployed in the `kube-system` and `giantswarm` namespaces as well as kubernetes and machine audit logs are collected by our managed `promtail` pods and sent to a Loki instance running in your management cluster. You can access its logs by accessing our managed Grafana.

## Why would I like to disable logging?

You might create clusters where you do not need support from our operations team, for instance because you might just want to try something new for a while, or you are running a playground cluster where you know what you are doing.
You may also have storage constraints and therefore would like to turn logging off.

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
