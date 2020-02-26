---
title: infrastructure.giantswarm.io/v1alpha2
date: "2020-02-21"
weight: 1
---

<p>Packages:</p>
<ul>
<li>
<a href="#infrastructure.giantswarm.io%2fv1alpha2">infrastructure.giantswarm.io/v1alpha2</a>
</li>
</ul>
<h2 id="infrastructure.giantswarm.io/v1alpha2">infrastructure.giantswarm.io/v1alpha2</h2>
<p>
</p>
Resource Types:
<ul><li>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSCluster">AWSCluster</a>
</li><li>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSControlPlane">AWSControlPlane</a>
</li><li>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeployment">AWSMachineDeployment</a>
</li><li>
<a href="#infrastructure.giantswarm.io/v1alpha2.G8sControlPlane">G8sControlPlane</a>
</li></ul>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSCluster">AWSCluster
</h3>
<p>
<p>AWSCluster is the infrastructure provider referenced in upstream CAPI Cluster
CRs.</p>
<pre><code>apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
labels:
aws-operator.giantswarm.io/version: 6.2.0
cluster-operator.giantswarm.io/version: 0.17.0
giantswarm.io/cluster: &quot;8y5kc&quot;
giantswarm.io/organization: &quot;giantswarm&quot;
release.giantswarm.io/version: 7.3.1
name: 8y5kc
spec:
cluster:
description: my fancy cluster
dns:
domain: gauss.eu-central-1.aws.gigantic.io
oidc:
claims:
username: email
groups: groups
clientID: foobar-dex-client
issuerURL: https://dex.gatekeeper.eu-central-1.aws.example.com
provider:
credentialSecret:
name: credential-default
namespace: giantswarm
master:
availabilityZone: eu-central-1a
instanceType: m4.large
region: eu-central-1
status:
cluster:
conditions:
- lastTransitionTime: &quot;2019-03-25T17:10:09.333633991Z&quot;
type: Created
id: 8y5kc
versions:
- lastTransitionTime: &quot;2019-03-25T17:10:09.995948706Z&quot;
version: 4.9.0
provider:
network:
cidr: 10.1.6.0/24
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
infrastructure.giantswarm.io/v1alpha2
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AWSCluster</code></td>
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
<p>metav1.ObjectMeta is standard Kubernetes resource metadata.</p>
Refer to the Kubernetes API documentation for the fields of the
<code>metadata</code> field.
</td>
</tr>
<tr>
<td>
<code>spec</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpec">
AWSClusterSpec
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecCluster">
AWSClusterSpecCluster
</a>
</em>
</td>
<td>
<p>Cluster provides cluster specification details.</p>
</td>
</tr>
<tr>
<td>
<code>provider</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProvider">
AWSClusterSpecProvider
</a>
</em>
</td>
<td>
<p>Provider holds provider-specific configuration details.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatus">
AWSClusterStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSControlPlane">AWSControlPlane
</h3>
<p>
<p>AWSControlPlane is the infrastructure provider referenced in ControlPlane
CRs.</p>
<pre><code>apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSControlPlane
metadata:
annotations:
giantswarm.io/docs: https://docs.giantswarm.io/reference/awscontrolplanes.infrastructure.giantswarm.io/v1alpha2/
labels:
aws-operator.giantswarm.io/version: &quot;6.2.0&quot;
giantswarm.io/cluster: 8y5kc
giantswarm.io/organization: giantswarm
release.giantswarm.io/version: &quot;7.3.1&quot;
name: 8y5kc
ownerReference:
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: G8sControlPlane
name: 8y5kc
namespace: default
spec:
availabilityZones:
- eu-central-1a
- eu-central-1b
- eu-central-1c
instanceType: m4.large
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
infrastructure.giantswarm.io/v1alpha2
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AWSControlPlane</code></td>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSControlPlaneSpec">
AWSControlPlaneSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>availabilityZones</code></br>
<em>
[]string
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
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSControlPlaneStatus">
AWSControlPlaneStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeployment">AWSMachineDeployment
</h3>
<p>
<p>AWSMachineDeployment is the infrastructure provider referenced in upstream
CAPI MachineDeployment CRs.</p>
<pre><code>apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSMachineDeployment
metadata:
labels:
aws-operator.giantswarm.io/version: 6.2.0
cluster-operator.giantswarm.io/version: 0.17.0
giantswarm.io/cluster: 8y5kc
giantswarm.io/organization: &quot;giantswarm&quot;
giantswarm.io/machine-deployment: al9qy
release.giantswarm.io/version: 7.3.1
name: al9qy
spec:
nodePool:
description: my fancy node pool
machine:
dockerVolumeSizeGB: 100
kubeletVolumeSizeGB: 100
scaling:
max: 3
min: 3
provider:
availabilityZones:
- eu-central-1a
worker:
instanceType: m4.xlarge
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
infrastructure.giantswarm.io/v1alpha2
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>AWSMachineDeployment</code></td>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpec">
AWSMachineDeploymentSpec
</a>
</em>
</td>
<td>
<br/>
<br/>
<table>
<tr>
<td>
<code>nodePool</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePool">
AWSMachineDeploymentSpecNodePool
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProvider">
AWSMachineDeploymentSpecProvider
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
<h3 id="infrastructure.giantswarm.io/v1alpha2.G8sControlPlane">G8sControlPlane
</h3>
<p>
<p>G8sControlPlane defines the Control Plane Nodes (Kubernetes Master Nodes) of
a Giant Swarm Tenant Cluster</p>
<pre><code>apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: G8sControlPlane
metadata:
annotations:
giantswarm.io/docs: https://docs.giantswarm.io/reference/g8scontrolplanes.infrastructure.giantswarm.io/v1alpha2/
labels:
aws-operator.giantswarm.io/version: &quot;6.2.0&quot;
cluster-operator.giantswarm.io/version: &quot;0.17.0&quot;
giantswarm.io/cluster: 8y5kc
giantswarm.io/organization: giantswarm
release.giantswarm.io/version: &quot;7.3.1&quot;
name: 8y5kc
spec:
infrastructureRef:
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSControlPlane
name: 5f3kb
namespace: default
replicas: 3
status:
readyReplicas: 3
replicas: 3
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
infrastructure.giantswarm.io/v1alpha2
</code>
</td>
</tr>
<tr>
<td>
<code>kind</code></br>
string
</td>
<td><code>G8sControlPlane</code></td>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.G8sControlPlaneSpec">
G8sControlPlaneSpec
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
<p>Replicas is the number replicas of the master node.</p>
</td>
</tr>
<tr>
<td>
<code>infrastructureRef</code></br>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#objectreference-v1-core">
Kubernetes core/v1.ObjectReference
</a>
</em>
</td>
<td>
<p>InfrastructureRef is a required reference to provider-specific
Infrastructure.</p>
</td>
</tr>
</table>
</td>
</tr>
<tr>
<td>
<code>status</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.G8sControlPlaneStatus">
G8sControlPlaneStatus
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpec">AWSClusterSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSCluster">AWSCluster</a>)
</p>
<p>
<p>AWSClusterSpec is the spec part for the AWSCluster resource.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecCluster">
AWSClusterSpecCluster
</a>
</em>
</td>
<td>
<p>Cluster provides cluster specification details.</p>
</td>
</tr>
<tr>
<td>
<code>provider</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProvider">
AWSClusterSpecProvider
</a>
</em>
</td>
<td>
<p>Provider holds provider-specific configuration details.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecCluster">AWSClusterSpecCluster
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpec">AWSClusterSpec</a>)
</p>
<p>
<p>AWSClusterSpecCluster provides cluster specification details.</p>
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
<p>Description is a user-friendly description that should explain the purpose of the
cluster to humans.</p>
</td>
</tr>
<tr>
<td>
<code>dns</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterDNS">
AWSClusterSpecClusterDNS
</a>
</em>
</td>
<td>
<p>DNS holds DNS configuration details.</p>
</td>
</tr>
<tr>
<td>
<code>oidc</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterOIDC">
AWSClusterSpecClusterOIDC
</a>
</em>
</td>
<td>
<p>OIDC holds configuration for OpenID Connect (OIDC) authentication.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterDNS">AWSClusterSpecClusterDNS
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecCluster">AWSClusterSpecCluster</a>)
</p>
<p>
<p>AWSClusterSpecClusterDNS holds DNS configuration details.</p>
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
<code>domain</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterOIDC">AWSClusterSpecClusterOIDC
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecCluster">AWSClusterSpecCluster</a>)
</p>
<p>
<p>AWSClusterSpecClusterOIDC holds configuration for OpenID Connect (OIDC) authentication.</p>
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
<code>claims</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterOIDCClaims">
AWSClusterSpecClusterOIDCClaims
</a>
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>clientID</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>issuerURL</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterOIDCClaims">AWSClusterSpecClusterOIDCClaims
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecClusterOIDC">AWSClusterSpecClusterOIDC</a>)
</p>
<p>
<p>AWSClusterSpecClusterOIDCClaims defines OIDC claims.</p>
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
<code>username</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>groups</code></br>
<em>
string
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProvider">AWSClusterSpecProvider
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpec">AWSClusterSpec</a>)
</p>
<p>
<p>AWSClusterSpecProvider holds some AWS details.</p>
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
<code>credentialSecret</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProviderCredentialSecret">
AWSClusterSpecProviderCredentialSecret
</a>
</em>
</td>
<td>
<p>CredentialSecret specifies the location of the secret providing the ARN of AWS IAM identity
to use with this cluster.</p>
</td>
</tr>
<tr>
<td>
<code>master</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProviderMaster">
AWSClusterSpecProviderMaster
</a>
</em>
</td>
<td>
<p>Master holds master node configuration details.</p>
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
<p>Region is the AWS region the cluster is to be running in.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProviderCredentialSecret">AWSClusterSpecProviderCredentialSecret
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProvider">AWSClusterSpecProvider</a>)
</p>
<p>
<p>AWSClusterSpecProviderCredentialSecret details how to chose the AWS IAM identity ARN
to use with this cluster.</p>
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
<p>Name is the name of the provider credential resoure.</p>
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
<p>Namespace is the kubernetes namespace that holds the provider credential.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProviderMaster">AWSClusterSpecProviderMaster
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterSpecProvider">AWSClusterSpecProvider</a>)
</p>
<p>
<p>AWSClusterSpecProviderMaster holds master node configuration details.</p>
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
<code>availabilityZone</code></br>
<em>
string
</em>
</td>
<td>
<p>AvailabilityZone is the AWS availability zone to place the master node in.</p>
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
<p>InstanceType specifies the AWS EC2 instance type to use for the master node.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterStatus">AWSClusterStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSCluster">AWSCluster</a>)
</p>
<p>
<p>AWSClusterStatus holds status information about the cluster, populated once the
cluster is in creation or created.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatus">
CommonClusterStatus
</a>
</em>
</td>
<td>
<p>Cluster provides cluster-specific status details, including conditions and versions.</p>
</td>
</tr>
<tr>
<td>
<code>provider</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatusProvider">
AWSClusterStatusProvider
</a>
</em>
</td>
<td>
<p>Provider provides provider-specific status details.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterStatusProvider">AWSClusterStatusProvider
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatus">AWSClusterStatus</a>)
</p>
<p>
<p>AWSClusterStatusProvider holds provider-specific status details.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatusProviderNetwork">
AWSClusterStatusProviderNetwork
</a>
</em>
</td>
<td>
<p>Network provides network-specific configuration details</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSClusterStatusProviderNetwork">AWSClusterStatusProviderNetwork
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatusProvider">AWSClusterStatusProvider</a>)
</p>
<p>
<p>AWSClusterStatusProviderNetwork holds network details.</p>
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
<p>IPv4 address block used by the tenant cluster, in CIDR notation.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSControlPlaneSpec">AWSControlPlaneSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSControlPlane">AWSControlPlane</a>)
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
[]string
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
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSControlPlaneStatus">AWSControlPlaneStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSControlPlane">AWSControlPlane</a>)
</p>
<p>
<p>TODO</p>
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
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpec">AWSMachineDeploymentSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeployment">AWSMachineDeployment</a>)
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
<code>nodePool</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePool">
AWSMachineDeploymentSpecNodePool
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProvider">
AWSMachineDeploymentSpecProvider
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePool">AWSMachineDeploymentSpecNodePool
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpec">AWSMachineDeploymentSpec</a>)
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
<code>machine</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePoolMachine">
AWSMachineDeploymentSpecNodePoolMachine
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
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePoolScaling">
AWSMachineDeploymentSpecNodePoolScaling
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePoolMachine">AWSMachineDeploymentSpecNodePoolMachine
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePool">AWSMachineDeploymentSpecNodePool</a>)
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
<code>dockerVolumeSizeGB</code></br>
<em>
int
</em>
</td>
<td>
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
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePoolScaling">AWSMachineDeploymentSpecNodePoolScaling
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecNodePool">AWSMachineDeploymentSpecNodePool</a>)
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
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProvider">AWSMachineDeploymentSpecProvider
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpec">AWSMachineDeploymentSpec</a>)
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
[]string
</em>
</td>
<td>
</td>
</tr>
<tr>
<td>
<code>worker</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProviderWorker">
AWSMachineDeploymentSpecProviderWorker
</a>
</em>
</td>
<td>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProviderWorker">AWSMachineDeploymentSpecProviderWorker
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSMachineDeploymentSpecProvider">AWSMachineDeploymentSpecProvider</a>)
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
<h3 id="infrastructure.giantswarm.io/v1alpha2.CommonClusterObject">CommonClusterObject
</h3>
<p>
<p>CommonClusterObject represents common interface for all provider specific
cluster objects.</p>
</p>
<h3 id="infrastructure.giantswarm.io/v1alpha2.CommonClusterStatus">CommonClusterStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.AWSClusterStatus">AWSClusterStatus</a>)
</p>
<p>
<p>CommonClusterStatus is shared type to contain provider independent cluster
status information.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusCondition">
[]CommonClusterStatusCondition
</a>
</em>
</td>
<td>
<p>One or several conditions that are currently applicable to the cluster.</p>
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
<p>Identifier of the cluster.</p>
</td>
</tr>
<tr>
<td>
<code>versions</code></br>
<em>
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusVersion">
[]CommonClusterStatusVersion
</a>
</em>
</td>
<td>
<p>Release versions the cluster used so far.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusCondition">CommonClusterStatusCondition
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatus">CommonClusterStatus</a>)
</p>
<p>
<p>CommonClusterStatusCondition explains the current condition(s) of the cluster.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>Time the condition occurred.</p>
</td>
</tr>
<tr>
<td>
<code>condition</code></br>
<em>
string
</em>
</td>
<td>
<p>Condition string, e. g. <code>Creating</code>, <code>Created</code>, <code>Upgraded</code></p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusGetSetter">CommonClusterStatusGetSetter
</h3>
<p>
<p>CommonClusterStatusGetSetter provides abstract way to manipulate common
provider independent cluster status field in provider CR&rsquo;s status.</p>
</p>
<h3 id="infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusVersion">CommonClusterStatusVersion
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatus">CommonClusterStatus</a>)
</p>
<p>
<p>CommonClusterStatusVersion informs which aws-operator version was/responsible for this cluster.</p>
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
<a href="#infrastructure.giantswarm.io/v1alpha2.DeepCopyTime">
DeepCopyTime
</a>
</em>
</td>
<td>
<p>Time the cluster assumed the given version.</p>
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
<p>The aws-operator version responsible for handling the cluster.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.DeepCopyTime">DeepCopyTime
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusCondition">CommonClusterStatusCondition</a>, 
<a href="#infrastructure.giantswarm.io/v1alpha2.CommonClusterStatusVersion">CommonClusterStatusVersion</a>)
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
<h3 id="infrastructure.giantswarm.io/v1alpha2.G8sControlPlaneSpec">G8sControlPlaneSpec
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.G8sControlPlane">G8sControlPlane</a>)
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
<p>Replicas is the number replicas of the master node.</p>
</td>
</tr>
<tr>
<td>
<code>infrastructureRef</code></br>
<em>
<a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.13/#objectreference-v1-core">
Kubernetes core/v1.ObjectReference
</a>
</em>
</td>
<td>
<p>InfrastructureRef is a required reference to provider-specific
Infrastructure.</p>
</td>
</tr>
</tbody>
</table>
<h3 id="infrastructure.giantswarm.io/v1alpha2.G8sControlPlaneStatus">G8sControlPlaneStatus
</h3>
<p>
(<em>Appears on:</em>
<a href="#infrastructure.giantswarm.io/v1alpha2.G8sControlPlane">G8sControlPlane</a>)
</p>
<p>
<p>G8sControlPlaneStatus defines the observed state of G8sControlPlane.</p>
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
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>Total number of non-terminated machines targeted by this control plane
(their labels match the selector).</p>
</td>
</tr>
<tr>
<td>
<code>readyReplicas</code></br>
<em>
int32
</em>
</td>
<td>
<em>(Optional)</em>
<p>Total number of fully running and ready control plane machines.</p>
</td>
</tr>
</tbody>
</table>
<hr/>
<p><em>
Generated with <code>gen-crd-api-reference-docs</code>
on git commit <code>29b580c</code>.
</em></p>
