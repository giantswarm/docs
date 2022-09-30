---
linkTitle: Cluster API Azure
title: "'kubectl gs template cluster' command reference for CAPZ"
description: How to create a manifest for a workload cluster using Cluster API provider Azure (CAPZ) via 'kubectl gs'.
menu:
  main:
    parent: uiapi-kubectlgs-templatecluster
    identifier: uiapi-kubectlgs-templatecluster-capz
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a CAPZ cluster manifest via the Management API?
last_review_date: 2022-09-29
---

Here we explain how to use [`kubectl gs template cluster`]({{< relref "/ui-api/kubectl-gs/template-cluster" >}}) with Cluster API provider Azure (also known as CAPZ).

**Note:* Please be aware that this is an early alpha release. Clusters created using this release won't be monitored by Giant Swarm and, they won't be able to be upgraded to newer stable releases.

To enable Cluster API compatible resources, you have to select release version `v20.0.0-alpha1` via the `--release` flag and set the provider name to `azure` via the `--provider` flag.


## Usage

### Flags

### Examples

## Output

Manifests for the following resources will be created:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`KubeadmControlPlane`]({{< relref "/ui-api/management-api/crd/kubeadmcontrolplanes.controlplane.cluster.x-k8s.io.md" >}}) (API version `controlplane.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the control plane nodes.
- [`MachineDeployment`]({{< relref "/ui-api/management-api/crd/machinedeployments.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the bastion host specification.
- [`AzureMachineTemplate`]({{< relref "/ui-api/management-api/crd/azuremachinetemplates.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration for the bastion host.
