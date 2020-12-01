---
title: AzureMachinePool CRD Schema Reference
linktitle: AzureMachinePool
technical_name: azuremachinepools.exp.infrastructure.cluster.x-k8s.io
description:   AzureMachinePool is the Schema for the azuremachinepools API
date: 2020-12-01
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.10.0
layout: "crd"
---

# AzureMachinePool


<p class="crd-description">AzureMachinePool is the Schema for the azuremachinepools API</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">azuremachinepools.exp.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">exp.infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">azuremachinepool</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">azuremachinepools</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha3" title="Show schema for version v1alpha3">v1alpha3</a></dd>
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
<p>AzureMachinePoolSpec defines the desired state of AzureMachinePool</p>

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
<p>AdditionalTags is an optional set of tags to add to an instance, in addition to the ones added by default by the Azure provider. If both the AzureCluster and the AzureMachine specify the same tag name with different values, the AzureMachine&rsquo;s value takes precedence.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.location">.spec.location</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Location is the Azure region location e.g. westus2</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.providerID">.spec.providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the identification ID of the Virtual Machine Scale Set</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.providerIDList">.spec.providerIDList</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ProviderIDList are the identification IDs of machine instances provided by the provider. This field must match the provider IDs as seen on the node objects corresponding to a machine pool&rsquo;s machine instances.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.providerIDList[*]">.spec.providerIDList[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

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
<p>Template contains the details used to build a replica virtual machine within the Machine Pool</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.acceleratedNetworking">.spec.template.acceleratedNetworking</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks">.spec.template.dataDisks</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>DataDisks specifies the list of data disks to be created for a Virtual Machine</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*]">.spec.template.dataDisks[*]</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].cachingType">.spec.template.dataDisks[*].cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].diskSizeGB">.spec.template.dataDisks[*].diskSizeGB</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].lun">.spec.template.dataDisks[*].lun</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].nameSuffix">.spec.template.dataDisks[*].nameSuffix</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image">.spec.template.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is used to provide details of an image to use during Virtual Machine creation. If image details are omitted the image will default the Azure Marketplace &ldquo;capi&rdquo; offer, which is based on Ubuntu.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.id">.spec.template.image.id</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace">.spec.template.image.marketplace</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace.offer">.spec.template.image.marketplace.offer</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace.publisher">.spec.template.image.marketplace.publisher</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace.sku">.spec.template.image.marketplace.sku</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace.thirdPartyImage">.spec.template.image.marketplace.thirdPartyImage</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.marketplace.version">.spec.template.image.marketplace.version</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery">.spec.template.image.sharedGallery</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery.gallery">.spec.template.image.sharedGallery.gallery</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery.name">.spec.template.image.sharedGallery.name</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery.resourceGroup">.spec.template.image.sharedGallery.resourceGroup</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery.subscriptionID">.spec.template.image.sharedGallery.subscriptionID</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.image.sharedGallery.version">.spec.template.image.sharedGallery.version</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk">.spec.template.osDisk</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>OSDisk contains the operating system disk information for a Virtual Machine</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.cachingType">.spec.template.osDisk.cachingType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.diffDiskSettings">.spec.template.osDisk.diffDiskSettings</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.diffDiskSettings.option">.spec.template.osDisk.diffDiskSettings.option</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.diskSizeGB">.spec.template.osDisk.diskSizeGB</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.managedDisk">.spec.template.osDisk.managedDisk</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.managedDisk.storageAccountType">.spec.template.osDisk.managedDisk.storageAccountType</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.osType">.spec.template.osDisk.osType</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.sshPublicKey">.spec.template.sshPublicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SSHPublicKey is the SSH public key string base64 encoded to add to a Virtual Machine</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.terminateNotificationTimeout">.spec.template.terminateNotificationTimeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>TerminateNotificationTimeout enables or disables VMSS scheduled events termination notification with specified timeout allowed values are between 5 and 15 (mins)</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.vmSize">.spec.template.vmSize</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>VMSize is the size of the Virtual Machine to build. See <a href="https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/createorupdate#virtualmachinesizetypes">https://docs.microsoft.com/en-us/rest/api/compute/virtualmachines/createorupdate#virtualmachinesizetypes</a></p>

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
<p>AzureMachinePoolStatus defines the observed state of AzureMachinePool</p>

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
<p>Conditions defines current service state of the AzureMachinePool.</p>

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
<h3 class="property-path" id="v1alpha3-.status.failureMessage">.status.failureMessage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FailureMessage will be set in the event that there is a terminal problem reconciling the MachinePool and will contain a more verbose string suitable for logging and human consumption.
 This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the MachinePool&rsquo;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.
 Any transient errors that occur during the reconciliation of MachinePools can be added as events to the MachinePool object and/or logged in the controller&rsquo;s output.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.failureReason">.status.failureReason</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FailureReason will be set in the event that there is a terminal problem reconciling the MachinePool and will contain a succinct value suitable for machine interpretation.
 This field should not be set for transitive errors that a controller faces that are expected to be fixed automatically over time (like service outages), but instead indicate that something is fundamentally wrong with the MachinePool&rsquo;s spec or the configuration of the controller, and that manual intervention is required. Examples of terminal errors would be invalid combinations of settings in the spec, values that are unsupported by the controller, or the responsible controller itself being critically misconfigured.
 Any transient errors that occur during the reconciliation of MachinePools can be added as events to the MachinePool object and/or logged in the controller&rsquo;s output.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.provisioningState">.status.provisioningState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProvisioningState is the provisioning state of the Azure virtual machine.</p>

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

</div>

<div class="property-description">
<p>Ready is true when the provider resource is ready.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.replicas">.status.replicas</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Replicas is the most recently observed number of replicas.</p>

</div>

</div>
</div>


</div>



