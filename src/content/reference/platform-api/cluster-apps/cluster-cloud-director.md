---
title: cluster-cloud-director chart reference
linkTitle: cluster-cloud-director
description:  A helm chart for creating Cluster API clusters with the VMware Cloud Director (VCD) infrastructure provider (CAPVCD).; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster-cloud-director
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-cloud-director?
owner:
- https://github.com/orgs/giantswarm/teams/team-rocket
source_repository: https://github.com/giantswarm/cluster-cloud-director
source_repository_ref: v0.14.2
---

The `cluster-cloud-director` chart templates all the VMware infrastructure resources that are necessary to create a Cluster API VCD cluster.

## Chart configuration reference

###  {#}

---

`.internal.apiServer`

**Type:** `object`

---

`.internal.apiServer.enableAdmissionPlugins`

**Type:** `array`

**Admission plugins**

List of admission plugins to be passed to the API server via the --enable-admission-plugins flag.

**Default:** `["DefaultStorageClass","DefaultTolerationSeconds","LimitRanger","MutatingAdmissionWebhook","NamespaceLifecycle","PersistentVolumeClaimResize","Priority","ResourceQuota","ServiceAccount","ValidatingAdmissionWebhook"]`

---

`.internal.apiServer.enableAdmissionPlugins[*]`

**Type:** `string`

**Plugin**

**Examples:** `"DefaultStorageClass"`, `"Priority"`

**Value pattern:** `^[A-Za-z0-9]+$`

---

`.internal.apiServer.featureGates`

**Type:** `array`

**Feature gates**

API server feature gate activation/deactivation.

**Default:** `[]`

---

`.internal.apiServer.featureGates[*]`

**Type:** `object`

**Feature gate**

---

`.internal.apiServer.featureGates[*].enabled`

**Type:** `boolean`

**Enabled**

---

`.internal.apiServer.featureGates[*].name`

**Type:** `string`

**Name**

**Example:** `"UserNamespacesStatelessPodsSupport"`

**Value pattern:** `^[A-Za-z0-9]+$`

---

`.internal.ciliumNetworkPolicy`

**Type:** `object`

**CiliumNetworkPolicies**

---

`.internal.ciliumNetworkPolicy.enabled`

**Type:** `boolean`

**Enable CiliumNetworkPolicies**

Installs the network-policies-app (deny all by default) if set to true

**Default:** `true`

---

`.internal.controllerManager`

**Type:** `object`

**Controller manager**

---

`.internal.controllerManager.featureGates`

**Type:** `array`

**Feature gates**

Controller manager feature gate activation/deactivation.

**Default:** `[]`

---

`.internal.controllerManager.featureGates[*]`

**Type:** `object`

**Feature gate**

---

`.internal.controllerManager.featureGates[*].enabled`

**Type:** `boolean`

**Enabled**

---

`.internal.controllerManager.featureGates[*].name`

**Type:** `string`

**Name**

**Example:** `"UserNamespacesStatelessPodsSupport"`

**Value pattern:** `^[A-Za-z0-9]+$`

---

`.internal.kubernetesVersion`

**Type:** `string`

**Kubernetes version**

---

`.internal.parentUid`

**Type:** `string`

**Management cluster UID**

If set, create the cluster from a specific management cluster associated with this UID.

---

`.internal.rdeId`

**Type:** `string`

**Runtime defined entity (RDE) identifier**

This cluster's RDE ID in the VCD API.

---

`.internal.sandboxContainerImage`

**Type:** `object`

**Sandbox Container image (pause container)**

---

`.internal.sandboxContainerImage.name`

**Type:** `string`

**Repository**

**Default:** `"giantswarm/pause"`

---

`.internal.sandboxContainerImage.registry`

**Type:** `string`

**Registry**

**Default:** `"quay.io"`

---

`.internal.sandboxContainerImage.tag`

**Type:** `string`

**Tag**

**Default:** `"3.9"`

---

`.internal.skipRde`

**Type:** `boolean`

**Skip RDE**

Set to true if the API schema extension is installed in the correct version in VCD to create CAPVCD entities in the API. Set to false otherwise.

---

`.internal.useAsManagementCluster`

**Type:** `boolean`

**Display as management cluster**

**Default:** `false`

### Connectivity {#connectivity}Configurations related to cluster connectivity such as container registries.

---

`.connectivity.containerRegistries`

**Type:** `object`

**Container registries**

Endpoints and credentials configuration for container registries.

**Default:** `{}`

---

`.connectivity.containerRegistries.*`

**Type:** `array`

---

`.connectivity.containerRegistries.*[*]`

**Type:** `object`

---

`.connectivity.containerRegistries.*[*].credentials`

**Type:** `object`

**Credentials**

Credentials for the endpoint.

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

`.connectivity.network.controlPlaneEndpoint`

**Type:** `object`

**Control plane endpoint**

Kubernetes API endpoint.

---

`.connectivity.network.controlPlaneEndpoint.host`

**Type:** `string`

**Host**

---

`.connectivity.network.controlPlaneEndpoint.port`

**Type:** `integer`

**Port number**

**Default:** `6443`

---

`.connectivity.network.extraOvdcNetworks`

**Type:** `array`

**Extra OVDC networks**

OVDC networks to attach VMs to, additionally.

---

`.connectivity.network.extraOvdcNetworks[*]`

**Type:** `string`

---

`.connectivity.network.hostEntries`

**Type:** `array`

**Host entries**

---

`.connectivity.network.hostEntries[*]`

**Type:** `object`

---

`.connectivity.network.hostEntries[*].fqdn`

**Type:** `string`

**FQDN**

---

`.connectivity.network.hostEntries[*].ip`

**Type:** `string`

**IP address**

---

`.connectivity.network.loadBalancers`

**Type:** `object`

**Load Balancers**

---

`.connectivity.network.loadBalancers.vipSubnet`

**Type:** `string`

**Virtual IP subnet**

Virtual IP CIDR for the external network.

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

---

`.connectivity.network.staticRoutes`

**Type:** `array`

**Static routes**

---

`.connectivity.network.staticRoutes[*]`

**Type:** `object`

---

`.connectivity.network.staticRoutes[*].destination`

**Type:** `string`

**Destination**

IPv4 address range in CIDR notation.

**Example:** `"10.128.0.0/16"`

---

`.connectivity.network.staticRoutes[*].via`

**Type:** `string`

**Via**

---

`.connectivity.ntp`

**Type:** `object`

**Time synchronization (NTP)**

Servers/pools to synchronize this cluster's clocks with.

---

`.connectivity.ntp.pools`

**Type:** `array`

**Pools**

---

`.connectivity.ntp.pools[*]`

**Type:** `string`

**Pool**

**Example:** `"ntp.ubuntu.com"`

---

`.connectivity.ntp.servers`

**Type:** `array`

**Servers**

---

`.connectivity.ntp.servers[*]`

**Type:** `string`

**Server**

---

`.connectivity.proxy`

**Type:** `object`

**Proxy**

Whether/how outgoing traffic is routed through proxy servers.

---

`.connectivity.proxy.enabled`

**Type:** `boolean`

**Enable**

---

`.connectivity.proxy.secretName`

**Type:** `string`

**Secret name**

Name of a secret resource used by containerd to obtain the HTTP_PROXY, HTTPS_PROXY, and NO_PROXY environment variables. If empty the value will be defaulted to <clusterName>-cluster-values.

**Value pattern:** `^[a-z0-9-]{0,63}$`

---

`.connectivity.shell`

**Type:** `object`

**Shell access**

---

`.connectivity.shell.osUsers`

**Type:** `array`

**OS Users**

Configuration for OS users in cluster nodes.

**Default:** `[{"name":"giantswarm","sudo":"ALL=(ALL) NOPASSWD:ALL"}]`

---

`.connectivity.shell.osUsers[*]`

**Type:** `object`

**User**

---

`.connectivity.shell.osUsers[*].name`

**Type:** `string`

**Name**

Username of the user.

**Value pattern:** `^[a-z][-a-z0-9]+$`

---

`.connectivity.shell.osUsers[*].sudo`

**Type:** `string`

**Sudoers configuration**

Permissions string to add to /etc/sudoers for this user.

---

`.connectivity.shell.sshTrustedUserCAKeys`

**Type:** `array`

**Trusted SSH cert issuers**

CA certificates of issuers that are trusted to sign SSH user certificates.

**Default:** `["ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM4cvZ01fLmO9cJbWUj7sfF+NhECgy+Cl0bazSrZX7sU vault-ca@vault.operations.giantswarm.io"]`

---

`.connectivity.shell.sshTrustedUserCAKeys[*]`

**Type:** `string`

### Control plane {#control-plane}

---

`.controlPlane.catalog`

**Type:** `string`

**Catalog**

Name of the VCD catalog in which the VM template is stored.

**Example:** `"giantswarm"`

---

`.controlPlane.certSANs`

**Type:** `array`

**Subject alternative names (SAN)**

Alternative names to encode in the API server's certificate.

---

`.controlPlane.certSANs[*]`

**Type:** `string`

**SAN**

---

`.controlPlane.customNodeLabels`

**Type:** `array`

**Node labels**

---

`.controlPlane.customNodeLabels[*]`

**Type:** `string`

**Custom node label**

**Example:** `"key=value"`

**Value pattern:** `^[A-Za-z0-9-_\./]{1,63}=[A-Za-z0-9-_\.]{0,63}$`

---

`.controlPlane.diskSizeGB`

**Type:** `integer`

**Disk size**

**Example:** `30`

---

`.controlPlane.dns`

**Type:** `object`

**DNS container image**

---

`.controlPlane.dns.imageRepository`

**Type:** `string`

**Repository**

**Example:** `"projects.registry.vmware.com/tkg"`

**Default:** `"projects.registry.vmware.com/tkg"`

---

`.controlPlane.dns.imageTag`

**Type:** `string`

**Tag**

**Example:** `"v1.7.0_vmware.12"`

**Default:** `"v1.7.0_vmware.12"`

---

`.controlPlane.etcd`

**Type:** `object`

**Etcd container image**

---

`.controlPlane.etcd.imageRepository`

**Type:** `string`

**Repository**

**Example:** `"giantswarm"`

**Default:** `"giantswarm"`

---

`.controlPlane.etcd.imageTag`

**Type:** `string`

**Tag**

**Example:** `"3.5.4-0-k8s"`

**Default:** `"3.5.4-0-k8s"`

---

`.controlPlane.image`

**Type:** `object`

**Node container image**

---

`.controlPlane.image.repository`

**Type:** `string`

**Repository**

**Example:** `"projects.registry.vmware.com/tkg"`

**Default:** `"projects.registry.vmware.com/tkg"`

---

`.controlPlane.oidc`

**Type:** `object`

**OIDC authentication**

---

`.controlPlane.oidc.caFile`

**Type:** `string`

**Certificate authority file**

Path to identity provider's CA certificate in PEM format.

---

`.controlPlane.oidc.clientId`

**Type:** `string`

**Client ID**

OIDC client identifier to identify with.

---

`.controlPlane.oidc.groupsClaim`

**Type:** `string`

**Groups claim**

Name of the identity token claim bearing the user's group memberships.

---

`.controlPlane.oidc.groupsPrefix`

**Type:** `string`

**Groups prefix**

Prefix prepended to groups values to prevent clashes with existing names.

---

`.controlPlane.oidc.issuerUrl`

**Type:** `string`

**Issuer URL**

URL of the provider which allows the API server to discover public signing keys, not including any path. Discovery URL without the '/.well-known/openid-configuration' part.

---

`.controlPlane.oidc.usernameClaim`

**Type:** `string`

**Username claim**

Name of the identity token claim bearing the unique user identifier.

---

`.controlPlane.oidc.usernamePrefix`

**Type:** `string`

**Username prefix**

Prefix prepended to username values to prevent clashes with existing names.

---

`.controlPlane.placementPolicy`

**Type:** `string`

**VM placement policy**

Name of the VCD VM placement policy to use.

---

`.controlPlane.replicas`

**Type:** `integer`

**Number of nodes**

Number of control plane instances to create. Must be an odd number.

**Default:** `1`

---

`.controlPlane.resourceRatio`

**Type:** `integer`

**Resource ratio**

Ratio between node resources and apiserver resource requests.

**Default:** `8`

---

`.controlPlane.sizingPolicy`

**Type:** `string`

**Sizing policy**

Name of the VCD sizing policy to use.

**Example:** `"m1.medium"`

---

`.controlPlane.storageProfile`

**Type:** `string`

**Storage profile**

Name of the VCD storage profile to use.

---

`.controlPlane.template`

**Type:** `string`

**Template**

Name of the template used to create the node VMs.

**Example:** `"ubuntu-2004-kube-v1.22.5"`

### Kubectl image {#kubectl-image}Used by cluster-shared library chart to configure coredns in-cluster.

---

`.kubectlImage.name`

**Type:** `string`

**Repository**

**Default:** `"giantswarm/kubectl"`

---

`.kubectlImage.registry`

**Type:** `string`

**Registry**

**Default:** `"quay.io"`

---

`.kubectlImage.tag`

**Type:** `string`

**Tag**

**Default:** `"1.23.5"`

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

`.metadata.organization`

**Type:** `string`

**Organization**

---

`.metadata.preventDeletion`

**Type:** `boolean`

**Prevent cluster deletion**

**Default:** `false`

---

`.metadata.servicePriority`

**Type:** `string`

**Service priority**

The relative importance of this cluster.

**Allowed values:** `highest`, `medium`, `lowest`

**Default:** `"highest"`

### Node pools {#node-pools}Groups of worker nodes with identical configuration.

---

`.nodePools.PATTERN`

**Type:** `object`

**Key pattern:** `PATTERN`=`^[a-z0-9-]{3,10}$`

---

`.nodePools.PATTERN.class`

**Type:** `string`

**Node class**

A valid node class name, as specified in VMware Cloud Director (VCD) settings > Node classes.

**Key pattern:** `PATTERN`=`^[a-z0-9-]{3,10}$`

**Value pattern:** `^[a-z0-9-]+$`

---

`.nodePools.PATTERN.replicas`

**Type:** `integer`

**Number of nodes**

**Key pattern:** `PATTERN`=`^[a-z0-9-]{3,10}$`

**Default:** `1`

### VMware Cloud Director (VCD) settings {#vmware-cloud-director-(vcd)-settings}

---

`.providerSpecific.cloudProviderInterface`

**Type:** `object`

**Cloud provider interface (CPI)**

---

`.providerSpecific.cloudProviderInterface.enableVirtualServiceSharedIP`

**Type:** `boolean`

**Share IPs in virtual services**

If enabled, multiple virtual services can share the same virtual IP address.

**Default:** `true`

---

`.providerSpecific.cloudProviderInterface.oneArm`

**Type:** `object`

**One-arm**

If enabled, use an internal IP for the virtual service with a NAT rule to expose the external IP. Otherwise the virtual service will be exposed directly with the external IP.

---

`.providerSpecific.cloudProviderInterface.oneArm.enabled`

**Type:** `boolean`

**Enable**

**Default:** `false`

---

`.providerSpecific.containerStorageInterface`

**Type:** `object`

**Container storage interface (CSI)**

---

`.providerSpecific.containerStorageInterface.storageClass`

**Type:** `object`

**Pre-create storage class**

Pre-create storage class for the VCD CSI.

---

`.providerSpecific.containerStorageInterface.storageClass.delete`

**Type:** `object`

**Pre-create delete storage class**

---

`.providerSpecific.containerStorageInterface.storageClass.delete.isDefault`

**Type:** `boolean`

**Default storage class**

**Default:** `true`

---

`.providerSpecific.containerStorageInterface.storageClass.delete.vcdStorageProfileName`

**Type:** `string`

**Name of storage profile in VCD**

**Default:** `""`

---

`.providerSpecific.containerStorageInterface.storageClass.enabled`

**Type:** `boolean`

**Enable**

**Default:** `true`

---

`.providerSpecific.containerStorageInterface.storageClass.retain`

**Type:** `object`

**Pre-create retain storage class**

---

`.providerSpecific.containerStorageInterface.storageClass.retain.isDefault`

**Type:** `boolean`

**Default storage class**

**Default:** `false`

---

`.providerSpecific.containerStorageInterface.storageClass.retain.vcdStorageProfileName`

**Type:** `string`

**Name of storage profile in VCD**

**Default:** `""`

---

`.providerSpecific.nodeClasses`

**Type:** `object`

**Node classes**

Re-usable node configuration.

---

`.providerSpecific.nodeClasses.PATTERN`

**Type:** `object`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.catalog`

**Type:** `string`

**Catalog**

Name of the VCD catalog in which the VM template is stored.

**Example:** `"giantswarm"`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeLabels`

**Type:** `array`

**Node labels**

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeLabels[*]`

**Type:** `string`

**Custom node label**

**Example:** `"key=value"`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

**Value pattern:** `^[A-Za-z0-9-_\./]{1,63}=[A-Za-z0-9-_\.]{0,63}$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeTaints`

**Type:** `array`

**Node taints**

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*]`

**Type:** `object`

**Custom node taint**

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].effect`

**Type:** `string`

One of NoSchedule, PreferNoSchedule or NoExecute

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].key`

**Type:** `string`

Name of the label on a node

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.customNodeTaints[*].value`

**Type:** `string`

value of the label identified by the key

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.diskSizeGB`

**Type:** `integer`

**Disk size**

**Example:** `30`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.placementPolicy`

**Type:** `string`

**VM placement policy**

Name of the VCD VM placement policy to use.

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.sizingPolicy`

**Type:** `string`

**Sizing policy**

Name of the VCD sizing policy to use.

**Example:** `"m1.medium"`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.storageProfile`

**Type:** `string`

**Storage profile**

Name of the VCD storage profile to use.

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.nodeClasses.PATTERN.template`

**Type:** `string`

**Template**

Name of the template used to create the node VMs.

**Example:** `"ubuntu-2004-kube-v1.22.5"`

**Key pattern:** `PATTERN`=`^[a-z0-9-]+$`

---

`.providerSpecific.org`

**Type:** `string`

**Organization**

VCD organization name.

---

`.providerSpecific.ovdc`

**Type:** `string`

**OvDC name**

Name of the organization virtual datacenter (OvDC) to create this cluster in.

---

`.providerSpecific.ovdcNetwork`

**Type:** `string`

**OvDC network**

VCD network to connect VMs.

---

`.providerSpecific.site`

**Type:** `string`

**Endpoint**

VCD endpoint URL in the format https://VCD_HOST, without trailing slash.

---

`.providerSpecific.userContext`

**Type:** `object`

**VCD API access token**

---

`.providerSpecific.userContext.secretRef`

**Type:** `object`

**Secret reference**

---

`.providerSpecific.userContext.secretRef.secretName`

**Type:** `string`

**Name**

Name of the secret containing the VCD API token.

---

`.providerSpecific.vmNamingTemplate`

**Type:** `string`

**VM naming template**

Go template to specify the VM naming convention.

**Example:** `"mytenant-{{ .machine.Name | sha256sum | trunc 7 }}"`

### Other {#other}

---

`.baseDomain`

**Type:** `string`

**Base DNS domain**

**Default:** `"k8s.test"`

---

`.cluster-shared`

**Type:** `object`

**Library chart**

---

`.managementCluster`

**Type:** `string`

**Management cluster name**

The Cluster API management cluster that manages this cluster.

---

`.provider`

**Type:** `string`

**Cluster API provider name**

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-cloud-director)
