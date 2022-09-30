---
linkTitle: Cluster API OpenStack
title: "'kubectl gs template cluster' command reference for CAPO"
description: How to create a manifest for a workload cluster using Cluster API provider OpenStack (CAPO) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-capo
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a CAPG cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with Cluster API provider OpenStack (also known as CAPO).

## Usage

Basic command syntax:

```nohighlight
kubectl gs template cluster \
  --provider capo \
  FLAGS
```

### Flags

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

### Examples

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

<details>
<summary>Show example output</summary>

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

</details>

## Output

Manifests for the following resources will be created:

- [`App (name=<cluster name>-cluster)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>)` - describes the configuration for the above cluster chart.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps)` - describes the configuration for the above preinstalled apps charts.
