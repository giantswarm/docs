---
title: Creating tenant clusters on AWS via Control Plane Kubernetes API
description: This guide will walk you through the process of tenant cluster creation via Control Plane Kubernetes on AWS.
type: page
weight: 100
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Creating tenant clusters on AWS via the Control Plane Kubernetes API

## How cluster creation works

Starting from version {{% first_aws_nodepools_version %}} on AWS, Giant Swarm introduced a feature to create multiple [node pools](/basics/nodepools/) on AWS.
Alongside node pools support, a new API version for cluster management was released.

All the tenant clusters, created with tenant cluster release v{{% first_aws_nodepools_version %}} and newer, are managed as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in the Control Plane.

At a high-level, the Control Plane Kubernetes API is used to manage the following custom resources (CRs):

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

## Creating a cluster {#creating}

All the CRs, mentioned above, have strict spec and important requirements to be considered valid.
There is very limited CR validation available in the Control Plane for now.
Therefore, if you create a CR with wrong field values, that can result in a broken tenant cluster.
That's why we offer a [kubectl plugin](/reference/kubectl-gs/), which helps to template valid CRs.

The utility supports rendering CRs:

- Tenant cluster:
    - `Cluster` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSCluster` (API version `infrastructure.giantswarm.io/v1alpha2`)
    - `G8sControlPlane` (API version `infrastructure.giantswarm.io/v1alpha2`)
    - `AWSControlPlane` (API version `infrastructure.giantswarm.io/v1alpha2`)
- Node pool:
    - `MachineDeployment` (API version `cluster.x-k8s.io/v1alpha2`)
    - `AWSMachineDeployment` (API version `infrastructure.giantswarm.io/v1alpha2`)
- `AppCatalog`
- `App`

The installation procedure is described in the [`kubectl gs` reference](/reference/kubectl-gs/#install).
There are also specific reference pages for [cluster templating](/reference/kubectl-gs/template-cluster/) and [node pool templating](/reference/kubectl-gs/template-nodepool/).

As a result of rendering the CRs ([sample](/reference/kubectl-gs/template-cluster/#example)), a user will get YAML manifests containing valid CRs that can create a tenant cluster and its node pools.
The resources can then be created by applying the manifest files to the Control Plane, e.g. `kubectl create -f <cluster manifest file>.yaml`.
Of course, that requires the user to be authorized towards Kubernetes Control Plane API.

## Configuring OIDC authentication

Starting from version {{% first_aws_nodepools_version %}} on AWS, Giant Swarm has enabled the possibility to configure the OIDC parameters per cluster at creation stage. This feature includes an OIDC section in the `AWSCluster` CR with the necessary fields.

In order to configure a cluster with OIDC, you will have to add these fields to the AWSCluster CR as following:

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
spec:
  cluster:
    ...
    oidc:
      claims:
        groups: GROUP_CLAIM
        username: USERNAME_CLAIM
      clientID: OIDC_CLIENT_ID
      issuerURL: PROVIDER_URL_TO_DISCOVER_PUBLIC_KEYS
   ...
```

This will result in setting up the OIDC flags API manifest for the given cluster.

__Note__: Currently changing/adding config to already existing cluster is not fully supported at Giant Swarm (control plane nodes need to be recreated). Please talk to your SE if there is any need to change those settings.

## Deleting a cluster {#deleting}

Triggering a delete on the `Cluster` resource  will have a cascading effect on all other resources belonging to the cluster:

- `AWSCluster`
- `G8sControlPlane`
- `AWSControlPlane`
- `MachineDeployment`
- `AWSMachineDeployment`

This resources will not be deleted immediately, our operators will start the deletion process of the CloudFormation Stacks on AWS and remove the Kubernetes finalizer.

In order to review if a resource has been marked for deletion you can check if the resource has the attribute `deletionTimestamp` in the `metadata` field.

The whole deletion process can take up to one hour.
