---
title: Advanced PromQL Tutorial
description: Learn advanced PromQL techniques for querying and analyzing metrics data in the Giant Swarm observability platform.
weight: 20
menu:
  principal:
    parent: overview-observability-data-exploration
    identifier: overview-observability-advanced-promql
last_review_date: 2024-12-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I write advanced PromQL queries?
  - What are the best practices for metrics analysis?
  - How do I create complex aggregations and calculations?
  - How do I monitor Kubernetes resources effectively?
---

PromQL (Prometheus Query Language) is the powerful query language used by Prometheus and Mimir for analyzing time-series metrics data. This tutorial covers advanced PromQL techniques specifically for the Giant Swarm observability platform, helping you gain deep insights into your cluster and application performance.

For PromQL fundamentals and complete syntax reference, refer to the [official Prometheus PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).

## Prerequisites

- Access to your installation's Grafana interface (see [accessing Grafana tutorial]({{< relref "/tutorials/observability/data-exploration/accessing-grafana/" >}}))
- Basic understanding of metrics, labels, and time-series concepts

## Advanced metric selection and filtering

### Cluster and workload targeting

Target specific clusters and components using label combinations:

```promql
# CPU usage for management cluster nodes
node_cpu_seconds_total{cluster_id="installation", cluster_type="management_cluster", mode="idle"}

# Memory usage for workload cluster applications
container_memory_usage_bytes{cluster_id="cluster", cluster_type="workload_cluster", namespace="production", container!="POD"}

# API server request rates across clusters
rate(apiserver_request_total{cluster_id=~".*", verb="GET"}[5m])
```

These queries demonstrate how to use Giant Swarm's labeling conventions to target specific infrastructure components.

### Label-based filtering patterns

Use sophisticated label matching for precise metric selection:

```promql
# High-priority pods only
kube_pod_info{priority_class=~"system-.*|critical-.*"}

# Exclude system namespaces
container_cpu_usage_seconds_total{namespace!~"kube-system|giantswarm|kube-.*"}

# Multi-dimensional filtering
up{job=~"kubernetes-.*", instance=~".*:443"} == 1
```

Regular expressions in label selectors allow you to create flexible filters that adapt to your naming conventions and exclude noise from system components.

## Resource monitoring and capacity planning

### Node-level resource analysis

Monitor infrastructure health and capacity:

```promql
# Node CPU utilization percentage
(1 - avg by (instance, cluster_id) (rate(node_cpu_seconds_total{mode="idle"}[5m]))) * 100

# Node memory utilization with buffers/cache excluded
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk space utilization by mount point
(1 - (node_filesystem_avail_bytes{fstype!~"tmpfs|fuse.lxcfs"} / node_filesystem_size_bytes)) * 100

# Network I/O rates
rate(node_network_receive_bytes_total{device!~"lo|veth.*|docker.*|flannel.*|cali.*"}[5m])
```

These fundamental infrastructure metrics help you understand resource consumption patterns and identify capacity constraints before they impact workloads.

### Pod and container resource tracking

Analyze application resource consumption:

```promql
# Top CPU consuming pods
topk(10, sum by (namespace, pod) (rate(container_cpu_usage_seconds_total{container!="POD"}[5m])))

# Memory usage by namespace with limits
sum by (namespace) (container_memory_usage_bytes{container!="POD"}) / 
sum by (namespace) (container_spec_memory_limit_bytes{container!="POD"}) * 100

# Containers hitting CPU throttling
rate(container_cpu_cfs_throttled_seconds_total[5m]) > 0
```

Container-level metrics reveal which applications consume the most resources and help identify performance bottlenecks caused by resource limits.

## Application performance monitoring

### HTTP request analysis

Monitor application endpoints and performance:

```promql
# Request rate by status code
sum by (method, status) (rate(http_requests_total[5m]))

# 95th percentile response time
histogram_quantile(0.95, sum by (le) (rate(http_request_duration_seconds_bucket[5m])))

# Error rate calculation
sum(rate(http_requests_total{status=~"5.."}[5m])) / 
sum(rate(http_requests_total[5m])) * 100

# Requests per second growth over time
increase(http_requests_total[1h]) / 3600
```

HTTP metrics provide insights into user experience and application health, helping you track both performance trends and error patterns.

### Database and queue monitoring

Track data persistence and message processing:

```promql
# Database connection pool utilization
database_connections_active / database_connections_max * 100

# Queue depth and processing rates
queue_depth{queue_name="critical-tasks"} and
rate(queue_processed_total{queue_name="critical-tasks"}[5m])

# Cache hit ratio
rate(cache_hits_total[5m]) / (rate(cache_hits_total[5m]) + rate(cache_misses_total[5m])) * 100
```

Backend service metrics help identify bottlenecks in data storage and processing pipelines, crucial for maintaining application responsiveness.

## Kubernetes-specific monitoring

### Cluster health indicators

Monitor Kubernetes control plane and workload health:

```promql
# API server availability and latency
up{job="kubernetes-apiservers"} and
histogram_quantile(0.99, rate(apiserver_request_duration_seconds_bucket{verb="GET"}[5m]))

# etcd health and performance
up{job="kubernetes-etcd"} and
histogram_quantile(0.99, rate(etcd_request_duration_seconds_bucket[5m]))

# Pod restart rate
increase(kube_pod_container_status_restarts_total[1h]) > 0

# Nodes not ready
kube_node_status_condition{condition="Ready", status!="true"} == 1
```

Control plane monitoring ensures the Kubernetes cluster itself remains healthy and responsive, preventing cascading failures.

### Workload scaling and health

Analyze deployment status and scaling patterns:

```promql
# Deployment replica availability
kube_deployment_status_replicas_available / kube_deployment_spec_replicas * 100

# HPA current vs target scaling
kube_horizontalpodautoscaler_status_current_replicas / 
kube_horizontalpodautoscaler_spec_max_replicas * 100

# Persistent volume usage
(kubelet_volume_stats_capacity_bytes - kubelet_volume_stats_available_bytes) / 
kubelet_volume_stats_capacity_bytes * 100
```

Workload metrics help you understand how well your applications are scaling and whether they have sufficient resources to handle demand.

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
sum by (cluster_id) (container_spec_cpu_quota / container_spec_cpu_period)
```

Complex aggregations allow you to analyze data across multiple dimensions simultaneously, revealing patterns that simple queries might miss.

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

Time-based analysis helps identify trends, seasonal patterns, and predict future resource needs for proactive capacity management.

## Alerting and SLI/SLO monitoring

### Service Level Indicators

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

SLI metrics form the foundation of reliability engineering, providing objective measures of service quality that align with user experience.

### Anomaly detection patterns

Identify unusual behavior and potential issues:

```promql
# Detect traffic spikes (current vs historical average)
sum(rate(http_requests_total[5m])) / 
avg_over_time(sum(rate(http_requests_total[5m]))[1h:5m]) > 2

# Memory leak detection (sustained growth)
increase(container_memory_usage_bytes[1h]) > 100*1024*1024  # 100MB increase

# Unusual error rate increase
rate(http_requests_total{status=~"5.."}[5m]) > 
avg_over_time(rate(http_requests_total{status=~"5.."}[5m])[1h]) * 5
```

Anomaly detection queries help you catch unusual patterns that might indicate problems, allowing for proactive intervention before user impact occurs.

## Performance optimization techniques

### Query efficiency best practices

Write performant PromQL queries for large-scale monitoring:

```promql
# Efficient: Pre-aggregate at recording rule level
cluster:cpu_usage_rate5m = 
  sum by (cluster_id) (rate(container_cpu_usage_seconds_total[5m]))

# Use recording rules for complex calculations
instance:network_throughput:rate5m = 
  sum by (instance) (rate(node_network_transmit_bytes_total[5m])) +
  sum by (instance) (rate(node_network_receive_bytes_total[5m]))

# Efficient dashboard queries using pre-computed metrics
cluster:cpu_usage_rate5m{cluster_id="production"}
```

Recording rules pre-compute expensive queries, reducing dashboard load times and enabling more responsive monitoring. Learn how to implement these in our [alerting and recording rules guide]({{< relref "/tutorials/observability/alerting/create-rules" >}}).

### Resource-aware querying

Balance query precision with resource consumption:

```promql
# Use appropriate time ranges - avoid overly long lookbacks
rate(metric_name[5m])  # Good for real-time monitoring
rate(metric_name[1h])  # Good for trend analysis

# Limit cardinality with topk/bottomk
topk(20, sum by (service) (rate(http_requests_total[5m])))

# Use efficient aggregations
sum without (instance) (up)  # More efficient than sum by (job, cluster_id, ...)
```

Query optimization techniques ensure your monitoring remains performant even as your infrastructure scales, preventing monitoring overhead from impacting system performance.

## Practical troubleshooting scenarios

### Diagnosing performance issues

Common troubleshooting workflows using PromQL:

```promql
# Step 1: Identify high CPU usage containers
topk(5, rate(container_cpu_usage_seconds_total{container!="POD"}[5m]))

# Step 2: Check if they're hitting CPU limits
rate(container_cpu_cfs_throttled_seconds_total[5m]) > 0

# Step 3: Correlate with memory pressure
container_memory_usage_bytes / container_spec_memory_limit_bytes > 0.8
```

Step-by-step diagnostic approaches help you quickly identify root causes during incidents, reducing mean time to resolution.

### Capacity planning queries

Monitor resource trends for proactive scaling:

```promql
# Predict node CPU exhaustion
predict_linear(
  (1 - avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[1h])))[24h:1h], 
  7*24*3600
) > 0.8

# Identify underutilized resources
avg by (cluster_id) (rate(container_cpu_usage_seconds_total[1h])) < 0.1
```

Predictive queries enable proactive capacity management, helping you scale infrastructure before resource constraints impact performance.

## Giant Swarm platform integration

### Platform-specific monitoring

Leverage Giant Swarm's observability capabilities:

```promql
# Monitor cluster health across installations
up{job="cluster-operator"} == 0

# Track app deployment status
sum by (cluster_id, app_name) (app_operator_app_info{status!="deployed"})

# Observe platform version distribution
count by (version) (cluster_release_version)
```

Platform-specific metrics provide insights into Giant Swarm's operational components, helping you monitor the health of the management layer itself.

## Performance considerations

When writing PromQL queries, follow these best practices:

- **Use recording rules** for frequently executed complex queries
- **Limit time ranges** to what's actually needed for the analysis
- **Prefer efficient aggregations** using `without` instead of `by` when possible
- **Avoid high-cardinality operations** on metrics with many series
- **Use appropriate rate intervals** (typically 4x scrape interval minimum)

For dashboard optimization and complex alerting scenarios, consider creating [recording rules]({{< relref "/tutorials/observability/alerting/create-rules" >}}) to pre-compute expensive calculations.

## Next steps

- Apply your PromQL queries in [custom dashboard creation]({{< relref "/tutorials/observability/data-exploration/creating-custom-dashboards" >}})
- Set up [intelligent alerting rules]({{< relref "/tutorials/observability/alerting/create-rules" >}}) based on your metric analysis
- Explore [multi-tenancy]({{< relref "/tutorials/observability/multi-tenancy" >}}) for organizing your metrics data

For comprehensive PromQL syntax, functions, and operators reference, consult the [official Prometheus PromQL documentation](https://prometheus.io/docs/prometheus/latest/querying/basics/).
