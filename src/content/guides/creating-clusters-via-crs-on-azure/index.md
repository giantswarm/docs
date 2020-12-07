---
title: Creating tenant clusters on Azure via Control Plane Kubernetes API
description: This guide will walk you through the process of tenant cluster creation via Control Plane Kubernetes on Azure.
type: page
weight: 100
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
---

## How does cluster creation work

Starting from version {{% first_azure_nodepools_version %}} on Azure, Giant Swarm introduced a feature to create multiple [node pools](/basics/nodepools/) on Azure.
Alongside node pools support, a new API version for cluster management was released.

All the tenant clusters, created with tenant cluster release v{{% first_azure_nodepools_version %}} and newer, are managed as [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) in the Control Plane.

At a high-level, the Control Plane API is used to manage the following CRs:

- [Cluster](/reference/cp-k8s-api/clusters.cluster.x-k8s.io/) - represents a Kubernetes cluster excluding worker nodes.
- [MachinePool](/reference/cp-k8s-api/machinepools.exp.cluster.x-k8s.io/) - represents a node pool.

The CRs above then reference provider specific implementations. In our case, for clusters on Azure, they are:

- [AzureCluster](/reference/cp-k8s-api/azureclusters.infrastructure.cluster.x-k8s.io/) - represents a tenant cluster.
- [AzureMachinePool](/reference/cp-k8s-api/azuremachinepools.exp.infrastructure.cluster.x-k8s.io/) - configures the Azure-specific details of worker nodes in a node pool.

## Example CRs

### `Cluster`

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  name: nzr5z
  namespace: default
  labels:
    giantswarm.io/cluster: nzr5z
    cluster.x-k8s.io/cluster-name: nzr5z
    azure-operator.giantswarm.io/version: 5.0.0
    release.giantswarm.io/version: 13.0.0
    cluster-operator.giantswarm.io/version: 0.23.10
    giantswarm.io/organization: acme
spec:
  infrastructureRef:
    kind: AzureCluster
    namespace: default
    name: nzr5z
  controlPlaneEndpoint:
    host: api.nzr5z.k8s.ghost.westeurope.azure.gigantic.io
    port: 443
```

### `AzureCluster`

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureCluster
metadata:
  name: nzr5z
  namespace: default
  labels:
    giantswarm.io/cluster: nzr5z
    cluster.x-k8s.io/cluster-name: nzr5z
    azure-operator.giantswarm.io/version: 5.0.0
    release.giantswarm.io/version: 13.0.0
    giantswarm.io/organization: giantswarm
spec:
  networkSpec:
    vnet:
      resourceGroup: nzr5z
      id: nzr5z-VirtualNetwork
      name: nzr5z-VirtualNetwork
      cidrBlock: "10.1.0.0/16"
      tags: { }
    subnets: [ ]
  location: westeurope
  resourceGroup: nzr5z
  controlPlaneEndpoint:
    host: api.nzr5z.k8s.ghost.westeurope.azure.gigantic.io
    port: 443
```

### `MachinePool`

```yaml
apiVersion: exp.cluster.x-k8s.io/v1alpha3
kind: MachinePool
metadata:
  name: nopo1
  namespace: default
  labels:
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-pool: nopo1
    cluster.x-k8s.io/cluster-name: nzr5z
    azure-operator.giantswarm.io/version: 5.0.0
    release.giantswarm.io/version: 13.0.0
    giantswarm.io/organization: giantswarm
spec:
  clusterName: nzr5z
  replicas: 2
  failureDomains:
    - "1"
    - "3"
  template:
    spec:
      bootstrap: {}
      clusterName: nzr5z
      infrastructureRef:
        apiVersion: exp.infrastructure.cluster.x-k8s.io/v1alpha3
        kind: AzureMachinePool
        name: nopo1
```

### `AzureMachinePool`

```yaml
apiVersion: exp.infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureMachinePool
metadata:
  name: nopo1
  namespace: default
  labels:
    giantswarm.io/cluster: nzr5z
    giantswarm.io/machine-pool: nopo1
    cluster.x-k8s.io/cluster-name: nzr5z
    azure-operator.giantswarm.io/version: 5.0.0
    release.giantswarm.io/version: 13.0.0
    giantswarm.io/organization: giantswarm
spec:
  location: westeurope
  template:
    dataDisks:
      - DiskSizeGB: 50
        NameSuffix: docker
        Lun: 21
      - DiskSizeGB: 100
        NameSuffix: kubelet
        Lun: 22
    osDisk:
      diskSizeGB: 30
      managedDisk:
        storageAccountType: Premium_LRS
      osType: Linux
    sshPublicKey: "c3NoLXJzYSBBQUFBQjNOemFDMXljMkVBQUFBREFRQUJBQUFDQVFEa1RURmpnLzI4QWtnQWxiQmd1MmpXMXpsbW1ocDN0TFdmKzZ5cDNaTi9Na04rRXpoRkRGMHc3Z2pWWnhGZjlRRTBTc25KRjVvRDVzTjZnMHR1ZmF2ODllUjBUN0QwVVFjeWZNYmRST2VjRFFITkFpdEFDM1dtMmJnWkhDMzhFUXg1OVFicitlaWZpbmpDRzUvamQrNFpRY3pMMXUzakdBZWlBeURWZDBveGJ3TTFjSHhjZFdyOVdyKzZyazlrYks5WFJZSlJjMkJMVHV0VWtFdTM0bnp1a21wVFNEa2cwdDFjTFhWWWNUSzE1dzF6UEtMcENVcWVEMkhUQ0k4QkZYU1c5elVObjh0Qjc5KzhXNTB2UDYwVGRvMnpGOFpHV0JnWnlVc3VKWUxzVHdrNWVIZWdXVUVLVC9zLzd2ZG1JekZ5MXZrdTNublRPNW16NktLUjg2dDcyTnNYd3RGTy9WLzBUZHVNNTlKVjVmOWV5amJpWXJGV3hQR3puaFQvZDAvS05Mck5HNkYxOWJ1M2RjTEY0anZMQk9NeXZHdDhVdThsTG1iL3E3dUczc1NhR3NMRzdnS2loUUY1VFZhVTFldk9xMzJlKzNwektHUU96ZFRJNzFSUTMrY0pRZVRhTllKWXdvUVAvK0tpSHR3NkpCOTNmdExtQVlrUVd3NFp1SE1qclFSdnRMZUhUSEI0VzI4VVFMbnhJRFhHR1UvNytLYzJPbFk0UUR4OU5FVGVLYWpHNXovZzFxbFpGeEVDWUhyMTZSWEdtM0xLaFNxdkkyaDRWQmVGN3BsNEQ2V0UwK2NjdkR1K0hJVDRuK0N5eVJOaTVVaEZ4ZkZ5QVVWNS94d29lRmUyNGpWUlNpY2ZHd0JLUU1NSldTeTViM0RxcDFqTlJQNlp1R0RIRnc9PQ=="
    vmSize: Standard_D2s_v3
```

### Spark

```yaml
apiVersion: core.giantswarm.io/v1alpha1
kind: Spark
metadata:
  name: nopo1
  namespace: default
  labels:
    giantswarm.io/cluster: nzr5z
    cluster.x-k8s.io/cluster-name: nzr5z
    azure-operator.giantswarm.io/version: 5.0.0
    release.giantswarm.io/version: 13.0.0
    giantswarm.io/organization: giantswarm
spec: {}
```

## How to create a cluster using Cluster API

All the CRs, mentioned above, have strict spec and important requirements to be considered valid.
There is very limited CR validation available in the Control Plane for now.
Therefore, if you create a CR with wrong field values, that can result in a broken tenant cluster.
That's why we offer a [kubectl plugin](/reference/kubectl-gs/), which helps to template valid CRs.

The utility supports rendering CRs:

- Tenant clusters:
    - `Cluster` (API version `cluster.x-k8s.io/v1alpha3`)
    - `AzureCluster` (API version `infrastructure.cluster.x-k8s.io/v1alpha3`)
    - `AzureMachine` (API version `infrastructure.cluster.x-k8s.io/v1alpha3`)
- Node pool:
    - `MachinePool` (API version `exp.cluster.x-k8s.io/v1alpha3`)
    - `AzureMachinePool` (API version `exp.infrastructure.cluster.x-k8s.io/v1alpha3`)
    - `Spark` (API version `core.giantswarm.io/v1alpha1`)
- `AppCatalog`
- `App`

The installation procedure is described in the [`kubectl gs` reference](/reference/kubectl-gs/#install).
There are also specific reference pages for [cluster templating](/reference/kubectl-gs/template-cluster/) and [node pool templating](/reference/kubectl-gs/template-nodepool/).

As a result of rendering the CRs ([sample](/reference/kubectl-gs/template-cluster/#example)), a user will get YAML manifests containing valid CRs that can create a tenant cluster and its node pools.
The resources can then be created by applying the manifest files to the Control Plane, e.g. `kubectl create -f <cluster manifest file>.yaml`.
Of course, that requires the user to be authorized towards Kubernetes Control Plane API.

## How to configure OIDC authentication at cluster creation using Cluster API

Starting from version {{% first_azure_nodepools_version %}} on Azure we have enabled the possibility to configure the OIDC per cluster at the cluster creation stage. This feature only includes configuration of the OIDC in the `Cluster` CR before it is applied on the Control Plane.

In order to configure your new cluster with OIDC, you will have to add annotations to the Cluster CR as following:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:  
    oidc.giantswarm.io/client-id: OIDC_CLIENT_ID
    oidc.giantswarm.io/group-claim: GROUP_CLAIM
    oidc.giantswarm.io/issuer-url: https://login.microsoftonline.com/TENANT_ID/v2.0
    oidc.giantswarm.io/username-claim: USERNAME_CLAIM
```

This will result in setting up the OIDC config per cluster in the K8S API manifest.
Currently changing/adding config to already existing cluster is not fully supported at Giant Swarm. Please talk to your SE if there is any need to change those settings.

## How to delete cluster via Control Plane API

In order to delete your cluster created via the Cluster API on the Control Plane, simply delete the `Cluster` CR corresponding to the given cluster. This will result in starting the process of cluster deletion and clean up of all related CRs on the Control Plane.
