---
title: PromQL query reference
linkTitle: PromQL query reference
diataxis_content_type: reference
description: Reference catalog of PromQL query patterns for metrics analysis on the Giant Swarm observability platform, covering resource, application, and Kubernetes monitoring.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-promql
last_review_date: 2025-07-17
aliases:
  - /overview/observability/data-management/data-exploration/advanced-promql-tutorial/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I write advanced PromQL queries?
  - What are best practices for metrics analysis?
  - How do I aggregate and filter metrics?
  - How do I use PromQL for troubleshooting?
---

This page is a reference catalog of PromQL query patterns for the Giant Swarm Observability Platform, grouped by what you are monitoring. PromQL (Prometheus Query Language) is the query language used by Prometheus and Mimir for analyzing time-series metrics data.

To open Grafana Explore and select a Prometheus data source, see the [data exploration guide]({{< relref "/overview/observability/data-management/data-exploration/" >}}). For the concepts behind these queries — how to approach query construction, the Giant Swarm label model, and service level indicators — see [metrics monitoring concepts]({{< relref "/overview/observability/data-management/data-exploration/metrics-monitoring-concepts" >}}). For the complete language specification, see the [official Prometheus PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).

## Key functions and patterns

**Rate calculations**: `rate(metric[5m])` for per-second rates from counters
**Aggregations**: `sum by (label) (metric)` or `sum without (label) (metric)`
**Percentiles**: `histogram_quantile(0.95, rate(metric_bucket[5m]))`
**Time shifting**: `metric offset 1h` for historical comparison
**Predictions**: `predict_linear(metric[1h], 3600)` for forecasting

**Performance tip**: Use `without()` instead of `by()` when keeping most
labels - it's more efficient.

## Giant Swarm label structure

Every metric includes contextual labels:

- `cluster_id`: Specific cluster identifier
- `cluster_type`: `management_cluster` or `workload_cluster`
- `installation`: Your Giant Swarm installation ID
- `namespace`: Kubernetes namespace
- `job`: Prometheus scrape job name

Use these for precise targeting:
`{cluster_type="workload_cluster", namespace="production"}`

## Advanced metric selection and filtering

### Label-based filtering patterns

Use sophisticated label matching for precise metric selection:

```promql
# Target specific infrastructure components
node_cpu_seconds_total{cluster_type="management_cluster", mode="idle"}
container_memory_usage_bytes{cluster_type="workload_cluster",
  namespace="production"}

# High-priority pods only
kube_pod_info{priority_class=~"system-.*|critical-.*"}

# Exclude system namespaces
container_cpu_usage_seconds_total{
  namespace!~"kube-system|giantswarm|kube-.*"}

# Multi-dimensional filtering
up{job=~"kubernetes-.*", instance=~".*:443"} == 1
```

**Regex vs exact matching**: Use exact matching (`=`, `!=`) when possible for better performance. Use regex (`=~`, `!~`) for patterns or exclusions. See [RE2 syntax documentation](https://github.com/google/re2/wiki/Syntax) for complex patterns.

## Resource monitoring and capacity planning

Monitor infrastructure at three levels: **node** (physical resources),
**container** (application consumption), and **application** (business impact).

### Infrastructure monitoring

```promql
# Node CPU utilization percentage
(1 - avg by (instance, cluster_id) (rate(node_cpu_seconds_total{mode="idle"}[5m]))) * 100

# Node memory utilization (excludes buffers/cache)
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk space utilization by mount point
(1 - (node_filesystem_avail_bytes{fstype!~"tmpfs|fuse.lxcfs"} /
  node_filesystem_size_bytes)) * 100

# Top CPU consuming pods
topk(10, sum by (namespace, pod) (
  rate(container_cpu_usage_seconds_total{container!="POD"}[5m])))

# Memory usage vs limits by namespace
sum by (namespace) (container_memory_usage_bytes{container!="POD"}) /
sum by (namespace) (container_spec_memory_limit_bytes{container!="POD"}) * 100

# Containers hitting CPU throttling
rate(container_cpu_cfs_throttled_seconds_total[5m]) > 0
```

**Key insights**: CPU throttling indicates limit constraints even when nodes
aren't fully utilized. MemAvailable provides more accurate memory usage than
MemFree. See [node exporter documentation](https://github.com/prometheus/node_exporter#enabled-by-default)
for metric details.

## Application performance monitoring

### HTTP services

```promql
# Request rate by service and status
sum by (service, status) (rate(http_requests_total[5m]))

# Error rate percentage
sum(rate(http_requests_total{status=~"5.."}[5m])) / sum(rate(http_requests_total[5m])) * 100

# 95th percentile response time
histogram_quantile(0.95, sum by (le, service) (
  rate(http_request_duration_seconds_bucket[5m])))

# Top slowest endpoints
topk(10, histogram_quantile(0.95, sum by (le, endpoint) (
  rate(http_request_duration_seconds_bucket[5m]))))
```

**HTTP monitoring fundamentals**: Track request volume, error rates, and
response times to understand service health. Rate calculations show traffic
patterns, error percentages reveal reliability issues, and histogram percentiles
identify performance bottlenecks.

### Database and queue monitoring

```promql
# Database connection pool utilization
mysql_global_status_threads_connected /
  mysql_global_variables_max_connections * 100

# Queue depth and processing rate
queue_depth_total{queue="critical-jobs"}
rate(queue_messages_processed_total[5m])

# Average processing time
rate(queue_processing_time_seconds_sum[5m]) /
  rate(queue_processing_time_seconds_count[5m])
```

**Backend service health**: Monitor database connections, queue depths, and
processing rates to detect bottlenecks before they impact users. Connection
pool utilization reveals database load, queue metrics show processing capacity,
and timing calculations identify slow operations requiring optimization.

**Performance patterns**: Use `histogram_quantile()` for latency percentiles,
`topk()` for identifying problematic endpoints, and ratio calculations for error
rates. See [histogram documentation](https://prometheus.io/docs/practices/histograms/)
for best practices.

## Kubernetes-specific monitoring

### Cluster health indicators

Monitor Kubernetes control plane and workload health:

```promql
# API server availability and latency
up{job="kubernetes-apiservers"} and
histogram_quantile(0.99, rate(
  apiserver_request_duration_seconds_bucket{verb="GET"}[5m]))

# etcd health and performance
up{job="kubernetes-etcd"} and
histogram_quantile(0.99, rate(etcd_request_duration_seconds_bucket[5m]))

# Pod restart rate
increase(kube_pod_container_status_restarts_total[1h]) > 0

# Nodes not ready
kube_node_status_condition{condition="Ready", status!="true"} == 1
```

**Kubernetes foundation monitoring**: Track the health of cluster control plane
components that everything depends on. API server latency affects all kubectl
operations, etcd performance impacts cluster state storage, pod restarts
indicate application issues, and node readiness ensures workload placement
capacity.

### Workload scaling and health

Analyze deployment status and scaling patterns:

```promql
# Deployment replica availability
kube_deployment_status_replicas_available /
  kube_deployment_spec_replicas * 100

# HPA current vs target scaling
kube_horizontalpodautoscaler_status_current_replicas /
kube_horizontalpodautoscaler_spec_max_replicas * 100

# Persistent volume usage
(kubelet_volume_stats_capacity_bytes -
  kubelet_volume_stats_available_bytes) /
kubelet_volume_stats_capacity_bytes * 100
```

**Application scaling insights**: Monitor how well your applications adapt to
demand and maintain availability. Replica availability shows deployment health,
HPA metrics reveal autoscaling behavior and capacity limits, while persistent
volume usage prevents storage-related outages.

## Advanced aggregation patterns

### Multi-level aggregations

Combine metrics across different dimensions:

```promql
# Average response time per service across all clusters
avg by (service) (
  histogram_quantile(0.50,
    sum by (service, le) (
      rate(http_request_duration_seconds_bucket[5m])
    )
  )
)

# Resource usage efficiency by cluster
sum by (cluster_id) (rate(container_cpu_usage_seconds_total[5m])) /
sum by (cluster_id) (container_spec_cpu_quota /
  container_spec_cpu_period)
```

**Cross-dimensional analysis**: Build sophisticated queries that aggregate data
across multiple layers of your infrastructure. These patterns help you compare
service performance across environments, measure resource efficiency between
clusters, and identify optimization opportunities that single-dimension queries
might miss.

### Time-based calculations

Analyze trends and changes over time:

```promql
# Hour-over-hour growth rate
(
  sum(rate(http_requests_total[5m])) -
  sum(rate(http_requests_total[5m] offset 1h))
) / sum(rate(http_requests_total[5m] offset 1h)) * 100

# Weekly seasonality pattern
avg_over_time(sum(rate(http_requests_total[5m]))[7d:1h])

# Predict when disk will be full (linear regression)
predict_linear(node_filesystem_avail_bytes[1h], 24*3600) < 0
```

**Temporal pattern analysis**: Use time-based calculations to understand how
your systems behave over different periods. Growth rate comparisons reveal
traffic trends, seasonality patterns help with capacity planning, and predictive
queries enable proactive infrastructure management before problems occur.

## Service level and reliability queries

These queries express Service Level Indicators (SLIs) and error budgets. For what SLIs, SLOs, and error budgets mean and how to choose them, see [metrics monitoring concepts]({{< relref "/overview/observability/data-management/data-exploration/metrics-monitoring-concepts" >}}).

```promql
# Availability SLI (percentage of successful requests)
sum(rate(http_requests_total{status!~"5.."}[5m])) /
sum(rate(http_requests_total[5m])) * 100

# Latency SLI (percentage of requests under threshold)
sum(rate(http_request_duration_seconds_bucket{le="0.1"}[5m])) /
sum(rate(http_request_duration_seconds_count[5m])) * 100

# Error budget consumption rate
(1 - (
  sum(rate(http_requests_total{status!~"5.."}[30d])) /
  sum(rate(http_requests_total[30d]))
)) / 0.001  # 99.9% SLO
```

### Anomaly detection patterns

Identify unusual behavior and potential issues:

```promql
# Traffic spike detection
sum(rate(http_requests_total[5m])) /
  avg_over_time(sum(rate(http_requests_total[5m]))[1h:5m]) > 2

# Capacity planning prediction
predict_linear(node_filesystem_avail_bytes[1h], 4*3600) < 0

# Performance troubleshooting workflow
# Step 1: Find resource bottlenecks
topk(5, rate(container_cpu_usage_seconds_total{container!="POD"}[5m]))

# Step 2: Check for throttling
rate(container_cpu_cfs_throttled_seconds_total[5m]) > 0
```

**Proactive problem detection**: Use statistical and predictive techniques to
identify issues before they impact users. Traffic spike detection reveals
unusual load patterns, capacity predictions prevent resource exhaustion, and
systematic troubleshooting workflows help diagnose performance problems
efficiently.

## Performance optimization

### Best practices

- **Use recording rules** for complex, frequently executed queries
- **Limit time ranges** to actual analysis needs (avoid excessive historical
  queries)
- **Prefer `without()`** over `by()` when keeping most labels
- **Use exact matches** (`=`) instead of regex (`=~`) when possible

### Efficient query patterns

```promql
# Efficient: Pre-aggregated via recording rule
cluster:cpu_usage:rate5m{cluster_id="production"}

# Efficient: Limited cardinality
topk(10, sum by (service) (rate(http_requests_total[5m])))

# Avoid: High cardinality aggregation
sum by (instance, pod, container) (
  rate(container_cpu_usage_seconds_total[5m]))
```

Learn more about [recording rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}})
and [aggregation operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators).

## See also

- [Metrics monitoring concepts]({{< relref "/overview/observability/data-management/data-exploration/metrics-monitoring-concepts" >}}): query construction methodology, the label model, and SLIs/SLOs
- [Data exploration]({{< relref "/overview/observability/data-management/data-exploration" >}}): how to access Grafana and select a Prometheus data source
- [Dashboard creation]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}): visualize your PromQL queries in dashboards
- [Alerting rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}): turn these queries into proactive alerts
- [official Prometheus documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/): the complete PromQL specification
