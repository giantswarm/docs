---
title: Migration to Cluster API
description: A explanation on how the migration from our old Vintage management clusters to Cluster API works.
weight: 20
last_review_date: 2024-03-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are the requirements for migrating a cluster to Cluster API?
  - What are the recommendations for a smooth migration?
---

In Giant Swarm we have used Kubernetes to build platforms since our beginning. We started with a custom solution to manage the lifecycle of the clusters due to the lack of a standard way out of there. It has worked well for us and our customers, but we learnt many companies were resolving the same problem over and over again, so we foster and push for joining forces and build a standard approach. [Cluster API]({{< relref "/reference/fleet-management/introduction" >}}) is backed by the Kubernetes community and covers different providers like AWS, Azure, GCP, and others.

In this document we explain the migration path from our vintage system to the [Cluster API](https://cluster-api.sigs.k8s.io/) standard. This document provides an overview of the process, its requirements, and recommendations to ensure a successful migration.

## Goals

Our new migration process looks for ensuring a smooth transition of your Kubernetes workload clusters from vintage generation to the new Cluster API (CAPI) flavour. This document provides an overview of the process, its requirements, and recommendations to ensure a successful migration.

## Pre-migration requirements

Before you begin the migration:

1. Your cluster should be on a release version `>=20.0.0`.
2. An AWS IAM role, named `giantswarm-{CAPI_MC_NAME}-capa-controller`, must be pre-created for the workload cluster's (WC) AWS account.

__Note:__ The `CAPI_MC_NAME` is the name of the management cluster (MC) where the Cluster API controllers are installed.

## Recommendations for a smooth migration

In preparation for migration, we recommend increasing the size of your "master" node instance type to tow or three times its actual size (example, from `mx.large` to `mx.4xlarge`). This ensures the API server can efficiently handle the load during migration since there might be only one node to handle the traffic at certain points.

## The migration process

The migration process consists of several steps:

1. **Initialization:** Retrieval of necessary Kubernetes access credentials together with AWS credentials. At the same time, it creayes a vault client to interact with the Vault instance that contains all security assets of the cluster.
2. **Preparation:** Migration of secrets to the CAPI management cluster, including CA certs, encryption provider secrets, and service account secrets. The migration scripts are created as a secret in the CAPI management cluster. Additionally, AWS credentials for the cluster are migrated by creating an `AWSClusterRoleIdentity` in the CAPI management cluster. There are certain operations performed to avoid conflicts during migration, such as disabling machine health check on the vintage cluster resources, scaling down the app operator for the migrated workload cluster, or cleaning up certain charts.
3. **Stopping vintage cluster resource reconciliation:** To avoid conflicts, vintage reconciliation is stopped by removing all `aws-operator` labels from the vintage cluster resource.
4. **Cluster API cluster provisioning:** Generation and application of CAPI cluster templates. A separate routine runs in the background to ensure the old load balancer remains active. The tool waits until at least one CAPI control-plane node joins the cluster and is in a Ready state. Various operations are performed to ensure a smooth transition, such as stopping control-plane components on the vintage cluster, cordoning all vintage control-planes, and deleting certain pods to speed up installation and updates.
5. **Cleaning the vintage cluster:** All vintage control-plane nodes are drained, vintage auto scaling groups are deleted, and all worker nodes for each node pool are drained and deleted.

## Post-migration cleanup

Our engineer will check that all resources and infrastructure are correctly migrated and that the new cluster is working as expected.

By following this process, you can ensure a smooth and efficient migration of your Kubernetes clusters to the Cluster API. If you encounter any issues during the migration process, our team is ready to assist you.
