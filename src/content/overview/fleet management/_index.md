---
title: Fleet management
description: Supported cloud providers and management of clusters on the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview
    identifier: overview-fleet-management
last_review_date: 2024-05-10
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Our experience tells us that managing a large microservices platform is not easy. Ideally, workloads are created ready to run in the cloud and are optimized for the container lifecycle. But even so, when you need to manage several providers, regions and environments, the complexity multiplies exponentially. Having that in mind, we have created a some abstractions to help you dealing with that complexity in a more efficient way.

## Features

The fleet management features that our product offers are:

- **Multi-environment**: We support multiple providers, regions and environments. Platform engineers can map their company structure to our platform structure in order to ease the management of their teams and workloads.
- **Configuration management**: We rely on GitOps principles to manage the configuration of your clusters, environments and workloads having multiple layers of configuration.
- **Cluster lifecycle management**: We provide a way to manage the lifecycle of your clusters, from creation to deletion, including upgrades and scaling.
- **Workload management**: We have developed a solution to help your developers to configure and deploy their applications in a cloud-native way.

## Cloud-native applications

We have rely on [Cluster API implementation]({{ relref "" }}) to manage the lifecycle of your clusters. Together with the app platform, we provide a way to manage your workloads in a cloud-native way.
