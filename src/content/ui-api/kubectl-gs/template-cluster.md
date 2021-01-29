---
title: "'kubectl gs template cluster' command reference"
description: Reference documentation on how to create a manifest for a Cluster using 'kubectl gs'.
weight: 10
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `kubectl gs template cluster`

{{% kgs_alias_assumption %}}

This command helps with creating a cluster by producing a manifest based on user input. This manifest can then optionally be modified and finally be applied to the Management API to create a cluster.

The outcome depends on the provider, set via the `--provider` flag:

For AWS (`--provider aws`):

- [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) (API version `cluster.x-k8s.io/v1alpha2`) - holds the base cluster specification.
- [`AWSCluster`](/reference/management-api/awsclusters.infrastructure.giantswarm.io/) (API version `infrastructure.giantswarm.io/v1alpha2`) - holds AWS-specific configuration.
- [`G8sControlPlane`](/reference/management-api/g8scontrolplanes.infrastructure.giantswarm.io/) (API version `infrastructure.giantswarm.io/v1alpha2`) - specifies the master nodes
- [`AWSControlPlane`](/reference/management-api/awscontrolplanes.infrastructure.giantswarm.io/) (API version `infrastructure.giantswarm.io/v1alpha2`) - specifies the master nodes with AWS-specific details

For Azure (`--provider azure`):

- [`Cluster`](/reference/management-api/clusters.cluster.x-k8s.io/) (API version `cluster.x-k8s.io/v1alpha3`) - holds the base cluster specification.
- [`AzureCluster`](/reference/management-api/azureclusters.infrastructure.cluster.x-k8s.io/) (API version `infrastructure.cluster.x-k8s.io/v1alpha3`) - holds Azure-specific configuration.
- [`AzureMachine`](/reference/management-api/azuremachines.infrastructure.cluster.x-k8s.io/) (API version `infrastructure.cluster.x-k8s.io/v1alpha3`) - specifies the master nodes.

**Note:** The CRs generated won't trigger the creation of any worker nodes. Please see the [template nodepool](/reference/kubectl-gs/template-nodepool/) for instructions on how to create worker node pools.

## Usage

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (either `aws` or `azure`)
- `--name` - cluster name.
- `--pods-cidr` - CIDR applied to the pods. If you don't set any, the installation default will be applied. Only versions *11.1.4+ support this feature.
- `--owner` - organization, owning workload cluster. Must be configured with existing organization in installation.
- `--release` - valid workload cluster release version.
  Can be retrieved with `gsctl list releases` for your installation. Only versions above *10.x.x*+ support cluster CRs.
- `--label` - workload cluster label in the form of `key=value`. Can be specified multiple times. Only clusters with workload cluster release version above *10.x.x*+ support workload cluster labels.
- `--cluster-id` (optional) - Unique cluster identifier. Must me 5 characters in length, must contain numbers and letters, and match the regular expression `[a-z0-9]{5}`. If not given, an ID will be generated.
- `--release-branch` (optional) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--master-az` - Availability zone(s) of master instance.

  On AWS, it must be configured with AZ of the installation region. E.g. for region *eu-central-1* valid value is *eu-central-1a*.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one master node (on both Azure and AWS). For master node high availability,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

### AWS specific

- `--domain` - base domain of your installation. Customer solution engineer can provide this value.
- `--credential` - AWS cloud credentials that point to the AWS account used to spin up the cluster resources. To get this info run against the Control Plane API `kubectl -n giantswarm get secret -oyaml | grep ORG_NAME -A2 | tail -n 1 | awk '{print $2}'` replacing `ORG_NAME` for the name of the organization selected.
- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html). Only versions *11.3.1+ support this feature.

## Example

Example command for an AWS cluster:

```nohighlight
kgs template cluster \
  --provider aws
  --master-az eu-central-1a \
  --domain gauss.eu-central-1.aws.gigantic.io \
  --external-snat true \
  --name "Cluster #2" \
  --pods-cidr 10.2.0.0/16 \
  --owner acme \
  --credential credential-34hg5 \
  --release 11.2.1 \
  --label environment=testing \
  --label "team=upstate"
```

## Output

The above example command would generate the following output:

```yaml
apiVersion: cluster.x-k8s.io/v1alpha2
kind: Cluster
metadata:
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: 2.1.10
    giantswarm.io/cluster: o4omf
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.2.1
    environment: testing
    team: upstate
  name: o4omf
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSCluster
    name: o4omf
    namespace: default
status:
  controlPlaneInitialized: false
  infrastructureReady: false
---
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSCluster
metadata:
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: 8.4.0
    giantswarm.io/cluster: o4omf
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.2.1
  name: o4omf
  namespace: default
spec:
  cluster:
    description: 'Cluster #2'
    dns:
      domain: gauss.eu-central-1.aws.gigantic.io
    oidc:
      claims:
        groups: ""
        username: ""
      clientID: ""
      issuerURL: ""
  provider:
    credentialSecret:
      name: credential-34hg5
      namespace: giantswarm
    master:
      availabilityZone: eu-central-1a
      instanceType: m5.xlarge
    pods:
      cidrBlock: 10.2.0.0/16
      externalSNAT: true
    region: ""
status:
  cluster:
    id: ""
  provider:
    network:
      cidr: ""
---
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: G8sControlPlane
metadata:
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: 2.1.10
    giantswarm.io/cluster: o4omf
    giantswarm.io/control-plane: osss7
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.2.1
  name: osss7
  namespace: default
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha2
    kind: AWSControlPlane
    name: osss7
    namespace: default
  replicas: 1
status: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha2
kind: AWSControlPlane
metadata:
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: 8.4.0
    giantswarm.io/cluster: o4omf
    giantswarm.io/control-plane: osss7
    giantswarm.io/organization: acme
    release.giantswarm.io/version: 11.2.1
  name: osss7
  namespace: default
spec:
  availabilityZones:
  - eu-central-1a
  instanceType: m5.xlarge
status: {}
```
