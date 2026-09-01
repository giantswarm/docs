---
linkTitle: Cluster configuration
title: Cluster configuration
diataxis_content_type: explanation
description: Explanation of how cluster configuration works in Cluster API and how you can customize it.
weight: 10
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-configuration
last_review_date: 2026-08-19
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - What is cluster configuration in the Giant Swarm platform?
  - How can I customize the configuration of a cluster in the Giant Swarm platform?
---

Cluster configuration is managed through the [app platform]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}) configuration options.

A cluster has **three main configuration sources**:

- **Default, provider-independent app configuration.** This comes from the cluster chart. If an app carries this configuration, you should probably move it directly to the app's own repository.
- **Provider-specific app configuration.** This comes from `cluster-<provider>`.
- **Customer-specified app configuration.** This comes from the `cluster-<provider>` Helm values. It's usually specified in the customer's GitOps repository.

## Where the defaults come from

The interface to define a workload cluster is built on top of Helm and [the app platform]({{< relref "/overview/fleet-management/app-management/" >}}). Creating a cluster means delivering a configured `App` resource to the platform API.

Those definitions come from the cluster provider Helm template, [`cluster-aws`](https://github.com/giantswarm/cluster-aws) for example. That chart carries the provider-specific definition, and depends on two more charts:

- [`cluster`](https://github.com/giantswarm/cluster) holds the basic provider-agnostic definition.
- [`cluster-shared`](https://github.com/giantswarm/cluster-shared) holds the common resources that every cluster runs by default.

The chain is therefore `cluster-<provider>` → `cluster` → `cluster-shared`, with each link contributing part of what a cluster ends up being.

## How the configuration layers merge

Cluster configuration builds on the [app platform configuration levels]({{< relref "/tutorials/fleet-management/app-platform/app-configuration/#levels" >}}):

- The cluster template provides a default configuration through the `App` resource's `config` field.
- You add custom configuration through the `App` resource's `extraConfigs` field, which is overlaid on top of the default `config`. Where values collide, the entry with the higher priority prevails.

**Note**: [The RFC on merging configmaps in GitOps](https://github.com/giantswarm/rfc/tree/main/merging-configmaps-gitops) explains why we chose this approach.

To apply this with reusable Kustomize bases, see [creating a base template for your workload cluster]({{< relref "/tutorials/continuous-deployment/bases/" >}}).
