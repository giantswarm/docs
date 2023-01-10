---
title: Organization CRD schema reference (group security.giantswarm.io)
linkTitle: Organization
description: |
  Organization represents schema for managed Kubernetes namespace. Reconciled by organization-operator.
weight: 100
crd:
  name_camelcase: Organization
  name_plural: organizations
  name_singular: organization
  group: security.giantswarm.io
  technical_name: organizations.security.giantswarm.io
  scope: Cluster
  source_repository: https://github.com/giantswarm/organization-operator
  source_repository_ref: v1.0.2
  versions:
    - v1alpha1
  topics:
    - managementcluster
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
aliases:
  - /reference/cp-k8s-api/organizations.security.giantswarm.io/
technical_name: organizations.security.giantswarm.io
source_repository: https://github.com/giantswarm/organization-operator
source_repository_ref: v1.0.2
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

```yaml
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/organizations.security.giantswarm.io/
  name: example-inc
spec: {}
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

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.namespace">.status.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Namespace is the namespace containing the resources for this organization.</p>

</div>

</div>
</div>





</div>



