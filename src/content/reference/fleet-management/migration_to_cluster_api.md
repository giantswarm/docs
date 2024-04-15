---
title: Migration to Cluster API
description: How the migration from our old AWS vintage management clusters to Cluster API works.
weight: 20
last_review_date: 2024-03-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are the requirements for migrating a cluster to Cluster API?
  - What are the recommendations for a smooth migration?
---

From the outset, Giant Swarm has utilized Kubernetes to build platforms. In the early years, everybody was still figuring out how to effectively manage Kubernetes lifecycle across a fleet of clusters. We built our own tooling, largely based on [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), which worked well for us and our customers. As the Kubernetes project and the community around it evolved, it became clear that many companies in the ecosystem were trying to solve the same fundamental challenges regarding cluster lifecycle management. With our extensive experience, we saw an opportunity to contribute to a broader solution. We pushed for a joint effort to build a standardized method for cluster lifecycle management. [Cluster API]({{< relref "/reference/fleet-management/introduction" >}}) is backed by the Kubernetes community and covers different providers like AWS, Azure, GCP, and others.

This guide outlines the migration path from our AWS vintage platform to the [Cluster API](https://cluster-api.sigs.k8s.io/) (CAPI) standard, ensuring a seamless transition for customer workload clusters from the previous system to the modern CAPI framework. Within this document, you'll find an overview of the migration procedure in AWS, including its prerequisites and strategic advice, all aimed at facilitating a smooth and successful transition.

## Pre-migration requirements

Before you begin the migration:

1. Your cluster should be at least on a AWS vintage version [`20.0.0`](https://docs.giantswarm.io/changes/workload-cluster-releases-aws/releases/aws-v20.0.0/).
2. The AWS IAM role, with the specific name `giantswarm-{CAPI_MC_NAME}-capa-controller`, must be created for the workload cluster's (WC) AWS account before starting the migration. [For more information please refer to this guide]({{< relref "/vintage/getting-started/cloud-provider-accounts/cluster-api/aws/" >}}).
3. In case of using GitOps, Flux must be turned off during the migration since some of the cluster custom resources will be modified or removed by the migration scripts.

__Note:__ The `CAPI_MC_NAME` is the name of the management cluster (MC) where the Cluster API controllers are installed.

## Recommendations for a smooth migration

We also recommend increasing the size of your "master" node instance type to 2x or 3x its normal size for the duration of the migration. (e.g. `m5.large` to `m5.4xlarge`). This ensures the API server can effectively handle the load during the migration since there might only be one node to handle the traffic at certain points throughout the process.

## The migration process

The migration process consists of several steps:

0. __New CAPA cluster provision:__ First of all, a new management cluster is created in AWS using the Cluster API flavour (CAPA). This management cluster will have all the necessary controllers to manage the workload clusters once migrated. At the same time a new host zone is created in Route53 for the new management cluster.
1. __Initialization:__ Necessary Kubernetes access credentials and AWS credentials are retrieved. The Vault client is created to interact with the Vault instance containing all security assets of the cluster.
2. __Preparation:__ Migration of secrets to the CAPI management cluster, including CA certs, encryption provider secrets, and service account secrets. Migration scripts are created as secrets in the CAPI management cluster. Additionally, AWS credentials for the cluster are migrated by creating an `AWSClusterRoleIdentity` in the CAPI management cluster. Certain operations are performed to avoid conflicts during migration, such as disabling machine health check on the vintage cluster resources, scaling down the app operator for the migrated workload cluster, or cleaning up certain charts.
3. __Stopping vintage cluster resource reconciliation:__ To avoid conflicts, vintage reconciliation is stopped by removing all `aws-operator` labels from the vintage cluster resource.
4. __Cluster API cluster provisioning:__ Generation and application of CAPI cluster templates. A separate routine runs in the background to ensure the old load balancer remains active. The tool waits until at least one CAPI control-plane node joins the cluster and is in a `Ready` state. Various operations are performed to ensure a smooth transition, such as stopping control-plane components on the vintage cluster, cordoning all vintage control-planes, and deleting certain pods to speed up installation and updates.
5. __Cleaning the vintage cluster:__ All vintage control-plane nodes are drained, vintage auto scaling groups are deleted, and all worker nodes for each node pool are drained and deleted.

__Note:__ The migration process is automated and executed by our engineers. The process is monitored and controlled by a set of scripts and tools to ensure a smooth transition. We don't expect any downtime for the workload clusters during the migration process.

## Post-migration tasks

Our engineers will check that all resources and infrastructure are correctly migrated and that the new cluster is working as expected. There are some reminding tasks needed to be done by the customer:

- The DNS setup changes for the workload clusters. The new management cluster has a new host zone allocated in AWS. In the vintage setup, the host zone contained the management and the workload cluster name in the domain, for API and other components, meanwhile in the CAPI setup the DNS structure is more flexible not containing the management cluster name. Both the old and new host zones will be available for a certain period to ensure a smooth transition, but customers should migrate the DNS records to the new host zone as soon as possible in case they are using cluster wildcard DNS records.

- In case of using GitOps or any other tool pushing the state to the management cluster, the tool should be reconfigured to use the new customer resources used by Cluster API. In order to know which resources need to be updated, created or removed please run `kubectl gs template cluster --provider capa` and compare the output with the current resources in the management cluster. Our account engineers will help with this process providing the exact resources that need to be updated.

- Some customers have been using [k8s-initiator-app](https://github.com/giantswarm/k8s-initiator-app/) to configure some aspects of the workload cluster APIs. In the new Cluster API implementation, [most of the features enabled by the app](https://github.com/giantswarm/capi-migration-cli/tree/main/k8s-initiator-features) are now supported natively by the platform. The app should be removed and moved to the new syntax. Our account engineers will help with this process.
