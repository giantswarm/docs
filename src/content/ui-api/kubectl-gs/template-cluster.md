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
last_review_date: 2021-01-01
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
{{< /tabs >}}

**Note:** The CRs generated won't trigger the creation of any worker nodes. Please see the [template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool" >}}) for instructions on how to create worker node pools.

## Usage

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (either `aws` or `azure`).
- `--name` - Unique identifier of the cluster.
- `--organization` - Name of the organization that will "own" the cluster.
- `--release` - valid workload cluster release version.
  Can be retrieved with `gsctl list releases` for your installation. Only versions above *10.x.x*+ support cluster CRs.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--pods-cidr` (optional) - CIDR applied to the pods. If you don't set any, the installation default will be applied. Only versions *11.1.4+ support this feature.
- `--label` (optional) - workload cluster label in the form of `key=value`. Can be specified multiple times. Only clusters with workload cluster release version above *10.x.x*+ support workload cluster labels.
- `--release-branch` (optional) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s).

  On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

### AWS specific

- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html). Only versions *11.3.1+ support this feature.

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
{{< /tabs >}}
