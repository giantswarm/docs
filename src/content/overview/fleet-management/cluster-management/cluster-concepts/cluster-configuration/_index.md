---
title: Cluster configuration
description: How cluster configuration works and how can it be customized.
weight: 10
menu:
  principal:
    parent: overview-fleet-management-cluster-concepts
    identifier: overview-fleet-management-cluster-concepts-configuration
last_review_date: 2024-08-28
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - What is cluster configuration in the Giant Swarm platform?
  - How can I customize the configuration of a cluster in the Giant Swarm platform?
---

The cluster configuration is managed thanks to the [app platform]({{< relref "/vintage/getting-started/app-platform/app-configuration" >}}) configuration options.

In the cluster, there are 3 main configuration sources:

- Default provider-independent app config (comes from cluster chart; if some app has this, then this should be probably moved directly to the app repo itself)
- Provider-specific app config (comes from cluster-<provider>)
- Customer-specified app config (come from cluster-<provider> Helm values, it is probably specified in customer's gitops repo).
