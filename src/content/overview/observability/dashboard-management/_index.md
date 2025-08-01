---
title: Dashboard management
description: Understand how Giant Swarm's dashboard management capabilities help you create, organize, and maintain custom visualizations for your observability data.
weight: 30
menu:
  principal:
    parent: overview-observability
    identifier: overview-observability-dashboard-management
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is dashboard management in the observability platform?
  - How does Giant Swarm approach dashboard management?
  - What are the different ways to manage dashboards?
  - How do I find existing dashboards?
  - What dashboards are available out of the box?
  - How do I organize dashboards across teams?
  - What makes Giant Swarm's dashboard management different?
  - How do I create a custom dashboard?
  - How do I use GitOps for dashboards?
  - How do I share dashboards with my team?
---

## Introduction to dashboard management

Dashboard management in Giant Swarm's observability platform is our comprehensive approach to creating, organizing, and maintaining visual representations of your data. It's more than just building charts - it's about creating meaningful, actionable insights that help your teams monitor, troubleshoot, and optimize your systems.

Think of dashboard management as the bridge between your raw observability data (metrics, logs, traces) and the insights your teams need to make informed decisions. Whether you're a developer checking application performance, an operations engineer monitoring infrastructure health, or an executive tracking business Key Performance Indicators (KPIs), dashboard management ensures you have the right views at the right time.

## Our approach to dashboard management

Giant Swarm's dashboard management philosophy centers on three core principles:

### Self-service with guardrails

You control your dashboards, but we provide the infrastructure, best practices, and automation to make it easy. Create what you need, when you need it, without waiting for centralized teams or complex approval processes.

### GitOps-first, but flexible

We recommend treating dashboards as code - versioned, reviewed, and deployed like any other infrastructure component. But when you need to iterate quickly or explore data interactively, our platform supports direct UI creation too.

### Multi-tenant by design

Your dashboards live in organized spaces that align with your team structure and security requirements. Share insights across teams while maintaining appropriate access controls and data isolation.

## What dashboard management includes

### Discovery and exploration

Start your dashboard journey with our **[dashboard exploration guide]({{< relref "/overview/observability/dashboard-management/dashboard-exploration" >}})**, which covers:

- **[Out-of-the-box dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-exploration#out-of-the-box-dashboards" >}})** for immediate platform visibility across Kubernetes, networking, applications, and observability infrastructure
- **[Search and navigation]({{< relref "/overview/observability/dashboard-management/dashboard-exploration#how-to-search-and-navigate-dashboards" >}})** tools for finding relevant dashboards quickly
- **[Getting started recommendations]({{< relref "/overview/observability/dashboard-management/dashboard-exploration#getting-started-with-dashboard-exploration" >}})** tailored for different user roles (new users, developers, platform teams)
- **Organized structure** with logical categorization and tagging for easy discovery

### Creation and deployment

- **[GitOps workflows]({{< relref "/overview/observability/dashboard-management/dashboard-creation#gitops-approach" >}})** for production dashboards
- **[Interactive creation]({{< relref "/overview/observability/dashboard-management/dashboard-creation#interactive-creation" >}})** for rapid prototyping
- **Automated deployment** across environments
- **Version control** and change tracking

### Organization and governance

- **[Multi-tenant structure]({{< relref "/overview/observability/configuration/multi-tenancy" >}})** aligned with your teams
- **Access control** and permission management
- **Shared resources** for common patterns and templates
- **Standardization** across your organization

### Lifecycle management

- **Backup and recovery** for dashboard configurations
- **Performance optimization** for large-scale deployments

## Why dashboard management matters

Raw observability data is only valuable when it's accessible and actionable. Effective dashboard management transforms your metrics, logs, and traces into:

- **Operational awareness**: Real-time visibility into system health and performance
- **Troubleshooting efficiency**: Targeted views that help you identify and resolve issues faster
- **Strategic insights**: Business-relevant metrics that inform decision-making
- **Team alignment**: Shared understanding of system behavior and performance expectations

## Getting started

Your dashboard management journey starts with exploration. Begin with our **[dashboard exploration guide]({{< relref "/overview/observability/dashboard-management/dashboard-exploration" >}})** to:

1. **Discover pre-built dashboards** that provide immediate visibility into your clusters, applications, and platform health
2. **Learn navigation techniques** to find and organize dashboards effectively
3. **Understand role-specific recommendations** for new users, developers, and platform teams

Once you've explored the available dashboards and understand the navigation patterns, move on to our [dashboard creation guide]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}) to build custom visualizations. This guide covers both GitOps and interactive approaches, helping you choose the right method for your use case.

For a deeper understanding of how dashboards fit into your overall observability strategy, explore our [data management capabilities]({{< relref "/overview/observability/data-management" >}}) and [multi-tenancy configuration]({{< relref "/overview/observability/configuration/multi-tenancy" >}}).
