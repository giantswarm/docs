---
linkTitle: Management clusters
title: Management clusters
description: The role Management Clusters perform in the Giant Swarm architecture and how they are updated.
weight: 50
menu:
  main:
    identifier: management-clusters
    parent: general
last_review_date: 2021-02-19
user_questions:
  - How does Giant Swarm use Management Clusters?
  - How are Management Clusters kept up to date?
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
---

## Overview

As we are fully convinced of Kubernetes as a platform for building platforms, we build all our management clusters based on Kubernetes. Giant Swarm leverages the concept of [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) to control all resources that clusters need as [“Custom Resources”](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

As well as operators, our management clusters run supporting components such as our monitoring stack and our [web UI]({{< relref "/ui-api/web" >}}). All components are deployed using the Giant Swarm [App Platform]({{< relref "/app-platform/overview" >}}).

## Workload Cluster releases

Our workload clusters are versioned using [workload cluster releases]({{< relref "/general/releases" >}}). From a workload cluster point of view, upgrades are described in [cluster upgrades]({{< relref "/general/cluster-upgrades" >}}).

When we publish a new workload cluster release, we create a new [Release]({{< relref "/ui-api/management-api/crd/releases.release.giantswarm.io.md" >}}) custom resource and any new operator versions are deployed to the management cluster.

We deploy new instances of the operators with this new version, via the [release-operator](https://github.com/giantswarm/release-operator/) to avoid impacting existing workload clusters. These new operators will not become active until existing workload clusters are upgraded or a new cluster is created.

## Management cluster-only components

There are a number of components that are not a part of a workload cluster release, such as our monitoring stack, or web UI. These components are deployed exclusively to the management cluster, and do not affect workload clusters.

These components are deployed via app collections, which are a set of App custom resources, which are ultimately deployed via the App Platform. This collection contains the latest tagged version of each component, and is managed by our deployment component [draughtsman](https://github.com/giantswarm/draughtsman/).

These management cluster-only components are tested on our internal management clusters before releases are cut.

We plan on replacing draughtsman in Q2 2021, with a new component that more natively synchronises app collections to a management cluster, mostly to improve the scalability of the system.

## Configuration changes

Periodically, we need to update the configuration for management clusters.

This configuration is currently held in a ConfigMap and a Secret stored on the Management Cluster. When updates are required, these resources are updated manually using our current tooling, from our central configuration repository.

These configuration files are watched by the App Platform, and any necessary applications are reconfigured on changes.

Changes to configuration are tested on our internal management clusters before being applied.

This configuration system is being updated in Q1 2021, with a system based on the new [config-controller](https://github.com/giantswarm/config-controller/). This will remove the need for manual updates of configuration, remove the shared ConfigMap and Secret, and allow for versioning of configuration. Overall, aiming to further increase the safety, reliability, and scalability of configuration changes.

## Infrastructure upgrades

The management cluster infrastructure, such as the Kubernetes cluster itself, or other supporting resources such as bastion hosts, are managed using Terraform.

Updates to our Terraform modules are rolled out by CI as needed, with changes to our Terraform modules being tested on internal management clusters before being deployed.

In 2021, we plan to start reusing our own workload clusters as the clusters that base management clusters, to both avoid having to maintain two methods of provisioning clusters, but also to gain the reliability benefits of our workload clusters.
