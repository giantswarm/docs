---
linkTitle: template cluster
title: "'kubectl gs template cluster' command reference"
diataxis_content_type: reference
description: Reference documentation on how to create a manifest for a Cluster using 'kubectl gs'.
weight: 90
menu:
  principal:
    parent: reference-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How can I create a cluster manifest for the platform API?
last_review_date: 2026-11-19
aliases:
  - /vintage/use-the-api/kubectl-gs/template-cluster/
---

This command helps with creating a Cluster API (CAPI) cluster by producing a manifest based on user input. This manifest can then optionally be modified and finally be applied to the platform API to create a cluster.

The generated manifest includes:

- `ConfigMap` - describes the configuration for the cluster chart. The resource name is the cluster name plus the `-userconfig` suffix.
- Flux `OCIRepository` and `HelmRelease` - deploy the `release-<provider>` chart of the given release, such as `release-aws`, with the values of the above ConfigMap. The chart creates the actual cluster resources. Both resource names are identical with the cluster name.

When no `release-<provider>` chart exists for the given release, for example for a release that isn't published yet, the command generates an [`App`]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) of the `cluster-<provider>` chart instead of the `OCIRepository` and the `HelmRelease`, and prints a warning. It does the same when you pass `--cluster-version`. Please see [Creating a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster/" >}}) for which cluster chart is used, depending on the cloud provider.

By default, the generated resources are protected from deletion. See [deletion prevention](#deletion-prevention).

## Syntax and flags

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (one of: `capa`, `capz`, `vsphere`, `cloud-director`, `eks`).
- `--name` - Unique name of the cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` - Name of the organization that will own the cluster. Determines the namespace where resources will be created.
- `--release` - Workload cluster release version. Can be retrieved with `kubectl gs get releases`.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s). On AWS, must match the installation region (e.g. `eu-central-1a` for region `eu-central-1`). On Azure, can be any of `1`, `2`, `3`. Use the flag once for a single control plane node, or three times with distinct AZs for high-availability (AWS only).
- `--label` (optional) - Label in the form `key=value` to set on the cluster. Can be specified multiple times.
- `--prevent-deletion` (optional) - Protect the cluster from deletion (default: `true`). Pass `--prevent-deletion=false` to allow deleting it. See [deletion prevention](#deletion-prevention).
- `--service-priority` (optional) - Service priority of the cluster (one of: `highest`, `medium`, `lowest`).
- `--output` (optional) - The name of the file to write the output to instead of stdout.
- `--disable-oidc` (optional) - Leave `global.controlPlane.oidc` out, so that the cluster's API server trusts no OIDC issuer. Cannot be combined with the `--oidc-*` flags. See [OIDC](#oidc).
- `--oidc-issuer-url` (optional) - Issuer URL the cluster trusts instead of the management cluster's Dex. Requires `--oidc-client-id`.
- `--oidc-ca-file` (optional) - Path to a PEM file with the CA certificate used to verify the OIDC issuer, when it doesn't use a trusted Certificate Authority.
- `--oidc-client-id` (optional) - OIDC client ID (default: the management cluster's).
- `--oidc-username-claim` (optional) - Claim used to map the username identity of the user (default: the management cluster's, or `email` with `--oidc-issuer-url`).
- `--oidc-groups-claim` (optional) - Claim used to map the group identity of the user (default: the management cluster's, or `groups` with `--oidc-issuer-url`).

### OIDC {#oidc}

For the providers `capa`, `capz`, `vsphere` and `cloud-director`, the command sets `global.controlPlane.oidc` in the generated cluster configuration, so that the workload cluster's API server trusts the OIDC issuer (Dex) of the management cluster that the current kubeconfig context points at. You don't need to pass any `--oidc-*` flag for that. The values are read from the management cluster's own control plane. The `eks` provider runs a managed control plane and isn't affected.

- To override single settings, pass the matching `--oidc-*` flag, for example `--oidc-groups-claim`. Flags you pass win over the values read from the management cluster.
- To trust another issuer, pass `--oidc-issuer-url` together with `--oidc-client-id`. The management cluster isn't asked in that case.
- To leave the OIDC settings out, pass `--disable-oidc`. Combining it with any `--oidc-*` flag is an error.

If the values can't be read from the management cluster, for example because the kubeconfig has no context selected, the command fails with an error that names the cause and the two ways out: `--oidc-issuer-url` with `--oidc-client-id`, or `--disable-oidc`.

### Deletion prevention {#deletion-prevention}

Since kubectl-gs v7.0.0, the command protects the cluster from accidental deletion by default:

- It adds the `giantswarm.io/prevent-deletion: "true"` label to the ConfigMap, and to the `OCIRepository` and the `HelmRelease`, or to the `App`.
- It sets `global.metadata.preventDeletion: true` in the cluster values, so that the chart adds the label to the `Cluster` resource too.

The management cluster refuses to delete resources with this label. To delete the cluster later, remove the protection first, as described in [Prevent accidental deletion of resources]({{< relref "/tutorials/fleet-management/deletion-prevention#deleting-a-protected-cluster" >}}). To create a cluster without deletion prevention, pass `--prevent-deletion=false`.

### Flags specific to AWS {#flags-capa}

- `--aws-cluster-role-identity-name` (optional) - Refers to the IAM role used to create all AWS cloud resources when creating the cluster. The role can be in another AWS account in order to create all resources in that account (default: `default`).
- `--az-usage-limit` (optional) - Maximum number of availability zones (AZ) that should be used in a region. If a region has more than this number of AZs then this number of AZs will be picked randomly when creating subnets (default: `3`).
- `--bastion-instance-type` (optional) - Instance type used for the bastion machine (default: `t3.small`).
- `--bastion-replicas` (optional) - Number of bastion instances to run (default: `1`).
- `--control-plane-instance-type` (optional) - Instance type used for Control plane nodes (default: `r6i.xlarge`).
- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-aws` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-aws` helm chart to use. If not provided, the latest version will be used.
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

### Flags specific to Azure {#flags-capz}

- `--azure-subscription-id` - Azure subscription ID to use.
- `--bastion-instance-type` (optional) - Instance type used for the bastion machine (default: `Standard_D2s_v5`).
- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-azure` helm chart to use. If not provided, the latest version will be used.
- `--control-plane-instance-type` (optional) - Instance type used for Control plane nodes (default: `Standard_D4s_v3`).
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-azure` helm chart to use. If not provided, the latest version will be used.
- `--name` - must only contain alphanumeric characters, start with a letter, and be no longer than 20 characters in length.
- `--region` - Azure region where cluster will be created.

**Note:** The zones where the worker and control-plane nodes are deployed must be in the same region specified in the `--region` flag.

### Flags specific to vSphere {#flags-capv}

- `--cluster-catalog` (optional) - Name of the Giant Swarm app catalog that holds the cluster's app release.
- `--cluster-version` (optional) - Version of `cluster-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--default-apps-catalog` (optional) - Name of the Giant Swarm app catalog that holds the default-apps' app release.
- `--default-apps-version` (optional) - Version of `default-apps-vsphere` helm chart to use. If not provided, the latest version will be used.
- `--kubernetes-version` (optional) - Cluster's Kubernetes version (default: `v1.24.12`).
- `--vsphere-control-plane-disk-gib` (optional) - Disk size in GiB for individual control plane nodes (default: 50).
- `--vsphere-control-plane-ip` (optional) - Control plane IP, leave empty for auto allocation.
- `--vsphere-control-plane-ip-pool` (optional) - Name of `GlobalInClusterIpPool` CR from which to take an IP for the control plane (default: `wc-cp-ips`).
- `--vsphere-control-plane-memory-mib` (optional) - Memory size in MiB for individual control plane nodes (default: 8192).
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
{{< tab id="command-examples-aws-capi" for-impl="capa_ec2">}}

Example command for an AWS CAPI cluster:

```nohighlight
kubectl gs template cluster \
  --provider capa \
  --release 36.1.1 \
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
  --release 36.1.1 \
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

The above example commands would generate the following output. The OIDC settings that the command reads from the management cluster are left out.

{{< tabs >}}
{{< tab id="command-output-aws-capi" for-impl="capa_ec2">}}

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        availabilityZoneUsageLimit: 3
        network: {}
        topology: {}
      controlPlane: {}
      metadata:
        description: Development Cluster
        name: dev01
        organization: acme
        preventDeletion: true
        servicePriority: highest
      nodePools:
        nodepool0:
          availabilityZones:
          - eu-central-1a
          instanceType: m5.xlarge
          maxSize: 10
          minSize: 3
          rootVolumeSizeGB: 8
      providerSpecific: {}
kind: ConfigMap
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01-userconfig
  namespace: org-acme
---
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01
  namespace: org-acme
spec:
  interval: 10m0s
  provider: generic
  ref:
    tag: 36.1.1
  timeout: 1m0s
  url: oci://gsoci.azurecr.io/charts/giantswarm/release-aws
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01
  namespace: org-acme
spec:
  chartRef:
    kind: OCIRepository
    name: dev01
    namespace: org-acme
  install:
    remediation:
      remediateLastFailure: false
  interval: 5m0s
  releaseName: dev01
  serviceAccountName: automation
  storageNamespace: org-acme
  targetNamespace: org-acme
  timeout: 10m0s
  upgrade:
    remediation:
      remediateLastFailure: true
      retries: 10
      strategy: rollback
  valuesFrom:
  - kind: ConfigMap
    name: dev01-userconfig
    valuesKey: values
```

{{< /tab >}}
{{< tab id="command-output-azure-capi" for-impl="capz_vms">}}

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        bastion:
          enabled: true
      controlPlane:
        replicas: 3
      metadata:
        description: Development Cluster
        name: dev01
        organization: acme
        preventDeletion: true
        servicePriority: highest
      providerSpecific:
        location: germanywestcentral
        subscriptionId: xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
kind: ConfigMap
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01-userconfig
  namespace: org-acme
---
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01
  namespace: org-acme
spec:
  interval: 10m0s
  provider: generic
  ref:
    tag: 36.1.1
  timeout: 1m0s
  url: oci://gsoci.azurecr.io/charts/giantswarm/release-azure
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  labels:
    giantswarm.io/cluster: dev01
    giantswarm.io/prevent-deletion: "true"
  name: dev01
  namespace: org-acme
spec:
  chartRef:
    kind: OCIRepository
    name: dev01
    namespace: org-acme
  install:
    remediation:
      remediateLastFailure: false
  interval: 5m0s
  releaseName: dev01
  serviceAccountName: automation
  storageNamespace: org-acme
  targetNamespace: org-acme
  timeout: 10m0s
  upgrade:
    remediation:
      remediateLastFailure: true
      retries: 10
      strategy: rollback
  valuesFrom:
  - kind: ConfigMap
    name: dev01-userconfig
    valuesKey: values
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
