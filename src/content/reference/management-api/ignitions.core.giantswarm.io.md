---
title: Ignition CRD schema reference
linktitle: Ignition
technical_name: ignitions.core.giantswarm.io
description:   Ignition is a Kubernetes resource (CR) which is based on the Ignition CRD defined above. 
   An example Ignition resource can be viewed here https://github.com/giantswarm/apiextensions/blob/master/docs/cr/core.giantswarm.io_v1alpha1_ignition.yaml
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.14.1
layout: "crd"
aliases:
  - /reference/cp-k8s-api/ignitions.core.giantswarm.io/
---

# Ignition


<p class="crd-description">Ignition is a Kubernetes resource (CR) which is based on the Ignition CRD defined above. 
 An example Ignition resource can be viewed here https://github.com/giantswarm/apiextensions/blob/master/docs/cr/core.giantswarm.io_v1alpha1_ignition.yaml</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">ignitions.core.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">core.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">ignition</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">ignitions</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>
<pre class="crd-example-cr"><code class="language-yaml">
apiVersion: core.giantswarm.io/v1alpha1
kind: Ignition
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/ignitions.core.giantswarm.io/
  creationTimestamp: null
  name: abc12-master
spec:
  apiServerEncryptionKey: 5fd466f48df84f47bb8006b68f0355ba
  baseDomain: https://abc12.k8s.example.eu-west-1.aws.gigantic.io
  calico:
    cidr: &#34;16&#34;
    disable: false
    mtu: &#34;1430&#34;
    subnet: 10.250.0.0
  clusterID: abc12
  disableEncryptionAtRest: false
  docker:
    daemon:
      cidr: 172.100.0.1/16
    networkSetup:
      image: quay.io/giantswarm/k8s-setup-network-environment
  etcd:
    domain: https://etcd.abc12.k8s.example.eu-west-1.aws.gigantic.io
    port: 2379
    prefix: &#34;&#34;
  extension: {}
  ingress:
    disable: false
  isMaster: true
  kubernetes:
    api:
      domain: https://abc12.k8s.example.eu-west-1.aws.gigantic.io
      securePort: 443
    cloudProvider: aws
    dns:
      ip: 10.1.2.3/32
    domain: https://abc12.k8s.example.eu-west-1.aws.gigantic.io
    ipRange: 10.2.3.4/24
    kubelet:
      domain: https://abc12.k8s.example.eu-west-1.aws.gigantic.io
    oidc:
      clientID: abc12
      enabled: true
      groupsClaim: &#34;&#34;
      groupsPrefix: gs
      issuerUrl: https://giantswarm.io
      usernameClaim: &#34;&#34;
      usernamePrefix: gs
  provider: aws
  registry:
    domain: quay.io
    pullProgressDeadline: 10s
  sso:
    publicKey: ssh-rsa 1234567890
</code></pre>


<h3 id="property-details-v1alpha1">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.apiVersion">.apiVersion</h3>
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
<h3 class="property-path" id="v1alpha1-.kind">.kind</h3>
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
<h3 class="property-path" id="v1alpha1-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>IgnitionSpec is the interface which defines the input parameters for a newly rendered g8s ignition template.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.apiServerEncryptionKey">.spec.apiServerEncryptionKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>APIServerEncryptionKey is used in EncryptionConfiguration to encrypt Kubernetes secrets at rest.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.baseDomain">.spec.baseDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>BaseDomain is the base domain for all cluster services. For test installations, this may be in the form <clusterId>.k8s.<installation>.<region>.<provider>.gigantic.io.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.calico">.spec.calico</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Calico provides configuration for all calico-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.calico.cidr">.spec.calico.cidr</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CIDR is the CIDR-component of the IPv4 overlay subnetwork. Combined with Subnet below.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.calico.disable">.spec.calico.disable</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Disable can be set to true to disable Calico setup.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.calico.mtu">.spec.calico.mtu</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MTU is the maximum size of packets sent over Calico in bytes.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.calico.subnet">.spec.calico.subnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Subnet is the IP-component of the IPv4 overlay subnetwork. Combined with CIDR above.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.clusterID">.spec.clusterID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ClusterID is the name of the workload cluster to be created.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.disableEncryptionAtRest">.spec.disableEncryptionAtRest</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DisableEncryptionAtRest will disable secret encryption at rest when set to true.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.docker">.spec.docker</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Docker provides configuration for all calico-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.docker.daemon">.spec.docker.daemon</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Daemon provides information about the Docker daemon running on TC nodes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.docker.daemon.cidr">.spec.docker.daemon.cidr</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CIDR is the fully specified subnet used for DOCKER_OPT_BIP.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.docker.networkSetup">.spec.docker.networkSetup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NetworkSetup provides the Docker image to be used for network environment setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.docker.networkSetup.image">.spec.docker.networkSetup.image</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Image provides the Docker image to be used for network environment setup.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.etcd">.spec.etcd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Etcd provides configuration for all etcd-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.etcd.domain">.spec.etcd.domain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Domain is the domain of the etcd service.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.etcd.port">.spec.etcd.port</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Port is the port of the etcd service, usually 2379.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.etcd.prefix">.spec.etcd.prefix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Prefix is the prefix to add to all etcd keys created by Kubernetes.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension">.spec.extension</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Extension can be used to extend an ignition with extra configuration provided by the provider operator.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files">.spec.extension.files</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files is an optional array of files which will be rendered and added to the final node ignition.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*]">.spec.extension.files[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].content">.spec.extension.files[*].content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Content is the string containing a file with optional go-template-style replacements.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata">.spec.extension.files[*].metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Metadata is the filesystem metadata of the given file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.compression">.spec.extension.files[*].metadata.compression</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Compression allows a file to be passed in as a base64-encoded compressed string.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner">.spec.extension.files[*].metadata.owner</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Owner is the owner of the file.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.group">.spec.extension.files[*].metadata.owner.group</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Group is the group which owns the file.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.group.id">.spec.extension.files[*].metadata.owner.group.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the GID of the group.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.group.name">.spec.extension.files[*].metadata.owner.group.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the group.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.user">.spec.extension.files[*].metadata.owner.user</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>User is the user which owns the file.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.user.id">.spec.extension.files[*].metadata.owner.user.id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the UID of the user.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.owner.user.name">.spec.extension.files[*].metadata.owner.user.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the user.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.path">.spec.extension.files[*].metadata.path</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Path is the path of the file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.files[*].metadata.permissions">.spec.extension.files[*].metadata.permissions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Permissions is the numeric permissions applied to the file.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units">.spec.extension.units</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files is an optional array of systemd units which will be rendered and added to the final node ignition.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units[*]">.spec.extension.units[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units[*].content">.spec.extension.units[*].content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Content is the string containing a systemd unit with optional go-template-style replacements.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units[*].metadata">.spec.extension.units[*].metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Metadata is the filesystem metadata of the given file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units[*].metadata.enabled">.spec.extension.units[*].metadata.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Enabled indicates that the unit should be enabled by default.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.units[*].metadata.name">.spec.extension.units[*].metadata.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the unit on the filesystem and used in systemctl commands.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.users">.spec.extension.users</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files is an optional array of users which will be added to the final node ignition.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.users[*]">.spec.extension.users[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.users[*].name">.spec.extension.users[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the user to be added to the node via ignition.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.extension.users[*].publicKey">.spec.extension.users[*].publicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>PublicKey is the public key of the user to be added to the node via ignition.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.ingress">.spec.ingress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Ingress provides configuration for all ingress-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.ingress.disable">.spec.ingress.disable</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Disable will disable the ingress controller in the TC when true.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.isMaster">.spec.isMaster</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>IsMaster determines if the rendered ignition should contain master-specific configuration.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes">.spec.kubernetes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Kubernetes provides configuration for all Kubernetes-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.api">.spec.kubernetes.api</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>API holds information about the desired TC Kubernetes API.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.api.domain">.spec.kubernetes.api.domain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Domain is the domain of the API server.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.api.securePort">.spec.kubernetes.api.securePort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Secure port is the port on which the API will listen.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.cloudProvider">.spec.kubernetes.cloudProvider</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CloudProvider is the provider upon which the cluster is running. It is passed to API server as a flag.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.dns">.spec.kubernetes.dns</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DNS hold information about the in-cluster DNS service.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.dns.ip">.spec.kubernetes.dns.ip</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>IP is the IP of the in-cluster DNS service. Usually this is the same as the API server IP with the final component replaced with .10.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.domain">.spec.kubernetes.domain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Domain is the domain used for services running in the cluster. Usually this is &ldquo;cluster.local&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.ipRange">.spec.kubernetes.ipRange</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>IPRange is the range of IPs used for pod networking.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.kubelet">.spec.kubernetes.kubelet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Kubelet holds information about the kubelet running on nodes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.kubelet.domain">.spec.kubernetes.kubelet.domain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Domain is the domain of the network.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc">.spec.kubernetes.oidc</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>OIDC hold configuration which will be applied to the apiserver OIDC flags.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.clientID">.spec.kubernetes.oidc.clientID</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The client ID for the OpenID Connect client, must be set if IssuerURL is set.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.enabled">.spec.kubernetes.oidc.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Enabled indicates that the OIDC settings should be applied when true.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.groupsClaim">.spec.kubernetes.oidc.groupsClaim</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>If provided, the name of a custom OpenID Connect claim for specifying user groups. The claim value is expected to be a string or JSON encoded array of strings.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.groupsPrefix">.spec.kubernetes.oidc.groupsPrefix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>If provided, all groups will be prefixed with this value to prevent conflicts with other authentication strategies.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.issuerUrl">.spec.kubernetes.oidc.issuerUrl</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The URL of the OpenID issuer, only HTTPS scheme will be accepted. If set, it will be used to verify the OIDC JSON Web Token (JWT).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.usernameClaim">.spec.kubernetes.oidc.usernameClaim</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The OpenID claim to use as the user name. Note that claims other than the default (&lsquo;sub&rsquo;) is not guaranteed to be unique and immutable.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.kubernetes.oidc.usernamePrefix">.spec.kubernetes.oidc.usernamePrefix</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>If provided, all usernames will be prefixed with this value. If not provided, username claims other than &lsquo;email&rsquo; are prefixed by the issuer URL to avoid clashes. To skip any prefixing, provide the value &lsquo;-&rsquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.provider">.spec.provider</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Defines the provider which should be rendered.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.registry">.spec.registry</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Registry provides configuration for the docker registry used for core component images.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.registry.domain">.spec.registry.domain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Domain is the domain of the registry to be used for pulling core component images.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.registry.pullProgressDeadline">.spec.registry.pullProgressDeadline</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Pull progress deadline is a string representing a duration to be used as a deadline for pulling images.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.sso">.spec.sso</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>SSO provides configuration for all SSO-related services.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.sso.publicKey">.spec.sso.publicKey</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>PublicKey is the public key of the SSO service.</p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>IgnitionStatus holds the rendering result.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.dataSecretName">.status.dataSecretName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>DataSecret is a reference to the secret containing the rendered ignition once created.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.dataSecretName.name">.status.dataSecretName.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the secret containing the rendered ignition.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.dataSecretName.namespace">.status.dataSecretName.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Namespace is the namespace of the secret containing the rendered ignition.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.dataSecretName.resourceVersion">.status.dataSecretName.resourceVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ResourceVersion is the Kubernetes resource version of the secret. Used to detect if the secret has changed, e.g. 12345.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.failureMessage">.status.failureMessage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>FailureMessage is a longer message indicating the reason rendering failed (if it did).</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.failureReason">.status.failureReason</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>FailureReason is a short string indicating the reason rendering failed (if it did).</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.ready">.status.ready</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Ready will be true when the referenced secret contains the rendered ignition and can be used for creating nodes.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.verification">.status.verification</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Verification is a hash of the rendered ignition to ensure that it has not been changed when loaded as a remote file by the bootstrap ignition. See <a href="https://coreos.com/ignition/docs/latest/configuration-v2_2.html">https://coreos.com/ignition/docs/latest/configuration-v2_2.html</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.verification.algorithm">.status.verification.algorithm</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The algorithm used for hashing. Must be sha512 for now.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.verification.hash">.status.verification.hash</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>The content of the full rendered ignition hashed by the corresponding algorithm.</p>

</div>

</div>
</div>


</div>



