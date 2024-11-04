---
title: Architecture of the Giant Swarm cloud-native developer platform
linkTitle: Architecture of the platform
description: Components, capabilities, supported cloud providers, and the platform API.
weight: 20
menu:
  principal:
    parent: overview
    identifier: overview-architecture
user_questions:
  - What is the architecture of the Giant Swarm cloud-native developer platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-planeteers
last_review_date: 2024-11-04
---

Giant Swarm's cloud-native platform is a collection of open-source components that work together to provide a seamless experience for managing the lifecycle of containerized applications. The platform is designed to be cloud-agnostic, allowing you to deploy your applications on any of the supported cloud providers. Besides, the platform offers a rich set of APIs that our customers can use to offer a set of self-service capabilities to their developers.

## Platform architecture

![Platform architecture](./platform-architecture.png)

The platform architecture consists of the following layers:

- Infrastructure layer: responsible for managing the underlying infrastructure, including the cloud provider resources or on-premises infrastructure. To abstract the underlying infrastructure, the platform uses the `Kubernetes`.

- Capabilities layer: provides a set of capabilities to manage the lifecycle of applications, including deploying, scaling, and monitoring applications.

- Interface layer: offers a set of templates, APIs, and tools that developers can use to interact with the platform.

Along these layers, Giant Swarm provides a real support channel, incident management, and good documentation to help you get the most out of the platform. Additionally, you have a dedicated account engineer to help creating a common roadmap and to provide guidance on how to use the platform.

## Platform API

The Giant Swarm platform is build on top of `Kubernetes` thanks to [`Cluster API`](https://cluster-api.sigs.k8s.io/), a open source  project that standardize the cluster lifecycle management across different cloud providers or on-premises infrastructure.

In `Cluster API`, there is a distinction between the management cluster and the workload clusters. The management cluster is responsible for managing the lifecycle of the workload clusters. The workload clusters are the clusters where you deploy your applications.

In Giant Swarm, the management cluster is also used for enhancing the platform capabilities, such as monitoring, logging, and alerting. The customer platform team uses the management cluster to configure which capabilities are available to the developers, and even to create new capabilities.

Most often, you have a single management cluster that manages multiple workload clusters, but in case of running infrastructure in multiple regions, you can have multiple management clusters. The platform API isn't more than the `Kubernetes` management cluster API, but with some additional resources that allow you to manage the lifecycle of your workloads across multiple clusters or inspect the application metrics of your fleet of clusters.

[Learn how to access the platform API]({{< relref "/getting-started/access-to-platform-api" >}}).

## GitOps

Giant Swarm uses GitOps as first-class citizen to manage the lifecycle of cluster, applications and so on.

## Developer portal

The developer portal allows platform engineers and developers to interact with the platform in a visual way. It provides a set of templates and tools that developers can use to deploy and manage their applications.

## Observability

## Single sign-on

## Network and connectivity

## Runtime security

## Cost management

## Automatic cluster management

## Cluster scaling

## Cloud resources provisioning
