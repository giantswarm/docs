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

&lt;!-- DOCS_START --&gt;

### 
Properties within the `.internal` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `internal.apiServer` |**None**|**Type:** `object`&lt;br/&gt;|
| `internal.apiServer.enableAdmissionPlugins` | **Admission plugins** - List of admission plugins to be passed to the API server via the --enable-admission-plugins flag.|**Type:** `array`&lt;br/&gt;**Default:** `[&#34;DefaultStorageClass&#34;,&#34;DefaultTolerationSeconds&#34;,&#34;LimitRanger&#34;,&#34;MutatingAdmissionWebhook&#34;,&#34;NamespaceLifecycle&#34;,&#34;PersistentVolumeClaimResize&#34;,&#34;Priority&#34;,&#34;ResourceQuota&#34;,&#34;ServiceAccount&#34;,&#34;ValidatingAdmissionWebhook&#34;]`|
| `internal.apiServer.enableAdmissionPlugins[*]` | **Plugin**|**Type:** `string`&lt;br/&gt;**Examples:** `&#34;DefaultStorageClass&#34;, &#34;Priority&#34;`&lt;br/&gt;**Value pattern:** `^[A-Za-z0-9]&#43;$`&lt;br/&gt;|
| `internal.apiServer.featureGates` | **Feature gates** - API server feature gate activation/deactivation.|**Type:** `array`&lt;br/&gt;**Default:** `[]`|
| `internal.apiServer.featureGates[*]` | **Feature gate**|**Type:** `object`&lt;br/&gt;|
| `internal.apiServer.featureGates[*].enabled` | **Enabled**|**Type:** `boolean`&lt;br/&gt;|
| `internal.apiServer.featureGates[*].name` | **Name**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;UserNamespacesStatelessPodsSupport&#34;`&lt;br/&gt;**Value pattern:** `^[A-Za-z0-9]&#43;$`&lt;br/&gt;|
| `internal.ciliumNetworkPolicy` | **CiliumNetworkPolicies**|**Type:** `object`&lt;br/&gt;|
| `internal.ciliumNetworkPolicy.enabled` | **Enable CiliumNetworkPolicies** - Installs the network-policies-app (deny all by default) if set to true|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `internal.controllerManager` | **Controller manager**|**Type:** `object`&lt;br/&gt;|
| `internal.controllerManager.featureGates` | **Feature gates** - Controller manager feature gate activation/deactivation.|**Type:** `array`&lt;br/&gt;**Default:** `[]`|
| `internal.controllerManager.featureGates[*]` | **Feature gate**|**Type:** `object`&lt;br/&gt;|
| `internal.controllerManager.featureGates[*].enabled` | **Enabled**|**Type:** `boolean`&lt;br/&gt;|
| `internal.controllerManager.featureGates[*].name` | **Name**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;UserNamespacesStatelessPodsSupport&#34;`&lt;br/&gt;**Value pattern:** `^[A-Za-z0-9]&#43;$`&lt;br/&gt;|
| `internal.kubernetesVersion` | **Kubernetes version**|**Type:** `string`&lt;br/&gt;|
| `internal.parentUid` | **Management cluster UID** - If set, create the cluster from a specific management cluster associated with this UID.|**Type:** `string`&lt;br/&gt;|
| `internal.rdeId` | **Runtime defined entity (RDE) identifier** - This cluster&#39;s RDE ID in the VCD API.|**Type:** `string`&lt;br/&gt;|
| `internal.sandboxContainerImage` | **Sandbox Container image (pause container)**|**Type:** `object`&lt;br/&gt;|
| `internal.sandboxContainerImage.name` | **Repository**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;giantswarm/pause&#34;`|
| `internal.sandboxContainerImage.registry` | **Registry**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;quay.io&#34;`|
| `internal.sandboxContainerImage.tag` | **Tag**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;3.9&#34;`|
| `internal.skipRde` | **Skip RDE** - Set to true if the API schema extension is installed in the correct version in VCD to create CAPVCD entities in the API. Set to false otherwise.|**Type:** `boolean`&lt;br/&gt;|
| `internal.useAsManagementCluster` | **Display as management cluster**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|

### Connectivity
Properties within the `.connectivity` top-level object
Configurations related to cluster connectivity such as container registries.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `connectivity.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`&lt;br/&gt;**Default:** `{}`|
| `connectivity.containerRegistries.*` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].credentials` | **Credentials** - Credentials for the endpoint.|**Type:** `object`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`&lt;br/&gt;|
| `connectivity.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network` | **Network**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint` | **Control plane endpoint** - Kubernetes API endpoint.|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint.host` | **Host**|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.controlPlaneEndpoint.port` | **Port number**|**Type:** `integer`&lt;br/&gt;**Default:** `6443`|
| `connectivity.network.extraOvdcNetworks` | **Extra OVDC networks** - OVDC networks to attach VMs to, additionally.|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.extraOvdcNetworks[*]` |**None**|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.hostEntries` | **Host entries**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.hostEntries[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.hostEntries[*].fqdn` | **FQDN**|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.hostEntries[*].ip` | **IP address**|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.loadBalancers` | **Load Balancers**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.loadBalancers.vipSubnet` | **Virtual IP subnet** - Virtual IP CIDR for the external network.|**Type:** `string`&lt;br/&gt;|
| `connectivity.network.pods` | **Pods**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.pods.cidrBlocks` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.pods.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;10.244.0.0/16&#34;`&lt;br/&gt;|
| `connectivity.network.services` | **Services**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.services.cidrBlocks` |**None**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.services.cidrBlocks[*]` |IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;10.244.0.0/16&#34;`&lt;br/&gt;|
| `connectivity.network.staticRoutes` | **Static routes**|**Type:** `array`&lt;br/&gt;|
| `connectivity.network.staticRoutes[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `connectivity.network.staticRoutes[*].destination` | **Destination** - IPv4 address range in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;10.128.0.0/16&#34;`&lt;br/&gt;|
| `connectivity.network.staticRoutes[*].via` | **Via**|**Type:** `string`&lt;br/&gt;|
| `connectivity.ntp` | **Time synchronization (NTP)** - Servers/pools to synchronize this cluster&#39;s clocks with.|**Type:** `object`&lt;br/&gt;|
| `connectivity.ntp.pools` | **Pools**|**Type:** `array`&lt;br/&gt;|
| `connectivity.ntp.pools[*]` | **Pool**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;ntp.ubuntu.com&#34;`&lt;br/&gt;|
| `connectivity.ntp.servers` | **Servers**|**Type:** `array`&lt;br/&gt;|
| `connectivity.ntp.servers[*]` | **Server**|**Type:** `string`&lt;br/&gt;|
| `connectivity.proxy` | **Proxy** - Whether/how outgoing traffic is routed through proxy servers.|**Type:** `object`&lt;br/&gt;|
| `connectivity.proxy.enabled` | **Enable**|**Type:** `boolean`&lt;br/&gt;|
| `connectivity.proxy.secretName` | **Secret name** - Name of a secret resource used by containerd to obtain the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables. If empty the value will be defaulted to &lt;clusterName&gt;-cluster-values.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[a-z0-9-]{0,63}$`&lt;br/&gt;|
| `connectivity.shell` | **Shell access**|**Type:** `object`&lt;br/&gt;|
| `connectivity.shell.osUsers` | **OS Users** - Configuration for OS users in cluster nodes.|**Type:** `array`&lt;br/&gt;**Default:** `[{&#34;name&#34;:&#34;giantswarm&#34;,&#34;sudo&#34;:&#34;ALL=(ALL) NOPASSWD:ALL&#34;}]`|
| `connectivity.shell.osUsers[*]` | **User**|**Type:** `object`&lt;br/&gt;|
| `connectivity.shell.osUsers[*].name` | **Name** - Username of the user.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[a-z][-a-z0-9]&#43;$`&lt;br/&gt;|
| `connectivity.shell.osUsers[*].sudo` | **Sudoers configuration** - Permissions string to add to /etc/sudoers for this user.|**Type:** `string`&lt;br/&gt;|
| `connectivity.shell.sshTrustedUserCAKeys` | **Trusted SSH cert issuers** - CA certificates of issuers that are trusted to sign SSH user certificates.|**Type:** `array`&lt;br/&gt;**Default:** `[&#34;ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM4cvZ01fLmO9cJbWUj7sfF&#43;NhECgy&#43;Cl0bazSrZX7sU vault-ca@vault.operations.giantswarm.io&#34;]`|
| `connectivity.shell.sshTrustedUserCAKeys[*]` |**None**|**Type:** `string`&lt;br/&gt;|

### Control plane
Properties within the `.controlPlane` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `controlPlane.catalog` | **Catalog** - Name of the VCD catalog in which the VM template is stored.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;giantswarm&#34;`&lt;br/&gt;|
| `controlPlane.certSANs` | **Subject alternative names (SAN)** - Alternative names to encode in the API server&#39;s certificate.|**Type:** `array`&lt;br/&gt;|
| `controlPlane.certSANs[*]` | **SAN**|**Type:** `string`&lt;br/&gt;|
| `controlPlane.customNodeLabels` | **Node labels**|**Type:** `array`&lt;br/&gt;|
| `controlPlane.customNodeLabels[*]` | **Custom node label**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;key=value&#34;`&lt;br/&gt;**Value pattern:** `^[A-Za-z0-9-_\./]{1,63}=[A-Za-z0-9-_\.]{0,63}$`&lt;br/&gt;|
| `controlPlane.diskSizeGB` | **Disk size**|**Type:** `integer`&lt;br/&gt;**Example:** `30`&lt;br/&gt;|
| `controlPlane.dns` | **DNS container image**|**Type:** `object`&lt;br/&gt;|
| `controlPlane.dns.imageRepository` | **Repository**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;projects.registry.vmware.com/tkg&#34;`&lt;br/&gt;**Default:** `&#34;projects.registry.vmware.com/tkg&#34;`|
| `controlPlane.dns.imageTag` | **Tag**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;v1.7.0_vmware.12&#34;`&lt;br/&gt;**Default:** `&#34;v1.7.0_vmware.12&#34;`|
| `controlPlane.etcd` | **Etcd container image**|**Type:** `object`&lt;br/&gt;|
| `controlPlane.etcd.imageRepository` | **Repository**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;giantswarm&#34;`&lt;br/&gt;**Default:** `&#34;giantswarm&#34;`|
| `controlPlane.etcd.imageTag` | **Tag**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;3.5.4-0-k8s&#34;`&lt;br/&gt;**Default:** `&#34;3.5.4-0-k8s&#34;`|
| `controlPlane.image` | **Node container image**|**Type:** `object`&lt;br/&gt;|
| `controlPlane.image.repository` | **Repository**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;projects.registry.vmware.com/tkg&#34;`&lt;br/&gt;**Default:** `&#34;projects.registry.vmware.com/tkg&#34;`|
| `controlPlane.oidc` | **OIDC authentication**|**Type:** `object`&lt;br/&gt;|
| `controlPlane.oidc.caFile` | **Certificate authority file** - Path to identity provider&#39;s CA certificate in PEM format.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.clientId` | **Client ID** - OIDC client identifier to identify with.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.groupsClaim` | **Groups claim** - Name of the identity token claim bearing the user&#39;s group memberships.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.groupsPrefix` | **Groups prefix** - Prefix prepended to groups values to prevent clashes with existing names.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.issuerUrl` | **Issuer URL** - URL of the provider which allows the API server to discover public signing keys, not including any path. Discovery URL without the &#39;/.well-known/openid-configuration&#39; part.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.usernameClaim` | **Username claim** - Name of the identity token claim bearing the unique user identifier.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.oidc.usernamePrefix` | **Username prefix** - Prefix prepended to username values to prevent clashes with existing names.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.placementPolicy` | **VM placement policy** - Name of the VCD VM placement policy to use.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.replicas` | **Number of nodes** - Number of control plane instances to create. Must be an odd number.|**Type:** `integer`&lt;br/&gt;**Default:** `1`|
| `controlPlane.resourceRatio` | **Resource ratio** - Ratio between node resources and apiserver resource requests.|**Type:** `integer`&lt;br/&gt;**Default:** `8`|
| `controlPlane.sizingPolicy` | **Sizing policy** - Name of the VCD sizing policy to use.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;m1.medium&#34;`&lt;br/&gt;|
| `controlPlane.storageProfile` | **Storage profile** - Name of the VCD storage profile to use.|**Type:** `string`&lt;br/&gt;|
| `controlPlane.template` | **Template** - Name of the template used to create the node VMs.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;ubuntu-2004-kube-v1.22.5&#34;`&lt;br/&gt;|

### Kubectl image
Properties within the `.kubectlImage` top-level object
Used by cluster-shared library chart to configure coredns in-cluster.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` | **Repository**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;giantswarm/kubectl&#34;`|
| `kubectlImage.registry` | **Registry**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;quay.io&#34;`|
| `kubectlImage.tag` | **Tag**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;1.23.5&#34;`|

### Metadata
Properties within the `.metadata` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `metadata.description` | **Cluster description** - User-friendly description of the cluster&#39;s purpose.|**Type:** `string`&lt;br/&gt;|
| `metadata.labels` | **Labels** - These labels are added to the Kubernetes resources defining this cluster.|**Type:** `object`&lt;br/&gt;|
| `metadata.labels.PATTERN` | **Label**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-zA-Z0-9/\._-]&#43;$`&lt;br/&gt;**Value pattern:** `^[a-zA-Z0-9\._-]&#43;$`&lt;br/&gt;|
| `metadata.organization` | **Organization**|**Type:** `string`&lt;br/&gt;|
| `metadata.preventDeletion` | **Prevent cluster deletion**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|
| `metadata.servicePriority` | **Service priority** - The relative importance of this cluster.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;highest&#34;`|

### Node pools
Properties within the `.nodePools` top-level object
Groups of worker nodes with identical configuration.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `nodePools.PATTERN` |**None**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]{3,10}$`&lt;br/&gt;|
| `nodePools.PATTERN.class` | **Node class** - A valid node class name, as specified in VMware Cloud Director (VCD) settings &gt; Node classes.|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]{3,10}$`&lt;br/&gt;**Value pattern:** `^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `nodePools.PATTERN.replicas` | **Number of nodes**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]{3,10}$`&lt;br/&gt;**Default:** `1`|

### VMware Cloud Director (VCD) settings
Properties within the `.providerSpecific` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `providerSpecific.cloudProviderInterface` | **Cloud provider interface (CPI)**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.cloudProviderInterface.enableVirtualServiceSharedIP` | **Share IPs in virtual services** - If enabled, multiple virtual services can share the same virtual IP address.|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `providerSpecific.cloudProviderInterface.oneArm` | **One-arm** - If enabled, use an internal IP for the virtual service with a NAT rule to expose the external IP. Otherwise the virtual service will be exposed directly with the external IP.|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.cloudProviderInterface.oneArm.enabled` | **Enable**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|
| `providerSpecific.containerStorageInterface` | **Container storage interface (CSI)**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.containerStorageInterface.storageClass` | **Pre-create storage class** - Pre-create storage class for the VCD CSI.|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.containerStorageInterface.storageClass.delete` | **Pre-create delete storage class**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.containerStorageInterface.storageClass.delete.isDefault` | **Default storage class**|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `providerSpecific.containerStorageInterface.storageClass.delete.vcdStorageProfileName` | **Name of storage profile in VCD**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;&#34;`|
| `providerSpecific.containerStorageInterface.storageClass.enabled` | **Enable**|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `providerSpecific.containerStorageInterface.storageClass.retain` | **Pre-create retain storage class**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.containerStorageInterface.storageClass.retain.isDefault` | **Default storage class**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|
| `providerSpecific.containerStorageInterface.storageClass.retain.vcdStorageProfileName` | **Name of storage profile in VCD**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;&#34;`|
| `providerSpecific.nodeClasses` | **Node classes** - Re-usable node configuration.|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN` |**None**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.catalog` | **Catalog** - Name of the VCD catalog in which the VM template is stored.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;giantswarm&#34;`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeLabels` | **Node labels**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeLabels[*]` | **Custom node label**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;key=value&#34;`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;**Value pattern:** `^[A-Za-z0-9-_\./]{1,63}=[A-Za-z0-9-_\.]{0,63}$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints` | **Node taints**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*]` | **Custom node taint**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].effect` |One of NoSchedule, PreferNoSchedule or NoExecute|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].key` |Name of the label on a node|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].value` |value of the label identified by the key|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.diskSizeGB` | **Disk size**|**Type:** `integer`&lt;br/&gt;**Example:** `30`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.placementPolicy` | **VM placement policy** - Name of the VCD VM placement policy to use.|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.sizingPolicy` | **Sizing policy** - Name of the VCD sizing policy to use.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;m1.medium&#34;`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.storageProfile` | **Storage profile** - Name of the VCD storage profile to use.|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.nodeClasses.PATTERN.template` | **Template** - Name of the template used to create the node VMs.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;ubuntu-2004-kube-v1.22.5&#34;`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9-]&#43;$`&lt;br/&gt;|
| `providerSpecific.org` | **Organization** - VCD organization name.|**Type:** `string`&lt;br/&gt;|
| `providerSpecific.ovdc` | **OvDC name** - Name of the organization virtual datacenter (OvDC) to create this cluster in.|**Type:** `string`&lt;br/&gt;|
| `providerSpecific.ovdcNetwork` | **OvDC network** - VCD network to connect VMs.|**Type:** `string`&lt;br/&gt;|
| `providerSpecific.site` | **Endpoint** - VCD endpoint URL in the format https://VCD_HOST, without trailing slash.|**Type:** `string`&lt;br/&gt;|
| `providerSpecific.userContext` | **VCD API access token**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.userContext.secretRef` | **Secret reference**|**Type:** `object`&lt;br/&gt;|
| `providerSpecific.userContext.secretRef.secretName` | **Name** - Name of the secret containing the VCD API token.|**Type:** `string`&lt;br/&gt;|
| `providerSpecific.vmNamingTemplate` | **VM naming template** - Go template to specify the VM naming convention.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;mytenant-{{ .machine.Name | sha256sum | trunc 7 }}&#34;`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `baseDomain` | **Base DNS domain**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;k8s.test&#34;`|
| `cluster-shared` | **Library chart**|**Type:** `object`&lt;br/&gt;|
| `managementCluster` | **Management cluster name** - The Cluster API management cluster that manages this cluster.|**Type:** `string`&lt;br/&gt;|
| `provider` | **Cluster API provider name**|**Type:** `string`&lt;br/&gt;|



&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/cluster-cloud-director)
