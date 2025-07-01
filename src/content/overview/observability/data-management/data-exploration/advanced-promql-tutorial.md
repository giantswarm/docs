---
title: Advanced PromQL Tutorial
description: Learn advanced PromQL techniques for querying and analyzing metrics data in the Giant Swarm observability platform.
weight: 20
menu:
  principal:
    parent: overview-observability-data-exploration
    identifier: overview-observability-advanced-promql
last_review_date: 2025-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I write advanced PromQL queries?
  - What are the best practices for metrics analysis?
  - How do I create complex aggregations and calculations?
  - How do I monitor Kubernetes resources effectively?
---

PromQL (Prometheus Query Language) is the powerful query language used by
Prometheus and Mimir for analyzing time-series metrics data. This tutorial
covers advanced PromQL techniques specifically for the Giant Swarm
observability platform, helping you gain deep insights into your cluster and
application performance.

For PromQL fundamentals and complete syntax reference, refer to the
[official Prometheus PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).

## Prerequisites

- Access to your installation's Grafana interface (see
  [accessing Grafana tutorial]({{< relref "/tutorials/observability/data-exploration/accessing-grafana/" >}}))
- Familiarity with basic PromQL syntax and concepts
- Understanding of Prometheus metrics and labels

## Essential PromQL building blocks

This section covers key concepts you'll use throughout advanced monitoring scenarios.

### Query construction methodology

Build effective queries systematically:

1. **Define the question**: What exactly are you measuring?
2. **Identify metrics**: Which time series contain the data?
3. **Progressive construction**: Start simple, add complexity step by step
4. **Test and optimize**: Validate results and performance

#### Example: Service error rate

```promql
# Step 1: Basic selection
http_requests_total{service="web-api"}

# Step 2: Add rate calculation  
rate(http_requests_total{service="web-api"}[5m])

# Step 3: Calculate error percentage
sum(rate(http_requests_total{service="web-api", status=~"5.."}[5m])) / 
sum(rate(http_requests_total{service="web-api"}[5m])) * 100
```

### Key functions and patterns

**Rate calculations**: `rate(metric[5m])` for per-second rates from counters
**Aggregations**: `sum by (label) (metric)` or `sum without (label) (metric)`
**Percentiles**: `histogram_quantile(0.95, rate(metric_bucket[5m]))`
**Time shifting**: `metric offset 1h` for historical comparison
**Predictions**: `predict_linear(metric[1h], 3600)` for forecasting

**Performance tip**: Use `without()` instead of `by()` when keeping most
labels - it's more efficient.

### Giant Swarm label structure

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
operations, Etcd performance impacts cluster state storage, pod restarts
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

## Alerting and service level monitoring

### Service level indicators

Define and monitor key reliability metrics:

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

**Reliability engineering foundation**: Service Level Indicators (SLIs) provide
objective, measurable definitions of service quality that directly correlate
with user experience. These metrics form the basis for Service Level Objectives
(SLOs), error budgets, and data-driven reliability decisions.

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

Learn more about [recording rules]({{< relref "/tutorials/observability/alerting/create-rules" >}})
and [aggregation operators](https://prometheus.io/docs/prometheus/latest/querying/operators/#aggregation-operators).

## Next steps

- Create [custom dashboards]({{< relref "/tutorials/observability/data-exploration/creating-custom-dashboards" >}})
  with your PromQL queries
- Set up [alerting rules]({{< relref "/tutorials/observability/alerting/create-rules" >}})
  for proactive monitoring
- Explore [multi-tenancy]({{< relref "/tutorials/observability/multi-tenancy" >}})
  for organizing metrics data

For a comprehensive PromQL reference, see the
[official Prometheus documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).
