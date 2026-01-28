---
title: cluster-aws chart reference
linkTitle: cluster-aws
description:  A helm chart for creating Cluster API clusters with the AWS infrastructure provider (CAPA).; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster-aws
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-aws?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-aws
source_repository_ref: v0.60.1
---

The `cluster-aws` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API cluster.

## Chart configuration reference

### AWS settings {#aws-settings}

---

`.global.providerSpecific.additionalResourceTags`

**Type:** `object`

**Additional resource tags**

Additional tags to add to AWS resources created by the cluster.

---

`.global.providerSpecific.additionalResourceTags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.global.providerSpecific.ami`

**Type:** `string`

**Amazon machine image (AMI)**

If specified, this image will be used to provision EC2 instances.

---

`.global.providerSpecific.awsClusterRoleIdentityName`

**Type:** `string`

**Cluster role identity name**

Name of an AWSClusterRoleIdentity object. Learn more at https://docs.giantswarm.io/getting-started/cloud-provider-accounts/cluster-api/aws/#configure-the-awsclusterroleidentity .

**Value pattern:** `^[-a-zA-Z0-9_\.]{1,63}$`

**Default:** `"default"`

---

`.global.providerSpecific.flatcarAwsAccount`

**Type:** `string`

**AWS account owning Flatcar image**

AWS account ID owning the Flatcar Container Linux AMI.

**Default:** `"706635527432"`

---

`.global.providerSpecific.region`

**Type:** `string`

**Region**

### Apps {#apps}Configuration of apps that are part of the cluster.

---

`.global.apps.awsCloudControllerManager`

**Type:** `object`

**App**

Configuration of an default app that is part of the cluster.

---

`.global.apps.awsCloudControllerManager.extraConfigs`

**Type:** `array`

**Extra config maps or secrets**

Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.

---

`.global.apps.awsCloudControllerManager.extraConfigs[*]`

**Type:** `object`

**Config map or secret**

---

`.global.apps.awsCloudControllerManager.extraConfigs[*].kind`

**Type:** `string`

**Kind**

Specifies whether the resource is a config map or a secret.

**Allowed values:** `ConfigMap`, `Secret`

---

`.global.apps.awsCloudControllerManager.extraConfigs[*].name`

**Type:** `string`

**Name**

Name of the config map or secret. The object must exist in the same namespace as the cluster App.

---

`.global.apps.awsCloudControllerManager.extraConfigs[*].optional`

**Type:** `boolean`

**Optional**

Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

---

`.global.apps.awsCloudControllerManager.values`

**Type:** `object`

**Values**

Values to be passed to the app. Values will have higher priority than values from configmaps.

---

`.global.apps.awsEbsCsiDriver`

**Type:** `object`

**App**

Configuration of an default app that is part of the cluster.

---

`.global.apps.awsEbsCsiDriver.extraConfigs`

**Type:** `array`

**Extra config maps or secrets**

Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.

---

`.global.apps.awsEbsCsiDriver.extraConfigs[*]`

**Type:** `object`

**Config map or secret**

---

`.global.apps.awsEbsCsiDriver.extraConfigs[*].kind`

**Type:** `string`

**Kind**

Specifies whether the resource is a config map or a secret.

**Allowed values:** `ConfigMap`, `Secret`

---

`.global.apps.awsEbsCsiDriver.extraConfigs[*].name`

**Type:** `string`

**Name**

Name of the config map or secret. The object must exist in the same namespace as the cluster App.

---

`.global.apps.awsEbsCsiDriver.extraConfigs[*].optional`

**Type:** `boolean`

**Optional**

Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

---

`.global.apps.awsEbsCsiDriver.values`

**Type:** `object`

**Values**

Values to be passed to the app. Values will have higher priority than values from configmaps.

---

`.global.apps.cilium`

**Type:** `object`

**App**

Configuration of an default app that is part of the cluster.

---

`.global.apps.cilium.extraConfigs`

**Type:** `array`

**Extra config maps or secrets**

Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.

---

`.global.apps.cilium.extraConfigs[*]`

**Type:** `object`

**Config map or secret**

---

`.global.apps.cilium.extraConfigs[*].kind`

**Type:** `string`

**Kind**

Specifies whether the resource is a config map or a secret.

**Allowed values:** `ConfigMap`, `Secret`

---

`.global.apps.cilium.extraConfigs[*].name`

**Type:** `string`

**Name**

Name of the config map or secret. The object must exist in the same namespace as the cluster App.

---

`.global.apps.cilium.extraConfigs[*].optional`

**Type:** `boolean`

**Optional**

Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

---

`.global.apps.cilium.values`

**Type:** `object`

**Values**

Values to be passed to the app. Values will have higher priority than values from configmaps.

---

`.global.apps.coreDns`

**Type:** `object`

**App**

Configuration of an default app that is part of the cluster.

---

`.global.apps.coreDns.extraConfigs`

**Type:** `array`

**Extra config maps or secrets**

Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.

---

`.global.apps.coreDns.extraConfigs[*]`

**Type:** `object`

**Config map or secret**

---

`.global.apps.coreDns.extraConfigs[*].kind`

**Type:** `string`

**Kind**

Specifies whether the resource is a config map or a secret.

**Allowed values:** `ConfigMap`, `Secret`

---

`.global.apps.coreDns.extraConfigs[*].name`

**Type:** `string`

**Name**

Name of the config map or secret. The object must exist in the same namespace as the cluster App.

---

`.global.apps.coreDns.extraConfigs[*].optional`

**Type:** `boolean`

**Optional**

Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

---

`.global.apps.coreDns.values`

**Type:** `object`

**Values**

Values to be passed to the app. Values will have higher priority than values from configmaps.

---

`.global.apps.verticalPodAutoscalerCrd`

**Type:** `object`

**App**

Configuration of an default app that is part of the cluster.

---

`.global.apps.verticalPodAutoscalerCrd.extraConfigs`

**Type:** `array`

**Extra config maps or secrets**

Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key 'values'. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.

---

`.global.apps.verticalPodAutoscalerCrd.extraConfigs[*]`

**Type:** `object`

**Config map or secret**

---

`.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].kind`

**Type:** `string`

**Kind**

Specifies whether the resource is a config map or a secret.

**Allowed values:** `ConfigMap`, `Secret`

---

`.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].name`

**Type:** `string`

**Name**

Name of the config map or secret. The object must exist in the same namespace as the cluster App.

---

`.global.apps.verticalPodAutoscalerCrd.extraConfigs[*].optional`

**Type:** `boolean`

**Optional**

Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.

---

`.global.apps.verticalPodAutoscalerCrd.values`

**Type:** `object`

**Values**

Values to be passed to the app. Values will have higher priority than values from configmaps.

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

### Connectivity {#connectivity}

---

`.global.connectivity.availabilityZoneUsageLimit`

**Type:** `integer`

**Availability zones**

Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets.

**Default:** `3`

---

`.global.connectivity.baseDomain`

**Type:** `string`

**Base DNS domain**

---

`.global.connectivity.dns`

**Type:** `object`

**DNS**

---

`.global.connectivity.dns.resolverRulesOwnerAccount`

**Type:** `string`

**Resolver rules owner**

ID of the AWS account that created the resolver rules to be associated with the workload cluster VPC.

---

`.global.connectivity.dns.resolverRulesOwnerAccount[option#1]`

**Value pattern:** `^\d{12}$`

---

`.global.connectivity.dns.resolverRulesOwnerAccount[option#2]`

**Must have value:** ``

---

`.global.connectivity.network`

**Type:** `object`

**Network**

---

`.global.connectivity.network.internetGatewayId`

**Type:** `string`

**Internet Gateway ID**

ID of the Internet gateway for the VPC.

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

**K8s Service subnets**

**Default:** `["172.31.0.0/16"]`

---

`.global.connectivity.network.services.cidrBlocks[*]`

**Type:** `string`

**Service subnet**

IPv4 address range for kubernetes services, in CIDR notation.

**Example:** `"172.31.0.0/16"`

---

`.global.connectivity.network.vpcCidr`

**Type:** `string`

**VPC subnet**

IPv4 address range to assign to this cluster's VPC, in CIDR notation.

**Default:** `"10.0.0.0/16"`

---

`.global.connectivity.network.vpcId`

**Type:** `string`

**VPC id**

ID of the VPC, where the cluster will be deployed. The VPC must exist and it case this is set, VPC wont be created by controllers.

---

`.global.connectivity.proxy`

**Type:** `object`

**Proxy**

Whether/how outgoing traffic is routed through proxy servers.

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

To be passed to the NO_PROXY environment variable in all hosts.

---

`.global.connectivity.subnets`

**Type:** `array`

**Subnets**

Subnets are created and tagged based on this definition.

**Default:** `[{"cidrBlocks":[{"availabilityZone":"a","cidr":"10.0.0.0/20"},{"availabilityZone":"b","cidr":"10.0.16.0/20"},{"availabilityZone":"c","cidr":"10.0.32.0/20"}],"isPublic":true},{"cidrBlocks":[{"availabilityZone":"a","cidr":"10.0.64.0/18"},{"availabilityZone":"b","cidr":"10.0.128.0/18"},{"availabilityZone":"c","cidr":"10.0.192.0/18"}],"isPublic":false}]`

---

`.global.connectivity.subnets[*]`

**Type:** `object`

**Subnet**

---

`.global.connectivity.subnets[*].cidrBlocks`

**Type:** `array`

**Network**

---

`.global.connectivity.subnets[*].cidrBlocks[*]`

**Type:** `object`

---

`.global.connectivity.subnets[*].cidrBlocks[*].availabilityZone`

**Type:** `string`

**Availability zone**

**Example:** `"a"`

---

`.global.connectivity.subnets[*].cidrBlocks[*].cidr`

**Type:** `string`

**Address range**

IPv4 address range, in CIDR notation.

---

`.global.connectivity.subnets[*].cidrBlocks[*].tags`

**Type:** `object`

**Tags**

AWS resource tags to assign to this subnet.

---

`.global.connectivity.subnets[*].cidrBlocks[*].tags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.global.connectivity.subnets[*].id`

**Type:** `string`

**ID of the subnet**

ID of an existing subnet. When set, this subnet will be used instead of creating a new one.

---

`.global.connectivity.subnets[*].isPublic`

**Type:** `boolean`

**Public**

---

`.global.connectivity.subnets[*].natGatewayId`

**Type:** `string`

**ID of the NAT Gateway**

ID of the NAT Gateway used for this existing subnet.

---

`.global.connectivity.subnets[*].routeTableId`

**Type:** `string`

**ID of route table**

ID of the route table, assigned to the existing subnet. Must be provided when defining subnet via ID.

---

`.global.connectivity.subnets[*].tags`

**Type:** `object`

**Tags**

AWS resource tags to assign to this CIDR block.

---

`.global.connectivity.subnets[*].tags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.global.connectivity.topology`

**Type:** `object`

**Topology**

Networking architecture between management cluster and workload cluster.

---

`.global.connectivity.topology.mode`

**Type:** `string`

**Mode**

Valid values: GiantSwarmManaged, UserManaged, None.

**Allowed values:** `None`, `GiantSwarmManaged`, `UserManaged`

**Default:** `"None"`

---

`.global.connectivity.topology.prefixListId`

**Type:** `string`

**Prefix list ID**

ID of the managed prefix list to use when the topology mode is set to 'UserManaged'.

---

`.global.connectivity.topology.transitGatewayId`

**Type:** `string`

**Transit gateway ID**

If the topology mode is set to 'UserManaged', this can be used to specify the transit gateway to use.

---

`.global.connectivity.vpcEndpointMode`

**Type:** `string`

**VPC endpoint mode**

Who is reponsible for creation and management of VPC endpoints.

**Allowed values:** `GiantSwarmManaged`, `UserManaged`

**Default:** `"GiantSwarmManaged"`

---

`.global.connectivity.vpcMode`

**Type:** `string`

**VPC mode**

Whether the cluser's VPC is created with public, internet facing resources (public subnets, NAT gateway) or not (private).

**Allowed values:** `public`, `private`

**Default:** `"public"`

### Control plane {#control-plane}

---

`.global.controlPlane.additionalSecurityGroups`

**Type:** `array`

**Control Plane additional security groups**

Additional security groups that will be added to the control plane nodes.

---

`.global.controlPlane.additionalSecurityGroups[*]`

**Type:** `object`

**Security group**

---

`.global.controlPlane.additionalSecurityGroups[*].id`

**Type:** `string`

**Id of the security group**

ID of the security group that will be added to the control plane nodes. The security group must exist.

---

`.global.controlPlane.apiExtraArgs`

**Type:** `object`

**API extra arguments**

Extra arguments passed to the kubernetes API server.

---

`.global.controlPlane.apiExtraArgs.PATTERN`

**Type:** `string`

**argument**

**Key pattern:** `PATTERN`=`^.+:.+$`

---

`.global.controlPlane.apiExtraCertSANs`

**Type:** `array`

**API extra cert SANs**

Extra certs SANs passed to the kubeadmcontrolplane CR.

---

`.global.controlPlane.apiExtraCertSANs[*]`

**Type:** `string`

**cert SAN**

---

`.global.controlPlane.apiMode`

**Type:** `string`

**API mode**

Whether the Kubernetes API server load balancer should be reachable from the internet (public) or internal only (private).

**Allowed values:** `public`, `private`

**Default:** `"public"`

---

`.global.controlPlane.apiServerPort`

**Type:** `integer`

**API server port**

The API server Load Balancer port. This option sets the Spec.ClusterNetwork.APIServerPort field on the Cluster CR. In CAPI this field isn't used currently. It is instead used in providers. In CAPA this sets only the public facing port of the Load Balancer. In CAPZ both the public facing and the destination port are set to this value. CAPV and CAPVCD do not use it.

**Default:** `443`

---

`.global.controlPlane.containerdVolumeSizeGB`

**Type:** `integer`

**Containerd volume size (GB)**

**Default:** `100`

---

`.global.controlPlane.etcdVolumeSizeGB`

**Type:** `integer`

**Etcd volume size (GB)**

**Default:** `100`

---

`.global.controlPlane.instanceType`

**Type:** `string`

**EC2 instance type**

**Default:** `"r6i.xlarge"`

---

`.global.controlPlane.kubeletVolumeSizeGB`

**Type:** `integer`

**Kubelet volume size (GB)**

**Default:** `100`

---

`.global.controlPlane.loadBalancerIngressAllowCidrBlocks`

**Type:** `array`

**Load balancer allow list**

IPv4 address ranges that are allowed to connect to the control plane load balancer, in CIDR notation. When setting this field, remember to add the Management cluster Nat Gateway IPs provided by Giant Swarm so that the cluster can still be managed. These Nat Gateway IPs can be found in the Management Cluster AWSCluster '.status.networkStatus.natGatewaysIPs' field.

---

`.global.controlPlane.loadBalancerIngressAllowCidrBlocks[*]`

**Type:** `string`

**Address range**

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

`.global.controlPlane.rootVolumeSizeGB`

**Type:** `integer`

**Root volume size (GB)**

**Default:** `120`

---

`.global.controlPlane.subnetTags`

**Type:** `array`

**Subnet tags**

Tags to select AWS resources for the control plane by.

---

`.global.controlPlane.subnetTags[*]`

**Type:** `object`

**Subnet tag**

---

`.global.controlPlane.subnetTags[*].*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

### Internal {#internal}For Giant Swarm internal use only, not stable, or not supported by UIs.

---

`.internal.cgroupsv1`

**Type:** `boolean`

**CGroups v1**

Force use of CGroups v1 for whole cluster.

**Default:** `false`

---

`.internal.hashSalt`

**Type:** `string`

**Hash salt**

If specified, this token is used as a salt to the hash suffix of some resource names. Can be used to force-recreate some resources.

---

`.internal.kubernetesVersion`

**Type:** `string`

**Kubernetes version**

**Example:** `"1.24.7"`

**Default:** `"1.25.16"`

---

`.internal.migration`

**Type:** `object`

**Migration values**

Section used for migration of cluster from vintage to CAPI

---

`.internal.migration.apiBindPort`

**Type:** `integer`

**Kubernetes API bind port**

Kubernetes API bind port used for kube api pod

**Default:** `6443`

---

`.internal.migration.controlPlaneExtraFiles`

**Type:** `array`

**Control Plane extra files**

Additional fiels that will be provisioned to control-plane nodes, reference is from secret in the same namespace.

---

`.internal.migration.controlPlaneExtraFiles[*]`

**Type:** `object`

**file**

---

`.internal.migration.controlPlaneExtraFiles[*].contentFrom`

**Type:** `object`

**content from**

---

`.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret`

**Type:** `object`

**secret**

---

`.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.key`

**Type:** `string`

**secret key for file content**

---

`.internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.name`

**Type:** `string`

**secret name for file content**

---

`.internal.migration.controlPlaneExtraFiles[*].path`

**Type:** `string`

**file path**

---

`.internal.migration.controlPlaneExtraFiles[*].permissions`

**Type:** `string`

**file permissions in form 0644**

**Default:** `"0644"`

---

`.internal.migration.controlPlanePostKubeadmCommands`

**Type:** `array`

**Control Plane Post Kubeadm Commands**

Additional Post-Kubeadm Commands executed on the control plane node.

---

`.internal.migration.controlPlanePostKubeadmCommands[*]`

**Type:** `string`

**command**

---

`.internal.migration.controlPlanePreKubeadmCommands`

**Type:** `array`

**Control Plane Pre Kubeadm Commands**

Additional Pre-Kubeadm Commands executed on the control plane node.

---

`.internal.migration.controlPlanePreKubeadmCommands[*]`

**Type:** `string`

**command**

---

`.internal.migration.etcdExtraArgs`

**Type:** `object`

**Etcd extra arguments**

---

`.internal.migration.etcdExtraArgs.PATTERN`

**Type:** `string`

**argument**

**Key pattern:** `PATTERN`=`^.+:.+$`

---

`.internal.migration.irsaAdditionalDomain`

**Type:** `string`

**IRSA additional domain**

Additional domain to be added to IRSA trust relationship.

---

`.internal.nodePools`

**Type:** `object`

**Default node pool**

**Default:** `{"def00":{"customNodeLabels":["label=default"],"instanceType":"r6i.xlarge","maxSize":3,"minSize":3}}`

---

`.internal.nodePools.PATTERN`

**Type:** `object`

**Node pool**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.additionalSecurityGroups`

**Type:** `array`

**Machine pool additional security groups**

Additional security groups that will be added to the machine pool nodes.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.additionalSecurityGroups[*]`

**Type:** `object`

**security group**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.additionalSecurityGroups[*].id`

**Type:** `string`

**Id of the security group**

ID of the security group that will be added to the machine pool nodes. The security group must exist.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.availabilityZones`

**Type:** `array`

**Availability zones**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.availabilityZones[*]`

**Type:** `string`

**Availability zone**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeLabels`

**Type:** `array`

**Custom node labels**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeLabels[*]`

**Type:** `string`

**Label**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeTaints`

**Type:** `array`

**Custom node taints**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeTaints[*]`

**Type:** `object`

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeTaints[*].effect`

**Type:** `string`

**Effect**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.internal.nodePools.PATTERN.customNodeTaints[*].key`

**Type:** `string`

**Key**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.customNodeTaints[*].value`

**Type:** `string`

**Value**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.instanceType`

**Type:** `string`

**EC2 instance type**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.instanceTypeOverrides`

**Type:** `array`

**Instance type overrides**

Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Default:** `[]`

---

`.internal.nodePools.PATTERN.instanceTypeOverrides[*]`

**Type:** `string`

**EC2 instance type**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.maxSize`

**Type:** `integer`

**Maximum number of nodes**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.minSize`

**Type:** `integer`

**Minimum number of nodes**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.rootVolumeSizeGB`

**Type:** `integer`

**Root volume size (GB)**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.spotInstances`

**Type:** `object`

**Spot instances**

Compared to on-demand instances, spot instances can help you save cost.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.spotInstances.enabled`

**Type:** `boolean`

**Enable**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Default:** `false`

---

`.internal.nodePools.PATTERN.spotInstances.maxPrice`

**Type:** `number`

**Maximum price to pay per instance per hour, in USD.**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.subnetTags`

**Type:** `array`

**Subnet tags**

Tags to filter which AWS subnets will be used for this node pool.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.subnetTags[*]`

**Type:** `object`

**Subnet tag**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.internal.nodePools.PATTERN.subnetTags[*].*`

**Type:** `string`

**Tag value**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.internal.sandboxContainerImage`

**Type:** `object`

**Sandbox image**

The image used by sandbox / pause container

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

### Kubectl image {#kubectl-image}

---

`.kubectlImage.name`

**Type:** `string`

**Repository**

**Default:** `"giantswarm/kubectl"`

---

`.kubectlImage.registry`

**Type:** `string`

**Registry**

**Default:** `"gsoci.azurecr.io"`

---

`.kubectlImage.tag`

**Type:** `string`

**Tag**

**Default:** `"1.23.5"`

### Metadata {#metadata}

---

`.global.metadata.description`

**Type:** `string`

**Cluster description**

User-friendly description of the cluster's purpose.

---

`.global.metadata.name`

**Type:** `string`

**Cluster name**

Unique identifier, cannot be changed after creation.

---

`.global.metadata.organization`

**Type:** `string`

**Organization**

---

`.global.metadata.preventDeletion`

**Type:** `boolean`

**Prevent cluster deletion**

**Default:** `false`

---

`.global.metadata.servicePriority`

**Type:** `string`

**Service priority**

The relative importance of this cluster.

**Allowed values:** `highest`, `medium`, `lowest`

**Default:** `"highest"`

### Node pools {#node-pools}Node pools of the cluster. If not specified, this defaults to the value of `internal.nodePools`.

---

`.global.nodePools.PATTERN`

**Type:** `object`

**Node pool**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.additionalSecurityGroups`

**Type:** `array`

**Machine pool additional security groups**

Additional security groups that will be added to the machine pool nodes.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.additionalSecurityGroups[*]`

**Type:** `object`

**security group**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.additionalSecurityGroups[*].id`

**Type:** `string`

**Id of the security group**

ID of the security group that will be added to the machine pool nodes. The security group must exist.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.availabilityZones`

**Type:** `array`

**Availability zones**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.availabilityZones[*]`

**Type:** `string`

**Availability zone**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeLabels`

**Type:** `array`

**Custom node labels**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeLabels[*]`

**Type:** `string`

**Label**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeTaints`

**Type:** `array`

**Custom node taints**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeTaints[*]`

**Type:** `object`

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeTaints[*].effect`

**Type:** `string`

**Effect**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Allowed values:** `NoSchedule`, `PreferNoSchedule`, `NoExecute`

---

`.global.nodePools.PATTERN.customNodeTaints[*].key`

**Type:** `string`

**Key**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.customNodeTaints[*].value`

**Type:** `string`

**Value**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.instanceType`

**Type:** `string`

**EC2 instance type**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.instanceTypeOverrides`

**Type:** `array`

**Instance type overrides**

Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Default:** `[]`

---

`.global.nodePools.PATTERN.instanceTypeOverrides[*]`

**Type:** `string`

**EC2 instance type**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.maxSize`

**Type:** `integer`

**Maximum number of nodes**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.minSize`

**Type:** `integer`

**Minimum number of nodes**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.rootVolumeSizeGB`

**Type:** `integer`

**Root volume size (GB)**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.spotInstances`

**Type:** `object`

**Spot instances**

Compared to on-demand instances, spot instances can help you save cost.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.spotInstances.enabled`

**Type:** `boolean`

**Enable**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Default:** `false`

---

`.global.nodePools.PATTERN.spotInstances.maxPrice`

**Type:** `number`

**Maximum price to pay per instance per hour, in USD.**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.subnetTags`

**Type:** `array`

**Subnet tags**

Tags to filter which AWS subnets will be used for this node pool.

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.subnetTags[*]`

**Type:** `object`

**Subnet tag**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

---

`.global.nodePools.PATTERN.subnetTags[*].*`

**Type:** `string`

**Tag value**

**Key pattern:** `PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

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

**Default:** `true`

### Other {#other}

---

`.baseDomain`

**Type:** `string`

**Base DNS domain**

---

`.cluster`

**Type:** `object`

**Cluster**

Helm values for the provider-independent cluster chart

**Default:** `{"providerIntegration":{"clusterAnnotationsTemplateName":"awsConnectivityLabels","components":{"systemd":{"timesyncd":{"ntp":["169.254.169.123"]}}},"connectivity":{"proxy":{"noProxy":{"templateName":"awsNoProxyList","value":["elb.amazonaws.com","169.254.169.254"]}}},"controlPlane":{"kubeadmConfig":{"clusterConfiguration":{"apiServer":{"apiAudiences":{"templateName":"awsApiServerApiAudiences"},"featureGates":[{"enabled":true,"name":"CronJobTimeZone"}],"serviceAccountIssuer":{"clusterDomainPrefix":"irsa"}}},"ignition":{"containerLinuxConfig":{"additionalConfig":{"storage":{"filesystems":[{"mount":{"device":"/dev/xvdc","format":"xfs","label":"etcd","wipeFilesystem":true},"name":"etcd"},{"mount":{"device":"/dev/xvdd","format":"xfs","label":"containerd","wipeFilesystem":true},"name":"containerd"},{"mount":{"device":"/dev/xvde","format":"xfs","label":"kubelet","wipeFilesystem":true},"name":"kubelet"}]},"systemd":{"units":[{"contents":{"install":{"wantedBy":["local-fs-pre.target"]},"mount":{"type":"xfs","what":"/dev/disk/by-label/etcd","where":"/var/lib/etcd"},"unit":{"defaultDependencies":false,"description":"etcd volume"}},"enabled":true,"name":"var-lib-etcd.mount"},{"contents":{"install":{"wantedBy":["local-fs-pre.target"]},"mount":{"type":"xfs","what":"/dev/disk/by-label/kubelet","where":"/var/lib/kubelet"},"unit":{"defaultDependencies":false,"description":"kubelet volume"}},"enabled":true,"name":"var-lib-kubelet.mount"},{"contents":{"install":{"wantedBy":["local-fs-pre.target"]},"mount":{"type":"xfs","what":"/dev/disk/by-label/containerd","where":"/var/lib/containerd"},"unit":{"defaultDependencies":false,"description":"containerd volume"}},"enabled":true,"name":"var-lib-containerd.mount"}]}}}}},"resources":{"infrastructureMachineTemplate":{"group":"infrastructure.cluster.x-k8s.io","kind":"AWSMachineTemplate","version":"v1beta1"},"infrastructureMachineTemplateSpecTemplateName":"controlplane-awsmachinetemplate-spec"}},"pauseProperties":{"global.connectivity.vpcMode":"private"},"provider":"aws","resourcesApi":{"bastionResourceEnabled":false,"clusterResourceEnabled":true,"controlPlaneResourceEnabled":true,"infrastructureCluster":{"group":"infrastructure.cluster.x-k8s.io","kind":"AWSCluster","version":"v1beta1"},"machineHealthCheckResourceEnabled":false,"machinePoolResourcesEnabled":false,"nodePoolKind":"MachinePool"}}}`

---

`.cluster-shared`

**Type:** `object`

**Library chart**

---

`.managementCluster`

**Type:** `string`

**Management cluster**

Name of the Cluster API cluster managing this workload cluster.

---

`.provider`

**Type:** `string`

**Cluster API provider name**

<!-- DOCS_END -->

## Further reading

- [Source repository](https://github.com/giantswarm/cluster-aws)
