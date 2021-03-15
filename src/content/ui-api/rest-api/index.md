---
linkTitle: REST API
title: The Giant Swarm REST API
description: An overview of the APIs that provide you with programmatic access to
  resources like your workload clusters in a Giant Swarm installation. Namely the Rest
  API and the Management API.
weight: 50
menu:
  main:
    parent: ui-api
user_questions:
  - How can I manage Giant Swarm resources programmatically?
  - How can I manage clusters via an API?
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# The Giant Swarm REST API

The Giant Swarm REST API is an abstraction over the many resources that reside in the management cluster of a Giant Swarm installation. It is used by our dedicated user interfaces, the web user interface and gsctl.

Browse our [API documentation](/api/) for a complete overview into the provided functionality.

The REST API was originally designed to provide a simpler, easier access to the relevant resources for managing clusters, key pairs, etc. while keeping the internals under the hood. However at Giant Swarm we learned that there are always more use cases emerging on your side than we could anticipate in our API design. We realized that the best we can do for you to provide full insight into the state and spec of your infrastructure is by opening up the underlying system itself.

With this realization, we made the decision to phase out the development of the REST API in favor of providing access to the [Management API]({{< relref "/ui-api/management-api" >}}) instead.

As of now, there is no termination date for the REST API. As it might provide the much simpler and more accessible starting point, feel free to explore the [documentation](/api/), knowing that one day you may have to switch to the Management API.
