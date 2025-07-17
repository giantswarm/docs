---
title: Data transformation
description: Learn how to transform and enrich observability data in the Giant Swarm platform.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management
    identifier: overview-observability-data-management-data-transformation
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I transform observability data?
  - What are relabeling and recording rules?
  - How do I enrich logs and metrics?
  - How do I use Grafana transformations?
---

Data transformation allows you to process, enrich, and modify observability data to better suit your analysis and monitoring needs. The Giant Swarm Observability Platform offers several transformation approaches at different stages of the data pipeline.

## Transformation approaches

### Server-side transformations

Transform data before storage to improve performance and create derived metrics:

- **[Recording rules]({{< relref "/overview/observability/alert-management/alert-rules#recording-rules" >}})**: Pre-compute complex PromQL expressions as new time series
- **[Relabeling rules](#relabeling-rules)**: Modify, filter, or enrich metrics and logs during collection
- **[Data parsing](#data-parsing-and-enrichment)**: Extract structured data from logs and add contextual information

### Client-side transformations

Transform data during visualization for specific dashboard requirements:

- **[Grafana transformations](#grafana-transformations)**: Real-time data processing in dashboards and panels

## Recording rules

[Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) pre-compute frequently used or expensive PromQL expressions and store results as new time series. This improves dashboard performance and enables complex aggregations for alerting.

Recording rules are created using the same `PrometheusRule` resources as alerting rules and are covered in detail in our [alert rules documentation]({{< relref "/overview/observability/alert-management/alert-rules#recording-rules" >}}).

### Key benefits for data transformation

- **Performance optimization**: Pre-calculate expensive aggregations to speed up dashboards
- **Simplified queries**: Break complex expressions into manageable, reusable components  
- **Custom metrics creation**: Combine multiple metrics into business-relevant indicators
- **Consistent calculations**: Ensure identical computation across dashboards and alerts

For comprehensive guidance on creating and managing recording rules, including examples and best practices, see the [recording rules section]({{< relref "/overview/observability/alert-management/alert-rules#recording-rules" >}}) in our alert rules documentation.

## Relabeling rules

Relabeling rules modify metric and log labels during collection, allowing you to filter data, add context, or standardize naming conventions before storage.

### Metrics relabeling

Configure relabeling in ServiceMonitors and PodMonitors to transform metrics during scraping:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    observability.giantswarm.io/tenant: my_team
  name: application-metrics
  namespace: my-namespace
spec:
  endpoints:
  - path: /metrics
    port: metrics
    # Transform labels during collection
    relabelings:
    # Add environment label based on namespace
    - sourceLabels: [__meta_kubernetes_namespace]
      targetLabel: environment
      regex: "production-(.*)"
      replacement: "prod"
    
    # Drop sensitive metrics
    - sourceLabels: [__name__]
      regex: "secret_.*|password_.*"
      action: drop
    
    # Rename metric labels
    - sourceLabels: [application_name]
      targetLabel: app
      action: replace
  selector:
    matchLabels:
      app: my-application
```

### Log relabeling

Configure relabeling in PodLogs resources to enrich log metadata:

```yaml
apiVersion: monitoring.grafana.com/v1alpha2
kind: PodLogs
metadata:
  name: application-logs
  namespace: my-namespace
spec:
  relabelings:
  # Set tenant for data routing
  - action: replace
    replacement: my_team
    targetLabel: giantswarm_observability_tenant
  
  # Add application version from pod labels
  - sourceLabels: [__meta_kubernetes_pod_label_version]
    targetLabel: app_version
    action: replace
  
  # Extract service name from pod name
  - sourceLabels: [__meta_kubernetes_pod_name]
    targetLabel: service
    regex: "(.+)-[0-9a-f]+-[0-9a-z]{5}"
    replacement: "${1}"
  
  selector:
    matchLabels:
      app: my-application
```

For detailed relabeling configuration, see the [Prometheus relabeling documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config).

## Data parsing and enrichment

Transform unstructured logs into structured data using LogQL parsers and extract meaningful information for analysis.

### JSON parsing

Extract fields from JSON-formatted logs:

```promql
# Parse JSON logs and extract specific fields
{app="my-application"} 
| json 
| level="error" 
| line_format "{{.timestamp}} [{{.level}}] {{.component}}: {{.message}}"
```

### Pattern extraction

Use regex patterns to extract data from unstructured logs:

```promql
# Extract HTTP request details from access logs
{job="nginx"} 
| pattern `<ip> - - [<timestamp>] "<method> <uri> <protocol>" <status> <bytes>`
| status >= 400
```

### Label enhancement

Add contextual information during log processing:

```promql
# Add severity based on log level
{app="my-application"} 
| json level
| label_format severity=`{{ if eq .level "error" }}critical{{ else if eq .level "warn" }}warning{{ else }}info{{ end }}`
```

For advanced LogQL techniques, see our [advanced LogQL tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial" >}}).

## Grafana transformations

[Grafana transformations](https://grafana.com/docs/grafana/latest/panels/transformations/) process data client-side during visualization, enabling real-time calculations and formatting without modifying stored data.

### Common transformation use cases

- **Calculate derived values**: Create ratios, percentages, or growth rates
- **Merge data sources**: Combine metrics and logs in single visualizations  
- **Format for presentation**: Rename fields, apply units, or create custom formatting
- **Filter and aggregate**: Focus on specific data subsets or summary statistics

### Example transformations

**Calculate error percentage:**

1. Query total requests: `sum(rate(http_requests_total[5m]))`
2. Query error requests: `sum(rate(http_requests_total{status=~"5.."}[5m]))`
3. Apply "Add field from calculation" transformation
4. Formula: `Error Rate = (Error Requests / Total Requests) * 100`

**Merge time series data:**

1. Query multiple metrics with different time ranges
2. Apply "Merge" transformation to combine series
3. Use "Organize fields" to rename and reorder columns

### Performance considerations

- **Use sparingly**: Client-side transformations impact dashboard performance
- **Prefer recording rules**: For frequently used calculations, create recording rules instead
- **Consider data volume**: Large datasets may cause browser performance issues

For comprehensive transformation examples, see the [Grafana transformations documentation](https://grafana.com/docs/grafana/latest/panels/transformations/).

## Best practices

### Performance optimization

- **Use recording rules** for expensive calculations used in multiple dashboards
- **Apply relabeling early** in the pipeline to reduce storage and network overhead
- **Limit transformation complexity** in Grafana to maintain dashboard responsiveness

### Data quality

- **Validate transformations** in test environments before production deployment
- **Monitor transformation impact** on resource usage and query performance
- **Document transformation logic** for maintenance and troubleshooting

### Security and compliance

- **Drop sensitive data** early in the pipeline using relabeling rules
- **Standardize labeling** across teams to improve data discoverability
- **Use tenant isolation** to ensure data transformation doesn't cross tenant boundaries

## Next steps

- Learn how to [create effective dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}) with your transformed data
- Set up [alerting rules]({{< relref "/overview/observability/alert-management/alert-rules" >}}) using recording rules for better performance

For questions about data transformation, contact your Giant Swarm support team or explore our community resources.
