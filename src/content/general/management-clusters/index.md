---
linkTitle: Management clusters
title: Management clusters
description: The role Management Clusters perform in the Giant Swarm architecture and how they are updated.
weight: 50
menu:
  main:
    identifier: management-clusters
    parent: general
last_review_date: 2021-02-17
user_questions:
  - How do Giant Swarm use Management Clusters?
  - How are Management Clusters kept up to date?
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
---

## Overview

As we are fully convinced of Kubernetes as a platform for building platforms, we build all our management clusters based on Kubernetes. Giant Swarm leverages the concept of [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) to control all resources that clusters need as [“Custom Resources”](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/).

As well as operators, our management clusters run supporting components such as our monitoring stack and our [web UI]({{< relref "/ui-api/web" >}}). All components are deployed using the Giant Swarm [App Platform]({{< relref "/app-platform/overview" >}}).

## Workload Cluster releases

Our workload clusters are versioned using [workload cluster releases]({{< relref "/general/releases" >}}). From a workload cluster point of view, upgrades are described in [cluster upgrades]({{< relref "/general/cluster-upgrades" >}}).

When we publish a new Giant Swarm release, we create a new release custom resource and any new operator versions are deployed to the management cluster.
We deploy new instances of the operators with the new version to avoid impacting existing workload clusters. These new operators will not become active until existing workload clusters are upgraded or a new cluster is created.

## Management cluster-only components

The components that are not part of a workload cluster release -- like our monitoring stack -- are deployed via app collections. We run the latest version of each component and the collection is managed by our legacy deployment component called draughtsman (which we plan to retire in Q2 2021).

The components are deployed as App custom resources using our App Platform. Changes are tested in a number of internal management clusters before being deployed to all management clusters.

## Configuration changes

From time to time, we also need to update the configuration for management clusters. These changes are also tested on our internal management clusters before being applied.

## Infrastructure upgrades

The infrastructure including the management cluster nodes and supporting resources like bastion hosts are managed by our SRE team using Terraform.

However, we plan to move more of this provisioning to operators, reusing the components that manage our workload clusters where possible. As they continuously reconcile the cluster to its desired state, operators are more dynamic than Terraform and other tools such as Kops.
