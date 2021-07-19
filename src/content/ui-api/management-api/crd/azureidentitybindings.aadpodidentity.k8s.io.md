---
title: AzureIdentityBinding CRD schema reference
linkTitle: AzureIdentityBinding
technical_name: azureidentitybindings.aadpodidentity.k8s.io
description: |
  AzureIdentityBinding brings together the spec of matching pods and the identity which they can use.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.27.2
layout: crd
aliases:
  - /reference/cp-k8s-api/azureidentitybindings.aadpodidentity.k8s.io/
---

# AzureIdentityBinding


<p class="crd-description">AzureIdentityBinding brings together the spec of matching pods and the identity which they can use.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">azureidentitybindings.aadpodidentity.k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">aadpodidentity.k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">azureidentitybinding</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">azureidentitybindings</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1" title="Show schema for version v1">v1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1">Version v1</h2>



<h3 id="property-details-v1">Properties</h3>


<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1-.apiVersion">.apiVersion</h3>
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
<h3 class="property-path" id="v1-.kind">.kind</h3>
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
<h3 class="property-path" id="v1-.metadata">.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1-.spec">.spec</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureIdentityBindingSpec matches the pod with the Identity. Used to indicate the potential matches to look for between the pod/deployment and the identities present.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.spec.azureIdentity">.spec.azureIdentity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.spec.metadata">.spec.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.spec.selector">.spec.selector</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.spec.weight">.spec.weight</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Weight is used to figure out which of the matching identities would be selected.</p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AzureIdentityBindingStatus contains the status of an AzureIdentityBinding.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.status.availableReplicas">.status.availableReplicas</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1-.status.metadata">.status.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>





</div>



