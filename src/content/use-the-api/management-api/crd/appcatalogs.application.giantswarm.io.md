---
title: AppCatalog CRD schema reference (group application.giantswarm.io)
linkTitle: AppCatalog
description: |
  Deprecated, use Catalog CRD instead. AppCatalog represents a catalog of managed apps. It stores general information for potential apps to install. It is reconciled by app-operator.
weight: 100
crd:
  name_camelcase: AppCatalog
  name_plural: appcatalogs
  name_singular: appcatalog
  group: application.giantswarm.io
  technical_name: appcatalogs.application.giantswarm.io
  scope: Cluster
  source_repository: https://github.com/giantswarm/apiextensions-application
  source_repository_ref: v0.6.0
  versions:
    - v1alpha1
  topics:
    - apps
  deprecation:
    replaced_by:
      full_name: catalogs.application.giantswarm.io
      short_name: Catalog
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /reference/cp-k8s-api/appcatalogs.application.giantswarm.io/
technical_name: appcatalogs.application.giantswarm.io
source_repository: https://github.com/giantswarm/apiextensions-application
source_repository_ref: v0.6.0
---

# AppCatalog
<p class="well disclaimer">
<i class="fa fa-warning"></i> <b>Deprecation:</b>
This CRD is being replaced by <a href="../catalogs.application.giantswarm.io/">Catalog</a>.
</p>


<p class="crd-description">Deprecated, use Catalog CRD instead. AppCatalog represents a catalog of managed apps. It stores general information for potential apps to install. It is reconciled by app-operator.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">appcatalogs.application.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">application.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">appcatalog</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">appcatalogs</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Cluster</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: AppCatalog
metadata:
  creationTimestamp: null
  labels:
    app-operator.giantswarm.io/version: 1.0.0
  name: my-playground-catalog
spec:
  config:
    configMap:
      name: my-playground-catalog
      namespace: my-namespace
    secret:
      name: my-playground-catalog
      namespace: my-namespace
  description: A catalog to store all new application packages.
  logoURL: https://my-org.github.com/logo.png
  storage:
    URL: https://my-org.github.com/my-playground-catalog/
    type: helm
  title: My Playground Catalog
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

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config">.spec.config</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Config is the config to be applied when apps belonging to this catalog are deployed.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.configMap">.spec.config.configMap</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ConfigMap references a config map containing catalog values that should be applied to apps in this catalog.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.configMap.name">.spec.config.configMap.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the config map containing catalog values to apply, e.g. app-catalog-values.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.configMap.namespace">.spec.config.configMap.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Namespace is the namespace of the catalog values config map, e.g. giantswarm.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.secret">.spec.config.secret</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Secret references a secret containing catalog values that should be applied to apps in this catalog.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.secret.name">.spec.config.secret.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of the secret containing catalog values to apply, e.g. app-catalog-secret.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.config.secret.namespace">.spec.config.secret.namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Namespace is the namespace of the secret, e.g. giantswarm.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.description">.spec.description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.logoURL">.spec.logoURL</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>LogoURL contains the links for logo image file for this app catalog</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.storage">.spec.storage</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Storage references a map containing values that should be applied to the appcatalog.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.storage.URL">.spec.storage.URL</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>URL is the link to where this AppCatalog&rsquo;s repository is located e.g. <a href="https://example.com/app-catalog/">https://example.com/app-catalog/</a></p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.storage.type">.spec.storage.type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Type indicates which repository type would be used for this AppCatalog. e.g. helm</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.title">.spec.title</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Title is the name of the app catalog for this CR e.g. Catalog of Apps by Giant Swarm</p>

</div>

</div>
</div>





</div>



