---
title: KonfigurationSchema CRD schema reference (group konfigure.giantswarm.io)
linkTitle: KonfigurationSchema
description: |
  KonfigurationSchema is the Schema for the konfigurationschemas API.
weight: 100
crd:
  name_camelcase: KonfigurationSchema
  name_plural: konfigurationschemas
  name_singular: konfigurationschema
  group: konfigure.giantswarm.io
  technical_name: konfigurationschemas.konfigure.giantswarm.io
  scope: Namespaced
  source_repository: https://github.com/giantswarm/konfigure-operator
  source_repository_ref: v1.0.1
  versions:
    - v1alpha1
  topics:
    - configuration
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /use-the-api/management-api/crd/konfigurationschemas.konfigure.giantswarm.io/
technical_name: konfigurationschemas.konfigure.giantswarm.io
source_repository: https://github.com/giantswarm/konfigure-operator
source_repository_ref: v1.0.1
---

# KonfigurationSchema


<p class="crd-description">KonfigurationSchema is the Schema for the konfigurationschemas API.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">konfigurationschemas.konfigure.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">konfigure.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">konfigurationschema</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">konfigurationschemas</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>

```yaml
apiVersion: konfigure.giantswarm.io/v1alpha1
kind: KonfigurationSchema
metadata:
  name: konfigurationschema-sample
  namespace: default
spec:
  raw:
    remote:
      url: https://raw.githubusercontent.com/giantswarm/konfiguration-schemas/refs/tags/management-cluster-configuration/v1.0.0/schemas/management-cluster-configuration/schema.yaml
```


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
<p>APIVersion defines the versioned schema of this representation of an object.
Servers should convert recognized schemas to the latest internal value, and
may reject unrecognized values.
More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p>

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
<p>Kind is a string value representing the REST resource this object represents.
Servers may infer this from the endpoint the client submits requests to.
Cannot be updated.
In CamelCase.
More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds</a></p>

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

</div>

<div class="property-description">
<p>KonfigurationSchemaSpec defines the desired state of KonfigurationSchema.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.raw">.spec.raw</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Raw defines simple ways of accessing a konfiguration schema.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.raw.content">.spec.raw.content</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Provide the raw manifest store under this field as a multiline string.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.raw.remote">.spec.raw.remote</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Provide the schema manifest from a remote location.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.raw.remote.url">.spec.raw.remote.url</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>URL for the location of the schema manifest.</p>

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
<p>KonfigurationSchemaStatus defines the observed state of KonfigurationSchema.</p>

</div>

</div>
</div>





</div>



