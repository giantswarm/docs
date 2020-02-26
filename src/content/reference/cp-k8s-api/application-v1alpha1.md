---
title: application.giantswarm.io/v1alpha1
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#application.giantswarm.io%2fv1alpha1">application.giantswarm.io/v1alpha1</a>
</li>
</ul>
<h2 id="application.giantswarm.io/v1alpha1">application.giantswarm.io/v1alpha1</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#application.giantswarm.io/v1alpha1.App">App</a>
</li><li>
<a href="#application.giantswarm.io/v1alpha1.AppCatalog">AppCatalog</a>
</li><li>
<a href="#application.giantswarm.io/v1alpha1.Chart">Chart</a>
</li></ul>
<h3 id="application.giantswarm.io/v1alpha1.App">App
</h3>
<p>
<p>App CRs might look something like the following.</p>
<p>apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
name: &ldquo;prometheus&rdquo;
labels:
app-operator.giantswarm.io/version: &ldquo;1.0.0&rdquo;</p>
<p>spec:
catalog: &ldquo;giantswarm&rdquo;
name: &ldquo;prometheus&rdquo;
namespace: &ldquo;monitoring&rdquo;
version: &ldquo;1.0.0&rdquo;
config:
configMap:
name: &ldquo;prometheus-values&rdquo;
namespace: &ldquo;monitoring&rdquo;
secret:
name: &ldquo;prometheus-secrets&rdquo;
namespace: &ldquo;monitoring&rdquo;
kubeConfig:
inCluster: false
context:
name: &ldquo;giantswarm-12345&rdquo;
secret:
name: &ldquo;giantswarm-12345&rdquo;
namespace: &ldquo;giantswarm&rdquo;
userConfig:
configMap:
name: &ldquo;prometheus-user-values&rdquo;
namespace: &ldquo;monitoring&rdquo;</p>
<p>status:
appVersion: &ldquo;2.4.3&rdquo; # Optional value from Chart.yaml with the version of the deployed app.
release:
lastDeployed: &ldquo;2018-11-30T21:06:20Z&rdquo;
status: &ldquo;DEPLOYED&rdquo;
version: &ldquo;1.1.0&rdquo; # Required value from Chart.yaml with the version of the chart.</p>
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
application.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>App</code></td>
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
<a href="#application.giantswarm.io/v1alpha1.AppSpec">
AppSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>catalog</code></br>
<em>
string
</em>
</td>
<td>
<p>Catalog is the name of the app catalog this app belongs to.
e.g. giantswarm</p>
</td>
</tr>
<tr>
<td>
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfig">
AppSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when the app is deployed.</p>
</td>
</tr>
<tr>
<td>
<code>kubeConfig</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfig">
AppSpecKubeConfig
</a>
</em>
</td>
<td>
<p>KubeConfig is the kubeconfig to connect to the cluster when deploying
the app.</p>
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
<p>Name is the name of the app to be deployed.
e.g. kubernetes-prometheus</p>
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
<p>Namespace is the namespace where the app should be deployed.
e.g. monitoring</p>
</td>
</tr>
<tr>
<td>
<code>userConfig</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfig">
AppSpecUserConfig
</a>
</em>
</td>
<td>
<p>UserConfig is the user config to be applied when the app is deployed.</p>
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
<p>Version is the version of the app that should be deployed.
e.g. 1.0.0</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppStatus">
AppStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalog">AppCatalog
</h3>
<p>
<p>AppCatalog CRs might look something like the following.</p>
<p>apiVersion: application.giantswarm.io/v1alpha1
kind: AppCatalog
metadata:
name: &ldquo;giantswarm&rdquo;
labels:
app-operator.giantswarm.io/version: &ldquo;1.0.0&rdquo;</p>
<p>spec:
title: &ldquo;Giant Swarm&rdquo;
description: &ldquo;Catalog of Apps by Giant Swarm&rdquo;
config:
configMap:
name: &ldquo;app-catalog-values&rdquo;
namespace: &ldquo;giantswarm&rdquo;
secret:
name: &ldquo;app-catalog-secrets&rdquo;
namespace: &ldquo;giantswarm&rdquo;
logoURL: &ldquo;/images/repo_icons/incubator.png&rdquo;
storage:
type: &ldquo;helm&rdquo;
URL: &ldquo;<a href="https://giantswarm.github.com/app-catalog/&quot;">https://giantswarm.github.com/app-catalog/&rdquo;</a></p>
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
application.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AppCatalog</code></td>
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
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpec">
AppCatalogSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>title</code></br>
<em>
string
</em>
</td>
<td>
<p>Title is the name of the app catalog for this CR
e.g. Catalog of Apps by Giant Swarm</p>
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
</td>
</tr>
<tr>
<td>
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfig">
AppCatalogSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when apps belonging to this
catalog are deployed.</p>
</td>
</tr>
<tr>
<td>
<code>logoURL</code></br>
<em>
string
</em>
</td>
<td>
<p>LogoURL contains the links for logo image file for this app catalog</p>
</td>
</tr>
<tr>
<td>
<code>storage</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecStorage">
AppCatalogSpecStorage
</a>
</em>
</td>
<td>
<p>Storage references a map containing values that should be applied to
the appcatalog.</p>
</td>
</tr>
</table>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.Chart">Chart
</h3>
<p>
<p>Chart CRs might look something like the following.</p>
<p>apiVersion: application.giantswarm.io/v1alpha1
kind: Chart
metadata:
name: &ldquo;prometheus&rdquo;
labels:
chart-operator.giantswarm.io/version: &ldquo;1.0.0&rdquo;</p>
<p>spec:
name: &ldquo;prometheus&rdquo;
namespace: &ldquo;monitoring&rdquo;
config:
configMap:
name: &ldquo;prometheus-values&rdquo;
namespace: &ldquo;monitoring&rdquo;
resourceVersion: &ldquo;&rdquo;
secret:
name: &ldquo;prometheus-secrets&rdquo;
namespace: &ldquo;monitoring&rdquo;
resourceVersion: &ldquo;&rdquo;
tarballURL: &ldquo;<a href="https://giantswarm.github.com/app-catalog/prometheus-1-0-0.tgz&quot;">https://giantswarm.github.com/app-catalog/prometheus-1-0-0.tgz&rdquo;</a></p>
<p>status:
appVersion: &ldquo;2.4.3&rdquo; # Optional value from Chart.yaml with the version of the deployed app.
release:
lastDeployed: &ldquo;2018-11-30T21:06:20Z&rdquo;
status: &ldquo;DEPLOYED&rdquo;
version: &ldquo;1.1.0&rdquo; # Required value from Chart.yaml with the version of the chart.</p>
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
application.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>Chart</code></td>
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
<a href="#application.giantswarm.io/v1alpha1.ChartSpec">
ChartSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfig">
ChartSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when the chart is deployed.</p>
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
<p>Name is the name of the Helm chart to be deployed.
e.g. kubernetes-prometheus</p>
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
<p>Namespace is the namespace where the chart should be deployed.
e.g. monitoring</p>
</td>
</tr>
<tr>
<td>
<code>tarballURL</code></br>
<em>
string
</em>
</td>
<td>
<p>TarballURL is the URL for the Helm chart tarball to be deployed.
e.g. <a href="https://path/to/prom-1-0-0.tgz&quot;">https://path/to/prom-1-0-0.tgz&rdquo;</a></p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.ChartStatus">
ChartStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalogSpec">AppCatalogSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalog">AppCatalog</a>)
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
<code>title</code></br>
<em>
string
</em>
</td>
<td>
<p>Title is the name of the app catalog for this CR
e.g. Catalog of Apps by Giant Swarm</p>
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
</td>
</tr>
<tr>
<td>
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfig">
AppCatalogSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when apps belonging to this
catalog are deployed.</p>
</td>
</tr>
<tr>
<td>
<code>logoURL</code></br>
<em>
string
</em>
</td>
<td>
<p>LogoURL contains the links for logo image file for this app catalog</p>
</td>
</tr>
<tr>
<td>
<code>storage</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecStorage">
AppCatalogSpecStorage
</a>
</em>
</td>
<td>
<p>Storage references a map containing values that should be applied to
the appcatalog.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalogSpecConfig">AppCatalogSpecConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpec">AppCatalogSpec</a>)
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
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfigConfigMap">
AppCatalogSpecConfigConfigMap
</a>
</em>
</td>
<td>
<p>ConfigMap references a config map containing catalog values that
should be applied to apps in this catalog.</p>
</td>
</tr>
<tr>
<td>
<code>secret</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfigSecret">
AppCatalogSpecConfigSecret
</a>
</em>
</td>
<td>
<p>Secret references a secret containing catalog values that should be
applied to apps in this catalog.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalogSpecConfigConfigMap">AppCatalogSpecConfigConfigMap
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfig">AppCatalogSpecConfig</a>)
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
<p>Name is the name of the config map containing catalog values to
apply, e.g. app-catalog-values.</p>
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
<p>Namespace is the namespace of the catalog values config map,
e.g. giantswarm.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalogSpecConfigSecret">AppCatalogSpecConfigSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpecConfig">AppCatalogSpecConfig</a>)
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
<p>Name is the name of the secret containing catalog values to apply,
e.g. app-catalog-secret.</p>
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
e.g. giantswarm.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppCatalogSpecStorage">AppCatalogSpecStorage
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppCatalogSpec">AppCatalogSpec</a>)
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
<code>type</code></br>
<em>
string
</em>
</td>
<td>
<p>Type indicates which repository type would be used for this AppCatalog.
e.g. helm</p>
</td>
</tr>
<tr>
<td>
<code>URL</code></br>
<em>
string
</em>
</td>
<td>
<p>URL is the link to where this AppCatalog&rsquo;s repository is located
e.g. <a href="https://giantswarm.github.com/app-catalog/">https://giantswarm.github.com/app-catalog/</a>.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpec">AppSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.App">App</a>)
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
<code>catalog</code></br>
<em>
string
</em>
</td>
<td>
<p>Catalog is the name of the app catalog this app belongs to.
e.g. giantswarm</p>
</td>
</tr>
<tr>
<td>
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfig">
AppSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when the app is deployed.</p>
</td>
</tr>
<tr>
<td>
<code>kubeConfig</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfig">
AppSpecKubeConfig
</a>
</em>
</td>
<td>
<p>KubeConfig is the kubeconfig to connect to the cluster when deploying
the app.</p>
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
<p>Name is the name of the app to be deployed.
e.g. kubernetes-prometheus</p>
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
<p>Namespace is the namespace where the app should be deployed.
e.g. monitoring</p>
</td>
</tr>
<tr>
<td>
<code>userConfig</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfig">
AppSpecUserConfig
</a>
</em>
</td>
<td>
<p>UserConfig is the user config to be applied when the app is deployed.</p>
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
<p>Version is the version of the app that should be deployed.
e.g. 1.0.0</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecConfig">AppSpecConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpec">AppSpec</a>)
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
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfigConfigMap">
AppSpecConfigConfigMap
</a>
</em>
</td>
<td>
<p>ConfigMap references a config map containing values that should be
applied to the app.</p>
</td>
</tr>
<tr>
<td>
<code>secret</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfigSecret">
AppSpecConfigSecret
</a>
</em>
</td>
<td>
<p>Secret references a secret containing secret values that should be
applied to the app.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecConfigConfigMap">AppSpecConfigConfigMap
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfig">AppSpecConfig</a>)
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
<p>Name is the name of the config map containing app values to apply,
e.g. prometheus-values.</p>
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
e.g. monitoring.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecConfigSecret">AppSpecConfigSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecConfig">AppSpecConfig</a>)
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
<p>Name is the name of the secret containing app values to apply,
e.g. prometheus-secret.</p>
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
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecKubeConfig">AppSpecKubeConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpec">AppSpec</a>)
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
<code>inCluster</code></br>
<em>
bool
</em>
</td>
<td>
<p>InCluster is a flag for whether to use InCluster credentials. When true the
context name and secret should not be set.</p>
</td>
</tr>
<tr>
<td>
<code>context</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfigContext">
AppSpecKubeConfigContext
</a>
</em>
</td>
<td>
<p>Context is the kubeconfig context.</p>
</td>
</tr>
<tr>
<td>
<code>secret</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfigSecret">
AppSpecKubeConfigSecret
</a>
</em>
</td>
<td>
<p>Secret references a secret containing the kubconfig.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecKubeConfigContext">AppSpecKubeConfigContext
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfig">AppSpecKubeConfig</a>)
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
<p>Name is the name of the kubeconfig context.
e.g. giantswarm-12345.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecKubeConfigSecret">AppSpecKubeConfigSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecKubeConfig">AppSpecKubeConfig</a>)
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
<p>Name is the name of the secret containing the kubeconfig,
e.g. app-operator-kubeconfig.</p>
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
<p>Namespace is the namespace of the secret containing the kubeconfig,
e.g. giantswarm.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecUserConfig">AppSpecUserConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpec">AppSpec</a>)
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
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfigConfigMap">
AppSpecUserConfigConfigMap
</a>
</em>
</td>
<td>
<p>ConfigMap references a config map containing user values that should be
applied to the app.</p>
</td>
</tr>
<tr>
<td>
<code>secret</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfigSecret">
AppSpecUserConfigSecret
</a>
</em>
</td>
<td>
<p>Secret references a secret containing user secret values that should be
applied to the app.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecUserConfigConfigMap">AppSpecUserConfigConfigMap
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfig">AppSpecUserConfig</a>)
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
<p>Name is the name of the config map containing user values to apply,
e.g. prometheus-user-values.</p>
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
<p>Namespace is the namespace of the user values config map on the control plane,
e.g. 123ab.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppSpecUserConfigSecret">AppSpecUserConfigSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppSpecUserConfig">AppSpecUserConfig</a>)
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
<p>Name is the name of the secret containing user values to apply,
e.g. prometheus-user-secret.</p>
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
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppStatus">AppStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.App">App</a>)
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
<code>appVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>AppVersion is the value of the AppVersion field in the Chart.yaml of the
deployed app. This is an optional field with the version of the
component being deployed.
e.g. 0.21.0.
<a href="https://docs.helm.sh/developing_charts/#the-chart-yaml-file">https://docs.helm.sh/developing_charts/#the-chart-yaml-file</a></p>
</td>
</tr>
<tr>
<td>
<code>release</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.AppStatusRelease">
AppStatusRelease
</a>
</em>
</td>
<td>
<p>Release is the status of the Helm release for the deployed app.</p>
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
<p>Version is the value of the Version field in the Chart.yaml of the
deployed app.
e.g. 1.0.0.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.AppStatusRelease">AppStatusRelease
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppStatus">AppStatus</a>)
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
<code>lastDeployed</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastDeployed is the time when the app was last deployed.</p>
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
<p>Reason is the description of the last status of helm release when the app is
not installed successfully, e.g. deploy resource already exists.</p>
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
<p>Status is the status of the deployed app,
e.g. DEPLOYED.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.ChartSpec">ChartSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.Chart">Chart</a>)
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
<code>config</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfig">
ChartSpecConfig
</a>
</em>
</td>
<td>
<p>Config is the config to be applied when the chart is deployed.</p>
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
<p>Name is the name of the Helm chart to be deployed.
e.g. kubernetes-prometheus</p>
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
<p>Namespace is the namespace where the chart should be deployed.
e.g. monitoring</p>
</td>
</tr>
<tr>
<td>
<code>tarballURL</code></br>
<em>
string
</em>
</td>
<td>
<p>TarballURL is the URL for the Helm chart tarball to be deployed.
e.g. <a href="https://path/to/prom-1-0-0.tgz&quot;">https://path/to/prom-1-0-0.tgz&rdquo;</a></p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.ChartSpecConfig">ChartSpecConfig
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpec">ChartSpec</a>)
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
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfigConfigMap">
ChartSpecConfigConfigMap
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
<code>secret</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfigSecret">
ChartSpecConfigSecret
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
<h3 id="application.giantswarm.io/v1alpha1.ChartSpecConfigConfigMap">ChartSpecConfigConfigMap
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfig">ChartSpecConfig</a>)
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
e.g. prometheus-chart-values.</p>
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
e.g. monitoring.</p>
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
<h3 id="application.giantswarm.io/v1alpha1.ChartSpecConfigSecret">ChartSpecConfigSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.ChartSpecConfig">ChartSpecConfig</a>)
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
e.g. prometheus-chart-secret.</p>
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
<h3 id="application.giantswarm.io/v1alpha1.ChartStatus">ChartStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.Chart">Chart</a>)
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
<code>appVersion</code></br>
<em>
string
</em>
</td>
<td>
<p>AppVersion is the value of the AppVersion field in the Chart.yaml of the
deployed chart. This is an optional field with the version of the
component being deployed.
e.g. 0.21.0.
<a href="https://docs.helm.sh/developing_charts/#the-chart-yaml-file">https://docs.helm.sh/developing_charts/#the-chart-yaml-file</a></p>
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
<tr>
<td>
<code>release</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.ChartStatusRelease">
ChartStatusRelease
</a>
</em>
</td>
<td>
<p>Release is the status of the Helm release for the deployed chart.</p>
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
<p>Version is the value of the Version field in the Chart.yaml of the
deployed chart.
e.g. 1.0.0.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.ChartStatusRelease">ChartStatusRelease
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.ChartStatus">ChartStatus</a>)
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
<code>lastDeployed</code></br>
<em>
<a href="#application.giantswarm.io/v1alpha1.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>LastDeployed is the time when the deployed chart was last deployed.</p>
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
<p>Status is the status of the deployed chart,
e.g. DEPLOYED.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="application.giantswarm.io/v1alpha1.DeepCopyTime">DeepCopyTime
</h3>
<p>
(<em>Appears on:</em>
<a href="#application.giantswarm.io/v1alpha1.AppStatusRelease">AppStatusRelease</a>, 
<a href="#application.giantswarm.io/v1alpha1.ChartStatusRelease">ChartStatusRelease</a>)
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
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
