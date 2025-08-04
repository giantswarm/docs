---
title: Silence CRD schema reference (group observability.giantswarm.io)
linkTitle: Silence
description: |
  Silence is the Schema for the silences API.
weight: 100
crd:
  name_camelcase: Silence
  name_plural: silences
  name_singular: silence
  group: observability.giantswarm.io
  technical_name: silences.observability.giantswarm.io
  scope: Namespaced
  source_repository: https://github.com/giantswarm/silence-operator
  source_repository_ref: v0.18.0
  versions:
    - v1alpha2
  topics:
    - managementcluster
    - observability
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
aliases:
  - /use-the-api/management-api/crd/silences.observability.giantswarm.io/
technical_name: silences.observability.giantswarm.io
source_repository: https://github.com/giantswarm/silence-operator
source_repository_ref: v0.18.0
---

# Silence


<p class="crd-description">Silence is the Schema for the silences API.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">silences.observability.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">observability.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">silence</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">silences</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha2" title="Show schema for version v1alpha2">v1alpha2</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha2">Version v1alpha2</h2>



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
<p>APIVersion defines the versioned schema of this representation of an object.
Servers should convert recognized schemas to the latest internal value, and
may reject unrecognized values.
More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources</a></p>

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

</div>

<div class="property-description">
<p>SilenceSpec defines the desired state of Silence.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.matchers">.spec.matchers</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Matchers defines the alert matchers that this silence will apply to.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.matchers[*]">.spec.matchers[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>SilenceMatcher defines an alert matcher to be muted by the Silence.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.matchers[*].matchType">.spec.matchers[*].matchType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>MatchType defines the type of matching to perform.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.matchers[*].name">.spec.matchers[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the label to match.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.matchers[*].value">.spec.matchers[*].value</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Value to match for the given label name.</p>

</div>

</div>
</div>





</div>



