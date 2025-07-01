---
title: Introduction to Cluster API
description: How the Giant Swarm platform leverages the Cluster API standard for managing Kubernetes clusters across infrastructure providers.
weight: 10
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement
    identifier: overview-fleetmanagement-clustermanagement-capi
last_review_date: 2024-05-02
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How does Giant Swarm serve Cluster API features?
  - What other services are needed in a platform to complete Cluster API?
---

The [Cluster API project](https://cluster-api.sigs.k8s.io/) is a Kubernetes sub-project that presents an innovative approach to provisioning, configuring, and managing clusters. It employs a declarative model, which means that users can define the desired state of their clusters, and the system will automatically work to achieve that state. This powerful tool offers a standard mechanism to handle Kubernetes clusters, simplifying operations and increasing efficiency.

Cluster API leverages the concept of operators and custom resource definitions to manage Kubernetes clusters. An operator is essentially a controller that responds to cluster lifecycle events, allowing for automated creation, configuration, and management of clusters.

Custom resource definitions are extensions of the Kubernetes API that allow the creation of new resources—in this case, the cluster resources. When a user defines such cluster resources, the Cluster API operator reacts to this declarative statement and works to achieve the desired state of the cluster. This includes tasks such as provisioning infrastructure, bootstrapping nodes, and applying configuration.

## Giant Swarm flavor

The Giant Swarm platform offers additional capabilities on top of Cluster API that we consider as must-have for a complete production system, but aren't part of the upstream project, yet.

We leverage these features of Cluster API:

- Certificate management: Cluster API manages important certificates in a Kubernetes cluster, like for kubelet or Etcd.
- Node bootstrap: the operator correctly bootstraps nodes in the cluster from the defined configuration.
- Infrastructure provisioning: the operator talks to the provider-specfic API (for example AWS) to create the infrastructure needed for the cluster.
- Automatic cluster scaling: Cluster API integrates with the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) project to allow clusters to grow or shrink based on different policies.
- Health checks: the operator is able to check the health of the nodes and take actions to avoid manual intervention.

On top of that, we've some additional features that aren't part of the Cluster API standard:

- DNS management: we provide a DNS operator to manage DNS assets for the clusters dynamically.
- Provider credentials management: we've automated the credentials management to operate the provider infrastructure in a secure way.
- Encryption configuration: we've designed an operator that controls the cryptographic assets for workload clusters and configure them, making sure they're rotated and updated as needed.
- Cluster API monitoring: we monitor all the cluster API specific resources letting us know the status of the cluster creation and the health of the cluster.
- Further, we've got some other operators that are provider specific and help to automate all parts of the cluster lifecycle, like VPC provisioning or security group management, when upstream Cluster API doesn't provide it.

## Wrapping resources in charts

For creating a cluster using Cluster API, you would need to define a set of resources that will be used to create the cluster. For example: `Cluster`, `<PROVIDER_NAME>Cluster`, `KubeadmControlPlane`, `MachinePool`, `<PROVIDER_NAME>MachinePool`, etc. as standardized by the Cluster API custom resource definitions. You _could_ create these resources manually, exploring every single specification field that's possible to use, but we offer a more convenient way to do that: we've a set of charts that are ready to be used to provision a cluster correctly. For those, we provide proper release management, documentation and testing, such that you can trust that minor upgrades happen without disruption, or breaking changes are described and happening only in major releases.

On top the chart, we've got the [`App` concept]({{< relref "/overview/fleet-management/app-management" >}}), a custom resource which helps us to select a chart to be installed in the management cluster allowing extended configuration capabilities that enhance the fleet management experience.

Learn more by reading how to [create your first workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).
