---
title: Automatic termination of bad nodes
description: A general description of a feature that can detect and terminate unhealthy nodes in the tenant cluster.
date: 2020-11-05
weight: 120
type: page
categories: ["basics"]
---

# Automatic termination of unhealthy nodes

## Overview

Giant Swarm's `terminate-unhealthy-nodes` feature helps you keep the nodes in your cluster in a healthy, running state. When enabled, a service makes periodic checks on the health state of each node in your cluster. If a node fails consecutive health checks over an extended time period, it will be drained and terminated.

This is an `alpha` feature avaiable on theese providers:

* AWS - from `12.6.0` release

## Technical details

The node's health status is used to determine if a node needs to be terminated. A node reporting a Ready status is considered healthy. If a node reports consecutive unhealthy status reports for a given time threshold. An unhealthy status can mean:

*    A node reports a NotReady status on consecutive checks over the given time threshold (approximately 15 minutes).

## Enabling terminate-unhealthy-nodes feature

You can enable this feature on a cluster basis. To enable this feature you need to set annotation `alpha.node.giantswarm.io/terminate-unhealthy` on the `AWSCluster` CR. The value can be anything as only presence of that annotation is checked.

If you want to disable the feature, just remove the annotations from the `AWSCluster` CR.

The feature is disabled by default.

### example

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
