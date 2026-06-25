---
title: Introduction to Cluster API
description: How the Giant Swarm platform leverages the Cluster API standard for managing Kubernetes clusters across infrastructure providers.
weight: 10
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement
    identifier: overview-fleetmanagement-clustermanagement-capi
aliases:
  - /platform-overview/cluster-management/cloud-provider-implementations
last_review_date: 2026-06-22
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How does Giant Swarm serve Cluster API features?
  - What other services are needed in a platform to complete Cluster API?
---

The [Cluster API project](https://cluster-api.sigs.k8s.io/) is a Kubernetes sub-project that takes an **innovative approach** to provisioning, configuring, and managing clusters. It uses a **declarative model**: you define the desired state of your clusters, and the system automatically works to reach that state. This gives you a **standard mechanism** to handle Kubernetes clusters, which simplifies operations and increases efficiency.

Cluster API uses **operators** and **custom resource definitions** to manage Kubernetes clusters. An operator is essentially a controller that responds to cluster lifecycle events. It automates the creation, configuration, and management of clusters.

Custom resource definitions extend the Kubernetes API so you can create new resources—in this case, the cluster resources. When you define such cluster resources, the Cluster API operator reacts to this declarative statement and works to reach the desired state of the cluster. This includes tasks such as **provisioning infrastructure**, **bootstrapping nodes**, and **applying configuration**.

## Giant Swarm flavor

The Giant Swarm platform adds capabilities on top of Cluster API that we consider **must-haves** for a complete production system. These aren't part of the upstream project yet.

We use these features of Cluster API:

- **Certificate management**: Cluster API manages important certificates in a Kubernetes cluster, like for kubelet or Etcd.
- **Node bootstrap**: the operator correctly bootstraps nodes in the cluster from the defined configuration.
- **Infrastructure provisioning**: the operator talks to the provider-specific API (for example AWS) to create the infrastructure needed for the cluster.
- **Automatic cluster scaling**: Cluster API integrates with the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) project so clusters can grow or shrink based on different policies.
- **Health checks**: the operator can check the health of the nodes and act to avoid manual intervention.

On top of that, we've some additional features that aren't part of the Cluster API standard:

- **DNS management**: we provide a DNS operator to manage DNS assets for the clusters dynamically.
- **Provider credentials management**: we've automated the credentials management to operate the provider infrastructure securely.
- **Encryption configuration**: we've designed an operator that controls and configures the cryptographic assets for workload clusters, making sure they're rotated and updated as needed.
- **Cluster API monitoring**: we monitor all the Cluster API-specific resources. This tells us the status of the cluster creation and the health of the cluster.
- **Provider-specific operators**: we've further operators that help automate all parts of the cluster lifecycle, like VPC provisioning or security group management, when upstream Cluster API doesn't provide it.

## Wrapping resources in charts

To create a cluster with Cluster API, you need to define a set of resources. For example: `Cluster`, `<PROVIDER_NAME>Cluster`, `KubeadmControlPlane`, `MachinePool`, `<PROVIDER_NAME>MachinePool`, etc. as standardized by the Cluster API custom resource definitions.

You _could_ create these resources manually and explore every single specification field available. But we offer a more convenient way: a set of **ready-to-use charts** that provision a cluster correctly. For these charts, we provide proper release management, documentation, and testing. This means you can trust that minor upgrades happen without disruption, and that breaking changes are documented and happen only in major releases.

On top of the chart, we've got the [`App` concept]({{< relref "/overview/fleet-management/app-management" >}}). This is a custom resource that helps us select a chart to install in the management cluster. It adds extended configuration capabilities that enhance the fleet management experience.

Learn more by reading how to [create your first workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).
