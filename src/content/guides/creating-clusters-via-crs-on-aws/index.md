---
title: Creating tenant clusters on AWS via Control Plane Kubernetes API
description: This guide will walk you through the process of tenant cluster creation via Control Plane Kubernetes on AWS.
date: 2020-09-23
type: page
weight: 100
tags: ["tutorial"]
---

## How does cluster creation work

Starting from version {{% first_aws_nodepools_version %}} on AWS, Giant Swarm introduced a feature to create multiple [node pools](https://docs.giantswarm.io/basics/nodepools/) on AWS.
Alongside node pools support, a new API version for cluster management was released.

All the tenant clusters, created with release version {{% first_aws_nodepools_version %}} and newer, are managed as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in the Control Plane.

At a high-level, the Control Plane Kubernetes API is used to manage the following CRs:

- [Cluster](/reference/cp-k8s-api/clusters.cluster.x-k8s.io/) - represents a Kubernetes cluster excluding worker nodes.
- [G8sControlPlane](/reference/cp-k8s-api/g8scontrolplanes.infrastructure.giantswarm.io/) - hold configuration about the master node(s) of a cluster.
- [MachineDeployment](/reference/cp-k8s-api/machinedeployments.cluster.x-k8s.io/) - represents a node pool.

The CRs above then reference provider specific implementations. In our case, for clusters on AWS, they are:

- [AWSCluster](/reference/cp-k8s-api/awsclusters.infrastructure.giantswarm.io/) - represents a tenant cluster.
- [AWSControlPlane](/reference/cp-k8s-api/awscontrolplanes.infrastructure.giantswarm.io/) - configures the AWS-specific details of the worker node(s).
- [AWSMachineDeployment](/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/) - configures the AWS-specific details of worker nodes in a node pool.

## Example CRs

### `Cluster`

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  generation: 1
  labels:
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
    name: nzr5z
    namespace: default
```

### `AWSCluster`

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  generation: 1
  labels:
    aws-operator.giantswarm.io/version: 8.7.0
    giantswarm.io/cluster: nzr5z
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
  name: nzr5z
  namespace: default
spec:
  cluster:
    description: Demo cluster
    dns:
      domain: gorilla.eu-central-1.aws.gigantic.io
    oidc:
      claims: {}
  provider:
    credentialSecret:
      name: credential-default
      namespace: giantswarm
    pods:
      cidrBlock: 10.7.0.0/16
    region: eu-central-1
status:
  cluster:
    id: nzr5z
  provider:
    network:
      cidr: 10.6.0.0/24
```

### `G8sControlPlane`

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: G8sControlPlane
metadata:
  generation: 2
  labels:
    cluster-operator.giantswarm.io/version: 2.3.0
    giantswarm.io/cluster: nzr5z
    giantswarm.io/control-plane: 2m0kh
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
  name: 2m0kh
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSControlPlane
    name: 2m0kh
    namespace: default
    resourceVersion: "100323111"
    uid: 370a5c2d-d0d4-4ffd-825f-ec28f9d2957c
  replicas: 3
```

### `AWSControlPlane`

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSControlPlane
metadata:
  generation: 1
  labels:
    aws-operator.giantswarm.io/version: 8.7.0
    giantswarm.io/cluster: nzr5z
    giantswarm.io/control-plane: 2m0kh
    giantswarm.io/organization: giantswarm-production
    release.giantswarm.io/version: 11.4.0
  name: 2m0kh
  namespace: default
spec:
  availabilityZones:
  - eu-central-1a
  - eu-central-1b
  - eu-central-1c
  instanceType: m5.xlarge
```

### `MachineDeployment`

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: MachineDeployment
metadata:
  labels:
    cluster-operator.giantswarm.io/version: 2.1.1
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-deployment: pv7ps
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.4.0
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

### `AWSMachineDeployment`

```yaml
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

## How to create a cluster using Cluster API

All the CRs, mentioned above, have strict spec and important requirements to be considered valid.
There is very limited CR validation available in the Control Plane for now.
Therefore, if you create a CR with wrong field values, that can result in a broken tenant cluster.
That's why we've developed a simple [CLI utility](https://github.com/giantswarm/kubectl-gs), which helps to template valid CRs.

The utility supports rendering CRs:

- Tenant clusters (AWS only):
    - `Cluster` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSCluster` (API version `infrastructure.giantswarm.io/v1alpha2`)
    - `G8sControlPlane` (API version `infrastructure.giantswarm.io/v1alpha2`)
    - `AWSControlPlane` (API version `infrastructure.giantswarm.io/v1alpha2`)
- Node pool (AWS only):
    - `MachineDeployment` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSMachineDeployment` (API version `infrastructure.giantswarm.io/v1alpha2`)
- `AppCatalog`
- `App`

The installation procedure is described in [README](https://github.com/giantswarm/kubectl-gs#how-to-install-plugin).
There is also a [document](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md) describing the templating process in detail.

As a result of rendering the CRs ([sample](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md#example)), a user will get YAML manifests containing valid CRs that can create a tenant cluster and its node pools.
The resources can then be created by applying the manifest files to the Control Plane, e.g. `kubectl create -f <cluster manifest file>.yaml`.
Of course, that requires the user to be authorized towards Kubernetes Control Plane API.
