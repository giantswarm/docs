---
title: AzureMachinePool CRD schema reference (group infrastructure.cluster.x-k8s.io)
linkTitle: AzureMachinePool
description: |
  AzureMachinePool is the Schema for the azuremachinepools API.
weight: 100
crd:
  name_camelcase: AzureMachinePool
  name_plural: azuremachinepools
  name_singular: azuremachinepool
  group: infrastructure.cluster.x-k8s.io
  technical_name: azuremachinepools.infrastructure.cluster.x-k8s.io
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
    - azure
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
aliases:
  - /use-the-api/management-api/crd/azuremachinepools.infrastructure.cluster.x-k8s.io/
  - /reference/cp-k8s-api/azuremachinepools.infrastructure.cluster.x-k8s.io/
technical_name: azuremachinepools.infrastructure.cluster.x-k8s.io
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v5.0.0
---

# AzureMachinePool


<p class="crd-description">AzureMachinePool is the Schema for the azuremachinepools API.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">azuremachinepools.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">azuremachinepool</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">azuremachinepools</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha3" title="Show schema for version v1alpha3">v1alpha3</a><a class="version" href="#v1alpha4" title="Show schema for version v1alpha4">v1alpha4</a><a class="version" href="#v1beta1" title="Show schema for version v1beta1">v1beta1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha3">Version v1alpha3</h2>


<h3 id="crd-example-v1alpha3">Example CR</h3>

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureMachinePool
metadata:
  labels:
    azure-operator.giantswarm.io/version: 5.3.1
    cluster.x-k8s.io/cluster-name: mmh5x
    giantswarm.io/cluster: mmh5x
    giantswarm.io/machine-pool: w86vu
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 14.1.0
  name: w86vu
  namespace: org-giantswarm
spec:
  identity: None
  location: westeurope
  providerID: azure:///subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/mmh5x/providers/Microsoft.Compute/virtualMachineScaleSets/nodepool-w86vu
  providerIDList:
    - azure:///subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/mmh5x/providers/Microsoft.Compute/virtualMachineScaleSets/nodepool-w86vu/virtualMachines/0
    - azure:///subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/mmh5x/providers/Microsoft.Compute/virtualMachineScaleSets/nodepool-w86vu/virtualMachines/1
    - azure:///subscriptions/aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee/resourceGroups/mmh5x/providers/Microsoft.Compute/virtualMachineScaleSets/nodepool-w86vu/virtualMachines/2
  template:
    dataDisks:
      - diskSizeGB: 100
        lun: 21
        nameSuffix: docker
      - diskSizeGB: 100
        lun: 22
        nameSuffix: kubelet
    osDisk:
      diskSizeGB: 0
      managedDisk:
        storageAccountType: Premium_LRS
      osType: ""
    sshPublicKey: ""
    vmSize: Standard_D4s_v3
```


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
<p>AzureMachinePoolSpec defines the desired state of AzureMachinePool.</p>

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
<h3 class="property-path" id="v1alpha3-.spec.identity">.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the Virtual Machine Scale Set. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

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
<h3 class="property-path" id="v1alpha3-.spec.roleAssignmentName">.spec.roleAssignmentName</h3>
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
<p>Template contains the details used to build a replica virtual machine within the Machine Pool.</p>

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
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].managedDisk">.spec.template.dataDisks[*].managedDisk</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.dataDisks[*].managedDisk.storageAccountType">.spec.template.dataDisks[*].managedDisk.storageAccountType</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.managedDisk.diskEncryptionSet">.spec.template.osDisk.managedDisk.diskEncryptionSet</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.osDisk.managedDisk.diskEncryptionSet.id</h3>
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
<h3 class="property-path" id="v1alpha3-.spec.template.securityProfile">.spec.template.securityProfile</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.securityProfile.encryptionAtHost">.spec.template.securityProfile.encryptionAtHost</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spotVMOptions">.spec.template.spotVMOptions</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.template.spotVMOptions.maxPrice">.spec.template.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.userAssignedIdentities">.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachinePool. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.userAssignedIdentities[*]">.spec.userAssignedIdentities[*]</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.userAssignedIdentities[*].providerID">.spec.userAssignedIdentities[*].providerID</h3>
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

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolStatus defines the observed state of AzureMachinePool.</p>

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
<h3 class="property-path" id="v1alpha3-.status.instances">.status.instances</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Instances is the VM instance status for each VM in the VMSS</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*]">.status.instances[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolInstanceStatus provides status information for each instance in the VMSS.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].instanceID">.status.instances[*].instanceID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceID is the identification of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].instanceName">.status.instances[*].instanceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceName is the name of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].latestModelApplied">.status.instances[*].latestModelApplied</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>LatestModelApplied indicates the instance is running the most up-to-date VMSS model. A VMSS model describes the image version the VM is running. If the instance is not running the latest model, it means the instance may not be running the version of Kubernetes the Machine Pool has specified and needs to be updated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].providerID">.status.instances[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the provider identification of the VMSS Instance</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].provisioningState">.status.instances[*].provisioningState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProvisioningState is the provisioning state of the Azure virtual machine instance.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.instances[*].version">.status.instances[*].version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version defines the Kubernetes version for the VM Instance</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.longRunningOperationState">.status.longRunningOperationState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LongRunningOperationState saves the state for an Azure long running operations so it can be continued on the next reconciliation loop.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.longRunningOperationState.futureData">.status.longRunningOperationState.futureData</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FutureData is the base64 url encoded json Azure AutoRest Future.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.longRunningOperationState.name">.status.longRunningOperationState.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the name of the Azure resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.longRunningOperationState.resourceGroup">.status.longRunningOperationState.resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ResourceGroup is the Azure resource group for the resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.longRunningOperationState.type">.status.longRunningOperationState.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type describes the type of future, update, create, delete, etc.</p>

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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.version">.status.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version is the Kubernetes version for the current VMSS model</p>

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
<p>AzureMachinePoolSpec defines the desired state of AzureMachinePool.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.additionalTags">.spec.additionalTags</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.identity">.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the Virtual Machine Scale Set. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.location">.spec.location</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.nodeDrainTimeout">.spec.nodeDrainTimeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>NodeDrainTimeout is the total amount of time that the controller will spend on draining a node. The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from <code>kubectl drain --timeout</code></p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.providerID">.spec.providerID</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.providerIDList">.spec.providerIDList</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.providerIDList[*]">.spec.providerIDList[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.roleAssignmentName">.spec.roleAssignmentName</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy">.spec.strategy</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The deployment strategy to use to replace existing AzureMachinePoolMachines with new ones.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy.rollingUpdate">.spec.strategy.rollingUpdate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Rolling update config params. Present only if MachineDeploymentStrategyType = RollingUpdate.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy.rollingUpdate.deletePolicy">.spec.strategy.rollingUpdate.deletePolicy</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DeletePolicy defines the policy used by the MachineDeployment to identify nodes to delete when downscaling. Valid values are &ldquo;Random, &ldquo;Newest&rdquo;, &ldquo;Oldest&rdquo; When no value is supplied, the default is Oldest</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy.rollingUpdate.maxSurge">.spec.strategy.rollingUpdate.maxSurge</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>The maximum number of machines that can be scheduled above the desired number of machines. Value can be an absolute number (ex: 5) or a percentage of desired machines (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 1. Example: when this is set to 30%, the new MachineSet can be scaled up immediately when the rolling update starts, such that the total number of old and new machines do not exceed 130% of desired machines. Once old machines have been killed, new MachineSet can be scaled up further, ensuring that total number of machines running at any time during the update is at most 130% of desired machines.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy.rollingUpdate.maxUnavailable">.spec.strategy.rollingUpdate.maxUnavailable</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>The maximum number of machines that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired machines (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 0. Example: when this is set to 30%, the old MachineSet can be scaled down to 70% of desired machines immediately when the rolling update starts. Once new machines are ready, old MachineSet can be scaled down further, followed by scaling up the new MachineSet, ensuring that the total number of machines available at all times during the update is at least 70% of desired machines.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.strategy.type">.spec.strategy.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type of deployment. Currently the only supported strategy is RollingUpdate</p>

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
<p>Template contains the details used to build a replica virtual machine within the Machine Pool</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.acceleratedNetworking">.spec.template.acceleratedNetworking</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks">.spec.template.dataDisks</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*]">.spec.template.dataDisks[*]</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].cachingType">.spec.template.dataDisks[*].cachingType</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].diskSizeGB">.spec.template.dataDisks[*].diskSizeGB</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].lun">.spec.template.dataDisks[*].lun</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].managedDisk">.spec.template.dataDisks[*].managedDisk</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].managedDisk.storageAccountType">.spec.template.dataDisks[*].managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.dataDisks[*].nameSuffix">.spec.template.dataDisks[*].nameSuffix</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image">.spec.template.image</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.image.id">.spec.template.image.id</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace">.spec.template.image.marketplace</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace.offer">.spec.template.image.marketplace.offer</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace.publisher">.spec.template.image.marketplace.publisher</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace.sku">.spec.template.image.marketplace.sku</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace.thirdPartyImage">.spec.template.image.marketplace.thirdPartyImage</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.marketplace.version">.spec.template.image.marketplace.version</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery">.spec.template.image.sharedGallery</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.gallery">.spec.template.image.sharedGallery.gallery</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.name">.spec.template.image.sharedGallery.name</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.offer">.spec.template.image.sharedGallery.offer</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.publisher">.spec.template.image.sharedGallery.publisher</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.resourceGroup">.spec.template.image.sharedGallery.resourceGroup</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.sku">.spec.template.image.sharedGallery.sku</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.subscriptionID">.spec.template.image.sharedGallery.subscriptionID</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.image.sharedGallery.version">.spec.template.image.sharedGallery.version</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk">.spec.template.osDisk</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.cachingType">.spec.template.osDisk.cachingType</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.diffDiskSettings">.spec.template.osDisk.diffDiskSettings</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.diffDiskSettings.option">.spec.template.osDisk.diffDiskSettings.option</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.diskSizeGB">.spec.template.osDisk.diskSizeGB</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.managedDisk">.spec.template.osDisk.managedDisk</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.managedDisk.diskEncryptionSet">.spec.template.osDisk.managedDisk.diskEncryptionSet</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.osDisk.managedDisk.diskEncryptionSet.id</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.managedDisk.storageAccountType">.spec.template.osDisk.managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.osDisk.osType">.spec.template.osDisk.osType</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.securityProfile">.spec.template.securityProfile</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.securityProfile.encryptionAtHost">.spec.template.securityProfile.encryptionAtHost</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spotVMOptions">.spec.template.spotVMOptions</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.spotVMOptions.maxPrice">.spec.template.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.sshPublicKey">.spec.template.sshPublicKey</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.subnetName">.spec.template.subnetName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SubnetName selects the Subnet where the VMSS will be placed</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.template.terminateNotificationTimeout">.spec.template.terminateNotificationTimeout</h3>
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
<h3 class="property-path" id="v1alpha4-.spec.template.vmSize">.spec.template.vmSize</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.userAssignedIdentities">.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachinePool. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.userAssignedIdentities[*]">.spec.userAssignedIdentities[*]</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.userAssignedIdentities[*].providerID">.spec.userAssignedIdentities[*].providerID</h3>
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

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolStatus defines the observed state of AzureMachinePool.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.conditions">.status.conditions</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*]">.status.conditions[*]</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].lastTransitionTime">.status.conditions[*].lastTransitionTime</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].message">.status.conditions[*].message</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].reason">.status.conditions[*].reason</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].severity">.status.conditions[*].severity</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].status">.status.conditions[*].status</h3>
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
<h3 class="property-path" id="v1alpha4-.status.conditions[*].type">.status.conditions[*].type</h3>
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
<h3 class="property-path" id="v1alpha4-.status.failureMessage">.status.failureMessage</h3>
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
<h3 class="property-path" id="v1alpha4-.status.failureReason">.status.failureReason</h3>
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
<h3 class="property-path" id="v1alpha4-.status.image">.status.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is the current image used in the AzureMachinePool. When the spec image is nil, this image is populated with the details of the defaulted Azure Marketplace &ldquo;capi&rdquo; offer.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.id">.status.image.id</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace">.status.image.marketplace</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace.offer">.status.image.marketplace.offer</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace.publisher">.status.image.marketplace.publisher</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace.sku">.status.image.marketplace.sku</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace.thirdPartyImage">.status.image.marketplace.thirdPartyImage</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.marketplace.version">.status.image.marketplace.version</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery">.status.image.sharedGallery</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.gallery">.status.image.sharedGallery.gallery</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.name">.status.image.sharedGallery.name</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.offer">.status.image.sharedGallery.offer</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.publisher">.status.image.sharedGallery.publisher</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.resourceGroup">.status.image.sharedGallery.resourceGroup</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.sku">.status.image.sharedGallery.sku</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.subscriptionID">.status.image.sharedGallery.subscriptionID</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.image.sharedGallery.version">.status.image.sharedGallery.version</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances">.status.instances</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Instances is the VM instance status for each VM in the VMSS</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*]">.status.instances[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolInstanceStatus provides status information for each instance in the VMSS.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].instanceID">.status.instances[*].instanceID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceID is the identification of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].instanceName">.status.instances[*].instanceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceName is the name of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].latestModelApplied">.status.instances[*].latestModelApplied</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>LatestModelApplied indicates the instance is running the most up-to-date VMSS model. A VMSS model describes the image version the VM is running. If the instance is not running the latest model, it means the instance may not be running the version of Kubernetes the Machine Pool has specified and needs to be updated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].providerID">.status.instances[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the provider identification of the VMSS Instance</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].provisioningState">.status.instances[*].provisioningState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProvisioningState is the provisioning state of the Azure virtual machine instance.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.instances[*].version">.status.instances[*].version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version defines the Kubernetes version for the VM Instance</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates">.status.longRunningOperationStates</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>LongRunningOperationStates saves the state for Azure long-running operations so they can be continued on the next reconciliation loop.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*]">.status.longRunningOperationStates[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Future contains the data needed for an Azure long-running operation to continue across reconcile loops.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*].data">.status.longRunningOperationStates[*].data</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Data is the base64 url encoded json Azure AutoRest Future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*].name">.status.longRunningOperationStates[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*].resourceGroup">.status.longRunningOperationStates[*].resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ResourceGroup is the Azure resource group for the resource.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*].serviceName">.status.longRunningOperationStates[*].serviceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.longRunningOperationStates[*].type">.status.longRunningOperationStates[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type describes the type of future, such as update, create, delete, etc.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.provisioningState">.status.provisioningState</h3>
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
<h3 class="property-path" id="v1alpha4-.status.ready">.status.ready</h3>
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
<h3 class="property-path" id="v1alpha4-.status.replicas">.status.replicas</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.version">.status.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version is the Kubernetes version for the current VMSS model</p>

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
<p>AzureMachinePoolSpec defines the desired state of AzureMachinePool.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.additionalTags">.spec.additionalTags</h3>
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
<h3 class="property-path" id="v1beta1-.spec.identity">.spec.identity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Identity is the type of identity used for the Virtual Machine Scale Set. The type &lsquo;SystemAssigned&rsquo; is an implicitly created identity. The generated identity will be assigned a Subscription contributor role. The type &lsquo;UserAssigned&rsquo; is a standalone Azure resource provided by the user and assigned to the VM</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.location">.spec.location</h3>
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
<h3 class="property-path" id="v1beta1-.spec.nodeDrainTimeout">.spec.nodeDrainTimeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>NodeDrainTimeout is the total amount of time that the controller will spend on draining a node. The default value is 0, meaning that the node can be drained without any time limitations. NOTE: NodeDrainTimeout is different from <code>kubectl drain --timeout</code></p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.providerID">.spec.providerID</h3>
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
<h3 class="property-path" id="v1beta1-.spec.providerIDList">.spec.providerIDList</h3>
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
<h3 class="property-path" id="v1beta1-.spec.providerIDList[*]">.spec.providerIDList[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.roleAssignmentName">.spec.roleAssignmentName</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy">.spec.strategy</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The deployment strategy to use to replace existing AzureMachinePoolMachines with new ones.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy.rollingUpdate">.spec.strategy.rollingUpdate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Rolling update config params. Present only if MachineDeploymentStrategyType = RollingUpdate.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy.rollingUpdate.deletePolicy">.spec.strategy.rollingUpdate.deletePolicy</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DeletePolicy defines the policy used by the MachineDeployment to identify nodes to delete when downscaling. Valid values are &ldquo;Random, &ldquo;Newest&rdquo;, &ldquo;Oldest&rdquo; When no value is supplied, the default is Oldest</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy.rollingUpdate.maxSurge">.spec.strategy.rollingUpdate.maxSurge</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>The maximum number of machines that can be scheduled above the desired number of machines. Value can be an absolute number (ex: 5) or a percentage of desired machines (ex: 10%). This can not be 0 if MaxUnavailable is 0. Absolute number is calculated from percentage by rounding up. Defaults to 1. Example: when this is set to 30%, the new MachineSet can be scaled up immediately when the rolling update starts, such that the total number of old and new machines do not exceed 130% of desired machines. Once old machines have been killed, new MachineSet can be scaled up further, ensuring that total number of machines running at any time during the update is at most 130% of desired machines.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy.rollingUpdate.maxUnavailable">.spec.strategy.rollingUpdate.maxUnavailable</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>The maximum number of machines that can be unavailable during the update. Value can be an absolute number (ex: 5) or a percentage of desired machines (ex: 10%). Absolute number is calculated from percentage by rounding down. This can not be 0 if MaxSurge is 0. Defaults to 0. Example: when this is set to 30%, the old MachineSet can be scaled down to 70% of desired machines immediately when the rolling update starts. Once new machines are ready, old MachineSet can be scaled down further, followed by scaling up the new MachineSet, ensuring that the total number of machines available at all times during the update is at least 70% of desired machines.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.strategy.type">.spec.strategy.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type of deployment. Currently the only supported strategy is RollingUpdate</p>

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
<p>Template contains the details used to build a replica virtual machine within the Machine Pool</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.acceleratedNetworking">.spec.template.acceleratedNetworking</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks">.spec.template.dataDisks</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*]">.spec.template.dataDisks[*]</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].cachingType">.spec.template.dataDisks[*].cachingType</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].diskSizeGB">.spec.template.dataDisks[*].diskSizeGB</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].lun">.spec.template.dataDisks[*].lun</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].managedDisk">.spec.template.dataDisks[*].managedDisk</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id">.spec.template.dataDisks[*].managedDisk.diskEncryptionSet.id</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].managedDisk.storageAccountType">.spec.template.dataDisks[*].managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.dataDisks[*].nameSuffix">.spec.template.dataDisks[*].nameSuffix</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image">.spec.template.image</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.image.id">.spec.template.image.id</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace">.spec.template.image.marketplace</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace.offer">.spec.template.image.marketplace.offer</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace.publisher">.spec.template.image.marketplace.publisher</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace.sku">.spec.template.image.marketplace.sku</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace.thirdPartyImage">.spec.template.image.marketplace.thirdPartyImage</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.marketplace.version">.spec.template.image.marketplace.version</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery">.spec.template.image.sharedGallery</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.gallery">.spec.template.image.sharedGallery.gallery</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.name">.spec.template.image.sharedGallery.name</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.offer">.spec.template.image.sharedGallery.offer</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.publisher">.spec.template.image.sharedGallery.publisher</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.resourceGroup">.spec.template.image.sharedGallery.resourceGroup</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.sku">.spec.template.image.sharedGallery.sku</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.subscriptionID">.spec.template.image.sharedGallery.subscriptionID</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.image.sharedGallery.version">.spec.template.image.sharedGallery.version</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.osDisk">.spec.template.osDisk</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.cachingType">.spec.template.osDisk.cachingType</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.diffDiskSettings">.spec.template.osDisk.diffDiskSettings</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.diffDiskSettings.option">.spec.template.osDisk.diffDiskSettings.option</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.diskSizeGB">.spec.template.osDisk.diskSizeGB</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.managedDisk">.spec.template.osDisk.managedDisk</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.managedDisk.diskEncryptionSet">.spec.template.osDisk.managedDisk.diskEncryptionSet</h3>
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

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.managedDisk.diskEncryptionSet.id">.spec.template.osDisk.managedDisk.diskEncryptionSet.id</h3>
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

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.managedDisk.storageAccountType">.spec.template.osDisk.managedDisk.storageAccountType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.osDisk.osType">.spec.template.osDisk.osType</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.securityProfile">.spec.template.securityProfile</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.securityProfile.encryptionAtHost">.spec.template.securityProfile.encryptionAtHost</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spotVMOptions">.spec.template.spotVMOptions</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.spotVMOptions.maxPrice">.spec.template.spotVMOptions.maxPrice</h3>
</div>
<div class="property-body">
<div class="property-meta">


</div>

<div class="property-description">
<p>MaxPrice defines the maximum price the user is willing to pay for Spot VM instances</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.sshPublicKey">.spec.template.sshPublicKey</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.subnetName">.spec.template.subnetName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>SubnetName selects the Subnet where the VMSS will be placed</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.template.terminateNotificationTimeout">.spec.template.terminateNotificationTimeout</h3>
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
<h3 class="property-path" id="v1beta1-.spec.template.vmSize">.spec.template.vmSize</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.userAssignedIdentities">.spec.userAssignedIdentities</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>UserAssignedIdentities is a list of standalone Azure identities provided by the user The lifecycle of a user-assigned identity is managed separately from the lifecycle of the AzureMachinePool. See <a href="https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli">https://docs.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-to-manage-ua-identity-cli</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.userAssignedIdentities[*]">.spec.userAssignedIdentities[*]</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.userAssignedIdentities[*].providerID">.spec.userAssignedIdentities[*].providerID</h3>
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

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolStatus defines the observed state of AzureMachinePool.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.conditions">.status.conditions</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*]">.status.conditions[*]</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*].lastTransitionTime">.status.conditions[*].lastTransitionTime</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.conditions[*].message">.status.conditions[*].message</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*].reason">.status.conditions[*].reason</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*].severity">.status.conditions[*].severity</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*].status">.status.conditions[*].status</h3>
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
<h3 class="property-path" id="v1beta1-.status.conditions[*].type">.status.conditions[*].type</h3>
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
<h3 class="property-path" id="v1beta1-.status.failureMessage">.status.failureMessage</h3>
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
<h3 class="property-path" id="v1beta1-.status.failureReason">.status.failureReason</h3>
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
<h3 class="property-path" id="v1beta1-.status.image">.status.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Image is the current image used in the AzureMachinePool. When the spec image is nil, this image is populated with the details of the defaulted Azure Marketplace &ldquo;capi&rdquo; offer.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.id">.status.image.id</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace">.status.image.marketplace</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace.offer">.status.image.marketplace.offer</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace.publisher">.status.image.marketplace.publisher</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace.sku">.status.image.marketplace.sku</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace.thirdPartyImage">.status.image.marketplace.thirdPartyImage</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.marketplace.version">.status.image.marketplace.version</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery">.status.image.sharedGallery</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.gallery">.status.image.sharedGallery.gallery</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.name">.status.image.sharedGallery.name</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.offer">.status.image.sharedGallery.offer</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.publisher">.status.image.sharedGallery.publisher</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.resourceGroup">.status.image.sharedGallery.resourceGroup</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.sku">.status.image.sharedGallery.sku</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.subscriptionID">.status.image.sharedGallery.subscriptionID</h3>
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

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.image.sharedGallery.version">.status.image.sharedGallery.version</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances">.status.instances</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Instances is the VM instance status for each VM in the VMSS</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*]">.status.instances[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureMachinePoolInstanceStatus provides status information for each instance in the VMSS.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].instanceID">.status.instances[*].instanceID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceID is the identification of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].instanceName">.status.instances[*].instanceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>InstanceName is the name of the Machine Instance within the VMSS</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].latestModelApplied">.status.instances[*].latestModelApplied</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>LatestModelApplied indicates the instance is running the most up-to-date VMSS model. A VMSS model describes the image version the VM is running. If the instance is not running the latest model, it means the instance may not be running the version of Kubernetes the Machine Pool has specified and needs to be updated.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].providerID">.status.instances[*].providerID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProviderID is the provider identification of the VMSS Instance</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].provisioningState">.status.instances[*].provisioningState</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ProvisioningState is the provisioning state of the Azure virtual machine instance.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.instances[*].version">.status.instances[*].version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version defines the Kubernetes version for the VM Instance</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates">.status.longRunningOperationStates</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>LongRunningOperationStates saves the state for Azure long-running operations so they can be continued on the next reconciliation loop.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*]">.status.longRunningOperationStates[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Future contains the data needed for an Azure long-running operation to continue across reconcile loops.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*].data">.status.longRunningOperationStates[*].data</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Data is the base64 url encoded json Azure AutoRest Future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*].name">.status.longRunningOperationStates[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the Azure resource. Together with the service name, this forms the unique identifier for the future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*].resourceGroup">.status.longRunningOperationStates[*].resourceGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ResourceGroup is the Azure resource group for the resource.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*].serviceName">.status.longRunningOperationStates[*].serviceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ServiceName is the name of the Azure service. Together with the name of the resource, this forms the unique identifier for the future.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.longRunningOperationStates[*].type">.status.longRunningOperationStates[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type describes the type of future, such as update, create, delete, etc.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.provisioningState">.status.provisioningState</h3>
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
<h3 class="property-path" id="v1beta1-.status.ready">.status.ready</h3>
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
<h3 class="property-path" id="v1beta1-.status.replicas">.status.replicas</h3>
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.version">.status.version</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Version is the Kubernetes version for the current VMSS model</p>

</div>

</div>
</div>





</div>



