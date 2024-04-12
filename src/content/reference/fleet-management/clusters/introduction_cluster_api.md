---
title: Introduction to Cluster API
description: How the Giant Swarm platform leverages the Cluster API standard for managing Kubernetes clusters across infrastructure providers.
weight: 100
last_review_date: 2024-03-07
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How does Giant Swarm serve Cluster API features?
  - What other services are needed in a platform to complete Cluster API?
---

The [Cluster API project](https://cluster-api.sigs.k8s.io/) is a Kubernetes sub-project that presents an innovative approach to provisioning, configuring, and managing clusters. It employs a declarative model, which means that users can define the desired state of their clusters, and the system will automatically work to achieve that state. This powerful tool offers a standard mechanism to handle Kubernetes clusters, simplifying operations and increasing efficiency.

Cluster API leverages the concept of operators and Custom Resource Definitions (CRDs) to manage Kubernetes clusters. An operator is essentially a controller that responds to cluster lifecycle events, allowing for automated creation, configuration, and management of clusters.

Custom Resource Definitions (CRDs) are extensions of the Kubernetes API that allow the creation of new resources – in this case, the cluster resources. When a user defines such cluster resources, the Cluster API operator reacts to this declarative statement and works to achieve the desired state of the cluster. This includes tasks such as provisioning infrastructure, bootstrapping nodes, and applying configuration.

## Giant Swarm flavor

The Giant Swarm platform offers additional capabilities on top of Cluster API that we consider as must-have for a complete production system, but are not part of the upstream project, yet.

We leverage these features of Cluster API:

- Certificate management: Cluster API manages important certificates in a Kubernetes cluster, like for kubelet or etcd.
- Node bootstrap: the operator correctly bootstraps nodes in the cluster from the defined configuration.
- Infrastructure provisioning: the operator talks to the provider-specfic API (e.g. AWS API) to create the infrastructure needed for the cluster.
- Cluster autoscaling: Cluster API integrates with the [cluster-autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) project to allow clusters to grow or shrink based on different policies.
- Health checks: the operator is able to check the health of the nodes and take actions to avoid manual intervention.

On top of that, we have some additional features that are not part of the Cluster API standard:

- DNS management: we provide a DNS operator to manage DNS assets for the clusters dynamically.
- Provider credentials management: we have automated the credentials management to operate the provider infrastructure in a secure way.
- Encryption configuration: we have designed an operator that controls the cryptographic assets for workload clusters and configure them properly making sure they are rotated and updated as needed.
- Cluster API monitoring: we monitor all the cluster API specific resources letting us know the status of the cluster creation and the health of the cluster.
- Further, we have some other operators that are provider specific and help to automate all parts of the cluster lifecycle, like VPC provisioning or security group management, when upstream Cluster API does not provide it.

## Wrapping resources in charts

For creating a cluster using Cluster API, you would need to define a set of resources that will be used to create the cluster. For example: `Cluster`, `<PROVIDER_NAME>Cluster`, `KubeadmControlPlane`, `MachinePool`, `<PROVIDER_NAME>MachinePool`, etc. as standardized by the Cluster API custom resource definitions. You _could_ create these resources manually, exploring every single specification field that is possible to use, but we offer a more convenient way to do that: we have a set of charts that are ready to be used to provision a cluster correctly. For those, we provide proper release management, documentation and testing, such that you can trust that minor upgrades go smoothly, or breaking changes are described and happening only in major releases.

On top the chart, we have the [`App` concept]({{< relref "vintage/getting-started/app-platform/app-bundle" >}}), a custom resource which helps us to select a chart to be installed in the management cluster allowing extended configuration capabilities that enhance the fleet management experience.

Learn more by reading how to [create your first workload cluster]({{< relref "vintage/getting-started/create-workload-cluster" >}}) or check the cluster apps we offer in our [catalog]({{< relref "vintage/use-the-api/management-api/cluster-apps" >}}).
