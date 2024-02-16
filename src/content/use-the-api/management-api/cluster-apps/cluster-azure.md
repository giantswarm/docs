---
title: Cluster-Azure chart reference
linkTitle: cluster-azure chart reference
description: |
  A helm chart for creating Cluster API clusters with the Azure infrastructure provider (CAPZ).
weight: 100
menu:
  main:
    identifier: cluster-azure
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-azure
source_repository_ref: v0.0.35
---

The `cluster-azure` chart templates all the Azure infrastructure resources that are necessary to create a Cluster API Azure cluster.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-aws version.

&lt;!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-azure/values.schema.json -o helm/cluster-azure/README.md

--&gt;



### Azure settings
Properties within the `.providerSpecific` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `providerSpecific.azureClusterIdentity` | **Identity** - AzureClusterIdentity resource to use for this cluster.|**Type:** `object`|
| `providerSpecific.azureClusterIdentity.name` | **Name**|**Type:** `string`**Default:** `&#34;cluster-identity&#34;`|
| `providerSpecific.azureClusterIdentity.namespace` | **Namespace**|**Type:** `string`**Default:** `&#34;org-giantswarm&#34;`|
| `providerSpecific.location` | **Location**|**Type:** `string`**Default:** `&#34;westeurope&#34;`|
| `providerSpecific.network` | **Azure network settings** - Azure VNet peering and other Azure-specific network settings.|**Type:** `object`|
| `providerSpecific.network.peerings` | **VNet peerings** - Specifying VNets (their resource groups and names) to which the peering is established.|**Type:** `array`**Default:** `[]`|
| `providerSpecific.network.peerings[*]` | **VNet peering**|**Type:** `object`|
| `providerSpecific.network.peerings[*].remoteVnetName` | **VNet name** - Name of the remote VNet to which the peering is established.|**Type:** `string`|
| `providerSpecific.network.peerings[*].resourceGroup` | **Resource group name** - Resource group for the remote VNet to which the peering is established.|**Type:** `string`|
| `providerSpecific.subscriptionId` | **Subscription ID** - ID of the Azure subscription this cluster will run in.|**Type:** `string`|

### Connectivity
Properties within the `.connectivity` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `connectivity.allowedCIDRs` | **List of CIDRs which have to been allowed to connect to the API Server endpoint**|**Type:** `array`**Default:** `[]`|
| `connectivity.allowedCIDRs[*]` |**None**|**Type:** `string`|
| `connectivity.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`**Default:** `{&#34;docker.io&#34;:[{&#34;endpoint&#34;:&#34;registry-1.docker.io&#34;},{&#34;endpoint&#34;:&#34;giantswarm.azurecr.io&#34;}]}`|
| `connectivity.containerRegistries.*` | **Registries** - Container registries and mirrors|**Type:** `array`|
| `connectivity.containerRegistries.*[*]` | **Registry**|**Type:** `object`|
| `connectivity.containerRegistries.*[*].credentials` | **Credentials**|**Type:** `object`|
| `connectivity.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`|
| `connectivity.network` | **Network**|**Type:** `object`|
| `connectivity.network.controlPlane` | **Control plane**|**Type:** `object`|
| `connectivity.network.controlPlane.cidr` | **Subnet**|**Type:** `string`**Default:** `&#34;10.0.0.0/20&#34;`|
| `connectivity.network.hostCidr` | **Node subnet** - IPv4 address range for nodes, in CIDR notation.|**Type:** `string`**Default:** `&#34;10.0.0.0/16&#34;`|
| `connectivity.network.mode` | **Network mode** - Specifying if the cluster resources are publicly accessible or not.|**Type:** `string`**Default:** `&#34;public&#34;`|
| `connectivity.network.podCidr` | **Pod subnet** - IPv4 address range for pods, in CIDR notation.|**Type:** `string`**Default:** `&#34;192.168.0.0/16&#34;`|
| `connectivity.network.serviceCidr` | **Service subnet** - IPv4 address range for services, in CIDR notation.|**Type:** `string`**Default:** `&#34;172.31.0.0/16&#34;`|
| `connectivity.network.workers` | **Workers**|**Type:** `object`|
| `connectivity.network.workers.cidr` | **Subnet**|**Type:** `string`**Default:** `&#34;10.0.16.0/20&#34;`|

### Control plane
Properties within the `.controlPlane` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controlPlane.containerdVolumeSizeGB` | **Containerd volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `controlPlane.encryptionAtHost` | **Encryption at host** - Enable encryption at host for the control plane nodes.|**Type:** `boolean`**Default:** `false`|
| `controlPlane.etcdVolumeSizeGB` | **Etcd volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `controlPlane.instanceType` | **Node VM size**|**Type:** `string`**Default:** `&#34;Standard_D4s_v3&#34;`|
| `controlPlane.kubeletVolumeSizeGB` | **Kubelet volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `controlPlane.oidc` | **OIDC authentication**|**Type:** `object`|
| `controlPlane.oidc.caPem` | **Certificate authority** - Identity provider&#39;s CA certificate in PEM format.|**Type:** `string`**Default:** `&#34;&#34;`|
| `controlPlane.oidc.clientId` | **Client ID**|**Type:** `string`**Default:** `&#34;&#34;`|
| `controlPlane.oidc.groupsClaim` | **Groups claim**|**Type:** `string`**Default:** `&#34;&#34;`|
| `controlPlane.oidc.issuerUrl` | **Issuer URL**|**Type:** `string`**Default:** `&#34;&#34;`|
| `controlPlane.oidc.usernameClaim` | **Username claim**|**Type:** `string`**Default:** `&#34;&#34;`|
| `controlPlane.replicas` | **Number of nodes**|**Type:** `integer`**Default:** `3`|
| `controlPlane.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`**Default:** `50`|

### Internal settings
Properties within the `.internal` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `internal.defaults` | **Default settings**|**Type:** `object`|
| `internal.defaults.evictionMinimumReclaim` | **Default settings for eviction minimum reclaim**|**Type:** `string`**Default:** `&#34;imagefs.available=5%,memory.available=100Mi,nodefs.available=5%&#34;`|
| `internal.defaults.hardEvictionThresholds` | **Default settings for hard eviction thresholds**|**Type:** `string`**Default:** `&#34;memory.available\u003c200Mi,nodefs.available\u003c10%,nodefs.inodesFree\u003c3%,imagefs.available\u003c10%,pid.available\u003c20%&#34;`|
| `internal.defaults.softEvictionGracePeriod` | **Default settings for soft eviction grace period**|**Type:** `string`**Default:** `&#34;memory.available=30s,nodefs.available=2m,nodefs.inodesFree=1m,imagefs.available=2m,pid.available=1m&#34;`|
| `internal.defaults.softEvictionThresholds` | **Default settings for soft eviction thresholds**|**Type:** `string`**Default:** `&#34;memory.available\u003c500Mi,nodefs.available\u003c15%,nodefs.inodesFree\u003c5%,imagefs.available\u003c15%,pid.available\u003c30%&#34;`|
| `internal.enableVpaResources` | **Enable VPA Resources in helmreleases**|**Type:** `boolean`**Default:** `true`|
| `internal.identity` | **Identity**|**Type:** `object`|
| `internal.identity.attachCapzControllerUserAssignedIdentity` | **Attach CAPZ controller UserAssigned identity**|**Type:** `boolean`**Default:** `false`|
| `internal.identity.systemAssignedScope` | **Scope of SystemAssignedIdentity**|**Type:** `string`**Default:** `&#34;ResourceGroup&#34;`|
| `internal.identity.type` | **Type of Identity**|**Type:** `string`**Default:** `&#34;SystemAssigned&#34;`|
| `internal.identity.userAssignedCustomIdentities` | **List of custom UserAssigned Identities to attach to all nodes**|**Type:** `array`**Default:** `[]`|
| `internal.image` | **Node Image**|**Type:** `object`|
| `internal.image.gallery` | **Gallery** - Name of the community gallery hosting the image|**Type:** `string`**Default:** `&#34;gsCapzFlatcar-41c2d140-ac44-4d8b-b7e1-7b2f1ddbe4d0&#34;`|
| `internal.image.name` | **Image Definition** - Name of the image definition in the Gallery|**Type:** `string`**Default:** `&#34;&#34;`|
| `internal.image.version` | **Image version**|**Type:** `string`**Default:** `&#34;3510.2.5&#34;`|
| `internal.kubectlImage` | **Kubectl Image settings**|**Type:** `object`|
| `internal.kubectlImage.name` | **Image name** - Name of the image Registry|**Type:** `string`**Default:** `&#34;giantswarm/kubectl&#34;`|
| `internal.kubectlImage.registry` | **Kubectl Image Registry** - Registry for the kubectl image|**Type:** `string`**Default:** `&#34;gsoci.azurecr.io&#34;`|
| `internal.kubectlImage.tag` | **Image tag**|**Type:** `string`**Default:** `&#34;1.23.5&#34;`|
| `internal.kubernetesVersion` | **Kubernetes version**|**Type:** `string`**Default:** `&#34;1.24.17&#34;`|
| `internal.network` | **Network configuration** - Internal network configuration that is susceptible to more frequent change|**Type:** `object`|
| `internal.network.subnets` | **VNet spec** - Customize subnets configuration|**Type:** `object`**Default:** `{}`|
| `internal.network.subnets.controlPlaneSubnetName` | **ControlPlane subnet name** - Name of the control plane subnet.|**Type:** `string`|
| `internal.network.subnets.nodeSubnetNatGatewayName` | **Nodes subnet nat-gateway name** - Name of the nat gateway on the nodes subnet.|**Type:** `string`|
| `internal.network.subnets.nodesSubnetName` | **Nodes subnet name** - Name of the nodes subnet.|**Type:** `string`|
| `internal.network.vnet` | **VNet spec** - Existing VNet configuration. This is susceptible to more frequent change or removal.|**Type:** `object`**Default:** `{}`|
| `internal.network.vnet.name` | **VNet name** - Name of the existing VNet.|**Type:** `string`|
| `internal.network.vnet.resourceGroup` | **Resource group name** - Resource group where the existing VNet is deployed.|**Type:** `string`|
| `internal.network.vpn` | **VPN configuration** - Internal VPN configuration that is susceptible to more frequent change|**Type:** `object`|
| `internal.network.vpn.gatewayMode` | **VPN gateway mode**|**Type:** `string`**Default:** `&#34;none&#34;`|
| `internal.sandboxContainerImage` | **The image used by sandbox / pause container**|**Type:** `object`|
| `internal.sandboxContainerImage.name` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm/pause&#34;`|
| `internal.sandboxContainerImage.registry` | **Registry**|**Type:** `string`**Default:** `&#34;gsoci.azurecr.io&#34;`|
| `internal.sandboxContainerImage.tag` | **Tag**|**Type:** `string`**Default:** `&#34;3.9&#34;`|
| `internal.teleport` | **Teleport**|**Type:** `object`|
| `internal.teleport.enabled` | **Enable teleport**|**Type:** `boolean`**Default:** `true`|
| `internal.teleport.proxyAddr` | **Teleport proxy address**|**Type:** `string`**Default:** `&#34;teleport.giantswarm.io:443&#34;`|
| `internal.teleport.version` | **Teleport version**|**Type:** `string`**Default:** `&#34;14.1.3&#34;`|

### Metadata
Properties within the `.metadata` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `metadata.description` | **Cluster description** - User-friendly description of the cluster&#39;s purpose.|**Type:** `string`|
| `metadata.labels` | **Labels** - These labels are added to the Kubernetes resources defining this cluster.|**Type:** `object`|
| `metadata.labels.PATTERN` | **Label**|**Type:** `string`|
| `metadata.name` | **Cluster name** - Unique identifier, cannot be changed after creation.|**Type:** `string`|
| `metadata.organization` | **Organization**|**Type:** `string`|
| `metadata.servicePriority` | **Service priority** - The relative importance of this cluster.|**Type:** `string`**Default:** `&#34;highest&#34;`|

### Node pools
Properties within the `.nodePools` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `nodePools[*].customNodeLabels` | **Custom node labels**|**Type:** `array`|
| `nodePools[*].customNodeLabels[*]` | **Label**|**Type:** `string`|
| `nodePools[*].customNodeTaints` | **Custom node taints**|**Type:** `array`|
| `nodePools[*].customNodeTaints[*]` | **Node taint**|**Type:** `object`|
| `nodePools[*].customNodeTaints[*].effect` | **Effect**|**Type:** `string`|
| `nodePools[*].customNodeTaints[*].key` | **Key**|**Type:** `string`|
| `nodePools[*].customNodeTaints[*].value` | **Value**|**Type:** `string`|
| `nodePools[*].disableHealthCheck` | **Disable HealthChecks for the MachineDeployment**|**Type:** `boolean`|
| `nodePools[*].encryptionAtHost` | **Encryption at host** - Enable encryption at host for the worker nodes.|**Type:** `boolean`**Default:** `false`|
| `nodePools[*].failureDomain` | **Availability zone**|**Type:** `string`|
| `nodePools[*].instanceType` | **VM size**|**Type:** `string`|
| `nodePools[*].name` | **Name** - Unique identifier, cannot be changed after creation.|**Type:** `string`|
| `nodePools[*].replicas` | **Number of nodes**|**Type:** `integer`|
| `nodePools[*].rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`|

### Pod Security Standards
Properties within the `.global.podSecurityStandards` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.podSecurityStandards.enforced` | **Enforced Pod Security Standards** - Use PSSs instead of PSPs.|**Type:** `boolean`**Default:** `false`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `baseDomain` | **Base DNS domain**|**Type:** `string`**Default:** `&#34;azuretest.gigantic.io&#34;`|
| `cluster-shared` | **Library chart**|**Type:** `object`|
| `managementCluster` | **The capi MC managing this cluster**|**Type:** `string`|
| `provider` | **Cluster API provider name**|**Type:** `string`|






## Further reading

- [Source repository](https://github.com/giantswarm/cluster-azure)
