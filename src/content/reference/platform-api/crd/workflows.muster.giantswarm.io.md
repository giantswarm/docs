---
title: Workflow CRD schema reference (group muster.giantswarm.io)
diataxis_content_type: reference
linkTitle: Workflow
description: |
  Workflow is the Schema for the workflows API
weight: 100
crd:
  name_camelcase: Workflow
  name_plural: workflows
  name_singular: workflow
  group: muster.giantswarm.io
  technical_name: workflows.muster.giantswarm.io
  scope: Namespaced
  source_repository: https://github.com/giantswarm/muster
  source_repository_ref: v5.53.3
  versions:
    - v1alpha1
  topics:
    - managementcluster
    - agent-platform
layout: crd
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
aliases:
  - /use-the-api/management-api/crd/workflows.muster.giantswarm.io/
technical_name: workflows.muster.giantswarm.io
source_repository: https://github.com/giantswarm/muster
source_repository_ref: v5.53.3
---

# Workflow


<p class="crd-description">Workflow is the Schema for the workflows API</p>
<dl class="crd-meta">
<dt class="fullname">Full name:</dt>
<dd class="fullname">workflows.muster.giantswarm.io</dd>
<dt class="groupname">Group:</dt>
<dd class="groupname">muster.giantswarm.io</dd>
<dt class="singularname">Singular name:</dt>
<dd class="singularname">workflow</dd>
<dt class="pluralname">Plural name:</dt>
<dd class="pluralname">workflows</dd>
<dt class="scope">Scope:</dt>
<dd class="scope">Namespaced</dd>
<dt class="versions">Versions:</dt>
<dd class="versions"><a class="version" href="#v1alpha1" title="Show schema for version v1alpha1">v1alpha1</a></dd>
</dl>



<div class="crd-schema-version">
<h2 id="v1alpha1">Version v1alpha1</h2>


<h3 id="crd-example-v1alpha1">Example CR</h3>

```yaml
apiVersion: muster.giantswarm.io/v1alpha1
kind: Workflow
metadata:
  name: deploy-application
  namespace: default
spec:
  description: "Deploy application to production environment with validation"
  args:
    app_name:
      type: string
      required: true
      description: "Name of the application to deploy"
    environment:
      type: string
      default: "production"
      description: "Target deployment environment"
    replicas:
      type: integer
      default: 3
      description: "Number of application replicas"
  steps:
    - id: build_image
      tool: docker_build
      args:
        name: "{{.input.app_name}}"
        tag: "{{.input.environment}}-latest"
      output: true
    - id: deploy_service
      tool: kubectl_apply
      args:
        name: "{{.input.app_name}}-{{.input.environment}}"
        image: "{{.results.build_image.image_id}}"
        replicas: "{{.input.replicas}}"
      output: true
    - id: verify_deployment
      tool: health_check
      args:
        service_name: "{{.results.deploy_service.name}}"
        timeout: "5m"
      output: true
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
<p>WorkflowSpec defines the desired state of Workflow</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.args">.spec.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args defines the argument schema for workflow execution validation.</p>

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

</div>

<div class="property-description">
<p>Description provides a human-readable description of the workflow&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure">.spec.onFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>OnFailure defines best-effort cleanup/rollback steps that run when the
workflow fails on a step that does not allow failure. The steps execute
sequentially and their own failures are tolerated.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*]">.spec.onFailure[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowSubStep is a step used inside forEach bodies, parallel groups, and
onFailure handlers: a tool call or, in a forEach body only, a nested
forEach. Unlike WorkflowStep it cannot hold a parallel group, and a nested
forEach holds tool calls only, which keeps the CRD schema structural
(non-recursive).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].allowFailure">.spec.onFailure[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].args">.spec.onFailure[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition">.spec.onFailure[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.args">.spec.onFailure[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expect">.spec.onFailure[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expect.jsonPath">.spec.onFailure[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expect.success">.spec.onFailure[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expectNot">.spec.onFailure[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expectNot.jsonPath">.spec.onFailure[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.expectNot.success">.spec.onFailure[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.fromStep">.spec.onFailure[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.template">.spec.onFailure[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].condition.tool">.spec.onFailure[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].description">.spec.onFailure[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach">.spec.onFailure[*].forEach</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ForEach makes this sub-step a nested loop, one level deep. Only valid in
a forEach body (not in parallel or onFailure); its loop variable must
differ from the outer one. Mutually exclusive with tool.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.as">.spec.onFailure[*].forEach.as</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>As is the loop variable name made available to the body as
&ldquo;{{ .vars.<as> }}&rdquo;. Defaults to &ldquo;item&rdquo;; it must differ from the outer
loop&rsquo;s.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.items">.spec.onFailure[*].forEach.items</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Items is a template expression that must resolve to an array, typically
a result of an earlier sub-step of the outer iteration, e.g.
&ldquo;{{ .results.clusters.items }}&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.parallelism">.spec.onFailure[*].forEach.parallelism</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Parallelism is how many iterations may run at once within one outer
iteration. The calls in flight at once are at most the outer
parallelism times this one.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps">.spec.onFailure[*].forEach.steps</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Steps is the body executed for each item.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*]">.spec.onFailure[*].forEach.steps[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowNestedStep is a tool-call step in the body of a nested forEach.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].allowFailure">.spec.onFailure[*].forEach.steps[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].args">.spec.onFailure[*].forEach.steps[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition">.spec.onFailure[*].forEach.steps[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.args">.spec.onFailure[*].forEach.steps[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expect">.spec.onFailure[*].forEach.steps[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expect.jsonPath">.spec.onFailure[*].forEach.steps[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expect.success">.spec.onFailure[*].forEach.steps[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expectNot">.spec.onFailure[*].forEach.steps[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expectNot.jsonPath">.spec.onFailure[*].forEach.steps[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.expectNot.success">.spec.onFailure[*].forEach.steps[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.fromStep">.spec.onFailure[*].forEach.steps[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.template">.spec.onFailure[*].forEach.steps[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].condition.tool">.spec.onFailure[*].forEach.steps[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].description">.spec.onFailure[*].forEach.steps[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].id">.spec.onFailure[*].forEach.steps[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].jq">.spec.onFailure[*].forEach.steps[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].output">.spec.onFailure[*].forEach.steps[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by
later steps regardless of this flag.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].paginate">.spec.onFailure[*].forEach.steps[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes the sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].paginate.itemsField">.spec.onFailure[*].forEach.steps[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].paginate.maxPages">.spec.onFailure[*].forEach.steps[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].paginate.tokenArg">.spec.onFailure[*].forEach.steps[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].paginate.tokenField">.spec.onFailure[*].forEach.steps[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].store">.spec.onFailure[*].forEach.steps[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].forEach.steps[*].tool">.spec.onFailure[*].forEach.steps[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].id">.spec.onFailure[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].jq">.spec.onFailure[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq). On a nested forEach it reshapes the loop&rsquo;s
per-iteration records.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].output">.spec.onFailure[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by later
steps regardless of this flag. When unset, the deprecated Store flag is
used as a fallback.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].paginate">.spec.onFailure[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes a tool sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].paginate.itemsField">.spec.onFailure[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].paginate.maxPages">.spec.onFailure[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].paginate.tokenArg">.spec.onFailure[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].paginate.tokenField">.spec.onFailure[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].store">.spec.onFailure[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.onFailure[*].tool">.spec.onFailure[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute. Mutually exclusive
with forEach.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.output">.spec.output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Output is an optional output template that shapes the workflow&rsquo;s
returned document. It is rendered once after all steps complete, against
.input / .results / .vars, and replaces the default
{execution_id, workflow, status, input, steps[], &hellip;} response. Each leaf
is a Go-template/sprig expression; JSON structure is preserved so numbers
stay numbers and arrays stay arrays (e.g. &ldquo;{{ .results.pods.items }}&rdquo; or
&ldquo;{{ len .results.events.items }}&rdquo;). A leaf&rsquo;s type comes from the value it
evaluates to, not from how its rendered text looks: a single-action leaf
keeps its real type (a number stays a number, &ldquo;{{ len .x }}&rdquo; is a number),
and a computed string keeps its exact string form, so values whose form
matters (leading zeros, versions, IDs like &ldquo;08&rdquo; or &ldquo;1.20&rdquo;) are preserved
without any coercion or workaround. Every step result is referenceable
here regardless of its output flag. When omitted, the default response is
returned unchanged.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps">.spec.steps</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Steps defines the sequence of workflow steps defining the execution flow.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*]">.spec.steps[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowStep defines a single step in the workflow execution.
A step is exactly one of: a tool call (tool), a loop (forEach), or a
concurrent group (parallel).</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].allowFailure">.spec.steps[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error the next step is executed or not.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].args">.spec.steps[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).
Values may be any JSON type (string, integer, boolean, number, object, array)
because the schema uses x-kubernetes-preserve-unknown-fields. Templated
strings such as &ldquo;{{.input.namespace}}&rdquo; are resolved server-side at
execution time.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition">.spec.steps[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this step should execute.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.args">.spec.steps[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expect">.spec.steps[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expect.jsonPath">.spec.steps[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expect.success">.spec.steps[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expectNot">.spec.steps[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expectNot.jsonPath">.spec.steps[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.expectNot.success">.spec.steps[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.fromStep">.spec.steps[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.template">.spec.steps[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].condition.tool">.spec.steps[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].description">.spec.steps[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach">.spec.steps[*].forEach</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ForEach executes a body of sub-steps once per item of a list. Mutually
exclusive with tool and parallel.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.as">.spec.steps[*].forEach.as</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>As is the loop variable name made available to the body as
&ldquo;{{ .vars.<as> }}&rdquo;. Defaults to &ldquo;item&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.items">.spec.steps[*].forEach.items</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Items is a template expression that must resolve to an array, e.g.
&ldquo;{{ .input.clusters }}&rdquo;. Each element is bound to the loop variable for
the duration of one iteration.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.parallelism">.spec.steps[*].forEach.parallelism</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Parallelism is how many iterations may run at once. Unset, they run
one after another. Results, step records and the loop&rsquo;s per-iteration
records come out in item order either way.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps">.spec.steps[*].forEach.steps</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Steps is the body executed for each item.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*]">.spec.steps[*].forEach.steps[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowSubStep is a step used inside forEach bodies, parallel groups, and
onFailure handlers: a tool call or, in a forEach body only, a nested
forEach. Unlike WorkflowStep it cannot hold a parallel group, and a nested
forEach holds tool calls only, which keeps the CRD schema structural
(non-recursive).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].allowFailure">.spec.steps[*].forEach.steps[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].args">.spec.steps[*].forEach.steps[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition">.spec.steps[*].forEach.steps[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.args">.spec.steps[*].forEach.steps[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expect">.spec.steps[*].forEach.steps[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expect.jsonPath">.spec.steps[*].forEach.steps[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expect.success">.spec.steps[*].forEach.steps[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expectNot">.spec.steps[*].forEach.steps[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expectNot.jsonPath">.spec.steps[*].forEach.steps[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.expectNot.success">.spec.steps[*].forEach.steps[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.fromStep">.spec.steps[*].forEach.steps[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.template">.spec.steps[*].forEach.steps[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].condition.tool">.spec.steps[*].forEach.steps[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].description">.spec.steps[*].forEach.steps[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach">.spec.steps[*].forEach.steps[*].forEach</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ForEach makes this sub-step a nested loop, one level deep. Only valid in
a forEach body (not in parallel or onFailure); its loop variable must
differ from the outer one. Mutually exclusive with tool.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.as">.spec.steps[*].forEach.steps[*].forEach.as</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>As is the loop variable name made available to the body as
&ldquo;{{ .vars.<as> }}&rdquo;. Defaults to &ldquo;item&rdquo;; it must differ from the outer
loop&rsquo;s.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.items">.spec.steps[*].forEach.steps[*].forEach.items</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Items is a template expression that must resolve to an array, typically
a result of an earlier sub-step of the outer iteration, e.g.
&ldquo;{{ .results.clusters.items }}&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.parallelism">.spec.steps[*].forEach.steps[*].forEach.parallelism</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Parallelism is how many iterations may run at once within one outer
iteration. The calls in flight at once are at most the outer
parallelism times this one.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps">.spec.steps[*].forEach.steps[*].forEach.steps</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Steps is the body executed for each item.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*]">.spec.steps[*].forEach.steps[*].forEach.steps[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowNestedStep is a tool-call step in the body of a nested forEach.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].allowFailure">.spec.steps[*].forEach.steps[*].forEach.steps[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].args">.spec.steps[*].forEach.steps[*].forEach.steps[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.args">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-11">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect.jsonPath">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-11">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect.success">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-11">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot.jsonPath">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-11">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot.success">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.fromStep">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.template">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.tool">.spec.steps[*].forEach.steps[*].forEach.steps[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].description">.spec.steps[*].forEach.steps[*].forEach.steps[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].id">.spec.steps[*].forEach.steps[*].forEach.steps[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].jq">.spec.steps[*].forEach.steps[*].forEach.steps[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq).</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].output">.spec.steps[*].forEach.steps[*].forEach.steps[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by
later steps regardless of this flag.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate">.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes the sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.itemsField">.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.maxPages">.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.tokenArg">.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.tokenField">.spec.steps[*].forEach.steps[*].forEach.steps[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].store">.spec.steps[*].forEach.steps[*].forEach.steps[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].forEach.steps[*].tool">.spec.steps[*].forEach.steps[*].forEach.steps[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].id">.spec.steps[*].forEach.steps[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].jq">.spec.steps[*].forEach.steps[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq). On a nested forEach it reshapes the loop&rsquo;s
per-iteration records.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].output">.spec.steps[*].forEach.steps[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by later
steps regardless of this flag. When unset, the deprecated Store flag is
used as a fallback.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].paginate">.spec.steps[*].forEach.steps[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes a tool sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].paginate.itemsField">.spec.steps[*].forEach.steps[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].paginate.maxPages">.spec.steps[*].forEach.steps[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].paginate.tokenArg">.spec.steps[*].forEach.steps[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].paginate.tokenField">.spec.steps[*].forEach.steps[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].store">.spec.steps[*].forEach.steps[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].forEach.steps[*].tool">.spec.steps[*].forEach.steps[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute. Mutually exclusive
with forEach.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].id">.spec.steps[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this step within the workflow.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].jq">.spec.steps[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ is a jq program that reshapes the step&rsquo;s result before it is stored:
the tool&rsquo;s result for a tool step, the per-iteration records for a
forEach step. It sees the workflow input as $input and the loop
variables as $vars, and must yield one value.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].output">.spec.steps[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this step&rsquo;s result is included in the workflow&rsquo;s
returned document (what the caller receives). Every step result is always
referenceable by later steps via {{ .results.<id>.<field> }} regardless of
this flag; Output only controls visibility in the returned result. When
unset, the deprecated Store flag is used as a fallback.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].paginate">.spec.steps[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes a tool step follow the tool&rsquo;s next-page token and store
every page&rsquo;s items as one list. Only valid with tool.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].paginate.itemsField">.spec.steps[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].paginate.maxPages">.spec.steps[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].paginate.tokenArg">.spec.steps[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].paginate.tokenField">.spec.steps[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel">.spec.steps[*].parallel</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Parallel executes a group of sub-steps concurrently. Each sub-step
resolves its arguments from the workflow state as it was before the
group started; siblings cannot reference each other&rsquo;s results. Mutually
exclusive with tool and forEach.</p>

</div>

</div>
</div>

<div class="property depth-4">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*]">.spec.steps[*].parallel[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowSubStep is a step used inside forEach bodies, parallel groups, and
onFailure handlers: a tool call or, in a forEach body only, a nested
forEach. Unlike WorkflowStep it cannot hold a parallel group, and a nested
forEach holds tool calls only, which keeps the CRD schema structural
(non-recursive).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].allowFailure">.spec.steps[*].parallel[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].args">.spec.steps[*].parallel[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition">.spec.steps[*].parallel[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.args">.spec.steps[*].parallel[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expect">.spec.steps[*].parallel[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expect.jsonPath">.spec.steps[*].parallel[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expect.success">.spec.steps[*].parallel[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expectNot">.spec.steps[*].parallel[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expectNot.jsonPath">.spec.steps[*].parallel[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.expectNot.success">.spec.steps[*].parallel[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.fromStep">.spec.steps[*].parallel[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.template">.spec.steps[*].parallel[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].condition.tool">.spec.steps[*].parallel[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].description">.spec.steps[*].parallel[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach">.spec.steps[*].parallel[*].forEach</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ForEach makes this sub-step a nested loop, one level deep. Only valid in
a forEach body (not in parallel or onFailure); its loop variable must
differ from the outer one. Mutually exclusive with tool.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.as">.spec.steps[*].parallel[*].forEach.as</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>As is the loop variable name made available to the body as
&ldquo;{{ .vars.<as> }}&rdquo;. Defaults to &ldquo;item&rdquo;; it must differ from the outer
loop&rsquo;s.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.items">.spec.steps[*].parallel[*].forEach.items</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Items is a template expression that must resolve to an array, typically
a result of an earlier sub-step of the outer iteration, e.g.
&ldquo;{{ .results.clusters.items }}&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.parallelism">.spec.steps[*].parallel[*].forEach.parallelism</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>Parallelism is how many iterations may run at once within one outer
iteration. The calls in flight at once are at most the outer
parallelism times this one.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps">.spec.steps[*].parallel[*].forEach.steps</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Steps is the body executed for each item.</p>

</div>

</div>
</div>

<div class="property depth-7">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*]">.spec.steps[*].parallel[*].forEach.steps[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>WorkflowNestedStep is a tool-call step in the body of a nested forEach.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].allowFailure">.spec.steps[*].parallel[*].forEach.steps[*].allowFailure</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>AllowFailure defines if in case of an error execution continues.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].args">.spec.steps[*].parallel[*].forEach.steps[*].args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides arguments for the tool execution (supports templating).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition">.spec.steps[*].parallel[*].forEach.steps[*].condition</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition defines an optional condition that determines whether this sub-step should execute.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.args">.spec.steps[*].parallel[*].forEach.steps[*].condition.args</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Args provides the arguments to pass to the condition tool.
Values may be any JSON type.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expect">.spec.steps[*].parallel[*].forEach.steps[*].condition.expect</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Expect defines positive health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expect.jsonPath">.spec.steps[*].parallel[*].forEach.steps[*].condition.expect.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expect.success">.spec.steps[*].parallel[*].forEach.steps[*].condition.expect.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot">.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>ExpectNot defines negative health check expectations.</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot.jsonPath">.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot.jsonPath</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>JsonPath defines JSON path conditions to check in the result.
Values may be any JSON type (typically scalars compared to a result field).</p>

</div>

</div>
</div>

<div class="property depth-10">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot.success">.spec.steps[*].parallel[*].forEach.steps[*].condition.expectNot.success</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Success indicates whether the tool call should succeed.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.fromStep">.spec.steps[*].parallel[*].forEach.steps[*].condition.fromStep</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>FromStep specifies the step ID to reference for condition evaluation.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.template">.spec.steps[*].parallel[*].forEach.steps[*].condition.template</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Template is a boolean Go-template gate. When set, the step executes only
if the template renders to &ldquo;true&rdquo; (e.g. &ldquo;{{ eq .input.env \&ldquo;production\&rdquo; }}&ldquo;).
Mutually exclusive with Tool/FromStep; when present, Expect/ExpectNot are ignored.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].condition.tool">.spec.steps[*].parallel[*].forEach.steps[*].condition.tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for condition evaluation.
Optional when FromStep or Template is used.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].description">.spec.steps[*].parallel[*].forEach.steps[*].description</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Description provides human-readable documentation for this sub-step&rsquo;s purpose.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].id">.spec.steps[*].parallel[*].forEach.steps[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].jq">.spec.steps[*].parallel[*].forEach.steps[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq).</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].output">.spec.steps[*].parallel[*].forEach.steps[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by
later steps regardless of this flag.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].paginate">.spec.steps[*].parallel[*].forEach.steps[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes the sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].paginate.itemsField">.spec.steps[*].parallel[*].forEach.steps[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].paginate.maxPages">.spec.steps[*].parallel[*].forEach.steps[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].paginate.tokenArg">.spec.steps[*].parallel[*].forEach.steps[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-9">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].paginate.tokenField">.spec.steps[*].parallel[*].forEach.steps[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].store">.spec.steps[*].parallel[*].forEach.steps[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-8">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].forEach.steps[*].tool">.spec.steps[*].parallel[*].forEach.steps[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].id">.spec.steps[*].parallel[*].id</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>ID is the unique identifier for this sub-step.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].jq">.spec.steps[*].parallel[*].jq</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>JQ reshapes the sub-step&rsquo;s result before it is stored (see
WorkflowStep.jq). On a nested forEach it reshapes the loop&rsquo;s
per-iteration records.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].output">.spec.steps[*].parallel[*].output</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Output indicates whether this sub-step&rsquo;s result is included in the
workflow&rsquo;s returned document. The result is always referenceable by later
steps regardless of this flag. When unset, the deprecated Store flag is
used as a fallback.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].paginate">.spec.steps[*].parallel[*].paginate</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Paginate makes a tool sub-step follow the tool&rsquo;s pages (see
WorkflowStep.paginate).</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].paginate.itemsField">.spec.steps[*].parallel[*].paginate.itemsField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>ItemsField is where a page&rsquo;s list is. Defaults to &ldquo;items&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].paginate.maxPages">.spec.steps[*].parallel[*].paginate.maxPages</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>MaxPages bounds the pages fetched. Defaults to 10.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].paginate.tokenArg">.spec.steps[*].parallel[*].paginate.tokenArg</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenArg is the tool argument the token is passed in. Defaults to
&ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-6">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].paginate.tokenField">.spec.steps[*].parallel[*].paginate.tokenField</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>TokenField is where a page&rsquo;s next-page token is. Defaults to &ldquo;continue&rdquo;.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].store">.spec.steps[*].parallel[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output, kept for backwards compatibility.
Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-5">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].parallel[*].tool">.spec.steps[*].parallel[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute. Mutually exclusive
with forEach.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].store">.spec.steps[*].store</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Store is a deprecated alias for Output. It originally also controlled
whether a step result was referenceable by later steps, but referencing
is now always available; Store now only affects result visibility and is
kept for backwards compatibility. Prefer Output.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.spec.steps[*].tool">.spec.steps[*].tool</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

<div class="property-description">
<p>Tool specifies the name of the tool to execute for this step.
Mutually exclusive with forEach and parallel.</p>

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
<p>WorkflowStatus defines the observed state of Workflow</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions">.status.conditions</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>Conditions represent the latest available observations of the workflow&rsquo;s state.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*]">.status.conditions[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">object</span>

</div>

<div class="property-description">
<p>Condition contains details for one aspect of the current state of this API Resource.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].lastTransitionTime">.status.conditions[*].lastTransitionTime</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>lastTransitionTime is the last time the condition transitioned from one status to another.
This should be when the underlying condition changed.  If that is not known, then using the time when the API field changed is acceptable.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].message">.status.conditions[*].message</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>message is a human readable message indicating details about the transition.
This may be an empty string.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].observedGeneration">.status.conditions[*].observedGeneration</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>observedGeneration represents the .metadata.generation that the condition was set based upon.
For instance, if .metadata.generation is currently 12, but the .status.conditions[x].observedGeneration is 9, the condition is out of date
with respect to the current state of the instance.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].reason">.status.conditions[*].reason</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>reason contains a programmatic identifier indicating the reason for the condition&rsquo;s last transition.
Producers of specific condition types may define expected values and meanings for this field,
and whether the values are considered a guaranteed API.
The value should be a CamelCase string.
This field may not be empty.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].status">.status.conditions[*].status</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>status of the condition, one of True, False, Unknown.</p>

</div>

</div>
</div>

<div class="property depth-3">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.conditions[*].type">.status.conditions[*].type</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>
<span class="property-required">Required</span>
</div>

<div class="property-description">
<p>type of condition in CamelCase or in foo.example.com/CamelCase.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.referencedTools">.status.referencedTools</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ReferencedTools lists all tools mentioned in the Workflow steps.
This is informational only; actual availability depends on the user&rsquo;s session.
See ADR 007 for details on session-scoped tool visibility.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.referencedTools[*]">.status.referencedTools[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.stepCount">.status.stepCount</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">integer</span>

</div>

<div class="property-description">
<p>StepCount is the number of steps in the workflow.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.valid">.status.valid</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">boolean</span>

</div>

<div class="property-description">
<p>Valid indicates whether the Workflow spec passes structural validation.</p>

</div>

</div>
</div>

<div class="property depth-1">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.validationErrors">.status.validationErrors</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">array</span>

</div>

<div class="property-description">
<p>ValidationErrors contains any spec validation error messages.</p>

</div>

</div>
</div>

<div class="property depth-2">
<div class="property-header">
<h3 class="property-path" id="v1alpha1-.status.validationErrors[*]">.status.validationErrors[*]</h3>
</div>
<div class="property-body">
<div class="property-meta">
<span class="property-type">string</span>

</div>

</div>
</div>





</div>



