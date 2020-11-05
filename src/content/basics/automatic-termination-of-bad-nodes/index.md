---
title: Automatic termination of unhealthy nodes
description: A general description of a feature that can detect and terminate unhealthy nodes in the tenant cluster.
date: 2020-11-05
weight: 120
type: page
categories: ["basics"]
---

# Automatic termination of unhealthy nodes

## Overview

Giant Swarm's `terminate-unhealthy-nodes` feature helps you keep the nodes in your cluster in a healthy, running state. When enabled, a service makes periodic checks on the health of each node in your cluster. If a node fails consecutive health checks over an extended time period, it will be drained and terminated.

This is an `alpha` feature available on these providers:

* AWS - `12.6.0` release onwards

## Technical details

The node's health status is used to determine if a node needs to be terminated. A node reporting a `Ready` status is considered healthy. If a node reports an unhealthy status continuously for a given time threshold it will be recycled. 

An unhealthy status means the `kubelet` on a given node has reported `NotReady` status on consecutive checks over a certain time threshold (approximately 15 minutes).

## Enabling terminate-unhealthy-nodes feature

You can enable this feature on a cluster basis. To enable this feature you need to set the annotation `alpha.node.giantswarm.io/terminate-unhealthy` on the `AWSCluster` custom resource. The value can be anything as the only presence of that annotation is checked.

If you want to disable the feature you must remove the annotation from the `AWSCluster` custom resource.

The feature is disabled by default.

### Example

```yaml

apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    alpha.node.giantswarm.io/terminate-unhealthy: ""
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.7.0
  name: jni9x
  namespace: default
spec:
 ....


```
