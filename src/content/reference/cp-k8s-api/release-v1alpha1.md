---
title: release.giantswarm.io/v1alpha1
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#release.giantswarm.io%2fv1alpha1">release.giantswarm.io/v1alpha1</a>
</li>
</ul>
<h2 id="release.giantswarm.io/v1alpha1">release.giantswarm.io/v1alpha1</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#release.giantswarm.io/v1alpha1.Release">Release</a>
</li><li>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycle">ReleaseCycle</a>
</li></ul>
<h3 id="release.giantswarm.io/v1alpha1.Release">Release
</h3>
<p>
<p>Release CRs might look something like the following.</p>
<pre><code>apiVersion: &quot;release.giantswarm.io/v1alpha1&quot;
kind: &quot;Release&quot;
metadata:
name: &quot;aws.v6.1.0&quot;
labels:
giantswarm.io/managed-by: &quot;app-operator&quot;
giantswarm.io/provider: &quot;aws&quot;
spec:
changelog:
- component: &quot;cloudconfig&quot;
description: &quot;Replace cloudinit with ignition.&quot;
kind: &quot;changed&quot;
components:
- name: &quot;aws-operator&quot;
version: &quot;4.6.0&quot;
- name: &quot;cert-operator&quot;
version: &quot;0.1.0&quot;
- name: &quot;chart-operator&quot;
version: &quot;0.5.0&quot;
- name: &quot;cluster-operator&quot;
version: &quot;0.10.0&quot;
parentVersion: &quot;6.0.1&quot;
version: &quot;6.1.0&quot;
status:
cycle:
phase: &quot;eol&quot;
enabledDate: 2019-01-08
disabledDate: 2019-01-12
</code></pre>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>apiVersion</code></br>
string</td>
<td>
<code>
release.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>Release</code></td>
</tr>
<tr>
<td>
<code>metadata</code></br>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#objectmeta-v1-meta">
Kubernetes meta/v1.ObjectMeta
</a>
</em>
</td>
<td>
Refer to the Kubernetes API documentation for the fields of the
<code>metadata</code> field.
</td>
</tr>
<tr>
<td>
<code>spec</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpec">
ReleaseSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>changelog</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpecChangelogEntry">
[]ReleaseSpecChangelogEntry
</a>
</em>
</td>
<td>
<p>Changelog is the changelog since ParentVersion.</p>
</td>
</tr>
<tr>
<td>
<code>components</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpecComponent">
[]ReleaseSpecComponent
</a>
</em>
</td>
<td>
<p>Components describes components managing this release.</p>
</td>
</tr>
<tr>
<td>
<code>parentVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>ParentVersion is a version from which the changes in changelog are
described. We need that because we may introduce bug fixes after
next major release and then taking previous semver version may not
render correct changelog. This should always be in the semver format
without the &ldquo;v&rdquo; prefix.</p>
</td>
</tr>
<tr>
<td>
<code>version</code></br>
<em>
string
</em>
</td>
<td>
<p>Version is the version of the release. Releases with semver version
(without the &ldquo;v&rdquo; prefix) are taken from control-plane AppCatalog.
All other releases are taken from control-plane-test AppCatalog.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseStatus">
ReleaseStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseCycle">ReleaseCycle
</h3>
<p>
<p>ReleaseCycle CRs might look something like the following.</p>
<pre><code>apiVersion: &quot;release.giantswarm.io/v1alpha1&quot;
kind: &quot;ReleaseCycle&quot;
metadata:
name: &quot;aws.v6.1.0&quot;
labels:
giantswarm.io/managed-by: &quot;opsctl&quot;
giantswarm.io/provider: &quot;aws&quot;
spec:
disabledDate: 2019-01-12
enabledDate: 2019-01-08
phase: &quot;enabled&quot;
</code></pre>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>apiVersion</code></br>
string</td>
<td>
<code>
release.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>ReleaseCycle</code></td>
</tr>
<tr>
<td>
<code>metadata</code></br>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#objectmeta-v1-meta">
Kubernetes meta/v1.ObjectMeta
</a>
</em>
</td>
<td>
Refer to the Kubernetes API documentation for the fields of the
<code>metadata</code> field.
</td>
</tr>
<tr>
<td>
<code>spec</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycleSpec">
ReleaseCycleSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>disabledDate</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.DeepCopyDate">
DeepCopyDate
</a>
</em>
</td>
<td>
<p>DisabledDate is the date of the cycle phase being changed to &ldquo;disabled&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>enabledDate</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.DeepCopyDate">
DeepCopyDate
</a>
</em>
</td>
<td>
<p>EnabledDate is the date of the cycle phase being changed to &ldquo;enabled&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>phase</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCyclePhase">
ReleaseCyclePhase
</a>
</em>
</td>
<td>
<p>Phase is the release phase. It can be one of: &ldquo;upcoming&rdquo;, &ldquo;enabled&rdquo;,
&ldquo;disabled&rdquo;, &ldquo;eol&rdquo;.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycleStatus">
ReleaseCycleStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.DeepCopyDate">DeepCopyDate
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycleSpec">ReleaseCycleSpec</a>)
</p>
<p>
<p>DeepCopyDate is a date type designed to be validated with json-schema date
type.</p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>Time</code></br>
<em>
time.Time
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseChangelogKind">ReleaseChangelogKind
(<code>string</code> alias)</p></h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpecChangelogEntry">ReleaseSpecChangelogEntry</a>)
</p>
<p>
</p>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseCyclePhase">ReleaseCyclePhase
(<code>string</code> alias)</p></h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycleSpec">ReleaseCycleSpec</a>)
</p>
<p>
</p>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseCycleSpec">ReleaseCycleSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycle">ReleaseCycle</a>, 
<a href="#release.giantswarm.io/v1alpha1.ReleaseStatus">ReleaseStatus</a>)
</p>
<p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>disabledDate</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.DeepCopyDate">
DeepCopyDate
</a>
</em>
</td>
<td>
<p>DisabledDate is the date of the cycle phase being changed to &ldquo;disabled&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>enabledDate</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.DeepCopyDate">
DeepCopyDate
</a>
</em>
</td>
<td>
<p>EnabledDate is the date of the cycle phase being changed to &ldquo;enabled&rdquo;.</p>
</td>
</tr>
<tr>
<td>
<code>phase</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCyclePhase">
ReleaseCyclePhase
</a>
</em>
</td>
<td>
<p>Phase is the release phase. It can be one of: &ldquo;upcoming&rdquo;, &ldquo;enabled&rdquo;,
&ldquo;disabled&rdquo;, &ldquo;eol&rdquo;.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseCycleStatus">ReleaseCycleStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycle">ReleaseCycle</a>)
</p>
<p>
</p>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseSpec">ReleaseSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.Release">Release</a>)
</p>
<p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>changelog</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpecChangelogEntry">
[]ReleaseSpecChangelogEntry
</a>
</em>
</td>
<td>
<p>Changelog is the changelog since ParentVersion.</p>
</td>
</tr>
<tr>
<td>
<code>components</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpecComponent">
[]ReleaseSpecComponent
</a>
</em>
</td>
<td>
<p>Components describes components managing this release.</p>
</td>
</tr>
<tr>
<td>
<code>parentVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>ParentVersion is a version from which the changes in changelog are
described. We need that because we may introduce bug fixes after
next major release and then taking previous semver version may not
render correct changelog. This should always be in the semver format
without the &ldquo;v&rdquo; prefix.</p>
</td>
</tr>
<tr>
<td>
<code>version</code></br>
<em>
string
</em>
</td>
<td>
<p>Version is the version of the release. Releases with semver version
(without the &ldquo;v&rdquo; prefix) are taken from control-plane AppCatalog.
All other releases are taken from control-plane-test AppCatalog.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseSpecChangelogEntry">ReleaseSpecChangelogEntry
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpec">ReleaseSpec</a>)
</p>
<p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>component</code></br>
<em>
string
</em>
</td>
<td>
<p>Component name.</p>
</td>
</tr>
<tr>
<td>
<code>description</code></br>
<em>
string
</em>
</td>
<td>
<p>Description of the component changes expressed in full sentence.</p>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseChangelogKind">
ReleaseChangelogKind
</a>
</em>
</td>
<td>
<p>Kind of the component changes. It can be one of: &ldquo;added&rdquo;, &ldquo;changed&rdquo;,
&ldquo;deprecated&rdquo;, &ldquo;fixed&rdquo;, &ldquo;removed&rdquo;, &ldquo;security&rdquo;.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseSpecChangelogEntryKind">ReleaseSpecChangelogEntryKind
(<code>string</code> alias)</p></h3>
<p>
</p>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseSpecComponent">ReleaseSpecComponent
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseSpec">ReleaseSpec</a>)
</p>
<p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>name</code></br>
<em>
string
</em>
</td>
<td>
<p>Name of the release component.</p>
</td>
</tr>
<tr>
<td>
<code>version</code></br>
<em>
string
</em>
</td>
<td>
<p>Version of the release component.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="release.giantswarm.io/v1alpha1.ReleaseStatus">ReleaseStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#release.giantswarm.io/v1alpha1.Release">Release</a>)
</p>
<p>
</p>
<table>
<thead>
<tr>
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<code>cycle</code></br>
<em>
<a href="#release.giantswarm.io/v1alpha1.ReleaseCycleSpec">
ReleaseCycleSpec
</a>
</em>
</td>
<td>
<p>Cycle is the most recent observed copy of the specification of the
ReleaseCycle CR referencing this Release CR.</p>
</td>
</tr>
</tbody>
</table>
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
