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

[Cluster API]() is a Kubernetes sub-project that presents an innovative approach to creating, configuring, and managing clusters. It employs a declarative model, which means that users can define the desired state of their clusters, and the system will automatically work to achieve that state. This powerful tool offers a standard mechanism to handle Kubernetes clusters, simplifying operations and increasing efficiency.

Cluster API leverages the concept of operators and Custom Resource Definitions (CRDs) to manage Kubernetes clusters. An operator in Kubernetes is a method of packaging, deploying, and managing a Kubernetes application. In the context of Cluster API, an operator is essentially a controller that responds to cluster lifecycle events, allowing for automated creation, configuration, and management of clusters.

Custom Resource Definitions (CRDs) are extensions of the Kubernetes API that allow the creation of new custom resources - in this case, the cluster resources. When a user defines a cluster configuration using these custom resources, the Cluster API operator reacts to this declarative statement and works to achieve the desired state of the cluster. This includes tasks such as provisioning infrastructure, bootstrapping nodes, and applying configurations. The use of operators and CRDs not only automates these processes but also provides a consistent and standardized way to manage clusters, reducing complexity and increasing efficiency.

## Giant Swarm Adoption

In our platform we offer the Cluster API features with some addtional sugar to complete some capabilities we understand are needed to have a complete feature-set.

- DNS creation via operator
- IRSA or credentials creation...
- ...

Learn more reading how to [create your first workload cluster]()