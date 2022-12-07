---
linkTitle: Prometheus Volume Size
title: Prometheus Volume Sizing
description: A guide explaining how to resize the Prometheus persistent volume to fit your needs
weight: 50
menu:
  main:
    identifier: getting-started-observability-prometheusvolumesize
    parent: getting-started-observability-prometheus
user_questions:
  - How can I shrink the persistent volume of the Giant Swarm managed Prometheus?
  - How can I expand the persistent volume of the Giant Swarm managed Prometheus?
  - Why would I resize the Giant Swarm managed Prometheus persistent volume ?
aliases:
  - /observability/prometheus/volume-size
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2022-10-26
---

In this document you will learn how to size the Prometheus persistent volume.

Prometheus uses a persistent volume to store its recorded metrics and, for historical reasons, we decided to define the needed capacity to 100Gi per cluster (Workload and management clusters alike).


__Warning:__ 
* This feature and the documentation is quite new, so do not hesitate to ask for support or help us improve this documentation.


## Why would I like to resize the volume
Our observability architecture is based on one Prometheus instance per workload cluster.
As mentioned above, the Prometheus volume is set to 100Gi.
This capacity is the same for a small or a large cluster.

Imagine that you want to create multiple testing clusters for a training.
You don't need to have 100Gi reserved for each cluster.
It would be useful to set a smaller size for each Prometheus volume.

On the other hand, if you have large clusters with lots of traffic, and so lots of metrics to store, you might like to set a larger size for each Prometheus volume.

## How can I resize Prometheus volume
The Prometheus volume size can be set on the cluster CR using the dedicated annotation `monitoring.giantswarm.io/prometheus-volume-size`

Three values are possible:
* `small` = 30 Gi
* `medium` = 100 Gi
* `large` = 200 Gi

`medium` is the default value, so if the annotation is not set, so the volume size will be created with a size of 100Gi.

Below is an example of a cluster CR defining a small Prometheus volume:
```
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  annotations:
    cluster.giantswarm.io/description: AWS Production Cluster.
    monitoring.giantswarm.io/prometheus-volume-size: small
  labels:
    tag.provider.giantswarm.io/Environment: PROD
    cluster-operator.giantswarm.io/version: 2.3.0
    giantswarm.io/cluster: nzr5z
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
  name: nzr5z
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSCluster
    name: nzr5z:
    namespace: default
```

## Limitations

* __Downsizing__: be aware that reducing the volume size will cause data loss.



