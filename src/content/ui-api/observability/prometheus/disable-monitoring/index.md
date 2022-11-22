---
linkTitle: Disable Monitoring
title: Disable Monitoring
description: A guide explaining how to disable cluster monitoring
weight: 50
menu:
  main:
    identifier: uiapi-observability-clustermonitoring
    parent: uiapi-observability-prometheus
user_questions:
  - How can I disable monitoring on my cluster ?
aliases:
  - /observability/prometheus/disable-monitoring
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2022-11-21
---

In this document you will learn how you can disable monitoring for your cluster.

## Introduction to monitoring

Each cluster created on the Giant Swarm Platform benefits from our monitoring which allow us to provide you with 24/7 support to ensure best quality of service.

Each cluster is monitored by a dedicated Prometheus instance.
This comes by default and storage is reserved for data retention, storage size can be adjusted via [Prometheus Volume Sizing](https://docs.giantswarm.io/ui-api/observability/prometheus/volume-size/) feature.

## Why would I like to disable monitoring

You might create clusters where you do not need support from our Operations team, for instance because you might just want to try something new for a short amount of time, or you are running a playground cluster where you know what you are doing.
You might as well have storage constraints and therefore would like to turn monitoring off.

## What does disabling monitoring involves

When you turn off monitoring this has several implication:

- Giantswarm will not actively provide support on this cluster, as we will not be receiving alerts for this cluster.
- Giantswarm will not be able to provide detailed investigation, as we will not have monitoring data over time to read from.

But nevertheless we are still here to help and support you in case you need it.

## How to disable monitoring ?

To disable monitoring for a cluster you need to label the Cluster CR with :

```yaml
giantswarm.io/monitoring: false
```

You can achieve this by running the following command :

```
$ k label cl nzr8z giantswarm.io/monitoring=false
cluster.cluster.x-k8s.io/nzr8z labeled
```

Below is an example of a cluster CR with monitoring disabled :

```
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  annotations:
    cluster.giantswarm.io/description: Playground test Cluster
  labels:
    giantswarm.io/cluster: nzr8z
    giantswarm.io/monitoring: false
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
  name: nzr5z
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSCluster
    name: nzr8z:
    namespace: default
```

