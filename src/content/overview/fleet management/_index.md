---
title: Fleet management
description: Supported cloud providers and management of clusters on the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview
    identifier: overview-fleet-management
last_review_date: 2024-04-18
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Our experience tells us that managing a large microservices platform is not easy. Ideally, workloads are created ready to run in the cloud and are optimized for the container lifecycle. But even so, when you need to manage several providers, regions and environments, the complexity multiplies exponentially. Having that in mind, we have created a some abstractions to help you dealing with that complexity in a more efficient way.

## Features

The Giant Swarm platform offers these fleet management features:

- **Multi-environment**: Deploy to multiple providers, regions and environments. Platform engineers can [[[map their company structure to our platform structure]]] <== I HAVE NO IDEA WHAT THIS MEANS in order to ease the management of their teams and workloads.
- **Configuration management**: Manage configuration of your clusters, environments and workloads with GitOps, a versioned, single source of truth repository that shows the currently deployed state.
- **Cluster lifecycle management**: Creation and deletion of clusters is only a matter of minutes. Giant Swarm offers well-tested releases so make upgrades smooth and fully-automated. Scaling features for clusters are built-in.
- **Workload management**: We have developed a solution to help your developers to configure and deploy their applications in a cloud-native way.

## Cloud-native applications

The Giant Swarm platform uses [Cluster API](https://cluster-api.sigs.k8s.io/), an open-source, well-supported subproject of Kubernetes, to manage the lifecycle of your clusters. Together with the app platform, we provide a way to manage your workloads in a [[[cloud-native way]]] <= VAGUE TERM WHICH NEWCOMERS TO THE K8S WORLD MAY NOT UNDERSTAND LET'S RATHER EXPLAIN BENEFITS EXPLICITLY.
