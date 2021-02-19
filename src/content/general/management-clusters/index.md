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

Users have direct access to the Kubernetes API of the management cluster. The gives full access to the automation we've built into our operators, as well as visibility into the components running within the management cluster. Documentation can be found [here]({{< relref "/ui-api/management-api/" >}}).

We do not support the upstream Cluster API for all our providers yet, but are fully committed to supporting this open standard soon.

## Workload Cluster releases

Our workload clusters are versioned using [workload cluster releases]({{< relref "/general/releases" >}}). From a workload cluster point of view, upgrades are described in [cluster upgrades]({{< relref "/general/cluster-upgrades" >}}).

A core focus of development in our versioning approach is to guarantee stability and reliability. Our upgrades follow a lockstep approach, where we move from one tested set of versions of our components to the next set of versions of our components. This strict versioning also allows you to test out new versions, test upgrades, and even integrate cluster creation into your own CI, such as to run integration tests.

When we publish a new workload cluster release, we create a new [Release]({{< relref "/ui-api/management-api/crd/releases.release.giantswarm.io.md" >}}) custom resource, which is deployed to the management cluster, and any new operator versions are also subsequently deployed. All release definitions can be found at [giantswarm/releases](https://github.com/giantswarm/releases).

To make sure that existing workload clusters aren't affected by new versions, our operators are immutable. With each new release, we deploy new instances of the operators with the new version, via the [release-operator](https://github.com/giantswarm/release-operator/), which avoids impacting existing workload clusters. These new operators will not become active until existing workload clusters are upgraded or a new cluster is created. Overall, this entails that the operators are versioned together with the cloud provider infrastructure and component versions (e.g: Kubernetes, CoreDNS, etc.) of the cluster itself, with the new operators taking over when the cluster is upgraded to the new version.

## Management cluster-only components

There are a number of components that are not a part of a workload cluster release, such as our monitoring stack, or web UI. These components are deployed exclusively to the management cluster, and do not affect workload clusters.

These components are deployed via app collections, which are a set of App custom resources, which are ultimately deployed via the App Platform. This collection contains the latest tagged version of each component, and is managed by our deployment component [draughtsman](https://github.com/giantswarm/draughtsman/).

These management cluster-only components are tested on our internal management clusters before releases are cut.

We plan on replacing draughtsman in Q2 2021, with a new component that more natively synchronises app collections to a management cluster, mostly to improve the scalability of the system.

## Configuration changes

Periodically, we need to update the configuration for management clusters.

This configuration is currently held in a ConfigMap and a Secret stored on the management cluster. When updates are required, these resources are updated manually using our current tooling, from our central configuration repository.

These configuration files are watched by the App Platform, and any necessary applications are reconfigured on changes.

Changes to configuration are tested on our internal management clusters before being applied.

This configuration system is being updated in Q1 2021, with a system based on the new [config-controller](https://github.com/giantswarm/config-controller/). This will remove the need for manual updates of configuration, remove the shared ConfigMap and Secret, and allow for versioning of configuration. Overall, aiming to further increase the safety, reliability, and scalability of configuration changes.

## Infrastructure upgrades

The management cluster infrastructure, such as the Kubernetes cluster itself, or other supporting resources such as bastion hosts, are managed using Terraform.

Updates to our Terraform modules are rolled out by CI as needed, with changes to our Terraform modules being tested on internal management clusters before being deployed.

In 2021, we plan to start reusing our own workload clusters as the clusters that base management clusters, to both avoid having to maintain two methods of provisioning clusters, but also to gain the reliability benefits of our workload clusters.
