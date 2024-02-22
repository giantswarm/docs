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

&lt;!-- DOCS_START --&gt;

### Cluster
Properties within the `.cluster` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `cluster.kubernetesVersion` | **Kubernetes version**|**Type:** `string`&lt;br/&gt;|

### Connectivity
Properties within the `.connectivity` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `connectivity.network` | **Network**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.allowAllEgress` | **Allow all egress**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|
| `connectivity.network.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`&lt;br/&gt;**Default:** `{}`|
| `connectivity.network.containerRegistries.*` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].credentials` | **Credentials** - Credentials for the endpoint.|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint` | **Endpoint** - Kubernetes API configuration.|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint.host` | **Host** - IP for access to the Kubernetes API.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint.ipPoolName` | **Ip Pool Name** - Ip for control plane will be drawn from this GlobalInClusterIPPool resource.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`&lt;br/&gt;**Default:** `&#34;wc-cp-ips&#34;`|
| `connectivity.network.controlPlaneEndpoint.port` | **Port number** - Port for access to the Kubernetes API.|**Type:** `integer`&lt;br/&gt;|
| `connectivity.network.loadBalancers` | **Load balancers**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.pods` | **Pods**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.pods.cidrBlocks` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.pods.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;10.244.0.0/16&#34;`&lt;br/&gt;**Value pattern:** `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/([0-9]|[1,2][0-9]|[3][0-2]))?$`&lt;br/&gt;|
| `connectivity.network.services` | **Services**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.services.cidrBlocks` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.services.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;10.244.0.0/16&#34;`&lt;br/&gt;**Value pattern:** `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/([0-9]|[1,2][0-9]|[3][0-2]))?$`&lt;br/&gt;|

### Control plane
Properties within the `.controlPlane` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controlPlane.etcd` | **Etcd**|**Type:** `object`&lt;br/&gt;|
| `controlPlane.etcd.imageRepository` | **Image repository**|**Type:** `string`&lt;br/&gt;|
| `controlPlane.etcd.imageTag` | **Image tag**|**Type:** `string`&lt;br/&gt;|
| `controlPlane.replicas` | **Number of nodes**|**Type:** `integer`&lt;br/&gt;|

### Kubeadm
Properties within the `.kubeadm` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubeadm.users` | **Users**|**Type:** `array`&lt;br/&gt;|
| `kubeadm.users[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `kubeadm.users[*].authorizedKeys` | **Authorized keys**|**Type:** `array`&lt;br/&gt;|
| `kubeadm.users[*].authorizedKeys[*]` | **Key**|**Type:** `string`&lt;br/&gt;|
| `kubeadm.users[*].name` | **Name**|**Type:** `string`&lt;br/&gt;|

### Kubectl image
Properties within the `.kubectlImage` top-level object
Used by cluster-shared library chart to configure coredns in-cluster.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` |**None**|**Type:** `string`&lt;br/&gt;|
| `kubectlImage.registry` |**None**|**Type:** `string`&lt;br/&gt;|
| `kubectlImage.tag` |**None**|**Type:** `string`&lt;br/&gt;|

### Kubernetes API server
Properties within the `.apiServer` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `apiServer.certSANs` | **Subject alternative names (SAN)** - Alternative names to encode in the API server&#39;s certificate.|**Type:** `array`&lt;br/&gt;**Default:** `[]`|
| `apiServer.certSANs[*]` | **SAN**|**Type:** `string`&lt;br/&gt;|
| `apiServer.enableAdmissionPlugins` | **Admission plugins** - Comma-separated list of admission plugins to enable.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;NamespaceLifecycle,LimitRanger,ServiceAccount,ResourceQuota,PersistentVolumeClaimResize,DefaultStorageClass,Priority,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook&#34;`|
| `apiServer.featureGates` | **Feature gates** - Enabled feature gates, as a comma-separated list.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;&#34;`|

### Kubernetes Controller Manager
Properties within the `.controllerManager` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controllerManager.featureGates` | **Feature gates** - Enabled feature gates, as a comma-separated list.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;&#34;`|

### Node template
Properties within the `.template` top-level object
Provisioning options for node templates.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `template.cloneMode` | **Clone mode** - Method used to clone template image.|**Type:** `string`&lt;br/&gt;|
| `template.diskGiB` | **Disk size (GB)** - Node disk size in GB. Must be at least as large as the source image.|**Type:** `integer`&lt;br/&gt;|
| `template.folder` | **Folder** - VSphere folder to deploy instances in. Must already exist.|**Type:** `string`&lt;br/&gt;|
| `template.memoryMiB` | **Memory (MB)** - Node memory allocation in MB.|**Type:** `integer`&lt;br/&gt;|
| `template.networkName` | **Segment name** - Segment name to attach nodes to. Must already exist.|**Type:** `string`&lt;br/&gt;|
| `template.numCPUs` | **CPU cores** - Number of CPUs to assign per node.|**Type:** `integer`&lt;br/&gt;|
| `template.resourcePool` | **Resource pool** - Resource pool to allocate nodes from. Must already exist.|**Type:** `string`&lt;br/&gt;|
| `template.storagePolicyName` | **Storage policy** - Storage policy to use. If specified, it must already exist.|**Type:** `string`&lt;br/&gt;|
| `template.templateName` | **Name** - Image template name to use for nodes.|**Type:** `string`&lt;br/&gt;|

### VCenter
Properties within the `.vcenter` top-level object
Configuration for vSphere API access.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `vcenter.datacenter` | **Datacenter** - Name of the datacenter to deploy nodes into.|**Type:** `string`&lt;br/&gt;|
| `vcenter.datastore` | **Datastore** - Name of the datastore for node disk storage.|**Type:** `string`&lt;br/&gt;|
| `vcenter.password` | **Password** - Password for the VSphere API.|**Type:** `string`&lt;br/&gt;|
| `vcenter.region` | **Region** - Category name in VSphere for topology.kubernetes.io/region labels.|**Type:** `string`&lt;br/&gt;|
| `vcenter.server` | **Server** - URL of the VSphere API.|**Type:** `string`&lt;br/&gt;|
| `vcenter.thumbprint` | **Thumbprint** - TLS certificate signature of the VSphere API.|**Type:** `string`&lt;br/&gt;|
| `vcenter.username` | **Username** - Username for the VSphere API.|**Type:** `string`&lt;br/&gt;|
| `vcenter.zone` | **Zone** - Category name in VSphere for topology.kubernetes.io/zone labels.|**Type:** `string`&lt;br/&gt;|

### Worker
Properties within the `.worker` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `worker.replicas` | **Number of nodes**|**Type:** `integer`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `organization` | **Organization**|**Type:** `string`&lt;br/&gt;|



&lt;!-- DOCS_END --&gt;

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-vsphere)
