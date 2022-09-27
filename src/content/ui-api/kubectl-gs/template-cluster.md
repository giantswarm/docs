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
last_review_date: 2022-09-26
---

This command helps with creating a cluster by producing a manifest based on user input. This manifest can then optionally be modified and finally be applied to the Management API to create a cluster.

The outcome depends on the provider, set via the `--provider` flag.

{{< tabs >}}
{{< tab id="flags-aws" title="AWS">}}

For AWS (`--provider aws`):

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - holds AWS-specific configuration.
- [`G8sControlPlane`]({{< relref "/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes
- [`AWSControlPlane`]({{< relref "/ui-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes with AWS-specific details

{{< /tab >}}
{{< tab id="flags-aws-capa" title="AWS CAPI">}}

For AWS CAPI (`--provider capa`):

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`KubeadmControlPlane`]({{< relref "/ui-api/management-api/crd/kubeadmcontrolplanes.controlplane.cluster.x-k8s.io.md" >}}) (API version `controlplane.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the bastion host specification.
- [`MachinePool`]({{< relref "/ui-api/management-api/crd/machinepools.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - worker nodes machine pools.


{{< /tab >}}
{{< tab id="flags-azure" title="Azure">}}

For Azure (`--provider azure`):

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`AzureMachine`]({{< relref "/ui-api/management-api/crd/azuremachines.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.

{{< /tab >}}
{{< tab id="flags-capz" title="Cluster API on Azure">}}

We also support creating clusters on Azure using ClusterAPI by selecting our `v20.0.0-alpha1` release  (`--provider azure --release v20.0.0-alpha1`).
Please be aware that this is an early alpha release. Clusters created using this release won't be monitored by Giant Swarm and, they won't be able to be upgraded to newer stable releases.

In this case the outcome is a bit different:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`KubeadmControlPlane`]({{< relref "/ui-api/management-api/crd/kubeadmcontrolplanes.controlplane.cluster.x-k8s.io.md" >}}) (API version `controlplane.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the control plane nodes.
- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the bastion host specification.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the bastion host.

{{< /tab >}}
{{< tab id="flags-gcp" title="GCP (alpha)">}}

For Google Cloud Platform (`--provider gcp`):

- [`App (name=<cluster name>)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>-userconfig)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps-userconfig)` - describes the configuration for the above preinstalled apps charts.

{{< /tab >}}
{{< tab id="flags-openstack" title="OpenStack (alpha)">}}

For OpenStack (`--provider openstack`):

- [`App (name=<cluster name>-cluster)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps)` - describes the configuration for the above preinstalled apps charts.

{{< /tab >}}
{{< /tabs >}}

**Note:** For OpenStack and GCP one default nodepool will be created. For the othe providers, the CRs generated by this command won't trigger the creation of any worker nodes. Please see the [template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool" >}}) for instructions on how to create worker node pools on all other providers.

## Usage

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (one of: `aws`, `azure`, `capa`, `gcp`, or `openstack`).
- `--name` - Unique name of the cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` - Name of the organization that will own the cluster. Determines the namespace where resources will be created.
- `--release` (non CAPI AWS and Azure only) - Workload cluster release version.
  Can be retrieved with `kubectl get releases` for your installation.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--pods-cidr` (optional and non CAPI AWS) - CIDR applied to the pods. If this isn't provided, the installation default will be applied.
- `--label` (optional and non CAPI AWS) - workload cluster label in the form of `key=value`. Can be specified multiple times.
- `--service-priority` (optional and non CAPI AWS) - [Service priority]({{< relref "/advanced/labelling-workload-clusters#service-priority" >}}) of the cluster (one of: `highest`, `medium`, or `lowest`; default: `highest`).
- `--release-branch` (optional and non CAPI AWS and Azure only) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s).
- `--output` (optional) - The name of the file to write the output to instead of stdout.

  On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

### AWS specific (CAPI)

 - `--name` must only contain alphanumeric characters, start with a letter, and be no longer than 5 characters in length

### AWS specific (non CAPI)

- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html).

### GCP specific

- `--gcp-project` - The Google Cloud Platform project where the cluster will be deployed.
- `--region` - The Google Cloud Platform region where the cluster will be deployed.
- `--gcp-failure-domains` - The Google Cloud Platform zones where the cluster's control-plane nodes will be deployed.
- `--gcp-control-plane-sa-email` (optional) - The Google Cloud Platform Service Account which the control-plane nodes will use (default: "default").
- `--gcp-control-plane-sa-scopes` (optional) - The Google Cloud Platform API scopes the control-plane will have access to (default: `https://www.googleapis.com/auth/compute`).
- `--gcp-machine-deployment-name` (optional) - The name of the MachineDeployment (default: `worker1`).
- `--gcp-machine-deployment-instance-type` (optional) - The Google Cloud Platform Instance Type for the default nodepool isntances (default: `n1-standard-2`).
- `--gcp-machine-deployment-failure-domain` (optional) - The Google Cloud Platform zones where the cluster's default nodepool will be deployed. (default: `europe-west6-a`).
- `--gcp-machine-deployment-replicas` (optional) - The number of nodes in the default nodepool (default: 3).
- `--gcp-machine-deployment-disk-size` (optional) - The node disk size in GB for the default nodepool (default: 100).

**Note:** The zones where the worker and control-plane nodes are deployed must be in the same region specified in the `--region` flag.

### OpenStack specific

- `--cluster-version` (optional) - Version of `cluster-openstack` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-version` (optional) - Version of `default-apps-openstack` helm chart to use. If not provided, the latest version will be used.
- `--cloud` - Name of the cloud in the `cloud-config` secret. This is almost always "openstack".
- `--cloud-config` - Name of the `cloud-config` secret which defines the credentials for the OpenStack project in which the cluster should be created. This must be created in the organization namespace before creating a cluster.
- `--dns-nameservers` (optional) - A list of DNS nameservers to be used to resolve external names.
- `--external-network-id` - UUID of the external network to be used. Only required if multiple external networks are available.
- `--node-cidr` - CIDR defining the IP range of cluster nodes. When used, new network and subnet will be created.
- `--network-name` (optional) - Name of existing network for the cluster. Can be used when `--node-cidr` is empty. 
- `--subnet-name` (optional) - Name of existing subnet for the cluster. Can be used when `--node-cidr` is empty. 
- `--bastion-boot-from-volume` - If true, bation machine will use a persistent root volume instead of an ephemeral volume.
- `--bastion-disk-size` - Size of root volume attached to the cluster bastion machine in gigabytes. Must be greater than or equal to the size of the bastion source image (`--bastion-image`).
- `--bastion-image` - Bastion image name or root volume source UUID if --bastion-boot-from-volume is set.
- `--bastion-machine-flavor` - Flavor (a.k.a. size) of the bastion machine.
- `--control-plane-boot-from-volume` - If true, control plane machine(s) will use a persistent root volume instead of an ephemeral volume.
- `--control-plane-disk-size` - Size of root volumes attached to each control plane node machine in gigabytes. Must be greater than or equal to the size of the node source image.
- `--control-plane-image` - Control plane image name or root volume source UUID if --control-plane-boot-from-volume is set.
- `--control-plane-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--control-plane-replicas` - Number of control plane replicas. This should be 1 for a non-HA control plane or 3 for an HA control plane (etcd requires an odd number of members).
- `--oidc-issuer-url` (optional) - This is the issuer URL for configuring OpenID connect in the cluster API.
- `--oidc-ca-file` (optional) - This is the CA file path in case is not used a trusted Certificate Authority for OIDC endpoint.
- `--oidc-client-id` (optional) - This is the client ID that is configured in the OIDC endpoint.
- `--oidc-username-claim` (optional) - This is the claim used to map the username identity of the user.
- `--oidc-groups-claim` (optional) - This is the claim used to map the group identity of the user.
- `--worker-boot-from-volume` - If true, worker machines will use a persistent root volume instead of an ephemeral volume.
- `--worker-disk-size` - Size of root volumes attached to each worker node machine in gigabytes. Must be greater than or equal to the size of the node source image (`--worker-image`).
- `--worker-failure-domain` - Failure domain of worker nodes.
- `--worker-image` - Worker image name or root volume source UUID if --worker-boot-from-volume is set.
- `--worker-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--worker-replicas` - Number of replicas in the primary worker node pool.

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
  --release 17.0.0 \
  --label environment=testing \
  --label team=upstate \
  --service-priority lowest
```

{{< /tab >}}
{{< tab id="command-examples-aws-capi" title="AWS CAPI">}}

Example command for an AWS CAPI cluster:

```nohighlight
kubectl gs template cluster \
  --provider capa \  
  --control-plane-az eu-central-1a \  
  --description "Development Cluster" \  
  --name dev01
  --organization acme
```

{{< /tab >}}
{{< tab id="command-examples-azure" title="Azure">}}

```nohighlight
kubectl gs template cluster \
  --provider azure \
  --organization acme \
  --release 17.0.0 \
  --description "Test cluster" \
  --label environment=testing \
  --label team=upstate \
  --service-priority lowest
```
{{< /tab >}}
{{< tab id="command-examples-gcp" title="GCP">}}

```nohighlight
kubectl gs template cluster \
  --provider gcp \
  --name demo1 \
  --organization demo \
  --region europe-west3 \
  --gcp-project project-1234 \
  --gcp-failure-domains europe-west3-a \
  --gcp-machine-deployment-failure-domain europe-west3-a \
  --description "a test cluster" \
  --gcp-control-plane-sa-email "test-service-account@project-1234.iam.gserviceaccount.com"
```

{{< /tab >}}

{{< tab id="command-examples-openstack" title="OpenStack">}}

```nohighlight
kubectl gs template cluster \
  --provider openstack \
  --name demo1 \
  --organization multi-project \
  --cloud openstack \
  --cloud-config cloud-config-giantswarm-2 \
  --external-network-id 12345678-abcd-1234-abcd-1234567890ef \
  --node-cidr 10.6.0.0/24 \
  --bastion-boot-from-volume \
  --bastion-disk-size 50 \
  --bastion-image 12345678-abcd-1234-abcd-1234567890ab \
  --bastion-machine-flavor a1.tiny \
  --control-plane-az us-east-1 \
  --control-plane-boot-from-volume \
  --control-plane-disk-size 50 \
  --control-plane-image 12345678-abcd-1234-abcd-1234567890cd \
  --control-plane-machine-flavor a1.small \
  --worker-boot-from-volume \
  --worker-disk-size 50 \
  --worker-failure-domain us-east-1 \
  --worker-image 12345678-abcd-1234-abcd-1234567890gh \
  --worker-machine-flavor a1.small \
  --worker-replicas 3
```

{{< /tab >}}
{{< /tabs >}}

## Output

The above example command would generate the following output:

{{< tabs >}}
{{< tab id="command-output-aws" title="AWS">}}

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/clusters.cluster.x-k8s.io/
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: 3.13.0
    cluster.x-k8s.io/cluster-name: x5g6e
    environment: testing
    giantswarm.io/cluster: x5g6e
    giantswarm.io/organization: acme
    giantswarm.io/service-priority: lowest
    release.giantswarm.io/version: 17.0.0
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
    aws-operator.giantswarm.io/version: 10.17.0
    cluster.x-k8s.io/cluster-name: x5g6e
    giantswarm.io/cluster: x5g6e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
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
    cluster-operator.giantswarm.io/version: 3.13.0
    cluster.x-k8s.io/cluster-name: x5g6e
    giantswarm.io/cluster: x5g6e
    giantswarm.io/control-plane: wy76e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
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
    aws-operator.giantswarm.io/version: 10.17.0
    cluster.x-k8s.io/cluster-name: x5g6e
    giantswarm.io/cluster: x5g6e
    giantswarm.io/control-plane: wy76e
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
  name: wy76e
  namespace: org-acme
spec:
  availabilityZones:
  - eu-central-1a
  instanceType: m5.xlarge
```

{{< /tab >}}
{{< tab id="command-output-aws-capi" title="AWS CAPI">}}
```yaml
---
apiVersion: v1
data:
  values: |
    aws: {}
    bastion: {}
    clusterDescription: Test Cluster
    clusterName: dev01
    controlPlane:
      replicas: 3
    machinePools:
    - availabilityZones:
      - eu-central-1a
      instanceType: m5.xlarge
      maxSize: 10
      minSize: 3
      name: machine-pool0
      rootVolumeSizeGB: 300
    network:
      availabilityZoneUsageLimit: 3
    organization: acme
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: dev01
  name: dev01-userconfig
  namespace: org-acme
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: dev01
  namespace: org-acme
spec:
  catalog: cluster
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
  name: cluster-aws
  namespace: org-acme
  userConfig:
    configMap:
      name: dev01-userconfig
      namespace: org-acme
  version: 0.9.2
---
apiVersion: v1
data:
  values: |
    clusterName: dev01
    organization: acme
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: dev01
  name: dev01-default-apps-userconfig
  namespace: org-acme
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: dev01-default-apps
  namespace: org-acme
spec:
  catalog: cluster
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
  name: default-apps-aws
  namespace: org-acme
  userConfig:
    configMap:
      name: dev01-default-apps-userconfig
      namespace: org-acme
  version: 0.5.4
```
{{< /tab >}}
{{< tab id="command-output-azure" title="Azure">}}

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureCluster
metadata:
  creationTimestamp: null
  labels:
    azure-operator.giantswarm.io/version: 5.17.0
    cluster.x-k8s.io/cluster-name: tt0m5
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
  name: tt0m5
  namespace: org-acme
spec:
  bastionSpec: {}
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
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  annotations:
    cluster.giantswarm.io/description: Test cluster
  creationTimestamp: null
  labels:
    azure-operator.giantswarm.io/version: 5.17.0
    cluster-operator.giantswarm.io/version: 3.12.0
    cluster.x-k8s.io/cluster-name: tt0m5
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    giantswarm.io/service-priority: lowest
    release.giantswarm.io/version: 17.0.0
  name: tt0m5
  namespace: org-acme
spec:
  controlPlaneEndpoint:
    host: ""
    port: 0
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: AzureCluster
    name: tt0m5
    namespace: org-acme
status:
  controlPlaneInitialized: false
  infrastructureReady: false
---
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureMachine
metadata:
  creationTimestamp: null
  labels:
    azure-operator.giantswarm.io/version: 5.17.0
    cluster.x-k8s.io/cluster-name: tt0m5
    cluster.x-k8s.io/control-plane: "true"
    giantswarm.io/cluster: tt0m5
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 17.0.0
  name: tt0m5-master-0
  namespace: org-acme
spec:
  image:
    marketplace:
      offer: flatcar-container-linux-free
      publisher: kinvolk
      sku: stable
      thirdPartyImage: false
      version: 2345.3.1
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
{{< tab id="command-output-gcp" title="GCP">}}

```yaml
---
apiVersion: v1
data:
  values: |
    clusterDescription: a test cluster
    clusterName: demo1
    controlPlane:
      replicas: 3
      serviceAccount:
        email: test-service-account@project-1234.iam.gserviceaccount.com
        scopes:
        - https://www.googleapis.com/auth/compute
    gcp:
      failureDomains:
      - europe-west3-a
      project: project-1234
      region: europe-west3
    machineDeployments:
    - failureDomain: europe-west3-a
      instanceType: n1-standard-2
      name: worker0
      replicas: 3
      rootVolumeSizeGB: 100
    organization: demo
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: demo1
  name: demo1-userconfig
  namespace: org-demo
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: demo1
  namespace: org-demo
spec:
  catalog: cluster
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
  name: cluster-gcp
  namespace: org-demo
  userConfig:
    configMap:
      name: demo1-userconfig
      namespace: org-demo
  version: 0.14.3
---
apiVersion: v1
data:
  values: |
    clusterName: demo1
    organization: demo
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: demo1
  name: demo1-default-apps-userconfig
  namespace: org-demo
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: demo1-default-apps
  namespace: org-demo
spec:
  catalog: cluster
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
  name: default-apps-gcp
  namespace: org-demo
  userConfig:
    configMap:
      name: demo1-default-apps-userconfig
      namespace: org-demo
  version: 0.9.0
```

{{< /tab >}}
{{< tab id="command-output-openstack" title="OpenStack">}}

```yaml
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo1-cluster-userconfig
  namespace: org-multi-project
data:
  values: |
    bastion:
      bootFromVolume: true
      diskSize: 10
      flavor: a1.tiny
      image: 12345678-abcd-1234-abcd-1234567890ab
    cloudConfig: cloud-config-giantswarm-2
    cloudName: openstack
    clusterName: demo1
    controlPlane:
      bootFromVolume: true
      diskSize: 50
      flavor: a1.small
      image: 12345678-abcd-1234-abcd-1234567890cd
      replicas: 1
    externalNetworkID: 12345678-abcd-1234-abcd-1234567890ef
    kubernetesVersion: v1.20.9
    nodeCIDR: 10.6.0.0/24
    nodeClasses:
    - bootFromVolume: true
      diskSize: 50
      flavor: a1.small
      image: 12345678-abcd-1234-abcd-1234567890gh
      name: default
    nodePools:
    - class: default
      failureDomain: us-east-1
      name: default
      replicas: 3
    oidc:
      enabled: false
    organization: multi-project
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
  name: demo1-cluster
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
      name: demo1-cluster-userconfig
      namespace: org-multi-project
  version: 0.5.0
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: demo1-default-apps-userconfig
  namespace: org-multi-project
data:
  values: |
    clusterName: demo1
    oidc:
      enabled: false
    organization: multi-project
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
  version: 0.1.1
```

{{< /tab >}}
{{< /tabs >}}
