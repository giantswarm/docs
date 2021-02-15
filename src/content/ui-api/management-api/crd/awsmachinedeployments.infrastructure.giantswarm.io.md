---
title: AWSMachineDeployment CRD schema reference
linkTitle: AWSMachineDeployment
technical_name: awsmachinedeployments.infrastructure.giantswarm.io
description:   AWSMachineDeployment is the infrastructure provider referenced in Kubernetes Cluster API MachineDeployment resources. It contains provider-specific specification and status for a node pool. In use on AWS since Giant Swarm release v10.x.x and reconciled by aws-operator.
weight: 100
source_repository: https://github.com/giantswarm/apiextensions
source_repository_ref: v3.18.1
layout: crd
aliases:
  - /reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io/
---

# AWSMachineDeployment


<p class="crd-description">AWSMachineDeployment is the infrastructure provider referenced in Kubernetes Cluster API MachineDeployment resources. It contains provider-specific specification and status for a node pool. In use on AWS since Giant Swarm release v10.x.x and reconciled by aws-operator.</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">awsmachinedeployments.infrastructure.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">infrastructure.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">awsmachinedeployment</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">awsmachinedeployments</dd>
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
kind: AWSMachineDeployment
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/reference/cp-k8s-api/awsmachinedeployments.infrastructure.giantswarm.io
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: 8.7.0
    giantswarm.io/cluster: al9qy
    giantswarm.io/machine-deployment: wk4np
    giantswarm.io/organization: giantswarm
    release.giantswarm.io/version: 11.5.0
  name: wk4np
  namespace: default
spec:
  nodePool:
    description: General purpose worker nodes
    machine:
      dockerVolumeSizeGB: 100
      kubeletVolumeSizeGB: 100
    scaling:
      max: 50
      min: 2
  provider:
    availabilityZones:
    - eu-central-1b
    - eu-central-1c
    instanceDistribution:
      onDemandBaseCapacity: 2
      onDemandPercentageAboveBaseCapacity: 50
    worker:
      instanceType: m5.4xlarge
      useAlikeInstanceTypes: true
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
<p>Contains the specification.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool">.spec.nodePool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Specifies details of node pool and the worker nodes it should contain.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.description">.spec.nodePool.description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>User-friendly name or description of the purpose of the node pool.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.machine">.spec.nodePool.machine</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Specification of the worker node machine.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.machine.dockerVolumeSizeGB">.spec.nodePool.machine.dockerVolumeSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Size of the volume reserved for Docker images and overlay file systems of Docker containers. Unit: 1 GB = 1,000,000,000 Bytes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.machine.kubeletVolumeSizeGB">.spec.nodePool.machine.kubeletVolumeSizeGB</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Size of the volume reserved for the kubelet, which can be used by Pods via volumes of type EmptyDir. Unit: 1 GB = 1,000,000,000 Bytes.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.scaling">.spec.nodePool.scaling</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Scaling settings for the node pool, configuring the cluster-autoscaler determining the number of nodes to have in this node pool.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.scaling.max">.spec.nodePool.scaling.max</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Maximum number of worker nodes in this node pool.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.nodePool.scaling.min">.spec.nodePool.scaling.min</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Minimum number of worker nodes in this node pool.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider">.spec.provider</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Contains AWS specific details.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.availabilityZones">.spec.provider.availabilityZones</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Name(s) of the availability zone(s) to use for worker nodes. Using multiple availability zones results in higher resilience but can also result in higher cost due to network traffic between availability zones.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.availabilityZones[*]">.spec.provider.availabilityZones[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.instanceDistribution">.spec.provider.instanceDistribution</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Settings defining the distribution of on-demand and spot instances in the node pool.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.instanceDistribution.onDemandBaseCapacity">.spec.provider.instanceDistribution.onDemandBaseCapacity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Base capacity of on-demand instances to use for worker nodes in this pool. When this larger than 0, this value defines a number of worker nodes that will be created using on-demand EC2 instances, regardless of the value configured as <code>onDemandPercentageAboveBaseCapacity</code>.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.instanceDistribution.onDemandPercentageAboveBaseCapacity">.spec.provider.instanceDistribution.onDemandPercentageAboveBaseCapacity</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Percentage of on-demand EC2 instances to use for worker nodes, instead of spot instances, for instances exceeding <code>onDemandBaseCapacity</code>. For example, to have half of the worker nodes use spot instances and half use on-demand, set this value to 50.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.worker">.spec.provider.worker</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Specification of worker nodes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.worker.instanceType">.spec.provider.worker.instanceType</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>AWS EC2 instance type name to use for the worker nodes in this node pool.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.spec.provider.worker.useAlikeInstanceTypes">.spec.provider.worker.useAlikeInstanceTypes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>If true, certain instance types with specs similar to instanceType will be used.</p>

</div>

</div>
</div>

<div class="property depth-0">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status">.status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Holds status information.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.provider">.status.provider</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Status specific to AWS.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.provider.worker">.status.provider.worker</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Status of worker nodes.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.provider.worker.instanceTypes">.status.provider.worker.instanceTypes</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>AWS EC2 instance types used for the worker nodes in this node pool.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.provider.worker.instanceTypes[*]">.status.provider.worker.instanceTypes[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha2-.status.provider.worker.spotInstances">.status.provider.worker.spotInstances</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Number of EC2 spot instances used in this node pool.</p>

</div>

</div>
</div>




<h3 id="annotation-details-v1alpha2">Annotations</h3>


<div class="annotation">
<div class="annotation-header">
<h3 class="annotation-path" id="v1alpha2-alpha.aws.giantswarm.io/aws-subnet-size">alpha.aws.giantswarm.io/aws-subnet-size</h3>
</div>
<div class="annotation-body">
<div class="annotation-meta">
<span class="annotation-release">Since 12.7.0</span>
</div>

<div class="annotation-description">
<p>This annotation is used for configuring the subnet size of AWSCluster or AWSMachineDeployment. The value is a number that will represent the subnet mask used when creating the subnet. This value must be smaller than 28 due to AWS restrictions.</p>

</div>

</div>
</div>

<div class="annotation">
<div class="annotation-header">
<h3 class="annotation-path" id="v1alpha2-alpha.aws.giantswarm.io/update-max-batch-size">alpha.aws.giantswarm.io/update-max-batch-size</h3>
</div>
<div class="annotation-body">
<div class="annotation-meta">
<span class="annotation-release">Since 12.7.0</span>
</div>

<div class="annotation-description">
<p>This annotation is used for configuring maximum batch size for instances termination during ASG update. The value can be either a whole number specifying the number of instances or a percentage of total instances as decimal number ie <code>0.3</code> for 30%. See <a href="https://docs.giantswarm.io/guides/fine-tuning-upgrade-disruption-on-aws/">Fine Tuning Upgrades</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-rollingupdate-maxbatchsize">AWS Documentation</a> for additional information.</p>

</div>

</div>
</div>

<div class="annotation">
<div class="annotation-header">
<h3 class="annotation-path" id="v1alpha2-alpha.aws.giantswarm.io/update-pause-time">alpha.aws.giantswarm.io/update-pause-time</h3>
</div>
<div class="annotation-body">
<div class="annotation-meta">
<span class="annotation-release">Since 12.7.0</span>
</div>

<div class="annotation-description">
<p>This annotation is used for configuring time pause between rolling a single batch during ASG update. The value must be in ISO 8601 duration format, e. g. &ldquo;PT5M&rdquo; for five minutes or &ldquo;PT10S&rdquo; for 10 seconds. See <a href="https://docs.giantswarm.io/guides/fine-tuning-upgrade-disruption-on-aws/">Fine Tuning Upgrades</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-updatepolicy.html#cfn-attributes-updatepolicy-rollingupdate-maxbatchsize">AWS Documentation</a> for additional information.</p>

</div>

</div>
</div>



</div>



