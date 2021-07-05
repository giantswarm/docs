---
title: AWSCluster CRD schema reference
linkTitle: AWSCluster
technical_name: awsclusters.infrastructure.cluster.x-k8s.io
description: |
  AWSCluster is the Schema for the awsclusters API
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.27.1
layout: crd
aliases:
  - /reference/cp-k8s-api/awsclusters.infrastructure.cluster.x-k8s.io/
---

# AWSCluster


<p class="crd-description">AWSCluster is the Schema for the awsclusters API</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">awsclusters.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">awscluster</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">awsclusters</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha2" title="Show schema for version v1alpha2">v1alpha2</a><a class="version" href="#v1alpha3" title="Show schema for version v1alpha3">v1alpha3</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha2">Version v1alpha2</h2>



<h3 id="property-details-v1alpha2">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.apiVersion">.apiVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.kind">.kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AWSClusterSpec defines the desired state of AWSCluster</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.additionalTags">.spec.additionalTags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.controlPlaneLoadBalancer">.spec.controlPlaneLoadBalancer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlaneLoadBalancer is optional configuration for customizing control plane behavior</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.controlPlaneLoadBalancer.scheme">.spec.controlPlaneLoadBalancer.scheme</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scheme sets the scheme of the load balancer (defaults to Internet-facing)</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.disableBastionHost">.spec.disableBastionHost</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>DisableBastionHost is an optional configuration field to prevent the creation of a bastion host instance.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec">.spec.networkSpec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NetworkSpec encapsulates all things related to AWS network.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets">.spec.networkSpec.subnets</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Subnets configuration.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*]">.spec.networkSpec.subnets[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SubnetSpec configures an AWS Subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].availabilityZone">.spec.networkSpec.subnets[*].availabilityZone</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AvailabilityZone defines the availability zone to use for this subnet in the cluster&rsquo;s region.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].cidrBlock">.spec.networkSpec.subnets[*].cidrBlock</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CidrBlock is the CIDR block to be used when the provider creates a managed VPC.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].id">.spec.networkSpec.subnets[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines a unique identifier to reference this resource.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].isPublic">.spec.networkSpec.subnets[*].isPublic</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>IsPublic defines the subnet as a public subnet. A subnet is public when it is associated with a route table that has a route to an internet gateway.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].natGatewayId">.spec.networkSpec.subnets[*].natGatewayId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>NatGatewayID is the NAT gateway id associated with the subnet. Ignored unless the subnet is managed by the provider, in which case this is set on the public subnet where the NAT gateway resides. It is then used to determine routes for private subnets in the same AZ as the public subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].routeTableId">.spec.networkSpec.subnets[*].routeTableId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>RouteTableID is the routing table id associated with the subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.subnets[*].tags">.spec.networkSpec.subnets[*].tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a collection of tags describing the resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.vpc">.spec.networkSpec.vpc</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>VPC configuration.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.vpc.cidrBlock">.spec.networkSpec.vpc.cidrBlock</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CidrBlock is the CIDR block to be used when the provider creates a managed VPC. Defaults to 10.0.0.0/16.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.vpc.id">.spec.networkSpec.vpc.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID is the vpc-id of the VPC this provider should use to create resources.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.vpc.internetGatewayId">.spec.networkSpec.vpc.internetGatewayId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InternetGatewayID is the id of the internet gateway associated with the VPC.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.networkSpec.vpc.tags">.spec.networkSpec.vpc.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a collection of tags describing the resource.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.region">.spec.region</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The AWS Region the cluster lives in.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.sshKeyName">.spec.sshKeyName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SSHKeyName is the name of the ssh key to attach to the bastion host.</p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AWSClusterStatus defines the observed state of AWSCluster</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.apiEndpoints">.status.apiEndpoints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>APIEndpoints represents the endpoints to communicate with the control plane.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.apiEndpoints[*]">.status.apiEndpoints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIEndpoint represents a reachable Kubernetes API endpoint.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.apiEndpoints[*].host">.status.apiEndpoints[*].host</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The hostname on which the API server is serving.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.apiEndpoints[*].port">.status.apiEndpoints[*].port</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The port on which the API server is serving.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion">.status.bastion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Instance describes an AWS instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.addresses">.status.bastion.addresses</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Addresses contains the AWS instance associated addresses.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.addresses[*]">.status.bastion.addresses[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>MachineAddress contains information for the node&rsquo;s address.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.addresses[*].address">.status.bastion.addresses[*].address</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The machine address.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.addresses[*].type">.status.bastion.addresses[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Machine address type, one of Hostname, ExternalIP or InternalIP.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.ebsOptimized">.status.bastion.ebsOptimized</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Indicates whether the instance is optimized for Amazon EBS I/O.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.enaSupport">.status.bastion.enaSupport</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Specifies whether enhanced networking with ENA is enabled.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.iamProfile">.status.bastion.iamProfile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the IAM instance profile associated with the instance, if applicable.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.id">.status.bastion.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.imageId">.status.bastion.imageId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The ID of the AMI used to launch the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.instanceState">.status.bastion.instanceState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The current state of the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.networkInterfaces">.status.bastion.networkInterfaces</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Specifies ENIs attached to instance</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.networkInterfaces[*]">.status.bastion.networkInterfaces[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.privateIp">.status.bastion.privateIp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The private IPv4 address assigned to the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.publicIp">.status.bastion.publicIp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The public IPv4 address assigned to the instance, if applicable.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.rootDeviceSize">.status.bastion.rootDeviceSize</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Specifies size (in Gi) of the root storage device</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.securityGroupIds">.status.bastion.securityGroupIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SecurityGroupIDs are one or more security group IDs this instance belongs to.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.securityGroupIds[*]">.status.bastion.securityGroupIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.sshKeyName">.status.bastion.sshKeyName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the SSH key pair.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.subnetId">.status.bastion.subnetId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The ID of the subnet of the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.tags">.status.bastion.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The tags associated with the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.type">.status.bastion.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The instance type.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.bastion.userData">.status.bastion.userData</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network">.status.network</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Network encapsulates AWS networking resources.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb">.status.network.apiServerElb</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIServerELB is the Kubernetes api server classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.attributes">.status.network.apiServerElb.attributes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Attributes defines extra attributes associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.attributes.idleTimeout">.status.network.apiServerElb.attributes.idleTimeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>IdleTimeout is time that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.dnsName">.status.network.apiServerElb.dnsName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DNSName is the dns name of the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks">.status.network.apiServerElb.healthChecks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HealthCheck is the classic elb health check associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks.healthyThreshold">.status.network.apiServerElb.healthChecks.healthyThreshold</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks.interval">.status.network.apiServerElb.healthChecks.interval</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks.target">.status.network.apiServerElb.healthChecks.target</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks.timeout">.status.network.apiServerElb.healthChecks.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.healthChecks.unhealthyThreshold">.status.network.apiServerElb.healthChecks.unhealthyThreshold</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners">.status.network.apiServerElb.listeners</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Listeners is an array of classic elb listeners associated with the load balancer. There must be at least one.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners[*]">.status.network.apiServerElb.listeners[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClassicELBListener defines an AWS classic load balancer listener.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners[*].instancePort">.status.network.apiServerElb.listeners[*].instancePort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners[*].instanceProtocol">.status.network.apiServerElb.listeners[*].instanceProtocol</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ClassicELBProtocol defines listener protocols for a classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners[*].port">.status.network.apiServerElb.listeners[*].port</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.listeners[*].protocol">.status.network.apiServerElb.listeners[*].protocol</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ClassicELBProtocol defines listener protocols for a classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.name">.status.network.apiServerElb.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.scheme">.status.network.apiServerElb.scheme</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scheme is the load balancer scheme, either internet-facing or private.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.securityGroupIds">.status.network.apiServerElb.securityGroupIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SecurityGroupIDs is an array of security groups assigned to the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.securityGroupIds[*]">.status.network.apiServerElb.securityGroupIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.subnetIds">.status.network.apiServerElb.subnetIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SubnetIDs is an array of subnets in the VPC attached to the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.subnetIds[*]">.status.network.apiServerElb.subnetIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.apiServerElb.tags">.status.network.apiServerElb.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a map of tags associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.network.securityGroups">.status.network.securityGroups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityGroups is a map from the role/kind of the security group to its unique name, if any.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.ready">.status.ready</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

</div>
</div>





</div>

<div class="crd-schema-version">
<h2 id="v1alpha3">Version v1alpha3</h2>



<h3 id="property-details-v1alpha3">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.apiVersion">.apiVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.kind">.kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AWSClusterSpec defines the desired state of AWSCluster</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.additionalTags">.spec.additionalTags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AdditionalTags is an optional set of tags to add to AWS resources managed by the AWS provider, in addition to the ones added by default.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion">.spec.bastion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Bastion contains options to configure the bastion host.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.allowedCIDRBlocks">.spec.bastion.allowedCIDRBlocks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>AllowedCIDRBlocks is a list of CIDR blocks allowed to access the bastion host. They are set as ingress rules for the Bastion host&rsquo;s Security Group (defaults to 0.0.0.0/0).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.allowedCIDRBlocks[*]">.spec.bastion.allowedCIDRBlocks[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.ami">.spec.bastion.ami</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AMI will use the specified AMI to boot the bastion. If not specified, the AMI will default to one picked out in public space.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.disableIngressRules">.spec.bastion.disableIngressRules</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>DisableIngressRules will ensure there are no Ingress rules in the bastion host&rsquo;s security group. Requires AllowedCIDRBlocks to be empty.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.enabled">.spec.bastion.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled allows this provider to create a bastion host instance with a public ip to access the VPC private network.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.bastion.instanceType">.spec.bastion.instanceType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceType will use the specified instance type for the bastion. If not specified, Cluster API Provider AWS will use t3.micro for all regions except us-east-1, where t2.micro will be the default.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneEndpoint">.spec.controlPlaneEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlaneEndpoint represents the endpoint used to communicate with the control plane.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneEndpoint.host">.spec.controlPlaneEndpoint.host</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The hostname on which the API server is serving.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneEndpoint.port">.spec.controlPlaneEndpoint.port</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The port on which the API server is serving.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer">.spec.controlPlaneLoadBalancer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlaneLoadBalancer is optional configuration for customizing control plane behavior.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.additionalSecurityGroups">.spec.controlPlaneLoadBalancer.additionalSecurityGroups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>AdditionalSecurityGroups sets the security groups used by the load balancer. Expected to be security group IDs. This is optional - if not provided new security groups will be created for the load balancer</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.additionalSecurityGroups[*]">.spec.controlPlaneLoadBalancer.additionalSecurityGroups[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.crossZoneLoadBalancing">.spec.controlPlaneLoadBalancer.crossZoneLoadBalancing</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>CrossZoneLoadBalancing enables the classic ELB cross availability zone balancing.
 With cross-zone load balancing, each load balancer node for your Classic Load Balancer distributes requests evenly across the registered instances in all enabled Availability Zones. If cross-zone load balancing is disabled, each load balancer node distributes requests evenly across the registered instances in its Availability Zone only.
 Defaults to false.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.scheme">.spec.controlPlaneLoadBalancer.scheme</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scheme sets the scheme of the load balancer (defaults to Internet-facing)</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.subnets">.spec.controlPlaneLoadBalancer.subnets</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Subnets sets the subnets that should be applied to the control plane load balancer (defaults to discovered subnets for managed VPCs or an empty set for unmanaged VPCs)</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.controlPlaneLoadBalancer.subnets[*]">.spec.controlPlaneLoadBalancer.subnets[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.identityRef">.spec.identityRef</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>IdentityRef is a reference to a identity to be used when reconciling this cluster</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.identityRef.kind">.spec.identityRef.kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Kind of the identity.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.identityRef.name">.spec.identityRef.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the identity.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.imageLookupBaseOS">.spec.imageLookupBaseOS</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageLookupBaseOS is the name of the base operating system used to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupBaseOS.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.imageLookupFormat">.spec.imageLookupFormat</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageLookupFormat is the AMI naming format to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg. Supports substitutions for {{.BaseOS}} and {{.K8sVersion}} with the base OS and kubernetes version, respectively. The BaseOS will be the value in ImageLookupBaseOS or ubuntu (the default), and the kubernetes version as defined by the packages produced by kubernetes/release without v as a prefix: 1.13.0, 1.12.5-mybuild.1, or 1.17.3. For example, the default image format of capa-ami-{{.BaseOS}}-?{{.K8sVersion}}-* will end up searching for AMIs that match the pattern capa-ami-ubuntu-?1.18.0-* for a Machine that is targeting kubernetes v1.18.0 and the ubuntu base OS. See also: <a href="https://golang.org/pkg/text/template/">https://golang.org/pkg/text/template/</a></p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.imageLookupOrg">.spec.imageLookupOrg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageLookupOrg is the AWS Organization ID to look up machine images when a machine does not specify an AMI. When set, this will be used for all cluster machines unless a machine specifies a different ImageLookupOrg.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec">.spec.networkSpec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NetworkSpec encapsulates all things related to AWS network.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni">.spec.networkSpec.cni</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>CNI configuration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules">.spec.networkSpec.cni.cniIngressRules</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CNIIngressRules specify rules to apply to control plane and worker node security groups. The source for the rule will be set to control plane and worker security group IDs.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules[*]">.spec.networkSpec.cni.cniIngressRules[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>CNIIngressRule defines an AWS ingress rule for CNI requirements.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules[*].description">.spec.networkSpec.cni.cniIngressRules[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules[*].fromPort">.spec.networkSpec.cni.cniIngressRules[*].fromPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules[*].protocol">.spec.networkSpec.cni.cniIngressRules[*].protocol</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SecurityGroupProtocol defines the protocol type for a security group rule.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.cni.cniIngressRules[*].toPort">.spec.networkSpec.cni.cniIngressRules[*].toPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.securityGroupOverrides">.spec.networkSpec.securityGroupOverrides</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityGroupOverrides is an optional set of security groups to use for cluster instances This is optional - if not provided new security groups will be created for the cluster</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets">.spec.networkSpec.subnets</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Subnets configuration.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*]">.spec.networkSpec.subnets[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SubnetSpec configures an AWS Subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].availabilityZone">.spec.networkSpec.subnets[*].availabilityZone</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AvailabilityZone defines the availability zone to use for this subnet in the cluster&rsquo;s region.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].cidrBlock">.spec.networkSpec.subnets[*].cidrBlock</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CidrBlock is the CIDR block to be used when the provider creates a managed VPC.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].id">.spec.networkSpec.subnets[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines a unique identifier to reference this resource.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].isPublic">.spec.networkSpec.subnets[*].isPublic</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>IsPublic defines the subnet as a public subnet. A subnet is public when it is associated with a route table that has a route to an internet gateway.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].natGatewayId">.spec.networkSpec.subnets[*].natGatewayId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>NatGatewayID is the NAT gateway id associated with the subnet. Ignored unless the subnet is managed by the provider, in which case this is set on the public subnet where the NAT gateway resides. It is then used to determine routes for private subnets in the same AZ as the public subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].routeTableId">.spec.networkSpec.subnets[*].routeTableId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>RouteTableID is the routing table id associated with the subnet.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.subnets[*].tags">.spec.networkSpec.subnets[*].tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a collection of tags describing the resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc">.spec.networkSpec.vpc</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>VPC configuration.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.availabilityZoneSelection">.spec.networkSpec.vpc.availabilityZoneSelection</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AvailabilityZoneSelection specifies how AZs should be selected if there are more AZs in a region than specified by AvailabilityZoneUsageLimit. There are 2 selection schemes: Ordered - selects based on alphabetical order Random - selects AZs randomly in a region Defaults to Ordered</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.availabilityZoneUsageLimit">.spec.networkSpec.vpc.availabilityZoneUsageLimit</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>AvailabilityZoneUsageLimit specifies the maximum number of availability zones (AZ) that should be used in a region when automatically creating subnets. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating default subnets. Defaults to 3</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.cidrBlock">.spec.networkSpec.vpc.cidrBlock</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CidrBlock is the CIDR block to be used when the provider creates a managed VPC. Defaults to 10.0.0.0/16.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.id">.spec.networkSpec.vpc.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID is the vpc-id of the VPC this provider should use to create resources.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.internetGatewayId">.spec.networkSpec.vpc.internetGatewayId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InternetGatewayID is the id of the internet gateway associated with the VPC.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.networkSpec.vpc.tags">.spec.networkSpec.vpc.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a collection of tags describing the resource.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.region">.spec.region</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The AWS Region the cluster lives in.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.sshKeyName">.spec.sshKeyName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SSHKeyName is the name of the ssh key to attach to the bastion host. Valid values are empty string (do not use SSH keys), a valid SSH key name, or omitted (use the default SSH key name)</p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AWSClusterStatus defines the observed state of AWSCluster</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion">.status.bastion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Instance describes an AWS instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.addresses">.status.bastion.addresses</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Addresses contains the AWS instance associated addresses.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.addresses[*]">.status.bastion.addresses[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>MachineAddress contains information for the node&rsquo;s address.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.addresses[*].address">.status.bastion.addresses[*].address</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The machine address.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.addresses[*].type">.status.bastion.addresses[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Machine address type, one of Hostname, ExternalIP or InternalIP.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.availabilityZone">.status.bastion.availabilityZone</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Availability zone of instance</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.ebsOptimized">.status.bastion.ebsOptimized</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Indicates whether the instance is optimized for Amazon EBS I/O.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.enaSupport">.status.bastion.enaSupport</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Specifies whether enhanced networking with ENA is enabled.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.iamProfile">.status.bastion.iamProfile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the IAM instance profile associated with the instance, if applicable.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.id">.status.bastion.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.imageId">.status.bastion.imageId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The ID of the AMI used to launch the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.instanceState">.status.bastion.instanceState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The current state of the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.networkInterfaces">.status.bastion.networkInterfaces</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Specifies ENIs attached to instance</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.networkInterfaces[*]">.status.bastion.networkInterfaces[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes">.status.bastion.nonRootVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Configuration options for the non root storage volumes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*]">.status.bastion.nonRootVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Volume encapsulates the configuration options for the storage device</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].deviceName">.status.bastion.nonRootVolumes[*].deviceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Device name</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].encrypted">.status.bastion.nonRootVolumes[*].encrypted</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Encrypted is whether the volume should be encrypted or not.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].encryptionKey">.status.bastion.nonRootVolumes[*].encryptionKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].iops">.status.bastion.nonRootVolumes[*].iops</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>IOPS is the number of IOPS requested for the disk. Not applicable to all types.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].size">.status.bastion.nonRootVolumes[*].size</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater).</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.nonRootVolumes[*].type">.status.bastion.nonRootVolumes[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type is the type of the volume (e.g. gp2, io1, etc&hellip;).</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.privateIp">.status.bastion.privateIp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The private IPv4 address assigned to the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.publicIp">.status.bastion.publicIp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The public IPv4 address assigned to the instance, if applicable.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume">.status.bastion.rootVolume</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Configuration options for the root storage volume.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.deviceName">.status.bastion.rootVolume.deviceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Device name</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.encrypted">.status.bastion.rootVolume.encrypted</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Encrypted is whether the volume should be encrypted or not.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.encryptionKey">.status.bastion.rootVolume.encryptionKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>EncryptionKey is the KMS key to use to encrypt the volume. Can be either a KMS key ID or ARN. If Encrypted is set and this is omitted, the default AWS key will be used. The key must already exist and be accessible by the controller.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.iops">.status.bastion.rootVolume.iops</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>IOPS is the number of IOPS requested for the disk. Not applicable to all types.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.size">.status.bastion.rootVolume.size</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Size specifies size (in Gi) of the storage device. Must be greater than the image snapshot size or 8 (whichever is greater).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.rootVolume.type">.status.bastion.rootVolume.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type is the type of the volume (e.g. gp2, io1, etc&hellip;).</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.securityGroupIds">.status.bastion.securityGroupIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SecurityGroupIDs are one or more security group IDs this instance belongs to.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.securityGroupIds[*]">.status.bastion.securityGroupIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.spotMarketOptions">.status.bastion.spotMarketOptions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SpotMarketOptions option for configuring instances to be run using AWS Spot instances.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.spotMarketOptions.maxPrice">.status.bastion.spotMarketOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.sshKeyName">.status.bastion.sshKeyName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the SSH key pair.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.subnetId">.status.bastion.subnetId</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The ID of the subnet of the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.tags">.status.bastion.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The tags associated with the instance.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.tenancy">.status.bastion.tenancy</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tenancy indicates if instance should run on shared or single-tenant hardware.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.type">.status.bastion.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The instance type.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bastion.userData">.status.bastion.userData</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>UserData is the raw data script passed to the instance which is run upon bootstrap. This field must not be base64 encoded and should only be used when running a new instance.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions">.status.conditions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Conditions provide observations of the operational state of a Cluster API resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*]">.status.conditions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an observation of a Cluster API resource operational state.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].lastTransitionTime">.status.conditions[*].lastTransitionTime</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].message">.status.conditions[*].message</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>A human readable message indicating details about the transition. This field may be empty.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].reason">.status.conditions[*].reason</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The reason for the condition&rsquo;s last transition in CamelCase. The specific API may choose whether or not this field is considered a guaranteed API. This field may not be empty.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].severity">.status.conditions[*].severity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Severity provides an explicit classification of Reason code, so the users or machines can immediately understand the current situation and act accordingly. The Severity field MUST be set only when Status=False.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].status">.status.conditions[*].status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Status of the condition, one of True, False, Unknown.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.conditions[*].type">.status.conditions[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type of condition in CamelCase or in foo.example.com/CamelCase. Many .condition.type values are consistent across resources like Available, but because arbitrary conditions can be useful (see .node.status.conditions), the ability to deconflict is important.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.failureDomains">.status.failureDomains</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>FailureDomains is a slice of FailureDomains.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network">.status.network</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Network encapsulates AWS networking resources.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb">.status.network.apiServerElb</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIServerELB is the Kubernetes api server classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.attributes">.status.network.apiServerElb.attributes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Attributes defines extra attributes associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.attributes.crossZoneLoadBalancing">.status.network.apiServerElb.attributes.crossZoneLoadBalancing</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>CrossZoneLoadBalancing enables the classic load balancer load balancing.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.attributes.idleTimeout">.status.network.apiServerElb.attributes.idleTimeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>IdleTimeout is time that the connection is allowed to be idle (no data has been sent over the connection) before it is closed by the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.availabilityZones">.status.network.apiServerElb.availabilityZones</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>AvailabilityZones is an array of availability zones in the VPC attached to the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.availabilityZones[*]">.status.network.apiServerElb.availabilityZones[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.dnsName">.status.network.apiServerElb.dnsName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DNSName is the dns name of the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks">.status.network.apiServerElb.healthChecks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HealthCheck is the classic elb health check associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks.healthyThreshold">.status.network.apiServerElb.healthChecks.healthyThreshold</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks.interval">.status.network.apiServerElb.healthChecks.interval</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks.target">.status.network.apiServerElb.healthChecks.target</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks.timeout">.status.network.apiServerElb.healthChecks.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>A Duration represents the elapsed time between two instants as an int64 nanosecond count. The representation limits the largest representable duration to approximately 290 years.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.healthChecks.unhealthyThreshold">.status.network.apiServerElb.healthChecks.unhealthyThreshold</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners">.status.network.apiServerElb.listeners</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Listeners is an array of classic elb listeners associated with the load balancer. There must be at least one.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners[*]">.status.network.apiServerElb.listeners[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClassicELBListener defines an AWS classic load balancer listener.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners[*].instancePort">.status.network.apiServerElb.listeners[*].instancePort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners[*].instanceProtocol">.status.network.apiServerElb.listeners[*].instanceProtocol</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ClassicELBProtocol defines listener protocols for a classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners[*].port">.status.network.apiServerElb.listeners[*].port</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.listeners[*].protocol">.status.network.apiServerElb.listeners[*].protocol</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ClassicELBProtocol defines listener protocols for a classic load balancer.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.name">.status.network.apiServerElb.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The name of the load balancer. It must be unique within the set of load balancers defined in the region. It also serves as identifier.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.scheme">.status.network.apiServerElb.scheme</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Scheme is the load balancer scheme, either internet-facing or private.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.securityGroupIds">.status.network.apiServerElb.securityGroupIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SecurityGroupIDs is an array of security groups assigned to the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.securityGroupIds[*]">.status.network.apiServerElb.securityGroupIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.subnetIds">.status.network.apiServerElb.subnetIds</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SubnetIDs is an array of subnets in the VPC attached to the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.subnetIds[*]">.status.network.apiServerElb.subnetIds[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.apiServerElb.tags">.status.network.apiServerElb.tags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Tags is a map of tags associated with the load balancer.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.network.securityGroups">.status.network.securityGroups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityGroups is a map from the role/kind of the security group to its unique name, if any.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.ready">.status.ready</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

</div>
</div>





</div>



