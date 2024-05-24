---
title: Container registry within a management cluster
linkTitle: Container registry
description: Giant Swarm management clusters include a container registry that stores images for the platform and customer workloads. Workload clusters can make use of them to reduce bandwith usage, improve deployment speed, and increase resiliance.
weight: 100
menu:
  principal:
    parent: overview
    identifier: overview-architecture
user_questions:
  - Does the Giant Swarm platform provide a container registry?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-05-24
---

Outline

- In general, any accessible container registry can be used with the Giant Swarm platform.
- As of DATE, management clusters includes a container registry (Zot).
- The registry in the management cluster is used as a pull-through cache from management cluster nodes.
- The registry in the management cluster can also be used from workload clusters.
    - A basic use case is the pull-through cache.
        - TODO: link to tutorial for using the registry as pull-through cache.
    - Zot supports more advanced use cases. For example: active replication of upstream registries, to support intermittent connectivity scenarios. Giant Swarm will help customers to set up such advanced use cases.
- Benefits of using the registry in the management cluster:
    - Reduced bandwidth usage
    - Reduced cost for upstream registry pulls
    - Improved deployment speed
    - Increased resilience
- Noteworthy:
    - The registry in the management cluster is not intended for long-term storage of images.
    - Storage is limited, but can be adjusted according to customer needs.
    - TODO: something about access control and security.
- Giant Swarm provides a Zot app to deploy a registry in workload clusters.
    - This might be useful for installations with large clusters and a need for more flexibility.
