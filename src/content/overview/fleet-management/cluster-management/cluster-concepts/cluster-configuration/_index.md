---
title: Cluster configuration
description: Explanation of how cluster configuration works in Cluster API and how you can customize it.
weight: 10
menu:
  principal:
    parent: overview-fleetmanagement-clustermanagement-concepts
    identifier: overview-fleetmanagement-clustermanagement-concepts-configuration
last_review_date: 2024-08-28
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - What is cluster configuration in the Giant Swarm platform?
  - How can I customize the configuration of a cluster in the Giant Swarm platform?
---

The cluster configuration is managed thanks to the [app platform]({{< relref "/vintage/getting-started/app-platform/app-configuration" >}}) configuration options.

In the cluster, there are 3 main configuration sources:

- Default provider-independent app configuration (comes from cluster chart; if some app has this, then this should probably be moved directly to the app repository itself)
- Provider-specific app configuration (comes from cluster-<provider>)
- Customer-specified app configuration (come from cluster-<provider> Helm values, it's probably specified in customer's GitOps repository).
