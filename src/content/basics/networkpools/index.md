---
title: Network Pools
description: A general description of network pools as a concept, it's benefits, and some details you should be aware of.
date: 2021-01-28
weight: 130
type: page
categories: ["basics"]
user_questions:
  - What is a network pool?
  - What are network pools?
  - In which cloud environments are network pools supported?
  - Which releases introduced network pools?
---

# Network Pools

{{< platform_support_table aws="ga=v12.7.0" >}}

## Definition

A NetworkPool defines a CIDR range for the Control Plane and MachineDeployment nodes of a Cluster.

NetworkPools have been introduced in release 12.7.0 on AWS and are not yet available in KVM or Azure.

## Advantages

The main advantages of using NetworkPools are:

- Extending installation default CIDR range.
- Limit the CIDR range a single cluster can have.

## Lifecycle

NetworkPools must be created before the cluster is created via Management Cluster Kubernetes API.

NetworkPools can be modified as long as the CIDR doesn't overlap with other NetworkPools and contains the original CIDR. For example 10.0.0.0/16 could be modified to 10.0.0.0/15 but not to 10.0.0.0/17.

## Assigning clusters to NetworkPools

When creating a Cluster, you can assing the NetworkPool in the `.spec.provider.nodes.networkPool` attribute like:

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: NetworkPool
metadata:
  labels:
    giantswarm.io/organization: giantswarm
  name: custom
  namespace: development-networkpool
spec:
  cidrBlock: 192.168.0.0/16
```

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  name: g8kw3
spec:
  provider:
    master:
      availabilityZone: eu-central-1b
      instanceType: m5.2xlarge
    nodes:
      networkPool: development-networkpool
    pods:
      cidrBlock: 192.168.1.0/16
    ...
```

## NetworkPool deletion

Before deleting a NetworkPool you must ensure there are no clusters using it.

## NetworkPool YAML format

You can check out the YAML definition in the [Management API](/reference/management-api/networkpools.infrastructure.giantswarm.io/).

## Limitations

- NetworkPools must be at least /20 in order to be able to create clusters.
- NetworkPools must be created in the same namespace as the cluster.
- NetworkPools can not overlap with each other.
- NetworkPools can not overlap with the installation default CIDR.
- The Pod CIDR must be in the same Private IP Block as the NetworkPool.
