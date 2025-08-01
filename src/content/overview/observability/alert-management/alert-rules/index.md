---
title: Alert rules
description: Learn how to create and manage alerting and recording rules in the Giant Swarm observability platform.
weight: 10
menu:
  principal:
    parent: overview-observability-alert-management
    identifier: overview-observability-alert-management-alert-rules
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I create alert rules?
  - What is the difference between alerting and recording rules?
  - How do I use PromQL and LogQL for alerting?
  - How do I deploy alert rules?
aliases:
  - /tutorials/observability/alerting/create-rules/
---

This guide shows you how to create and deploy alerting and recording rules using Kubernetes resources. For an overview of what these rules are and how they fit into the alerting pipeline, see the [alert management overview]({{< relref "/overview/observability/alert-management/" >}}).

## How to deploy rules

You define alerting and recording rules using [Prometheus Operator](https://prometheus-operator.dev/) `PrometheusRule` resources, following Giant Swarm's GitOps approach. Deploy these rules to both management clusters and workload clusters.

The platform evaluates your rules and routes alerts through the [alerting pipeline]({{< relref "/overview/observability/alert-management/" >}}) to configured receivers.

## Required tenant labeling

**Important:** All alert rules must include the `observability.giantswarm.io/tenant` label that references an existing tenant defined in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization/" >}}). The system ignores any `PrometheusRule` that references a non-existing tenant.

Get familiar with tenant management in our [multi-tenancy documentation]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}).

## Alerting rule examples

Create alerting rules using [Prometheus alerting rule syntax](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) with PromQL or LogQL expressions.

### Metric-based alert

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    # Required: specifies which tenant this alert belongs to
    observability.giantswarm.io/tenant: my_team
  name: component-availability
  namespace: my-namespace
spec:
  groups:
  - name: reliability
    rules:
      - alert: ComponentDown
        annotations:
          summary: 'Component {{ $labels.service }} is down'
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

- **`alert`**: Unique name for the alert rule
- **`expr`**: PromQL or LogQL expression defining when the alert fires
- **`for`**: Duration the condition must remain true before firing
- **`labels`**: Key-value pairs for routing and grouping alerts
- **`annotations`**: Human-readable information about the alert

For guidance on writing effective PromQL queries, see the [Prometheus querying documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/) or our [advanced PromQL tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial" >}}). You can also explore queries in your [installation's Grafana]({{< relref "/getting-started/observe-your-clusters-and-apps/" >}}) explore interface.

## Recording rule examples

Create recording rules using [Prometheus recording rule syntax](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) to pre-compute expensive expressions.

### Basic recording rule

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    observability.giantswarm.io/tenant: my_team
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

## Log-based alerting examples

Create log-based alerts using LogQL queries. These require specific labels to route to the Loki ruler.

### Log pattern alert

You'll need specific labels to indicate evaluation by Loki:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    observability.giantswarm.io/tenant: my_team
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

For more information about writing LogQL queries, see the [Loki LogQL documentation](https://grafana.com/docs/loki/latest/logql/).

## Rule scoping

The platform provides scoping mechanisms to prevent conflicts when deploying the same rules across multiple clusters within a tenant.

### Scoping behavior

#### Workload cluster deployment (cluster-scoped)

When you deploy a `PrometheusRule` in a workload cluster, the system automatically scopes rules to that specific cluster. For example, deploying a rule with expression `up{job="good"} > 0` in workload cluster `alpha1` results in: `up{cluster_id="alpha1", job="good"} > 0`.

#### Management cluster deployment (installation-scoped)

When you deploy a `PrometheusRule` in a management cluster, rules target all clusters in the installation without modification.

### Limitations

- Only metric-based alerts support cluster scoping due to upstream limitations
- Manual conflict management required for rules deployed per application in different namespaces
- Consider unique naming or namespace-specific labeling for multi-environment deployments

## Tenant federation

With Alloy 1.9, the platform supports tenant federation, letting you create rules based on other tenants' data without duplicating data intake. Just add the `monitoring.grafana.com/source_tenants` label to your `PrometheusRule`.

### Example: System metrics alerting

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    observability.giantswarm.io/tenant: my_team
    # Define the source tenant for metrics used in the alert
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
          __dashboardUid__: system-metrics-dashboard
        # Query system metrics from the giantswarm tenant
        expr: up{job="node-exporter"} == 0
        for: 5m
        labels:
          severity: critical
```

## Next steps

- Configure [alert routing]({{< relref "/overview/observability/alert-management/alert-routing/" >}}) for your tenants to complete the alerting pipeline
- Review the [alerting pipeline]({{< relref "/overview/observability/alert-management/" >}}) architecture to understand how alerts flow through the system
- Learn about [data exploration]({{< relref "/overview/observability/data-management/data-exploration/" >}}) to query and analyze the metrics and logs that drive your alerts

## Related observability features

Alert rules work best when integrated with other platform capabilities:

- **[Data management]({{< relref "/overview/observability/data-management/" >}})**: Use advanced querying techniques to test and refine your alert expressions before deploying them
- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: Essential for understanding tenant labeling requirements and secure alert isolation
- **[Data Import and Export]({{< relref "/overview/observability/data-management/data-import-export/" >}})**: Import external logs that can trigger alerts and export alert data for comprehensive monitoring coverage across your infrastructure
