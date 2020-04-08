+++
title = "Creating tenant clusters on AWS via Control Plane Kubernetes API"
description = "This guide will walk you through the process of tenant cluster creation via Control Plane Kubernetes."
date = "2020-04-01"
type = "page"
weight = 100
tags = ["tutorial"]
+++
# Creating tenant clusters via the Control Plane Kubernetes API

Starting from version 10.0.0, Giant Swarm introduced a feature to create multiple [node pools](https://docs.giantswarm.io/basics/nodepools/) on AWS.
Alongside node pools support, a new API version for cluster management was released. 
Therefore, [v5](https://docs.giantswarm.io/api/#operation/addClusterV5) API is used now within happa and [gsctl](https://docs.giantswarm.io/reference/gsctl/create-cluster/).

As for now, Giant Swarm is replacing its own REST API for cluster management with the [Control Plane](https://docs.giantswarm.io/basics/aws-architecture/#giant-swarm-control-plane) Kubernetes API based on the upstream [Cluster API](https://cluster-api.sigs.k8s.io/).
Following this strategy, the Giant Swarm API is going to be deprecated in the near feature. You can find the related roadmap issue [here](https://github.com/giantswarm/roadmap/issues/90).

## How does cluster creation work now?

All the tenant clusters, created with release version 10.x.x+, are managed as [Cluster API](https://github.com/kubernetes-sigs/cluster-api) [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in Control Plane Kubernetes.
The Cluster API is a Kubernetes project to bring declarative, Kubernetes-style APIs to cluster creation, configuration, and management. It provides optional, additive functionality on top of core Kubernetes.

That means, when you're creating a new cluster via [v5](https://docs.giantswarm.io/api/#operation/addClusterV5) API, *Giant Swarm API* service creates 
 *Cluster* and *AWSCluster* CRs in Control-Plane Kubernetes.

On high-level Cluster API is used to manage two types of CR kinds:
  - `Cluster` - represents generic Kubernetes control plane.
  - `MachineDeployment` -  represents generic node pool.

Mentioned CRs reference provider specific implementations, which in Giant Swarm case for AWS platform are:
  - `AWSCluster` - represents tenant cluster Kubernetes control plane.
  - `AWSMachineDeployment` -  represents tenant cluster node pool.


## Cluster CRs

*Cluster* CR object example :

```
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  labels:
    cluster-operator.giantswarm.io/version: 2.1.1
    giantswarm.io/cluster: nzr5z
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.0.1
  name: nzr5z
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSCluster
    name: nzr5z
    namespace: default
```

*AWSCluster* CR object example:

```
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
  labels:
    aws-operator.giantswarm.io/version: 8.1.1
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-deployment: pv7ps
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.0.1
  name: pv7ps
  namespace: default
spec:
  nodePool:
    description: np1
    machine:
      dockerVolumeSizeGB: 100
      kubeletVolumeSizeGB: 100
    scaling:
      max: 10
      min: 3
  provider:
    availabilityZones:
    - eu-central-1a
    worker:
      instanceType: m4.xlarge
```

## MachineDeployment CRs

*MachineDeployment* CR object example:

```
apiVersion: cluster.x-k8s.io/v1alpha2
kind: MachineDeployment
metadata:
  labels:
    cluster-operator.giantswarm.io/version: 2.1.1
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-deployment: pv7ps
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.0.1
  name: pv7ps
  namespace: default
spec:
  selector: {}
  template:
    metadata: {}
    spec:
      bootstrap: {}
      infrastructureRef:
        apiVersion: infrastructure.giantswarm.io/v1alpha2
        kind: AWSMachineDeployment
        name: pv7ps
        namespace: default
      metadata: {}
```

*AWSMachineDeployment* CR object example:

```
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
  labels:
    aws-operator.giantswarm.io/version: 8.1.1
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-deployment: pv7ps
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.0.1
  name: pv7ps
  namespace: default
spec:
  nodePool:
    description: np1
    machine:
      dockerVolumeSizeGB: 100
      kubeletVolumeSizeGB: 100
    scaling:
      max: 10
      min: 3
  provider:
    availabilityZones:
    - eu-central-1a
    worker:
      instanceType: m4.xlarge
```

## How to create the cluster omitting Giant Swarm API?

All the CRs, mentioned above, have the strict spec and important requirements to be considered valid. 
There is no cluster/node pool CRs validation available in Control Plane Kubernetes of Giant Swarm for now. 
Therefore, if you create CR with wrong field values, that can result in a broken tenant cluster, which then causes unwanted alerts in Giant Swarm monitoring system.
That's why we've developed a simple [kubectl gs plugin](https://github.com/giantswarm/kubectl-gs), which helps to template valid CRs.

Plugin supports rendering CRs:
  - Tenat control-plane (AWS only):
    - `Cluster` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSCluster` (API version `infrastructure.giantswarm.io/v1alpha2`)
  - Nodepool (AWS only):
    - `MachineDeployment` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSMachineDeployment` (API version `infrastructure.giantswarm.io/v1alpha2`)
  - `AppCatalog`
  - `App`

The installation procedure is described in [README](https://github.com/giantswarm/kubectl-gs#how-to-install-plugin).
There is also a [document](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md), describing the templating process in detail.

As a result of rendering the CRs ([sample](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md#example)), a user will get a *yaml* file with a valid Cluster/Node pools definition. 
The tenant cluster can be created by applying the cluster manifest file to the Giant Swarm Kubernetes Control Plane, .e.g. `kubectl create -f <cluster manifest file>.yaml`. 
Of course, that requires the user to be authorized towards Kubernetes Control Plane API. 
