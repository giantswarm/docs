---
title: Cluster configuration
description: Explanation of how cluster configuration works in Cluster API and how you can customize it.
weight: 10
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-configuration
last_review_date: 2026-06-22
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
