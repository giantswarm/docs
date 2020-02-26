---
title: core.giantswarm.io/v1alpha1
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#core.giantswarm.io%2fv1alpha1">core.giantswarm.io/v1alpha1</a>
</li>
</ul>
<h2 id="core.giantswarm.io/v1alpha1">core.giantswarm.io/v1alpha1</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfig">AWSClusterConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfig">AzureClusterConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.CertConfig">CertConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.ChartConfig">ChartConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.Cluster">Cluster</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfig">DrainerConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfig">DraughtsmanConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfig">FlannelConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.IngressConfig">IngressConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfig">KVMClusterConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.NodeConfig">NodeConfig</a>
</li><li>
<a href="#core.giantswarm.io/v1alpha1.StorageConfig">StorageConfig</a>
</li></ul>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfig">AWSClusterConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AWSClusterConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpec">
AWSClusterConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">
AWSClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecVersionBundle">
AWSClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfig">AzureClusterConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AzureClusterConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpec">
AzureClusterConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">
AzureClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecVersionBundle">
AzureClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.CertConfig">CertConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>CertConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpec">
CertConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>cert</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpecCert">
CertConfigSpecCert
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpecVersionBundle">
CertConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfig">ChartConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>ChartConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpec">
ChartConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>chart</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecChart">
ChartConfigSpecChart
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecVersionBundle">
ChartConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigStatus">
ChartConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.Cluster">Cluster
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>Cluster</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.ClusterSpec">
ClusterSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>description</code></br>
<em>
string
</em>
</td>
<td>
<p>Description is the optional cluster description users can provide. If left
blank a cluster description will be generated. The cluster description is
propagated into the CR status.</p>
</td>
</tr>
<tr>
<td>
<code>organization</code></br>
<em>
string
</em>
</td>
<td>
<p>Organization is the mandatory cluster organization in which a tenant
cluster will be scoped into.</p>
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
<p>Version is the optional release version users can provide. If left blank
the current default release version will be used. The release version is
propagated into the CR status.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatus">
ClusterStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfig">DrainerConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>DrainerConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpec">
DrainerConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuest">
DrainerConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecVersionBundle">
DrainerConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigStatus">
DrainerConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DraughtsmanConfig">DraughtsmanConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>DraughtsmanConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfigSpec">
DraughtsmanConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>projects</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfigSpecProject">
[]DraughtsmanConfigSpecProject
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfig">FlannelConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>FlannelConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">
FlannelConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>bridge</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridge">
FlannelConfigSpecBridge
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecCluster">
FlannelConfigSpecCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>flannel</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannel">
FlannelConfigSpecFlannel
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>health</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecHealth">
FlannelConfigSpecHealth
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecVersionBundle">
FlannelConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfig">IngressConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>IngressConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpec">
IngressConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>guestCluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecGuestCluster">
IngressConfigSpecGuestCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>hostCluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecHostCluster">
IngressConfigSpecHostCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>protocolPorts</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecProtocolPort">
[]IngressConfigSpecProtocolPort
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecVersionBundle">
IngressConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfig">KVMClusterConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>KVMClusterConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpec">
KVMClusterConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">
KVMClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecVersionBundle">
KVMClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.NodeConfig">NodeConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>NodeConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.NodeConfigSpec">
NodeConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.NodeConfigStatus">
NodeConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.StorageConfig">StorageConfig
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
core.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>StorageConfig</code></td>
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
<a href="#core.giantswarm.io/v1alpha1.StorageConfigSpec">
StorageConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>storage</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.StorageConfigSpecStorage">
StorageConfigSpecStorage
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpec">AWSClusterConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfig">AWSClusterConfig</a>)
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
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">
AWSClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecVersionBundle">
AWSClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">AWSClusterConfigSpecGuest
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpec">AWSClusterConfigSpec</a>)
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
<code>ClusterGuestConfig</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterGuestConfig">
ClusterGuestConfig
</a>
</em>
</td>
<td>
<p>
(Members of <code>ClusterGuestConfig</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>credentialSecret</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestCredentialSecret">
AWSClusterConfigSpecGuestCredentialSecret
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>masters</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestMaster">
[]AWSClusterConfigSpecGuestMaster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>workers</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestWorker">
[]AWSClusterConfigSpecGuestWorker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestCredentialSecret">AWSClusterConfigSpecGuestCredentialSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">AWSClusterConfigSpecGuest</a>)
</p>
<p>
<p>AWSClusterConfigSpecGuestCredentialSecret points to the K8s Secret
containing credentials for an AWS account in which the guest cluster should
be created.</p>
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
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestMaster">AWSClusterConfigSpecGuestMaster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">AWSClusterConfigSpecGuest</a>)
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
<code>AWSClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestNode">
AWSClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>AWSClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestNode">AWSClusterConfigSpecGuestNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestMaster">AWSClusterConfigSpecGuestMaster</a>, 
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestWorker">AWSClusterConfigSpecGuestWorker</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>instanceType</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestWorker">AWSClusterConfigSpecGuestWorker
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">AWSClusterConfigSpecGuest</a>)
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
<code>AWSClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuestNode">
AWSClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>AWSClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>labels</code></br>
<em>
map[string]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AWSClusterConfigSpecVersionBundle">AWSClusterConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpec">AWSClusterConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpec">AzureClusterConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfig">AzureClusterConfig</a>)
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
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">
AzureClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecVersionBundle">
AzureClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">AzureClusterConfigSpecGuest
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpec">AzureClusterConfigSpec</a>)
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
<code>ClusterGuestConfig</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterGuestConfig">
ClusterGuestConfig
</a>
</em>
</td>
<td>
<p>
(Members of <code>ClusterGuestConfig</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>credentialSecret</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestCredentialSecret">
AzureClusterConfigSpecGuestCredentialSecret
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>masters</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestMaster">
[]AzureClusterConfigSpecGuestMaster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>workers</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestWorker">
[]AzureClusterConfigSpecGuestWorker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestCredentialSecret">AzureClusterConfigSpecGuestCredentialSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">AzureClusterConfigSpecGuest</a>)
</p>
<p>
<p>AzureClusterConfigSpecGuestCredentialSecret points to the K8s Secret
containing credentials for an Azure subscription in which the tenant cluster
should be created.</p>
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
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestMaster">AzureClusterConfigSpecGuestMaster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">AzureClusterConfigSpecGuest</a>)
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
<code>AzureClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestNode">
AzureClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>AzureClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestNode">AzureClusterConfigSpecGuestNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestMaster">AzureClusterConfigSpecGuestMaster</a>, 
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestWorker">AzureClusterConfigSpecGuestWorker</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>vmSize</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestWorker">AzureClusterConfigSpecGuestWorker
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">AzureClusterConfigSpecGuest</a>)
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
<code>AzureClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuestNode">
AzureClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>AzureClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>labels</code></br>
<em>
map[string]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.AzureClusterConfigSpecVersionBundle">AzureClusterConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpec">AzureClusterConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.CertConfigSpec">CertConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.CertConfig">CertConfig</a>)
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
<code>cert</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpecCert">
CertConfigSpecCert
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpecVersionBundle">
CertConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.CertConfigSpecCert">CertConfigSpecCert
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpec">CertConfigSpec</a>)
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
<code>allowBareDomains</code></br>
<em>
bool
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>altNames</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>clusterComponent</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>clusterID</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>commonName</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>disableRegeneration</code></br>
<em>
bool
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ipSans</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>organizations</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ttl</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.CertConfigSpecVersionBundle">CertConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.CertConfigSpec">CertConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigSpec">ChartConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfig">ChartConfig</a>)
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
<code>chart</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecChart">
ChartConfigSpecChart
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecVersionBundle">
ChartConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigSpecChart">ChartConfigSpecChart
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpec">ChartConfigSpec</a>)
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
<code>channel</code></br>
<em>
string
</em>
</td>
<td>
<p>Channel is the name of the Appr channel to reconcile against,
e.g. 1-0-stable.</p>
</td>
</tr>
<tr>
<td>
<code>configMap</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecConfigMap">
ChartConfigSpecConfigMap
</a>
</em>
</td>
<td>
<p>ConfigMap references a config map containing values that should be
applied to the chart.</p>
</td>
</tr>
<tr>
<td>
<code>userConfigMap</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecConfigMap">
ChartConfigSpecConfigMap
</a>
</em>
</td>
<td>
<p>UserConfigMap references a config map containing custom values.
These custom values are specified by the user to override default values.</p>
</td>
</tr>
<tr>
<td>
<code>name</code></br>
<em>
string
</em>
</td>
<td>
<p>Name is the name of the Helm chart to deploy,
e.g. kubernetes-node-exporter.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
<p>Namespace is the namespace where the Helm chart is to be deployed,
e.g. giantswarm.</p>
</td>
</tr>
<tr>
<td>
<code>release</code></br>
<em>
string
</em>
</td>
<td>
<p>Release is the name of the Helm release when the chart is deployed,
e.g. node-exporter.</p>
</td>
</tr>
<tr>
<td>
<code>secret</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecSecret">
ChartConfigSpecSecret
</a>
</em>
</td>
<td>
<p>Secret references a secret containing secret values that should be
applied to the chart.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigSpecConfigMap">ChartConfigSpecConfigMap
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecChart">ChartConfigSpecChart</a>)
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
<p>Name is the name of the config map containing chart values to apply,
e.g. node-exporter-chart-values.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
<p>Namespace is the namespace of the values config map,
e.g. kube-system.</p>
</td>
</tr>
<tr>
<td>
<code>resourceVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>ResourceVersion is the Kubernetes resource version of the configmap.
Used to detect if the configmap has changed, e.g. 12345.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigSpecSecret">ChartConfigSpecSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpecChart">ChartConfigSpecChart</a>)
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
<p>Name is the name of the secret containing chart values to apply,
e.g. node-exporter-chart-secret.</p>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
<p>Namespace is the namespace of the secret,
e.g. kube-system.</p>
</td>
</tr>
<tr>
<td>
<code>resourceVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>ResourceVersion is the Kubernetes resource version of the secret.
Used to detect if the secret has changed, e.g. 12345.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigSpecVersionBundle">ChartConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfigSpec">ChartConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ChartConfigStatus">ChartConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ChartConfig">ChartConfig</a>)
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
<code>releaseStatus</code></br>
<em>
string
</em>
</td>
<td>
<p>ReleaseStatus is the status of the Helm release when the chart is
installed, e.g. DEPLOYED.</p>
</td>
</tr>
<tr>
<td>
<code>reason</code></br>
<em>
string
</em>
</td>
<td>
<p>Reason is the description of the last status of helm release when the chart is
not installed successfully, e.g. deploy resource already exists.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterGuestConfig">ClusterGuestConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.AWSClusterConfigSpecGuest">AWSClusterConfigSpecGuest</a>, 
<a href="#core.giantswarm.io/v1alpha1.AzureClusterConfigSpecGuest">AzureClusterConfigSpecGuest</a>, 
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">KVMClusterConfigSpecGuest</a>)
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
<code>availabilityZones</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>dnsZone</code></br>
<em>
string
</em>
</td>
<td>
<p>DNSZone for guest cluster is supplemented with host prefixes for
specific services such as Kubernetes API or Etcd. In general this DNS
Zone should start with <code>k8s</code> like for example
<code>k8s.cluster.example.com.</code>.</p>
</td>
</tr>
<tr>
<td>
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>name</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>owner</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>releaseVersion</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundles</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterGuestConfigVersionBundle">
[]ClusterGuestConfigVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterGuestConfigVersionBundle">ClusterGuestConfigVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ClusterGuestConfig">ClusterGuestConfig</a>)
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
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterSpec">ClusterSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
</p>
<p>
<p>ClusterSpec is the part of the interface available to users in order to
request a tenant cluster creation by providing necessary configurations.
Fields here are either mandatory or optional. Optional fields left blank will
be filled with appropriate default values which are then propagated into the
CR status.</p>
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
<code>description</code></br>
<em>
string
</em>
</td>
<td>
<p>Description is the optional cluster description users can provide. If left
blank a cluster description will be generated. The cluster description is
propagated into the CR status.</p>
</td>
</tr>
<tr>
<td>
<code>organization</code></br>
<em>
string
</em>
</td>
<td>
<p>Organization is the mandatory cluster organization in which a tenant
cluster will be scoped into.</p>
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
<p>Version is the optional release version users can provide. If left blank
the current default release version will be used. The release version is
propagated into the CR status.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterStatus">ClusterStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
</p>
<p>
<p>ClusterStatus is the part of the interface available to users in order to
fetch a tenant cluster&rsquo;s status information after creation was requested.
Fields here are automatically filled and can only ever be read. For instance
the tenant cluster description will be generated if left blank upon cluster
creation and made available here.</p>
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
<code>lastHeartbeatTime</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastHeartbeatTime is the last time we got an update on a given condition.</p>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastTransitionTime is the last time the condition transitioned from one
status to another.</p>
</td>
</tr>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatusCluster">
ClusterStatusCluster
</a>
</em>
</td>
<td>
<p>Cluster holds cluster specific status information.</p>
</td>
</tr>
<tr>
<td>
<code>conditions</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatusCondition">
[]ClusterStatusCondition
</a>
</em>
</td>
<td>
<p>Conditions is a list of status conditions.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterStatusCluster">ClusterStatusCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatus">ClusterStatus</a>)
</p>
<p>
<p>ClusterStatusCluster holds cluster specific status information. Some of the
fields from this structure may move back to the spec in the future once we
make more use of mutating admission controllers for defaulting reasons. For
instance the cluster ID and version are candidates for this.</p>
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
<code>description</code></br>
<em>
string
</em>
</td>
<td>
<p>Description is the propagated cluster description users can provide or the
system generates automatically if left blank.</p>
</td>
</tr>
<tr>
<td>
<code>id</code></br>
<em>
string
</em>
</td>
<td>
<p>ID is the internal cluster ID automatically generated upon cluster
creation.</p>
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
<p>Version is the propagated release version users can provide or the system
sets to the current default release version.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.ClusterStatusCondition">ClusterStatusCondition
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatus">ClusterStatus</a>)
</p>
<p>
<p>ClusterStatusCondition holds a specific status condition describing certain
aspects of the current state of the tenant cluster.</p>
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
<code>status</code></br>
<em>
string
</em>
</td>
<td>
<p>Status may be True, False or Unknown.</p>
</td>
</tr>
<tr>
<td>
<code>type</code></br>
<em>
string
</em>
</td>
<td>
<p>Type may be Creating, Created, Updating, Updated, or Deleting.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DeepCopyTime">DeepCopyTime
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.ClusterStatus">ClusterStatus</a>, 
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigStatusCondition">DrainerConfigStatusCondition</a>)
</p>
<p>
<p>DeepCopyTime implements the deep copy logic for time.Time which the k8s
codegen is not able to generate out of the box.</p>
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
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpec">DrainerConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfig">DrainerConfig</a>)
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
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuest">
DrainerConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecVersionBundle">
DrainerConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpecGuest">DrainerConfigSpecGuest
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpec">DrainerConfigSpec</a>)
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
<code>cluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestCluster">
DrainerConfigSpecGuestCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>node</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestNode">
DrainerConfigSpecGuestNode
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestCluster">DrainerConfigSpecGuestCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuest">DrainerConfigSpecGuest</a>)
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
<code>api</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestClusterAPI">
DrainerConfigSpecGuestClusterAPI
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>id</code></br>
<em>
string
</em>
</td>
<td>
<p>ID is the guest cluster ID of which a node should be drained.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestClusterAPI">DrainerConfigSpecGuestClusterAPI
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestCluster">DrainerConfigSpecGuestCluster</a>)
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
<code>endpoint</code></br>
<em>
string
</em>
</td>
<td>
<p>Endpoint is the guest cluster API endpoint.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpecGuestNode">DrainerConfigSpecGuestNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpecGuest">DrainerConfigSpecGuest</a>)
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
<p>Name is the identifier of the guest cluster&rsquo;s master and worker nodes. In
Kubernetes/Kubectl they are represented as node names. The names are manage
in an abstracted way because of provider specific differences.</p>
<pre><code>AWS: EC2 instance DNS.
Azure: VM name.
KVM: host cluster pod name.
</code></pre>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigSpecVersionBundle">DrainerConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigSpec">DrainerConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigStatus">DrainerConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfig">DrainerConfig</a>)
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
<code>conditions</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigStatusCondition">
[]DrainerConfigStatusCondition
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DrainerConfigStatusCondition">DrainerConfigStatusCondition
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DrainerConfigStatus">DrainerConfigStatus</a>)
</p>
<p>
<p>DrainerConfigStatusCondition expresses a condition in which a node may is.</p>
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
<code>lastHeartbeatTime</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastHeartbeatTime is the last time we got an update on a given condition.</p>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastTransitionTime is the last time the condition transitioned from one
status to another.</p>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
string
</em>
</td>
<td>
<p>Status may be True, False or Unknown.</p>
</td>
</tr>
<tr>
<td>
<code>type</code></br>
<em>
string
</em>
</td>
<td>
<p>Type may be Pending, Ready, Draining, Drained.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DraughtsmanConfigSpec">DraughtsmanConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfig">DraughtsmanConfig</a>)
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
<code>projects</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfigSpecProject">
[]DraughtsmanConfigSpecProject
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.DraughtsmanConfigSpecProject">DraughtsmanConfigSpecProject
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.DraughtsmanConfigSpec">DraughtsmanConfigSpec</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>name</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ref</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfig">FlannelConfig</a>)
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
<code>bridge</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridge">
FlannelConfigSpecBridge
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecCluster">
FlannelConfigSpecCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>flannel</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannel">
FlannelConfigSpecFlannel
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>health</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecHealth">
FlannelConfigSpecHealth
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecVersionBundle">
FlannelConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecBridge">FlannelConfigSpecBridge
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec</a>)
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
<code>docker</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeDocker">
FlannelConfigSpecBridgeDocker
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>spec</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpec">
FlannelConfigSpecBridgeSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>interface</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>privateNetwork</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>dns</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecDNS">
FlannelConfigSpecBridgeSpecDNS
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ntp</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecNTP">
FlannelConfigSpecBridgeSpecNTP
</a>
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeDocker">FlannelConfigSpecBridgeDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridge">FlannelConfigSpecBridge</a>)
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
<code>image</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpec">FlannelConfigSpecBridgeSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridge">FlannelConfigSpecBridge</a>)
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
<code>interface</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>privateNetwork</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>dns</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecDNS">
FlannelConfigSpecBridgeSpecDNS
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ntp</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecNTP">
FlannelConfigSpecBridgeSpecNTP
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecDNS">FlannelConfigSpecBridgeSpecDNS
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpec">FlannelConfigSpecBridgeSpec</a>)
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
<code>servers</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpecNTP">FlannelConfigSpecBridgeSpecNTP
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecBridgeSpec">FlannelConfigSpecBridgeSpec</a>)
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
<code>servers</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecCluster">FlannelConfigSpecCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>customer</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannel">FlannelConfigSpecFlannel
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec</a>)
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
<code>spec</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannelSpec">
FlannelConfigSpecFlannelSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>network</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>subnetLen</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>runDir</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>vni</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannelSpec">FlannelConfigSpecFlannelSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecFlannel">FlannelConfigSpecFlannel</a>)
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
<code>network</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>subnetLen</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>runDir</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>vni</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecHealth">FlannelConfigSpecHealth
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec</a>)
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
<code>docker</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecHealthDocker">
FlannelConfigSpecHealthDocker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecHealthDocker">FlannelConfigSpecHealthDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpecHealth">FlannelConfigSpecHealth</a>)
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
<code>image</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.FlannelConfigSpecVersionBundle">FlannelConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.FlannelConfigSpec">FlannelConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpec">IngressConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfig">IngressConfig</a>)
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
<code>guestCluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecGuestCluster">
IngressConfigSpecGuestCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>hostCluster</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecHostCluster">
IngressConfigSpecHostCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>protocolPorts</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecProtocolPort">
[]IngressConfigSpecProtocolPort
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecVersionBundle">
IngressConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpecGuestCluster">IngressConfigSpecGuestCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpec">IngressConfigSpec</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>service</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpecHostCluster">IngressConfigSpecHostCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpec">IngressConfigSpec</a>)
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
<code>ingressController</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecHostClusterIngressController">
IngressConfigSpecHostClusterIngressController
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpecHostClusterIngressController">IngressConfigSpecHostClusterIngressController
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpecHostCluster">IngressConfigSpecHostCluster</a>)
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
<code>configMap</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>namespace</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>service</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpecProtocolPort">IngressConfigSpecProtocolPort
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpec">IngressConfigSpec</a>)
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
<code>ingressPort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>lbPort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>protocol</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.IngressConfigSpecVersionBundle">IngressConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.IngressConfigSpec">IngressConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpec">KVMClusterConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfig">KVMClusterConfig</a>)
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
<code>guest</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">
KVMClusterConfigSpecGuest
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versionBundle</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecVersionBundle">
KVMClusterConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">KVMClusterConfigSpecGuest
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpec">KVMClusterConfigSpec</a>)
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
<code>ClusterGuestConfig</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.ClusterGuestConfig">
ClusterGuestConfig
</a>
</em>
</td>
<td>
<p>
(Members of <code>ClusterGuestConfig</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>masters</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestMaster">
[]KVMClusterConfigSpecGuestMaster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>workers</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestWorker">
[]KVMClusterConfigSpecGuestWorker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestMaster">KVMClusterConfigSpecGuestMaster
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">KVMClusterConfigSpecGuest</a>)
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
<code>KVMClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestNode">
KVMClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>KVMClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestNode">KVMClusterConfigSpecGuestNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestMaster">KVMClusterConfigSpecGuestMaster</a>, 
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestWorker">KVMClusterConfigSpecGuestWorker</a>)
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
<code>id</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>cpuCores</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>memorySizeGB</code></br>
<em>
float64
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>storageSizeGB</code></br>
<em>
float64
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestWorker">KVMClusterConfigSpecGuestWorker
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuest">KVMClusterConfigSpecGuest</a>)
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
<code>KVMClusterConfigSpecGuestNode</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpecGuestNode">
KVMClusterConfigSpecGuestNode
</a>
</em>
</td>
<td>
<p>
(Members of <code>KVMClusterConfigSpecGuestNode</code> are embedded into this type.)
</p>
</td>
</tr>
<tr>
<td>
<code>labels</code></br>
<em>
map[string]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.KVMClusterConfigSpecVersionBundle">KVMClusterConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.KVMClusterConfigSpec">KVMClusterConfigSpec</a>)
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
<code>version</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.NodeConfigSpec">NodeConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.NodeConfig">NodeConfig</a>)
</p>
<p>
</p>
<h3 id="core.giantswarm.io/v1alpha1.NodeConfigStatus">NodeConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.NodeConfig">NodeConfig</a>)
</p>
<p>
</p>
<h3 id="core.giantswarm.io/v1alpha1.StorageConfigSpec">StorageConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.StorageConfig">StorageConfig</a>)
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
<code>storage</code></br>
<em>
<a href="#core.giantswarm.io/v1alpha1.StorageConfigSpecStorage">
StorageConfigSpecStorage
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="core.giantswarm.io/v1alpha1.StorageConfigSpecStorage">StorageConfigSpecStorage
</h3>
<p>
(<em>Appears on:</em>
<a href="#core.giantswarm.io/v1alpha1.StorageConfigSpec">StorageConfigSpec</a>)
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
<code>data</code></br>
<em>
map[string]string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
