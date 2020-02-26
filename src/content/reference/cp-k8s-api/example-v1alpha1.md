---
title: example.giantswarm.io/v1alpha1
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#example.giantswarm.io%2fv1alpha1">example.giantswarm.io/v1alpha1</a>
</li>
</ul>
<h2 id="example.giantswarm.io/v1alpha1">example.giantswarm.io/v1alpha1</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#example.giantswarm.io/v1alpha1.MemcachedConfig">MemcachedConfig</a>
</li></ul>
<h3 id="example.giantswarm.io/v1alpha1.MemcachedConfig">MemcachedConfig
</h3>
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
<code>apiVersion</code></br>
string</td>
<td>
<code>
example.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>MemcachedConfig</code></td>
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
<a href="#example.giantswarm.io/v1alpha1.MemcachedConfigSpec">
MemcachedConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>replicas</code></br>
<em>
int
</em>
</td>
<td>
<p>Replicas is the number of instances of Memcache.</p>
</td>
</tr>
<tr>
<td>
<code>memory</code></br>
<em>
string
</em>
</td>
<td>
<p>e.g. 3
Memory is how much RAM to use for item storage.
e.g. 4G</p>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="example.giantswarm.io/v1alpha1.MemcachedConfigSpec">MemcachedConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#example.giantswarm.io/v1alpha1.MemcachedConfig">MemcachedConfig</a>)
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
<code>replicas</code></br>
<em>
int
</em>
</td>
<td>
<p>Replicas is the number of instances of Memcache.</p>
</td>
</tr>
<tr>
<td>
<code>memory</code></br>
<em>
string
</em>
</td>
<td>
<p>e.g. 3
Memory is how much RAM to use for item storage.
e.g. 4G</p>
</td>
</tr>
</tbody>
</table>
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
