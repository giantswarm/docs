---
linkTitle: Azure
title: "'kubectl gs template cluster' command reference for Azure"
description: How to create a manifest for a workload cluster on Azure (before Cluster API) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-azure
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create an Azure cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with Azure.

**Note:** If you want to create Cluster API compatible cluster resources, please head to the page on [Cluster API provider Azure (CAPZ)]({{< relref "/ui-api/kubectl-gs/template-cluster/capz" >}}).

## Usage

Basic command syntax:

```nohighlight
kubectl gs template cluster \
  --provider azure \
  FLAGS
```

### Flags

{{% kubectl-gs/template_cluster_common_flags %}}
{{% kubectl-gs/template_cluster_common_flags_vintage %}}

TODO: Verify if all these flags are usable on Azure.

**Note:** Please use these numbers to specify availability zones: `1`, `2`, `3`.

### Examples

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

<details>
<summary>Show example output</summary>

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

</details>

## Output

Manifests for the following resources will be created:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`AzureMachine`]({{< relref "/ui-api/management-api/crd/azuremachines.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.

**Note:** The cluster created based on these resources **won't have any worker nodes**. Please see the [template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool" >}}) command for instructions on how to create node pools.
