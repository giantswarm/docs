---
linkTitle: REST API
title: The Giant Swarm REST API
description: An overview of the APIs that provide you with programmatic access to resources like your workload clusters in a Giant Swarm installation. Namely the Rest API and the Management API.
weight: 50
menu:
  main:
    parent: use-the-api
user_questions:
  - How can I manage Giant Swarm resources programmatically?
  - How can I manage clusters via an API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
last_review_date: 2022-12-07
---

The REST API has been designed originally to provide a simple, easy to use interface to the relevant resources for managing clusters, key pairs, etc. while keeping the internals under the hood.

Since its inception at Giant Swarm, we learned that there are always more use cases emerging on our customer's side than we could anticipate in our REST API design. We realized that the best we can do to provide full insight into the state and spec of your infrastructure is by opening up the underlying system itself.

With this realization, we made the decision to **phase out the development of the REST API** in favor of providing access to the [Management API]({{< relref "/use-the-api/management-api" >}}) instead.

As of now, there is no termination date for the REST API. As it might provide a much simpler and more accessible starting point, feel free to explore the [REST API documentation](/api/), knowing that one day you may have to switch to the Management API.
