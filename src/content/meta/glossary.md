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
  - "What is a platform operator?"
  - "What is smart platform engineering?"
  - "What is a workload cluster?"
---

We use a set of terms across our documentation that could be unclear to readers. In the following article we define those terms to clarify their meaning in the context of Giant Swarm.

## Cloud native developer platform

A cloud-native developer platform is an integrated collection of capabilities exposed through intuitive interfaces that facilitate the application development lifecycle. It offers flexible configuration to build a system that encodes your company practices. It integrates with different open source solutions to enable automation, connectivity, observability, and security for your workloads.

## Developer environment

In our context, a developer environment is the entity that defines the space where the developers will deploy their applications. It can be mapped to a Kubernetes namespace(s) or a cluster. The Platform capabilities like access management, security or observability are related to those environments.

## Management cluster

It is a Kubernetes cluster that acts a central point of the platform. It is in charge of hosting platform wide services like observability or security to ensure visualization and compliance over all the workloads in all clusters. [Platform operator](#platform-operator) have access to the its [API](#platform-api) to manage [workload clusters](#workload-cluster) and [managed apps](#managed-apps).

## Managed app

The managed apps are a set of curated components that can optionally be used in the [platform](#cloud-native-developer-platform) to enable diverse capabilities across the [developer environments](#developer-environment). As an example, in case the developers want to dynamically allocate DNS records for their services, they can leverage [external-dns](https://github.com/giantswarm/external-dns-app/). The managed apps are operated by us and we provide regular upgrades to avoid security vulnerabilities and bugs.

## Platform API

The Platform API is the entrypoint of Giant Swarm's [cloud-native developer platform](#cloud-native-developer-platform). Everything in the platform is exposed via the Platform API, allowing the automation of processes, including GitOps support, and fostering standardization. The Platform API is the Kubernetes API of the Management Cluster, extended with custom resources such as [`App`](#managed-apps] to enable a variety of use cases. [Learn more here](#future-link-to-platform-api-intro-page).

## Platform operator

The platform team is a team that is in charge of providing the [cloud-native developer platform](#cloud-native-developer-platform). With the help of Giant Swarms managed platform they compose, manage and customize the platform for the specific needs of the development teams within their company.

## Smart platform engineering

Smart Platform Engineering is the design and development of intelligent platforms that help create a developer platform for your teams. Instead of starting from scratch and building an entire platform piece by piece while running it 24/7, use our knowledge, products and support to achieve your goals faster.

## Workload cluster

The customer platform teams can define several clusters where the developers can run their applications based on different requirements like location, stage or isolation.
