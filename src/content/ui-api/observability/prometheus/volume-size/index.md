---
linkTitle: Prometheus Volume Size
title: Prometheus VolumeSize
description: A guide explaining how to size the Prometheus persistent volume
menu:
  main:
    identifier: uiapi-observability-prometheusvolumesize
    parent: uiapi-observability-prometheus
user_questions:
  - How can I downsize the persistent volume?
  - How do I expand the Prometheus volume?
  - Why would I like to resize the Prometheus persistent volume ?
aliases:
  - /observability/prometheus/volume-size
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

In this document you will learn how to size the Prometheus persistent volume.

__Warning:__ 
* The volume expansion on OpenStack clusters is currently not working properly
* Downsizing the persistent volume will cause a data loss
* This feature and the documentation is quite new, so do not hesitate to ask for support or help us improve this documentation.

## Introduction to persistent volume
Each Prometheus instance needs a persistent volume to store the recorded metrics.
Persistent storage is crucial to be able to retrieve metrics data even when Prometheus instance is dead.
Before implementing the volume resizing feature, the volume attached of each Prometheus instance had a capacity of 100Gi.

## Why would I like to resize the volume
Our observability architecture is based on one Prometheus instance by workload cluster.
As mentioned above, Prometheus volume is set to 100Gi.
This capacity is the same for a small or a large cluster.

Imagine that you want to create multiple testing clusters for a training.
You don't need to have 100Gi reserved for each cluster.
It will be interesting to set a smaller size for each Prometheus volume.

In an other hand, if you have large clusters with lots of traffic, and so lots of metrics to store, you might like to set a larger size for each Prometheus volume.

## How can I resize Prometheus volume
The Prometheus volume size can be set in the cluster CR by a dedicated annotation `monitoring.giantswarm.io/prometheus-volume-size`

Three values are possible:
* `small`
* `medium`
* `large`

`small` represents 30Gi, `medium` represents 100Gi and `large` represents 200Gi.

`medium` is the default value, it means if the annotation doesn't exist, so the volume size will be 100Gi.

Below is an example of a cluster CR that defines a small Prometheus volume:
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

* __Expanding__: we are encountering an issue with OpenStack clusters and the expanding feature. 
When you expand the volume from a smaller size to a larger size, you will see the correct value size on the provider side, also on the Persistant Volume Claim and Persistent Volume Kubernetes resources but the volume will not be resized on filesystem.

* __Downsizing__: be aware that reducing the volume size will cause a data loss.



