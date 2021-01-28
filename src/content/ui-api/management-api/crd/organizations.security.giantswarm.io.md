---
title: Organization CRD schema reference
linktitle: Organization
technical_name: organizations.security.giantswarm.io
description:   Organization represents schema for managed Kubernetes namespace. Reconciled by organization-operator.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.15.0
layout: "crd"
aliases:
  - /reference/cp-k8s-api/organizations.security.giantswarm.io/
---

# Organization


<p class="crd-description">Organization represents schema for managed Kubernetes namespace. Reconciled by organization-operator.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">organizations.security.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">security.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">organization</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">organizations</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Cluster</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>
<pre class="crd-example-cr"><code class="language-yaml">
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/organizations.security.giantswarm.io/
  creationTimestamp: null
  name: example-inc
spec:
  {}
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

</div>
</div>


</div>



