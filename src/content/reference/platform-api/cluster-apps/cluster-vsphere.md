---
title: cluster-vsphere chart reference
linkTitle: cluster-vsphere
description:  A helm chart for creating Cluster API clusters with the vSphere provider (CAPV).; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster-vsphere
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-vsphere?
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-vsphere
source_repository_ref: v0.9.8
---

The `cluster-vsphere` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API vSphere cluster.

## Chart configuration reference

###  {#}

---

`.internal.sandboxContainerImage`

**Type:** `object`

**Sandbox Container image**

---

`.internal.sandboxContainerImage.name`

**Type:** `string`

**Repository**

**Default:** `"tkg/pause"`

---

`.internal.sandboxContainerImage.registry`

**Type:** `string`

**Registry**

**Default:** `"projects.registry.vmware.com/"`

---

`.internal.sandboxContainerImage.tag`

**Type:** `string`

**Tag**

**Default:** `"3.7"`

---

`.internal.teleport`

**Type:** `object`

**Teleport**

---

`.internal.teleport.enabled`

**Type:** `boolean`

**Enable teleport**

**Default:** `true`

---

`.internal.teleport.proxyAddr`

**Type:** `string`

**Teleport proxy address**

**Default:** `"teleport.giantswarm.io:443"`

---

`.internal.teleport.version`

**Type:** `string`

**Teleport version**

**Default:** `"14.1.3"`

### Cluster {#cluster}

---

`.cluster.kubernetesVersion`

**Type:** `string`

**Kubernetes version**

### Connectivity {#connectivity}

---

`.connectivity.network`

**Type:** `object`

**Network**

---

`.connectivity.network.allowAllEgress`

**Type:** `boolean`

**Allow all egress**

**Default:** `false`

---

`.connectivity.network.containerRegistries`

**Type:** `object`

**Container registries**

Endpoints and credentials configuration for container registries.

**Default:** `{}`

---

`.connectivity.network.containerRegistries.*`

**Type:** `array`

---

`.connectivity.network.containerRegistries.*[*]`

**Type:** `object`

---

`.connectivity.network.containerRegistries.*[*].credentials`

**Type:** `object`

**Credentials**

Credentials for the endpoint.

---

`.connectivity.network.containerRegistries.*[*].credentials.auth`

**Type:** `string`

**Auth**

Base64-encoded string from the concatenation of the username, a colon, and the password.

---

`.connectivity.network.containerRegistries.*[*].credentials.identitytoken`

**Type:** `string`

**Identity token**

Used to authenticate the user and obtain an access token for the registry.

---

`.connectivity.network.containerRegistries.*[*].credentials.password`

**Type:** `string`

**Password**

Used to authenticate for the registry with username/password.

---

`.connectivity.network.containerRegistries.*[*].credentials.username`

**Type:** `string`

**Username**

Used to authenticate for the registry with username/password.

---

`.connectivity.network.containerRegistries.*[*].endpoint`

**Type:** `string`

**Endpoint**

Endpoint for the container registry.

---

`.connectivity.network.controlPlaneEndpoint`

**Type:** `object`

**Endpoint**

Kubernetes API configuration.

---

`.connectivity.network.controlPlaneEndpoint.host`

**Type:** `string`

**Host**

IP for access to the Kubernetes API.

---

`.connectivity.network.controlPlaneEndpoint.ipPoolName`

**Type:** `string`

**Ip Pool Name**

Ip for control plane will be drawn from this GlobalInClusterIPPool resource.

**Value pattern:** `^[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*$`

**Default:** `"wc-cp-ips"`

---

`.connectivity.network.controlPlaneEndpoint.port`

**Type:** `integer`

**Port number**

Port for access to the Kubernetes API.

---

`.connectivity.network.loadBalancers`

**Type:** `object`

**Load balancers**

---

`.connectivity.network.pods`

**Type:** `object`

**Pods**

---

`.connectivity.network.pods.cidrBlocks`

**Type:** `array`

---

`.connectivity.network.pods.cidrBlocks[*]`

**Type:** `string`

IPv4 address range, in CIDR notation.

**Example:** `"10.244.0.0/16"`

**Value pattern:** `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/([0-9]|[1,2][0-9]|[3][0-2]))?$`

---

`.connectivity.network.services`

**Type:** `object`

**Services**

---

`.connectivity.network.services.cidrBlocks`

**Type:** `array`

---

`.connectivity.network.services.cidrBlocks[*]`

**Type:** `string`

IPv4 address range, in CIDR notation.

**Example:** `"10.244.0.0/16"`

**Value pattern:** `^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(/([0-9]|[1,2][0-9]|[3][0-2]))?$`

### Control plane {#control-plane}

---

`.controlPlane.etcd`

**Type:** `object`

**Etcd**

---

`.controlPlane.etcd.imageRepository`

**Type:** `string`

**Image repository**

---

`.controlPlane.etcd.imageTag`

**Type:** `string`

**Image tag**

---

`.controlPlane.replicas`

**Type:** `integer`

**Number of nodes**

### Kubeadm {#kubeadm}

---

`.kubeadm.users`

**Type:** `array`

**Users**

---

`.kubeadm.users[*]`

**Type:** `object`

---

`.kubeadm.users[*].authorizedKeys`

**Type:** `array`

**Authorized keys**

---

`.kubeadm.users[*].authorizedKeys[*]`

**Type:** `string`

**Key**

---

`.kubeadm.users[*].name`

**Type:** `string`

**Name**

### Kubectl image {#kubectl-image}Used by cluster-shared library chart to configure coredns in-cluster.

---

`.kubectlImage.name`

**Type:** `string`

---

`.kubectlImage.registry`

**Type:** `string`

---

`.kubectlImage.tag`

**Type:** `string`

### Kubernetes API server {#kubernetes-api-server}

---

`.apiServer.certSANs`

**Type:** `array`

**Subject alternative names (SAN)**

Alternative names to encode in the API server's certificate.

**Default:** `[]`

---

`.apiServer.certSANs[*]`

**Type:** `string`

**SAN**

---

`.apiServer.enableAdmissionPlugins`

**Type:** `string`

**Admission plugins**

Comma-separated list of admission plugins to enable.

**Default:** `"NamespaceLifecycle,LimitRanger,ServiceAccount,ResourceQuota,PersistentVolumeClaimResize,DefaultStorageClass,Priority,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook"`

---

`.apiServer.featureGates`

**Type:** `string`

**Feature gates**

Enabled feature gates, as a comma-separated list.

**Default:** `""`

### Kubernetes Controller Manager {#kubernetes-controller-manager}

---

`.controllerManager.featureGates`

**Type:** `string`

**Feature gates**

Enabled feature gates, as a comma-separated list.

**Default:** `""`

### Node template {#node-template}Provisioning options for node templates.

---

`.template.cloneMode`

**Type:** `string`

**Clone mode**

Method used to clone template image.

---

`.template.diskGiB`

**Type:** `integer`

**Disk size (GB)**

Node disk size in GB. Must be at least as large as the source image.

---

`.template.folder`

**Type:** `string`

**Folder**

VSphere folder to deploy instances in. Must already exist.

---

`.template.memoryMiB`

**Type:** `integer`

**Memory (MB)**

Node memory allocation in MB.

---

`.template.networkName`

**Type:** `string`

**Segment name**

Segment name to attach nodes to. Must already exist.

---

`.template.numCPUs`

**Type:** `integer`

**CPU cores**

Number of CPUs to assign per node.

---

`.template.resourcePool`

**Type:** `string`

**Resource pool**

Resource pool to allocate nodes from. Must already exist.

---

`.template.storagePolicyName`

**Type:** `string`

**Storage policy**

Storage policy to use. If specified, it must already exist.

---

`.template.templateName`

**Type:** `string`

**Name**

Image template name to use for nodes.

### VCenter {#vcenter}Configuration for vSphere API access.

---

`.vcenter.datacenter`

**Type:** `string`

**Datacenter**

Name of the datacenter to deploy nodes into.

---

`.vcenter.datastore`

**Type:** `string`

**Datastore**

Name of the datastore for node disk storage.

---

`.vcenter.password`

**Type:** `string`

**Password**

Password for the VSphere API.

---

`.vcenter.region`

**Type:** `string`

**Region**

Category name in VSphere for topology.kubernetes.io/region labels.

---

`.vcenter.server`

**Type:** `string`

**Server**

URL of the VSphere API.

---

`.vcenter.thumbprint`

**Type:** `string`

**Thumbprint**

TLS certificate signature of the VSphere API.

---

`.vcenter.username`

**Type:** `string`

**Username**

Username for the VSphere API.

---

`.vcenter.zone`

**Type:** `string`

**Zone**

Category name in VSphere for topology.kubernetes.io/zone labels.

### Worker {#worker}

---

`.worker.replicas`

**Type:** `integer`

**Number of nodes**

### Other {#other}

---

`.organization`

**Type:** `string`

**Organization**

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-vsphere)
