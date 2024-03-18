---
title: Introduction to Cluster API
description: A throughout explanation of how our platform implements Cluster API standard.
weight: 100
last_review_date: 2024-03-07
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How does Giant Swarm serve Cluster API features?
  - What other services are needed in a platform to complete Cluster API?
---

The [Cluster API project](https://cluster-api.sigs.k8s.io/) is indeed a Kubernetes sub-project that presents an innovative approach to provisioning, configuring, and managing clusters. It employs a declarative model, which means that users can define the desired state of their clusters, and the system will automatically work to achieve that state. This powerful tool offers a standard mechanism to handle Kubernetes clusters, simplifying operations and increasing efficiency.

Cluster API leverages the concept of operators and Custom Resource Definitions (CRDs) to manage Kubernetes clusters. An operator is essentially a controller that responds to cluster lifecycle events, allowing for automated creation, configuration, and management of clusters.

Custom Resource Definitions (CRDs) are extensions of the Kubernetes API that allow the creation of new resources - in this case, the cluster resources. When a user defines a cluster configuration using these custom resources, the Cluster API operator reacts to this declarative statement and works to achieve the desired state of the cluster. This includes tasks such as provisioning infrastructure, bootstrapping nodes, and applying configurations.

## Giant Swarm flavour

In our platform we offer the Cluster API features with some additional sugar on top to complete some capabilities we consider as must-have for a complete production system. Next we list the features coming with our Cluster API implementation:

- Certificate management: Cluster API does provide a way to manage certificates that are needed for all components in a Kubernetes cluster like kubelet or etcd.
- Node bootstrap: the implementation generates a cloud-init file that is used to bootstrap the nodes in the cluster.
- Infrastructure provisioning: the operator talks to the provider specfic API to create the infrastructure needed for the cluster.
- Cluster autoscaling: by default Cluster API integrates with the [cluster autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) project to allow clusters to grow or shrinks based on different policies.
- Health checks: the operator is able to check the health of the machines and take actions to avoid manual intervention.

On top of that, we have some additional features that are not part of the Cluster API standard:

- DNS management: we provide a DNS operator to create DNS assets for the clusters.
- Provider credentials management: our implementation has the ability to configure credentials needed to talk to the provider API.
- Encryption configuration: we have create an operator that deals with all the logic needed to create cryptographic assets and configure them properly making sure they are rotated and updated as needed.
- Cluster API monitoring: we have a extended service that is able to monitor the cluster API specific resources.
- Further, we have some other operators that are provider specific and helps to automate all parts of the cluster lifecycle like VPC provisioning, security groups, etc.

## Wrapping resources in apps

Once you want to create a cluster, you will need to define a set of resources that will be used to create the cluster. Obviously, you can create these resources manually exploring every single specification field that is possible to use, but we offer a more convenient way to do that. We have a set of apps that are ready to be used to provision a cluster correctly.

An [`App` is custom resource]() which help us to group the all needed resources allowing expose the configuration in way it can be validated, defaulted and documented properly.

Learn more reading how to [create your first workload cluster]() or check the cluster app definitions we offer in our [catalog]()