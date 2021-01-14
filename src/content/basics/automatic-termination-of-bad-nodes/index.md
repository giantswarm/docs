---
title: Automatic termination of unhealthy nodes
description: Unhealthy cluster nodes can lead to impaired workload reliability and wasted cluster resources. Here we explain how you can activate automatic termination of such nodes.
weight: 120
type: page
categories: ["basics"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Automatic termination of unhealthy nodes

{{< platform_support_table aws="ga=v12.6.0" azure="ga=v13.1.0" kvm="roadmap=https://github.com/giantswarm/roadmap/issues/176" >}}

## Introduction

Degraded nodes in a Kubernetes cluster should be a rare issue, however when it occurs, it can have severe consequences for the workloads scheduled to the affected nodes. The goal should be to detect bad nodes early and remove them from the cluster, replacing them with healthy ones.

Starting with workload cluster release v12.6.0 for AWS and v13.1.0 for Azure, you now have the option to automate the detection and termination of bad nodes. When enabled, all nodes in your cluster are periodically checked. If a node fails consecutive health checks over an extended time period, it will be drained and terminated.

## Technical details

The node's health status is used to determine if a node needs to be terminated. A node reporting a `Ready` status is considered healthy. If a node reports an unhealthy status continuously for a given time threshold it will be recycled.

An unhealthy status means the `kubelet` on a given node has reported `NotReady` status on consecutive checks over a certain time threshold (approximately 15 minutes).

## Enabling automatic termination

Automatic termination of unhealthy nodes is **disabled by default**. You can enable it for each individual cluster.

This section explains how you can enable the feature for each supported provider.

### AWS

To enable it, you have to edit the [`AWSCluster`](/reference/management-api/awsclusters.infrastructure.giantswarm.io/) resource of your cluster using the [Management API](/basics/api/#management-api).

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

If you want to disable the feature you must remove the annotation from the [`AWSCluster`](/reference/management-api/awsclusters.infrastructure.giantswarm.io/) custom resource.

### Azure

To enable it, you have to edit the [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) resource of your cluster using the [Management API](/basics/api/#management-api).

Make sure the resource has the `alpha.node.giantswarm.io/terminate-unhealthy` annotation. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

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

If you want to disable the feature you must remove the annotation from the [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) custom resource.

### KVM

To enable it, you have to edit the [`KVMConfig`](/reference/cp-k8s-api/kvmconfigs.provider.giantswarm.io/) resource of your cluster using the [Control Plane Kubernetes API](/basics/api/#cp-k8s-api).

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

If you want to disable the feature you must remove the annotation from the [`KVMConfig`](/reference/management-api/kvmconfigs.provider.giantswarm.io/) custom resource.

