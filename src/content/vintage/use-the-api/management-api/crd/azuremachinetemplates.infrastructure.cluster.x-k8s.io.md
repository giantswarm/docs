---
title: AzureMachineTemplate CRD schema reference (group infrastructure.cluster.x-k8s.io)
linkTitle: AzureMachineTemplate
description: |
  AzureMachineTemplate is the Schema for the azuremachinetemplates API.
weight: 100
crd:
  name_camelcase: AzureMachineTemplate
  name_plural: azuremachinetemplates
  name_singular: azuremachinetemplate
  group: infrastructure.cluster.x-k8s.io
  technical_name: azuremachinetemplates.infrastructure.cluster.x-k8s.io
  scope: Namespaced
  source_repository: https://github.com/giantswarm/apiextensions
  source_repository_ref: v5.0.0
  versions:
    - v1alpha3
    - v1alpha4
    - v1beta1
  topics:
    - workloadcluster
  providers:
    - aws
    - azure
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
aliases:
  - /use-the-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io/
technical_name: azuremachinetemplates.infrastructure.cluster.x-k8s.io
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v5.0.0
---

# AzureMachineTemplate


<p class="crd-description">AzureMachineTemplate is the Schema for the azuremachinetemplates API.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">azuremachinetemplates.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">azuremachinetemplate</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">azuremachinetemplates</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha3" title="Show schema for version v1alpha3">v1alpha3</a><a class="version" href="#v1alpha4" title="Show schema for version v1alpha4">v1alpha4</a><a class="version" href="#v1beta1" title="Show schema for version v1beta1">v1beta1</a></dd>
</dl>



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
<p>AzureMachineTemplateSpec defines the desired state of AzureMachineTemplate.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template">.spec.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AzureMachineTemplateResource describes the data needed to create an AzureMachine from a template.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec">.spec.template.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Spec is the specification of the desired behavior of the machine.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.acceleratedNetworking">.spec.template.spec.acceleratedNetworking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AcceleratedNetworking enables or disables Azure accelerated networking. If omitted, it will be set based on whether the requested VMSize supports accelerated networking. If AcceleratedNetworking is set to true with a VMSize that does not support it, Azure will return an error.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.additionalTags">.spec.template.spec.additionalTags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the Azure provider. If both the AzureCluster and the AzureMachine specify the same tag name with different values, the AzureMachine&rsquo;s value takes precedence.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.allocatePublicIP">.spec.template.spec.allocatePublicIP</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllocatePublicIP allows the ability to create dynamic public ips for machines where this value is true.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.availabilityZone">.spec.template.spec.availabilityZone</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DEPRECATED: use FailureDomain instead</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.availabilityZone.enabled">.spec.template.spec.availabilityZone.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.availabilityZone.id">.spec.template.spec.availabilityZone.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks">.spec.template.spec.dataDisks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*]">.spec.template.spec.dataDisks[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].cachingType">.spec.template.spec.dataDisks[*].cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].diskSizeGB">.spec.template.spec.dataDisks[*].diskSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DiskSizeGB is the size in GB to assign to the data disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].lun">.spec.template.spec.dataDisks[*].lun</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Lun Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. The value must be between 0 and 63.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].managedDisk">.spec.template.spec.dataDisks[*].managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ManagedDisk defines the managed disk options for a VM.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].managedDisk.storageAccountType">.spec.template.spec.dataDisks[*].managedDisk.storageAccountType</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.spec.dataDisks[*].nameSuffix">.spec.template.spec.dataDisks[*].nameSuffix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NameSuffix is the suffix to be appended to the machine name to generate the disk name. Each disk name will be in format <machineName>_<nameSuffix>.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.enableIPForwarding">.spec.template.spec.enableIPForwarding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>EnableIPForwarding enables IP Forwarding in Azure which is required for some CNI&rsquo;s to send traffic from a pods on one machine to another. This is required for IpV6 with Calico in combination with User Defined Routes (set by the Azure Cloud Controller manager). Default is false for disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.failureDomain">.spec.template.spec.failureDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. This relates to an Azure Availability Zone</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.identity">.spec.template.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the virtual machine. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image">.spec.template.spec.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is used to provide details of an image to use during VM creation. If image details are omitted the image will default the Azure Marketplace &ldquo;capi&rdquo; offer, which is based on Ubuntu.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.id">.spec.template.spec.image.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID specifies an image to use by ID</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace">.spec.template.spec.image.marketplace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Marketplace specifies an image to use from the Azure Marketplace</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace.offer">.spec.template.spec.image.marketplace.offer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace.publisher">.spec.template.spec.image.marketplace.publisher</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Publisher is the name of the organization that created the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace.sku">.spec.template.spec.image.marketplace.sku</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace.thirdPartyImage">.spec.template.spec.image.marketplace.thirdPartyImage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ThirdPartyImage indicates the image is published by a third party publisher and a Plan will be generated for it.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.marketplace.version">.spec.template.spec.image.marketplace.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of an image sku. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery">.spec.template.spec.image.sharedGallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SharedGallery specifies an image to use from an Azure Shared Image Gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery.gallery">.spec.template.spec.image.sharedGallery.gallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Gallery specifies the name of the shared image gallery that contains the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery.name">.spec.template.spec.image.sharedGallery.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery.resourceGroup">.spec.template.spec.image.sharedGallery.resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ResourceGroup specifies the resource group containing the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery.subscriptionID">.spec.template.spec.image.sharedGallery.subscriptionID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SubscriptionID is the identifier of the subscription that contains the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.image.sharedGallery.version">.spec.template.spec.image.sharedGallery.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of the marketplace image. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.location">.spec.template.spec.location</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DEPRECATED: to support old clients, will be removed in v1alpha4/v1beta1</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk">.spec.template.spec.osDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>OSDisk specifies the parameters for the operating system disk of the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.cachingType">.spec.template.spec.osDisk.cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.diffDiskSettings">.spec.template.spec.osDisk.diffDiskSettings</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiffDiskSettings describe ephemeral disk settings for the os disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.diffDiskSettings.option">.spec.template.spec.osDisk.diffDiskSettings.option</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Option enables ephemeral OS when set to &ldquo;Local&rdquo; See <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks">https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks</a> for full details</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.diskSizeGB">.spec.template.spec.osDisk.diskSizeGB</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.managedDisk">.spec.template.spec.osDisk.managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ManagedDisk defines the managed disk options for a VM.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.managedDisk.storageAccountType">.spec.template.spec.osDisk.managedDisk.storageAccountType</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.spec.osDisk.osType">.spec.template.spec.osDisk.osType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.providerID">.spec.template.spec.providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the unique identifier as specified by the cloud provider.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.roleAssignmentName">.spec.template.spec.roleAssignmentName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>RoleAssignmentName is the name of the role assignment to create for a system assigned identity. It can be any valid GUID. If not specified, a random GUID will be generated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.securityProfile">.spec.template.spec.securityProfile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityProfile specifies the Security profile settings for a virtual machine.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.securityProfile.encryptionAtHost">.spec.template.spec.securityProfile.encryptionAtHost</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>This field indicates whether Host Encryption should be enabled or disabled for a virtual machine or virtual machine scale set. Default is disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.spotVMOptions">.spec.template.spec.spotVMOptions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SpotVMOptions allows the ability to specify the Machine should use a Spot VM.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.spotVMOptions.maxPrice">.spec.template.spec.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.sshPublicKey">.spec.template.spec.sshPublicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.userAssignedIdentities">.spec.template.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachine. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.userAssignedIdentities[*]">.spec.template.spec.userAssignedIdentities[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>UserAssignedIdentity defines the user-assigned identities provided by the user to be assigned to Azure resources.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.userAssignedIdentities[*].providerID">.spec.template.spec.userAssignedIdentities[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ProviderID is the identification ID of the user-assigned Identity, the format of an identity is: &lsquo;azure:///subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&rsquo;</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spec.vmSize">.spec.template.spec.vmSize</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>





</div>
<div class="crd-schema-version">
<h2 id="v1alpha4">Version v1alpha4</h2>



<h3 id="property-details-v1alpha4">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.apiVersion">.apiVersion</h3>
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
<h3 class="property-path" id="v1alpha4-.kind">.kind</h3>
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
<h3 class="property-path" id="v1alpha4-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachineTemplateSpec defines the desired state of AzureMachineTemplate.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template">.spec.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AzureMachineTemplateResource describes the data needed to create an AzureMachine from a template.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec">.spec.template.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Spec is the specification of the desired behavior of the machine.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.acceleratedNetworking">.spec.template.spec.acceleratedNetworking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AcceleratedNetworking enables or disables Azure accelerated networking. If omitted, it will be set based on whether the requested VMSize supports accelerated networking. If AcceleratedNetworking is set to true with a VMSize that does not support it, Azure will return an error.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.additionalTags">.spec.template.spec.additionalTags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the Azure provider. If both the AzureCluster and the AzureMachine specify the same tag name with different values, the AzureMachine&rsquo;s value takes precedence.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.allocatePublicIP">.spec.template.spec.allocatePublicIP</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllocatePublicIP allows the ability to create dynamic public ips for machines where this value is true.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks">.spec.template.spec.dataDisks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*]">.spec.template.spec.dataDisks[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].cachingType">.spec.template.spec.dataDisks[*].cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CachingType specifies the caching requirements.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].diskSizeGB">.spec.template.spec.dataDisks[*].diskSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DiskSizeGB is the size in GB to assign to the data disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].lun">.spec.template.spec.dataDisks[*].lun</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Lun Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. The value must be between 0 and 63.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].managedDisk">.spec.template.spec.dataDisks[*].managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ManagedDisk specifies the Managed Disk parameters for the data disk.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].managedDisk.storageAccountType">.spec.template.spec.dataDisks[*].managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.dataDisks[*].nameSuffix">.spec.template.spec.dataDisks[*].nameSuffix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NameSuffix is the suffix to be appended to the machine name to generate the disk name. Each disk name will be in format <machineName>_<nameSuffix>.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.enableIPForwarding">.spec.template.spec.enableIPForwarding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>EnableIPForwarding enables IP Forwarding in Azure which is required for some CNI&rsquo;s to send traffic from a pods on one machine to another. This is required for IpV6 with Calico in combination with User Defined Routes (set by the Azure Cloud Controller manager). Default is false for disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.failureDomain">.spec.template.spec.failureDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. This relates to an Azure Availability Zone</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.identity">.spec.template.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the virtual machine. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image">.spec.template.spec.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is used to provide details of an image to use during VM creation. If image details are omitted the image will default the Azure Marketplace &ldquo;capi&rdquo; offer, which is based on Ubuntu.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.id">.spec.template.spec.image.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID specifies an image to use by ID</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace">.spec.template.spec.image.marketplace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Marketplace specifies an image to use from the Azure Marketplace</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace.offer">.spec.template.spec.image.marketplace.offer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace.publisher">.spec.template.spec.image.marketplace.publisher</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Publisher is the name of the organization that created the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace.sku">.spec.template.spec.image.marketplace.sku</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace.thirdPartyImage">.spec.template.spec.image.marketplace.thirdPartyImage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ThirdPartyImage indicates the image is published by a third party publisher and a Plan will be generated for it.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.marketplace.version">.spec.template.spec.image.marketplace.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of an image sku. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery">.spec.template.spec.image.sharedGallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SharedGallery specifies an image to use from an Azure Shared Image Gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.gallery">.spec.template.spec.image.sharedGallery.gallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Gallery specifies the name of the shared image gallery that contains the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.name">.spec.template.spec.image.sharedGallery.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.offer">.spec.template.spec.image.sharedGallery.offer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.publisher">.spec.template.spec.image.sharedGallery.publisher</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Publisher is the name of the organization that created the image. This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.resourceGroup">.spec.template.spec.image.sharedGallery.resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ResourceGroup specifies the resource group containing the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.sku">.spec.template.spec.image.sharedGallery.sku</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.subscriptionID">.spec.template.spec.image.sharedGallery.subscriptionID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SubscriptionID is the identifier of the subscription that contains the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.image.sharedGallery.version">.spec.template.spec.image.sharedGallery.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of the marketplace image. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk">.spec.template.spec.osDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>OSDisk specifies the parameters for the operating system disk of the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.cachingType">.spec.template.spec.osDisk.cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CachingType specifies the caching requirements.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.diffDiskSettings">.spec.template.spec.osDisk.diffDiskSettings</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiffDiskSettings describe ephemeral disk settings for the os disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.diffDiskSettings.option">.spec.template.spec.osDisk.diffDiskSettings.option</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Option enables ephemeral OS when set to &ldquo;Local&rdquo; See <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks">https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks</a> for full details</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.diskSizeGB">.spec.template.spec.osDisk.diskSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>DiskSizeGB is the size in GB to assign to the OS disk. Will have a default of 30GB if not provided</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.managedDisk">.spec.template.spec.osDisk.managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ManagedDisk specifies the Managed Disk parameters for the OS disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.managedDisk.storageAccountType">.spec.template.spec.osDisk.managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.osDisk.osType">.spec.template.spec.osDisk.osType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.providerID">.spec.template.spec.providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the unique identifier as specified by the cloud provider.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.roleAssignmentName">.spec.template.spec.roleAssignmentName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>RoleAssignmentName is the name of the role assignment to create for a system assigned identity. It can be any valid GUID. If not specified, a random GUID will be generated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.securityProfile">.spec.template.spec.securityProfile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityProfile specifies the Security profile settings for a virtual machine.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.securityProfile.encryptionAtHost">.spec.template.spec.securityProfile.encryptionAtHost</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>This field indicates whether Host Encryption should be enabled or disabled for a virtual machine or virtual machine scale set. Default is disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.spotVMOptions">.spec.template.spec.spotVMOptions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SpotVMOptions allows the ability to specify the Machine should use a Spot VM</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.spotVMOptions.maxPrice">.spec.template.spec.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.sshPublicKey">.spec.template.spec.sshPublicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.subnetName">.spec.template.spec.subnetName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SubnetName selects the Subnet where the VM will be placed</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.userAssignedIdentities">.spec.template.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachine. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.userAssignedIdentities[*]">.spec.template.spec.userAssignedIdentities[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>UserAssignedIdentity defines the user-assigned identities provided by the user to be assigned to Azure resources.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.userAssignedIdentities[*].providerID">.spec.template.spec.userAssignedIdentities[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ProviderID is the identification ID of the user-assigned Identity, the format of an identity is: &lsquo;azure:///subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&rsquo;</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spec.vmSize">.spec.template.spec.vmSize</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>





</div>
<div class="crd-schema-version">
<h2 id="v1beta1">Version v1beta1</h2>



<h3 id="property-details-v1beta1">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.apiVersion">.apiVersion</h3>
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
<h3 class="property-path" id="v1beta1-.kind">.kind</h3>
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
<h3 class="property-path" id="v1beta1-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachineTemplateSpec defines the desired state of AzureMachineTemplate.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template">.spec.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AzureMachineTemplateResource describes the data needed to create an AzureMachine from a template.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.metadata">.spec.template.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create. This is a copy of customizable fields from metav1.ObjectMeta.
 ObjectMeta is embedded in <code>Machine.Spec</code>, <code>MachineDeployment.Template</code> and <code>MachineSet.Template</code>, which are not top-level Kubernetes objects. Given that metav1.ObjectMeta has lots of special cases and read-only fields which end up in the generated CRD validation, having it as a subset simplifies the API and some issues that can impact user experience.
 During the <a href="https://github.com/kubernetes-sigs/cluster-api/pull/1054">upgrade to controller-tools@v2</a> for v1alpha2, we noticed a failure would occur running Cluster API test suite against the new CRDs, specifically <code>spec.metadata.creationTimestamp in body must be of type string: &quot;null&quot;</code>. The investigation showed that <code>controller-tools@v2</code> behaves differently than its previous version when handling types from <a href="k8s.io/apimachinery/pkg/apis/meta/v1">metav1</a> package.
 In more details, we found that embedded (non-top level) types that embedded <code>metav1.ObjectMeta</code> had validation properties, including for <code>creationTimestamp</code> (metav1.Time). The <code>metav1.Time</code> type specifies a custom json marshaller that, when IsZero() is true, returns <code>null</code> which breaks validation because the field isn&rsquo;t marked as nullable.
 In future versions, controller-tools@v2 might allow overriding the type and validation for embedded types. When that happens, this hack should be revisited.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.metadata.annotations">.spec.template.metadata.annotations</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <a href="http://kubernetes.io/docs/user-guide/annotations">http://kubernetes.io/docs/user-guide/annotations</a></p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.metadata.labels">.spec.template.metadata.labels</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <a href="http://kubernetes.io/docs/user-guide/labels">http://kubernetes.io/docs/user-guide/labels</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec">.spec.template.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Spec is the specification of the desired behavior of the machine.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.acceleratedNetworking">.spec.template.spec.acceleratedNetworking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AcceleratedNetworking enables or disables Azure accelerated networking. If omitted, it will be set based on whether the requested VMSize supports accelerated networking. If AcceleratedNetworking is set to true with a VMSize that does not support it, Azure will return an error.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.additionalTags">.spec.template.spec.additionalTags</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the Azure provider. If both the AzureCluster and the AzureMachine specify the same tag name with different values, the AzureMachine&rsquo;s value takes precedence.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.allocatePublicIP">.spec.template.spec.allocatePublicIP</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllocatePublicIP allows the ability to create dynamic public ips for machines where this value is true.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks">.spec.template.spec.dataDisks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*]">.spec.template.spec.dataDisks[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DataDisk specifies the parameters that are used to add one or more data disks to the machine.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].cachingType">.spec.template.spec.dataDisks[*].cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CachingType specifies the caching requirements.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].diskSizeGB">.spec.template.spec.dataDisks[*].diskSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DiskSizeGB is the size in GB to assign to the data disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].lun">.spec.template.spec.dataDisks[*].lun</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Lun Specifies the logical unit number of the data disk. This value is used to identify data disks within the VM and therefore must be unique for each data disk attached to a VM. The value must be between 0 and 63.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].managedDisk">.spec.template.spec.dataDisks[*].managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ManagedDisk specifies the Managed Disk parameters for the data disk.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.spec.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].managedDisk.storageAccountType">.spec.template.spec.dataDisks[*].managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.dataDisks[*].nameSuffix">.spec.template.spec.dataDisks[*].nameSuffix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NameSuffix is the suffix to be appended to the machine name to generate the disk name. Each disk name will be in format <machineName>_<nameSuffix>.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.enableIPForwarding">.spec.template.spec.enableIPForwarding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>EnableIPForwarding enables IP Forwarding in Azure which is required for some CNI&rsquo;s to send traffic from a pods on one machine to another. This is required for IpV6 with Calico in combination with User Defined Routes (set by the Azure Cloud Controller manager). Default is false for disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.failureDomain">.spec.template.spec.failureDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FailureDomain is the failure domain unique identifier this Machine should be attached to, as defined in Cluster API. This relates to an Azure Availability Zone</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.identity">.spec.template.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the virtual machine. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image">.spec.template.spec.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is used to provide details of an image to use during VM creation. If image details are omitted the image will default the Azure Marketplace &ldquo;capi&rdquo; offer, which is based on Ubuntu.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.id">.spec.template.spec.image.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID specifies an image to use by ID</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace">.spec.template.spec.image.marketplace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Marketplace specifies an image to use from the Azure Marketplace</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace.offer">.spec.template.spec.image.marketplace.offer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace.publisher">.spec.template.spec.image.marketplace.publisher</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Publisher is the name of the organization that created the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace.sku">.spec.template.spec.image.marketplace.sku</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace.thirdPartyImage">.spec.template.spec.image.marketplace.thirdPartyImage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ThirdPartyImage indicates the image is published by a third party publisher and a Plan will be generated for it.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.marketplace.version">.spec.template.spec.image.marketplace.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of an image sku. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery">.spec.template.spec.image.sharedGallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SharedGallery specifies an image to use from an Azure Shared Image Gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.gallery">.spec.template.spec.image.sharedGallery.gallery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Gallery specifies the name of the shared image gallery that contains the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.name">.spec.template.spec.image.sharedGallery.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the image</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.offer">.spec.template.spec.image.sharedGallery.offer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Offer specifies the name of a group of related images created by the publisher. For example, UbuntuServer, WindowsServer This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.publisher">.spec.template.spec.image.sharedGallery.publisher</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Publisher is the name of the organization that created the image. This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.resourceGroup">.spec.template.spec.image.sharedGallery.resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ResourceGroup specifies the resource group containing the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.sku">.spec.template.spec.image.sharedGallery.sku</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SKU specifies an instance of an offer, such as a major release of a distribution. For example, 18.04-LTS, 2019-Datacenter This value will be used to add a <code>Plan</code> in the API request when creating the VM/VMSS resource. This is needed when the source image from which this SIG image was built requires the <code>Plan</code> to be used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.subscriptionID">.spec.template.spec.image.sharedGallery.subscriptionID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SubscriptionID is the identifier of the subscription that contains the shared image gallery</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.image.sharedGallery.version">.spec.template.spec.image.sharedGallery.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Version specifies the version of the marketplace image. The allowed formats are Major.Minor.Build or &lsquo;latest&rsquo;. Major, Minor, and Build are decimal numbers. Specify &lsquo;latest&rsquo; to use the latest version of an image available at deploy time. Even if you use &lsquo;latest&rsquo;, the VM image will not automatically update after deploy time even if a new version becomes available.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk">.spec.template.spec.osDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>OSDisk specifies the parameters for the operating system disk of the machine</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.cachingType">.spec.template.spec.osDisk.cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CachingType specifies the caching requirements.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.diffDiskSettings">.spec.template.spec.osDisk.diffDiskSettings</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiffDiskSettings describe ephemeral disk settings for the os disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.diffDiskSettings.option">.spec.template.spec.osDisk.diffDiskSettings.option</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Option enables ephemeral OS when set to &ldquo;Local&rdquo; See <a href="https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks">https://docs.microsoft.com/en-us/azure/virtual-machines/ephemeral-os-disks</a> for full details</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.diskSizeGB">.spec.template.spec.osDisk.diskSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>DiskSizeGB is the size in GB to assign to the OS disk. Will have a default of 30GB if not provided</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.managedDisk">.spec.template.spec.osDisk.managedDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ManagedDisk specifies the Managed Disk parameters for the OS disk.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskEncryptionSetParameters defines disk encryption options.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.spec.osDisk.managedDisk.diskEncryptionSet.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ID defines resourceID for diskEncryptionSet resource. It must be in the same subscription</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.managedDisk.storageAccountType">.spec.template.spec.osDisk.managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.osDisk.osType">.spec.template.spec.osDisk.osType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.providerID">.spec.template.spec.providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the unique identifier as specified by the cloud provider.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.roleAssignmentName">.spec.template.spec.roleAssignmentName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>RoleAssignmentName is the name of the role assignment to create for a system assigned identity. It can be any valid GUID. If not specified, a random GUID will be generated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.securityProfile">.spec.template.spec.securityProfile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SecurityProfile specifies the Security profile settings for a virtual machine.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.securityProfile.encryptionAtHost">.spec.template.spec.securityProfile.encryptionAtHost</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>This field indicates whether Host Encryption should be enabled or disabled for a virtual machine or virtual machine scale set. Default is disabled.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.spotVMOptions">.spec.template.spec.spotVMOptions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SpotVMOptions allows the ability to specify the Machine should use a Spot VM</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.spotVMOptions.maxPrice">.spec.template.spec.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.sshPublicKey">.spec.template.spec.sshPublicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.subnetName">.spec.template.spec.subnetName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SubnetName selects the Subnet where the VM will be placed</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.userAssignedIdentities">.spec.template.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachine. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.userAssignedIdentities[*]">.spec.template.spec.userAssignedIdentities[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>UserAssignedIdentity defines the user-assigned identities provided by the user to be assigned to Azure resources.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.userAssignedIdentities[*].providerID">.spec.template.spec.userAssignedIdentities[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ProviderID is the identification ID of the user-assigned Identity, the format of an identity is: &lsquo;azure:///subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&rsquo;</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spec.vmSize">.spec.template.spec.vmSize</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>





</div>



