---
title: AWSControlPlane CRD schema reference
linkTitle: AWSControlPlane
technical_name: awscontrolplanes.infrastructure.giantswarm.io
description:   AWSControlPlane is the infrastructure provider referenced in ControlPlane CRs. Represents the master nodes (also called Control Plane) of a workload cluster on AWS. Reconciled by aws-operator.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.18.1
layout: crd
aliases:
  - /reference/cp-k8s-api/awscontrolplanes.infrastructure.giantswarm.io/
---

# AWSControlPlane


<p class="crd-description">AWSControlPlane is the infrastructure provider referenced in ControlPlane CRs. Represents the master nodes (also called Control Plane) of a workload cluster on AWS. Reconciled by aws-operator.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">awscontrolplanes.infrastructure.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">awscontrolplane</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">awscontrolplanes</dd>
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
kind: AWSControlPlane
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/awscontrolplanes.infrastructure.giantswarm.io/
  creationTimestamp: null
  name: ier2s
spec:
  availabilityZones:
  - eu-central-1a
  - eu-central-1b
  - eu-central-1c
  instanceType: m4.xlarge
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
<p>Specification part of the resource.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.availabilityZones">.spec.availabilityZones</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Configures which AWS availability zones to use by master nodes, as a list of availability zone names like e. g. <code>eu-central-1c</code>. We support either 1 or 3 availability zones.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.availabilityZones[*]">.spec.availabilityZones[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.instanceType">.spec.instanceType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>EC2 instance type identifier to use for the master node(s).</p>

</div>

</div>
</div>





</div>



