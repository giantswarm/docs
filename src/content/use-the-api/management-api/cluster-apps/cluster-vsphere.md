---
title: Cluster-Vsphere chart reference
linkTitle: cluster-vsphere chart reference
description: |
  A helm chart for creating Cluster API clusters with the vSphere provider (CAPV).
weight: 100
menu:
  main:
    identifier: cluster-vsphere
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-vsphere
source_repository_ref: v0.9.8
---

The `default-apps-vsphere` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API vSphere cluster.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).



### Cluster
Properties within the `.cluster` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `cluster.kubernetesVersion` | **Kubernetes version**|**Type:** `string`|

### Connectivity
Properties within the `.connectivity` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `connectivity.network` | **Network**|**Type:** `object`|
| `connectivity.network.allowAllEgress` | **Allow all egress**|**Type:** `boolean`**Default:** `false`|
| `connectivity.network.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`**Default:** `{}`|
| `connectivity.network.containerRegistries.*` |**None**|**Type:** `array`|
| `connectivity.network.containerRegistries.*[*]` |**None**|**Type:** `object`|
| `connectivity.network.containerRegistries.*[*].credentials` | **Credentials** - Credentials for the endpoint.|**Type:** `object`|
| `connectivity.network.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`|
| `connectivity.network.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`|
| `connectivity.network.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.network.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.network.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`|
| `connectivity.network.controlPlaneEndpoint` | **Endpoint** - Kubernetes API configuration.|**Type:** `object`|
| `connectivity.network.controlPlaneEndpoint.host` | **Host** - IP for access to the Kubernetes API.|**Type:** `string`|
| `connectivity.network.controlPlaneEndpoint.ipPoolName` | **Ip Pool Name** - Ip for control plane will be drawn from this GlobalInClusterIPPool resource.|**Type:** `string`**Default:** `&#34;wc-cp-ips&#34;`|
| `connectivity.network.controlPlaneEndpoint.port` | **Port number** - Port for access to the Kubernetes API.|**Type:** `integer`|
| `connectivity.network.loadBalancers` | **Load balancers**|**Type:** `object`|
| `connectivity.network.pods` | **Pods**|**Type:** `object`|
| `connectivity.network.pods.cidrBlocks` |**None**|**Type:** `array`|
| `connectivity.network.pods.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`|
| `connectivity.network.services` | **Services**|**Type:** `object`|
| `connectivity.network.services.cidrBlocks` |**None**|**Type:** `array`|
| `connectivity.network.services.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`|

### Control plane
Properties within the `.controlPlane` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controlPlane.etcd` | **Etcd**|**Type:** `object`|
| `controlPlane.etcd.imageRepository` | **Image repository**|**Type:** `string`|
| `controlPlane.etcd.imageTag` | **Image tag**|**Type:** `string`|
| `controlPlane.replicas` | **Number of nodes**|**Type:** `integer`|

### Kubeadm
Properties within the `.kubeadm` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubeadm.users` | **Users**|**Type:** `array`|
| `kubeadm.users[*]` |**None**|**Type:** `object`|
| `kubeadm.users[*].authorizedKeys` | **Authorized keys**|**Type:** `array`|
| `kubeadm.users[*].authorizedKeys[*]` | **Key**|**Type:** `string`|
| `kubeadm.users[*].name` | **Name**|**Type:** `string`|

### Kubectl image
Properties within the `.kubectlImage` top-level object
Used by cluster-shared library chart to configure coredns in-cluster.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` |**None**|**Type:** `string`|
| `kubectlImage.registry` |**None**|**Type:** `string`|
| `kubectlImage.tag` |**None**|**Type:** `string`|

### Kubernetes API server
Properties within the `.apiServer` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apiServer.certSANs` | **Subject alternative names (SAN)** - Alternative names to encode in the API server&#39;s certificate.|**Type:** `array`**Default:** `[]`|
| `apiServer.certSANs[*]` | **SAN**|**Type:** `string`|
| `apiServer.enableAdmissionPlugins` | **Admission plugins** - Comma-separated list of admission plugins to enable.|**Type:** `string`**Default:** `&#34;NamespaceLifecycle,LimitRanger,ServiceAccount,ResourceQuota,PersistentVolumeClaimResize,DefaultStorageClass,Priority,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook&#34;`|
| `apiServer.featureGates` | **Feature gates** - Enabled feature gates, as a comma-separated list.|**Type:** `string`**Default:** `&#34;&#34;`|

### Kubernetes Controller Manager
Properties within the `.controllerManager` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controllerManager.featureGates` | **Feature gates** - Enabled feature gates, as a comma-separated list.|**Type:** `string`**Default:** `&#34;&#34;`|

### Node template
Properties within the `.template` top-level object
Provisioning options for node templates.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `template.cloneMode` | **Clone mode** - Method used to clone template image.|**Type:** `string`|
| `template.diskGiB` | **Disk size (GB)** - Node disk size in GB. Must be at least as large as the source image.|**Type:** `integer`|
| `template.folder` | **Folder** - VSphere folder to deploy instances in. Must already exist.|**Type:** `string`|
| `template.memoryMiB` | **Memory (MB)** - Node memory allocation in MB.|**Type:** `integer`|
| `template.networkName` | **Segment name** - Segment name to attach nodes to. Must already exist.|**Type:** `string`|
| `template.numCPUs` | **CPU cores** - Number of CPUs to assign per node.|**Type:** `integer`|
| `template.resourcePool` | **Resource pool** - Resource pool to allocate nodes from. Must already exist.|**Type:** `string`|
| `template.storagePolicyName` | **Storage policy** - Storage policy to use. If specified, it must already exist.|**Type:** `string`|
| `template.templateName` | **Name** - Image template name to use for nodes.|**Type:** `string`|

### VCenter
Properties within the `.vcenter` top-level object
Configuration for vSphere API access.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `vcenter.datacenter` | **Datacenter** - Name of the datacenter to deploy nodes into.|**Type:** `string`|
| `vcenter.datastore` | **Datastore** - Name of the datastore for node disk storage.|**Type:** `string`|
| `vcenter.password` | **Password** - Password for the VSphere API.|**Type:** `string`|
| `vcenter.region` | **Region** - Category name in VSphere for topology.kubernetes.io/region labels.|**Type:** `string`|
| `vcenter.server` | **Server** - URL of the VSphere API.|**Type:** `string`|
| `vcenter.thumbprint` | **Thumbprint** - TLS certificate signature of the VSphere API.|**Type:** `string`|
| `vcenter.username` | **Username** - Username for the VSphere API.|**Type:** `string`|
| `vcenter.zone` | **Zone** - Category name in VSphere for topology.kubernetes.io/zone labels.|**Type:** `string`|

### Worker
Properties within the `.worker` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `worker.replicas` | **Number of nodes**|**Type:** `integer`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `organization` | **Organization**|**Type:** `string`|





## Further reading

- [Source repository](https://github.com/giantswarm/cluster-vsphere)
