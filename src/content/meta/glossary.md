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

## Cloud native developer platform

A cloud-native developer platform is an integrated collection of capabilities exposed through intuitive interfaces that facilitate the application development lifecycle. It offers flexible configuration to build a system that encodes your company practices. It integrates with different open source solutions to enable automation, connectivity, observability, and security for your workloads. You may be familiar with the term ["internal developer platform"](https://internaldeveloperplatform.org/) which is fairly similar but in our case we emphasize the betting for cloud-native technologies to accomplish the desired goals.

## Developer environment

In our context, a developer environment defines the space where developers will deploy their applications. It can be mapped to a particular namespace or cluster. Platform capabilities like access management, security, or observability are related to those environments.

## Managed app

The managed apps are a set of curated components that can optionally be used in the [platform](#cloud-native-developer-platform) to enable diverse capabilities across the [developer environments](#developer-environment). As an example, in case the developers want to dynamically allocate DNS records for their services, they can leverage [external-dns](https://github.com/giantswarm/external-dns-app/). The managed apps are operated by us and we provide regular upgrades to avoid security vulnerabilities and bugs.

## Management cluster

A management cluster is a Kubernetes cluster that acts as a central management point of the platform. This cluster hosts platform-wide services for GitOps, observability, security and user management to ensure automation and visibility of the workloads across all clusters. Users can create new clusters via a Management Cluster. [Platform engineers](#platform-engineers) usually have access to the [API](#platform-api) of the management cluster to manage [workload clusters](#workload-cluster) and services of the platform.

## Platform API

The Platform API is the entrypoint of Giant Swarm's [cloud-native developer platform](#cloud-native-developer-platform). Everything in the platform is exposed via the Platform API, allowing the automation of processes, including GitOps support, and fostering standardization. The Platform API is the Kubernetes API of the Management Cluster, extended with custom resources such as [`App`](#managed-apps] to enable a variety of use cases. [Learn more here](#future-link-to-platform-api-intro-page).

## Platform team

The platform team is in charge of providing a [cloud-native developer platform](#cloud-native-developer-platform). With the help of the Giant Swarms managed platform, they compose, manage and customize the platform for the specific needs of the development teams within their company.

## Smart platform engineering

Smart Platform Engineering is designing and developing intelligent platforms that help create a developer platform for your teams. Instead of starting from scratch and building an entire platform piece by piece while running it every day, use our knowledge, products and support to achieve your goals faster.

## Workload cluster

The customer platform teams can define several clusters where the developers can run their applications based on different requirements, such as location (Ireland, US, China), stage (development, staging, production), or isolation (payments, e-commerce).
