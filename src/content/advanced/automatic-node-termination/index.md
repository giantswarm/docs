---
linkTitle: Automatic termination of unhealthy nodes
title: Automatic termination of unhealthy nodes
description: Unhealthy cluster nodes can lead to impaired workload reliability and wasted cluster resources. Here we explain how you can activate automatic termination of such nodes.
weight: 60
menu:
  main:
    parent: advanced
last_review_date: 2021-06-21
user_questions:
  - How can I turn off automatic termination of unhealthy nodes?
  - Since what release are unhealthy nodes terminated automatically?
  - How are unhealthy worker nodes treated?
aliases:
  - /basics/automatic-termination-of-bad-nodes/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

{{< platform_support_table aws="alpha=v12.6.0,ga=v15.0.0" azure="alpha=v13.1.0" kvm="alpha=v14.0.0" >}}

## Introduction

Degraded nodes in a Kubernetes cluster should be a rare issue, however when it occurs, it can have severe consequences for the workloads scheduled to the affected nodes. The goal should be to detect bad nodes early and remove them from the cluster, replacing them with healthy ones.

Starting with workload cluster release v12.6.0 for AWS, v13.1.0 for Azure and v14.0.0 for KVM, you have the option to automate the detection and termination of bad nodes. When enabled, all nodes in your cluster are periodically checked. If a node fails consecutive health checks over an extended time period, it will be drained and terminated.

From AWS workload cluster release v15.0.0 the feature is enabled by default. In order to enable this functionality for other providers, please refer to the applicable section below.

## Technical details

The node's health status is used to determine if a node needs to be terminated. A node reporting a `Ready` status is considered healthy. If a node reports an unhealthy status continuously for a given time threshold it will be recycled.

An unhealthy status means the `kubelet` on a given node has reported `NotReady` status on consecutive checks (aproximately every 2-3 minutes)  over a certain time threshold (approximately 15 minutes).

## Enabling automatic termination

Automatic termination of unhealthy nodes is **enabled by default** on AWS as of release `v15.0.0`. It continues to be **disabled by default** for older releases.

This section explains how you can enable the feature for each supported provider.

### AWS

#### workload cluster releases v12.6.x to v14.x.x

To enable the feature, edit the [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api/" >}}).

Make sure the resource has the `alpha.node.giantswarm.io/terminate-unhealthy` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    alpha.node.giantswarm.io/terminate-unhealthy: "true"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.6.0
  name: jni9x
  namespace: default
spec:
  ...
```

If you want to disable the feature you must remove the annotation from the [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) custom resource.

### workload cluster releases v15.x.x and newer

To disable automatic termination of unhealthy nodes, edit the [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api/" >}}).

Make sure the resource has the annotation

```yaml
node.giantswarm.io/terminate-unhealthy: "false"

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  annotations:
    node.giantswarm.io/terminate-unhealthy: "false"
  labels:
    giantswarm.io/cluster: jni9x
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 12.6.0
  name: jni9x
  namespace: default
spec:
  ...
```

### Azure

To enable automatic termination of unhealthy nodes, edit the [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api" >}}).

Make sure the resource has the `alpha.node.giantswarm.io/terminate-unhealthy` annotation. The value can be anything you like, as just the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:
    alpha.node.giantswarm.io/terminate-unhealthy: "true"
  name: fn7t8
  namespace: org-giantswarm
spec:
  ...
```

If you want to disable the feature you must remove the annotation from the [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) custom resource.

### KVM

To enable it, you have to edit the [`KVMConfig`]({{< relref "/ui-api/management-api/crd/kvmconfigs.provider.giantswarm.io.md" >}}) resource of your cluster using the [Management API]({{< relref "/ui-api/management-api/" >}}).

Make sure the resource has the `alpha.node.giantswarm.io/terminate-unhealthy` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: provider.giantswarm.io/v1alpha1
kind: KVMConfig
metadata:
  annotations:
    alpha.node.giantswarm.io/terminate-unhealthy: "true"
  name: fn7t8
  namespace: default
spec:
  ...
```

If you want to disable the feature you must remove the annotation from the [`KVMConfig`]({{< relref "/ui-api/management-api/crd/kvmconfigs.provider.giantswarm.io.md" >}}) custom resource.
