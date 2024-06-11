---
title: Developer portal
description: The central Giant Swarm self-service portal for your platform engineers and developers.
weight: 30
menu:
  principal:
    parent: overview
    identifier: overview-developer-portal
last_review_date: 2024-06-11
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

The Giant Swarm Developer Portal is the central self-service portal for your platform engineers and developers. It provides access to all the tools and resources needed to manage and develop applications on your Giant Swarm platform.

Giant Swarm uses [Backstage](https://www.cncf.io/projects/backstage/) as the foundation for the developer portal. Backstage is an open-source platform for building developer portals. It provides a unified view of all your software development tools and services, navigate across the documentation even creating custom plugins to integrate with your existing tools.

## Managed capabilities

The Developer Portal provides the following features:

- **Service catalog**: a catalog of all the services available on your platform, including documentation, metrics, and other information.
- **Application management**: the ability to create golden paths or template to boost the application development process and the same time you can observe the status of your applications.
- **Documentation**: A central location for all your platform documentation, including guides, tutorials, and API references.
- **Metrics and monitoring**: basic metrics and monitoring capabilities for your applications and connection to extended monitoring tools.
- **Alerts and notifications**: define alerts and notifications for your applications and services in a common place.

## Cloud-native applications

In Giant Swarm we have been working hard to make Backstage run in our managed clusters to provide a central place for the platform. We are still working on how to integrate with the customer applications and services more and more.

Our belief is Backstage will grow in next years enabling more use cases so we invite you to collaborate with us to find those.
