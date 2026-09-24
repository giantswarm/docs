---
linkTitle: Cluster app charts
title: Cluster app charts
description: These charts are used to provision clusters in the Giant Swarm platform (here, even clusters are apps, in a way).
weight: 100
menu:
  principal:
    identifier: container-platform-reference-platform-api-cluster-apps
    parent: container-platform-reference-platform-api
last_review_date: 2024-10-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-planeteers
aliases:
  - /reference/platform-api/cluster-apps/
---

Note that we maintain one provider-agnostic chart named `cluster` that has most configuration options, while the provider-specific ones (named in the form `cluster-PROVIDER`) only add options specific to the respective provider.

See [Create a workload cluster]({{< relref "/container-platform/getting-started/provision-your-first-workload-cluster" >}}) to learn how to create clusters.
