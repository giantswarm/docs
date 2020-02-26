---
title: provider.giantswarm.io/v1alpha1
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#provider.giantswarm.io%2fv1alpha1">provider.giantswarm.io/v1alpha1</a>
</li>
</ul>
<h2 id="provider.giantswarm.io/v1alpha1">provider.giantswarm.io/v1alpha1</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfig">AWSConfig</a>
</li><li>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfig">AzureConfig</a>
</li><li>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfig">KVMConfig</a>
</li></ul>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfig">AWSConfig
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
provider.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AWSConfig</code></td>
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpec">
AWSConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>aws</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">
AWSConfigSpecAWS
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecVersionBundle">
AWSConfigSpecVersionBundle
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatus">
AWSConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfig">AzureConfig
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
provider.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AzureConfig</code></td>
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpec">
AzureConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>azure</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">
AzureConfigSpecAzure
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecVersionBundle">
AzureConfigSpecVersionBundle
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatus">
AzureConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfig">KVMConfig
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
provider.giantswarm.io/v1alpha1
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>KVMConfig</code></td>
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpec">
KVMConfigSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>cluster</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>kvm</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">
KVMConfigSpecKVM
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecVersionBundle">
KVMConfigSpecVersionBundle
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigStatus">
KVMConfigStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpec">AWSConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfig">AWSConfig</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>aws</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">
AWSConfigSpecAWS
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecVersionBundle">
AWSConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpec">AWSConfigSpec</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSAPI">
AWSConfigSpecAWSAPI
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>az</code></br>
<em>
string
</em>
</td>
<td>
<p>TODO remove the deprecated AZ field due to AvailabilityZones.</p>
<pre><code>https://github.com/giantswarm/giantswarm/issues/4507
</code></pre>
</td>
</tr>
<tr>
<td>
<code>availabilityZones</code></br>
<em>
int
</em>
</td>
<td>
<p>AvailabilityZones is the number of AWS availability zones used to spread
the tenant cluster&rsquo;s worker nodes across. There are limitations on
availability zone settings due to binary IP range splitting and provider
specific region capabilities. When for instance choosing 3 availability
zones, the configured IP range will be split into 4 ranges and thus one of
it will not be able to be utilized. Such limitations have to be considered
when designing the network topology and configuring tenant cluster HA via
AvailabilityZones.</p>
<p>The selection and usage of the actual availability zones for the created
tenant cluster is randomized. In case there are 4 availability zones
provided in the used region and the user selects 2 availability zones, the
actually used availability zones in which tenant cluster workload is put
into will tend to be different across tenant cluster creations. This is
done in order to provide more HA during single availability zone failures.
In case a specific availability zone fails, not all tenant clusters will be
affected due to the described selection process.</p>
</td>
</tr>
<tr>
<td>
<code>credentialSecret</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.CredentialSecret">
CredentialSecret
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>etcd</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSEtcd">
AWSConfigSpecAWSEtcd
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>hostedZones</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZones">
AWSConfigSpecAWSHostedZones
</a>
</em>
</td>
<td>
<p>HostedZones is AWS hosted zones names in the host cluster account.
For each zone there will be &ldquo;CLUSTER_ID.k8s&rdquo; NS record created in
the host cluster account. Then for each created NS record there will
be a zone created in the guest account. After that component
specific records under those zones:
- api.CLUSTER_ID.k8s.\{\{ .Spec.AWS.HostedZones.API.Name \}\}
- etcd.CLUSTER_ID.k8s.\{\{ .Spec.AWS.HostedZones.Etcd.Name \}\}
- ingress.CLUSTER_ID.k8s.\{\{ .Spec.AWS.HostedZones.Ingress.Name \}\}
- *.CLUSTER_ID.k8s.\{\{ .Spec.AWS.HostedZones.Ingress.Name \}\}</p>
</td>
</tr>
<tr>
<td>
<code>ingress</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSIngress">
AWSConfigSpecAWSIngress
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSNode">
[]AWSConfigSpecAWSNode
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>region</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>vpc</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSVPC">
AWSConfigSpecAWSVPC
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSNode">
[]AWSConfigSpecAWSNode
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSAPI">AWSConfigSpecAWSAPI
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
</p>
<p>
<p>AWSConfigSpecAWSAPI deprecated since aws-operator v12 resources.</p>
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
<code>hostedZones</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>elb</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSAPIELB">
AWSConfigSpecAWSAPIELB
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSAPIELB">AWSConfigSpecAWSAPIELB
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSAPI">AWSConfigSpecAWSAPI</a>)
</p>
<p>
<p>AWSConfigSpecAWSAPIELB deprecated since aws-operator v12 resources.</p>
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
<code>idleTimeoutSeconds</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSEtcd">AWSConfigSpecAWSEtcd
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
</p>
<p>
<p>AWSConfigSpecAWSEtcd deprecated since aws-operator v12 resources.</p>
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
<code>hostedZones</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>elb</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSEtcdELB">
AWSConfigSpecAWSEtcdELB
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSEtcdELB">AWSConfigSpecAWSEtcdELB
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSEtcd">AWSConfigSpecAWSEtcd</a>)
</p>
<p>
<p>AWSConfigSpecAWSEtcdELB deprecated since aws-operator v12 resources.</p>
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
<code>idleTimeoutSeconds</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZones">AWSConfigSpecAWSHostedZones
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZonesZone">
AWSConfigSpecAWSHostedZonesZone
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>etcd</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZonesZone">
AWSConfigSpecAWSHostedZonesZone
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ingress</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZonesZone">
AWSConfigSpecAWSHostedZonesZone
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZonesZone">AWSConfigSpecAWSHostedZonesZone
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSHostedZones">AWSConfigSpecAWSHostedZones</a>)
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
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSIngress">AWSConfigSpecAWSIngress
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
</p>
<p>
<p>AWSConfigSpecAWSIngress deprecated since aws-operator v12 resources.</p>
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
<code>hostedZones</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>elb</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSIngressELB">
AWSConfigSpecAWSIngressELB
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSIngressELB">AWSConfigSpecAWSIngressELB
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSIngress">AWSConfigSpecAWSIngress</a>)
</p>
<p>
<p>AWSConfigSpecAWSIngressELB deprecated since aws-operator v12 resources.</p>
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
<code>idleTimeoutSeconds</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSNode">AWSConfigSpecAWSNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
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
<code>imageID</code></br>
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
<tr>
<td>
<code>dockerVolumeSizeGB</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecAWSVPC">AWSConfigSpecAWSVPC
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>)
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>privateSubnetCidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>publicSubnetCidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>routeTableNames</code></br>
<em>
[]string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>peerId</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigSpecVersionBundle">AWSConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpec">AWSConfigSpec</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatus">AWSConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfig">AWSConfig</a>)
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
<code>aws</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWS">
AWSConfigStatusAWS
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
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">
StatusCluster
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWS">AWSConfigStatusAWS
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatus">AWSConfigStatus</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZone">
[]AWSConfigStatusAWSAvailabilityZone
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>autoScalingGroup</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAutoScalingGroup">
AWSConfigStatusAWSAutoScalingGroup
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAutoScalingGroup">AWSConfigStatusAWSAutoScalingGroup
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWS">AWSConfigStatusAWS</a>)
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
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZone">AWSConfigStatusAWSAvailabilityZone
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWS">AWSConfigStatusAWS</a>)
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
<code>subnet</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnet">
AWSConfigStatusAWSAvailabilityZoneSubnet
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnet">AWSConfigStatusAWSAvailabilityZoneSubnet
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZone">AWSConfigStatusAWSAvailabilityZone</a>)
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
<code>private</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnetPrivate">
AWSConfigStatusAWSAvailabilityZoneSubnetPrivate
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>public</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnetPublic">
AWSConfigStatusAWSAvailabilityZoneSubnetPublic
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnetPrivate">AWSConfigStatusAWSAvailabilityZoneSubnetPrivate
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnet">AWSConfigStatusAWSAvailabilityZoneSubnet</a>)
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnetPublic">AWSConfigStatusAWSAvailabilityZoneSubnetPublic
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatusAWSAvailabilityZoneSubnet">AWSConfigStatusAWSAvailabilityZoneSubnet</a>)
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpec">AzureConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfig">AzureConfig</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>azure</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">
AzureConfigSpecAzure
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecVersionBundle">
AzureConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">AzureConfigSpecAzure
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpec">AzureConfigSpec</a>)
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
[]int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>credentialSecret</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.CredentialSecret">
CredentialSecret
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>dnsZones</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZones">
AzureConfigSpecAzureDNSZones
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureNode">
[]AzureConfigSpecAzureNode
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>virtualNetwork</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureVirtualNetwork">
AzureConfigSpecAzureVirtualNetwork
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureNode">
[]AzureConfigSpecAzureNode
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZones">AzureConfigSpecAzureDNSZones
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">AzureConfigSpecAzure</a>)
</p>
<p>
<p>AzureConfigSpecAzureDNSZones contains the DNS Zones of the cluster.</p>
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
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZonesDNSZone">
AzureConfigSpecAzureDNSZonesDNSZone
</a>
</em>
</td>
<td>
<p>API is the DNS Zone for the Kubernetes API.</p>
</td>
</tr>
<tr>
<td>
<code>etcd</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZonesDNSZone">
AzureConfigSpecAzureDNSZonesDNSZone
</a>
</em>
</td>
<td>
<p>Etcd is the DNS Zone for the etcd cluster.</p>
</td>
</tr>
<tr>
<td>
<code>ingress</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZonesDNSZone">
AzureConfigSpecAzureDNSZonesDNSZone
</a>
</em>
</td>
<td>
<p>Ingress is the DNS Zone for the Ingress resource, used for customer traffic.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZonesDNSZone">AzureConfigSpecAzureDNSZonesDNSZone
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureDNSZones">AzureConfigSpecAzureDNSZones</a>)
</p>
<p>
<p>AzureConfigSpecAzureDNSZonesDNSZone points to a DNS Zone in Azure.</p>
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
<code>resourceGroup</code></br>
<em>
string
</em>
</td>
<td>
<p>ResourceGroup is the resource group of the zone.</p>
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
<p>Name is the name of the zone.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureNode">AzureConfigSpecAzureNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">AzureConfigSpecAzure</a>)
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
<code>vmSize</code></br>
<em>
string
</em>
</td>
<td>
<p>VMSize is the master vm size (e.g. Standard_A1)</p>
</td>
</tr>
<tr>
<td>
<code>dockerVolumeSizeGB</code></br>
<em>
int
</em>
</td>
<td>
<p>DockerVolumeSizeGB is the size of a volume mounted to /var/lib/docker.</p>
</td>
</tr>
<tr>
<td>
<code>kubeletVolumeSizeGB</code></br>
<em>
int
</em>
</td>
<td>
<p>KubeletVolumeSizeGB is the size of a volume mounted to /var/lib/kubelet.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecAzureVirtualNetwork">AzureConfigSpecAzureVirtualNetwork
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">AzureConfigSpecAzure</a>)
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
<p>CIDR is the CIDR for the Virtual Network.</p>
</td>
</tr>
<tr>
<td>
<code>masterSubnetCIDR</code></br>
<em>
string
</em>
</td>
<td>
<p>TODO: remove Master, Worker and Calico subnet cidr after azure-operator v2
is deleted. MasterSubnetCIDR is the CIDR for the master subnet.</p>
<pre><code>https://github.com/giantswarm/giantswarm/issues/4358
</code></pre>
</td>
</tr>
<tr>
<td>
<code>workerSubnetCIDR</code></br>
<em>
string
</em>
</td>
<td>
<p>WorkerSubnetCIDR is the CIDR for the worker subnet.</p>
</td>
</tr>
<tr>
<td>
<code>calicoSubnetCIDR</code></br>
<em>
string
</em>
</td>
<td>
<p>CalicoSubnetCIDR is the CIDR for the calico subnet. It has to be
also a worker subnet (Azure limitation).</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigSpecVersionBundle">AzureConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpec">AzureConfigSpec</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigStatus">AzureConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfig">AzureConfig</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">
StatusCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>provider</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatusProvider">
AzureConfigStatusProvider
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigStatusProvider">AzureConfigStatusProvider
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatus">AzureConfigStatus</a>)
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
[]int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ingress</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatusProviderIngress">
AzureConfigStatusProviderIngress
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigStatusProviderIngress">AzureConfigStatusProviderIngress
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatusProvider">AzureConfigStatusProvider</a>)
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
<code>loadBalancer</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatusProviderIngressLoadBalancer">
AzureConfigStatusProviderIngressLoadBalancer
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.AzureConfigStatusProviderIngressLoadBalancer">AzureConfigStatusProviderIngressLoadBalancer
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatusProviderIngress">AzureConfigStatusProviderIngress</a>)
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
<code>publicIPName</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.Cluster">Cluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpec">AWSConfigSpec</a>, 
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpec">AzureConfigSpec</a>, 
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpec">KVMConfigSpec</a>)
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
<code>calico</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterCalico">
ClusterCalico
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>customer</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterCustomer">
ClusterCustomer
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>docker</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterDocker">
ClusterDocker
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>etcd</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterEtcd">
ClusterEtcd
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
</td>
</tr>
<tr>
<td>
<code>kubernetes</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">
ClusterKubernetes
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
<a href="#provider.giantswarm.io/v1alpha1.ClusterNode">
[]ClusterNode
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>scaling</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterScaling">
ClusterScaling
</a>
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
<p>Version is DEPRECATED and should just be dropped.</p>
</td>
</tr>
<tr>
<td>
<code>workers</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterNode">
[]ClusterNode
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterCalico">ClusterCalico
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
<code>cidr</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>mtu</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>subnet</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterCustomer">ClusterCustomer
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterDocker">ClusterDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
<code>daemon</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterDockerDaemon">
ClusterDockerDaemon
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterDockerDaemon">ClusterDockerDaemon
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterDocker">ClusterDocker</a>)
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterEtcd">ClusterEtcd
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
<code>altNames</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>port</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>prefix</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesAPI">
ClusterKubernetesAPI
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>cloudProvider</code></br>
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
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesDNS">
ClusterKubernetesDNS
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ingressController</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesIngressController">
ClusterKubernetesIngressController
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>kubelet</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesKubelet">
ClusterKubernetesKubelet
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>networkSetup</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesNetworkSetup">
ClusterKubernetesNetworkSetup
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>ssh</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesSSH">
ClusterKubernetesSSH
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesAPI">ClusterKubernetesAPI
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<code>clusterIPRange</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>securePort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesDNS">ClusterKubernetesDNS
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<code>ip</code></br>
<em>
net.IP
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesIngressController">ClusterKubernetesIngressController
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesIngressControllerDocker">
ClusterKubernetesIngressControllerDocker
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>wildcardDomain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>insecurePort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>securePort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesIngressControllerDocker">ClusterKubernetesIngressControllerDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesIngressController">ClusterKubernetesIngressController</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesKubelet">ClusterKubernetesKubelet
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<code>altNames</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>labels</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>port</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesNetworkSetup">ClusterKubernetesNetworkSetup
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesNetworkSetupDocker">
ClusterKubernetesNetworkSetupDocker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesNetworkSetupDocker">ClusterKubernetesNetworkSetupDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesNetworkSetup">ClusterKubernetesNetworkSetup</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesSSH">ClusterKubernetesSSH
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetes">ClusterKubernetes</a>)
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
<code>userList</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesSSHUser">
[]ClusterKubernetesSSHUser
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterKubernetesSSHUser">ClusterKubernetesSSHUser
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.ClusterKubernetesSSH">ClusterKubernetesSSH</a>)
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
<code>publicKey</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterNode">ClusterNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.ClusterScaling">ClusterScaling
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.Cluster">Cluster</a>)
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
<code>max</code></br>
<em>
int
</em>
</td>
<td>
<p>Max defines maximum number of worker nodes guest cluster is allowed to have.</p>
</td>
</tr>
<tr>
<td>
<code>min</code></br>
<em>
int
</em>
</td>
<td>
<p>Min defines minimum number of worker nodes required to be present in guest cluster.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.CredentialSecret">CredentialSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigSpecAWS">AWSConfigSpecAWS</a>, 
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigSpecAzure">AzureConfigSpecAzure</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.DeepCopyTime">DeepCopyTime
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterCondition">StatusClusterCondition</a>, 
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterNode">StatusClusterNode</a>, 
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterResourceCondition">StatusClusterResourceCondition</a>, 
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterVersion">StatusClusterVersion</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpec">KVMConfigSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfig">KVMConfig</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.Cluster">
Cluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>kvm</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">
KVMConfigSpecKVM
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecVersionBundle">
KVMConfigSpecVersionBundle
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpec">KVMConfigSpec</a>)
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
<code>endpointUpdater</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMEndpointUpdater">
KVMConfigSpecKVMEndpointUpdater
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>k8sKVM</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMK8sKVM">
KVMConfigSpecKVMK8sKVM
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNode">
[]KVMConfigSpecKVMNode
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>network</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNetwork">
KVMConfigSpecKVMNetwork
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>nodeController</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNodeController">
KVMConfigSpecKVMNodeController
</a>
</em>
</td>
<td>
<p>NOTE THIS IS DEPRECATED</p>
</td>
</tr>
<tr>
<td>
<code>portMappings</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMPortMappings">
[]KVMConfigSpecKVMPortMappings
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNode">
[]KVMConfigSpecKVMNode
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMEndpointUpdater">KVMConfigSpecKVMEndpointUpdater
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMEndpointUpdaterDocker">
KVMConfigSpecKVMEndpointUpdaterDocker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMEndpointUpdaterDocker">KVMConfigSpecKVMEndpointUpdaterDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMEndpointUpdater">KVMConfigSpecKVMEndpointUpdater</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMK8sKVM">KVMConfigSpecKVMK8sKVM
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMK8sKVMDocker">
KVMConfigSpecKVMK8sKVMDocker
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>storageType</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMK8sKVMDocker">KVMConfigSpecKVMK8sKVMDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMK8sKVM">KVMConfigSpecKVMK8sKVM</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNetwork">KVMConfigSpecKVMNetwork
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
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
<code>flannel</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNetworkFlannel">
KVMConfigSpecKVMNetworkFlannel
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNetworkFlannel">KVMConfigSpecKVMNetworkFlannel
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNetwork">KVMConfigSpecKVMNetwork</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNode">KVMConfigSpecKVMNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
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
<code>cpus</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>disk</code></br>
<em>
float64
</em>
</td>
<td>
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
</td>
</tr>
<tr>
<td>
<code>dockerVolumeSizeGB</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNodeController">KVMConfigSpecKVMNodeController
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
</p>
<p>
<p>NOTE THIS IS DEPRECATED</p>
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
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNodeControllerDocker">
KVMConfigSpecKVMNodeControllerDocker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNodeControllerDocker">KVMConfigSpecKVMNodeControllerDocker
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMNodeController">KVMConfigSpecKVMNodeController</a>)
</p>
<p>
<p>NOTE THIS IS DEPRECATED</p>
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecKVMPortMappings">KVMConfigSpecKVMPortMappings
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpecKVM">KVMConfigSpecKVM</a>)
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
<code>nodePort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>targetPort</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigSpecVersionBundle">KVMConfigSpecVersionBundle
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigSpec">KVMConfigSpec</a>)
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
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigStatus">KVMConfigStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfig">KVMConfig</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">
StatusCluster
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>kvm</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigStatusKVM">
KVMConfigStatusKVM
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.KVMConfigStatusKVM">KVMConfigStatusKVM
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigStatus">KVMConfigStatus</a>)
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
<code>nodeIndexes</code></br>
<em>
map[string]int
</em>
</td>
<td>
<p>NodeIndexes is a map from nodeID -&gt; nodeIndex. This is used to create deterministic iSCSI initiator names.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.AWSConfigStatus">AWSConfigStatus</a>, 
<a href="#provider.giantswarm.io/v1alpha1.AzureConfigStatus">AzureConfigStatus</a>, 
<a href="#provider.giantswarm.io/v1alpha1.KVMConfigStatus">KVMConfigStatus</a>)
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
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterCondition">
[]StatusClusterCondition
</a>
</em>
</td>
<td>
<p>Conditions is a list of status information expressing the current
conditional state of a guest cluster. This may reflect the status of the
guest cluster being updating or being up to date.</p>
</td>
</tr>
<tr>
<td>
<code>network</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterNetwork">
StatusClusterNetwork
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>nodes</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterNode">
[]StatusClusterNode
</a>
</em>
</td>
<td>
<p>Nodes is a list of guest cluster node information reflecting the current
state of the guest cluster nodes.</p>
</td>
</tr>
<tr>
<td>
<code>resources</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterResource">
[]StatusClusterResource
</a>
</em>
</td>
<td>
<p>Resources is a list of arbitrary conditions of operatorkit resource
implementations.</p>
</td>
</tr>
<tr>
<td>
<code>scaling</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterScaling">
StatusClusterScaling
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>versions</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterVersion">
[]StatusClusterVersion
</a>
</em>
</td>
<td>
<p>Versions is a list that acts like a historical track record of versions a
guest cluster went through. A version is only added to the list as soon as
the guest cluster successfully migrated to the version added here.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterCondition">StatusClusterCondition
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>StatusClusterCondition expresses the conditions in which a guest cluster may
is.</p>
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
<code>lastTransitionTime</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.DeepCopyTime">
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
<p>Type may be Creating, Created, Scaling, Scaled, Draining, Drained,
Updating, Updated, Deleting, Deleted.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterNetwork">StatusClusterNetwork
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>StatusClusterNetwork expresses the network segment that is allocated for a
guest cluster.</p>
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
<code>cidr</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterNode">StatusClusterNode
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>StatusClusterNode holds information about a guest cluster node.</p>
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
<code>labels</code></br>
<em>
map[string]string
</em>
</td>
<td>
<p>Labels contains the kubernetes labels for corresponding node.</p>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.DeepCopyTime">
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
<code>name</code></br>
<em>
string
</em>
</td>
<td>
<p>Name referrs to a tenant cluster node name.</p>
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
<p>Version referrs to the version used by the node as mandated by the provider
operator.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterResource">StatusClusterResource
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>Resource is structure holding arbitrary conditions of operatorkit resource
implementations. Imagine an operator implements an instance resource. This
resource may operates sequentially but has to operate based on a certain
system state it manages. So it tracks the status as needed here specific to
its own implementation and means in order to fulfil its premise.</p>
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
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterResourceCondition">
[]StatusClusterResourceCondition
</a>
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
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterResourceCondition">StatusClusterResourceCondition
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusClusterResource">StatusClusterResource</a>)
</p>
<p>
<p>StatusClusterResourceCondition expresses the conditions in which an
operatorkit resource may is.</p>
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
<code>lastTransitionTime</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.DeepCopyTime">
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
<p>Type may be anything an operatorkit resource may define.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterScaling">StatusClusterScaling
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>StatusClusterScaling expresses the current status of desired number of
worker nodes in guest cluster.</p>
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
<code>desiredCapacity</code></br>
<em>
int
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="provider.giantswarm.io/v1alpha1.StatusClusterVersion">StatusClusterVersion
</h3>
<p>
(<em>Appears on:</em>
<a href="#provider.giantswarm.io/v1alpha1.StatusCluster">StatusCluster</a>)
</p>
<p>
<p>StatusClusterVersion expresses the versions in which a guest cluster was and
may still be.</p>
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
<code>date</code></br>
<em>
time.Time
</em>
</td>
<td>
<p>TODO date is deprecated due to LastTransitionTime
This can be removed ones the new properties are properly used in all tenant
clusters.</p>
<pre><code>https://github.com/giantswarm/giantswarm/issues/3988
</code></pre>
</td>
</tr>
<tr>
<td>
<code>lastTransitionTime</code></br>
<em>
<a href="#provider.giantswarm.io/v1alpha1.DeepCopyTime">
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
<code>semver</code></br>
<em>
string
</em>
</td>
<td>
<p>Semver is some semver version, e.g. 1.0.0.</p>
</td>
</tr>
</tbody>
</table>
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
