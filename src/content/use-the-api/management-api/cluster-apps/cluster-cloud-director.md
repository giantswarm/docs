---
title: Cluster-Cloud-Director chart reference
linkTitle: cluster-cloud-director chart reference
description: |
  A helm chart for creating Cluster API clusters with the VMware Cloud Director (VCD) infrastructure provider (CAPVCD).
weight: 100
menu:
  main:
    identifier: cluster-cloud-director
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-cloud-director
source_repository_ref: v0.14.2
---

The `default-apps-cloud-director` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API VCD cluster.

# cluster-cloud-director values



### 
Properties within the `.internal` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `internal.apiServer` |**None**|**Type:** `object`|
| `internal.apiServer.enableAdmissionPlugins` | **Admission plugins** - List of admission plugins to be passed to the API server via the --enable-admission-plugins flag.|**Type:** `array`**Default:** `[&#34;DefaultStorageClass&#34;,&#34;DefaultTolerationSeconds&#34;,&#34;LimitRanger&#34;,&#34;MutatingAdmissionWebhook&#34;,&#34;NamespaceLifecycle&#34;,&#34;PersistentVolumeClaimResize&#34;,&#34;Priority&#34;,&#34;ResourceQuota&#34;,&#34;ServiceAccount&#34;,&#34;ValidatingAdmissionWebhook&#34;]`|
| `internal.apiServer.enableAdmissionPlugins[*]` | **Plugin**|**Type:** `string`|
| `internal.apiServer.featureGates` | **Feature gates** - API server feature gate activation/deactivation.|**Type:** `array`**Default:** `[]`|
| `internal.apiServer.featureGates[*]` | **Feature gate**|**Type:** `object`|
| `internal.apiServer.featureGates[*].enabled` | **Enabled**|**Type:** `boolean`|
| `internal.apiServer.featureGates[*].name` | **Name**|**Type:** `string`|
| `internal.ciliumNetworkPolicy` | **CiliumNetworkPolicies**|**Type:** `object`|
| `internal.ciliumNetworkPolicy.enabled` | **Enable CiliumNetworkPolicies** - Installs the network-policies-app (deny all by default) if set to true|**Type:** `boolean`**Default:** `true`|
| `internal.controllerManager` | **Controller manager**|**Type:** `object`|
| `internal.controllerManager.featureGates` | **Feature gates** - Controller manager feature gate activation/deactivation.|**Type:** `array`**Default:** `[]`|
| `internal.controllerManager.featureGates[*]` | **Feature gate**|**Type:** `object`|
| `internal.controllerManager.featureGates[*].enabled` | **Enabled**|**Type:** `boolean`|
| `internal.controllerManager.featureGates[*].name` | **Name**|**Type:** `string`|
| `internal.kubernetesVersion` | **Kubernetes version**|**Type:** `string`|
| `internal.parentUid` | **Management cluster UID** - If set, create the cluster from a specific management cluster associated with this UID.|**Type:** `string`|
| `internal.rdeId` | **Runtime defined entity (RDE) identifier** - This cluster&#39;s RDE ID in the VCD API.|**Type:** `string`|
| `internal.sandboxContainerImage` | **Sandbox Container image (pause container)**|**Type:** `object`|
| `internal.sandboxContainerImage.name` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm/pause&#34;`|
| `internal.sandboxContainerImage.registry` | **Registry**|**Type:** `string`**Default:** `&#34;quay.io&#34;`|
| `internal.sandboxContainerImage.tag` | **Tag**|**Type:** `string`**Default:** `&#34;3.9&#34;`|
| `internal.skipRde` | **Skip RDE** - Set to true if the API schema extension is installed in the correct version in VCD to create CAPVCD entities in the API. Set to false otherwise.|**Type:** `boolean`|
| `internal.useAsManagementCluster` | **Display as management cluster**|**Type:** `boolean`**Default:** `false`|

### Connectivity
Properties within the `.connectivity` top-level object
Configurations related to cluster connectivity such as container registries.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `connectivity.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`**Default:** `{}`|
| `connectivity.containerRegistries.*` |**None**|**Type:** `array`|
| `connectivity.containerRegistries.*[*]` |**None**|**Type:** `object`|
| `connectivity.containerRegistries.*[*].credentials` | **Credentials** - Credentials for the endpoint.|**Type:** `object`|
| `connectivity.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `connectivity.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`|
| `connectivity.network` | **Network**|**Type:** `object`|
| `connectivity.network.controlPlaneEndpoint` | **Control plane endpoint** - Kubernetes API endpoint.|**Type:** `object`|
| `connectivity.network.controlPlaneEndpoint.host` | **Host**|**Type:** `string`|
| `connectivity.network.controlPlaneEndpoint.port` | **Port number**|**Type:** `integer`**Default:** `6443`|
| `connectivity.network.extraOvdcNetworks` | **Extra OVDC networks** - OVDC networks to attach VMs to, additionally.|**Type:** `array`|
| `connectivity.network.extraOvdcNetworks[*]` |**None**|**Type:** `string`|
| `connectivity.network.hostEntries` | **Host entries**|**Type:** `array`|
| `connectivity.network.hostEntries[*]` |**None**|**Type:** `object`|
| `connectivity.network.hostEntries[*].fqdn` | **FQDN**|**Type:** `string`|
| `connectivity.network.hostEntries[*].ip` | **IP address**|**Type:** `string`|
| `connectivity.network.loadBalancers` | **Load Balancers**|**Type:** `object`|
| `connectivity.network.loadBalancers.vipSubnet` | **Virtual IP subnet** - Virtual IP CIDR for the external network.|**Type:** `string`|
| `connectivity.network.pods` | **Pods**|**Type:** `object`|
| `connectivity.network.pods.cidrBlocks` |**None**|**Type:** `array`|
| `connectivity.network.pods.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`|
| `connectivity.network.services` | **Services**|**Type:** `object`|
| `connectivity.network.services.cidrBlocks` |**None**|**Type:** `array`|
| `connectivity.network.services.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`|
| `connectivity.network.staticRoutes` | **Static routes**|**Type:** `array`|
| `connectivity.network.staticRoutes[*]` |**None**|**Type:** `object`|
| `connectivity.network.staticRoutes[*].destination` | **Destination** - IPv4 address range in CIDR notation.|**Type:** `string`|
| `connectivity.network.staticRoutes[*].via` | **Via**|**Type:** `string`|
| `connectivity.ntp` | **Time synchronization (NTP)** - Servers/pools to synchronize this cluster&#39;s clocks with.|**Type:** `object`|
| `connectivity.ntp.pools` | **Pools**|**Type:** `array`|
| `connectivity.ntp.pools[*]` | **Pool**|**Type:** `string`|
| `connectivity.ntp.servers` | **Servers**|**Type:** `array`|
| `connectivity.ntp.servers[*]` | **Server**|**Type:** `string`|
| `connectivity.proxy` | **Proxy** - Whether/how outgoing traffic is routed through proxy servers.|**Type:** `object`|
| `connectivity.proxy.enabled` | **Enable**|**Type:** `boolean`|
| `connectivity.proxy.secretName` | **Secret name** - Name of a secret resource used by containerd to obtain the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables. If empty the value will be defaulted to |
| `connectivity.shell` | **Shell access**|**Type:** `object`|
| `connectivity.shell.osUsers` | **OS Users** - Configuration for OS users in cluster nodes.|**Type:** `array`**Default:** `[{&#34;name&#34;:&#34;giantswarm&#34;,&#34;sudo&#34;:&#34;ALL=(ALL) NOPASSWD:ALL&#34;}]`|
| `connectivity.shell.osUsers[*]` | **User**|**Type:** `object`|
| `connectivity.shell.osUsers[*].name` | **Name** - Username of the user.|**Type:** `string`|
| `connectivity.shell.osUsers[*].sudo` | **Sudoers configuration** - Permissions string to add to /etc/sudoers for this user.|**Type:** `string`|
| `connectivity.shell.sshTrustedUserCAKeys` | **Trusted SSH cert issuers** - CA certificates of issuers that are trusted to sign SSH user certificates.|**Type:** `array`**Default:** `[&#34;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM4cvZ01fLmO9cJbWUj7sfF&#43;NhECgy&#43;Cl0bazSrZX7sU vault-ca@vault.operations.giantswarm.io&#34;]`|
| `connectivity.shell.sshTrustedUserCAKeys[*]` |**None**|**Type:** `string`|

### Control plane
Properties within the `.controlPlane` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controlPlane.catalog` | **Catalog** - Name of the VCD catalog in which the VM template is stored.|**Type:** `string`|
| `controlPlane.certSANs` | **Subject alternative names (SAN)** - Alternative names to encode in the API server&#39;s certificate.|**Type:** `array`|
| `controlPlane.certSANs[*]` | **SAN**|**Type:** `string`|
| `controlPlane.customNodeLabels` | **Node labels**|**Type:** `array`|
| `controlPlane.customNodeLabels[*]` | **Custom node label**|**Type:** `string`|
| `controlPlane.diskSizeGB` | **Disk size**|**Type:** `integer`|
| `controlPlane.dns` | **DNS container image**|**Type:** `object`|
| `controlPlane.dns.imageRepository` | **Repository**|**Type:** `string`**Default:** `&#34;projects.registry.vmware.com/tkg&#34;`|
| `controlPlane.dns.imageTag` | **Tag**|**Type:** `string`**Default:** `&#34;v1.7.0_vmware.12&#34;`|
| `controlPlane.etcd` | **Etcd container image**|**Type:** `object`|
| `controlPlane.etcd.imageRepository` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm&#34;`|
| `controlPlane.etcd.imageTag` | **Tag**|**Type:** `string`**Default:** `&#34;3.5.4-0-k8s&#34;`|
| `controlPlane.image` | **Node container image**|**Type:** `object`|
| `controlPlane.image.repository` | **Repository**|**Type:** `string`**Default:** `&#34;projects.registry.vmware.com/tkg&#34;`|
| `controlPlane.oidc` | **OIDC authentication**|**Type:** `object`|
| `controlPlane.oidc.caFile` | **Certificate authority file** - Path to identity provider&#39;s CA certificate in PEM format.|**Type:** `string`|
| `controlPlane.oidc.clientId` | **Client ID** - OIDC client identifier to identify with.|**Type:** `string`|
| `controlPlane.oidc.groupsClaim` | **Groups claim** - Name of the identity token claim bearing the user&#39;s group memberships.|**Type:** `string`|
| `controlPlane.oidc.groupsPrefix` | **Groups prefix** - Prefix prepended to groups values to prevent clashes with existing names.|**Type:** `string`|
| `controlPlane.oidc.issuerUrl` | **Issuer URL** - URL of the provider which allows the API server to discover public signing keys, not including any path. Discovery URL without the &#39;/.well-known/openid-configuration&#39; part.|**Type:** `string`|
| `controlPlane.oidc.usernameClaim` | **Username claim** - Name of the identity token claim bearing the unique user identifier.|**Type:** `string`|
| `controlPlane.oidc.usernamePrefix` | **Username prefix** - Prefix prepended to username values to prevent clashes with existing names.|**Type:** `string`|
| `controlPlane.placementPolicy` | **VM placement policy** - Name of the VCD VM placement policy to use.|**Type:** `string`|
| `controlPlane.replicas` | **Number of nodes** - Number of control plane instances to create. Must be an odd number.|**Type:** `integer`**Default:** `1`|
| `controlPlane.resourceRatio` | **Resource ratio** - Ratio between node resources and apiserver resource requests.|**Type:** `integer`**Default:** `8`|
| `controlPlane.sizingPolicy` | **Sizing policy** - Name of the VCD sizing policy to use.|**Type:** `string`|
| `controlPlane.storageProfile` | **Storage profile** - Name of the VCD storage profile to use.|**Type:** `string`|
| `controlPlane.template` | **Template** - Name of the template used to create the node VMs.|**Type:** `string`|

### Kubectl image
Properties within the `.kubectlImage` top-level object
Used by cluster-shared library chart to configure coredns in-cluster.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm/kubectl&#34;`|
| `kubectlImage.registry` | **Registry**|**Type:** `string`**Default:** `&#34;quay.io&#34;`|
| `kubectlImage.tag` | **Tag**|**Type:** `string`**Default:** `&#34;1.23.5&#34;`|

### Metadata
Properties within the `.metadata` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `metadata.description` | **Cluster description** - User-friendly description of the cluster&#39;s purpose.|**Type:** `string`|
| `metadata.labels` | **Labels** - These labels are added to the Kubernetes resources defining this cluster.|**Type:** `object`|
| `metadata.labels.PATTERN` | **Label**|**Type:** `string`|
| `metadata.organization` | **Organization**|**Type:** `string`|
| `metadata.preventDeletion` | **Prevent cluster deletion**|**Type:** `boolean`**Default:** `false`|
| `metadata.servicePriority` | **Service priority** - The relative importance of this cluster.|**Type:** `string`**Default:** `&#34;highest&#34;`|

### Node pools
Properties within the `.nodePools` top-level object
Groups of worker nodes with identical configuration.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `nodePools.PATTERN` |**None**|**Type:** `object`|
| `nodePools.PATTERN.class` | **Node class** - A valid node class name, as specified in VMware Cloud Director (VCD) settings &gt; Node classes.|**Type:** `string`|
| `nodePools.PATTERN.replicas` | **Number of nodes**|**Type:** `integer`**Default:** `1`|

### VMware Cloud Director (VCD) settings
Properties within the `.providerSpecific` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `providerSpecific.cloudProviderInterface` | **Cloud provider interface (CPI)**|**Type:** `object`|
| `providerSpecific.cloudProviderInterface.enableVirtualServiceSharedIP` | **Share IPs in virtual services** - If enabled, multiple virtual services can share the same virtual IP address.|**Type:** `boolean`**Default:** `true`|
| `providerSpecific.cloudProviderInterface.oneArm` | **One-arm** - If enabled, use an internal IP for the virtual service with a NAT rule to expose the external IP. Otherwise the virtual service will be exposed directly with the external IP.|**Type:** `object`|
| `providerSpecific.cloudProviderInterface.oneArm.enabled` | **Enable**|**Type:** `boolean`**Default:** `false`|
| `providerSpecific.containerStorageInterface` | **Container storage interface (CSI)**|**Type:** `object`|
| `providerSpecific.containerStorageInterface.storageClass` | **Pre-create storage class** - Pre-create storage class for the VCD CSI.|**Type:** `object`|
| `providerSpecific.containerStorageInterface.storageClass.delete` | **Pre-create delete storage class**|**Type:** `object`|
| `providerSpecific.containerStorageInterface.storageClass.delete.isDefault` | **Default storage class**|**Type:** `boolean`**Default:** `true`|
| `providerSpecific.containerStorageInterface.storageClass.delete.vcdStorageProfileName` | **Name of storage profile in VCD**|**Type:** `string`**Default:** `&#34;&#34;`|
| `providerSpecific.containerStorageInterface.storageClass.enabled` | **Enable**|**Type:** `boolean`**Default:** `true`|
| `providerSpecific.containerStorageInterface.storageClass.retain` | **Pre-create retain storage class**|**Type:** `object`|
| `providerSpecific.containerStorageInterface.storageClass.retain.isDefault` | **Default storage class**|**Type:** `boolean`**Default:** `false`|
| `providerSpecific.containerStorageInterface.storageClass.retain.vcdStorageProfileName` | **Name of storage profile in VCD**|**Type:** `string`**Default:** `&#34;&#34;`|
| `providerSpecific.nodeClasses` | **Node classes** - Re-usable node configuration.|**Type:** `object`|
| `providerSpecific.nodeClasses.PATTERN` |**None**|**Type:** `object`|
| `providerSpecific.nodeClasses.PATTERN.catalog` | **Catalog** - Name of the VCD catalog in which the VM template is stored.|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.customNodeLabels` | **Node labels**|**Type:** `array`|
| `providerSpecific.nodeClasses.PATTERN.customNodeLabels[*]` | **Custom node label**|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints` | **Node taints**|**Type:** `array`|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*]` | **Custom node taint**|**Type:** `object`|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].effect` |One of NoSchedule, PreferNoSchedule or NoExecute|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].key` |Name of the label on a node|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].value` |value of the label identified by the key|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.diskSizeGB` | **Disk size**|**Type:** `integer`|
| `providerSpecific.nodeClasses.PATTERN.placementPolicy` | **VM placement policy** - Name of the VCD VM placement policy to use.|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.sizingPolicy` | **Sizing policy** - Name of the VCD sizing policy to use.|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.storageProfile` | **Storage profile** - Name of the VCD storage profile to use.|**Type:** `string`|
| `providerSpecific.nodeClasses.PATTERN.template` | **Template** - Name of the template used to create the node VMs.|**Type:** `string`|
| `providerSpecific.org` | **Organization** - VCD organization name.|**Type:** `string`|
| `providerSpecific.ovdc` | **OvDC name** - Name of the organization virtual datacenter (OvDC) to create this cluster in.|**Type:** `string`|
| `providerSpecific.ovdcNetwork` | **OvDC network** - VCD network to connect VMs.|**Type:** `string`|
| `providerSpecific.site` | **Endpoint** - VCD endpoint URL in the format https://VCD_HOST, without trailing slash.|**Type:** `string`|
| `providerSpecific.userContext` | **VCD API access token**|**Type:** `object`|
| `providerSpecific.userContext.secretRef` | **Secret reference**|**Type:** `object`|
| `providerSpecific.userContext.secretRef.secretName` | **Name** - Name of the secret containing the VCD API token.|**Type:** `string`|
| `providerSpecific.vmNamingTemplate` | **VM naming template** - Go template to specify the VM naming convention.|**Type:** `string`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `baseDomain` | **Base DNS domain**|**Type:** `string`**Default:** `&#34;k8s.test&#34;`|
| `cluster-shared` | **Library chart**|**Type:** `object`|
| `managementCluster` | **Management cluster name** - The Cluster API management cluster that manages this cluster.|**Type:** `string`|
| `provider` | **Cluster API provider name**|**Type:** `string`|






## Further reading

- [Source repository](https://github.com/giantswarm/cluster-cloud-director)
