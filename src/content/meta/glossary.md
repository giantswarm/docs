---
title: Glossary
description: A page with the term definitions Giant Swarm uses in the documentation.
search: false
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - "What is a Cloud Native Developer Platform?"
  - "What is a Developer Environment?"
  - "What is a Management Cluster?"
  - "What is a Managed App?"
  - "What is the Platform API?"
  - "What is a Platform Operator?"
  - "What is Smart Platform Engineering?"
  - "What is a Workload Cluster?"
---

We used a set of terms across our documentation that could be no clear to readers. In the following article we define of those terms to clarify the complexity that could carry.

## Cloud Native developer platform

A Cloud Native Developer Platform is an integrated collection of capabilities exposed by intuitive interface that facilitates the application development lifecycle. It offers a flexible configuration to build a system that encodes your company practices. It integrates with different open source solutions to enable automation, observability and security for your workloads.

## Developer environment

In our context, a developer environment is the entity that defines the space where the developers will deploy their applications. It can be mapped to a Kubernetes namespace(s) or a cluster. The Platform capabilities like access management, security or observability are related to those environments.

## Management cluster

It is a Kubernetes cluster that acts a central point of the platform. It is in charge of hosting platform wide services like observability or security to ensure visualization and compliance over all the workloads in all clusters. [Platform operator](#platform-operator) have access to the its [API](#platform-api) to manage [workload clusters](#workload-cluster) and [managed apps](#managed-apps).

## Managed app

The managed apps are a set of curated diverse components that can be used in the [platform](#cloud-native-developer-platform) to enable capabilities across the [developer environments](#developer-environment). As an example, in case the developers want to allocate dynamically DNS records for their services they can leverage in [external-dns](https://github.com/giantswarm/external-dns-app/). The managed apps are operated by us and we provide regular upgrades to avoid security vulnerabilities and bugs.

## Platform API

Is the entrypoint of the [Cloud Native Developer Platform](#cloud-native-developer-platform). Everything in the platform is exposed via the API, allowing the automation of processes and fostering standardization. The Platform API is a fully compliant Kubernetes API extended with some custom resources to enable a variety of use cases. [Know more here](#future-link-to-platform-api-intro-page).

## Platform operator

The platform operator is the person or team that is in charge of the operation of the [Cloud Native Developer Platform](#cloud-native-developer-platform). They are responsible for the management of the [management cluster](#management-cluster) and its capabilities.

## Smart platform engineering

Smart Platform Engineering refers to the design and development of intelligent platforms that help you to create the desired Developer Platform for your teams in a quick fashion. Instead of starting from scratch to build piece by piece an entire platform meanwhile you operate it 24/7, leverage in our knowledge, product and support to reach your goals in a decent amount of time.

## Workload cluster

The customer platform teams can define several clusters where the developers can run their applications based on different requirements like location, stage or isolation.
