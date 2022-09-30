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

### Flags

### Examples

## Output

Manifests for the following resources will be created:

- [`Cluster`]({{< relref "/ui-api/management-api/crd/clusters.cluster.x-k8s.io.md" >}}) (API version `cluster.x-k8s.io/v1beta1`) - holds the base cluster specification.
- [`AzureCluster`]({{< relref "/ui-api/management-api/crd/azureclusters.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - holds Azure-specific configuration.
- [`AzureMachine`]({{< relref "/ui-api/management-api/crd/azuremachines.infrastructure.cluster.x-k8s.io.md" >}}) (API version `infrastructure.cluster.x-k8s.io/v1beta1`) - specifies the control plane nodes.
