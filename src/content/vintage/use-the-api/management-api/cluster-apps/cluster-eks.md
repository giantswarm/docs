---
title: Cluster-Eks chart reference
linkTitle: cluster-eks chart reference
description: |
  A helm chart for creating Cluster API EKS clusters with the AWS infrastructure provider (CAPA).
weight: 100
menu:
  main:
    identifier: cluster-eks
    parent: uiapi-cluster-apps
layout: cluster-app
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-eks
source_repository_ref: v0.12.0
---

The `cluster-eks` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API EKS cluster.

# Values schema documentation

This page lists all available configuration options, based on the [configuration values schema](values.schema.json).

Note that configuration options can change between releases. Use the GitHub function for selecting a branch/tag to view the documentation matching your cluster-eks version.

&lt;!-- Update the content below by executing (from the repo root directory)

schemadocs generate helm/cluster-eks/values.schema.json -o helm/cluster-eks/README.md

--&gt;

&lt;!-- DOCS_START --&gt;

### AWS settings
Properties within the `.global.providerSpecific` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.providerSpecific.additionalResourceTags` | **Additional resource tags** - Additional tags to add to AWS resources created by the cluster.|**Type:** `object`&lt;br/&gt;|
| `global.providerSpecific.additionalResourceTags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `global.providerSpecific.ami` | **Amazon machine image (AMI)** - If specified, this image will be used to provision EC2 instances.|**Type:** `string`&lt;br/&gt;|
| `global.providerSpecific.awsAccountId` | **AWS account ID** - AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[0-9]{0,12}$`&lt;br/&gt;**Default:** `&#34;&#34;`|
| `global.providerSpecific.awsClusterRoleIdentityName` | **Cluster role identity name** - Name of an AWSClusterRoleIdentity object. This in turn refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account. Note: This name does not refer directly to an IAM role name/ARN.|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[-a-zA-Z0-9_\.]{1,63}$`&lt;br/&gt;**Default:** `&#34;default&#34;`|
| `global.providerSpecific.region` | **Region**|**Type:** `string`&lt;br/&gt;|

### Connectivity
Properties within the `.global.connectivity` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.connectivity.availabilityZoneUsageLimit` | **Availability zones** - Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets.|**Type:** `integer`&lt;br/&gt;**Default:** `3`|
| `global.connectivity.baseDomain` | **Base DNS domain**|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.network` | **Network**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.network.pods` | **Pods**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.network.pods.cidrBlocks` | **Pod subnets**|**Type:** `array`&lt;br/&gt;**Default:** `[&#34;100.64.0.0/16&#34;]`|
| `global.connectivity.network.pods.cidrBlocks[*]` | **Pod subnet** - IPv4 address range for pods, in CIDR notation. Must be within the 100.64.0.0/10 or 198.19.0.0/16 range. The CIDR block size must be betwen /16 and /28.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;100.64.0.0/16&#34;`&lt;br/&gt;|
| `global.connectivity.network.services` | **Services**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.network.services.cidrBlocks` | **K8s Service subnets**|**Type:** `array`&lt;br/&gt;**Default:** `[&#34;172.31.0.0/16&#34;]`|
| `global.connectivity.network.services.cidrBlocks[*]` | **Service subnet** - IPv4 address range for kubernetes services, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Example:** `&#34;172.31.0.0/16&#34;`&lt;br/&gt;|
| `global.connectivity.network.vpcCidr` | **VPC subnet** - IPv4 address range to assign to this cluster&#39;s VPC, in CIDR notation.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;10.0.0.0/16&#34;`|
| `global.connectivity.podSubnets` | **Pod Subnets** - Pod Subnets are created and tagged based on this definition.|**Type:** `array`&lt;br/&gt;**Default:** `[{&#34;cidrBlocks&#34;:[{&#34;availabilityZone&#34;:&#34;a&#34;,&#34;cidr&#34;:&#34;100.64.0.0/18&#34;,&#34;tags&#34;:{&#34;sigs.k8s.io/cluster-api-provider-aws/association&#34;:&#34;secondary&#34;}},{&#34;availabilityZone&#34;:&#34;b&#34;,&#34;cidr&#34;:&#34;100.64.64.0/18&#34;,&#34;tags&#34;:{&#34;sigs.k8s.io/cluster-api-provider-aws/association&#34;:&#34;secondary&#34;}},{&#34;availabilityZone&#34;:&#34;c&#34;,&#34;cidr&#34;:&#34;100.64.128.0/18&#34;,&#34;tags&#34;:{&#34;sigs.k8s.io/cluster-api-provider-aws/association&#34;:&#34;secondary&#34;}}]}]`|
| `global.connectivity.podSubnets[*]` | **Subnet**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks` | **Network**|**Type:** `array`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks[*].availabilityZone` | **Availability zone**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;a&#34;`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks[*].cidr` | **Address range** - IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks[*].tags` | **Tags** - AWS resource tags to assign to this subnet.|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].cidrBlocks[*].tags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].tags` | **Tags** - AWS resource tags to assign to this CIDR block.|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.podSubnets[*].tags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `global.connectivity.proxy` | **Proxy** - Whether/how outgoing traffic is routed through proxy servers.|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.proxy.enabled` | **Enable**|**Type:** `boolean`&lt;br/&gt;|
| `global.connectivity.proxy.httpProxy` | **HTTP proxy** - To be passed to the HTTP_PROXY environment variable in all hosts.|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.proxy.httpsProxy` | **HTTPS proxy** - To be passed to the HTTPS_PROXY environment variable in all hosts.|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.proxy.noProxy` | **No proxy** - To be passed to the NO_PROXY environment variable in all hosts.|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.subnets` | **Subnets** - Subnets are created and tagged based on this definition.|**Type:** `array`&lt;br/&gt;**Default:** `[{&#34;cidrBlocks&#34;:[{&#34;availabilityZone&#34;:&#34;a&#34;,&#34;cidr&#34;:&#34;10.0.0.0/20&#34;},{&#34;availabilityZone&#34;:&#34;b&#34;,&#34;cidr&#34;:&#34;10.0.16.0/20&#34;},{&#34;availabilityZone&#34;:&#34;c&#34;,&#34;cidr&#34;:&#34;10.0.32.0/20&#34;}],&#34;isPublic&#34;:true},{&#34;cidrBlocks&#34;:[{&#34;availabilityZone&#34;:&#34;a&#34;,&#34;cidr&#34;:&#34;10.0.64.0/18&#34;},{&#34;availabilityZone&#34;:&#34;b&#34;,&#34;cidr&#34;:&#34;10.0.128.0/18&#34;},{&#34;availabilityZone&#34;:&#34;c&#34;,&#34;cidr&#34;:&#34;10.0.192.0/18&#34;}],&#34;isPublic&#34;:false}]`|
| `global.connectivity.subnets[*]` | **Subnet**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks` | **Network**|**Type:** `array`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks[*]` |**None**|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks[*].availabilityZone` | **Availability zone**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;a&#34;`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks[*].cidr` | **Address range** - IPv4 address range, in CIDR notation.|**Type:** `string`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks[*].tags` | **Tags** - AWS resource tags to assign to this subnet.|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.subnets[*].cidrBlocks[*].tags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `global.connectivity.subnets[*].isPublic` | **Public**|**Type:** `boolean`&lt;br/&gt;|
| `global.connectivity.subnets[*].tags` | **Tags** - AWS resource tags to assign to this CIDR block.|**Type:** `object`&lt;br/&gt;|
| `global.connectivity.subnets[*].tags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|

### Control plane
Properties within the `.global.controlPlane` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.controlPlane.apiMode` | **API mode** - Whether the Kubernetes API server load balancer should be reachable from the internet (public) or internal only (private).|**Type:** `string`&lt;br/&gt;**Default:** `&#34;public&#34;`|
| `global.controlPlane.logging` | **Logging**|**Type:** `object`&lt;br/&gt;|
| `global.controlPlane.logging.apiServer` | **Api Server** - Enable or disable Api server logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `global.controlPlane.logging.audit` | **Audit** - Enable or disable audit logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `global.controlPlane.logging.authenticator` | **Authenticator** - Enable or disable IAM Authenticator logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `global.controlPlane.logging.controllerManager` | **Controller Manager** - Enable or disable Controller Manager logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).|**Type:** `boolean`&lt;br/&gt;**Default:** `true`|
| `global.controlPlane.oidcIdentityProviderConfig` | **OIDC identity provider config** - OIDC identity provider configuration for the Kubernetes API server.|**Type:** `object`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.clientId` | **Client ID** - Client ID of the OIDC identity provider.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.groupsClaim` | **Groups claim** - Claim to use for mapping groups.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.groupsPrefix` | **Groups prefix** - Prefix to use for mapping groups.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.identityProviderConfigName` | **Identity provider config name** - Name of the OIDC identity provider config.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.issuerUrl` | **Issuer URL** - URL of the OIDC identity provider.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.requiredClaims` | **Required claims** - Required claims for the OIDC identity provider.|**Type:** `object`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.requiredClaims.*` | **Claim**|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.tags` | **Tags** - AWS resource tags to assign to the IAM OIDC provider.|**Type:** `object`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.tags.*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.usernameClaim` | **Username claim** - Claim to use for mapping usernames.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.oidcIdentityProviderConfig.usernamePrefix` | **Username prefix** - Prefix to use for mapping usernames.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.roleMapping` | **Role mappings**|**Type:** `array`&lt;br/&gt;|
| `global.controlPlane.roleMapping[*]` | **Role mapping** - Maps AWS IAM role to Kubernetes role.|**Type:** `object`&lt;br/&gt;|
| `global.controlPlane.roleMapping[*].groups` | **Groups** - Kubernetes groups.|**Type:** `array`&lt;br/&gt;|
| `global.controlPlane.roleMapping[*].groups[*]` | **Group** - Kubernetes group, for example `system:masters`.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.roleMapping[*].rolearn` | **AWS Role ARN** - Full ARN of the AWS IAM role.|**Type:** `string`&lt;br/&gt;|
| `global.controlPlane.roleMapping[*].username` | **Kubernetes username** - Kubernetes username, for example `cluster-admin`.|**Type:** `string`&lt;br/&gt;|

### Internal
Properties within the `.internal` top-level object
For Giant Swarm internal use only, not stable, or not supported by UIs.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `internal.hashSalt` | **Hash salt** - If specified, this token is used as a salt to the hash suffix of some resource names. Can be used to force-recreate some resources.|**Type:** `string`&lt;br/&gt;|
| `internal.kubernetesVersion` | **Kubernetes version**|**Type:** `string`&lt;br/&gt;**Example:** `&#34;1.24.7&#34;`&lt;br/&gt;**Default:** `&#34;1.24.10&#34;`|
| `internal.nodePools` | **Default node pool**|**Type:** `object`&lt;br/&gt;**Default:** `{&#34;def00&#34;:{&#34;customNodeLabels&#34;:[&#34;label=default&#34;],&#34;instanceType&#34;:&#34;r6i.xlarge&#34;,&#34;maxSize&#34;:4,&#34;minSize&#34;:3}}`|
| `internal.nodePools.PATTERN` | **Node pool**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.availabilityZones` | **Availability zones**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.availabilityZones[*]` | **Availability zone**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeLabels` | **Custom node labels**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeLabels[*]` | **Label**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeTaints` | **Custom node taints**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeTaints[*]` |**None**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeTaints[*].effect` | **Effect**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeTaints[*].key` | **Key**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.customNodeTaints[*].value` | **Value**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.instanceType` | **EC2 instance type**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.maxSize` | **Maximum number of nodes**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.minSize` | **Minimum number of nodes**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.subnetTags` | **Subnet tags** - Tags to filter which AWS subnets will be used for this node pool.|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.subnetTags[*]` | **Subnet tag**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `internal.nodePools.PATTERN.subnetTags[*].*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|
| `internal.sandboxContainerImage` | **Kubectl image**|**Type:** `object`&lt;br/&gt;|
| `internal.sandboxContainerImage.name` | **Repository**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;giantswarm/pause&#34;`|
| `internal.sandboxContainerImage.registry` | **Registry**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;quay.io&#34;`|
| `internal.sandboxContainerImage.tag` | **Tag**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;3.9&#34;`|

### Kubectl image
Properties within the `.kubectlImage` top-level object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `kubectlImage.name` | **Repository**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;giantswarm/kubectl&#34;`|
| `kubectlImage.registry` | **Registry**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;quay.io&#34;`|
| `kubectlImage.tag` | **Tag**|**Type:** `string`&lt;br/&gt;**Default:** `&#34;1.23.5&#34;`|

### Metadata
Properties within the `.global.metadata` object

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.metadata.description` | **Cluster description** - User-friendly description of the cluster&#39;s purpose.|**Type:** `string`&lt;br/&gt;|
| `global.metadata.name` | **Cluster name** - Unique identifier, cannot be changed after creation.|**Type:** `string`&lt;br/&gt;|
| `global.metadata.organization` | **Organization**|**Type:** `string`&lt;br/&gt;|
| `global.metadata.preventDeletion` | **Prevent cluster deletion**|**Type:** `boolean`&lt;br/&gt;**Default:** `false`|
| `global.metadata.servicePriority` | **Service priority** - The relative importance of this cluster.|**Type:** `string`&lt;br/&gt;**Default:** `&#34;highest&#34;`|

### Node pools
Properties within the `.global.nodePools` object
Node pools of the cluster. If not specified, this defaults to the value of `internal.nodePools`.

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.nodePools.PATTERN` | **Node pool**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.availabilityZones` | **Availability zones**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.availabilityZones[*]` | **Availability zone**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeLabels` | **Custom node labels**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeLabels[*]` | **Label**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeTaints` | **Custom node taints**|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeTaints[*]` |**None**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeTaints[*].effect` | **Effect**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeTaints[*].key` | **Key**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.customNodeTaints[*].value` | **Value**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.instanceType` | **EC2 instance type**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.maxSize` | **Maximum number of nodes**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.minSize` | **Minimum number of nodes**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.rootVolumeSizeGB` | **Root volume size (GB)**|**Type:** `integer`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.subnetTags` | **Subnet tags** - Tags to filter which AWS subnets will be used for this node pool.|**Type:** `array`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.subnetTags[*]` | **Subnet tag**|**Type:** `object`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;|
| `global.nodePools.PATTERN.subnetTags[*].*` | **Tag value**|**Type:** `string`&lt;br/&gt;**Key pattern:**&lt;br/&gt;`PATTERN`=`^[a-z0-9][-a-z0-9]{3,18}[a-z0-9]$`&lt;br/&gt;**Value pattern:** `^[ a-zA-Z0-9\._:/=&#43;-@]&#43;$`&lt;br/&gt;|

### Other global

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `global.managementCluster` | **Management cluster** - Name of the Cluster API cluster managing this workload cluster.|**Type:** `string`&lt;br/&gt;|

### Other

| **Property** | **Description** | **More Details** |
| :----------- | :-------------- | :--------------- |
| `baseDomain` | **Base DNS domain**|**Type:** `string`&lt;br/&gt;|
| `cluster-shared` | **Library chart**|**Type:** `object`&lt;br/&gt;|
| `managementCluster` | **Management cluster** - Name of the Cluster API cluster managing this workload cluster.|**Type:** `string`&lt;br/&gt;|
| `provider` | **Cluster API provider name**|**Type:** `string`&lt;br/&gt;|



&lt;!-- DOCS_END --&gt;


## Further reading

- [Source repository](https://github.com/giantswarm/cluster-eks)
