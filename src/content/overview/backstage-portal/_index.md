---
title: Backstage portal
description: Backstage is your engineer's front end to the platform. We provide our self-service user interface as plugins for Backstage, so that engineers using your platform find all the information they need in the right place.
weight: 30
menu:
  principal:
    parent: overview
    identifier: overview-backstage-portal
last_review_date: 2024-07-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

[Backstage](https://backstage.io/) is your engineer's front end to the platform. We provide our self-service user interface as plugins for Backstage, so that engineers using your platform find all the information they need in the right place.

Depending on where you are in your journey towards your own Backstage portal, Giant Swarm can assist you in various ways. We provide a pre-configured Backstage instance as a starting point to customers who don't run their own instance yet. We also provide plugins that can be used to extend the functionality of your Backstage instance.

## Why developer portals

The Giant Swarm platform combines capabilities provided by a variety of open source tools, and likely your engineers are using even more tools to accomplish their goals. Developer portals should serve as a single entry point and provide a navigation path to the tools engineers need access to. Furthermore, they can give an overview of the software landscape and the platform itself, make documentation and troubleshooting runbooks accessible, and assist in the creation of new services according to platform standards.

## Why Backstage

Backstage, originally developed by Spotify and donated to the Cloud Native Computing Foundation in 2020, is an open-source framework for building developer portals. With more than 1.500 contributors and a fast-paced release cycle, Backstage is improving and extending its capabilities rapidly. More and more enterprises are adopting Backstage as their foundation for developer portals, creating [plugins](https://backstage.io/plugins/) and open-sourcing them to the community.

## Core features

Backstage as we provide it to customers and as we run it internally at Giant Swarm comes with a set of core features:

- **Cluster overview**: An overview of all Kubernetes clusters managed through the Giant Swarm platform.
- **Catalog**: A catalog of all applications that Giant Swarm publishes in app catalogs. As a customer, you can extend this catalog with your own applications, services, and more.
- **Deployment details**: Where applicable, you get access to deployment information, showing the status of the respective service's deployment in your clusters.
- **Templates**: Fast and easy creation of new clusters, services, and more through templates.
