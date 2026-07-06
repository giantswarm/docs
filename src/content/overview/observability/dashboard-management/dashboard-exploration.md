---
title: Dashboard exploration
diataxis_content_type: how-to-guide
description: Learn how to discover, navigate, and use the pre-built dashboards in the Giant Swarm Observability Platform, plus tips for searching and organizing your own dashboards.
weight: 10
menu:
  principal:
    parent: overview-observability-dashboard-management
    identifier: overview-observability-dashboard-management-dashboard-exploration
last_review_date: 2026-07-03
user_questions:
  - How do I find dashboards in Grafana?
  - What dashboards come out of the box?
  - How do I search for specific dashboards?
  - What system dashboards are available?
  - How do I navigate between dashboards?
  - What dashboards should I look at first?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

This guide shows you how to explore and discover dashboards in the Giant Swarm Observability Platform. You'll learn about the pre-built dashboards available out of the box, how to search and navigate between dashboards, and tips for organizing your dashboard workspace.

Giant Swarm provides a comprehensive set of pre-built dashboards that give you immediate visibility into your infrastructure, applications, and platform health. These dashboards are designed to help you monitor everything from Kubernetes cluster performance to application metrics without requiring initial setup.

## Accessing dashboards in Grafana

To start exploring dashboards, you'll need access to your Grafana instance. If you haven't accessed Grafana yet, follow the [data exploration guide]({{< relref "/overview/observability/data-management/data-exploration#how-to-access-and-authenticate-in-grafana" >}}) for authentication steps.

Once you're logged in to Grafana:

1. **Navigate to dashboards**: Click the **Dashboards** icon (grid squares) in the left sidebar
2. **Browse by organization**: You'll see all dashboards available in your selected [Grafana organization]({{< relref "/overview/observability/configuration/multi-tenancy" >}}), switching to another Grafana organization will most likely change the list of available dashboards.
3. **Start with Shared Org**: The `Shared Org` contains system dashboards accessible to all users

## Out-of-the-box dashboards

Giant Swarm provides a comprehensive set of public dashboards, accessible to all users through the `Shared Org`. They cover cluster and node health, Kubernetes components, networking and ingress, application workloads, the observability platform itself, and cluster automation. For the full catalog grouped by category, see the [pre-built dashboards reference]({{< relref "/overview/observability/dashboard-management/prebuilt-dashboards" >}}).

## How to search and navigate dashboards

### Using the dashboard browser

1. **Browse by folder**: Dashboards are organized in folders by category (Platform, Kubernetes, Applications, etc.)
2. **Use tags**: Filter dashboards using tags like `cluster`, `application`, or `infrastructure`
3. **Recent dashboards**: Quick access to your recently viewed dashboards
4. **Starred dashboards**: Mark important dashboards as favorites for easy access

### Search functionality

Grafana provides powerful search capabilities:

1. **Quick search**: Use the search box at the top of the dashboard list
2. **Search by name**: Type dashboard names or partial names
3. **Search by tags**: Filter using tags like `kubernetes`, `monitoring`, or `alerts`
4. **Advanced filters**: Use the filter options to narrow by organization, folder, or dashboard type

### Dashboard navigation tips

- **Dashboard links**: Many dashboards include navigation links to related dashboards
- **Time range consistency**: Your selected time range carries across dashboard navigation
- **Breadcrumb navigation**: Use the breadcrumb trail to understand your current location
- **Bookmark important dashboards**: Save URLs to dashboards you use frequently

## Getting started with dashboard exploration

### For new users

Start with these essential dashboards to get oriented:

1. **Management Cluster Overview**: Understand your overall platform health and management cluster status
2. **K8s Resources - Cluster**: Get familiar with your cluster resources and capacity
3. **Nodes Overview**: Check the health and performance of your infrastructure nodes

### For developers

Focus on application and development-related dashboards:

1. **K8s Resources - Namespace**: Monitor your team's namespace resources and workload distribution
2. **K8s Resources - Pod**: Understand individual pod resource consumption patterns
3. **Managed Apps**: Track the performance of Giant Swarm managed applications you're using
4. **Container Images from docker.io**: Monitor Docker image pull patterns and registry usage

### For platform teams

Concentrate on infrastructure and platform monitoring:

1. **Management Cluster Overview**: Monitor platform stability and control plane health
2. **K8s API Performance**: Track cluster API performance and ETCD health
3. **Prometheus Overview**: Monitor the observability platform itself
4. **Alertmanager Overview**: Stay on top of platform alerts and notification routing
5. **Service Level**: Track SLOs and error budgets across platform services

## Next steps

Once you're comfortable navigating existing dashboards:

- **Learn dashboard creation**: Follow our [dashboard creation guide]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}) to build custom visualizations
- **Explore data sources**: Use [Grafana Explore]({{< relref "/overview/observability/data-management/data-exploration" >}}) to query data directly
- **Set up alerts**: Configure [alert rules]({{< relref "/overview/observability/alert-management/alert-rules" >}}) based on dashboard insights
- **Advanced queries**: Learn [PromQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial" >}}) and [LogQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial" >}}) for custom queries

## Related observability features

Dashboard exploration works best when integrated with other platform capabilities:

- **[Data exploration]({{< relref "/overview/observability/data-management/data-exploration" >}})**: Use Explore to query data behind dashboard visualizations
- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}})**: Understand dashboard organization and access controls
- **[Alert management]({{< relref "/overview/observability/alert-management" >}})**: Connect dashboard insights to automated alerting
