---
title: Cluster-Aws chart reference
linkTitle: cluster-aws chart reference
description: |
  A helm chart for creating Cluster API clusters with the AWS infrastructure provider (CAPA).
weight: 100
menu:
  main:
    identifier: cluster-aws
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-aws
source_repository_ref: v0.60.1
---

The `cluster-aws` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API cluster.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-aws version.

&lt;!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-aws/values.schema.json -o helm/cluster-aws/README.md

--&gt;



### AWS settings
Properties within the `.global.providerSpecific` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.providerSpecific.additionalResourceTags` | **Additional resource tags** - Additional tags to add to AWS resources created by the cluster.|**Type:** `object`|
| `global.providerSpecific.additionalResourceTags.*` | **Tag value**|**Type:** `string`|
| `global.providerSpecific.ami` | **Amazon machine image (AMI)** - If specified, this image will be used to provision EC2 instances.|**Type:** `string`|
| `global.providerSpecific.awsClusterRoleIdentityName` | **Cluster role identity name** - Name of an AWSClusterRoleIdentity object. Learn more at https://docs.giantswarm.io/getting-started/cloud-provider-accounts/cluster-api/aws/#configure-the-awsclusterroleidentity .|**Type:** `string`**Default:** `&#34;default&#34;`|
| `global.providerSpecific.flatcarAwsAccount` | **AWS account owning Flatcar image** - AWS account ID owning the Flatcar Container Linux AMI.|**Type:** `string`**Default:** `&#34;706635527432&#34;`|
| `global.providerSpecific.region` | **Region**|**Type:** `string`|

### Apps
Properties within the `.global.apps` object
Configuration of apps that are part of the cluster.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.apps.awsCloudControllerManager` | **App** - Configuration of an default app that is part of the cluster.|**Type:** `object`|
| `global.apps.awsCloudControllerManager.extraConfigs` | **Extra config maps or secrets** - Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key &#39;values&#39;. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.|**Type:** `array`|
| `global.apps.awsCloudControllerManager.extraConfigs[*]` | **Config map or secret**|**Type:** `object`|
| `global.apps.awsCloudControllerManager.extraConfigs[*].kind` | **Kind** - Specifies whether the resource is a config map or a secret.|**Type:** `string`|
| `global.apps.awsCloudControllerManager.extraConfigs[*].name` | **Name** - Name of the config map or secret. The object must exist in the same namespace as the cluster App.|**Type:** `string`|
| `global.apps.awsCloudControllerManager.extraConfigs[*].optional` | **Optional** - Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.|**Type:** `boolean`|
| `global.apps.awsCloudControllerManager.values` | **Values** - Values to be passed to the app. Values will have higher priority than values from configmaps.|**Type:** `object`|
| `global.apps.awsEbsCsiDriver` | **App** - Configuration of an default app that is part of the cluster.|**Type:** `object`|
| `global.apps.awsEbsCsiDriver.extraConfigs` | **Extra config maps or secrets** - Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key &#39;values&#39;. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.|**Type:** `array`|
| `global.apps.awsEbsCsiDriver.extraConfigs[*]` | **Config map or secret**|**Type:** `object`|
| `global.apps.awsEbsCsiDriver.extraConfigs[*].kind` | **Kind** - Specifies whether the resource is a config map or a secret.|**Type:** `string`|
| `global.apps.awsEbsCsiDriver.extraConfigs[*].name` | **Name** - Name of the config map or secret. The object must exist in the same namespace as the cluster App.|**Type:** `string`|
| `global.apps.awsEbsCsiDriver.extraConfigs[*].optional` | **Optional** - Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.|**Type:** `boolean`|
| `global.apps.awsEbsCsiDriver.values` | **Values** - Values to be passed to the app. Values will have higher priority than values from configmaps.|**Type:** `object`|
| `global.apps.cilium` | **App** - Configuration of an default app that is part of the cluster.|**Type:** `object`|
| `global.apps.cilium.extraConfigs` | **Extra config maps or secrets** - Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key &#39;values&#39;. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.|**Type:** `array`|
| `global.apps.cilium.extraConfigs[*]` | **Config map or secret**|**Type:** `object`|
| `global.apps.cilium.extraConfigs[*].kind` | **Kind** - Specifies whether the resource is a config map or a secret.|**Type:** `string`|
| `global.apps.cilium.extraConfigs[*].name` | **Name** - Name of the config map or secret. The object must exist in the same namespace as the cluster App.|**Type:** `string`|
| `global.apps.cilium.extraConfigs[*].optional` | **Optional** - Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.|**Type:** `boolean`|
| `global.apps.cilium.values` | **Values** - Values to be passed to the app. Values will have higher priority than values from configmaps.|**Type:** `object`|
| `global.apps.coreDns` | **App** - Configuration of an default app that is part of the cluster.|**Type:** `object`|
| `global.apps.coreDns.extraConfigs` | **Extra config maps or secrets** - Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key &#39;values&#39;. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.|**Type:** `array`|
| `global.apps.coreDns.extraConfigs[*]` | **Config map or secret**|**Type:** `object`|
| `global.apps.coreDns.extraConfigs[*].kind` | **Kind** - Specifies whether the resource is a config map or a secret.|**Type:** `string`|
| `global.apps.coreDns.extraConfigs[*].name` | **Name** - Name of the config map or secret. The object must exist in the same namespace as the cluster App.|**Type:** `string`|
| `global.apps.coreDns.extraConfigs[*].optional` | **Optional** - Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.|**Type:** `boolean`|
| `global.apps.coreDns.values` | **Values** - Values to be passed to the app. Values will have higher priority than values from configmaps.|**Type:** `object`|
| `global.apps.verticalPodAutoscalerCrd` | **App** - Configuration of an default app that is part of the cluster.|**Type:** `object`|
| `global.apps.verticalPodAutoscalerCrd.extraConfigs` | **Extra config maps or secrets** - Extra config maps or secrets that will be used to customize to the app. The desired values must be under configmap or secret key &#39;values&#39;. The values are merged in the order given, with the later values overwriting earlier, and then inline values overwriting those. Resources must be in the same namespace as the cluster.|**Type:** `array`|
| `global.apps.verticalPodAutoscalerCrd.extraConfigs[*]` | **Config map or secret**|**Type:** `object`|
| `global.apps.verticalPodAutoscalerCrd.extraConfigs[*].kind` | **Kind** - Specifies whether the resource is a config map or a secret.|**Type:** `string`|
| `global.apps.verticalPodAutoscalerCrd.extraConfigs[*].name` | **Name** - Name of the config map or secret. The object must exist in the same namespace as the cluster App.|**Type:** `string`|
| `global.apps.verticalPodAutoscalerCrd.extraConfigs[*].optional` | **Optional** - Optional marks this ValuesReference as optional. When set, a not found error for the values reference is ignored, but any ValuesKey, TargetPath or transient error will still result in a reconciliation failure.|**Type:** `boolean`|
| `global.apps.verticalPodAutoscalerCrd.values` | **Values** - Values to be passed to the app. Values will have higher priority than values from configmaps.|**Type:** `object`|

### Components
Properties within the `.global.components` object
Advanced configuration of components that are running on all nodes.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.components.containerd` | **Containerd** - Configuration of containerd.|**Type:** `object`|
| `global.components.containerd.containerRegistries` | **Container registries** - Endpoints and credentials configuration for container registries.|**Type:** `object`**Default:** `{&#34;docker.io&#34;:[{&#34;endpoint&#34;:&#34;registry-1.docker.io&#34;},{&#34;endpoint&#34;:&#34;giantswarm.azurecr.io&#34;}]}`|
| `global.components.containerd.containerRegistries.*` | **Registries** - Container registries and mirrors|**Type:** `array`|
| `global.components.containerd.containerRegistries.*[*]` | **Registry**|**Type:** `object`|
| `global.components.containerd.containerRegistries.*[*].credentials` | **Credentials**|**Type:** `object`|
| `global.components.containerd.containerRegistries.*[*].credentials.auth` | **Auth** - Base64-encoded string from the concatenation of the username, a colon, and the password.|**Type:** `string`|
| `global.components.containerd.containerRegistries.*[*].credentials.identitytoken` | **Identity token** - Used to authenticate the user and obtain an access token for the registry.|**Type:** `string`|
| `global.components.containerd.containerRegistries.*[*].credentials.password` | **Password** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `global.components.containerd.containerRegistries.*[*].credentials.username` | **Username** - Used to authenticate for the registry with username/password.|**Type:** `string`|
| `global.components.containerd.containerRegistries.*[*].endpoint` | **Endpoint** - Endpoint for the container registry.|**Type:** `string`|

### Connectivity
Properties within the `.global.connectivity` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.connectivity.availabilityZoneUsageLimit` | **Availability zones** - Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets.|**Type:** `integer`**Default:** `3`|
| `global.connectivity.baseDomain` | **Base DNS domain**|**Type:** `string`|
| `global.connectivity.dns` | **DNS**|**Type:** `object`|
| `global.connectivity.dns.resolverRulesOwnerAccount` | **Resolver rules owner** - ID of the AWS account that created the resolver rules to be associated with the workload cluster VPC.|**Type:** `string`|
| `global.connectivity.network` | **Network**|**Type:** `object`|
| `global.connectivity.network.internetGatewayId` | **Internet Gateway ID** - ID of the Internet gateway for the VPC.|**Type:** `string`|
| `global.connectivity.network.pods` | **Pods**|**Type:** `object`|
| `global.connectivity.network.pods.cidrBlocks` | **Pod subnets**|**Type:** `array`**Default:** `[&#34;100.64.0.0/12&#34;]`|
| `global.connectivity.network.pods.cidrBlocks[*]` | **Pod subnet** - IPv4 address range for pods, in CIDR notation.|**Type:** `string`|
| `global.connectivity.network.services` | **Services**|**Type:** `object`|
| `global.connectivity.network.services.cidrBlocks` | **K8s Service subnets**|**Type:** `array`**Default:** `[&#34;172.31.0.0/16&#34;]`|
| `global.connectivity.network.services.cidrBlocks[*]` | **Service subnet** - IPv4 address range for kubernetes services, in CIDR notation.|**Type:** `string`|
| `global.connectivity.network.vpcCidr` | **VPC subnet** - IPv4 address range to assign to this cluster&#39;s VPC, in CIDR notation.|**Type:** `string`**Default:** `&#34;10.0.0.0/16&#34;`|
| `global.connectivity.network.vpcId` | **VPC id** - ID of the VPC, where the cluster will be deployed. The VPC must exist and it case this is set, VPC wont be created by controllers.|**Type:** `string`|
| `global.connectivity.proxy` | **Proxy** - Whether/how outgoing traffic is routed through proxy servers.|**Type:** `object`|
| `global.connectivity.proxy.enabled` | **Enable**|**Type:** `boolean`|
| `global.connectivity.proxy.httpProxy` | **HTTP proxy** - To be passed to the HTTP_PROXY environment variable in all hosts.|**Type:** `string`|
| `global.connectivity.proxy.httpsProxy` | **HTTPS proxy** - To be passed to the HTTPS_PROXY environment variable in all hosts.|**Type:** `string`|
| `global.connectivity.proxy.noProxy` | **No proxy** - To be passed to the NO_PROXY environment variable in all hosts.|**Type:** `string`|
| `global.connectivity.subnets` | **Subnets** - Subnets are created and tagged based on this definition.|**Type:** `array`**Default:** `[{&#34;cidrBlocks&#34;:[{&#34;availabilityZone&#34;:&#34;a&#34;,&#34;cidr&#34;:&#34;10.0.0.0/20&#34;},{&#34;availabilityZone&#34;:&#34;b&#34;,&#34;cidr&#34;:&#34;10.0.16.0/20&#34;},{&#34;availabilityZone&#34;:&#34;c&#34;,&#34;cidr&#34;:&#34;10.0.32.0/20&#34;}],&#34;isPublic&#34;:true},{&#34;cidrBlocks&#34;:[{&#34;availabilityZone&#34;:&#34;a&#34;,&#34;cidr&#34;:&#34;10.0.64.0/18&#34;},{&#34;availabilityZone&#34;:&#34;b&#34;,&#34;cidr&#34;:&#34;10.0.128.0/18&#34;},{&#34;availabilityZone&#34;:&#34;c&#34;,&#34;cidr&#34;:&#34;10.0.192.0/18&#34;}],&#34;isPublic&#34;:false}]`|
| `global.connectivity.subnets[*]` | **Subnet**|**Type:** `object`|
| `global.connectivity.subnets[*].cidrBlocks` | **Network**|**Type:** `array`|
| `global.connectivity.subnets[*].cidrBlocks[*]` |**None**|**Type:** `object`|
| `global.connectivity.subnets[*].cidrBlocks[*].availabilityZone` | **Availability zone**|**Type:** `string`|
| `global.connectivity.subnets[*].cidrBlocks[*].cidr` | **Address range** - IPv4 address range, in CIDR notation.|**Type:** `string`|
| `global.connectivity.subnets[*].cidrBlocks[*].tags` | **Tags** - AWS resource tags to assign to this subnet.|**Type:** `object`|
| `global.connectivity.subnets[*].cidrBlocks[*].tags.*` | **Tag value**|**Type:** `string`|
| `global.connectivity.subnets[*].id` | **ID of the subnet** - ID of an existing subnet. When set, this subnet will be used instead of creating a new one.|**Type:** `string`|
| `global.connectivity.subnets[*].isPublic` | **Public**|**Type:** `boolean`|
| `global.connectivity.subnets[*].natGatewayId` | **ID of the NAT Gateway** - ID of the NAT Gateway used for this existing subnet.|**Type:** `string`|
| `global.connectivity.subnets[*].routeTableId` | **ID of route table** - ID of the route table, assigned to the existing subnet. Must be provided when defining subnet via ID.|**Type:** `string`|
| `global.connectivity.subnets[*].tags` | **Tags** - AWS resource tags to assign to this CIDR block.|**Type:** `object`|
| `global.connectivity.subnets[*].tags.*` | **Tag value**|**Type:** `string`|
| `global.connectivity.topology` | **Topology** - Networking architecture between management cluster and workload cluster.|**Type:** `object`|
| `global.connectivity.topology.mode` | **Mode** - Valid values: GiantSwarmManaged, UserManaged, None.|**Type:** `string`**Default:** `&#34;None&#34;`|
| `global.connectivity.topology.prefixListId` | **Prefix list ID** - ID of the managed prefix list to use when the topology mode is set to &#39;UserManaged&#39;.|**Type:** `string`|
| `global.connectivity.topology.transitGatewayId` | **Transit gateway ID** - If the topology mode is set to &#39;UserManaged&#39;, this can be used to specify the transit gateway to use.|**Type:** `string`|
| `global.connectivity.vpcEndpointMode` | **VPC endpoint mode** - Who is reponsible for creation and management of VPC endpoints.|**Type:** `string`**Default:** `&#34;GiantSwarmManaged&#34;`|
| `global.connectivity.vpcMode` | **VPC mode** - Whether the cluser&#39;s VPC is created with public, internet facing resources (public subnets, NAT gateway) or not (private).|**Type:** `string`**Default:** `&#34;public&#34;`|

### Control plane
Properties within the `.global.controlPlane` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.controlPlane.additionalSecurityGroups` | **Control Plane additional security groups** - Additional security groups that will be added to the control plane nodes.|**Type:** `array`|
| `global.controlPlane.additionalSecurityGroups[*]` | **Security group**|**Type:** `object`|
| `global.controlPlane.additionalSecurityGroups[*].id` | **Id of the security group** - ID of the security group that will be added to the control plane nodes. The security group must exist.|**Type:** `string`|
| `global.controlPlane.apiExtraArgs` | **API extra arguments** - Extra arguments passed to the kubernetes API server.|**Type:** `object`|
| `global.controlPlane.apiExtraArgs.PATTERN` | **argument**|**Type:** `string`|
| `global.controlPlane.apiExtraCertSANs` | **API extra cert SANs** - Extra certs SANs passed to the kubeadmcontrolplane CR.|**Type:** `array`|
| `global.controlPlane.apiExtraCertSANs[*]` | **cert SAN**|**Type:** `string`|
| `global.controlPlane.apiMode` | **API mode** - Whether the Kubernetes API server load balancer should be reachable from the internet (public) or internal only (private).|**Type:** `string`**Default:** `&#34;public&#34;`|
| `global.controlPlane.apiServerPort` | **API server port** - The API server Load Balancer port. This option sets the Spec.ClusterNetwork.APIServerPort field on the Cluster CR. In CAPI this field isn&#39;t used currently. It is instead used in providers. In CAPA this sets only the public facing port of the Load Balancer. In CAPZ both the public facing and the destination port are set to this value. CAPV and CAPVCD do not use it.|**Type:** `integer`**Default:** `443`|
| `global.controlPlane.containerdVolumeSizeGB` | **Containerd volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `global.controlPlane.etcdVolumeSizeGB` | **Etcd volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `global.controlPlane.instanceType` | **EC2 instance type**|**Type:** `string`**Default:** `&#34;r6i.xlarge&#34;`|
| `global.controlPlane.kubeletVolumeSizeGB` | **Kubelet volume size (GB)**|**Type:** `integer`**Default:** `100`|
| `global.controlPlane.loadBalancerIngressAllowCidrBlocks` | **Load balancer allow list** - IPv4 address ranges that are allowed to connect to the control plane load balancer, in CIDR notation. When setting this field, remember to add the Management cluster Nat Gateway IPs provided by Giant Swarm so that the cluster can still be managed. These Nat Gateway IPs can be found in the Management Cluster AWSCluster &#39;.status.networkStatus.natGatewaysIPs&#39; field.|**Type:** `array`|
| `global.controlPlane.loadBalancerIngressAllowCidrBlocks[*]` | **Address range**|**Type:** `string`|
| `global.controlPlane.machineHealthCheck` | **Machine health check**|**Type:** `object`|
| `global.controlPlane.machineHealthCheck.enabled` | **Enable**|**Type:** `boolean`**Default:** `true`|
| `global.controlPlane.machineHealthCheck.maxUnhealthy` | **Maximum unhealthy nodes**|**Type:** `string`**Default:** `&#34;40%&#34;`|
| `global.controlPlane.machineHealthCheck.nodeStartupTimeout` | **Node startup timeout** - Determines how long a machine health check should wait for a node to join the cluster, before considering a machine unhealthy.|**Type:** `string`**Default:** `&#34;8m0s&#34;`|
| `global.controlPlane.machineHealthCheck.unhealthyNotReadyTimeout` | **Timeout for ready** - If a node is not in condition &#39;Ready&#39; after this timeout, it will be considered unhealthy.|**Type:** `string`**Default:** `&#34;10m0s&#34;`|
| `global.controlPlane.machineHealthCheck.unhealthyUnknownTimeout` | **Timeout for unknown condition** - If a node is in &#39;Unknown&#39; condition after this timeout, it will be considered unhealthy.|**Type:** `string`**Default:** `&#34;10m0s&#34;`|
| `global.controlPlane.oidc` | **OIDC authentication**|**Type:** `object`|
| `global.controlPlane.oidc.caPem` | **Certificate authority** - Identity provider&#39;s CA certificate in PEM format.|**Type:** `string`|
| `global.controlPlane.oidc.clientId` | **Client ID**|**Type:** `string`|
| `global.controlPlane.oidc.groupsClaim` | **Groups claim**|**Type:** `string`|
| `global.controlPlane.oidc.issuerUrl` | **Issuer URL** - Exact issuer URL that will be included in identity tokens.|**Type:** `string`|
| `global.controlPlane.oidc.usernameClaim` | **Username claim**|**Type:** `string`|
| `global.controlPlane.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`**Default:** `120`|
| `global.controlPlane.subnetTags` | **Subnet tags** - Tags to select AWS resources for the control plane by.|**Type:** `array`|
| `global.controlPlane.subnetTags[*]` | **Subnet tag**|**Type:** `object`|
| `global.controlPlane.subnetTags[*].*` | **Tag value**|**Type:** `string`|

### Internal
Properties within the `.internal` top-level object
For Giant Swarm internal use only, not stable, or not supported by UIs.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `internal.cgroupsv1` | **CGroups v1** - Force use of CGroups v1 for whole cluster.|**Type:** `boolean`**Default:** `false`|
| `internal.hashSalt` | **Hash salt** - If specified, this token is used as a salt to the hash suffix of some resource names. Can be used to force-recreate some resources.|**Type:** `string`|
| `internal.kubernetesVersion` | **Kubernetes version**|**Type:** `string`**Default:** `&#34;1.25.16&#34;`|
| `internal.migration` | **Migration values** - Section used for migration of cluster from vintage to CAPI|**Type:** `object`|
| `internal.migration.apiBindPort` | **Kubernetes API bind port** - Kubernetes API bind port used for kube api pod|**Type:** `integer`**Default:** `6443`|
| `internal.migration.controlPlaneExtraFiles` | **Control Plane extra files** - Additional fiels that will be provisioned to control-plane nodes, reference is from secret in the same namespace.|**Type:** `array`|
| `internal.migration.controlPlaneExtraFiles[*]` | **file**|**Type:** `object`|
| `internal.migration.controlPlaneExtraFiles[*].contentFrom` | **content from**|**Type:** `object`|
| `internal.migration.controlPlaneExtraFiles[*].contentFrom.secret` | **secret**|**Type:** `object`|
| `internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.key` | **secret key for file content**|**Type:** `string`|
| `internal.migration.controlPlaneExtraFiles[*].contentFrom.secret.name` | **secret name for file content**|**Type:** `string`|
| `internal.migration.controlPlaneExtraFiles[*].path` | **file path**|**Type:** `string`|
| `internal.migration.controlPlaneExtraFiles[*].permissions` | **file permissions in form 0644**|**Type:** `string`**Default:** `&#34;0644&#34;`|
| `internal.migration.controlPlanePostKubeadmCommands` | **Control Plane Post Kubeadm Commands** - Additional Post-Kubeadm Commands executed on the control plane node.|**Type:** `array`|
| `internal.migration.controlPlanePostKubeadmCommands[*]` | **command**|**Type:** `string`|
| `internal.migration.controlPlanePreKubeadmCommands` | **Control Plane Pre Kubeadm Commands** - Additional Pre-Kubeadm Commands executed on the control plane node.|**Type:** `array`|
| `internal.migration.controlPlanePreKubeadmCommands[*]` | **command**|**Type:** `string`|
| `internal.migration.etcdExtraArgs` | **Etcd extra arguments**|**Type:** `object`|
| `internal.migration.etcdExtraArgs.PATTERN` | **argument**|**Type:** `string`|
| `internal.migration.irsaAdditionalDomain` | **IRSA additional domain** - Additional domain to be added to IRSA trust relationship.|**Type:** `string`|
| `internal.nodePools` | **Default node pool**|**Type:** `object`**Default:** `{&#34;def00&#34;:{&#34;customNodeLabels&#34;:[&#34;label=default&#34;],&#34;instanceType&#34;:&#34;r6i.xlarge&#34;,&#34;maxSize&#34;:3,&#34;minSize&#34;:3}}`|
| `internal.nodePools.PATTERN` | **Node pool**|**Type:** `object`|
| `internal.nodePools.PATTERN.additionalSecurityGroups` | **Machine pool additional security groups** - Additional security groups that will be added to the machine pool nodes.|**Type:** `array`|
| `internal.nodePools.PATTERN.additionalSecurityGroups[*]` | **security group**|**Type:** `object`|
| `internal.nodePools.PATTERN.additionalSecurityGroups[*].id` | **Id of the security group** - ID of the security group that will be added to the machine pool nodes. The security group must exist.|**Type:** `string`|
| `internal.nodePools.PATTERN.availabilityZones` | **Availability zones**|**Type:** `array`|
| `internal.nodePools.PATTERN.availabilityZones[*]` | **Availability zone**|**Type:** `string`|
| `internal.nodePools.PATTERN.customNodeLabels` | **Custom node labels**|**Type:** `array`|
| `internal.nodePools.PATTERN.customNodeLabels[*]` | **Label**|**Type:** `string`|
| `internal.nodePools.PATTERN.customNodeTaints` | **Custom node taints**|**Type:** `array`|
| `internal.nodePools.PATTERN.customNodeTaints[*]` |**None**|**Type:** `object`|
| `internal.nodePools.PATTERN.customNodeTaints[*].effect` | **Effect**|**Type:** `string`|
| `internal.nodePools.PATTERN.customNodeTaints[*].key` | **Key**|**Type:** `string`|
| `internal.nodePools.PATTERN.customNodeTaints[*].value` | **Value**|**Type:** `string`|
| `internal.nodePools.PATTERN.instanceType` | **EC2 instance type**|**Type:** `string`|
| `internal.nodePools.PATTERN.instanceTypeOverrides` | **Instance type overrides** - Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/|**Type:** `array`**Default:** `[]`|
| `internal.nodePools.PATTERN.instanceTypeOverrides[*]` | **EC2 instance type**|**Type:** `string`|
| `internal.nodePools.PATTERN.maxSize` | **Maximum number of nodes**|**Type:** `integer`|
| `internal.nodePools.PATTERN.minSize` | **Minimum number of nodes**|**Type:** `integer`|
| `internal.nodePools.PATTERN.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`|
| `internal.nodePools.PATTERN.spotInstances` | **Spot instances** - Compared to on-demand instances, spot instances can help you save cost.|**Type:** `object`|
| `internal.nodePools.PATTERN.spotInstances.enabled` | **Enable**|**Type:** `boolean`**Default:** `false`|
| `internal.nodePools.PATTERN.spotInstances.maxPrice` | **Maximum price to pay per instance per hour, in USD.**|**Type:** `number`|
| `internal.nodePools.PATTERN.subnetTags` | **Subnet tags** - Tags to filter which AWS subnets will be used for this node pool.|**Type:** `array`|
| `internal.nodePools.PATTERN.subnetTags[*]` | **Subnet tag**|**Type:** `object`|
| `internal.nodePools.PATTERN.subnetTags[*].*` | **Tag value**|**Type:** `string`|
| `internal.sandboxContainerImage` | **Sandbox image** - The image used by sandbox / pause container|**Type:** `object`|
| `internal.sandboxContainerImage.name` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm/pause&#34;`|
| `internal.sandboxContainerImage.registry` | **Registry**|**Type:** `string`**Default:** `&#34;gsoci.azurecr.io&#34;`|
| `internal.sandboxContainerImage.tag` | **Tag**|**Type:** `string`**Default:** `&#34;3.9&#34;`|
| `internal.teleport` | **Teleport**|**Type:** `object`|
| `internal.teleport.enabled` | **Enable teleport**|**Type:** `boolean`**Default:** `true`|
| `internal.teleport.proxyAddr` | **Teleport proxy address**|**Type:** `string`**Default:** `&#34;teleport.giantswarm.io:443&#34;`|
| `internal.teleport.version` | **Teleport version**|**Type:** `string`**Default:** `&#34;14.1.3&#34;`|

### Kubectl image
Properties within the `.kubectlImage` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` | **Repository**|**Type:** `string`**Default:** `&#34;giantswarm/kubectl&#34;`|
| `kubectlImage.registry` | **Registry**|**Type:** `string`**Default:** `&#34;gsoci.azurecr.io&#34;`|
| `kubectlImage.tag` | **Tag**|**Type:** `string`**Default:** `&#34;1.23.5&#34;`|

### Metadata
Properties within the `.global.metadata` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.metadata.description` | **Cluster description** - User-friendly description of the cluster&#39;s purpose.|**Type:** `string`|
| `global.metadata.name` | **Cluster name** - Unique identifier, cannot be changed after creation.|**Type:** `string`|
| `global.metadata.organization` | **Organization**|**Type:** `string`|
| `global.metadata.preventDeletion` | **Prevent cluster deletion**|**Type:** `boolean`**Default:** `false`|
| `global.metadata.servicePriority` | **Service priority** - The relative importance of this cluster.|**Type:** `string`**Default:** `&#34;highest&#34;`|

### Node pools
Properties within the `.global.nodePools` object
Node pools of the cluster. If not specified, this defaults to the value of `internal.nodePools`.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.nodePools.PATTERN` | **Node pool**|**Type:** `object`|
| `global.nodePools.PATTERN.additionalSecurityGroups` | **Machine pool additional security groups** - Additional security groups that will be added to the machine pool nodes.|**Type:** `array`|
| `global.nodePools.PATTERN.additionalSecurityGroups[*]` | **security group**|**Type:** `object`|
| `global.nodePools.PATTERN.additionalSecurityGroups[*].id` | **Id of the security group** - ID of the security group that will be added to the machine pool nodes. The security group must exist.|**Type:** `string`|
| `global.nodePools.PATTERN.availabilityZones` | **Availability zones**|**Type:** `array`|
| `global.nodePools.PATTERN.availabilityZones[*]` | **Availability zone**|**Type:** `string`|
| `global.nodePools.PATTERN.customNodeLabels` | **Custom node labels**|**Type:** `array`|
| `global.nodePools.PATTERN.customNodeLabels[*]` | **Label**|**Type:** `string`|
| `global.nodePools.PATTERN.customNodeTaints` | **Custom node taints**|**Type:** `array`|
| `global.nodePools.PATTERN.customNodeTaints[*]` |**None**|**Type:** `object`|
| `global.nodePools.PATTERN.customNodeTaints[*].effect` | **Effect**|**Type:** `string`|
| `global.nodePools.PATTERN.customNodeTaints[*].key` | **Key**|**Type:** `string`|
| `global.nodePools.PATTERN.customNodeTaints[*].value` | **Value**|**Type:** `string`|
| `global.nodePools.PATTERN.instanceType` | **EC2 instance type**|**Type:** `string`|
| `global.nodePools.PATTERN.instanceTypeOverrides` | **Instance type overrides** - Ordered list of instance types to be used for the machine pool. The first instance type that is available in the region will be used. Read more in our docs https://docs.giantswarm.io/advanced/cluster-management/node-pools-capi/|**Type:** `array`**Default:** `[]`|
| `global.nodePools.PATTERN.instanceTypeOverrides[*]` | **EC2 instance type**|**Type:** `string`|
| `global.nodePools.PATTERN.maxSize` | **Maximum number of nodes**|**Type:** `integer`|
| `global.nodePools.PATTERN.minSize` | **Minimum number of nodes**|**Type:** `integer`|
| `global.nodePools.PATTERN.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`|
| `global.nodePools.PATTERN.spotInstances` | **Spot instances** - Compared to on-demand instances, spot instances can help you save cost.|**Type:** `object`|
| `global.nodePools.PATTERN.spotInstances.enabled` | **Enable**|**Type:** `boolean`**Default:** `false`|
| `global.nodePools.PATTERN.spotInstances.maxPrice` | **Maximum price to pay per instance per hour, in USD.**|**Type:** `number`|
| `global.nodePools.PATTERN.subnetTags` | **Subnet tags** - Tags to filter which AWS subnets will be used for this node pool.|**Type:** `array`|
| `global.nodePools.PATTERN.subnetTags[*]` | **Subnet tag**|**Type:** `object`|
| `global.nodePools.PATTERN.subnetTags[*].*` | **Tag value**|**Type:** `string`|

### Other global

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.managementCluster` | **Management cluster** - Name of the Cluster API cluster managing this workload cluster.|**Type:** `string`|

### Pod Security Standards
Properties within the `.global.podSecurityStandards` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.podSecurityStandards.enforced` | **Enforced**|**Type:** `boolean`**Default:** `true`|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `baseDomain` | **Base DNS domain**|**Type:** `string`|
| `cluster` | **Cluster** - Helm values for the provider-independent cluster chart|**Type:** `object`**Default:** `{&#34;providerIntegration&#34;:{&#34;clusterAnnotationsTemplateName&#34;:&#34;awsConnectivityLabels&#34;,&#34;components&#34;:{&#34;systemd&#34;:{&#34;timesyncd&#34;:{&#34;ntp&#34;:[&#34;169.254.169.123&#34;]}}},&#34;connectivity&#34;:{&#34;proxy&#34;:{&#34;noProxy&#34;:{&#34;templateName&#34;:&#34;awsNoProxyList&#34;,&#34;value&#34;:[&#34;elb.amazonaws.com&#34;,&#34;169.254.169.254&#34;]}}},&#34;controlPlane&#34;:{&#34;kubeadmConfig&#34;:{&#34;clusterConfiguration&#34;:{&#34;apiServer&#34;:{&#34;apiAudiences&#34;:{&#34;templateName&#34;:&#34;awsApiServerApiAudiences&#34;},&#34;featureGates&#34;:[{&#34;enabled&#34;:true,&#34;name&#34;:&#34;CronJobTimeZone&#34;}],&#34;serviceAccountIssuer&#34;:{&#34;clusterDomainPrefix&#34;:&#34;irsa&#34;}}},&#34;ignition&#34;:{&#34;containerLinuxConfig&#34;:{&#34;additionalConfig&#34;:{&#34;storage&#34;:{&#34;filesystems&#34;:[{&#34;mount&#34;:{&#34;device&#34;:&#34;/dev/xvdc&#34;,&#34;format&#34;:&#34;xfs&#34;,&#34;label&#34;:&#34;etcd&#34;,&#34;wipeFilesystem&#34;:true},&#34;name&#34;:&#34;etcd&#34;},{&#34;mount&#34;:{&#34;device&#34;:&#34;/dev/xvdd&#34;,&#34;format&#34;:&#34;xfs&#34;,&#34;label&#34;:&#34;containerd&#34;,&#34;wipeFilesystem&#34;:true},&#34;name&#34;:&#34;containerd&#34;},{&#34;mount&#34;:{&#34;device&#34;:&#34;/dev/xvde&#34;,&#34;format&#34;:&#34;xfs&#34;,&#34;label&#34;:&#34;kubelet&#34;,&#34;wipeFilesystem&#34;:true},&#34;name&#34;:&#34;kubelet&#34;}]},&#34;systemd&#34;:{&#34;units&#34;:[{&#34;contents&#34;:{&#34;install&#34;:{&#34;wantedBy&#34;:[&#34;local-fs-pre.target&#34;]},&#34;mount&#34;:{&#34;type&#34;:&#34;xfs&#34;,&#34;what&#34;:&#34;/dev/disk/by-label/etcd&#34;,&#34;where&#34;:&#34;/var/lib/etcd&#34;},&#34;unit&#34;:{&#34;defaultDependencies&#34;:false,&#34;description&#34;:&#34;etcd volume&#34;}},&#34;enabled&#34;:true,&#34;name&#34;:&#34;var-lib-etcd.mount&#34;},{&#34;contents&#34;:{&#34;install&#34;:{&#34;wantedBy&#34;:[&#34;local-fs-pre.target&#34;]},&#34;mount&#34;:{&#34;type&#34;:&#34;xfs&#34;,&#34;what&#34;:&#34;/dev/disk/by-label/kubelet&#34;,&#34;where&#34;:&#34;/var/lib/kubelet&#34;},&#34;unit&#34;:{&#34;defaultDependencies&#34;:false,&#34;description&#34;:&#34;kubelet volume&#34;}},&#34;enabled&#34;:true,&#34;name&#34;:&#34;var-lib-kubelet.mount&#34;},{&#34;contents&#34;:{&#34;install&#34;:{&#34;wantedBy&#34;:[&#34;local-fs-pre.target&#34;]},&#34;mount&#34;:{&#34;type&#34;:&#34;xfs&#34;,&#34;what&#34;:&#34;/dev/disk/by-label/containerd&#34;,&#34;where&#34;:&#34;/var/lib/containerd&#34;},&#34;unit&#34;:{&#34;defaultDependencies&#34;:false,&#34;description&#34;:&#34;containerd volume&#34;}},&#34;enabled&#34;:true,&#34;name&#34;:&#34;var-lib-containerd.mount&#34;}]}}}}},&#34;resources&#34;:{&#34;infrastructureMachineTemplate&#34;:{&#34;group&#34;:&#34;infrastructure.cluster.x-k8s.io&#34;,&#34;kind&#34;:&#34;AWSMachineTemplate&#34;,&#34;version&#34;:&#34;v1beta1&#34;},&#34;infrastructureMachineTemplateSpecTemplateName&#34;:&#34;controlplane-awsmachinetemplate-spec&#34;}},&#34;pauseProperties&#34;:{&#34;global.connectivity.vpcMode&#34;:&#34;private&#34;},&#34;provider&#34;:&#34;aws&#34;,&#34;resourcesApi&#34;:{&#34;bastionResourceEnabled&#34;:false,&#34;clusterResourceEnabled&#34;:true,&#34;controlPlaneResourceEnabled&#34;:true,&#34;infrastructureCluster&#34;:{&#34;group&#34;:&#34;infrastructure.cluster.x-k8s.io&#34;,&#34;kind&#34;:&#34;AWSCluster&#34;,&#34;version&#34;:&#34;v1beta1&#34;},&#34;machineHealthCheckResourceEnabled&#34;:false,&#34;machinePoolResourcesEnabled&#34;:false,&#34;nodePoolKind&#34;:&#34;MachinePool&#34;}}}`|
| `cluster-shared` | **Library chart**|**Type:** `object`|
| `managementCluster` | **Management cluster** - Name of the Cluster API cluster managing this workload cluster.|**Type:** `string`|
| `provider` | **Cluster API provider name**|**Type:** `string`|






## Further reading

- [Source repository](https://github.com/giantswarm/cluster-aws)
