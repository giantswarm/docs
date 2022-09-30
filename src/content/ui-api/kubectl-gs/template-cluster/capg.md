---
linkTitle: Cluster API GCP
title: "'kubectl gs template cluster' command reference for GCP"
description: How to create a manifest for a workload cluster using Cluster API provider GCP (CAPG) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-capg
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a CAPG cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with Cluster API provider GCP (also known as CAPG).

## Usage

Basic command syntax:

```nohighlight
kubectl gs template cluster \
  --provider gcp \
  FLAGS
```

### Flags

Common flags:

{{% kubectl-gs/template_cluster_common_flags %}}

Flags specific to GCP:

- `--gcp-project` -- GCP project where the cluster will be deployed. (required)
- `--region` -- GCP region where the cluster will be deployed. (required)
- `--gcp-failure-domains` -- GCP zones where the cluster's control-plane nodes will be deployed. (required)
- `--gcp-control-plane-sa-email` -- The GCP Service Account which the control-plane nodes will use (default: "default").
- `--gcp-control-plane-sa-scopes` -- The GCP API scopes the control-plane will have access to (default: `https://www.googleapis.com/auth/compute`).
- `--gcp-machine-deployment-name` -- The name of the MachineDeployment (default: `worker1`).
- `--gcp-machine-deployment-instance-type` -- The GCP Instance Type for the default node pool instances (default: `n1-standard-2`).
- `--gcp-machine-deployment-failure-domain` -- The GCP zones where the cluster's default node pool will be deployed. (default: `europe-west6-a`).
- `--gcp-machine-deployment-replicas` -- The number of nodes in the default node pool (default: 3).
- `--gcp-machine-deployment-disk-size` -- The node disk size in GB for the default node pool (default: 100).
- `--version` -- Version of the [cluster-gcp](https://github.com/giantswarm/cluster-gcp/releases) app to use. If not specified, the latest one will be used. In this case, an authenticated kubectl context is required for communication with the management API.

**Note:** The zones where the worker and control-plane nodes are deployed must be in the same region as specified in the `--region` flag.

### Examples

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

<details>
<summary>Show example output</summary>

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

</details>

## Output

Manifests for the following resources will be created:

- [`App (name=<cluster name>)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>-userconfig)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps-userconfig)` - describes the configuration for the above preinstalled apps charts.
