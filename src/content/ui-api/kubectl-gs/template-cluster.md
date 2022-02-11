---
linkTitle: template cluster
title: "'kubectl gs template cluster' command reference"
description: Reference documentation on how to create a manifest for a Cluster using 'kubectl gs'.
weight: 90
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-cluster/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a cluster manifest for the Management API?
last_review_date: 2021-02-11
---

# `kubectl gs template cluster`

This command helps with creating a cluster by producing a manifest based on user input. This manifest can then optionally be modified and finally be applied to the Management API to create a cluster.

The outcome depends on the provider, set via the `--provider` flag.

{{< tabs >}}
{{< tab id="flags-aws" title="AWS">}}

For AWS (`--provider aws`):

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1alpha2`) - holds the base cluster specification.
- [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha2`) - holds AWS-specific configuration.
- [`G8sControlPlane`]({{< relref "/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha2`) - specifies the control plane nodes
- [`AWSControlPlane`]({{< relref "/ui-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha2`) - specifies the control plane nodes with AWS-specific details

{{< /tab >}}
{{< tab id="flags-azure" title="Azure">}}

For Azure (`--provider azure`):

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1alpha3`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1alpha3`) - holds Azure-specific configuration.
- [`AzureMachine`]({{< relref "/ui-api/management-api/crd/azuremachines.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1alpha3`) - specifies the control plane nodes.

{{< /tab >}}
{{< tab id="flags-capz" title="Cluster API on Azure">}}

We also support creating clusters on Azure using ClusterAPI by selecting our `v20.0.0-alpha1` release  (`--provider azure --release v20.0.0-alpha1`).
Please be aware that this is an early alpha release. Clusters created using this release won't be monitored by GiantSwarm and, they won't be able to be upgraded to newer stable releases.

In this case the outcome is a bit different:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`KubeadmControlPlane`]({{< relref "/ui-api/management-api/crd/kubeadmcontrolplanes.controlplane.cluster.x-k8s.io.md" >}}) (API version `controlplane.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the control plane nodes.
- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the bastion host specification.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the bastion host.

{{< /tab >}}
{{< tab id="flags-openstack" title="OpenStack (alpha)">}}

For OpenStack (`--provider openstack`):

- [`App (name=<cluster name>)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps)` - describes the configuration for the above preinstalled apps charts.

{{< /tab >}}
{{< /tabs >}}

**Note:** With the exception of OpenStack, the CRs generated by this command won't trigger the creation of any worker nodes. Please see the [template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool" >}}) for instructions on how to create worker node pools on all other providers.

## Usage

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (one of: `aws`, `azure`, or `openstack`).
- `--name` - Unique name of the cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` - Name of the organization that will own the cluster. Determines the namespace where resources will be created.
- `--release` (AWS and Azure only) - Workload cluster release version.
  Can be retrieved with `kubectl get releases` for your installation.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--pods-cidr` (optional) - CIDR applied to the pods. If this isn't provided, the installation default will be applied.
- `--label` (optional) - workload cluster label in the form of `key=value`. Can be specified multiple times.
- `--release-branch` (optional, AWS and Azure only) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s).
- `--output` (optional) - The name of the file to write the output to instead of stdout.

  On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

### AWS specific

- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html).

### OpenStack specific

- `--cloud` - Name of the cloud in the `cloud-config` secret. This is almost always "openstack".
- `--cloud-config` - Name of the `cloud-config` secret which defines the credentials for the OpenStack project in which the cluster should be created. This must be created in the organization namespace before creating a cluster.
- `--external-network-id` - UUID of the external network to be used. Only required if multiple external networks are available.
- `--failure-domain` - Failure domain of worker nodes.
- `--node-cidr` - CIDR defining the IP range of cluster nodes.
- `--node-image-uuid` - UUID of the root volume image source for the control plane and worker machines.
- `--bastion-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--bastion-disk-size` - Size of root volumes attached to the cluster bastion machine in gigabytes. Must be greater than or equal to the size of the bastion source image (`--bastion-image-uuid`).
- `--bastion-image-uuid` - UUID of the root volume image source for the bastion machine.
- `--control-plane-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--control-plane-disk-size` - Size of root volumes attached to each control plane node machine in gigabytes. Must be greater than or equal to the size of the node source image.
- `--control-plane-replicas` - Number of control plane replicas. This should be 1 for a non-HA control plane or 3 for an HA control plane (etcd requires an odd number of members).
- `--worker-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--worker-disk-size` - Size of root volumes attached to each worker node machine in gigabytes. Must be greater than or equal to the size of the node source image (`--node-image-uuid`).
- `--worker-replicas` - Number of replicas in the primary worker node pool.
- `--cluster-version` (optional) - Version of `cluster-openstack` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-version` (optional) - Version of `default-apps-openstack` helm chart to use. If not provided, the latest version will be used.
- `--dns-nameservers` (optional) - A list of DNS nameservers to be used to resolve external names.
- `--enable-oidc` (optional) - If `true`, the control plane will be configured to accept OIDC-based authentication and Dex will be deployed in the workload cluster to authenticate with.

## Examples

{{< tabs >}}
{{< tab id="command-examples-aws" title="AWS">}}

Example command for an AWS cluster:

```nohighlight
kubectl gs template cluster \
  --provider aws \
  --control-plane-az eu-central-1a \
  --external-snat true \
  --description "Cluster #2" \
  --pods-cidr 10.2.0.0/16 \
  --organization acme \
  --release 16.0.0 \
  --label environment=testing \
  --label team=upstate
```

{{< /tab >}}
{{< tab id="command-examples-azure" title="Azure">}}

```nohighlight
kubectl gs template cluster \
  --provider azure \
  --organization acme \
  --release 16.0.0 \
  --description "Test cluster" \
  --label environment=testing \
  --label team=upstate
```

{{< /tab >}}
{{< tab id="command-examples-openstack" title="OpenStack">}}

```nohighlight
kubectl gs template cluster \
  --provider openstack \
  --enable-oidc \
  --organization multi-project \
  --failure-domain us-east-1 \
  --cloud openstack \
  --cloud-config cloud-config-giantswarm-2 \
  --bastion-image-uuid 4b4bbad1-0eca-4937-9fe5-f5e767b36c5f \
  --node-image-uuid c3cc570d-cfd5-4cdb-aa46-fa82a6e72ecb \
  --external-network-id 0d2b02e2-6003-4c09-8457-604d0a963f7a \
  --node-cidr 10.6.0.0/24 \
  --bastion-machine-flavor a1.tiny \
  --control-plane-machine-flavor a1.small \
  --worker-machine-flavor a1.small \
  --control-plane-disk-size 50 \
  --worker-disk-size 50 \
  --name demo1
```

{{< /tab >}}
{{< /tabs >}}

## Output

The above example command would generate the following output:

{{< tabs >}}
{{< tab id="command-output-aws" title="AWS">}}

```yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/clusters.cluster.x-k8s.io/
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: ""
    environment: testing
    giantswarm.io/cluster: x5g6e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
    team: upstate
  name: x5g6e
  namespace: org-acme
spec:
  controlPlaneEndpoint:
    host: ""
    port: 0
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha3
    kind: AWSCluster
    name: x5g6e
    namespace: org-acme
status:
  controlPlaneInitialized: false
  infrastructureReady: false
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSCluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: ""
    cluster.x-k8s.io/cluster-name: x5g6e
    giantswarm.io/cluster: x5g6e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: x5g6e
  namespace: org-acme
spec:
  cluster:
    description: 'Cluster #2'
    dns:
      domain: ""
    kubeProxy: {}
    oidc:
      claims: {}
  provider:
    credentialSecret:
      name: ""
      namespace: giantswarm
    master:
      availabilityZone: eu-central-1a
      instanceType: m5.xlarge
    nodes: {}
    pods:
      cidrBlock: 10.2.0.0/16
      externalSNAT: true
    region: ""
status:
  cluster: {}
  provider:
    network: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: G8sControlPlane
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: ""
    giantswarm.io/cluster: x5g6e
    giantswarm.io/control-plane: wy76e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: wy76e
  namespace: org-acme
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha3
    kind: AWSControlPlane
    name: wy76e
    namespace: org-acme
  replicas: 1
status: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSControlPlane
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: ""
    giantswarm.io/cluster: x5g6e
    giantswarm.io/control-plane: wy76e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: wy76e
  namespace: org-acme
spec:
  availabilityZones:
  - eu-central-1a
  instanceType: m5.xlarge
```

{{< /tab >}}
{{< tab id="command-output-azure" title="Azure">}}

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureCluster
metadata:
  creationTimestamp: null
  labels:
    cluster.x-k8s.io/cluster-name: tt0m5
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: tt0m5
  namespace: org-acme
spec:
  controlPlaneEndpoint:
    host: ""
    port: 0
  location: ""
  networkSpec:
    apiServerLB:
      frontendIPs:
      - name: tt0m5-API-PublicLoadBalancer-Frontend
      name: tt0m5-API-PublicLoadBalancer
      sku: Standard
      type: Public
    vnet:
      name: ""
  resourceGroup: tt0m5
status:
  ready: false
---
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:
    cluster.giantswarm.io/description: Test cluster
  creationTimestamp: null
  labels:
    cluster.x-k8s.io/cluster-name: tt0m5
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: tt0m5
  namespace: org-acme
spec:
  controlPlaneEndpoint:
    host: ""
    port: 0
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
    kind: AzureCluster
    name: tt0m5
    namespace: org-acme
status:
  controlPlaneInitialized: false
  infrastructureReady: false
---
apiVersion: infrastructure.cluster.x-k8s.io/v1alpha3
kind: AzureMachine
metadata:
  creationTimestamp: null
  labels:
    cluster.x-k8s.io/cluster-name: tt0m5
    cluster.x-k8s.io/control-plane: "true"
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 16.0.0
  name: tt0m5-master-0
  namespace: org-acme
spec:
  availabilityZone: {}
  image:
    marketplace:
      offer: flatcar-container-linux-free
      publisher: kinvolk
      sku: stable
      thirdPartyImage: false
      version: 2345.3.1
  location: ""
  osDisk:
    cachingType: ReadWrite
    diskSizeGB: 50
    managedDisk:
      storageAccountType: Premium_LRS
    osType: Linux
  sshPublicKey: ""
  vmSize: Standard_D4s_v3
status:
  ready: false
```

{{< /tab >}}
{{< tab id="command-output-openstack" title="OpenStack">}}

```yaml
---
apiVersion: v1
data:
  values: |
    bastion:
      flavor: a1.tiny
      image: ""
      rootVolume:
        diskSize: 10
        sourceUUID: 4b4bbad1-0eca-4937-9fe5-f5e767b36c5f
    cloudConfig: cloud-config-giantswarm-2
    cloudName: openstack
    controlPlane:
      diskSize: 50
      machineFlavor: a1.small
      replicas: 1
    externalNetworkID: 0d2b02e2-6003-4c09-8457-604d0a963f7a
    nodeCIDR: 10.6.0.0/24
    nodeClasses:
    - diskSize: 50
      machineFlavor: a1.small
      name: default
    nodePools:
    - class: default
      name: default
      replicas: 2
    oidc:
      enabled: true
    organization: multi-project
    rootVolume:
      enabled: true
      sourceUUID: c3cc570d-cfd5-4cdb-aa46-fa82a6e72ecb
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: demo1-userconfig
  namespace: org-multi-project
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: demo1
  namespace: org-multi-project
spec:
  catalog: giantswarm
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: cluster-openstack
  namespace: org-multi-project
  userConfig:
    configMap:
      name: demo1-userconfig
      namespace: org-multi-project
  version: 0.4.0
---
apiVersion: v1
data:
  values: |
    clusterName: demo1
    oidc:
      enabled: true
    organization: multi-project
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: demo1-default-apps-userconfig
  namespace: org-multi-project
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: demo1-default-apps
  namespace: org-multi-project
spec:
  catalog: giantswarm
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: default-apps-openstack
  namespace: org-multi-project
  userConfig:
    configMap:
      name: demo1-default-apps-userconfig
      namespace: org-multi-project
  version: 0.1.0
```

{{< /tab >}}
{{< /tabs >}}
