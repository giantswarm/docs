---
title: KubeadmConfig CRD schema reference (group bootstrap.cluster.x-k8s.io)
linkTitle: KubeadmConfig
description: |
  KubeadmConfig is the Schema for the kubeadmconfigs API.
weight: 100
crd:
  name_camelcase: KubeadmConfig
  name_plural: kubeadmconfigs
  name_singular: kubeadmconfig
  group: bootstrap.cluster.x-k8s.io
  technical_name: kubeadmconfigs.bootstrap.cluster.x-k8s.io
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
  - https://github.com/orgs/giantswarm/teams/team-rocket
aliases:
  - /use-the-api/management-api/crd/kubeadmconfigs.bootstrap.cluster.x-k8s.io/
technical_name: kubeadmconfigs.bootstrap.cluster.x-k8s.io
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v5.0.0
---

# KubeadmConfig


<p class="crd-description">KubeadmConfig is the Schema for the kubeadmconfigs API.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">kubeadmconfigs.bootstrap.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">bootstrap.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">kubeadmconfig</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">kubeadmconfigs</dd>
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
<p>KubeadmConfigSpec defines the desired state of KubeadmConfig. Either ClusterConfiguration and InitConfiguration should be defined or the JoinConfiguration should be defined.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration">.spec.clusterConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClusterConfiguration along with InitConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer">.spec.clusterConfiguration.apiServer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIServer contains extra settings for the API server control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.certSANs">.spec.clusterConfiguration.apiServer.certSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CertSANs sets extra Subject Alternative Names for the API Server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.certSANs[*]">.spec.clusterConfiguration.apiServer.certSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraArgs">.spec.clusterConfiguration.apiServer.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes">.spec.clusterConfiguration.apiServer.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*]">.spec.clusterConfiguration.apiServer.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*].name">.spec.clusterConfiguration.apiServer.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType">.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly">.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiServer.timeoutForControlPlane">.spec.clusterConfiguration.apiServer.timeoutForControlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeoutForControlPlane controls the timeout that we use for API server to appear</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.apiVersion">.spec.clusterConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.certificatesDir">.spec.clusterConfiguration.certificatesDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CertificatesDir specifies where to store or look for all required certificates. NB: if not provided, this will default to <code>/etc/kubernetes/pki</code></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.clusterName">.spec.clusterConfiguration.clusterName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The cluster name</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controlPlaneEndpoint">.spec.clusterConfiguration.controlPlaneEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ControlPlaneEndpoint sets a stable IP address or DNS name for the control plane; it can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port. In case the ControlPlaneEndpoint is not specified, the AdvertiseAddress + BindPort are used; in case the ControlPlaneEndpoint is specified but without a TCP port, the BindPort is used. Possible usages are: e.g. In a cluster with more than one control plane instances, this field should be assigned the address of the external load balancer in front of the control plane instances. e.g.  in environments with enforced node recycling, the ControlPlaneEndpoint could be used for assigning a stable DNS to the control plane. NB: This value defaults to the first value in the Cluster object status.apiEndpoints array.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager">.spec.clusterConfiguration.controllerManager</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControllerManager contains extra settings for the controller manager control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraArgs">.spec.clusterConfiguration.controllerManager.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes">.spec.clusterConfiguration.controllerManager.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*]">.spec.clusterConfiguration.controllerManager.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*].name">.spec.clusterConfiguration.controllerManager.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType">.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly">.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.dns">.spec.clusterConfiguration.dns</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DNS defines the options for the DNS add-on installed in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.dns.imageRepository">.spec.clusterConfiguration.dns.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.dns.imageTag">.spec.clusterConfiguration.dns.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.dns.type">.spec.clusterConfiguration.dns.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Type defines the DNS add-on to be used</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd">.spec.clusterConfiguration.etcd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Etcd holds configuration for etcd. NB: This value defaults to a Local (stacked) etcd</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external">.spec.clusterConfiguration.etcd.external</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>External describes how to connect to an external etcd cluster Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external.caFile">.spec.clusterConfiguration.etcd.external.caFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CAFile is an SSL Certificate Authority file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external.certFile">.spec.clusterConfiguration.etcd.external.certFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CertFile is an SSL certification file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external.endpoints">.spec.clusterConfiguration.etcd.external.endpoints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Endpoints of etcd members. Required for ExternalEtcd.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external.endpoints[*]">.spec.clusterConfiguration.etcd.external.endpoints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.external.keyFile">.spec.clusterConfiguration.etcd.external.keyFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KeyFile is an SSL key file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local">.spec.clusterConfiguration.etcd.local</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Local provides configuration knobs for configuring the local etcd instance Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.dataDir">.spec.clusterConfiguration.etcd.local.dataDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataDir is the directory etcd will place its data. Defaults to &ldquo;/var/lib/etcd&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.extraArgs">.spec.clusterConfiguration.etcd.local.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs are extra arguments provided to the etcd binary when run inside a static pod.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.imageRepository">.spec.clusterConfiguration.etcd.local.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.imageTag">.spec.clusterConfiguration.etcd.local.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.peerCertSANs">.spec.clusterConfiguration.etcd.local.peerCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PeerCertSANs sets extra Subject Alternative Names for the etcd peer signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.peerCertSANs[*]">.spec.clusterConfiguration.etcd.local.peerCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.serverCertSANs">.spec.clusterConfiguration.etcd.local.serverCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ServerCertSANs sets extra Subject Alternative Names for the etcd server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.etcd.local.serverCertSANs[*]">.spec.clusterConfiguration.etcd.local.serverCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.featureGates">.spec.clusterConfiguration.featureGates</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>FeatureGates enabled by the user.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.imageRepository">.spec.clusterConfiguration.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. If empty, <code>k8s.gcr.io</code> will be used by default; in case of kubernetes version is a CI build (kubernetes version starts with <code>ci/</code> or <code>ci-cross/</code>) <code>gcr.io/k8s-staging-ci-images</code> will be used as a default for control plane components and for kube-proxy, while <code>k8s.gcr.io</code> will be used for all the other images.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.kind">.spec.clusterConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.kubernetesVersion">.spec.clusterConfiguration.kubernetesVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>KubernetesVersion is the target version of the control plane. NB: This value defaults to the Machine object spec.version</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.networking">.spec.clusterConfiguration.networking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Networking holds configuration for the networking topology of the cluster. NB: This value defaults to the Cluster object spec.clusterNetwork.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.networking.dnsDomain">.spec.clusterConfiguration.networking.dnsDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DNSDomain is the dns domain used by k8s services. Defaults to &ldquo;cluster.local&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.networking.podSubnet">.spec.clusterConfiguration.networking.podSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PodSubnet is the subnet used by pods. If unset, the API server will not allocate CIDR ranges for every node. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.services.cidrBlocks if that is set</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.networking.serviceSubnet">.spec.clusterConfiguration.networking.serviceSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ServiceSubnet is the subnet used by k8s services. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.pods.cidrBlocks, or to &ldquo;10.96.0.0/12&rdquo; if that&rsquo;s unset.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler">.spec.clusterConfiguration.scheduler</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Scheduler contains extra settings for the scheduler control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraArgs">.spec.clusterConfiguration.scheduler.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes">.spec.clusterConfiguration.scheduler.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*]">.spec.clusterConfiguration.scheduler.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*].name">.spec.clusterConfiguration.scheduler.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType">.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly">.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.clusterConfiguration.useHyperKubeImage">.spec.clusterConfiguration.useHyperKubeImage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UseHyperKubeImage controls if hyperkube should be used for Kubernetes components instead of their respective separate images</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup">.spec.diskSetup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskSetup specifies options for the creation of partition tables and file systems on devices.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems">.spec.diskSetup.filesystems</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Filesystems specifies the list of file systems to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*]">.spec.diskSetup.filesystems[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Filesystem defines the file systems to be created.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].device">.spec.diskSetup.filesystems[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device specifies the device name</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].extraOpts">.spec.diskSetup.filesystems[*].extraOpts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraOpts defined extra options to add to the command for creating the file system.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].extraOpts[*]">.spec.diskSetup.filesystems[*].extraOpts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].filesystem">.spec.diskSetup.filesystems[*].filesystem</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Filesystem specifies the file system type.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].label">.spec.diskSetup.filesystems[*].label</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Label specifies the file system label to be used. If set to None, no label is used.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].overwrite">.spec.diskSetup.filesystems[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite defines whether or not to overwrite any existing filesystem. If true, any pre-existing file system will be destroyed. Use with Caution.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].partition">.spec.diskSetup.filesystems[*].partition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Partition specifies the partition to use. The valid options are: &ldquo;auto|any&rdquo;, &ldquo;auto&rdquo;, &ldquo;any&rdquo;, &ldquo;none&rdquo;, and <NUM>, where NUM is the actual partition number.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.filesystems[*].replaceFS">.spec.diskSetup.filesystems[*].replaceFS</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ReplaceFS is a special directive, used for Microsoft Azure that instructs cloud-init to replace a file system of <FS_TYPE>. NOTE: unless you define a label, this requires the use of the &lsquo;any&rsquo; partition directive.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions">.spec.diskSetup.partitions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Partitions specifies the list of the partitions to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions[*]">.spec.diskSetup.partitions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Partition defines how to create and layout a partition.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions[*].device">.spec.diskSetup.partitions[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device is the name of the device.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions[*].layout">.spec.diskSetup.partitions[*].layout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Layout specifies the device layout. If it is true, a single partition will be created for the entire device. When layout is false, it means don&rsquo;t partition or ignore existing partitioning.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions[*].overwrite">.spec.diskSetup.partitions[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite describes whether to skip checks and create the partition if a partition or filesystem is found on the device. Use with caution. Default is &lsquo;false&rsquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.diskSetup.partitions[*].tableType">.spec.diskSetup.partitions[*].tableType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TableType specifies the tupe of partition table. The following are supported: &lsquo;mbr&rsquo;: default and setups a MS-DOS partition table &lsquo;gpt&rsquo;: setups a GPT partition table</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files">.spec.files</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files specifies extra files to be passed to user_data upon creation.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*]">.spec.files[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File defines the input for generating write_files in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].content">.spec.files[*].content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Content is the actual content of the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].contentFrom">.spec.files[*].contentFrom</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ContentFrom is a referenced source of content to populate the file.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].contentFrom.secret">.spec.files[*].contentFrom.secret</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Secret represents a secret that should populate this file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].contentFrom.secret.key">.spec.files[*].contentFrom.secret.key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Key is the key in the secret&rsquo;s data map for this value.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].contentFrom.secret.name">.spec.files[*].contentFrom.secret.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the secret in the KubeadmBootstrapConfig&rsquo;s namespace to use.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].encoding">.spec.files[*].encoding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Encoding specifies the encoding of the file contents.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].owner">.spec.files[*].owner</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Owner specifies the ownership of the file, e.g. &ldquo;root:root&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].path">.spec.files[*].path</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Path specifies the full path on disk where to store the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.files[*].permissions">.spec.files[*].permissions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Permissions specifies the permissions to assign to the file, e.g. &ldquo;0640&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.format">.spec.format</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Format specifies the output format of the bootstrap data</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration">.spec.initConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>InitConfiguration along with ClusterConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.apiVersion">.spec.initConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens">.spec.initConfiguration.bootstrapTokens</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>BootstrapTokens is respected at <code>kubeadm init</code> time and describes a set of Bootstrap Tokens to create. This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*]">.spec.initConfiguration.bootstrapTokens[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken describes one bootstrap token, stored as a Secret in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].description">.spec.initConfiguration.bootstrapTokens[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description sets a human-friendly message why this token exists and what it&rsquo;s used for, so other administrators can know its purpose.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].expires">.spec.initConfiguration.bootstrapTokens[*].expires</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Expires specifies the timestamp when this token expires. Defaults to being set dynamically at runtime based on the TTL. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].groups">.spec.initConfiguration.bootstrapTokens[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Groups specifies the extra groups that this token will authenticate as when/if used for authentication</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].groups[*]">.spec.initConfiguration.bootstrapTokens[*].groups[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].token">.spec.initConfiguration.bootstrapTokens[*].token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is used for establishing bidirectional trust between nodes and control-planes. Used for joining nodes in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].ttl">.spec.initConfiguration.bootstrapTokens[*].ttl</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TTL defines the time to live for this token. Defaults to 24h. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].usages">.spec.initConfiguration.bootstrapTokens[*].usages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Usages describes the ways in which this token can be used. Can by default be used for establishing bidirectional trust, but that can be changed here.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.bootstrapTokens[*].usages[*]">.spec.initConfiguration.bootstrapTokens[*].usages[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.kind">.spec.initConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.localAPIEndpoint">.spec.initConfiguration.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance that&rsquo;s deployed on this control plane node In HA setups, this differs from ClusterConfiguration.ControlPlaneEndpoint in the sense that ControlPlaneEndpoint is the global endpoint for the cluster, which then loadbalances the requests to each individual API server. This configuration object lets you customize what IP/DNS name and port the local API server advertises it&rsquo;s accessible on. By default, kubeadm tries to auto-detect the IP of the default interface and use that, but in case that process fails you may set the desired value here.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.localAPIEndpoint.advertiseAddress">.spec.initConfiguration.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.localAPIEndpoint.bindPort">.spec.initConfiguration.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration">.spec.initConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.criSocket">.spec.initConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.kubeletExtraArgs">.spec.initConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.name">.spec.initConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints">.spec.initConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints[*]">.spec.initConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints[*].effect">.spec.initConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints[*].key">.spec.initConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints[*].timeAdded">.spec.initConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.initConfiguration.nodeRegistration.taints[*].value">.spec.initConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration">.spec.joinConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JoinConfiguration is the kubeadm configuration for the join command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.apiVersion">.spec.joinConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.caCertPath">.spec.joinConfiguration.caCertPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to &ldquo;/etc/kubernetes/pki/ca.crt&rdquo;. TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.controlPlane">.spec.joinConfiguration.controlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlane defines the additional control plane instance to be deployed on the joining node. If nil, no additional control plane instance will be deployed.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.controlPlane.localAPIEndpoint">.spec.joinConfiguration.controlPlane.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance to be deployed on this node.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress">.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort">.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery">.spec.joinConfiguration.discovery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Discovery specifies the options for the kubelet to use during the TLS Bootstrap process TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken">.spec.joinConfiguration.discovery.bootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken is used to set the options for bootstrap token based discovery BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint">.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIServerEndpoint is an IP or domain name to the API server from which info will be fetched.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CACertHashes specifies a set of public key pins to verify when token-based discovery is used. The root CA found during discovery must match one of these values. Specifying an empty set disables root CA pinning, which can be unsafe. Each hash is specified as &ldquo;<type>:<value>&rdquo;, where the only currently supported type is &ldquo;sha256&rdquo;. This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI) object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL: openssl x509 -pubkey -in ca.crt openssl rsa -pubin -outform der 2&gt;&amp;/dev/null | openssl dgst -sha256 -hex</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken.token">.spec.joinConfiguration.discovery.bootstrapToken.token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is a token used to validate cluster information fetched from the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification">.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>UnsafeSkipCAVerification allows token-based discovery without CA verification via CACertHashes. This can weaken the security of kubeadm since other nodes can impersonate the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.file">.spec.joinConfiguration.discovery.file</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File is used to specify a file or URL to a kubeconfig file from which to load cluster information BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.file.kubeConfigPath">.spec.joinConfiguration.discovery.file.kubeConfigPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KubeConfigPath is used to specify the actual file path or URL to the kubeconfig file from which to load cluster information</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.timeout">.spec.joinConfiguration.discovery.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Timeout modifies the discovery timeout</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.discovery.tlsBootstrapToken">.spec.joinConfiguration.discovery.tlsBootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TLSBootstrapToken is a token used for TLS bootstrapping. If .BootstrapToken is set, this field is defaulted to .BootstrapToken.Token, but can be overridden. If .File is set, this field <strong>must be set</strong> in case the KubeConfigFile does not contain any other authentication information TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.kind">.spec.joinConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration">.spec.joinConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.criSocket">.spec.joinConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs">.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.name">.spec.joinConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints">.spec.joinConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints[*]">.spec.joinConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints[*].effect">.spec.joinConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints[*].key">.spec.joinConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded">.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.joinConfiguration.nodeRegistration.taints[*].value">.spec.joinConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.mounts">.spec.mounts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Mounts specifies a list of mount points to be setup.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.mounts[*]">.spec.mounts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>MountPoints defines input for generated mounts in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.ntp">.spec.ntp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NTP specifies NTP configuration</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.ntp.enabled">.spec.ntp.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled specifies whether NTP should be enabled</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.ntp.servers">.spec.ntp.servers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Servers specifies which NTP servers to use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.ntp.servers[*]">.spec.ntp.servers[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.postKubeadmCommands">.spec.postKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PostKubeadmCommands specifies extra commands to run after kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.postKubeadmCommands[*]">.spec.postKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.preKubeadmCommands">.spec.preKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PreKubeadmCommands specifies extra commands to run before kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.preKubeadmCommands[*]">.spec.preKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.useExperimentalRetryJoin">.spec.useExperimentalRetryJoin</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.
 This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.
 This will add about 40KB to userdata
 For more information, refer to <a href="https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055">https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055</a>.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users">.spec.users</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Users specifies extra users to add</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*]">.spec.users[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>User defines the input for a generated user in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].gecos">.spec.users[*].gecos</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Gecos specifies the gecos to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].groups">.spec.users[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Groups specifies the additional groups for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].homeDir">.spec.users[*].homeDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>HomeDir specifies the home directory to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].inactive">.spec.users[*].inactive</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Inactive specifies whether to mark the user as inactive</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].lockPassword">.spec.users[*].lockPassword</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>LockPassword specifies if password login should be disabled</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].name">.spec.users[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name specifies the user name</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].passwd">.spec.users[*].passwd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Passwd specifies a hashed password for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].primaryGroup">.spec.users[*].primaryGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PrimaryGroup specifies the primary group for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].shell">.spec.users[*].shell</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Shell specifies the user&rsquo;s shell</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].sshAuthorizedKeys">.spec.users[*].sshAuthorizedKeys</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SSHAuthorizedKeys specifies a list of ssh authorized keys for the user</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].sshAuthorizedKeys[*]">.spec.users[*].sshAuthorizedKeys[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.users[*].sudo">.spec.users[*].sudo</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Sudo specifies a sudo role for the user</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.verbosity">.spec.verbosity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Verbosity is the number for the kubeadm log level verbosity. It overrides the <code>--v</code> flag in kubeadm commands.</p>

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
<p>KubeadmConfigStatus defines the observed state of KubeadmConfig.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.bootstrapData">.status.bootstrapData</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>BootstrapData will be a cloud-init script for now.
 Deprecated: Switch to DataSecretName.</p>

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
<p>Conditions defines current service state of the KubeadmConfig.</p>

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
<h3 class="property-path" id="v1alpha3-.status.dataSecretName">.status.dataSecretName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataSecretName is the name of the secret that stores the bootstrap data script.</p>

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
<p>FailureMessage will be set on non-retryable errors</p>

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
<p>FailureReason will be set on non-retryable errors</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.status.observedGeneration">.status.observedGeneration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>ObservedGeneration is the latest generation observed by the controller.</p>

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
<p>Ready indicates the BootstrapData field is ready to be consumed</p>

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
<p>KubeadmConfigSpec defines the desired state of KubeadmConfig. Either ClusterConfiguration and InitConfiguration should be defined or the JoinConfiguration should be defined.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration">.spec.clusterConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClusterConfiguration along with InitConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer">.spec.clusterConfiguration.apiServer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIServer contains extra settings for the API server control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.certSANs">.spec.clusterConfiguration.apiServer.certSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CertSANs sets extra Subject Alternative Names for the API Server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.certSANs[*]">.spec.clusterConfiguration.apiServer.certSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraArgs">.spec.clusterConfiguration.apiServer.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes">.spec.clusterConfiguration.apiServer.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*]">.spec.clusterConfiguration.apiServer.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*].name">.spec.clusterConfiguration.apiServer.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType">.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly">.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiServer.timeoutForControlPlane">.spec.clusterConfiguration.apiServer.timeoutForControlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeoutForControlPlane controls the timeout that we use for API server to appear</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.apiVersion">.spec.clusterConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.certificatesDir">.spec.clusterConfiguration.certificatesDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CertificatesDir specifies where to store or look for all required certificates. NB: if not provided, this will default to <code>/etc/kubernetes/pki</code></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.clusterName">.spec.clusterConfiguration.clusterName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The cluster name</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controlPlaneEndpoint">.spec.clusterConfiguration.controlPlaneEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ControlPlaneEndpoint sets a stable IP address or DNS name for the control plane; it can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port. In case the ControlPlaneEndpoint is not specified, the AdvertiseAddress + BindPort are used; in case the ControlPlaneEndpoint is specified but without a TCP port, the BindPort is used. Possible usages are: e.g. In a cluster with more than one control plane instances, this field should be assigned the address of the external load balancer in front of the control plane instances. e.g.  in environments with enforced node recycling, the ControlPlaneEndpoint could be used for assigning a stable DNS to the control plane. NB: This value defaults to the first value in the Cluster object status.apiEndpoints array.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager">.spec.clusterConfiguration.controllerManager</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControllerManager contains extra settings for the controller manager control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraArgs">.spec.clusterConfiguration.controllerManager.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes">.spec.clusterConfiguration.controllerManager.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*]">.spec.clusterConfiguration.controllerManager.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*].name">.spec.clusterConfiguration.controllerManager.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType">.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly">.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.dns">.spec.clusterConfiguration.dns</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DNS defines the options for the DNS add-on installed in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.dns.imageRepository">.spec.clusterConfiguration.dns.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.dns.imageTag">.spec.clusterConfiguration.dns.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd">.spec.clusterConfiguration.etcd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Etcd holds configuration for etcd. NB: This value defaults to a Local (stacked) etcd</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external">.spec.clusterConfiguration.etcd.external</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>External describes how to connect to an external etcd cluster Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external.caFile">.spec.clusterConfiguration.etcd.external.caFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CAFile is an SSL Certificate Authority file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external.certFile">.spec.clusterConfiguration.etcd.external.certFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CertFile is an SSL certification file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external.endpoints">.spec.clusterConfiguration.etcd.external.endpoints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Endpoints of etcd members. Required for ExternalEtcd.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external.endpoints[*]">.spec.clusterConfiguration.etcd.external.endpoints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.external.keyFile">.spec.clusterConfiguration.etcd.external.keyFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KeyFile is an SSL key file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local">.spec.clusterConfiguration.etcd.local</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Local provides configuration knobs for configuring the local etcd instance Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.dataDir">.spec.clusterConfiguration.etcd.local.dataDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataDir is the directory etcd will place its data. Defaults to &ldquo;/var/lib/etcd&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.extraArgs">.spec.clusterConfiguration.etcd.local.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs are extra arguments provided to the etcd binary when run inside a static pod.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.imageRepository">.spec.clusterConfiguration.etcd.local.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.imageTag">.spec.clusterConfiguration.etcd.local.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.peerCertSANs">.spec.clusterConfiguration.etcd.local.peerCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PeerCertSANs sets extra Subject Alternative Names for the etcd peer signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.peerCertSANs[*]">.spec.clusterConfiguration.etcd.local.peerCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.serverCertSANs">.spec.clusterConfiguration.etcd.local.serverCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ServerCertSANs sets extra Subject Alternative Names for the etcd server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.etcd.local.serverCertSANs[*]">.spec.clusterConfiguration.etcd.local.serverCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.featureGates">.spec.clusterConfiguration.featureGates</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>FeatureGates enabled by the user.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.imageRepository">.spec.clusterConfiguration.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. If empty, <code>k8s.gcr.io</code> will be used by default; in case of kubernetes version is a CI build (kubernetes version starts with <code>ci/</code> or <code>ci-cross/</code>) <code>gcr.io/k8s-staging-ci-images</code> will be used as a default for control plane components and for kube-proxy, while <code>k8s.gcr.io</code> will be used for all the other images.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.kind">.spec.clusterConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.kubernetesVersion">.spec.clusterConfiguration.kubernetesVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>KubernetesVersion is the target version of the control plane. NB: This value defaults to the Machine object spec.version</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.networking">.spec.clusterConfiguration.networking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Networking holds configuration for the networking topology of the cluster. NB: This value defaults to the Cluster object spec.clusterNetwork.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.networking.dnsDomain">.spec.clusterConfiguration.networking.dnsDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DNSDomain is the dns domain used by k8s services. Defaults to &ldquo;cluster.local&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.networking.podSubnet">.spec.clusterConfiguration.networking.podSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PodSubnet is the subnet used by pods. If unset, the API server will not allocate CIDR ranges for every node. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.services.cidrBlocks if that is set</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.networking.serviceSubnet">.spec.clusterConfiguration.networking.serviceSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ServiceSubnet is the subnet used by k8s services. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.pods.cidrBlocks, or to &ldquo;10.96.0.0/12&rdquo; if that&rsquo;s unset.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler">.spec.clusterConfiguration.scheduler</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Scheduler contains extra settings for the scheduler control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraArgs">.spec.clusterConfiguration.scheduler.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes">.spec.clusterConfiguration.scheduler.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*]">.spec.clusterConfiguration.scheduler.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*].name">.spec.clusterConfiguration.scheduler.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType">.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly">.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup">.spec.diskSetup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskSetup specifies options for the creation of partition tables and file systems on devices.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems">.spec.diskSetup.filesystems</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Filesystems specifies the list of file systems to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*]">.spec.diskSetup.filesystems[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Filesystem defines the file systems to be created.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].device">.spec.diskSetup.filesystems[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device specifies the device name</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].extraOpts">.spec.diskSetup.filesystems[*].extraOpts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraOpts defined extra options to add to the command for creating the file system.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].extraOpts[*]">.spec.diskSetup.filesystems[*].extraOpts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].filesystem">.spec.diskSetup.filesystems[*].filesystem</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Filesystem specifies the file system type.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].label">.spec.diskSetup.filesystems[*].label</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Label specifies the file system label to be used. If set to None, no label is used.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].overwrite">.spec.diskSetup.filesystems[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite defines whether or not to overwrite any existing filesystem. If true, any pre-existing file system will be destroyed. Use with Caution.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].partition">.spec.diskSetup.filesystems[*].partition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Partition specifies the partition to use. The valid options are: &ldquo;auto|any&rdquo;, &ldquo;auto&rdquo;, &ldquo;any&rdquo;, &ldquo;none&rdquo;, and <NUM>, where NUM is the actual partition number.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.filesystems[*].replaceFS">.spec.diskSetup.filesystems[*].replaceFS</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ReplaceFS is a special directive, used for Microsoft Azure that instructs cloud-init to replace a file system of <FS_TYPE>. NOTE: unless you define a label, this requires the use of the &lsquo;any&rsquo; partition directive.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions">.spec.diskSetup.partitions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Partitions specifies the list of the partitions to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions[*]">.spec.diskSetup.partitions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Partition defines how to create and layout a partition.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions[*].device">.spec.diskSetup.partitions[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device is the name of the device.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions[*].layout">.spec.diskSetup.partitions[*].layout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Layout specifies the device layout. If it is true, a single partition will be created for the entire device. When layout is false, it means don&rsquo;t partition or ignore existing partitioning.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions[*].overwrite">.spec.diskSetup.partitions[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite describes whether to skip checks and create the partition if a partition or filesystem is found on the device. Use with caution. Default is &lsquo;false&rsquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.diskSetup.partitions[*].tableType">.spec.diskSetup.partitions[*].tableType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TableType specifies the tupe of partition table. The following are supported: &lsquo;mbr&rsquo;: default and setups a MS-DOS partition table &lsquo;gpt&rsquo;: setups a GPT partition table</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files">.spec.files</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files specifies extra files to be passed to user_data upon creation.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*]">.spec.files[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File defines the input for generating write_files in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].content">.spec.files[*].content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Content is the actual content of the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].contentFrom">.spec.files[*].contentFrom</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ContentFrom is a referenced source of content to populate the file.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].contentFrom.secret">.spec.files[*].contentFrom.secret</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Secret represents a secret that should populate this file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].contentFrom.secret.key">.spec.files[*].contentFrom.secret.key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Key is the key in the secret&rsquo;s data map for this value.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].contentFrom.secret.name">.spec.files[*].contentFrom.secret.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the secret in the KubeadmBootstrapConfig&rsquo;s namespace to use.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].encoding">.spec.files[*].encoding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Encoding specifies the encoding of the file contents.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].owner">.spec.files[*].owner</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Owner specifies the ownership of the file, e.g. &ldquo;root:root&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].path">.spec.files[*].path</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Path specifies the full path on disk where to store the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.files[*].permissions">.spec.files[*].permissions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Permissions specifies the permissions to assign to the file, e.g. &ldquo;0640&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.format">.spec.format</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Format specifies the output format of the bootstrap data</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration">.spec.initConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>InitConfiguration along with ClusterConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.apiVersion">.spec.initConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens">.spec.initConfiguration.bootstrapTokens</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>BootstrapTokens is respected at <code>kubeadm init</code> time and describes a set of Bootstrap Tokens to create. This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*]">.spec.initConfiguration.bootstrapTokens[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken describes one bootstrap token, stored as a Secret in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].description">.spec.initConfiguration.bootstrapTokens[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description sets a human-friendly message why this token exists and what it&rsquo;s used for, so other administrators can know its purpose.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].expires">.spec.initConfiguration.bootstrapTokens[*].expires</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Expires specifies the timestamp when this token expires. Defaults to being set dynamically at runtime based on the TTL. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].groups">.spec.initConfiguration.bootstrapTokens[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Groups specifies the extra groups that this token will authenticate as when/if used for authentication</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].groups[*]">.spec.initConfiguration.bootstrapTokens[*].groups[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].token">.spec.initConfiguration.bootstrapTokens[*].token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is used for establishing bidirectional trust between nodes and control-planes. Used for joining nodes in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].ttl">.spec.initConfiguration.bootstrapTokens[*].ttl</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TTL defines the time to live for this token. Defaults to 24h. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].usages">.spec.initConfiguration.bootstrapTokens[*].usages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Usages describes the ways in which this token can be used. Can by default be used for establishing bidirectional trust, but that can be changed here.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.bootstrapTokens[*].usages[*]">.spec.initConfiguration.bootstrapTokens[*].usages[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.kind">.spec.initConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.localAPIEndpoint">.spec.initConfiguration.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance that&rsquo;s deployed on this control plane node In HA setups, this differs from ClusterConfiguration.ControlPlaneEndpoint in the sense that ControlPlaneEndpoint is the global endpoint for the cluster, which then loadbalances the requests to each individual API server. This configuration object lets you customize what IP/DNS name and port the local API server advertises it&rsquo;s accessible on. By default, kubeadm tries to auto-detect the IP of the default interface and use that, but in case that process fails you may set the desired value here.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.localAPIEndpoint.advertiseAddress">.spec.initConfiguration.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.localAPIEndpoint.bindPort">.spec.initConfiguration.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration">.spec.initConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.criSocket">.spec.initConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.ignorePreflightErrors">.spec.initConfiguration.nodeRegistration.ignorePreflightErrors</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>IgnorePreflightErrors provides a slice of pre-flight errors to be ignored when the current node is registered.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.ignorePreflightErrors[*]">.spec.initConfiguration.nodeRegistration.ignorePreflightErrors[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.kubeletExtraArgs">.spec.initConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.name">.spec.initConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints">.spec.initConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints[*]">.spec.initConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints[*].effect">.spec.initConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints[*].key">.spec.initConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints[*].timeAdded">.spec.initConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.initConfiguration.nodeRegistration.taints[*].value">.spec.initConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration">.spec.joinConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JoinConfiguration is the kubeadm configuration for the join command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.apiVersion">.spec.joinConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.caCertPath">.spec.joinConfiguration.caCertPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to &ldquo;/etc/kubernetes/pki/ca.crt&rdquo;. TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.controlPlane">.spec.joinConfiguration.controlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlane defines the additional control plane instance to be deployed on the joining node. If nil, no additional control plane instance will be deployed.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.controlPlane.localAPIEndpoint">.spec.joinConfiguration.controlPlane.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance to be deployed on this node.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress">.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort">.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery">.spec.joinConfiguration.discovery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Discovery specifies the options for the kubelet to use during the TLS Bootstrap process TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken">.spec.joinConfiguration.discovery.bootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken is used to set the options for bootstrap token based discovery BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint">.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIServerEndpoint is an IP or domain name to the API server from which info will be fetched.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CACertHashes specifies a set of public key pins to verify when token-based discovery is used. The root CA found during discovery must match one of these values. Specifying an empty set disables root CA pinning, which can be unsafe. Each hash is specified as &ldquo;<type>:<value>&rdquo;, where the only currently supported type is &ldquo;sha256&rdquo;. This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI) object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL: openssl x509 -pubkey -in ca.crt openssl rsa -pubin -outform der 2&gt;&amp;/dev/null | openssl dgst -sha256 -hex</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken.token">.spec.joinConfiguration.discovery.bootstrapToken.token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is a token used to validate cluster information fetched from the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification">.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UnsafeSkipCAVerification allows token-based discovery without CA verification via CACertHashes. This can weaken the security of kubeadm since other nodes can impersonate the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.file">.spec.joinConfiguration.discovery.file</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File is used to specify a file or URL to a kubeconfig file from which to load cluster information BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.file.kubeConfigPath">.spec.joinConfiguration.discovery.file.kubeConfigPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KubeConfigPath is used to specify the actual file path or URL to the kubeconfig file from which to load cluster information</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.timeout">.spec.joinConfiguration.discovery.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Timeout modifies the discovery timeout</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.discovery.tlsBootstrapToken">.spec.joinConfiguration.discovery.tlsBootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TLSBootstrapToken is a token used for TLS bootstrapping. If .BootstrapToken is set, this field is defaulted to .BootstrapToken.Token, but can be overridden. If .File is set, this field <strong>must be set</strong> in case the KubeConfigFile does not contain any other authentication information</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.kind">.spec.joinConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration">.spec.joinConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.criSocket">.spec.joinConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors">.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>IgnorePreflightErrors provides a slice of pre-flight errors to be ignored when the current node is registered.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors[*]">.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs">.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.name">.spec.joinConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints">.spec.joinConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints[*]">.spec.joinConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints[*].effect">.spec.joinConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints[*].key">.spec.joinConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded">.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.joinConfiguration.nodeRegistration.taints[*].value">.spec.joinConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.mounts">.spec.mounts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Mounts specifies a list of mount points to be setup.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.mounts[*]">.spec.mounts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>MountPoints defines input for generated mounts in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.ntp">.spec.ntp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NTP specifies NTP configuration</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.ntp.enabled">.spec.ntp.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled specifies whether NTP should be enabled</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.ntp.servers">.spec.ntp.servers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Servers specifies which NTP servers to use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.ntp.servers[*]">.spec.ntp.servers[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.postKubeadmCommands">.spec.postKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PostKubeadmCommands specifies extra commands to run after kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.postKubeadmCommands[*]">.spec.postKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.preKubeadmCommands">.spec.preKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PreKubeadmCommands specifies extra commands to run before kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.preKubeadmCommands[*]">.spec.preKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.useExperimentalRetryJoin">.spec.useExperimentalRetryJoin</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.
 This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.
 This will add about 40KB to userdata
 For more information, refer to <a href="https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055">https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055</a>.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users">.spec.users</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Users specifies extra users to add</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*]">.spec.users[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>User defines the input for a generated user in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].gecos">.spec.users[*].gecos</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Gecos specifies the gecos to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].groups">.spec.users[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Groups specifies the additional groups for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].homeDir">.spec.users[*].homeDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>HomeDir specifies the home directory to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].inactive">.spec.users[*].inactive</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Inactive specifies whether to mark the user as inactive</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].lockPassword">.spec.users[*].lockPassword</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>LockPassword specifies if password login should be disabled</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].name">.spec.users[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name specifies the user name</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].passwd">.spec.users[*].passwd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Passwd specifies a hashed password for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].primaryGroup">.spec.users[*].primaryGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PrimaryGroup specifies the primary group for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].shell">.spec.users[*].shell</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Shell specifies the user&rsquo;s shell</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].sshAuthorizedKeys">.spec.users[*].sshAuthorizedKeys</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SSHAuthorizedKeys specifies a list of ssh authorized keys for the user</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].sshAuthorizedKeys[*]">.spec.users[*].sshAuthorizedKeys[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.users[*].sudo">.spec.users[*].sudo</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Sudo specifies a sudo role for the user</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.spec.verbosity">.spec.verbosity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Verbosity is the number for the kubeadm log level verbosity. It overrides the <code>--v</code> flag in kubeadm commands.</p>

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
<p>KubeadmConfigStatus defines the observed state of KubeadmConfig.</p>

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
<p>Conditions defines current service state of the KubeadmConfig.</p>

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
<h3 class="property-path" id="v1alpha4-.status.dataSecretName">.status.dataSecretName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataSecretName is the name of the secret that stores the bootstrap data script.</p>

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
<p>FailureMessage will be set on non-retryable errors</p>

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
<p>FailureReason will be set on non-retryable errors</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha4-.status.observedGeneration">.status.observedGeneration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>ObservedGeneration is the latest generation observed by the controller.</p>

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
<p>Ready indicates the BootstrapData field is ready to be consumed</p>

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
<p>KubeadmConfigSpec defines the desired state of KubeadmConfig. Either ClusterConfiguration and InitConfiguration should be defined or the JoinConfiguration should be defined.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration">.spec.clusterConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ClusterConfiguration along with InitConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer">.spec.clusterConfiguration.apiServer</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>APIServer contains extra settings for the API server control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.certSANs">.spec.clusterConfiguration.apiServer.certSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CertSANs sets extra Subject Alternative Names for the API Server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.certSANs[*]">.spec.clusterConfiguration.apiServer.certSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraArgs">.spec.clusterConfiguration.apiServer.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes">.spec.clusterConfiguration.apiServer.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*]">.spec.clusterConfiguration.apiServer.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath">.spec.clusterConfiguration.apiServer.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*].name">.spec.clusterConfiguration.apiServer.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType">.spec.clusterConfiguration.apiServer.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly">.spec.clusterConfiguration.apiServer.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiServer.timeoutForControlPlane">.spec.clusterConfiguration.apiServer.timeoutForControlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeoutForControlPlane controls the timeout that we use for API server to appear</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.apiVersion">.spec.clusterConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.certificatesDir">.spec.clusterConfiguration.certificatesDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CertificatesDir specifies where to store or look for all required certificates. NB: if not provided, this will default to <code>/etc/kubernetes/pki</code></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.clusterName">.spec.clusterConfiguration.clusterName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The cluster name</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controlPlaneEndpoint">.spec.clusterConfiguration.controlPlaneEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ControlPlaneEndpoint sets a stable IP address or DNS name for the control plane; it can be a valid IP address or a RFC-1123 DNS subdomain, both with optional TCP port. In case the ControlPlaneEndpoint is not specified, the AdvertiseAddress + BindPort are used; in case the ControlPlaneEndpoint is specified but without a TCP port, the BindPort is used. Possible usages are: e.g. In a cluster with more than one control plane instances, this field should be assigned the address of the external load balancer in front of the control plane instances. e.g.  in environments with enforced node recycling, the ControlPlaneEndpoint could be used for assigning a stable DNS to the control plane. NB: This value defaults to the first value in the Cluster object status.apiEndpoints array.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager">.spec.clusterConfiguration.controllerManager</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControllerManager contains extra settings for the controller manager control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraArgs">.spec.clusterConfiguration.controllerManager.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes">.spec.clusterConfiguration.controllerManager.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*]">.spec.clusterConfiguration.controllerManager.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath">.spec.clusterConfiguration.controllerManager.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*].name">.spec.clusterConfiguration.controllerManager.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType">.spec.clusterConfiguration.controllerManager.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly">.spec.clusterConfiguration.controllerManager.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.dns">.spec.clusterConfiguration.dns</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DNS defines the options for the DNS add-on installed in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.dns.imageRepository">.spec.clusterConfiguration.dns.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.dns.imageTag">.spec.clusterConfiguration.dns.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd">.spec.clusterConfiguration.etcd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Etcd holds configuration for etcd. NB: This value defaults to a Local (stacked) etcd</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external">.spec.clusterConfiguration.etcd.external</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>External describes how to connect to an external etcd cluster Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external.caFile">.spec.clusterConfiguration.etcd.external.caFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CAFile is an SSL Certificate Authority file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external.certFile">.spec.clusterConfiguration.etcd.external.certFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>CertFile is an SSL certification file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external.endpoints">.spec.clusterConfiguration.etcd.external.endpoints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Endpoints of etcd members. Required for ExternalEtcd.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external.endpoints[*]">.spec.clusterConfiguration.etcd.external.endpoints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.external.keyFile">.spec.clusterConfiguration.etcd.external.keyFile</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KeyFile is an SSL key file used to secure etcd communication. Required if using a TLS connection.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local">.spec.clusterConfiguration.etcd.local</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Local provides configuration knobs for configuring the local etcd instance Local and External are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.dataDir">.spec.clusterConfiguration.etcd.local.dataDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataDir is the directory etcd will place its data. Defaults to &ldquo;/var/lib/etcd&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.extraArgs">.spec.clusterConfiguration.etcd.local.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs are extra arguments provided to the etcd binary when run inside a static pod.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.imageRepository">.spec.clusterConfiguration.etcd.local.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. if not set, the ImageRepository defined in ClusterConfiguration will be used instead.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.imageTag">.spec.clusterConfiguration.etcd.local.imageTag</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageTag allows to specify a tag for the image. In case this value is set, kubeadm does not change automatically the version of the above components during upgrades.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.peerCertSANs">.spec.clusterConfiguration.etcd.local.peerCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PeerCertSANs sets extra Subject Alternative Names for the etcd peer signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.peerCertSANs[*]">.spec.clusterConfiguration.etcd.local.peerCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.serverCertSANs">.spec.clusterConfiguration.etcd.local.serverCertSANs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ServerCertSANs sets extra Subject Alternative Names for the etcd server signing cert.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.etcd.local.serverCertSANs[*]">.spec.clusterConfiguration.etcd.local.serverCertSANs[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.featureGates">.spec.clusterConfiguration.featureGates</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>FeatureGates enabled by the user.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.imageRepository">.spec.clusterConfiguration.imageRepository</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ImageRepository sets the container registry to pull images from. If empty, <code>k8s.gcr.io</code> will be used by default; in case of kubernetes version is a CI build (kubernetes version starts with <code>ci/</code> or <code>ci-cross/</code>) <code>gcr.io/k8s-staging-ci-images</code> will be used as a default for control plane components and for kube-proxy, while <code>k8s.gcr.io</code> will be used for all the other images.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.kind">.spec.clusterConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.kubernetesVersion">.spec.clusterConfiguration.kubernetesVersion</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>KubernetesVersion is the target version of the control plane. NB: This value defaults to the Machine object spec.version</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.networking">.spec.clusterConfiguration.networking</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Networking holds configuration for the networking topology of the cluster. NB: This value defaults to the Cluster object spec.clusterNetwork.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.networking.dnsDomain">.spec.clusterConfiguration.networking.dnsDomain</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DNSDomain is the dns domain used by k8s services. Defaults to &ldquo;cluster.local&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.networking.podSubnet">.spec.clusterConfiguration.networking.podSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PodSubnet is the subnet used by pods. If unset, the API server will not allocate CIDR ranges for every node. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.services.cidrBlocks if that is set</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.networking.serviceSubnet">.spec.clusterConfiguration.networking.serviceSubnet</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ServiceSubnet is the subnet used by k8s services. Defaults to a comma-delimited string of the Cluster object&rsquo;s spec.clusterNetwork.pods.cidrBlocks, or to &ldquo;10.96.0.0/12&rdquo; if that&rsquo;s unset.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler">.spec.clusterConfiguration.scheduler</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Scheduler contains extra settings for the scheduler control plane component</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraArgs">.spec.clusterConfiguration.scheduler.extraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExtraArgs is an extra set of flags to pass to the control plane component. TODO: This is temporary and ideally we would like to switch all components to use ComponentConfig + ConfigMaps.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes">.spec.clusterConfiguration.scheduler.extraVolumes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraVolumes is an extra set of host volumes, mounted to the control plane component.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*]">.spec.clusterConfiguration.scheduler.extraVolumes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>HostPathMount contains elements describing volumes that are mounted from the host.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].hostPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>HostPath is the path in the host that will be mounted inside the pod.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath">.spec.clusterConfiguration.scheduler.extraVolumes[*].mountPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>MountPath is the path inside the pod where hostPath will be mounted.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*].name">.spec.clusterConfiguration.scheduler.extraVolumes[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the volume inside the pod template.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType">.spec.clusterConfiguration.scheduler.extraVolumes[*].pathType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PathType is the type of the HostPath.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly">.spec.clusterConfiguration.scheduler.extraVolumes[*].readOnly</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>ReadOnly controls write access to the volume</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup">.spec.diskSetup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>DiskSetup specifies options for the creation of partition tables and file systems on devices.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems">.spec.diskSetup.filesystems</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Filesystems specifies the list of file systems to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*]">.spec.diskSetup.filesystems[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Filesystem defines the file systems to be created.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].device">.spec.diskSetup.filesystems[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device specifies the device name</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].extraOpts">.spec.diskSetup.filesystems[*].extraOpts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ExtraOpts defined extra options to add to the command for creating the file system.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].extraOpts[*]">.spec.diskSetup.filesystems[*].extraOpts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].filesystem">.spec.diskSetup.filesystems[*].filesystem</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Filesystem specifies the file system type.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].label">.spec.diskSetup.filesystems[*].label</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Label specifies the file system label to be used. If set to None, no label is used.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].overwrite">.spec.diskSetup.filesystems[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite defines whether or not to overwrite any existing filesystem. If true, any pre-existing file system will be destroyed. Use with Caution.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].partition">.spec.diskSetup.filesystems[*].partition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Partition specifies the partition to use. The valid options are: &ldquo;auto|any&rdquo;, &ldquo;auto&rdquo;, &ldquo;any&rdquo;, &ldquo;none&rdquo;, and <NUM>, where NUM is the actual partition number.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.filesystems[*].replaceFS">.spec.diskSetup.filesystems[*].replaceFS</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ReplaceFS is a special directive, used for Microsoft Azure that instructs cloud-init to replace a file system of <FS_TYPE>. NOTE: unless you define a label, this requires the use of the &lsquo;any&rsquo; partition directive.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions">.spec.diskSetup.partitions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Partitions specifies the list of the partitions to setup.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions[*]">.spec.diskSetup.partitions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Partition defines how to create and layout a partition.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions[*].device">.spec.diskSetup.partitions[*].device</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Device is the name of the device.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions[*].layout">.spec.diskSetup.partitions[*].layout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Layout specifies the device layout. If it is true, a single partition will be created for the entire device. When layout is false, it means don&rsquo;t partition or ignore existing partitioning.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions[*].overwrite">.spec.diskSetup.partitions[*].overwrite</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Overwrite describes whether to skip checks and create the partition if a partition or filesystem is found on the device. Use with caution. Default is &lsquo;false&rsquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.diskSetup.partitions[*].tableType">.spec.diskSetup.partitions[*].tableType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TableType specifies the tupe of partition table. The following are supported: &lsquo;mbr&rsquo;: default and setups a MS-DOS partition table &lsquo;gpt&rsquo;: setups a GPT partition table</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files">.spec.files</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Files specifies extra files to be passed to user_data upon creation.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*]">.spec.files[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File defines the input for generating write_files in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].content">.spec.files[*].content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Content is the actual content of the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].contentFrom">.spec.files[*].contentFrom</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ContentFrom is a referenced source of content to populate the file.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].contentFrom.secret">.spec.files[*].contentFrom.secret</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Secret represents a secret that should populate this file.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].contentFrom.secret.key">.spec.files[*].contentFrom.secret.key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Key is the key in the secret&rsquo;s data map for this value.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].contentFrom.secret.name">.spec.files[*].contentFrom.secret.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the secret in the KubeadmBootstrapConfig&rsquo;s namespace to use.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].encoding">.spec.files[*].encoding</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Encoding specifies the encoding of the file contents.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].owner">.spec.files[*].owner</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Owner specifies the ownership of the file, e.g. &ldquo;root:root&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].path">.spec.files[*].path</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Path specifies the full path on disk where to store the file.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.files[*].permissions">.spec.files[*].permissions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Permissions specifies the permissions to assign to the file, e.g. &ldquo;0640&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.format">.spec.format</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Format specifies the output format of the bootstrap data</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration">.spec.initConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>InitConfiguration along with ClusterConfiguration are the configurations necessary for the init command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.apiVersion">.spec.initConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens">.spec.initConfiguration.bootstrapTokens</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>BootstrapTokens is respected at <code>kubeadm init</code> time and describes a set of Bootstrap Tokens to create. This information IS NOT uploaded to the kubeadm cluster configmap, partly because of its sensitive nature</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*]">.spec.initConfiguration.bootstrapTokens[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken describes one bootstrap token, stored as a Secret in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].description">.spec.initConfiguration.bootstrapTokens[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description sets a human-friendly message why this token exists and what it&rsquo;s used for, so other administrators can know its purpose.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].expires">.spec.initConfiguration.bootstrapTokens[*].expires</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Expires specifies the timestamp when this token expires. Defaults to being set dynamically at runtime based on the TTL. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].groups">.spec.initConfiguration.bootstrapTokens[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Groups specifies the extra groups that this token will authenticate as when/if used for authentication</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].groups[*]">.spec.initConfiguration.bootstrapTokens[*].groups[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].token">.spec.initConfiguration.bootstrapTokens[*].token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is used for establishing bidirectional trust between nodes and control-planes. Used for joining nodes in the cluster.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].ttl">.spec.initConfiguration.bootstrapTokens[*].ttl</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TTL defines the time to live for this token. Defaults to 24h. Expires and TTL are mutually exclusive.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].usages">.spec.initConfiguration.bootstrapTokens[*].usages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Usages describes the ways in which this token can be used. Can by default be used for establishing bidirectional trust, but that can be changed here.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.bootstrapTokens[*].usages[*]">.spec.initConfiguration.bootstrapTokens[*].usages[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.kind">.spec.initConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.localAPIEndpoint">.spec.initConfiguration.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance that&rsquo;s deployed on this control plane node In HA setups, this differs from ClusterConfiguration.ControlPlaneEndpoint in the sense that ControlPlaneEndpoint is the global endpoint for the cluster, which then loadbalances the requests to each individual API server. This configuration object lets you customize what IP/DNS name and port the local API server advertises it&rsquo;s accessible on. By default, kubeadm tries to auto-detect the IP of the default interface and use that, but in case that process fails you may set the desired value here.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.localAPIEndpoint.advertiseAddress">.spec.initConfiguration.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.localAPIEndpoint.bindPort">.spec.initConfiguration.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration">.spec.initConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.criSocket">.spec.initConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.ignorePreflightErrors">.spec.initConfiguration.nodeRegistration.ignorePreflightErrors</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>IgnorePreflightErrors provides a slice of pre-flight errors to be ignored when the current node is registered.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.ignorePreflightErrors[*]">.spec.initConfiguration.nodeRegistration.ignorePreflightErrors[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.kubeletExtraArgs">.spec.initConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.name">.spec.initConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints">.spec.initConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints[*]">.spec.initConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints[*].effect">.spec.initConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints[*].key">.spec.initConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints[*].timeAdded">.spec.initConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.initConfiguration.nodeRegistration.taints[*].value">.spec.initConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration">.spec.joinConfiguration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JoinConfiguration is the kubeadm configuration for the join command</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.apiVersion">.spec.joinConfiguration.apiVersion</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.caCertPath">.spec.joinConfiguration.caCertPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CACertPath is the path to the SSL certificate authority used to secure comunications between node and control-plane. Defaults to &ldquo;/etc/kubernetes/pki/ca.crt&rdquo;. TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.controlPlane">.spec.joinConfiguration.controlPlane</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ControlPlane defines the additional control plane instance to be deployed on the joining node. If nil, no additional control plane instance will be deployed.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.controlPlane.localAPIEndpoint">.spec.joinConfiguration.controlPlane.localAPIEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>LocalAPIEndpoint represents the endpoint of the API server instance to be deployed on this node.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress">.spec.joinConfiguration.controlPlane.localAPIEndpoint.advertiseAddress</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>AdvertiseAddress sets the IP address for the API server to advertise.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort">.spec.joinConfiguration.controlPlane.localAPIEndpoint.bindPort</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>BindPort sets the secure port for the API Server to bind to. Defaults to 6443.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery">.spec.joinConfiguration.discovery</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Discovery specifies the options for the kubelet to use during the TLS Bootstrap process TODO: revisit when there is defaulting from k/k</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken">.spec.joinConfiguration.discovery.bootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>BootstrapToken is used to set the options for bootstrap token based discovery BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint">.spec.joinConfiguration.discovery.bootstrapToken.apiServerEndpoint</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIServerEndpoint is an IP or domain name to the API server from which info will be fetched.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>CACertHashes specifies a set of public key pins to verify when token-based discovery is used. The root CA found during discovery must match one of these values. Specifying an empty set disables root CA pinning, which can be unsafe. Each hash is specified as &ldquo;<type>:<value>&rdquo;, where the only currently supported type is &ldquo;sha256&rdquo;. This is a hex-encoded SHA-256 hash of the Subject Public Key Info (SPKI) object in DER-encoded ASN.1. These hashes can be calculated using, for example, OpenSSL: openssl x509 -pubkey -in ca.crt openssl rsa -pubin -outform der 2&gt;&amp;/dev/null | openssl dgst -sha256 -hex</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]">.spec.joinConfiguration.discovery.bootstrapToken.caCertHashes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken.token">.spec.joinConfiguration.discovery.bootstrapToken.token</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Token is a token used to validate cluster information fetched from the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification">.spec.joinConfiguration.discovery.bootstrapToken.unsafeSkipCAVerification</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UnsafeSkipCAVerification allows token-based discovery without CA verification via CACertHashes. This can weaken the security of kubeadm since other nodes can impersonate the control-plane.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.file">.spec.joinConfiguration.discovery.file</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>File is used to specify a file or URL to a kubeconfig file from which to load cluster information BootstrapToken and File are mutually exclusive</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.file.kubeConfigPath">.spec.joinConfiguration.discovery.file.kubeConfigPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>KubeConfigPath is used to specify the actual file path or URL to the kubeconfig file from which to load cluster information</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.timeout">.spec.joinConfiguration.discovery.timeout</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Timeout modifies the discovery timeout</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.discovery.tlsBootstrapToken">.spec.joinConfiguration.discovery.tlsBootstrapToken</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TLSBootstrapToken is a token used for TLS bootstrapping. If .BootstrapToken is set, this field is defaulted to .BootstrapToken.Token, but can be overridden. If .File is set, this field <strong>must be set</strong> in case the KubeConfigFile does not contain any other authentication information</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.kind">.spec.joinConfiguration.kind</h3>
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

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration">.spec.joinConfiguration.nodeRegistration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NodeRegistration holds fields that relate to registering the new control-plane node to the cluster. When used in the context of control plane nodes, NodeRegistration should remain consistent across both InitConfiguration and JoinConfiguration</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.criSocket">.spec.joinConfiguration.nodeRegistration.criSocket</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>CRISocket is used to retrieve container runtime info. This information will be annotated to the Node API object, for later re-use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors">.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>IgnorePreflightErrors provides a slice of pre-flight errors to be ignored when the current node is registered.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors[*]">.spec.joinConfiguration.nodeRegistration.ignorePreflightErrors[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs">.spec.joinConfiguration.nodeRegistration.kubeletExtraArgs</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>KubeletExtraArgs passes through extra arguments to the kubelet. The arguments here are passed to the kubelet command line via the environment file kubeadm writes at runtime for the kubelet to source. This overrides the generic base-level configuration in the kubelet-config-1.X ConfigMap Flags have higher priority when parsing. These values are local and specific to the node kubeadm is executing on.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.name">.spec.joinConfiguration.nodeRegistration.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is the <code>.Metadata.Name</code> field of the Node API object that will be created in this <code>kubeadm init</code> or <code>kubeadm join</code> operation. This field is also used in the CommonName field of the kubelet&rsquo;s client certificate to the API server. Defaults to the hostname of the node if not provided.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints">.spec.joinConfiguration.nodeRegistration.taints</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Taints specifies the taints the Node API object should be registered with. If this field is unset, i.e. nil, in the <code>kubeadm init</code> process it will be defaulted to []v1.Taint{&lsquo;node-role.kubernetes.io/master=&ldquo;&rdquo;&rsquo;}. If you don&rsquo;t want to taint your control-plane node, set this field to an empty slice, i.e. <code>taints: {}</code> in the YAML file. This field is solely used for Node registration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints[*]">.spec.joinConfiguration.nodeRegistration.taints[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>The node this Taint is attached to has the &ldquo;effect&rdquo; on any pod that does not tolerate the Taint.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints[*].effect">.spec.joinConfiguration.nodeRegistration.taints[*].effect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The effect of the taint on pods that do not tolerate the taint. Valid effects are NoSchedule, PreferNoSchedule and NoExecute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints[*].key">.spec.joinConfiguration.nodeRegistration.taints[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Required. The taint key to be applied to a node.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded">.spec.joinConfiguration.nodeRegistration.taints[*].timeAdded</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TimeAdded represents the time at which the taint was added. It is only written for NoExecute taints.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.joinConfiguration.nodeRegistration.taints[*].value">.spec.joinConfiguration.nodeRegistration.taints[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>The taint value corresponding to the taint key.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.mounts">.spec.mounts</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Mounts specifies a list of mount points to be setup.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.mounts[*]">.spec.mounts[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>MountPoints defines input for generated mounts in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.ntp">.spec.ntp</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>NTP specifies NTP configuration</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.ntp.enabled">.spec.ntp.enabled</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Enabled specifies whether NTP should be enabled</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.ntp.servers">.spec.ntp.servers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Servers specifies which NTP servers to use</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.ntp.servers[*]">.spec.ntp.servers[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.postKubeadmCommands">.spec.postKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PostKubeadmCommands specifies extra commands to run after kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.postKubeadmCommands[*]">.spec.postKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.preKubeadmCommands">.spec.preKubeadmCommands</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>PreKubeadmCommands specifies extra commands to run before kubeadm runs</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.preKubeadmCommands[*]">.spec.preKubeadmCommands[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.useExperimentalRetryJoin">.spec.useExperimentalRetryJoin</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>UseExperimentalRetryJoin replaces a basic kubeadm command with a shell script with retries for joins.
 This is meant to be an experimental temporary workaround on some environments where joins fail due to timing (and other issues). The long term goal is to add retries to kubeadm proper and use that functionality.
 This will add about 40KB to userdata
 For more information, refer to <a href="https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055">https://github.com/kubernetes-sigs/cluster-api/pull/2763#discussion_r397306055</a>.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users">.spec.users</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Users specifies extra users to add</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*]">.spec.users[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>User defines the input for a generated user in cloud-init.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].gecos">.spec.users[*].gecos</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Gecos specifies the gecos to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].groups">.spec.users[*].groups</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Groups specifies the additional groups for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].homeDir">.spec.users[*].homeDir</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>HomeDir specifies the home directory to use for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].inactive">.spec.users[*].inactive</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Inactive specifies whether to mark the user as inactive</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].lockPassword">.spec.users[*].lockPassword</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>LockPassword specifies if password login should be disabled</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].name">.spec.users[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name specifies the user name</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].passwd">.spec.users[*].passwd</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Passwd specifies a hashed password for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].primaryGroup">.spec.users[*].primaryGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>PrimaryGroup specifies the primary group for the user</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].shell">.spec.users[*].shell</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Shell specifies the user&rsquo;s shell</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].sshAuthorizedKeys">.spec.users[*].sshAuthorizedKeys</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>SSHAuthorizedKeys specifies a list of ssh authorized keys for the user</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].sshAuthorizedKeys[*]">.spec.users[*].sshAuthorizedKeys[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.users[*].sudo">.spec.users[*].sudo</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Sudo specifies a sudo role for the user</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.spec.verbosity">.spec.verbosity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Verbosity is the number for the kubeadm log level verbosity. It overrides the <code>--v</code> flag in kubeadm commands.</p>

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
<p>KubeadmConfigStatus defines the observed state of KubeadmConfig.</p>

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
<p>Conditions defines current service state of the KubeadmConfig.</p>

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
<h3 class="property-path" id="v1beta1-.status.dataSecretName">.status.dataSecretName</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>DataSecretName is the name of the secret that stores the bootstrap data script.</p>

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
<p>FailureMessage will be set on non-retryable errors</p>

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
<p>FailureReason will be set on non-retryable errors</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1beta1-.status.observedGeneration">.status.observedGeneration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>ObservedGeneration is the latest generation observed by the controller.</p>

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
<p>Ready indicates the BootstrapData field is ready to be consumed</p>

</div>

</div>
</div>





</div>



