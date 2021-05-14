---
title: HAProxyLoadBalancer CRD schema reference
linkTitle: HAProxyLoadBalancer
technical_name: haproxyloadbalancers.infrastructure.cluster.x-k8s.io
description:   HAProxyLoadBalancer is the Schema for the haproxyloadbalancers API DEPRECATED: will be removed in v1alpha4
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.23.0
layout: crd
aliases:
  - /reference/cp-k8s-api/haproxyloadbalancers.infrastructure.cluster.x-k8s.io/
---

# HAProxyLoadBalancer


<p class="crd-description">HAProxyLoadBalancer is the Schema for the haproxyloadbalancers API DEPRECATED: will be removed in v1alpha4</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">haproxyloadbalancers.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">haproxyloadbalancer</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">haproxyloadbalancers</dd>
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
<p>HAProxyLoadBalancerSpec defines the desired state of HAProxyLoadBalancer.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.user">.spec.user</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SSHUser specifies the name of a user that is granted remote access to the deployed VM.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.user.authorizedKeys">.spec.user.authorizedKeys</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AuthorizedKeys is one or more public SSH keys that grant remote access.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.user.authorizedKeys[*]">.spec.user.authorizedKeys[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.user.name">.spec.user.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the SSH user.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration">.spec.virtualMachineConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>VirtualMachineConfiguration is information used to deploy a load balancer VM.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.cloneMode">.spec.virtualMachineConfiguration.cloneMode</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CloneMode specifies the type of clone operation. The LinkedClone mode is only support for templates that have at least one snapshot. If the template has no snapshots, then CloneMode defaults to FullClone. When LinkedClone mode is enabled the DiskGiB field is ignored as it is not possible to expand disks of linked clones. Defaults to LinkedClone, but fails gracefully to FullClone if the source of the clone operation has no snapshots.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.customVMXKeys">.spec.virtualMachineConfiguration.customVMXKeys</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>CustomVMXKeys is a dictionary of advanced VMX options that can be set on VM Defaults to empty map</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.datacenter">.spec.virtualMachineConfiguration.datacenter</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Datacenter is the name or inventory path of the datacenter in which the virtual machine is created/located.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.datastore">.spec.virtualMachineConfiguration.datastore</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Datastore is the name or inventory path of the datastore in which the virtual machine is created/located.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.diskGiB">.spec.virtualMachineConfiguration.diskGiB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>DiskGiB is the size of a virtual machine&rsquo;s disk, in GiB. Defaults to the eponymous property value in the template from which the virtual machine is cloned.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.folder">.spec.virtualMachineConfiguration.folder</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Folder is the name or inventory path of the folder in which the virtual machine is created/located.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.memoryMiB">.spec.virtualMachineConfiguration.memoryMiB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MemoryMiB is the size of a virtual machine&rsquo;s memory, in MiB. Defaults to the eponymous property value in the template from which the virtual machine is cloned.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network">.spec.virtualMachineConfiguration.network</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Network is the network configuration for this machine&rsquo;s VM.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices">.spec.virtualMachineConfiguration.network.devices</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Devices is the list of network devices used by the virtual machine. TODO(akutz) Make sure at least one network matches the             ClusterSpec.CloudProviderConfiguration.Network.Name</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*]">.spec.virtualMachineConfiguration.network.devices[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NetworkDeviceSpec defines the network configuration for a virtual machine&rsquo;s network device.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].deviceName">.spec.virtualMachineConfiguration.network.devices[*].deviceName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DeviceName may be used to explicitly assign a name to the network device as it exists in the guest operating system.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].dhcp4">.spec.virtualMachineConfiguration.network.devices[*].dhcp4</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>DHCP4 is a flag that indicates whether or not to use DHCP for IPv4 on this device. If true then IPAddrs should not contain any IPv4 addresses.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].dhcp6">.spec.virtualMachineConfiguration.network.devices[*].dhcp6</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>DHCP6 is a flag that indicates whether or not to use DHCP for IPv6 on this device. If true then IPAddrs should not contain any IPv6 addresses.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].gateway4">.spec.virtualMachineConfiguration.network.devices[*].gateway4</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Gateway4 is the IPv4 gateway used by this device. Required when DHCP4 is false.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].gateway6">.spec.virtualMachineConfiguration.network.devices[*].gateway6</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Gateway4 is the IPv4 gateway used by this device. Required when DHCP6 is false.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].ipAddrs">.spec.virtualMachineConfiguration.network.devices[*].ipAddrs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>IPAddrs is a list of one or more IPv4 and/or IPv6 addresses to assign to this device. Required when DHCP4 and DHCP6 are both false.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].ipAddrs[*]">.spec.virtualMachineConfiguration.network.devices[*].ipAddrs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].macAddr">.spec.virtualMachineConfiguration.network.devices[*].macAddr</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>MACAddr is the MAC address used by this device. It is generally a good idea to omit this field and allow a MAC address to be generated. Please note that this value must use the VMware OUI to work with the in-tree vSphere cloud provider.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].mtu">.spec.virtualMachineConfiguration.network.devices[*].mtu</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MTU is the device’s Maximum Transmission Unit size in bytes.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].nameservers">.spec.virtualMachineConfiguration.network.devices[*].nameservers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Nameservers is a list of IPv4 and/or IPv6 addresses used as DNS nameservers. Please note that Linux allows only three nameservers (<a href="https://linux.die.net/man/5/resolv.conf">https://linux.die.net/man/5/resolv.conf</a>).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].nameservers[*]">.spec.virtualMachineConfiguration.network.devices[*].nameservers[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].networkName">.spec.virtualMachineConfiguration.network.devices[*].networkName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NetworkName is the name of the vSphere network to which the device will be connected.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].routes">.spec.virtualMachineConfiguration.network.devices[*].routes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Routes is a list of optional, static routes applied to the device.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].routes[*]">.spec.virtualMachineConfiguration.network.devices[*].routes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NetworkRouteSpec defines a static network route.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].routes[*].metric">.spec.virtualMachineConfiguration.network.devices[*].routes[*].metric</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Metric is the weight/priority of the route.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].routes[*].to">.spec.virtualMachineConfiguration.network.devices[*].routes[*].to</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>To is an IPv4 or IPv6 address.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].routes[*].via">.spec.virtualMachineConfiguration.network.devices[*].routes[*].via</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Via is an IPv4 or IPv6 address.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].searchDomains">.spec.virtualMachineConfiguration.network.devices[*].searchDomains</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SearchDomains is a list of search domains used when resolving IP addresses with DNS.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.devices[*].searchDomains[*]">.spec.virtualMachineConfiguration.network.devices[*].searchDomains[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.preferredAPIServerCidr">.spec.virtualMachineConfiguration.network.preferredAPIServerCidr</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PreferredAPIServeCIDR is the preferred CIDR for the Kubernetes API server endpoint on this machine</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.routes">.spec.virtualMachineConfiguration.network.routes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Routes is a list of optional, static routes applied to the virtual machine.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.routes[*]">.spec.virtualMachineConfiguration.network.routes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NetworkRouteSpec defines a static network route.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.routes[*].metric">.spec.virtualMachineConfiguration.network.routes[*].metric</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Metric is the weight/priority of the route.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.routes[*].to">.spec.virtualMachineConfiguration.network.routes[*].to</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>To is an IPv4 or IPv6 address.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.network.routes[*].via">.spec.virtualMachineConfiguration.network.routes[*].via</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Via is an IPv4 or IPv6 address.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.numCPUs">.spec.virtualMachineConfiguration.numCPUs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>NumCPUs is the number of virtual processors in a virtual machine. Defaults to the eponymous property value in the template from which the virtual machine is cloned.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.numCoresPerSocket">.spec.virtualMachineConfiguration.numCoresPerSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>NumCPUs is the number of cores among which to distribute CPUs in this virtual machine. Defaults to the eponymous property value in the template from which the virtual machine is cloned.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.resourcePool">.spec.virtualMachineConfiguration.resourcePool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ResourcePool is the name or inventory path of the resource pool in which the virtual machine is created/located.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.server">.spec.virtualMachineConfiguration.server</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Server is the IP address or FQDN of the vSphere server on which the virtual machine is created/located.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.snapshot">.spec.virtualMachineConfiguration.snapshot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Snapshot is the name of the snapshot from which to create a linked clone. This field is ignored if LinkedClone is not enabled. Defaults to the source&rsquo;s current snapshot.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.storagePolicyName">.spec.virtualMachineConfiguration.storagePolicyName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>StoragePolicyName of the storage policy to use with this Virtual Machine</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.template">.spec.virtualMachineConfiguration.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Template is the name or inventory path of the template used to clone the virtual machine.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.virtualMachineConfiguration.thumbprint">.spec.virtualMachineConfiguration.thumbprint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Thumbprint is the colon-separated SHA-1 checksum of the given vCenter server&rsquo;s host certificate When this is set to empty, this VirtualMachine would be created without TLS certificate validation of the communication between Cluster API Provider vSphere and the VMware vCenter server.</p>

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
<p>HAProxyLoadBalancerStatus defines the observed state of HAProxyLoadBalancer.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.address">.status.address</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Address is the IP address or DNS name of the load balancer.
 This field is required as part of the Portable Load Balancer model and is inspected via an unstructured reader by other controllers to determine the status of the load balancer.</p>

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
<p>Ready indicates whether or not the load balancer is ready.
 This field is required as part of the Portable Load Balancer model and is inspected via an unstructured reader by other controllers to determine the status of the load balancer.</p>

</div>

</div>
</div>





</div>



