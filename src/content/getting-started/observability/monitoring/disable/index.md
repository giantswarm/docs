---
linkTitle: Disable monitoring
title: Disable Monitoring
description: This article explains how to turn off all monitoring for an entire workload cluster.
weight: 50
menu:
  main:
    identifier: getting-started-observability-monitoring-disable
    parent: getting-started-observability-monitoring
user_questions:
  - How can I disable monitoring on my cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2023-02-22
aliases:
  - /ui-api/observability/monitoring/disable
  - /observability/monitoring/disable
---

In this article you will learn how you can disable monitoring for your cluster.

## Introduction to monitoring

Each cluster created on the Giant Swarm platform benefits from our monitoring which allow us to provide you with 24/7 support to ensure best quality of service.

Each cluster is monitored by a dedicated Prometheus instance.
This comes by default and storage is reserved for data retention, storage size can be adjusted via [Prometheus Volume Sizing](https://docs.giantswarm.io/getting-started/observability/prometheus/volume-size/) feature.

## Why would I like to disable monitoring?

You might create clusters where you do not need support from our operations team, for instance because you might just want to try something new for a while, or you are running a playground cluster where you know what you are doing.
You may also have storage constraints and therefore would like to turn monitoring off.

## Implications

When you turn off monitoring this has several implication:

- Giant Swarm will not actively provide support on this cluster, as we will not be receiving alerts for this cluster.
- Giant Swarm will not be able to provide detailed investigation, as we will not have monitoring data over time to read from.

But nevertheless we are still here to help and support you in case you need it.

## How to disable monitoring?

To disable monitoring for a cluster you need to label the Cluster CR with:

```yaml
giantswarm.io/monitoring: "false"
```

You can achieve this by running the following command :

```nohighlight
$ kubectl label clusters.cluster.x-k8s.io myclustername giantswarm.io/monitoring=false --overwrite
cluster.cluster.x-k8s.io/myclustername labeled
```

Below is an example of a Cluster CR with monitoring disabled:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  annotations:
    cluster.giantswarm.io/description: Playground test Cluster
  labels:
    giantswarm.io/cluster: myclustername
    giantswarm.io/monitoring: "false"
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

