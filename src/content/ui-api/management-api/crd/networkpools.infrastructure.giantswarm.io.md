---
title: NetworkPool CRD schema reference
linkTitle: NetworkPool
technical_name: networkpools.infrastructure.giantswarm.io
description:   NetworkPool is the infrastructure provider referenced in upstream CAPI Cluster CRs.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.20.0
layout: crd
aliases:
  - /reference/cp-k8s-api/networkpools.infrastructure.giantswarm.io/
---

# NetworkPool


<p class="crd-description">NetworkPool is the infrastructure provider referenced in upstream CAPI Cluster CRs.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">networkpools.infrastructure.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">networkpool</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">networkpools</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha2" title="Show schema for version v1alpha2">v1alpha2</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha2">Version v1alpha2</h2>


<h3 id="crd-example-v1alpha2">Example CR</h3>

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: NetworkPool
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/networkpools.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    giantswarm.io/organization: giantswarm
  name: custom
  namespace: default
spec:
  cidrBlock: 192.168.0.0/16
```


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
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>NetworkPoolSpec is the spec part for the NetworkPool resource.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.cidrBlock">.spec.cidrBlock</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>IPv4 address block in CIDR notation.</p>

</div>

</div>
</div>





</div>



