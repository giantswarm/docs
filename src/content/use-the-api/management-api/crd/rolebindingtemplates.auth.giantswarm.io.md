---
title: RoleBindingTemplate CRD schema reference (group auth.giantswarm.io)
linkTitle: RoleBindingTemplate
description: |
  RoleBindingTemplate is the Schema for the rolebindingtemplates API
weight: 100
crd:
  name_camelcase: RoleBindingTemplate
  name_plural: rolebindingtemplates
  name_singular: rolebindingtemplate
  group: auth.giantswarm.io
  technical_name: rolebindingtemplates.auth.giantswarm.io
  scope: Cluster
  source_repository: https://github.com/giantswarm/rbac-operator
  source_repository_ref: v0.37.1
  versions:
    - v1alpha1
  topics:
    - managementcluster
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
aliases:
  - /reference/cp-k8s-api/rolebindingtemplates.auth.giantswarm.io/
technical_name: rolebindingtemplates.auth.giantswarm.io
source_repository: https://github.com/giantswarm/rbac-operator
source_repository_ref: v0.37.1
---

# RoleBindingTemplate


<p class="crd-description">RoleBindingTemplate is the Schema for the rolebindingtemplates API</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">rolebindingtemplates.auth.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">auth.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">rolebindingtemplate</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">rolebindingtemplates</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Cluster</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>

```yaml
apiVersion: auth.giantswarm.io/v1alpha1
kind: RoleBindingTemplate
metadata:
  name: rolebindingtemplate-sample
spec:
  template:
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: Role
      name: example-role
    subjects:
    - kind: ServiceAccount
      name: example-sa
    - kind: Group
      name: example-group
  scopes:
    organizationSelector:
      matchLabels:
        key: value
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

</div>

<div class="property-description">
<p>RoleBindingTemplateSpec defines the desired state of RoleBindingTemplate</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.scopes">.spec.scopes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>RoleBindingTemplateScopes describes the scopes the RoleBindingTemplate should be applied to</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.scopes.organizationSelector">.spec.scopes.organizationSelector</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ScopeSelector wraps a k8s label selector</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.scopes.organizationSelector.matchLabels">.spec.scopes.organizationSelector.matchLabels</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template">.spec.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>RoleBindingTemplateResource describes the data needed to create a rolebinding from a template.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.metadata">.spec.template.metadata</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Standard object&rsquo;s metadata.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.roleRef">.spec.template.roleRef</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>RoleRef can reference a Role in the current namespace or a ClusterRole in the global namespace. If the RoleRef cannot be resolved, the Authorizer must return an error.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.roleRef.apiGroup">.spec.template.roleRef.apiGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>APIGroup is the group for the resource being referenced</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.roleRef.kind">.spec.template.roleRef.kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Kind is the type of resource being referenced</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.roleRef.name">.spec.template.roleRef.name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name is the name of resource being referenced</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects">.spec.template.subjects</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Subjects holds references to the objects the role applies to.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects[*]">.spec.template.subjects[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Subject contains a reference to the object or user identities a role binding applies to.  This can either hold a direct API object reference, or a value for non-objects such as user and group names.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects[*].apiGroup">.spec.template.subjects[*].apiGroup</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>APIGroup holds the API group of the referenced subject. Defaults to &ldquo;&rdquo; for ServiceAccount subjects. Defaults to &ldquo;rbac.authorization.k8s.io&rdquo; for User and Group subjects.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects[*].kind">.spec.template.subjects[*].kind</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Kind of object being referenced. Values defined by this API group are &ldquo;User&rdquo;, &ldquo;Group&rdquo;, and &ldquo;ServiceAccount&rdquo;. If the Authorizer does not recognized the kind value, the Authorizer should report an error.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects[*].name">.spec.template.subjects[*].name</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Name of the object being referenced.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.template.subjects[*].namespace">.spec.template.subjects[*].namespace</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Namespace of the referenced object.  If the object kind is non-namespace, such as &ldquo;User&rdquo; or &ldquo;Group&rdquo;, and this value is not empty the Authorizer should report an error.</p>

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
<p>RoleBindingTemplateStatus defines the observed state of RoleBindingTemplate</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.namespaces">.status.namespaces</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Namespaces contains a list of namespaces the RoleBinding is currently applied to</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.namespaces[*]">.status.namespaces[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>





</div>



