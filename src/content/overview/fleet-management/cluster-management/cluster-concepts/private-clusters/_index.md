---
title: Private clusters
description: Definition of what do we mean by private clusters in the Giant Swarm platform.
weight: 10
menu:
  principal:
    parent: overview-fleet-management-cluster-concepts
    identifier: overview-fleet-management-cluster-concepts-private
last_review_date: 2024-06-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are private clusters in the Giant Swarm platform?
---

When we talk about private clusters in the Giant Swarm platform, we refer to Kubernetes clusters which has not API endpoint exposed to the public internet. This means that the cluster is only accessible from within the private network of the organization that owns the cluster.
