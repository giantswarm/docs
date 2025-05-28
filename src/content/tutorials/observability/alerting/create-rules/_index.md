---
linkTitle: Creating alerting rules
title: How to create alerting and recording rules
description: Learn how to create alerting and recording rules in the Giant Swarm Observability Platform using PrometheusRule resources.
menu:
  principal:
    identifier: tutorials-observability-alerting-alerts
    parent: tutorials-observability-alerting
weight: 40
last_review_date: 2025-05-28
user_questions:
  - How to create alerting rules?
  - How to create recording rules?
  - What is log-based alerting?
  - How to get alerts?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

The Giant Swarm Observability Platform provides an [alerting pipeline]({{< relref "/overview/observability/alerting/" >}}) that you can [configure per tenant]({{< relref "/tutorials/observability/alerting/configure-alertmanager" >}}). This platform allows you to create your own alerting and recording rules per tenant.

Following Giant Swarm's GitOps approach, alerting and recording rules must be defined using [Prometheus Operator](https://prometheus-operator.dev/) `PrometheusRule` resources. You can deploy these rules to both management clusters and workload clusters.

{{< admonition type="warning" title="Multi-tenancy requirement" >}}
The `observability.giantswarm.io/tenant` label on your rules must reference an existing tenant defined in a [Grafana Organization]({{< relref "/tutorials/observability/multi-tenancy/creating-grafana-organization/" >}}). Any `PrometheusRule` that references a non-existing tenant will be ignored. Learn more about our multi-tenancy in [Multi-tenancy in the observability platform]({{< relref "/tutorials/observability/multi-tenancy/" >}}).
{{< /admonition >}}

## Create alerting rules

[Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) define conditions that trigger notifications when specific issues occur in your infrastructure or applications. These rules use Prometheus (PromQL) or Loki (LogQL) expressions to evaluate conditions.

### Basic alerting rule structure

Here's a basic example of an alerting rule:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    # Required: specifies which tenant this alert belongs to
    observability.giantswarm.io/tenant: my-team
  name: component-availability
  namespace: my-namespace
spec:
  groups:
  - name: reliability
    rules:
      - alert: ComponentDown
        annotations:
          # Human-readable summary
          summary: 'Component {{ $labels.service }} is down'
          # Detailed description with context
          description: 'Component {{ $labels.service }} has been down for more than 5 minutes.'
          # Optional: link to relevant dashboard
          __dashboardUid__: my-dashboard-uid
          # Optional: link to troubleshooting documentation
          runbook_url: https://my-runbook-url
        # PromQL expression that defines the alert condition
        expr: up{job=~"component/.*"} == 0
        # Duration the condition must be true before firing
        for: 5m
        labels:
          # Severity level for routing and prioritization
          severity: critical
```

### Key components

- **`alert`**: unique name for the alert rule
- **`expr`**: PromQL or LogQL expression that defines when the alert should fire
- **`for`**: duration the condition must be true before the alert fires
- **`labels`**: key-value pairs for routing and grouping alerts
- **`annotations`**: human-readable information about the alert

{{< admonition type="tip" title="PromQL Resources" >}}
For guidance on writing effective PromQL queries, refer to the [Prometheus querying documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/). You can also explore queries in your [installation's Grafana]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}) explore interface.
{{< /admonition >}}

## Create recording rules

[Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) allow you to precompute frequently needed or computationally expensive expressions and save their results as new time series. This improves query performance and enables the creation of custom metrics for dashboards and alerts.

### When to use recording rules

Recording rules are useful when you need to:

- Improve performance by pre-calculating expensive aggregations used frequently
- Create custom metrics by combining multiple metrics into business-specific indicators
- Simplify complex queries by breaking them into manageable components

### Basic recording rule structure

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    # Required: specifies which tenant this rule belongs to
    observability.giantswarm.io/tenant: my-team
  name: cluster-resource-usage
  namespace: my-namespace
spec:
  groups:
  - name: cluster-resource-usage
    rules:
      - expr: |
          avg by (cluster_id) (
            node:node_cpu_utilization:ratio_rate5m
          )
        record: cluster:node_cpu:ratio_rate5m
```

## Log-based alerting

Log-based alerting allows you to monitor application logs for specific patterns, errors, or anomalies using LogQL queries. These alerts are evaluated by the Loki ruler and provide powerful capabilities for application-level monitoring.

### Configure log-based rules

To create log-based alerts, include specific labels to indicate evaluation by Loki:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    observability.giantswarm.io/tenant: my-team
    # Required: indicates this is a log-based rule
    observability.giantswarm.io/rule-type: logs
    # Deprecated but still required for compatibility
    application.giantswarm.io/prometheus-rule-kind: loki
  name: application-log-alerts
  namespace: my-namespace
spec:
  groups:
  - name: log-monitoring
    rules:
      - alert: HighErrorLogRate
        annotations:
          summary: 'High error rate in application logs'
          description: 'Application {{ $labels.app }} is producing {{ $value }} errors per minute'
        # LogQL expression to count error logs
        expr: |
          sum(rate({app="my-app"} |= "ERROR" [5m])) by (app) > 10
        for: 2m
        labels:
          severity: warning
```

For more information about writing LogQL queries, refer to the [Loki LogQL documentation](https://grafana.com/docs/loki/latest/logql/).

## Rule scoping

The Observability Platform provides scoping mechanisms to prevent conflicts when deploying the same rules across multiple clusters within a tenant.

### Scoping behavior

**Workload cluster deployment (cluster-scoped)**

When you deploy a `PrometheusRule` in a workload cluster, the rules are automatically scoped to that specific cluster. For example, deploying a rule with expression `up{job="good"} > 0` in workload cluster `alpha1` results in the loaded expression: `up{cluster_id="alpha1", job="good"} > 0`.

**Management cluster deployment (installation-scoped)**

When you deploy a `PrometheusRule` in a management cluster, the rules target all clusters in the installation without modification.

### Limitations

- Cluster scoping is only available for metric-based alerts due to upstream limitations
- Scoping applies when teams deploy the same rule across multiple clusters
- For rules deployed per application in different namespaces, you must manage conflicts manually

For multi-environment deployments, consider using unique naming or namespace-specific labeling to avoid conflicts.

## Using tenant federation for system data alerts

With the introduction of Alloy 1.9, the Giant Swarm Observability Platform supports tenant federation capabilities that allow you to create alerting rules based on system data without duplicating data intake. This feature enables you to reference metrics and logs from the `giantswarm` tenant directly in your own tenant's alerting rules using the `monitoring.grafana.com/source_tenants` label.

{{< admonition type="info" title="Tenant Federation" >}}
For more information about multi-tenancy and tenant management, see our [multi-tenancy documentation]({{< relref "/tutorials/observability/multi-tenancy/" >}}).
{{< /admonition >}}

### Example: Alerting on system metrics

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    observability.giantswarm.io/tenant: my-team
    monitoring.grafana.com/source_tenants: giantswarm
  name: system-node-alerts
  namespace: my-namespace
spec:
  groups:
  - name: system-monitoring
    rules:
      - alert: NodeDown
        annotations:
          summary: 'Cluster node is down'
          description: 'Node {{ $labels.instance }} in cluster {{ $labels.cluster_id }} has been down for more than 5 minutes.'
          # Reference the system metrics data source in Grafana
          __dashboardUid__: system-metrics-dashboard
        # Query system metrics from the giantswarm tenant
        expr: up{job="node-exporter"} == 0
        for: 5m
        labels:
          severity: critical
```
