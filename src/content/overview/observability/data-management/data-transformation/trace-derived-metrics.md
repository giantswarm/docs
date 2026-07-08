---
title: Trace-derived metrics reference
linkTitle: Trace-derived metrics reference
diataxis_content_type: reference
description: Catalog of the metrics Tempo's metrics-generator derives from trace data on the Giant Swarm observability platform, with the PromQL patterns for querying them.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-transformation
    identifier: overview-observability-data-management-data-transformation-trace-derived-metrics
last_review_date: 2026-06-22
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What metrics can be derived from trace data?
  - How do I query trace-derived metrics?
  - What are the RED metrics and how are they queried?
  - Which tempo_ metrics does the metrics-generator produce?
---

This page catalogs the metrics that Tempo's metrics-generator derives from your trace data on the Giant Swarm Observability Platform, together with the PromQL patterns for querying them. Because these are standard Prometheus metrics, you can use them in dashboards and alerts with familiar tooling.

For why these metrics exist and what RED metrics mean, see [understanding trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/understanding-trace-derived-metrics" >}}). To build alerts on them, see [alert on trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/alert-on-trace-derived-metrics" >}}). For the generator's configuration options, see the [Tempo metrics-generator documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-generator/).

## RED metrics

The metrics-generator produces rate, error, and duration (RED) metrics for each service and operation.

### Rate

Request rate, the number of requests per second for each service and operation:

```promql
# Total request rate for a service
rate(tempo_service_graph_request_total[5m])

# Request rate by operation
rate(tempo_service_graph_request_total{operation="GET /api/users"}[5m])
```

### Error

Error rate, the proportion of failed requests for each service and operation:

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

Response time, latency percentiles for each service and operation:

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

## See also

- [Understanding trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/understanding-trace-derived-metrics" >}}): why they exist and what RED metrics mean
- [Alert on trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/alert-on-trace-derived-metrics" >}}): build alert rules from these metrics
- [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql/" >}}): general PromQL query patterns
- [Service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs/" >}}): the visual service topology behind service graph metrics
- [Tempo metrics-generator documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-generator/): configuration options
