---
title: cluster-azure chart reference
linkTitle: cluster-azure
description:  A helm chart for creating Cluster API clusters with the Azure infrastructure provider (CAPZ).; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster-azure
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-azure?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-azure
source_repository_ref: v0.0.35
---

The `cluster-azure` chart templates all the Azure infrastructure resources that are necessary to create a Cluster API Azure cluster.

## Chart configuration reference

### Azure settings {#azure-settings}

---

`.providerSpecific.azureClusterIdentity`

**Type:** `object`

**Identity**

AzureClusterIdentity resource to use for this cluster.

---

`.providerSpecific.azureClusterIdentity.name`

**Type:** `string`

**Name**

**Default:** `"cluster-identity"`

---

`.providerSpecific.azureClusterIdentity.namespace`

**Type:** `string`

**Namespace**

**Default:** `"org-giantswarm"`

---

`.providerSpecific.location`

**Type:** `string`

**Location**

**Allowed values:** `eastus`, `germanywestcentral`, `northeurope`, `westeurope`, `westus2`

**Default:** `"westeurope"`

---

`.providerSpecific.network`

**Type:** `object`

**Azure network settings**

Azure VNet peering and other Azure-specific network settings.

---

`.providerSpecific.network.peerings`

**Type:** `array`

**VNet peerings**

Specifying VNets (their resource groups and names) to which the peering is established.

**Default:** `[]`

---

`.providerSpecific.network.peerings[*]`

**Type:** `object`

**VNet peering**

---

`.providerSpecific.network.peerings[*].remoteVnetName`

**Type:** `string`

**VNet name**

Name of the remote VNet to which the peering is established.

**Value pattern:** `^[-\w\._]+$`

---

`.providerSpecific.network.peerings[*].resourceGroup`

**Type:** `string`

**Resource group name**

Resource group for the remote VNet to which the peering is established.

**Value pattern:** `^[-\w\._\(\)]+$`

---

`.providerSpecific.subscriptionId`

**Type:** `string`

**Subscription ID**

ID of the Azure subscription this cluster will run in.

**Example:** `"291bba3f-e0a5-47bc-a099-3bdcb2a50a05"`

**Value pattern:** `^[a-fA-F0-9][-a-fA-F0-9]+[a-fA-F0-9]$`

### Connectivity {#connectivity}

---

`.connectivity.allowedCIDRs`

**Type:** `array`

**List of CIDRs which have to been allowed to connect to the API Server endpoint**

**Default:** `[]`

---

`.connectivity.allowedCIDRs[*]`

**Type:** `string`

---

`.connectivity.containerRegistries`

**Type:** `object`

**Container registries**

Endpoints and credentials configuration for container registries.

**Default:** `{"docker.io":[{"endpoint":"registry-1.docker.io"},{"endpoint":"giantswarm.azurecr.io"}]}`

---

`.connectivity.containerRegistries.*`

**Type:** `array`

**Registries**

Container registries and mirrors

---

`.connectivity.containerRegistries.*[*]`

**Type:** `object`

**Registry**

---

`.connectivity.containerRegistries.*[*].credentials`

**Type:** `object`

**Credentials**

---

`.connectivity.containerRegistries.*[*].credentials.auth`

**Type:** `string`

**Auth**

Base64-encoded string from the concatenation of the username, a colon, and the password.

---

`.connectivity.containerRegistries.*[*].credentials.identitytoken`

**Type:** `string`

**Identity token**

Used to authenticate the user and obtain an access token for the registry.

---

`.connectivity.containerRegistries.*[*].credentials.password`

**Type:** `string`

**Password**

Used to authenticate for the registry with username/password.

---

`.connectivity.containerRegistries.*[*].credentials.username`

**Type:** `string`

**Username**

Used to authenticate for the registry with username/password.

---

`.connectivity.containerRegistries.*[*].endpoint`

**Type:** `string`

**Endpoint**

Endpoint for the container registry.

---

`.connectivity.network`

**Type:** `object`

**Network**

---

`.connectivity.network.controlPlane`

**Type:** `object`

**Control plane**

---

`.connectivity.network.controlPlane.cidr`

**Type:** `string`

**Subnet**

**Default:** `"10.0.0.0/20"`

---

`.connectivity.network.hostCidr`

**Type:** `string`

**Node subnet**

IPv4 address range for nodes, in CIDR notation.

**Default:** `"10.0.0.0/16"`

---

`.connectivity.network.mode`

**Type:** `string`

**Network mode**

Specifying if the cluster resources are publicly accessible or not.

**Allowed values:** `public`, `private`

**Default:** `"public"`

---

`.connectivity.network.podCidr`

**Type:** `string`

**Pod subnet**

IPv4 address range for pods, in CIDR notation.

**Default:** `"192.168.0.0/16"`

---

`.connectivity.network.serviceCidr`

**Type:** `string`

**Service subnet**

IPv4 address range for services, in CIDR notation.

**Default:** `"172.31.0.0/16"`

---

`.connectivity.network.workers`

**Type:** `object`

**Workers**

---

`.connectivity.network.workers.cidr`

**Type:** `string`

**Subnet**

**Default:** `"10.0.16.0/20"`

### Control plane {#control-plane}

---

`.controlPlane.containerdVolumeSizeGB`

**Type:** `integer`

**Containerd volume size (GB)**

**Default:** `100`

---

`.controlPlane.encryptionAtHost`

**Type:** `boolean`

**Encryption at host**

Enable encryption at host for the control plane nodes.

**Default:** `false`

---

`.controlPlane.etcdVolumeSizeGB`

**Type:** `integer`

**Etcd volume size (GB)**

**Default:** `100`

---

`.controlPlane.instanceType`

**Type:** `string`

**Node VM size**

**Default:** `"Standard_D4s_v3"`

---

`.controlPlane.kubeletVolumeSizeGB`

**Type:** `integer`

**Kubelet volume size (GB)**

**Default:** `100`

---

`.controlPlane.oidc`

**Type:** `object`

**OIDC authentication**

---

`.controlPlane.oidc.caPem`

**Type:** `string`

**Certificate authority**

Identity provider's CA certificate in PEM format.

**Default:** `""`

---

`.controlPlane.oidc.clientId`

**Type:** `string`

**Client ID**

**Default:** `""`

---

`.controlPlane.oidc.groupsClaim`

**Type:** `string`

**Groups claim**

**Default:** `""`

---

`.controlPlane.oidc.issuerUrl`

**Type:** `string`

**Issuer URL**

**Default:** `""`

---

`.controlPlane.oidc.usernameClaim`

**Type:** `string`

**Username claim**

**Default:** `""`

---

`.controlPlane.replicas`

**Type:** `integer`

**Number of nodes**

**Default:** `3`

---

`.controlPlane.rootVolumeSizeGB`

**Type:** `integer`

**Root volume size (GB)**

**Default:** `50`

### Internal settings {#internal-settings}

---

`.internal.defaults`

**Type:** `object`

**Default settings**

---

`.internal.defaults.evictionMinimumReclaim`

**Type:** `string`

**Default settings for eviction minimum reclaim**

**Default:** `"imagefs.available=5%,memory.available=100Mi,nodefs.available=5%"`

---

`.internal.defaults.hardEvictionThresholds`

**Type:** `string`

**Default settings for hard eviction thresholds**

**Default:** `"memory.available\u003c200Mi,nodefs.available\u003c10%,nodefs.inodesFree\u003c3%,imagefs.available\u003c10%,pid.available\u003c20%"`

---

`.internal.defaults.softEvictionGracePeriod`

**Type:** `string`

**Default settings for soft eviction grace period**

**Default:** `"memory.available=30s,nodefs.available=2m,nodefs.inodesFree=1m,imagefs.available=2m,pid.available=1m"`

---

`.internal.defaults.softEvictionThresholds`

**Type:** `string`

**Default settings for soft eviction thresholds**

**Default:** `"memory.available\u003c500Mi,nodefs.available\u003c15%,nodefs.inodesFree\u003c5%,imagefs.available\u003c15%,pid.available\u003c30%"`

---

`.internal.enableVpaResources`

**Type:** `boolean`

**Enable VPA Resources in helmreleases**

**Default:** `true`

---

`.internal.identity`

**Type:** `object`

**Identity**

---

`.internal.identity.attachCapzControllerUserAssignedIdentity`

**Type:** `boolean`

**Attach CAPZ controller UserAssigned identity**

**Default:** `false`

---

`.internal.identity.systemAssignedScope`

**Type:** `string`

**Scope of SystemAssignedIdentity**

**Allowed values:** `Subscription`, `ResourceGroup`

**Default:** `"ResourceGroup"`

---

`.internal.identity.type`

**Type:** `string`

**Type of Identity**

**Allowed values:** `SystemAssigned`, `UserAssigned`

**Default:** `"SystemAssigned"`

---

`.internal.identity.userAssignedCustomIdentities`

**Type:** `array`

**List of custom UserAssigned Identities to attach to all nodes**

**Default:** `[]`

---

`.internal.image`

**Type:** `object`

**Node Image**

---

`.internal.image.gallery`

**Type:** `string`

**Gallery**

Name of the community gallery hosting the image

**Default:** `"gsCapzFlatcar-41c2d140-ac44-4d8b-b7e1-7b2f1ddbe4d0"`

---

`.internal.image.name`

**Type:** `string`

**Image Definition**

Name of the image definition in the Gallery

**Default:** `""`

---

`.internal.image.version`

**Type:** `string`

**Image version**

**Default:** `"3510.2.5"`

---

`.internal.kubectlImage`

**Type:** `object`

**Kubectl Image settings**

---

`.internal.kubectlImage.name`

**Type:** `string`

**Image name**

Name of the image Registry

**Default:** `"giantswarm/kubectl"`

---

`.internal.kubectlImage.registry`

**Type:** `string`

**Kubectl Image Registry**

Registry for the kubectl image

**Default:** `"gsoci.azurecr.io"`

---

`.internal.kubectlImage.tag`

**Type:** `string`

**Image tag**

**Default:** `"1.23.5"`

---

`.internal.kubernetesVersion`

**Type:** `string`

**Kubernetes version**

**Default:** `"1.24.17"`

---

`.internal.network`

**Type:** `object`

**Network configuration**

Internal network configuration that is susceptible to more frequent change

---

`.internal.network.subnets`

**Type:** `object`

**VNet spec**

Customize subnets configuration

**Default:** `{}`

---

`.internal.network.subnets.controlPlaneSubnetName`

**Type:** `string`

**ControlPlane subnet name**

Name of the control plane subnet.

**Value pattern:** `^[-\w\._]+$`

---

`.internal.network.subnets.nodeSubnetNatGatewayName`

**Type:** `string`

**Nodes subnet nat-gateway name**

Name of the nat gateway on the nodes subnet.

**Value pattern:** `^[-\w\._]+$`

---

`.internal.network.subnets.nodesSubnetName`

**Type:** `string`

**Nodes subnet name**

Name of the nodes subnet.

**Value pattern:** `^[-\w\._]+$`

---

`.internal.network.vnet`

**Type:** `object`

**VNet spec**

Existing VNet configuration. This is susceptible to more frequent change or removal.

**Default:** `{}`

---

`.internal.network.vnet.name`

**Type:** `string`

**VNet name**

Name of the existing VNet.

**Value pattern:** `^[-\w\._]+$`

---

`.internal.network.vnet.resourceGroup`

**Type:** `string`

**Resource group name**

Resource group where the existing VNet is deployed.

**Value pattern:** `^[-\w\._\(\)]+$`

---

`.internal.network.vpn`

**Type:** `object`

**VPN configuration**

Internal VPN configuration that is susceptible to more frequent change

---

`.internal.network.vpn.gatewayMode`

**Type:** `string`

**VPN gateway mode**

**Allowed values:** `local`, `none`, `remote`

**Default:** `"none"`

---

`.internal.sandboxContainerImage`

**Type:** `object`

**The image used by sandbox / pause container**

---

`.internal.sandboxContainerImage.name`

**Type:** `string`

**Repository**

**Default:** `"giantswarm/pause"`

---

`.internal.sandboxContainerImage.registry`

**Type:** `string`

**Registry**

**Default:** `"gsoci.azurecr.io"`

---

`.internal.sandboxContainerImage.tag`

**Type:** `string`

**Tag**

**Default:** `"3.9"`

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

### Metadata {#metadata}

---

`.metadata.description`

**Type:** `string`

**Cluster description**

User-friendly description of the cluster's purpose.

---

`.metadata.labels`

**Type:** `object`

**Labels**

These labels are added to the Kubernetes resources defining this cluster.

---

`.metadata.labels.PATTERN`

**Type:** `string`

**Label**

**Key pattern:** `PATTERN`=`^[a-zA-Z0-9/\._-]+$`

**Value pattern:** `^[a-zA-Z0-9\._-]+$`

---

`.metadata.name`

**Type:** `string`

**Cluster name**

Unique identifier, cannot be changed after creation.

---

`.metadata.organization`

**Type:** `string`

**Organization**

---

`.metadata.servicePriority`

**Type:** `string`

**Service priority**

The relative importance of this cluster.

**Allowed values:** `highest`, `medium`, `lowest`

**Default:** `"highest"`

### Node pools {#node-pools}

---

`.nodePools[*].customNodeLabels`

**Type:** `array`

**Custom node labels**

---

`.nodePools[*].customNodeLabels[*]`

**Type:** `string`

**Label**

---

`.nodePools[*].customNodeTaints`

**Type:** `array`

**Custom node taints**

---

`.nodePools[*].customNodeTaints[*]`

**Type:** `object`

**Node taint**

---

`.nodePools[*].customNodeTaints[*].effect`

**Type:** `string`

**Effect**

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.nodePools[*].customNodeTaints[*].key`

**Type:** `string`

**Key**

---

`.nodePools[*].customNodeTaints[*].value`

**Type:** `string`

**Value**

---

`.nodePools[*].disableHealthCheck`

**Type:** `boolean`

**Disable HealthChecks for the MachineDeployment**

---

`.nodePools[*].encryptionAtHost`

**Type:** `boolean`

**Encryption at host**

Enable encryption at host for the worker nodes.

**Default:** `false`

---

`.nodePools[*].failureDomain`

**Type:** `string`

**Availability zone**

**Allowed values:** `1`, `2`, `3`

---

`.nodePools[*].instanceType`

**Type:** `string`

**VM size**

---

`.nodePools[*].name`

**Type:** `string`

**Name**

Unique identifier, cannot be changed after creation.

**Value pattern:** `^[-\w\._]+$`

---

`.nodePools[*].replicas`

**Type:** `integer`

**Number of nodes**

---

`.nodePools[*].rootVolumeSizeGB`

**Type:** `integer`

**Root volume size (GB)**

### Pod Security Standards {#pod-security-standards}

---

`.global.podSecurityStandards.enforced`

**Type:** `boolean`

**Enforced Pod Security Standards**

Use PSSs instead of PSPs.

**Default:** `false`

### Other {#other}

---

`.baseDomain`

**Type:** `string`

**Base DNS domain**

**Default:** `"azuretest.gigantic.io"`

---

`.cluster-shared`

**Type:** `object`

**Library chart**

---

`.managementCluster`

**Type:** `string`

**The capi MC managing this cluster**

---

`.provider`

**Type:** `string`

**Cluster API provider name**

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-azure)
