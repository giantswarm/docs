---
title: cluster chart reference
linkTitle: cluster
description:  Giant Swarm cluster chart with provider-independent cluster resources; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster?
owner:
- https://github.com/orgs/giantswarm/teams/team-turtles
source_repository: https://github.com/giantswarm/cluster
source_repository_ref: v0.7.0
---

The `cluster` chart is the main entry point for the Giant Swarm platform. It is the first app that is installed on a new cluster. It is responsible for setting up the basic infrastructure and installing the necessary components to make the cluster operational.

## Chart configuration reference

### Components {#components}Advanced configuration of components that are running on all nodes.

---

`.global.components.containerd`

**Type:** `object`

**Containerd**

Configuration of containerd.

---

`.global.components.containerd.containerRegistries`

**Type:** `object`

**Container registries**

Endpoints and credentials configuration for container registries.

**Default:** `{"docker.io":[{"endpoint":"registry-1.docker.io"},{"endpoint":"giantswarm.azurecr.io"}]}`

---

`.global.components.containerd.containerRegistries.*`

**Type:** `array`

**Registries**

Container registries and mirrors

---

`.global.components.containerd.containerRegistries.*[*]`

**Type:** `object`

**Registry**

---

`.global.components.containerd.containerRegistries.*[*].credentials`

**Type:** `object`

**Credentials**

---

`.global.components.containerd.containerRegistries.*[*].credentials.auth`

**Type:** `string`

**Auth**

Base64-encoded string from the concatenation of the username, a colon, and the password.

---

`.global.components.containerd.containerRegistries.*[*].credentials.identitytoken`

**Type:** `string`

**Identity token**

Used to authenticate the user and obtain an access token for the registry.

---

`.global.components.containerd.containerRegistries.*[*].credentials.password`

**Type:** `string`

**Password**

Used to authenticate for the registry with username/password.

---

`.global.components.containerd.containerRegistries.*[*].credentials.username`

**Type:** `string`

**Username**

Used to authenticate for the registry with username/password.

---

`.global.components.containerd.containerRegistries.*[*].endpoint`

**Type:** `string`

**Endpoint**

Endpoint for the container registry.

### Connectivity {#connectivity}Configuration of connectivity and networking options.

---

`.global.connectivity.baseDomain`

**Type:** `string`

**Base DNS domain**

---

`.global.connectivity.bastion`

**Type:** `object`

**Bastion host**

---

`.global.connectivity.bastion.enabled`

**Type:** `boolean`

**Enable**

**Default:** `true`

---

`.global.connectivity.bastion.replicas`

**Type:** `integer`

**Number of hosts**

**Default:** `1`

---

`.global.connectivity.network`

**Type:** `object`

**Network**

---

`.global.connectivity.network.pods`

**Type:** `object`

**Pods**

---

`.global.connectivity.network.pods.cidrBlocks`

**Type:** `array`

**Pod subnets**

**Default:** `["100.64.0.0/12"]`

---

`.global.connectivity.network.pods.cidrBlocks[*]`

**Type:** `string`

**Pod subnet**

IPv4 address range for pods, in CIDR notation.

**Example:** `"10.244.0.0/16"`

---

`.global.connectivity.network.services`

**Type:** `object`

**Services**

---

`.global.connectivity.network.services.cidrBlocks`

**Type:** `array`

**Kubernetes Service subnets**

**Default:** `["172.31.0.0/16"]`

---

`.global.connectivity.network.services.cidrBlocks[*]`

**Type:** `string`

**Service subnet**

IPv4 address range for kubernetes services, in CIDR notation.

**Example:** `"172.31.0.0/16"`

---

`.global.connectivity.proxy`

**Type:** `object`

**Proxy**

Whether/how outgoing traffic is routed through proxy servers.

**Default:** `{"enabled":false}`

---

`.global.connectivity.proxy.enabled`

**Type:** `boolean`

**Enable**

---

`.global.connectivity.proxy.httpProxy`

**Type:** `string`

**HTTP proxy**

To be passed to the HTTP_PROXY environment variable in all hosts.

---

`.global.connectivity.proxy.httpsProxy`

**Type:** `string`

**HTTPS proxy**

To be passed to the HTTPS_PROXY environment variable in all hosts.

---

`.global.connectivity.proxy.noProxy`

**Type:** `string`

**No proxy**

Comma-separated addresses to be passed to the NO_PROXY environment variable in all hosts.

### Control plane {#control-plane}Configuration of the control plane.

---

`.global.controlPlane.apiServerPort`

**Type:** `integer`

**API server port**

The API server Load Balancer port. This option sets the Spec.ClusterNetwork.APIServerPort field on the Cluster CR. In CAPI this field isn't used currently. It is instead used in providers. In CAPA this sets only the public facing port of the Load Balancer. In CAPZ both the public facing and the destination port are set to this value. CAPV and CAPVCD do not use it.

**Default:** `6443`

---

`.global.controlPlane.customNodeTaints`

**Type:** `array`

**Custom node taints**

---

`.global.controlPlane.customNodeTaints[*]`

**Type:** `object`

---

`.global.controlPlane.customNodeTaints[*].effect`

**Type:** `string`

**Effect**

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.global.controlPlane.customNodeTaints[*].key`

**Type:** `string`

**Key**

---

`.global.controlPlane.customNodeTaints[*].value`

**Type:** `string`

**Value**

---

`.global.controlPlane.machineHealthCheck`

**Type:** `object`

**Machine health check**

---

`.global.controlPlane.machineHealthCheck.enabled`

**Type:** `boolean`

**Enable**

**Default:** `true`

---

`.global.controlPlane.machineHealthCheck.maxUnhealthy`

**Type:** `string`

**Maximum unhealthy nodes**

**Example:** `"40%"`

**Default:** `"40%"`

---

`.global.controlPlane.machineHealthCheck.nodeStartupTimeout`

**Type:** `string`

**Node startup timeout**

Determines how long a machine health check should wait for a node to join the cluster, before considering a machine unhealthy.

**Examples:** `"10m"`, `"100s"`

**Default:** `"8m0s"`

---

`.global.controlPlane.machineHealthCheck.unhealthyNotReadyTimeout`

**Type:** `string`

**Timeout for ready**

If a node is not in condition 'Ready' after this timeout, it will be considered unhealthy.

**Example:** `"300s"`

**Default:** `"10m0s"`

---

`.global.controlPlane.machineHealthCheck.unhealthyUnknownTimeout`

**Type:** `string`

**Timeout for unknown condition**

If a node is in 'Unknown' condition after this timeout, it will be considered unhealthy.

**Example:** `"300s"`

**Default:** `"10m0s"`

---

`.global.controlPlane.oidc`

**Type:** `object`

**OIDC authentication**

---

`.global.controlPlane.oidc.caPem`

**Type:** `string`

**Certificate authority**

Identity provider's CA certificate in PEM format.

---

`.global.controlPlane.oidc.clientId`

**Type:** `string`

**Client ID**

---

`.global.controlPlane.oidc.groupsClaim`

**Type:** `string`

**Groups claim**

---

`.global.controlPlane.oidc.issuerUrl`

**Type:** `string`

**Issuer URL**

Exact issuer URL that will be included in identity tokens.

---

`.global.controlPlane.oidc.usernameClaim`

**Type:** `string`

**Username claim**

---

`.global.controlPlane.replicas`

**Type:** `integer`

**Replicas**

The number of control plane nodes.

**Allowed values:** `1`, `3`, `5`

**Default:** `3`

### Internal {#internal}For Giant Swarm internal use only, not stable, or not supported by UIs.

---

`.internal.advancedConfiguration`

**Type:** `object`

**Advanced configuration**

Advanced configuration of cluster components, to be configured by Giant Swarm staff only.

---

`.internal.advancedConfiguration.cgroupsv1`

**Type:** `boolean`

**CGroups v1**

Force use of CGroups v1 for whole cluster.

**Default:** `false`

---

`.internal.advancedConfiguration.controlPlane`

**Type:** `object`

**Control plane**

Advanced configuration of control plane components.

---

`.internal.advancedConfiguration.controlPlane.apiServer`

**Type:** `object`

**API server**

Advanced configuration of API server.

---

`.internal.advancedConfiguration.controlPlane.apiServer.bindPort`

**Type:** `integer`

**Bind port**

Kubernetes API bind port used for API server pod.

---

`.internal.advancedConfiguration.controlPlane.apiServer.etcdPrefix`

**Type:** `string`

**etcd prefix**

The prefix to prepend to all resource paths in etcd. If nothing is specified, the API server uses '/registry' prefix by default.

---

`.internal.advancedConfiguration.controlPlane.apiServer.extraArgs`

**Type:** `object`

**Extra CLI args**

A map with the additional CLI flags that are appended to the default flags. Use with caution, as there is no validation for these values, so you can set incorrect or duplicate flags.

---

`.internal.advancedConfiguration.controlPlane.apiServer.extraCertificateSANs`

**Type:** `array`

**Extra certificate SANs**

The additional certificate SANs that are appended to the default SANs. Use with caution, as there is no validation for these values, so you can set incorrect or duplicate certificates.

---

`.internal.advancedConfiguration.controlPlane.apiServer.extraCertificateSANs[*]`

**Type:** `string`

**Extra certificate SAN**

---

`.internal.advancedConfiguration.controlPlane.etcd`

**Type:** `object`

**etcd**

Configuration of etcd

---

`.internal.advancedConfiguration.controlPlane.etcd.experimental`

**Type:** `object`

**Experimental**

---

`.internal.advancedConfiguration.controlPlane.etcd.experimental.peerSkipClientSanVerification`

**Type:** `boolean`

**Peer skip client SAN verification**

Skip verification of SAN field in client certificate for peer connections.

---

`.internal.advancedConfiguration.controlPlane.etcd.extraArgs`

**Type:** `object`

**Extra args**

---

`.internal.advancedConfiguration.controlPlane.etcd.initialCluster`

**Type:** `string`

**Initial cluster**

Initial cluster configuration for bootstrapping.

---

`.internal.advancedConfiguration.controlPlane.etcd.initialClusterState`

**Type:** `string`

**Initial cluster state**

**Allowed values:** `new`, `existing`

---

`.internal.advancedConfiguration.controlPlane.etcd.quotaBackendBytesGiB`

**Type:** `integer`

**Quota backend bytes in GiB**

Raise the etcd default backend bytes limit up to 16GiB.

**Default:** `8`

---

`.internal.advancedConfiguration.controlPlane.files`

**Type:** `array`

**Files**

Custom cluster-specific files that are deployed to control plane nodes.

---

`.internal.advancedConfiguration.controlPlane.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.internal.advancedConfiguration.controlPlane.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.internal.advancedConfiguration.controlPlane.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.internal.advancedConfiguration.controlPlane.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.internal.advancedConfiguration.controlPlane.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.internal.advancedConfiguration.controlPlane.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.internal.advancedConfiguration.controlPlane.postKubeadmCommands[*]`

**Type:** `string`

---

`.internal.advancedConfiguration.controlPlane.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.internal.advancedConfiguration.controlPlane.preKubeadmCommands[*]`

**Type:** `string`

---

`.internal.advancedConfiguration.files`

**Type:** `array`

**Files**

Custom cluster-specific files that are deployed to all nodes.

---

`.internal.advancedConfiguration.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.internal.advancedConfiguration.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.internal.advancedConfiguration.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.internal.advancedConfiguration.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.internal.advancedConfiguration.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.internal.advancedConfiguration.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.internal.advancedConfiguration.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.internal.advancedConfiguration.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.internal.advancedConfiguration.postKubeadmCommands[*]`

**Type:** `string`

---

`.internal.advancedConfiguration.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.internal.advancedConfiguration.preKubeadmCommands[*]`

**Type:** `string`

---

`.internal.advancedConfiguration.workers`

**Type:** `object`

**Workers**

Advanced configuration of worker nodes.

---

`.internal.advancedConfiguration.workers.files`

**Type:** `array`

**Files**

Custom cluster-specific files that are deployed to worker nodes.

---

`.internal.advancedConfiguration.workers.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.internal.advancedConfiguration.workers.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.internal.advancedConfiguration.workers.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.internal.advancedConfiguration.workers.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.internal.advancedConfiguration.workers.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.internal.advancedConfiguration.workers.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.internal.advancedConfiguration.workers.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.internal.advancedConfiguration.workers.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.internal.advancedConfiguration.workers.postKubeadmCommands[*]`

**Type:** `string`

---

`.internal.advancedConfiguration.workers.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.internal.advancedConfiguration.workers.preKubeadmCommands[*]`

**Type:** `string`

### Metadata {#metadata}

---

`.global.metadata.annotations`

**Type:** `object`

**Annotations**

These annotations are added to all Kubernetes resources defining this cluster.

---

`.global.metadata.annotations.PATTERN`

**Type:** `string`

**Annotation**

**Key pattern:** `PATTERN`=`^([a-zA-Z0-9\.-]{1,253}/)?[a-zA-Z0-9\._-]{1,63}$`

---

`.global.metadata.description`

**Type:** `string`

**Cluster description**

User-friendly description of the cluster's purpose.

---

`.global.metadata.labels`

**Type:** `object`

**Labels**

These labels are added to all Kubernetes resources defining this cluster.

---

`.global.metadata.labels.PATTERN`

**Type:** `string`

**Label**

**Key pattern:** `PATTERN`=`^[a-zA-Z0-9/\._-]+$`

**Value pattern:** `^[a-zA-Z0-9\._-]+$`

---

`.global.metadata.name`

**Type:** `string`

**Cluster name**

Unique identifier, cannot be changed after creation.

---

`.global.metadata.organization`

**Type:** `string`

**Organization**

The name of organization that owns the cluster.

---

`.global.metadata.preventDeletion`

**Type:** `boolean`

**Prevent cluster deletion**

Setting this to true will set giantswarm.io/prevent-deletion label to true, which will block cluster deletion.

**Default:** `false`

---

`.global.metadata.servicePriority`

**Type:** `string`

**Service priority**

The relative importance of this cluster.

**Allowed values:** `highest`, `medium`, `lowest`

**Default:** `"highest"`

### Node pools {#node-pools}

---

`.global.nodePools.PATTERN`

**Type:** `object`

**Node pool**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.annotations`

**Type:** `object`

**Annotations**

These annotations are added to all Kubernetes resources defining this node pool.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.annotations.PATTERN_2`

**Type:** `string`

**Annotation**

**Key patterns:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`, `PATTERN_2`=`^([a-zA-Z0-9\.-]{1,253}/)?[a-zA-Z0-9\._-]{1,63}$`

---

`.global.nodePools.PATTERN.labels`

**Type:** `object`

**Labels**

These labels are added to all Kubernetes resources defining this node pool.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.labels.PATTERN_2`

**Type:** `string`

**Label**

**Key patterns:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`, `PATTERN_2`=`^[a-zA-Z0-9/\._-]+$`

**Value pattern:** `^[a-zA-Z0-9\._-]+$`

---

`.global.nodePools.PATTERN.nodeLabels`

**Type:** `object`

**Node labels**

Labels that are passed to kubelet argument 'node-labels'.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.nodeLabels.*`

**Type:** `string`

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.nodeTaints`

**Type:** `array`

**Custom node taints**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.nodeTaints[*]`

**Type:** `object`

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.nodeTaints[*].effect`

**Type:** `string`

**Effect**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.global.nodePools.PATTERN.nodeTaints[*].key`

**Type:** `string`

**Key**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.nodeTaints[*].value`

**Type:** `string`

**Value**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.replicas`

**Type:** `integer`

**Replicas**

The number of node pool nodes.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

### Other global {#other-global}

---

`.global.managementCluster`

**Type:** `string`

**Management cluster**

Name of the Cluster API cluster managing this workload cluster.

### Pod Security Standards {#pod-security-standards}

---

`.global.podSecurityStandards.enforced`

**Type:** `boolean`

**Enforced**

**Default:** `false`

### Provider integration {#provider-integration}Provider-specific properties that can be set by cluster-$provider chart in order to render correct templates for the provider.

---

`.providerIntegration.bastion`

**Type:** `object`

**Internal bastion configuration**

---

`.providerIntegration.bastion.kubeadmConfig`

**Type:** `object`

**Kubeadm config**

Configuration of bastion nodes.

---

`.providerIntegration.bastion.kubeadmConfig.ignition`

**Type:** `object`

**Ignition**

Ignition-specific configuration.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig`

**Type:** `object`

**Container Linux configuration**

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig`

**Type:** `object`

**Additional config**

Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage`

**Type:** `object`

**Storage**

It describes the desired state of the system’s storage devices.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories`

**Type:** `array`

**Directories**

The list of directories to be created.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]`

**Type:** `object`

**Directory**

The directory to be created.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem`

**Type:** `string`

**Filesystem**

The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group`

**Type:** `object`

**Group**

It specifies the group of the owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id`

**Type:** `integer`

**ID**

The group ID of the owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name`

**Type:** `string`

**Name**

The group name of the owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode`

**Type:** `integer`

**Mode**

The directory’s permission mode.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite`

**Type:** `boolean`

**Overwrite**

Whether to delete preexisting nodes at the path.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path`

**Type:** `string`

**Path**

The absolute path to the directory.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user`

**Type:** `object`

**User**

It specifies the directory’s owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id`

**Type:** `integer`

**ID**

The user ID of the owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name`

**Type:** `string`

**Name**

The user name of the owner.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems`

**Type:** `array`

**File systems**

The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]`

**Type:** `object`

**File system**

The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount`

**Type:** `object`

**Mount**

It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device`

**Type:** `string`

**Device**

The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format`

**Type:** `string`

**Format**

The filesystem format (ext4, btrfs, or xfs).

**Allowed values:** `ext4`, `btrfs`, `xfs`

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label`

**Type:** `string`

**Label**

The label of the filesystem.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options`

**Type:** `array`

**Options**

Any additional options to be passed to the format-specific mkfs utility.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]`

**Type:** `string`

An additional option to be passed to the format-specific mkfs utility.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid`

**Type:** `string`

**UUID**

The uuid of the filesystem.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem`

**Type:** `boolean`

**Wipe filesystem**

Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name`

**Type:** `string`

**Name**

The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path`

**Type:** `string`

**Path**

The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd`

**Type:** `object`

**systemd**

It describes the desired state of the systemd units.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units`

**Type:** `array`

**Units**

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]`

**Type:** `object`

**systemd unit**

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents`

**Type:** `object`

**Contents**

The contents of the unit.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install`

**Type:** `object`

**Install**

Configuration of the [Install] section.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy`

**Type:** `array`

**WantedBy**

Units with (weak) requirement dependencies on this unit.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]`

**Type:** `string`

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount`

**Type:** `object`

**Mount**

Configuration of the [Mount] section.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type`

**Type:** `string`

**Type**

A file system type to mount.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what`

**Type:** `string`

**What**

An absolute path of a device node, file or other resource to mount.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where`

**Type:** `string`

**Where**

An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit`

**Type:** `object`

**Unit**

Configuration of the [Unit] section.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies`

**Type:** `boolean`

**DefaultDependencies**

Flag that indicates if this systemd unit should have the default systemd unit dependencies.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description`

**Type:** `string`

**Description**

systemd unit description.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins`

**Type:** `array`

**Unit drop-ins**

The list of drop-ins for the unit

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]`

**Type:** `object`

**Unit drop-in**

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents`

**Type:** `string`

**Contents**

The contents of the drop-in.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name`

**Type:** `string`

**Name**

The name of the drop-in. This must be suffixed with “.conf”

**Value pattern:** `^.+\.conf$`

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled`

**Type:** `boolean`

**Enabled?**

Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask`

**Type:** `boolean`

**Masked?**

Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name`

**Type:** `string`

**Name**

The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).

---

`.providerIntegration.bastion.kubeadmConfig.ignition.containerLinuxConfig.strict`

**Type:** `boolean`

**Strict**

It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.

---

`.providerIntegration.bastion.kubeadmConfig.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.providerIntegration.bastion.kubeadmConfig.preKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.clusterAnnotationsTemplateName`

**Type:** `string`

**Cluster annotations template name**

The name of the template that renders provider-specific annotations for the Cluster resource

---

`.providerIntegration.components`

**Type:** `object`

**Components**

Internal configuration of various components that form the Kubernetes cluster.

---

`.providerIntegration.components.containerd`

**Type:** `object`

**Containerd**

Configuration of containerd.

---

`.providerIntegration.components.containerd.sandboxContainerImage`

**Type:** `object`

**Sandbox image**

The image used by sandbox / pause container

---

`.providerIntegration.components.containerd.sandboxContainerImage.name`

**Type:** `string`

**Repository**

**Default:** `"giantswarm/pause"`

---

`.providerIntegration.components.containerd.sandboxContainerImage.registry`

**Type:** `string`

**Registry**

**Default:** `"gsoci.azurecr.io"`

---

`.providerIntegration.components.containerd.sandboxContainerImage.tag`

**Type:** `string`

**Tag**

**Default:** `"3.9"`

---

`.providerIntegration.components.systemd`

**systemd**

**Default:** `null`

---

`.providerIntegration.components.systemd[option#1]`

**Type:** `null`

---

`.providerIntegration.components.systemd[option#2]`

**Type:** `object`

---

`.providerIntegration.components.systemd[option#2].timesyncd`

**Type:** `object`

**timesyncd**

systemd-timesyncd is a system service that may be used to synchronize the local system clock with a remote Network Time Protocol (NTP) server.

---

`.providerIntegration.components.systemd[option#2].timesyncd.ntp`

**Type:** `array`

**NTP**

A list of NTP server host names or IP addresses.

---

`.providerIntegration.components.systemd[option#2].timesyncd.ntp[*]`

**Type:** `string`

---

`.providerIntegration.connectivity`

**Type:** `object`

**Connectivity**

Internal connectivity configuration.

---

`.providerIntegration.connectivity.proxy`

**Type:** `object`

**Proxy**

Whether/how outgoing traffic is routed through proxy servers.

---

`.providerIntegration.connectivity.proxy.noProxy`

**Type:** `object`

**No proxy**

To be passed to the NO_PROXY environment variable in all hosts.

---

`.providerIntegration.connectivity.proxy.noProxy.templateName`

**Type:** `string`

**Template name**

Name of Helm template that renders a YAML array with NO_PROXY addresses.

---

`.providerIntegration.connectivity.proxy.noProxy.value`

**Type:** `array`

**Value**

Pre-defined static NO_PROXY values.

---

`.providerIntegration.connectivity.proxy.noProxy.value[*]`

**Type:** `string`

---

`.providerIntegration.connectivity.sshSsoPublicKey`

**Type:** `string`

**SSH public key for single sign-on**

**Default:** `"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIM4cvZ01fLmO9cJbWUj7sfF+NhECgy+Cl0bazSrZX7sU vault-ca@vault.operations.giantswarm.io"`

---

`.providerIntegration.controlPlane`

**Type:** `object`

**Provider-specific control plane configuration**

---

`.providerIntegration.controlPlane.kubeadmConfig`

**Type:** `object`

**Kubeadm config**

Configuration of control plane nodes.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration`

**Type:** `object`

**Cluster configuration**

Configuration of Kubernetes components.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer`

**Type:** `object`

**API server**

Configuration of API server.

**Default:** `{}`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.additionalAdmissionPlugins`

**Type:** `array`

**Additional admission plugins**

A list of plugins to enable, in addition to the default ones that include DefaultStorageClass, DefaultTolerationSeconds, LimitRanger, MutatingAdmissionWebhook, NamespaceLifecycle, PersistentVolumeClaimResize, Priority, ResourceQuota, ServiceAccount and ValidatingAdmissionWebhook.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.additionalAdmissionPlugins[*]`

**Type:** `string`

**Additional admission plugin**

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences`

**API audiences**

Identifiers of the API. The service account token authenticator will validate that tokens used against the API are bound to at least one of these audiences. If the --service-account-issuer flag is configured and this flag is not, 'api-audiences' field defaults to a single element list containing the issuer URL.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#1]`

**Type:** `null`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#2]`

**Type:** `object`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#2].templateName`

**Type:** `string`

**Template name**

The name of the Helm template which renders the 'api-audiences' value

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#2].value`

**Type:** `string`

**Value**

Static value for api-audiences.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#2][option#1]`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.apiAudiences[option#2][option#2]`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates`

**Type:** `array`

**Feature gates**

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*]`

**Type:** `object`

**Feature gate**

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*].enabled`

**Type:** `boolean`

**Enabled**

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.featureGates[*].name`

**Type:** `string`

**Name**

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer`

**Service account issuer**

Configuration of the identifier of the service account token issuer. You must specify either URL or clusterDomainPrefix (only one, not both).

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#1]`

**Type:** `null`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#2]`

**Type:** `object`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#2].clusterDomainPrefix`

**Type:** `string`

**Cluster domain prefix**

Prefix that is prepended to the cluster domain name, so that resulting URL is used as the identifier of the service account token issuer.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#2].url`

**Type:** `string`

**URL**

This URL is used as the identifier of the service account token issuer.

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#2][option#1]`

---

`.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuer[option#2][option#2]`

---

`.providerIntegration.controlPlane.kubeadmConfig.files`

**Type:** `array`

**Files**

Provider-specific files that are deployed to control plane nodes. They are specified in the cluster-<provider> apps.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.providerIntegration.controlPlane.kubeadmConfig.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition`

**Type:** `object`

**Ignition**

Ignition-specific configuration.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig`

**Type:** `object`

**Container Linux configuration**

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig`

**Type:** `object`

**Additional config**

Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage`

**Type:** `object`

**Storage**

It describes the desired state of the system’s storage devices.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories`

**Type:** `array`

**Directories**

The list of directories to be created.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]`

**Type:** `object`

**Directory**

The directory to be created.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem`

**Type:** `string`

**Filesystem**

The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group`

**Type:** `object`

**Group**

It specifies the group of the owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id`

**Type:** `integer`

**ID**

The group ID of the owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name`

**Type:** `string`

**Name**

The group name of the owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode`

**Type:** `integer`

**Mode**

The directory’s permission mode.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite`

**Type:** `boolean`

**Overwrite**

Whether to delete preexisting nodes at the path.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path`

**Type:** `string`

**Path**

The absolute path to the directory.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user`

**Type:** `object`

**User**

It specifies the directory’s owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id`

**Type:** `integer`

**ID**

The user ID of the owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name`

**Type:** `string`

**Name**

The user name of the owner.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems`

**Type:** `array`

**File systems**

The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]`

**Type:** `object`

**File system**

The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount`

**Type:** `object`

**Mount**

It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device`

**Type:** `string`

**Device**

The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format`

**Type:** `string`

**Format**

The filesystem format (ext4, btrfs, or xfs).

**Allowed values:** `ext4`, `btrfs`, `xfs`

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label`

**Type:** `string`

**Label**

The label of the filesystem.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options`

**Type:** `array`

**Options**

Any additional options to be passed to the format-specific mkfs utility.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]`

**Type:** `string`

An additional option to be passed to the format-specific mkfs utility.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid`

**Type:** `string`

**UUID**

The uuid of the filesystem.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem`

**Type:** `boolean`

**Wipe filesystem**

Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name`

**Type:** `string`

**Name**

The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path`

**Type:** `string`

**Path**

The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd`

**Type:** `object`

**systemd**

It describes the desired state of the systemd units.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units`

**Type:** `array`

**Units**

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]`

**Type:** `object`

**systemd unit**

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents`

**Type:** `object`

**Contents**

The contents of the unit.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install`

**Type:** `object`

**Install**

Configuration of the [Install] section.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy`

**Type:** `array`

**WantedBy**

Units with (weak) requirement dependencies on this unit.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]`

**Type:** `string`

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount`

**Type:** `object`

**Mount**

Configuration of the [Mount] section.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type`

**Type:** `string`

**Type**

A file system type to mount.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what`

**Type:** `string`

**What**

An absolute path of a device node, file or other resource to mount.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where`

**Type:** `string`

**Where**

An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit`

**Type:** `object`

**Unit**

Configuration of the [Unit] section.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies`

**Type:** `boolean`

**DefaultDependencies**

Flag that indicates if this systemd unit should have the default systemd unit dependencies.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description`

**Type:** `string`

**Description**

systemd unit description.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins`

**Type:** `array`

**Unit drop-ins**

The list of drop-ins for the unit

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]`

**Type:** `object`

**Unit drop-in**

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents`

**Type:** `string`

**Contents**

The contents of the drop-in.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name`

**Type:** `string`

**Name**

The name of the drop-in. This must be suffixed with “.conf”

**Value pattern:** `^.+\.conf$`

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled`

**Type:** `boolean`

**Enabled?**

Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask`

**Type:** `boolean`

**Masked?**

Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name`

**Type:** `string`

**Name**

The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).

---

`.providerIntegration.controlPlane.kubeadmConfig.ignition.containerLinuxConfig.strict`

**Type:** `boolean`

**Strict**

It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.

---

`.providerIntegration.controlPlane.kubeadmConfig.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.providerIntegration.controlPlane.kubeadmConfig.postKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.controlPlane.kubeadmConfig.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.providerIntegration.controlPlane.kubeadmConfig.preKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.controlPlane.resources`

**Type:** `object`

**Resources configuration**

GVK and other configuration for control plane resources.

---

`.providerIntegration.controlPlane.resources.controlPlane`

**Type:** `object`

**Control plane resource config**

**Default:** `{"api":{"group":"controlplane.cluster.x-k8s.io","kind":"KubeadmControlPlane","version":"v1beta1"}}`

---

`.providerIntegration.controlPlane.resources.controlPlane.api`

**Type:** `object`

**Schema for Kubernetes API group, version and kind**

It can be used to specify which CustomResourceDefinition is used.

---

`.providerIntegration.controlPlane.resources.controlPlane.api.group`

**Type:** `string`

**API group**

**Examples:** `"cluster.x-k8s.io"`, `"controlplane.cluster.x-k8s.io"`, `"infrastructure.cluster.x-k8s.io"`

---

`.providerIntegration.controlPlane.resources.controlPlane.api.kind`

**Type:** `string`

**API kind**

**Examples:** `"Cluster"`, `"KubeadmControlPlane"`

---

`.providerIntegration.controlPlane.resources.controlPlane.api.version`

**Type:** `string`

**API version**

**Examples:** `"v1alpha1"`, `"v1alpha2"`, `"v1beta1"`, `"v1"`

---

`.providerIntegration.controlPlane.resources.infrastructureMachineTemplate`

**Type:** `object`

**Infrastructure Machine template**

Group, version and kind of provider-specific infrastructure Machine template resource.

---

`.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.group`

**Type:** `string`

**API group**

**Example:** `"infrastructure.cluster.x-k8s.io"`

---

`.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.kind`

**Type:** `string`

**API kind**

**Examples:** `"AWSMachineTemplate"`, `"AzureMachineTemplate"`

---

`.providerIntegration.controlPlane.resources.infrastructureMachineTemplate.version`

**Type:** `string`

**API version**

**Examples:** `"v1alpha1"`, `"v1beta1"`, `"v1beta2"`, `"v1"`, `"v2"`

---

`.providerIntegration.controlPlane.resources.infrastructureMachineTemplateSpecTemplateName`

**Type:** `string`

**Infrastructure Machine template spec template name**

The name of Helm template that renders Infrastructure Machine template spec.

---

`.providerIntegration.hashSalt`

**Type:** `string`

**Hash salt**

If specified, this token is used as a salt to the hash suffix of some resource names. Can be used to force-recreate some resources.

---

`.providerIntegration.kubeadmConfig`

**Type:** `object`

**Provider-specific kubeadm config**

Provider-specific kubeadm config that is common for all nodes, including both control plane and workers.

---

`.providerIntegration.kubeadmConfig.files`

**Type:** `array`

**Files**

Provider-specific files that are deployed to all nodes. They are specified in the cluster-<provider> apps.

---

`.providerIntegration.kubeadmConfig.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.providerIntegration.kubeadmConfig.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.providerIntegration.kubeadmConfig.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.providerIntegration.kubeadmConfig.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.providerIntegration.kubeadmConfig.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.providerIntegration.kubeadmConfig.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.providerIntegration.kubeadmConfig.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.providerIntegration.kubeadmConfig.ignition`

**Type:** `object`

**Ignition**

Ignition-specific configuration.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig`

**Type:** `object`

**Container Linux configuration**

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig`

**Type:** `object`

**Additional config**

Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage`

**Type:** `object`

**Storage**

It describes the desired state of the system’s storage devices.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories`

**Type:** `array`

**Directories**

The list of directories to be created.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]`

**Type:** `object`

**Directory**

The directory to be created.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem`

**Type:** `string`

**Filesystem**

The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group`

**Type:** `object`

**Group**

It specifies the group of the owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id`

**Type:** `integer`

**ID**

The group ID of the owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name`

**Type:** `string`

**Name**

The group name of the owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode`

**Type:** `integer`

**Mode**

The directory’s permission mode.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite`

**Type:** `boolean`

**Overwrite**

Whether to delete preexisting nodes at the path.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path`

**Type:** `string`

**Path**

The absolute path to the directory.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user`

**Type:** `object`

**User**

It specifies the directory’s owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id`

**Type:** `integer`

**ID**

The user ID of the owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name`

**Type:** `string`

**Name**

The user name of the owner.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems`

**Type:** `array`

**File systems**

The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]`

**Type:** `object`

**File system**

The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount`

**Type:** `object`

**Mount**

It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device`

**Type:** `string`

**Device**

The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format`

**Type:** `string`

**Format**

The filesystem format (ext4, btrfs, or xfs).

**Allowed values:** `ext4`, `btrfs`, `xfs`

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label`

**Type:** `string`

**Label**

The label of the filesystem.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options`

**Type:** `array`

**Options**

Any additional options to be passed to the format-specific mkfs utility.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]`

**Type:** `string`

An additional option to be passed to the format-specific mkfs utility.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid`

**Type:** `string`

**UUID**

The uuid of the filesystem.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem`

**Type:** `boolean`

**Wipe filesystem**

Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name`

**Type:** `string`

**Name**

The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path`

**Type:** `string`

**Path**

The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd`

**Type:** `object`

**systemd**

It describes the desired state of the systemd units.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units`

**Type:** `array`

**Units**

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]`

**Type:** `object`

**systemd unit**

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents`

**Type:** `object`

**Contents**

The contents of the unit.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install`

**Type:** `object`

**Install**

Configuration of the [Install] section.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy`

**Type:** `array`

**WantedBy**

Units with (weak) requirement dependencies on this unit.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]`

**Type:** `string`

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount`

**Type:** `object`

**Mount**

Configuration of the [Mount] section.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type`

**Type:** `string`

**Type**

A file system type to mount.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what`

**Type:** `string`

**What**

An absolute path of a device node, file or other resource to mount.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where`

**Type:** `string`

**Where**

An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit`

**Type:** `object`

**Unit**

Configuration of the [Unit] section.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies`

**Type:** `boolean`

**DefaultDependencies**

Flag that indicates if this systemd unit should have the default systemd unit dependencies.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description`

**Type:** `string`

**Description**

systemd unit description.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins`

**Type:** `array`

**Unit drop-ins**

The list of drop-ins for the unit

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]`

**Type:** `object`

**Unit drop-in**

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents`

**Type:** `string`

**Contents**

The contents of the drop-in.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name`

**Type:** `string`

**Name**

The name of the drop-in. This must be suffixed with “.conf”

**Value pattern:** `^.+\.conf$`

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled`

**Type:** `boolean`

**Enabled?**

Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask`

**Type:** `boolean`

**Masked?**

Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name`

**Type:** `string`

**Name**

The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).

---

`.providerIntegration.kubeadmConfig.ignition.containerLinuxConfig.strict`

**Type:** `boolean`

**Strict**

It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.

---

`.providerIntegration.kubeadmConfig.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.providerIntegration.kubeadmConfig.postKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.kubeadmConfig.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.providerIntegration.kubeadmConfig.preKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.kubernetesVersion`

**Type:** `string`

**Kubernetes version**

**Default:** `"1.25.16"`

---

`.providerIntegration.pauseProperties`

**Type:** `object`

**Pause properties**

A map of property names and their values that will affect setting pause annotation

---

`.providerIntegration.pauseProperties.*`

**Types:** `boolean`, `number`, `integer`, `string`

---

`.providerIntegration.provider`

**Type:** `string`

**Provider**

The name of the Cluster API provider. The name here must match the name of the provider in cluster-<provider> app name.

---

`.providerIntegration.resourcesApi.bastionResourceEnabled`

**Type:** `boolean`

**Bastion resource enabled**

Flag that indicates if the Bastion resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.

**Default:** `true`

---

`.providerIntegration.resourcesApi.clusterResourceEnabled`

**Type:** `boolean`

**Cluster resource enabled**

Flag that indicates if the Cluster resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.

**Default:** `true`

---

`.providerIntegration.resourcesApi.controlPlaneResourceEnabled`

**Type:** `boolean`

**Control plane resource enabled**

Flag that indicates if the control plane resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.

**Default:** `true`

---

`.providerIntegration.resourcesApi.infrastructureCluster`

**Type:** `object`

**Infrastructure cluster**

Group, version and kind of provider-specific infrastructure cluster resource.

---

`.providerIntegration.resourcesApi.infrastructureCluster.group`

**Type:** `string`

**API group**

**Example:** `"infrastructure.cluster.x-k8s.io"`

---

`.providerIntegration.resourcesApi.infrastructureCluster.kind`

**Type:** `string`

**API kind**

**Examples:** `"AWSCluster"`, `"AzureCluster"`, `"VCDCluster"`, `"VSphereCluster"`

---

`.providerIntegration.resourcesApi.infrastructureCluster.version`

**Type:** `string`

**API version**

**Examples:** `"v1alpha1"`, `"v1beta1"`, `"v1beta2"`, `"v1"`, `"v2"`

---

`.providerIntegration.resourcesApi.machineHealthCheckResourceEnabled`

**Type:** `boolean`

**MachineHealthCheck resource enabled**

Flag that indicates if the MachineHealthCheck resource is enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.

**Default:** `true`

---

`.providerIntegration.resourcesApi.machinePoolResourcesEnabled`

**Type:** `boolean`

**Machine pool resources enabled**

Flag that indicates if the machine pool resources are enabled and templated. This is meant only for the initial development purposes for the sake of incrementally integrating cluster chart into cluster-$provider apps.

**Default:** `true`

---

`.providerIntegration.teleport`

**Type:** `object`

**Teleport**

---

`.providerIntegration.teleport.enabled`

**Type:** `boolean`

**Enable teleport**

**Default:** `true`

---

`.providerIntegration.teleport.proxyAddr`

**Type:** `string`

**Teleport proxy address**

**Default:** `"teleport.giantswarm.io:443"`

---

`.providerIntegration.teleport.version`

**Type:** `string`

**Teleport version**

**Default:** `"14.1.3"`

---

`.providerIntegration.workers`

**Type:** `object`

**Provider-specific workers configuration**

---

`.providerIntegration.workers.kubeadmConfig`

**Type:** `object`

**Kubeadm config**

Configuration of workers nodes.

---

`.providerIntegration.workers.kubeadmConfig.files`

**Type:** `array`

**Files**

Provider-specific files that are deployed to worker nodes. They are specified in the cluster-<provider> apps.

---

`.providerIntegration.workers.kubeadmConfig.files[*]`

**Type:** `object`

**File from secret**

It defines a file with content in a Secret

---

`.providerIntegration.workers.kubeadmConfig.files[*].contentFrom`

**Type:** `object`

**Content from**

It specifies where the file content is coming from.

---

`.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret`

**Type:** `object`

**Secret**

Kubernetes Secret resource with the file content.

---

`.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret.key`

**Type:** `string`

**Key**

Secret key where the file content is.

---

`.providerIntegration.workers.kubeadmConfig.files[*].contentFrom.secret.name`

**Type:** `string`

**Name**

Name of the Secret resource.

---

`.providerIntegration.workers.kubeadmConfig.files[*].path`

**Type:** `string`

**Path**

File path on the node.

---

`.providerIntegration.workers.kubeadmConfig.files[*].permissions`

**Type:** `string`

**Permissions**

File permissions in form 0644

**Default:** `"0644"`

---

`.providerIntegration.workers.kubeadmConfig.ignition`

**Type:** `object`

**Ignition**

Ignition-specific configuration.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig`

**Type:** `object`

**Container Linux configuration**

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig`

**Type:** `object`

**Additional config**

Additional configuration to be merged with the Ignition. More info: https://coreos.github.io/ignition/operator-notes/#config-merging.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage`

**Type:** `object`

**Storage**

It describes the desired state of the system’s storage devices.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories`

**Type:** `array`

**Directories**

The list of directories to be created.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*]`

**Type:** `object`

**Directory**

The directory to be created.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].filesystem`

**Type:** `string`

**Filesystem**

The internal identifier of the filesystem in which to create the directory. This matches the last filesystem with the given identifier.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group`

**Type:** `object`

**Group**

It specifies the group of the owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.id`

**Type:** `integer`

**ID**

The group ID of the owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].group.name`

**Type:** `string`

**Name**

The group name of the owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].mode`

**Type:** `integer`

**Mode**

The directory’s permission mode.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].overwrite`

**Type:** `boolean`

**Overwrite**

Whether to delete preexisting nodes at the path.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].path`

**Type:** `string`

**Path**

The absolute path to the directory.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user`

**Type:** `object`

**User**

It specifies the directory’s owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.id`

**Type:** `integer`

**ID**

The user ID of the owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.directories[*].user.name`

**Type:** `string`

**Name**

The user name of the owner.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems`

**Type:** `array`

**File systems**

The list of filesystems to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*]`

**Type:** `object`

**File system**

The filesystem to be configured and/or used in the “files” section. Either “mount” or “path” needs to be specified.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount`

**Type:** `object`

**Mount**

It contains the set of mount and formatting options for the filesystem. A non-null entry indicates that the filesystem should be mounted before it is used by Ignition.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.device`

**Type:** `string`

**Device**

The absolute path to the device. Devices are typically referenced by the "/dev/disk/by-*" symlinks.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.format`

**Type:** `string`

**Format**

The filesystem format (ext4, btrfs, or xfs).

**Allowed values:** `ext4`, `btrfs`, `xfs`

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.label`

**Type:** `string`

**Label**

The label of the filesystem.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options`

**Type:** `array`

**Options**

Any additional options to be passed to the format-specific mkfs utility.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.options[*]`

**Type:** `string`

An additional option to be passed to the format-specific mkfs utility.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.uuid`

**Type:** `string`

**UUID**

The uuid of the filesystem.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].mount.wipeFilesystem`

**Type:** `boolean`

**Wipe filesystem**

Whether or not to wipe the device before filesystem creation, see Ignition’s documentation on filesystems for more information https://github.com/coreos/ignition/blob/main/docs/operator-notes.md#filesystem-reuse-semantics.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].name`

**Type:** `string`

**Name**

The identifier for the filesystem, internal to Ignition. This is only required if the filesystem needs to be referenced in the “files” section.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.storage.filesystems[*].path`

**Type:** `string`

**Path**

The mount-point of the filesystem. A non-null entry indicates that the filesystem has already been mounted by the system at the specified path. This is really only useful for “/sysroot”.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd`

**Type:** `object`

**systemd**

It describes the desired state of the systemd units.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units`

**Type:** `array`

**Units**

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*]`

**Type:** `object`

**systemd unit**

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents`

**Type:** `object`

**Contents**

The contents of the unit.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install`

**Type:** `object`

**Install**

Configuration of the [Install] section.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy`

**Type:** `array`

**WantedBy**

Units with (weak) requirement dependencies on this unit.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.install.wantedBy[*]`

**Type:** `string`

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount`

**Type:** `object`

**Mount**

Configuration of the [Mount] section.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.type`

**Type:** `string`

**Type**

A file system type to mount.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.what`

**Type:** `string`

**What**

An absolute path of a device node, file or other resource to mount.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.mount.where`

**Type:** `string`

**Where**

An absolute path of a file or directory for the mount point; in particular, the destination cannot be a symbolic link.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit`

**Type:** `object`

**Unit**

Configuration of the [Unit] section.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.defaultDependencies`

**Type:** `boolean`

**DefaultDependencies**

Flag that indicates if this systemd unit should have the default systemd unit dependencies.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].contents.unit.description`

**Type:** `string`

**Description**

systemd unit description.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins`

**Type:** `array`

**Unit drop-ins**

The list of drop-ins for the unit

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*]`

**Type:** `object`

**Unit drop-in**

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].contents`

**Type:** `string`

**Contents**

The contents of the drop-in.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].dropins[*].name`

**Type:** `string`

**Name**

The name of the drop-in. This must be suffixed with “.conf”

**Value pattern:** `^.+\.conf$`

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].enabled`

**Type:** `boolean`

**Enabled?**

Whether or not the service shall be enabled. When true, the service is enabled. When false, the service is disabled. When omitted, the service is unmodified. In order for this to have any effect, the unit must have an install section.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].mask`

**Type:** `boolean`

**Masked?**

Whether or not the service shall be masked. When true, the service is masked by symlinking it to /dev/null.

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.additionalConfig.systemd.units[*].name`

**Type:** `string`

**Name**

The name of the unit. This must be suffixed with a valid unit type (e.g. “thing.service”).

---

`.providerIntegration.workers.kubeadmConfig.ignition.containerLinuxConfig.strict`

**Type:** `boolean`

**Strict**

It controls if AdditionalConfig should be strictly parsed. If so, warnings are treated as errors.

---

`.providerIntegration.workers.kubeadmConfig.postKubeadmCommands`

**Type:** `array`

**Post-kubeadm commands**

Extra commands to run after kubeadm runs.

---

`.providerIntegration.workers.kubeadmConfig.postKubeadmCommands[*]`

**Type:** `string`

---

`.providerIntegration.workers.kubeadmConfig.preKubeadmCommands`

**Type:** `array`

**Pre-kubeadm commands**

Extra commands to run before kubeadm runs.

---

`.providerIntegration.workers.kubeadmConfig.preKubeadmCommands[*]`

**Type:** `string`

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster)
