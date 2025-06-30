---
title: Multi-tenancy
description: Learn about multi-tenancy concepts and implementation in the Giant Swarm observability platform.
weight: 10
menu:
  principal:
    parent: overview-observability-configuration
    identifier: overview-observability-configuration-multi-tenancy
last_review_date: 2025-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is multi-tenancy in observability?
  - How do I implement multi-tenancy?
  - How do I create Grafana organizations?
  - What are the multi-tenancy concepts?
---

Multi-tenancy in the Giant Swarm observability platform enables secure data isolation and access controls across teams, environments, and projects. This section covers both the conceptual foundation and practical implementation of multi-tenancy.

## Understanding multi-tenancy

Learn the core concepts behind multi-tenancy in the observability platform:

- **[Multi-tenancy concepts]({{< relref "/overview/observability/configuration/multi-tenancy/concepts" >}})**: Understand tenants, organizations, and how they work together to provide data isolation and access control

## Implementing multi-tenancy

Put multi-tenancy into practice:

- **Creating Grafana organizations**: Step-by-step guide to create and configure Grafana organizations for your teams

## Getting started

1. **Understand the concepts**: Start with [multi-tenancy concepts]({{< relref "/overview/observability/configuration/multi-tenancy/concepts" >}}) to plan your tenant strategy
2. **Create organizations**: Follow the Grafana organization creation guide to implement your strategy
3. **Configure data ingestion**: Set up [data collection]({{< relref "/tutorials/observability/data-ingestion" >}}) to send data to your tenants
