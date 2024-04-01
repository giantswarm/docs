---
title: Migration to Cluster API
description: An explanation of how the migration from our old vintage management clusters to Cluster API works.
weight: 20
last_review_date: 2024-03-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are the requirements for migrating a cluster to Cluster API?
  - What are the recommendations for a smooth migration?
---

From the outset, Giant Swarm has utilized Kubernetes to build platforms. In the early years, everybody was still figuring out how to effectively manage Kubernetes lifecycle across a fleet of clusters. We built our own tooling, largely based on [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), which worked well for us and our customers. As the Kubernetes project and the community around it evolved, it became clear that many companies in the ecosystem were trying to solve the same fundamental challenges regarding cluster lifecycle management. With our extensive experience, we saw an opportunity to contribute to a broader solution. We pushed for a joint effort to build a standardized method for cluster lifecycle management. [Cluster API]({{< relref "/reference/fleet-management/introduction" >}}) is backed by the Kubernetes community and covers different providers like AWS, Azure, GCP, and others.

This guide outlines the migration path from our vintage platform to the [Cluster API](https://cluster-api.sigs.k8s.io/) (CAPI) standard, ensuring a seamless transition for customers workload clusters from the traditional system to the modern CAPI framework. Within this document, you'll find a comprehensive overview of the migration procedure, including its prerequisites and strategic advice, all aimed at facilitating a smooth and successful transition.```

## Pre-migration requirements

Before you begin the migration:

1. Your cluster should be on a release version `>=20.0.0`.
2. The AWS IAM role, with the specific name `giantswarm-{CAPI_MC_NAME}-capa-controller`, must be created for the workload cluster's (WC) AWS account before starting the migration. [For more information please refer to this guide](https://docs.giantswarm.io/vintage/getting-started/cloud-provider-accounts/cluster-api/aws/#overview).

__Note:__ The `CAPI_MC_NAME` is the name of the management cluster (MC) where the Cluster API controllers are installed.

## Recommendations for a smooth migration

We also recommend increasing the size of your "master" node instance type to 2x or 3x its normal size for the duration of the migration. (e.g. `mx.large` to `mx.4xlarge`). This ensures the API server can effectively handle the load during the migration since there might only be one node to handle the traffic at certain points throughout the process.

## The migration process

The migration process consists of several steps:

1. __Initialization:__ Necessary Kubernetes access credentials and AWS credentials are retrieved.  Vault client is created to interact with the Vault instance containing all security assets of the cluster.
2. __Preparation:__ Migration of secrets to the CAPI management cluster, including CA certs, encryption provider secrets, and service account secrets. Migration scripts are created as secrets in the CAPI management cluster. Additionally, AWS credentials for the cluster are migrated by creating an `AWSClusterRoleIdentity` in the CAPI management cluster. Certain operations are performed to avoid conflicts during migration, such as disabling machine health check on the vintage cluster resources, scaling down the app operator for the migrated workload cluster, or cleaning up certain charts.
3. __Stopping vintage cluster resource reconciliation:__ To avoid conflicts, vintage reconciliation is stopped by removing all `aws-operator` labels from the vintage cluster resource.
4. __Cluster API cluster provisioning:__ Generation and application of CAPI cluster templates. A separate routine runs in the background to ensure the old load balancer remains active. The tool waits until at least one CAPI control-plane node joins the cluster and is in a Ready state. Various operations are performed to ensure a smooth transition, such as stopping control-plane components on the vintage cluster, cordoning all vintage control-planes, and deleting certain pods to speed up installation and updates.
5. __Cleaning the vintage cluster:__ All vintage control-plane nodes are drained, vintage auto scaling groups are deleted, and all worker nodes for each node pool are drained and deleted.

## Post-migration cleanup

Our engineer will check that all resources and infrastructure are correctly migrated and that the new cluster is working as expected.

By following this process, you can ensure a smooth and efficient migration of your Kubernetes clusters to the Cluster API. If you encounter any issues during the migration process, our team is ready to assist you.
