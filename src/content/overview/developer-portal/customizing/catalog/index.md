---
title: Adding your own catalog
linkTitle: Catalog
description: How to add your own catalog entities to the developer portal provided by Giant Swarm, for your own users, groups, components, and more.
weight: 30
menu:
  principal:
    parent: overview-developer-portal-customizing
    identifier: overview-developer-portal-customizing-catalog
last_review_date: 2025-04-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I have my own catalog entities in the developer portal?
---

The catalog is an important part of a Backstage portal. In the Giant Swarm developer portal, the catalog defines which software components are available to the users for further inspection. It also specifies which user groups and which users, mapped to the customer's identity provider, are to access the portal.

By default, Giant Swarm populates the catalog of your developer portal using the following sources:

- [Giant Swarm apps](https://github.com/giantswarm/backstage-catalogs/blob/main/catalogs/components.yaml) -- A catalog of apps Giant Swarm provides. Some of these are installed by default in management clusters or workload clusters in the Giant Swarm platform. Others are available for you to install in your clusters on demand.
- [Giant Swarm users](https://github.com/giantswarm/backstage-catalogs/blob/main/catalogs/users.yaml) -- A directory of staff members of Giant Swarm. This catalog exists to allow Giant Swarm members to access your developer portal.
- [Giant Swarm teams](https://github.com/giantswarm/backstage-catalogs/blob/main/catalogs/groups.yaml) -- A directory of teams at Giant Swarm. This catalog exists to help you identify owners of applications provided by Giant Swarm.

All of the above collections are placing entities in the `giantswarm` namespace of the catalog, to avoid any conflicts with your own entities.

We expect you to want to extend the catalog with your own software components, teams, and users, and even more entities. Please contact us to discuss your needs.

## Further reading

- [The Backstage software catalog](https://backstage.io/docs/features/software-catalog/)
