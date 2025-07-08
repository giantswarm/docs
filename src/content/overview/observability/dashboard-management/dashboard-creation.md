---
title: Dashboard Creation
description: Learn how to create custom Grafana dashboards using GitOps workflows or the interactive UI in the Giant Swarm platform.
weight: 10
menu:
  principal:
    parent: overview-observability-dashboard-management
    identifier: overview-observability-dashboard-creation
last_review_date: 2025-07-08
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I create a dashboard using GitOps?
  - How do I create a dashboard in the Grafana UI?
  - What's the recommended approach for dashboard creation?
  - How do I organize dashboards by team or environment?
  - How to customize dashboards?
  - How to create my own dashboards?
aliases:
  - /tutorials/observability/data-exploration/creating-custom-dashboards/
  - /tutorials/observability/data-exploration/creating-custom-dashboards/index.html
---

Creating custom dashboards lets you visualize your observability data exactly how your team needs it. The platform supports two main approaches: a GitOps workflow for production environments and interactive creation for rapid development and prototyping.

## GitOps approach

The GitOps approach stores dashboard definitions as code, making them versionable, reviewable, and automatically deployable across environments. This is the recommended method for production dashboards.

### Create a dashboard ConfigMap

Deploy dashboards by creating Kubernetes ConfigMaps in your management cluster:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-application-dashboard
  namespace: my-team-namespace
  labels:
    app.giantswarm.io/kind: dashboard
  annotations:
    observability.giantswarm.io/organization: MyTeam
data:
  dashboard.json: |
    {
      "dashboard": {
        "uid": "my-app-overview",
        "title": "My Application Overview",
        "tags": ["application", "performance"],
        "panels": [
          // Your dashboard panels here
        ]
      }
    }
```

### Organization targeting

The `observability.giantswarm.io/organization` annotation determines which [Grafana organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization" >}}) receives the dashboard. The value must match an existing organization's display name.

### Dashboard requirements

- **Unique identifier (UID)**: Each dashboard needs a unique identifier within its organization
- **Valid JSON**: Dashboard definitions must be valid Grafana JSON format
- **Proper labeling**: Include the `app.giantswarm.io/kind: dashboard` label for automatic detection

### Benefits of GitOps

- **Version control**: Track changes and collaborate on dashboard improvements
- **Automated deployment**: Dashboards deploy automatically when ConfigMaps are applied
- **Multi-environment support**: Deploy the same dashboard across development, staging, and production
- **CI/CD integration**: Include dashboard validation in your pipeline

## Interactive creation

For rapid prototyping and iterative development, create dashboards directly in Grafana's web interface.

### Getting started

1. [Access your Grafana instance]({{< relref "/overview/observability/data-management/data-exploration" >}})
2. Navigate to **Dashboards** > **New** > **New Dashboard**
3. Add panels, configure visualizations, and arrange your layout
4. Save your dashboard to the appropriate organization

### Grafana documentation

For detailed guidance on using Grafana's dashboard builder, see the [official Grafana documentation](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/create-dashboard/).

### Data persistence

Dashboards created in the UI are stored in PostgreSQL with automatic backups, ensuring they persist across platform updates and restarts.

## Best practices

### Start with exploration

Before building dashboards, spend time in [Grafana's Explore view]({{< relref "/overview/observability/data-management/data-exploration#how-to-use-explore-and-drilldown-in-grafana" >}}) to understand your data and refine your queries.

### Design for your audience

- **Executive dashboards**: Focus on high-level KPIs and trends
- **Operational dashboards**: Emphasize real-time status and alert states  
- **Troubleshooting dashboards**: Include detailed metrics and drill-down capabilities

### Leverage existing resources

- Explore [Giant Swarm's default dashboards](https://github.com/giantswarm/dashboards) for inspiration
- Check the [Grafana community dashboards](https://grafana.com/grafana/dashboards/) for common patterns
- Use dashboard templates for consistent layouts across your organization

## Next steps

- **[Set up multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}})**: organize dashboards by team or environment
- **[Configure data ingestion]({{< relref "/tutorials/observability/data-ingestion" >}})**: ensure you have the right data flowing into your dashboards
