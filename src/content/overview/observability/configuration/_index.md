---
title: Configuration
description: Learn how to configure and customize the Giant Swarm observability platform for your organization's needs.
weight: 30
menu:
  principal:
    parent: overview-observability
    identifier: overview-observability-configuration
last_review_date: 2025-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I configure the observability platform?
  - What configuration options are available?
  - How do I set up multi-tenancy?
  - What can I customize in Grafana?
  - How do I configure data ingestion?
  - What alerting options can I configure?
  - How do I manage access controls?
---

The Giant Swarm observability platform offers extensive configuration options to tailor the system to your organization's specific monitoring, alerting, and visualization needs. This overview covers the key areas you can configure to create a customized observability experience that fits your operational requirements.

## Platform-level configuration

Configure foundational platform settings that affect the entire observability stack:

### Initial platform setup

Work with Giant Swarm to configure core platform components:

- **OIDC provider integration**: Connect your identity provider for authentication
- **Base domain configuration**: Set up DNS and ingress for platform access

## Multi-tenancy and access control

**[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}})** forms the foundation of platform configuration, enabling you to:

- **Isolate data** between teams, environments, or projects through tenant separation
- **Control access** by mapping Grafana organizations to specific tenants and user groups
- **Manage permissions** with role-based access controls (RBAC) from your identity provider
- **Configure tenant lifecycle** including creation, management, and removal processes

Multi-tenancy configuration affects all other platform components, making it essential to understand before configuring other areas.

### Organization management

Manage your observability platform's organizational structure through **[`GrafanaOrganization`]({{< relref "/reference/platform-api/crd/grafanaorganizations.observability.giantswarm.io" >}})** resources. Organization management enables you to:

- **Create isolated workspaces**: Set up dedicated Grafana organizations for teams, environments, or projects
- **Configure access controls**: Map identity provider groups to appropriate roles (admin, editor, viewer)
- **Define tenant access**: Control which data tenants each organization can access
- **Provision datasources**: Automatically configure tenant-scoped access to metrics, logs, and alerting

Effective organization management provides teams with secure, isolated access to their observability data while maintaining proper governance and data separation. Learn how to [create and configure Grafana organizations]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organizations" >}}) with practical examples and step-by-step instructions.

## Data ingestion configuration

Control what observability data flows into your platform and how it's processed:

### Metrics collection

Configure **[metrics ingestion]({{< relref "/tutorials/observability/data-ingestion/metrics" >}})** to collect custom application and infrastructure metrics:

- **ServiceMonitors**: Define which services to scrape for metrics and how frequently
- **PodMonitors**: Configure direct pod-level metric collection for specialized use cases
- **Tenant routing**: Specify which tenant receives metrics through labeling
- **Metric transformation**: Apply relabeling rules to modify, filter, or enrich metrics before storage

### Log collection

Configure **[log ingestion]({{< relref "/tutorials/observability/data-ingestion/logs" >}})** to capture application and system logs:

- **PodLogs**: Select which pods to collect logs from using label selectors
- **Pod labels**: Enable automatic log collection by labeling pods with tenant information
- **Log parsing**: Configure structured parsing and label extraction from log content
- **Namespace filtering**: Control log collection scope by namespace

### External data sources

Integrate data from sources outside Giant Swarm managed clusters through the **[Observability Platform API]({{< relref "/overview/observability/observability-platform-api" >}})**:

- **OIDC authentication**: Configure your identity provider for secure API access
- **Data ingestion endpoints**: Send metrics, logs, and traces from external systems
- **OpenTelemetry Protocol (OTLP)**: Configure standardized telemetry data ingestion

## Visualization and dashboard configuration

Customize how you view and visualize your observability data:

### Grafana organizations

Once you've [created Grafana organizations]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organizations" >}}) as part of your multi-tenancy setup, you can leverage them for powerful visualization capabilities:

- **Isolated workspaces**: Each organization provides a dedicated environment for team-specific dashboards and visualizations
- **Tenant-scoped data access**: Automatically provisioned datasources provide teams with access only to their authorized data
- **Collaborative visualization**: Share dashboards and insights within organization boundaries
- **Custom dashboard organization**: Organize monitoring assets by team, environment, or service ownership

### Custom dashboards

**[Create custom dashboards]({{< relref "/tutorials/observability/data-exploration/creating-custom-dashboards" >}})** tailored to your specific monitoring needs:

- **GitOps approach**: Version-controlled dashboard definitions using ConfigMaps
- **UI creation**: Build dashboards directly in Grafana with persistent storage
- **Dashboard provisioning**: Automatically deploy dashboards to specific organizations
- **Cross-tenant dashboards**: Combine data from multiple tenants when authorized

## Alerting and notification configuration

Set up comprehensive alerting to provide timely notification of issues:

### Alert rules

**[Create alerting and recording rules]({{< relref "/tutorials/observability/alerting/create-rules" >}})** for proactive monitoring:

- **Metric-based alerts**: PromQL expressions for infrastructure and application monitoring
- **Log-based alerts**: LogQL expressions for application error detection and log pattern analysis
- **Recording rules**: Pre-computed metrics for improved dashboard performance
- **Tenant federation**: Create rules that query data across multiple tenants

### Alert management

**[Configure Alertmanager]({{< relref "/tutorials/observability/alerting/configure-alertmanager" >}})** for comprehensive alert handling and operational workflows:

- **Notification channels**: Integration with Slack, email, PagerDuty, and other services
- **Contact points**: Configure notification destinations and templates
- **Routing rules**: Define which alerts go to which teams based on labels and severity
- **Notification policies**: Define routing logic based on alert characteristics
- **Alert grouping**: Combine related alerts to reduce notification fatigue
- **Silences**: Manage alert suppression for planned maintenance or known issues
- **Alert templates**: Customize notification formatting and content

## Configuration best practices

### Start simple and iterate

Begin with basic configurations and gradually add complexity:

- Start with environment-based tenants (`production`, `staging`, `development`)
- Implement essential alerting rules before expanding to comprehensive monitoring
- Create basic dashboards before building complex visualization workflows

### Plan for scale

Design configurations that grow with your organization:

- Choose tenant strategies that align with your organizational structure
- Design alert routing that scales with team growth
- Plan dashboard organization that remains manageable as teams expand

### Maintain consistency

Establish patterns and standards across your configuration:

- Use consistent naming conventions for tenants, alerts, and dashboards
- Standardize alert severity levels and routing patterns
- Create reusable templates for common monitoring patterns

## Getting started

To begin configuring your observability platform:

1. **Understand multi-tenancy**: Review [multi-tenancy concepts]({{< relref "/overview/observability/configuration/multi-tenancy" >}}) to plan your data organization
2. **Set up organizations**: [Create Grafana organizations]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organizations" >}}) for your teams
3. **Configure data ingestion**: Set up [metrics]({{< relref "/tutorials/observability/data-ingestion/metrics" >}}) and [log collection]({{< relref "/tutorials/observability/data-ingestion/logs" >}}) for your applications
4. **Create essential alerts**: Implement [basic alerting rules]({{< relref "/tutorials/observability/alerting/create-rules" >}}) for critical system health
5. **Build dashboards**: Create [custom dashboards]({{< relref "/tutorials/observability/data-exploration/creating-custom-dashboards" >}}) for your specific monitoring needs

For platform-level configuration assistance, contact your Giant Swarm account engineer who can help with OIDC provider setup, resource allocation, and other foundational configurations.
