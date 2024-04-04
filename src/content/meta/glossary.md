---
title: Glossary
description: A page with the term definitions Giant Swarm uses in the documentation.
search: false
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - "What is a cloud-native developer platform?"
  - "What is a developer environment?"
  - "What is a management cluster?"
  - "What is a managed app?"
  - "What is the platform API?"
  - "What is a platform team?"
  - "What is smart platform engineering?"
  - "What is a workload cluster?"
---

<!-- All headings must be sorted alphabetically -->

We use a set of terms across our documentation that could be unclear to readers. In the following article we define those terms to clarify their meaning in the context of Giant Swarm.

## Cloud native developer platform

A cloud-native developer platform is an integrated collection of capabilities exposed through intuitive interfaces that facilitate the application development lifecycle. It offers flexible configuration to build a system that encodes your company practices. It integrates with different open source solutions to enable automation, connectivity, observability, and security for your workloads. You may be familiar with the term ["internal developer platform"](https://internaldeveloperplatform.org/) which is fairly similar but in our case we emphasize the betting for cloud-native technologies to accomplish the desired goals.

## Developer environment

In our context, a developer environment is the entity that defines the space where the developers will deploy their applications. It can be mapped to a Kubernetes namespace(s) or a cluster. The Platform capabilities like access management, security or observability are related to those environments.

## Managed app

The managed apps are a set of curated diverse components that can be used in the [platform](#cloud-native-developer-platform) to enable capabilities across the [developer environments](#developer-environment). As an example, in case the developers want to allocate dynamically DNS records for their services they can leverage in [external-dns](https://github.com/giantswarm/external-dns-app/). The managed apps are operated by us and we provide regular upgrades to avoid security vulnerabilities and bugs.

## Management cluster

A management cluster is a Kubernetes cluster that acts as a central management point of the platform. This cluster hosts platform-wide services for GitOps, observability, security and user management to ensure automation and visibility of the workloads across all clusters. Users can create new clusters via a Management Cluster. [Platform engineers](#platform-engineers) usually have access to the [API](#platform-api) of the management cluster to manage [workload clusters](#workload-cluster) and services of the platform.

## Platform API

Is the entrypoint of the [cloud-native developer platform](#cloud-native-developer-platform). Everything in the platform is exposed via the API, allowing the automation of processes and fostering standardization. The [Platform API](#link-to-platform-api-page) is a fully compliant Kubernetes API extended with some custom resources to enable a variety of use cases. [Know more here](#future-link-to-platform-api-intro-page).

## Platform team

The platform team is the person or team that is in charge of the operation of the [cloud-native developer platform](#cloud-native-developer-platform). They are responsible for the management of the [management cluster](#management-cluster) and its capabilities.

## Smart platform engineering

Smart Platform Engineering refers to the design and development of intelligent platforms that help you to create the desired Developer Platform for your teams in a quick fashion. Instead of starting from scratch to build piece by piece an entire platform meanwhile you operate it 24/7, leverage in our knowledge, product and support to reach your goals in a decent amount of time.

## Workload cluster

The customer platform teams can define several clusters where the developers can run their applications based on different requirements like location (Ireland, US, China), stage (dev, staging, production) or isolation (payments, ecommerce).
