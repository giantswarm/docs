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
last_review_date: 2026-10-06
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What metrics can be derived from trace data?
  - How do I query trace-derived metrics?
  - What are the RED metrics and how are they queried?
  - Which traces_ metrics does the metrics-generator produce?
---

This page catalogs the metrics that Tempo's metrics-generator derives from your trace data on the Giant Swarm Observability Platform, together with the PromQL patterns for querying them. Because these are standard Prometheus metrics, you can use them in dashboards and alerts with familiar tooling.

For why these metrics exist and what RED metrics mean, see [understanding trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/understanding-trace-derived-metrics" >}}). To build alerts on them, see [alert on trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/alert-on-trace-derived-metrics" >}}). For the generator's configuration options, see the [Tempo metrics-generator documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-generator/).

## RED metrics

The metrics-generator produces rate, error, and duration (RED) metrics for each service and operation.

### Rate

Request rate, the number of requests per second for each service and operation:

```promql
# Total request rate for a service
rate(traces_service_graph_request_total[5m])

# Request rate by operation
rate(traces_spanmetrics_calls_total{span_name="GET /api/users"}[5m])
```

### Error

Error rate, the proportion of failed requests for each service and operation:

```promql
# Error rate for a service
(
  rate(traces_service_graph_request_failed_total[5m]) /
  rate(traces_service_graph_request_total[5m])
) * 100

# Failed spans by operation
rate(traces_spanmetrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])
```

### Duration

Response time, latency percentiles for each service and operation:

```promql
# 95th percentile latency
histogram_quantile(0.95, sum by (server, le) (rate(traces_service_graph_request_server_seconds_bucket[5m])))

# Average response time
rate(traces_service_graph_request_server_seconds_sum[5m]) /
rate(traces_service_graph_request_server_seconds_count[5m])
```

## Available trace-derived metrics

Tempo's metrics-generator creates several categories of metrics from your traces:

### Service graph metrics

Metrics representing service-to-service communication:

```promql
# Request rate between services
traces_service_graph_request_total{client="api-gateway", server="user-service"}

# Failed requests between services
traces_service_graph_request_failed_total{client="api-gateway", server="user-service"}

# Request duration histogram buckets between services
traces_service_graph_request_server_seconds_bucket{client="api-gateway", server="user-service"}
```

### Span metrics

Metrics for individual operations within services:

```promql
# Span request rate by operation
traces_spanmetrics_calls_total{service="user-service", span_name="GET /api/users"}

# Span error rate
traces_spanmetrics_calls_total{service="user-service", status_code="STATUS_CODE_ERROR"}

# Span duration percentiles
histogram_quantile(0.95, sum by (le) (rate(traces_spanmetrics_latency_bucket{service="user-service", span_name="database_query"}[5m])))
```

### Custom dimensions

Additional dimensions based on span attributes:

```promql
# Metrics by HTTP method
traces_spanmetrics_calls_total{http_method="POST"}

# Metrics by database operation
traces_spanmetrics_calls_total{db_operation="SELECT"}

# Custom business dimensions
traces_spanmetrics_calls_total{customer_tier="premium"}
```

## Querying trace-derived metrics

### Finding available metrics

Discover metrics generated from your traces:

```promql
# List all trace-derived metrics
{__name__=~"traces_.*"}

# Service graph metrics
{__name__=~"traces_service_graph.*"}

# Span metrics
{__name__=~"traces_spanmetrics.*"}
```

### Common query patterns

#### Service health monitoring

```promql
# Service availability (requests per second)
sum(rate(traces_service_graph_request_total[5m])) by (server)

# Service error rates
sum(rate(traces_service_graph_request_failed_total[5m])) by (server) /
sum(rate(traces_service_graph_request_total[5m])) by (server)

# Service response times
histogram_quantile(0.95,
  sum(rate(traces_service_graph_request_server_seconds_bucket[5m])) by (server, le)
)
```

#### Operation-level monitoring

```promql
# HTTP endpoint error rates
sum(rate(traces_spanmetrics_calls_total{status_code="STATUS_CODE_ERROR"}[5m])) by (span_name) /
sum(rate(traces_spanmetrics_calls_total[5m])) by (span_name)

# Database operation latency
histogram_quantile(0.99,
  sum(rate(traces_spanmetrics_latency_bucket{span_kind="SPAN_KIND_CLIENT"}[5m]))
  by (span_name, le)
)

# External service dependencies
sum(rate(traces_spanmetrics_calls_total{span_kind="SPAN_KIND_CLIENT"}[5m]))
by (service, span_name)
```

#### Cross-service analysis

```promql
# Traffic between service pairs
sum(rate(traces_service_graph_request_total[5m])) by (client, server)

# Inter-service error propagation
sum(rate(traces_service_graph_request_failed_total[5m])) by (client, server)

# Service dependency latency
sum(rate(traces_service_graph_request_server_seconds_sum[5m])) by (client, server) /
sum(rate(traces_service_graph_request_server_seconds_count[5m])) by (client, server)
```

## See also

- [Understanding trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/understanding-trace-derived-metrics" >}}): why they exist and what RED metrics mean
- [Alert on trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/alert-on-trace-derived-metrics" >}}): build alert rules from these metrics
- [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql/" >}}): general PromQL query patterns
- [Service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs/" >}}): the visual service topology behind service graph metrics
- [Tempo metrics-generator documentation](https://grafana.com/docs/tempo/latest/metrics-from-traces/metrics-generator/): configuration options
