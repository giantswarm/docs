---
title: Developer portal introduction
linkTitle: Introduction
description: Our Backstage-based developer portal is your engineer's front end to the platform. We provide our self-service user interface as plugins for Backstage, so engineers using your platform find all the information they need in the right place.
weight: 1
menu:
  principal:
    parent: overview-developer-portal
    identifier: overview-developer-portal-introduction
last_review_date: 2025-04-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What is the Giant Swarm developer portal?
  - What is Backstage?
---

Our developer portal based on [Backstage](https://www.cncf.io/projects/backstage/) is your engineer's front end to the platform. We provide our self-service user interface as plugins for Backstage, so that engineers using your platform find all the information they need in the place they visit frequently.

Giant Swarm can assist you in various ways depending on where you are in your journey towards your own developer portal. We provide a pre-configured Backstage instance as a starting point to customers who don't run their own instance yet. We also provide plugins that can be used to extend the functionality of your Backstage instance.

## Why developer portals

The Giant Swarm platform combines capabilities provided by a variety of open source tools, and likely your engineers are using even more tools to accomplish their goals. Developer portals should serve as a single entry point and provide a navigation path to the tools engineers need access to. Furthermore, they can give an overview of the software landscape and the platform itself, make documentation and troubleshooting runbooks accessible, and assist in the creation of new services according to platform standards.

## Why Backstage

Backstage, originally developed by Spotify and donated to the Cloud Native Computing Foundation in 2020, is an open-source framework for building developer portals. With more than 1,500 contributors and a fast-paced release cycle, Backstage is improving and extending its capabilities rapidly. More and more enterprises are adopting Backstage as their foundation for developer portals, creating [plugins](https://backstage.io/plugins/) and open-sourcing them to the community.

## Capabilities

The pre-configured Backstage instance provides the following functionality:

- **Cluster overview**: An overview of all Kubernetes clusters managed through the Giant Swarm platform.
- **Catalog**: A catalog of all applications that Giant Swarm publishes in app catalogs. As a customer, you can extend this catalog with your own applications, services, and more.
- **Deployment details**: Where applicable, you get access to deployment information, showing the status of the respective service's deployment in your clusters.
- **Templates**: Fast and easy creation of new clusters, services, and more through templates.
