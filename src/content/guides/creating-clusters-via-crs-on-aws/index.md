# Creating tenant clusters directly via Control Plane Kubernetes API

Starting from version 10.0.0, Giant Swarm introduced [node pools](https://docs.giantswarm.io/basics/nodepools/) feature for AWS platform.
Alongside node pools support, a new API version for cluster management was released. 
Therefore, [v5](https://docs.giantswarm.io/api/#operation/addClusterV5) API is used now within happa and [gsctl](https://docs.giantswarm.io/reference/gsctl/create-cluster/).

As for now, Giant Swarm is moving towards replacing its own API with the direct cluster management via [Control Plane Kubernetes API](https://docs.giantswarm.io/basics/aws-architecture/#giant-swarm-control-plane).
Following this movement strategy, Giant Swarm API is going to be deprecated in the near feature. You can find related roadmap issue [here](https://github.com/giantswarm/roadmap/issues/90).

## How does cluster creation works now?

All the tenant clusters, created with release version 10.x.x+, are managed as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in Control Plane Kubernetes.
That means, when you're creating a new cluster via [v5](https://docs.giantswarm.io/api/#operation/addClusterV5) API, what *API* service does, it uses [Cluster API](https://github.com/kubernetes-sigs/cluster-api) to create tenant Kubernetes control-plane CR and optional node pools CRs.
The Cluster API is a Kubernetes project to bring declarative, Kubernetes-style APIs to cluster creation, configuration, and management. It provides optional, additive functionality on top of core Kubernetes.

On high-level Cluster API is used two manage two types of CR kinds:
  -  Cluster
  - MachineDeployment

## Cluster CRs

*Cluster* CR represents tenant cluster Kubernetes control plane.

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

*Cluster* references *AWSCluster* CR, which represents actual Cluster API implementation of the cluster for AWS platform.

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

So, when the release 10.x.x+ in AWS installation is used, *Giant Swarm API* service creates *Cluster* and *AWSCluster* CRs in Control-Plane Kubernetes.


## MachineDeployment CRs

The same approach applies to node pools management, where high level *MachineDeployment* CR represents Cluster API generic node pool implementation. 

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

As with *Cluster* CR, *MachineDeployment* has the reference to infrastructure object. In this case, it is *AWSMachineDeployment*, which represents actual Cluster API implementation of node pool for AWS platform.

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
There is also [document](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md), describing the templating process in details.

As a result of running CRs rendering([sample](https://github.com/giantswarm/kubectl-gs/blob/master/docs/template-cluster-cr.md#example)), user gets *yaml* file with the valid Cluster/Node pool definitions. 
Now tenant cluster control-plane and node pool can be created just by applying those CRs to the Giant Swarm Kubernetes Control Plane, .e.g. `kubectl create -f <CRs definition file>.yaml`. 
Of course, that requires the user to be authorized towards Kubernetes Control Plane API. 
