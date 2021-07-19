---
title: AWSClusterStaticIdentity CRD schema reference
linkTitle: AWSClusterStaticIdentity
technical_name: awsclusterstaticidentities.infrastructure.cluster.x-k8s.io
description: |
  AWSClusterStaticIdentity is the Schema for the awsclusterstaticidentities API It represents a reference to an AWS access key ID and secret access key, stored in a secret.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.27.2
layout: crd
aliases:
  - /reference/cp-k8s-api/awsclusterstaticidentities.infrastructure.cluster.x-k8s.io/
---

# AWSClusterStaticIdentity


<p class="crd-description">AWSClusterStaticIdentity is the Schema for the awsclusterstaticidentities API It represents a reference to an AWS access key ID and secret access key, stored in a secret.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">awsclusterstaticidentities.infrastructure.cluster.x-k8s.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.cluster.x-k8s.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">awsclusterstaticidentity</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">awsclusterstaticidentities</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Cluster</dd>
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
<p>Spec for this AWSClusterStaticIdentity</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces">.spec.allowedNamespaces</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AllowedNamespaces is used to identify which namespaces are allowed to use the identity from. Namespaces can be selected either using an array of namespaces or with label selector. An empty allowedNamespaces object indicates that AWSClusters can use this identity from any namespace. If this object is nil, no namespaces will be allowed (default behaviour, if this field is not provided) A namespace should be either in the NamespaceList or match with Selector to use the identity.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.list">.spec.allowedNamespaces.list</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>An nil or empty list indicates that AWSClusters cannot use the identity from any namespace.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.list[*]">.spec.allowedNamespaces.list[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector">.spec.allowedNamespaces.selector</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>AllowedNamespaces is a selector of namespaces that AWSClusters can use this ClusterPrincipal from. This is a standard Kubernetes LabelSelector, a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed.
 An empty selector indicates that AWSClusters cannot use this AWSClusterIdentity from any namespace.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions">.spec.allowedNamespaces.selector.matchExpressions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>matchExpressions is a list of label selector requirements. The requirements are ANDed.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions[*]">.spec.allowedNamespaces.selector.matchExpressions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions[*].key">.spec.allowedNamespaces.selector.matchExpressions[*].key</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>key is the label key that the selector applies to.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions[*].operator">.spec.allowedNamespaces.selector.matchExpressions[*].operator</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>operator represents a key&rsquo;s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions[*].values">.spec.allowedNamespaces.selector.matchExpressions[*].values</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchExpressions[*].values[*]">.spec.allowedNamespaces.selector.matchExpressions[*].values[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.allowedNamespaces.selector.matchLabels">.spec.allowedNamespaces.selector.matchLabels</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is &ldquo;key&rdquo;, the operator is &ldquo;In&rdquo;, and the values array contains only &ldquo;value&rdquo;. The requirements are ANDed.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.secretRef">.spec.secretRef</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Reference to a secret containing the credentials. The secret should contain the following data keys:  AccessKeyID: AKIAIOSFODNN7EXAMPLE  SecretAccessKey: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY  SessionToken: Optional</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.secretRef.name">.spec.secretRef.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Name is unique within a namespace to reference a secret resource.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha3-.spec.secretRef.namespace">.spec.secretRef.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Namespace defines the space within which the secret name must be unique.</p>

</div>

</div>
</div>





</div>



