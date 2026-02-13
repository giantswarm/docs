---
title: cluster-eks chart reference
linkTitle: cluster-eks
description:  A helm chart for creating Cluster API EKS clusters with the AWS infrastructure provider (CAPA).; Check here the different properties of the chart.
weight: 100
menu:
  principal:
    identifier: cluster-eks
    parent: reference-cluster-apps
layout: cluster-app
user_questions:
 - What properties can I configure for cluster-eks?
owner:
- https://github.com/orgs/giantswarm/teams/team-phoenix
source_repository: https://github.com/giantswarm/cluster-eks
source_repository_ref: v0.12.0
---

The `cluster-eks` chart templates all the AWS infrastructure resources that are necessary to create a Cluster API EKS cluster.

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

`.global.providerSpecific.awsAccountId`

**Type:** `string`

**AWS account ID**

AWS Account ID of the AWSClusterRoleIdentity IAM role, recommendation is to leave this value empty as it will be automatically calculated. This value is needed for tests.

**Value pattern:** `^[0-9]{0,12}$`

**Default:** `""`

---

`.global.providerSpecific.awsClusterRoleIdentityName`

**Type:** `string`

**Cluster role identity name**

Name of an AWSClusterRoleIdentity object. This in turn refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account. Note: This name does not refer directly to an IAM role name/ARN.

**Value pattern:** `^[-a-zA-Z0-9_\.]{1,63}$`

**Default:** `"default"`

---

`.global.providerSpecific.region`

**Type:** `string`

**Region**

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

**Default:** `["100.64.0.0/16"]`

---

`.global.connectivity.network.pods.cidrBlocks[*]`

**Type:** `string`

**Pod subnet**

IPv4 address range for pods, in CIDR notation. Must be within the 100.64.0.0/10 or 198.19.0.0/16 range. The CIDR block size must be betwen /16 and /28.

**Example:** `"100.64.0.0/16"`

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

**Allowed value:** `172.31.0.0/16`

---

`.global.connectivity.network.vpcCidr`

**Type:** `string`

**VPC subnet**

IPv4 address range to assign to this cluster's VPC, in CIDR notation.

**Default:** `"10.0.0.0/16"`

---

`.global.connectivity.podSubnets`

**Type:** `array`

**Pod Subnets**

Pod Subnets are created and tagged based on this definition.

**Default:** `[{"cidrBlocks":[{"availabilityZone":"a","cidr":"100.64.0.0/18","tags":{"sigs.k8s.io/cluster-api-provider-aws/association":"secondary"}},{"availabilityZone":"b","cidr":"100.64.64.0/18","tags":{"sigs.k8s.io/cluster-api-provider-aws/association":"secondary"}},{"availabilityZone":"c","cidr":"100.64.128.0/18","tags":{"sigs.k8s.io/cluster-api-provider-aws/association":"secondary"}}]}]`

---

`.global.connectivity.podSubnets[*]`

**Type:** `object`

**Subnet**

---

`.global.connectivity.podSubnets[*].cidrBlocks`

**Type:** `array`

**Network**

---

`.global.connectivity.podSubnets[*].cidrBlocks[*]`

**Type:** `object`

---

`.global.connectivity.podSubnets[*].cidrBlocks[*].availabilityZone`

**Type:** `string`

**Availability zone**

**Example:** `"a"`

---

`.global.connectivity.podSubnets[*].cidrBlocks[*].cidr`

**Type:** `string`

**Address range**

IPv4 address range, in CIDR notation.

---

`.global.connectivity.podSubnets[*].cidrBlocks[*].tags`

**Type:** `object`

**Tags**

AWS resource tags to assign to this subnet.

---

`.global.connectivity.podSubnets[*].cidrBlocks[*].tags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.global.connectivity.podSubnets[*].tags`

**Type:** `object`

**Tags**

AWS resource tags to assign to this CIDR block.

---

`.global.connectivity.podSubnets[*].tags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

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

`.global.connectivity.subnets[*].isPublic`

**Type:** `boolean`

**Public**

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

### Control plane {#control-plane}

---

`.global.controlPlane.apiMode`

**Type:** `string`

**API mode**

Whether the Kubernetes API server load balancer should be reachable from the internet (public) or internal only (private).

**Allowed values:** `public`, `private`

**Default:** `"public"`

---

`.global.controlPlane.logging`

**Type:** `object`

**Logging**

---

`.global.controlPlane.logging.apiServer`

**Type:** `boolean`

**Api Server**

Enable or disable Api server logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).

**Default:** `true`

---

`.global.controlPlane.logging.audit`

**Type:** `boolean`

**Audit**

Enable or disable audit logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).

**Default:** `true`

---

`.global.controlPlane.logging.authenticator`

**Type:** `boolean`

**Authenticator**

Enable or disable IAM Authenticator logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).

**Default:** `true`

---

`.global.controlPlane.logging.controllerManager`

**Type:** `boolean`

**Controller Manager**

Enable or disable Controller Manager logging to CloudWatch (https://docs.aws.amazon.com/eks/latest/userguide/control-plane-logs.html).

**Default:** `true`

---

`.global.controlPlane.oidcIdentityProviderConfig`

**Type:** `object`

**OIDC identity provider config**

OIDC identity provider configuration for the Kubernetes API server.

---

`.global.controlPlane.oidcIdentityProviderConfig.clientId`

**Type:** `string`

**Client ID**

Client ID of the OIDC identity provider.

---

`.global.controlPlane.oidcIdentityProviderConfig.groupsClaim`

**Type:** `string`

**Groups claim**

Claim to use for mapping groups.

---

`.global.controlPlane.oidcIdentityProviderConfig.groupsPrefix`

**Type:** `string`

**Groups prefix**

Prefix to use for mapping groups.

---

`.global.controlPlane.oidcIdentityProviderConfig.identityProviderConfigName`

**Type:** `string`

**Identity provider config name**

Name of the OIDC identity provider config.

---

`.global.controlPlane.oidcIdentityProviderConfig.issuerUrl`

**Type:** `string`

**Issuer URL**

URL of the OIDC identity provider.

---

`.global.controlPlane.oidcIdentityProviderConfig.requiredClaims`

**Type:** `object`

**Required claims**

Required claims for the OIDC identity provider.

---

`.global.controlPlane.oidcIdentityProviderConfig.requiredClaims.*`

**Type:** `string`

**Claim**

---

`.global.controlPlane.oidcIdentityProviderConfig.tags`

**Type:** `object`

**Tags**

AWS resource tags to assign to the IAM OIDC provider.

---

`.global.controlPlane.oidcIdentityProviderConfig.tags.*`

**Type:** `string`

**Tag value**

**Value pattern:** `^[ a-zA-Z0-9\._:/=+-@]+$`

---

`.global.controlPlane.oidcIdentityProviderConfig.usernameClaim`

**Type:** `string`

**Username claim**

Claim to use for mapping usernames.

---

`.global.controlPlane.oidcIdentityProviderConfig.usernamePrefix`

**Type:** `string`

**Username prefix**

Prefix to use for mapping usernames.

---

`.global.controlPlane.roleMapping`

**Type:** `array`

**Role mappings**

---

`.global.controlPlane.roleMapping[*]`

**Type:** `object`

**Role mapping**

Maps AWS IAM role to Kubernetes role.

---

`.global.controlPlane.roleMapping[*].groups`

**Type:** `array`

**Groups**

Kubernetes groups.

---

`.global.controlPlane.roleMapping[*].groups[*]`

**Type:** `string`

**Group**

Kubernetes group, for example `system:masters`.

---

`.global.controlPlane.roleMapping[*].rolearn`

**Type:** `string`

**AWS Role ARN**

Full ARN of the AWS IAM role.

---

`.global.controlPlane.roleMapping[*].username`

**Type:** `string`

**Kubernetes username**

Kubernetes username, for example `cluster-admin`.

### Internal {#internal}For Giant Swarm internal use only, not stable, or not supported by UIs.

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

**Default:** `"1.24.10"`

---

`.internal.nodePools`

**Type:** `object`

**Default node pool**

**Default:** `{"def00":{"customNodeLabels":["label=default"],"instanceType":"r6i.xlarge","maxSize":4,"minSize":3}}`

---

`.internal.nodePools.PATTERN`

**Type:** `object`

**Node pool**

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

**Kubectl image**

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

**Default:** `"quay.io"`

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

### Other {#other}

---

`.baseDomain`

**Type:** `string`

**Base DNS domain**

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

- [Source repository](https://github.com/giantswarm/cluster-eks)
