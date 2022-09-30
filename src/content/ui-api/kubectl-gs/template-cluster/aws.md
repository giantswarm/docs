---
linkTitle: AWS
title: "'kubectl gs template cluster' command reference for AWS"
description: How to create a manifest for a workload cluster on AWS (before Cluster API) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-aws
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create an AWS cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with AWS.

**Note:** If you want to create Cluster API compatible resources, please head to the page on [Cluster API provider AWS (CAPA)]({{< relref "/ui-api/kubectl-gs/template-cluster/capa" >}}).

## Usage

Basic command syntax:

```nohighlight
kubectl gs template cluster \
  --provider aws \
  FLAGS
```

### Flags

- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html).

### Examples

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

<details>
<summary>Show example output</summary>

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

</details>

## Output

Manifests for the following resources will be created:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - holds AWS-specific configuration.
- [`G8sControlPlane`]({{< relref "/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes
- [`AWSControlPlane`]({{< relref "/ui-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes with AWS-specific details

**Note:** The cluster created based on these resources **won't have any worker nodes**. Please see the [template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool" >}}) command for instructions on how to create node pools.
