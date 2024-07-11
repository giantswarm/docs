---
linkTitle: template cluster
title: "'kubectl gs template cluster' command reference"
description: Reference documentation on how to create a manifest for a Cluster using 'kubectl gs'.
weight: 90
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /use-the-api/kubectl-gs
  - /reference/kubectl-gs/template-cluster/
  - /ui-api/kubectl-gs/template-cluster/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create a cluster manifest for the Management API?
last_review_date: 2024-06-10
---

This command helps with creating a cluster by producing a manifest based on user input. This manifest can then optionally be modified and finally be applied to the Management API to create a cluster.

The outcome depends on the provider, set via the `--provider` flag.

{{< tabs >}}
{{< tab id="flags-capi" for-impl="capi_any">}}

For CAPI providers (`--provider {capa,capv,capvcd,capz,eks,...}`):

- [`App (name=<cluster name>)`]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the actual cluster resources.
- `ConfigMap (name=<cluster name>-userconfig)` - describes the configuration for the above cluster chart. Please see [Creating a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}) for which cluster chart is used, depending on the cloud provider.
- [`App (name=<cluster name>-default-apps)`]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) (API version `application.giantswarm.io/v1alpha1`) - describes the Giant Swarm App which defines the helm release which in turn creates the preinstalled apps which run in the workload cluster.
- `ConfigMap (name=<cluster name>-default-apps-userconfig)` - describes the configuration for the above preinstalled apps charts. Please see [Creating a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}) for which default apps chart is used, depending on the cloud provider.

{{< /tab >}}
{{< tab id="flags-aws" for-impl="vintage_aws">}}

For {{% impl_title "vintage_aws" %}} (`--provider aws`):

- [`Cluster`]({{< relref "/vintage/use-the-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AWSCluster`]({{< relref "/vintage/use-the-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - holds AWS-specific configuration.
- [`G8sControlPlane`]({{< relref "/vintage/use-the-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes
- [`AWSControlPlane`]({{< relref "/vintage/use-the-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io.md" >}}) (API version `infrastructure.giantswarm.io/v1alpha3`) - specifies the control plane nodes with AWS-specific details

{{< /tab >}}
{{< /tabs >}}

## General CLI flags

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (one of: `aws`, `azure`, `capa`, `gcp`, `vsphere` or `openstack`).
- `--name` - Unique name of the cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` - Name of the organization that will own the cluster. Determines the namespace where resources will be created.
  Can be retrieved with `kubectl get releases` for your installation.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s).
- `--output` (optional) - The name of the file to write the output to instead of stdout.
- `--oidc-issuer-url` (optional - CAPI) - This is the issuer URL for configuring OpenID connect in the cluster API.
- `--oidc-ca-file` (optional - CAPI) - This is the CA file path in case is not used a trusted Certificate Authority for OIDC endpoint.
- `--oidc-client-id` (optional - CAPI) - This is the client ID that is configured in the OIDC endpoint.
- `--oidc-username-claim` (optional - CAPI) - This is the claim used to map the username identity of the user.
- `--oidc-groups-claim` (optional - CAPI) - This is the claim used to map the group identity of the user.

  On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

### AWS CAPI specific flags

- `--aws-cluster-role-identity-name` (optional) - Refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account (default: `default`).
- `--az-usage-limit` (optional) - Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets (default: `3`).
- `--bastion-instance-type` (optional) - Instance type used for the bastion machine (default: `t3.small`).
- `--bastion-replicas` (optional) - Number of bastion instances to run.
- `--control-plane-instance-type` (optional) - Instance type used for Control plane nodes (default: `r6i.xlarge`).
- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--machine-pool-azs` (optional) - Availability zones for the machine pool.
- `--machine-pool-custom-node-labels` (optional) - Labels to add to the nodes in the machine pool.
- `--machine-pool-instance-type` (optional) - Instance type to use for the machine pool.
- `--machine-pool-max-size` (optional) - Maximum size of the machine pool.
- `--machine-pool-min-size` (optional) - Minimum size of the machine pool.
- `--machine-pool-name` (optional) - Name of the machine pool.
- `--machine-pool-root-volume-size-gb` (optional) - Size in GB of the root volume of the machines in the machine pool.
- `--name` - must only contain alphanumeric characters, start with a letter, and be no longer than 20 characters in length.
- `--region` - AWS region where cluster will be created.
- `--vpc-cidr` (optional) - IPv4 address range to assign to this cluster's VPC, in CIDR notation.

### AWS Vintage specific flags

- `--external-snat` - AWS CNI configuration to disable (is enabled by default) the [external source network address translation](https://docs.aws.amazon.com/eks/latest/userguide/external-snat.html).
- `--pods-cidr` (optional) - CIDR applied to the pods. If this isn't provided, the installation default will be applied.
- `--label` (optional) - workload cluster label in the form of `key=value`. Can be specified multiple times.
- `--service-priority` (optional) - [Service priority]({{< relref "/vintage/advanced/cluster-management/labelling-workload-clusters#service-priority" >}}) of the cluster (one of: `highest`, `medium`, or `lowest`; default: `highest`).
- `--release-branch` (optional) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--release` - Workload cluster release version.

### Azure CAPI specific flags

- `--azure-subscription-id` - Azure subscription ID to use.
- `--bastion-instance-type` (optional) - Instance type used for the bastion machine (default: `Standard_D2s_v5`).
- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--control-plane-instance-type` (optional) - Instance type used for Control plane nodes (default: `Standard_D4s_v3`).
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--name` - must only contain alphanumeric characters, start with a letter, and be no longer than 20 characters in length.
- `--region` - Azure region where cluster will be created.

### Azure Vintage specific flags

- `--release-branch` (optional) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--release` - Workload cluster release version.

### GCP specific flags

- `--gcp-project` - The Google Cloud Platform project where the cluster will be deployed.
- `--region` - The Google Cloud Platform region where the cluster will be deployed.
- `--gcp-failure-domains` - The Google Cloud Platform zones where the cluster's control-plane nodes will be deployed.
- `--gcp-control-plane-sa-email` (optional) - The Google Cloud Platform Service Account which the control-plane nodes will use (default: "default").
- `--gcp-control-plane-sa-scopes` (optional) - The Google Cloud Platform API scopes the control-plane will have access to (default: `https://www.googleapis.com/auth/compute`).
- `--gcp-machine-deployment-sa-email` (optional) - The Google Cloud Platform Service Account used by the worker nodes (default "default").
- `--gcp-machine-deployment-sa-scopes` (optional) - The Scope of the worker nodes' Google Cloud Platform Service Account (default [https://www.googleapis.com/auth/compute]).
- `--gcp-machine-deployment-name` (optional) - The name of the MachineDeployment (default: `worker1`).
- `--gcp-machine-deployment-instance-type` (optional) - The Google Cloud Platform Instance Type for the default nodepool isntances (default: `n1-standard-4`).
- `--gcp-machine-deployment-failure-domain` (optional) - The Google Cloud Platform zones where the cluster's default nodepool will be deployed. (default: `europe-west6-a`).
- `--gcp-machine-deployment-replicas` (optional) - The number of nodes in the default nodepool (default: 3).
- `--gcp-machine-deployment-disk-size` (optional) - The node disk size in GB for the default nodepool (default: 100).

**Note:** The zones where the worker and control-plane nodes are deployed must be in the same region specified in the `--region` flag.

### OpenStack specific flags

- `--cluster-version` (optional) - Version of `cluster-openstack` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-version` (optional) - Version of `default-apps-openstack` helm chart to use. If not provided, the latest version will be used.
- `--cloud` - Name of the cloud in the `cloud-config` secret. This is almost always "openstack".
- `--cloud-config` - Name of the `cloud-config` secret which defines the credentials for the OpenStack project in which the cluster should be created. This must be created in the organization namespace before creating a cluster.
- `--dns-nameservers` (optional) - A list of DNS nameservers to be used to resolve external names.
- `--external-network-id` - UUID of the external network to be used. Only required if multiple external networks are available.
- `--node-cidr` - CIDR defining the IP range of cluster nodes. When used, new network and subnet will be created.
- `--network-name` (optional) - Name of existing network for the cluster. Can be used when `--node-cidr` is empty.
- `--subnet-name` (optional) - Name of existing subnet for the cluster. Can be used when `--node-cidr` is empty.
- `--bastion-boot-from-volume` - If true, bastion machine will use a persistent root volume instead of an ephemeral volume.
- `--bastion-disk-size` - Size of root volume attached to the cluster bastion machine in gigabytes. Must be greater than or equal to the size of the bastion source image (`--bastion-image`).
- `--bastion-image` - Bastion image name or root volume source UUID if --bastion-boot-from-volume is set.
- `--bastion-machine-flavor` - Flavor (a.k.a. size) of the bastion machine.
- `--control-plane-boot-from-volume` - If true, control plane machine(s) will use a persistent root volume instead of an ephemeral volume.
- `--control-plane-disk-size` - Size of root volumes attached to each control plane node machine in gigabytes. Must be greater than or equal to the size of the node source image.
- `--control-plane-image` - Control plane image name or root volume source UUID if --control-plane-boot-from-volume is set.
- `--control-plane-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--control-plane-replicas` - Number of control plane replicas. This should be 1 for a non-HA control plane or 3 for an HA control plane (etcd requires an odd number of members).
- `--worker-boot-from-volume` - If true, worker machines will use a persistent root volume instead of an ephemeral volume.
- `--worker-disk-size` - Size of root volumes attached to each worker node machine in gigabytes. Must be greater than or equal to the size of the node source image (`--worker-image`).
- `--worker-failure-domain` - Failure domain of worker nodes.
- `--worker-image` - Worker image name or root volume source UUID if --worker-boot-from-volume is set.
- `--worker-machine-flavor` - Flavor (a.k.a. size) of the worker node machines.
- `--worker-replicas` - Number of replicas in the primary worker node pool.

### vSphere specific flags

- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--kubernetes-version` (optional) - Cluster's Kubernetes version (default: 1.24.11).
- `--vsphere-control-plane-disk-gib` (optional) - Disk size in GiB for individual control plane nodes (default: 50).
- `--vsphere-control-plane-ip` (optional) - Control plane IP, leave empty for auto allocation.
- `--vsphere-control-plane-ip-pool` (optional) - Name of `GlobalInClusterIpPool` CR from which to take an IP for the control plane (default: `wc-cp-ips`).
- `--vsphere-control-plane-memory-mib` (optional) - Memory size in MiB for individual control plane nodes (default: 8096).
- `--vsphere-control-plane-num-cpus` (optional) - Number of CPUs for individual control plane nodes (default: 4).
- `--vsphere-control-plane-replicas` (optional) - Number of control plane replicas in odd number (default: 3).
- `--vsphere-credentials-secret-name` (optional) - Name of the kubernetes secret that should be associated to the cluster app. It should exist in the organization's namespace and should contain the credentials for vsphere.
- `--vsphere-image-template` (optional) - Name of the vSphere template to deploy the VMs from (default: `ubuntu-2004-kube-${kubernetes-version}`).
- `--vsphere-network-name` - Portgroup name in vCenter to connect the new VMs to.
- `--vsphere-resource-pool` (optional) - Name of the vSphere resource pool to deploy the VMs to (default: cluster)
- `--vsphere-service-lb-pool` (optional) - Name of GlobalInClusterIpPool CR from which the IP for Service LB (kubevip) is taken (default "svc-lb-ips")
- `--vsphere-service-load-balancer-cidr` (optional) - CIDR for Service LB within workload cluster.
- `--vsphere-worker-disk-gib` (optional) - Disk size in GiB for individual worker nodes (default: 50).
- `--vsphere-worker-memory-mib` (optional) - Memory size in MiB for individual worker nodes (default: 14144).
- `--vsphere-worker-num-cpus` (optional) - Number of CPUs for individual worker nodes (default: 6).
- `--vsphere-worker-replicas` (optional) - Number of worker replicas (default: 3).

## Examples

{{< tabs >}}
{{< tab id="command-examples-aws" for-impl="vintage_aws">}}

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
{{< tab id="command-examples-aws-capi" for-impl="capa_ec2">}}

Example command for an AWS CAPI cluster:

```nohighlight
kubectl gs template cluster \
  --provider capa \
  --control-plane-az eu-central-1a \
  --description "Development Cluster" \
  --name dev01 \
  --organization acme
```

{{< /tab >}}
{{< tab id="command-examples-azure-capi" for-impl="capz_vms">}}

Example command for an Azure CAPI cluster:

```nohighlight
kubectl gs template cluster \
  --provider capz \
  --region germanywestcentral \
  --azure-subscription-id xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx \
  --description "Development Cluster" \
  --name dev01 \
  --organization acme
```

{{< /tab >}}
{{< tab id="command-examples-vsphere" for-impl="capv">}}

```nohighlight
kubectl gs template cluster \
  --provider vsphere \
  --name demo1 \
  --organization multi-project \
  --vsphere-service-load-balancer-cidr 10.10.222.238/30 \
  --vsphere-network-name demo1 \
  --vsphere-worker-memory-mib 4096 \
  --vsphere-worker-num-cpus 4 \
  --vsphere-worker-replicas 3 \
  --vsphere-control-plane-num-cpus 8 \
  --vsphere-control-plane-memory-mib 12000 \
```

{{< /tab >}}
{{< /tabs >}}

## Output

The above example command would generate the following output:

{{< tabs >}}
{{< tab id="command-output-aws" for-impl="vintage_aws">}}

```yaml
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/clusters.cluster.x-k8s.io/
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
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/awsclusters.infrastructure.giantswarm.io/
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
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io/
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
    giantswarm.io/docs: https://docs.giantswarm.io/use-the-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io/
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
{{< tab id="command-output-aws-capi" for-impl="capa_ec2">}}

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
      machine-pool0:
        availabilityZones:
        - eu-central-1a
        instanceType: m5.xlarge
        maxSize: 10
        minSize: 3
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
{{< tab id="command-output-azure-capi" for-impl="capz_vms">}}

```yaml
---
apiVersion: v1
data:
  values: |
    connectivity:
      bastion:
        enabled: true
    controlPlane:
      replicas: 3
    metadata:
      description: Development Cluster
      name: dev01
      organization: acme
    providerSpecific:
      location: germanywestcentral
      subscriptionId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
kind: ConfigMap
metadata:
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
  name: cluster-azure
  namespace: org-acme
  userConfig:
    configMap:
      name: dev01-userconfig
      namespace: org-acme
  version: 0.0.29
---
apiVersion: v1
data:
  values: |
    clusterName: dev01
    organization: acme
kind: ConfigMap
metadata:
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
    giantswarm.io/cluster: dev01
    giantswarm.io/managed-by: cluster
  name: dev01-default-apps
  namespace: org-acme
spec:
  catalog: cluster
  config:
    configMap:
      name: dev01-cluster-values
      namespace: org-acme
  kubeConfig:
    inCluster: true
  name: default-apps-azure
  namespace: org-acme
  userConfig:
    configMap:
      name: dev01-default-apps-userconfig
      namespace: org-acme
  version: 0.4.0
```

{{< /tab >}}
{{< tab id="command-output-vsphere" for-impl="capv">}}

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        baseDomain: test.gigantic.io
        network:
          controlPlaneEndpoint:
            host: ""
            ipPoolName: wc-cp-ips
            port: 6443
          loadBalancers:
            cidrBlocks:
            - 10.10.222.238/30
            ipPoolName: svc-lb-ips
      controlPlane:
        image:
          repository: gsoci.azurecr.io/giantswarm
        machineTemplate:
          cloneMode: linkedClone
          diskGiB: 50
          memoryMiB: 12000
          network:
            devices:
            - dhcp4: true
              networkName: demo1
          numCPUs: 8
          resourcePool: '*/Resources'
          template: flatcar-stable-3602.2.1-kube-v1.24.12-gs
        replicas: 3
      metadata:
        organization: multi-project
      nodeClasses:
        default:
          cloneMode: linkedClone
          diskGiB: 50
          memoryMiB: 4096
          network:
            devices:
            - dhcp4: true
              networkName: demo1
          numCPUs: 4
          resourcePool: '*/Resources'
          template: flatcar-stable-3602.2.1-kube-v1.24.12-gs
      nodePools:
        worker:
          class: default
          replicas: 3
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: demo1
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
  catalog: cluster
  config:
    configMap:
      name: ""
      namespace: ""
    secret:
      name: ""
      namespace: ""
  extraConfigs:
  - kind: secret
    name: container-registries-configuration
    namespace: default
    priority: 25
  kubeConfig:
    context:
      name: ""
    inCluster: true
    secret:
      name: ""
      namespace: ""
  name: cluster-vsphere
  namespace: org-multi-project
  userConfig:
    configMap:
      name: demo1-userconfig
      namespace: org-multi-project
    secret:
      name: vsphere-credentials
      namespace: org-multi-project
  version: 0.53.1
---
apiVersion: v1
data:
  values: |
    clusterName: demo1
    organization: multi-project
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: demo1
  name: demo1-default-apps-userconfig
  namespace: org-multi-project
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 0.0.0
    giantswarm.io/cluster: demo1
    giantswarm.io/managed-by: cluster
  name: demo1-default-apps
  namespace: org-multi-project
spec:
  catalog: cluster
  config:
    configMap:
      name: demo1-cluster-values
      namespace: org-multi-project
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
  name: default-apps-vsphere
  namespace: org-multi-project
  userConfig:
    configMap:
      name: demo1-default-apps-userconfig
      namespace: org-multi-project
  version: 0.14.0
```

{{< /tab >}}
{{< /tabs >}}
