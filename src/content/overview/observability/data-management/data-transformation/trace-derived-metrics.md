---
title: Trace-derived metrics
description: Learn how to generate metrics from trace data for alerting and monitoring with Tempo's metrics-generator feature.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-transformation
    identifier: overview-observability-data-management-data-transformation-trace-derived-metrics
last_review_date: 2025-09-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I generate metrics from traces?
  - What metrics can be derived from trace data?
  - How do I set up alerts based on traces?
  - What are RED metrics and how are they calculated?
  - How do I query trace-derived metrics?
  - Why can't I alert directly on trace data?
---

Giant Swarm's observability platform automatically generates metrics from your trace data using Tempo's metrics-generator. This transformation enables you to create alerts and dashboards based on distributed tracing insights while using familiar Prometheus/PromQL tooling.

You can't create alerts directly from trace data, so these automatically generated metrics bridge the gap between detailed trace analysis and reliable monitoring.

## Understanding metrics derived from traces

Tempo's metrics-generator automatically creates RED (Rate, Error, Duration) metrics from your trace data:

### Rate

**Request rate**: The number of requests per second for each service and operation.

```promql
# Total request rate for a service
rate(tempo_service_graph_request_total[5m])

# Request rate by operation
rate(tempo_service_graph_request_total{operation="GET /api/users"}[5m])
```

### Error

**Error rate**: The percentage of failed requests for each service and operation.

```promql
# Error rate for a service
(
  rate(tempo_service_graph_request_failed_total[5m]) / 
  rate(tempo_service_graph_request_total[5m])
) * 100

# Error rate by HTTP status code
rate(tempo_service_graph_request_total{status_code=~"5.."}[5m])
```

### Duration

**Response time**: Latency percentiles for each service and operation.

```promql
# 95th percentile latency
histogram_quantile(0.95, rate(tempo_service_graph_request_duration_seconds_bucket[5m]))

# Average response time
rate(tempo_service_graph_request_duration_seconds_sum[5m]) / 
rate(tempo_service_graph_request_duration_seconds_count[5m])
```

## Available trace-derived metrics

Tempo's metrics-generator creates several categories of metrics from your traces:

### Service graph metrics

Metrics representing service-to-service communication:

```promql
# Request rate between services
tempo_service_graph_request_total{client="api-gateway", server="user-service"}

# Failed requests between services
tempo_service_graph_request_failed_total{client="api-gateway", server="user-service"}

# Request duration between services
tempo_service_graph_request_duration_seconds{client="api-gateway", server="user-service"}
```

### Span metrics

Metrics for individual operations within services:

```promql
# Span request rate by operation
tempo_span_metrics_calls_total{service_name="user-service", span_name="GET /api/users"}

# Span error rate
tempo_span_metrics_calls_total{service_name="user-service", status_code="STATUS_CODE_ERROR"}

# Span duration percentiles
tempo_span_metrics_duration_seconds{service_name="user-service", span_name="database_query"}
```

### Custom dimensions

Additional dimensions based on span attributes:

```promql
# Metrics by HTTP method
tempo_span_metrics_calls_total{http_method="POST"}

# Metrics by database operation
tempo_span_metrics_calls_total{db_operation="SELECT"}

# Custom business dimensions
tempo_span_metrics_calls_total{customer_tier="premium"}
```

## Querying trace-derived metrics

### Finding available metrics

Discover metrics generated from your traces:

```promql
# List all trace-derived metrics
{__name__=~"tempo_.*"}

# Service graph metrics
{__name__=~"tempo_service_graph.*"}

# Span metrics
{__name__=~"tempo_span_metrics.*"}
```

### Common query patterns

#### Service health monitoring

```promql
# Service availability (requests per second)
sum(rate(tempo_service_graph_request_total[5m])) by (server)

# Service error rates
sum(rate(tempo_service_graph_request_failed_total[5m])) by (server) /
sum(rate(tempo_service_graph_request_total[5m])) by (server)

# Service response times
histogram_quantile(0.95, 
  sum(rate(tempo_service_graph_request_duration_seconds_bucket[5m])) by (server, le)
)
```

#### Operation-level monitoring

```promql
# HTTP endpoint error rates
sum(rate(tempo_span_metrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) by (span_name) /
sum(rate(tempo_span_metrics_calls_total[5m])) by (span_name)

# Database operation latency
histogram_quantile(0.99,
  sum(rate(tempo_span_metrics_duration_seconds_bucket{span_kind="SPAN_KIND_CLIENT"}[5m])) 
  by (span_name, le)
)

# External service dependencies
sum(rate(tempo_span_metrics_calls_total{span_kind="SPAN_KIND_CLIENT"}[5m])) 
by (service_name, span_name)
```

#### Cross-service analysis

```promql
# Traffic between service pairs
sum(rate(tempo_service_graph_request_total[5m])) by (client, server)

# Inter-service error propagation
sum(rate(tempo_service_graph_request_failed_total[5m])) by (client, server)

# Service dependency latency
avg(tempo_service_graph_request_duration_seconds) by (client, server)
```

## Setting up alerts based on trace data

### Alert rule examples

Create alerting rules using trace-derived metrics:

#### High error rate alert

```yaml
groups:
- name: trace-based-alerts
  rules:
  - alert: HighServiceErrorRate
    expr: |
      (
        sum(rate(tempo_service_graph_request_failed_total[5m])) by (server) /
        sum(rate(tempo_service_graph_request_total[5m])) by (server)
      ) * 100 > 5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High error rate detected for service {{ $labels.server }}"
      description: "Service {{ $labels.server }} has error rate of {{ $value }}% for 5 minutes"
```

#### High latency alert

```yaml
- alert: HighServiceLatency
  expr: |
    histogram_quantile(0.95,
      sum(rate(tempo_service_graph_request_duration_seconds_bucket[5m])) by (server, le)
    ) > 2
  for: 10m
  labels:
    severity: critical
  annotations:
    summary: "High latency detected for service {{ $labels.server }}"
    description: "Service {{ $labels.server }} 95th percentile latency is {{ $value }}s"
```

#### Service availability alert

```yaml
- alert: ServiceUnavailable
  expr: |
    absent_over_time(
      sum(rate(tempo_service_graph_request_total[1m])) by (server)[5m:]
    ) == 1
  labels:
    severity: critical
  annotations:
    summary: "Service {{ $labels.server }} appears to be unavailable"
    description: "No requests detected for service {{ $labels.server }} in the last 5 minutes"
```

## Best practices for using trace-derived metrics

### Alert design principles

- **Focus on business impact**: Alert on conditions that affect user experience
- **Use appropriate time windows**: Balance sensitivity with noise reduction
- **Set meaningful thresholds**: Base thresholds on historical data and SLA requirements
- **Include context**: Add relevant labels and annotations for effective incident response

### Common monitoring patterns

1. **Service-level monitoring**: Track overall service health using RED (Rate, Error, Duration) metrics
2. **Dependency monitoring**: Alert when upstream services affect downstream performance
3. **Capacity planning**: Monitor request rates and latency trends over time
4. **Quality monitoring**: Track degradation in service quality metrics

## Next steps

To effectively use trace-derived metrics:

- **[Configure comprehensive alerting]({{< relref "/overview/observability/alert-management/alert-rules/" >}})**: Set up alert rules using trace-derived metrics
- **[Create service dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation/" >}})**: Visualize trace metrics alongside other observability data
- **[Learn advanced PromQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial/" >}})**: Master querying techniques for trace-derived metrics
- **[Understand service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs/" >}})**: Connect metrics to visual service topology analysis

For more detailed configuration options, refer to the [Tempo metrics-generator documentation](https://grafana.com/docs/tempo/latest/metrics-generator/).
