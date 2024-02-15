---
linkTitle: REST API (deprecated)
title: The Giant Swarm REST API (deprecated)
description: An overview of the APIs that provide you with programmatic access to resources like your workload clusters in a Giant Swarm installation. Namely the Rest API and the Management API.
weight: 50
menu:
  main:
    parent: use-the-api
user_questions:
  - How can I manage Giant Swarm resources programmatically?
  - How can I manage clusters via an API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
last_review_date: 2023-08-29
aliases:
  - /reference/rest-api/
  - /ui-api/rest-api/
---

The REST API has been designed originally to provide a simple, easy to use interface to the relevant resources for managing clusters, key pairs, etc. while keeping the internals under the hood.

Since its inception at Giant Swarm, we learned that there are always more use cases emerging on our customer's side than we could anticipate in our REST API design. We realized that the best we can do to provide full insight into the state and spec of your infrastructure is by opening up the underlying system itself.

With this realization, we made the decision to **phase out the development of the REST API** in favor of providing access to the [Management API]({{< relref "/vintage/use-the-api/management-api" >}}) instead.

As of now, there is no termination date for the REST API. It is however **not available anymore for [newer generations of the platform]({{< relref "/vintage/platform-overview/cluster-management/cloud-provider-implementations" >}})**.

## Further reading

- [REST API documentation](/api/)
