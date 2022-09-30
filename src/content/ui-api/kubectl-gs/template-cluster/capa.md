---
linkTitle: Cluster API AWS
title: "'kubectl gs template cluster' command reference for CAPA"
description: How to create a manifest for a workload cluster using Cluster API provider AWS (CAPA) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-capa
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a CAPA cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with Cluster API provider AWS (also known as CAPA).

## Usage

Basic command syntax:

```nohighlight
kubectl gs template cluster \
  --provider capa \
  FLAGS
```

### Flags

- `--name` -- Name of the workload cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` -- Name of the organization that will own the cluster. Determines the namespace where resources will be created. (required)
- `--description` -- User-friendly description of the cluster's purpose. (recommended)
- `--control-plane-az` -- Availability zone(s) of the control plane instance(s).
- `--output` -- The name of the file to write the output. If not specified, manifests will be written to stdout.

### Examples

```nohighlight
kubectl gs template cluster \
  --provider capa \
  --organization acme \
  --name dev01 \
  --description "Development Cluster"
```

<details>
<summary>Show example output</summary>

```yaml
---
apiVersion: v1
data:
  values: |
    aws: {}
    bastion: {}
    clusterDescription: Development Cluster
    clusterName: dev01
    controlPlane:
      replicas: 3
    machinePools:
    - instanceType: m5.xlarge
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

</details>

## Output

Manifests for the following resources will be created:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`KubeadmControlPlane`]({{< relref "/ui-api/management-api/crd/kubeadmcontrolplanes.controlplane.cluster.x-k8s.io.md" >}}) (API version `controlplane.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the bastion host specification.
- [`MachinePool`]({{< relref "/ui-api/management-api/crd/machinepools.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - worker nodes machine pools.
- [`App (name=<cluster name>)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>-userconfig)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps-userconfig)` - describes the configuration for the above preinstalled apps charts.
