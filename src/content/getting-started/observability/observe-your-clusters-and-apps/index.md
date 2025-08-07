---
title: Observe your clusters and apps
description: Start monitoring your Giant Swarm clusters and applications immediately with pre-configured dashboards, metrics, and logs.
weight: 10
menu:
  principal:
    parent: getting-started-observability
    identifier: getting-started-observability-observe-clusters-apps
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I start monitoring my clusters?
  - Where can I see my application metrics?
  - How do I access cluster dashboards?
  - What monitoring data is available immediately?
  - How do I view logs for my applications?
  - What's included in the default monitoring setup?
---

Your Giant Swarm clusters are automatically connected to the observability platform the moment they're created. This means you can start monitoring your infrastructure and applications immediately, without any additional setup or configuration.

This tutorial shows you how to access and use the monitoring capabilities that are ready and waiting for you.

## Access your Grafana instance

Your observability platform is accessible through your dedicated Grafana instance:

1. **Find your Grafana URL**: Your Grafana instance is available at `https://grafana.<your-base-domain>`
2. **Log in**: Use your organization's single sign-on (SSO) credentials
3. **Start exploring**: You'll see a familiar Grafana interface with data already flowing in

🔗 **Need help with access?** Check our [data exploration guide]({{< relref "/overview/observability/data-management/data-exploration/index.md" >}}) for detailed authentication steps.

## Explore pre-configured dashboards

Giant Swarm provides production-ready dashboards that give you immediate insights into your clusters and workloads.

### Platform dashboards

These dashboards show the health and performance of your Giant Swarm platform:

- **Cluster Overview**: High-level view of all your clusters, their status, and resource utilization
- **Node Monitoring**: Detailed metrics for cluster nodes including CPU, memory, disk, and network
- **Kubernetes Monitoring**: Pod status, deployments, services, and Kubernetes-specific metrics
- **Platform Health**: Giant Swarm platform components and their operational status

### Application dashboards

Monitor your workloads with dashboards designed for application observability:

- **Application Performance**: Response times, throughput, and error rates for your services
- **Resource Usage**: CPU, memory, and storage consumption by your applications
- **Network Traffic**: Service-to-service communication and external connectivity
- **Log Analysis**: Application logs with filtering and search capabilities

### Finding and using dashboards

1. **Browse by folder**: Dashboards are organized in folders like "Platform", "Applications", and "Infrastructure"
2. **Use search**: Find specific dashboards using the search bar
3. **Filter by tags**: Dashboards are tagged by cluster, namespace, or application type
4. **Bookmark favorites**: Star the dashboards you use most frequently

## Monitor cluster health

### Key metrics to watch

Your clusters generate hundreds of metrics, but here are the most important ones to start with:

**Cluster-level health:**

- Overall cluster status and node availability
- Resource utilization across the cluster
- Network connectivity and performance

**Node-level health:**

- CPU and memory usage per node
- Disk space and I/O performance
- Network traffic and errors

**Application health:**

- Pod restart counts and failure rates
- Resource requests vs. actual usage
- Service response times and error rates

### Quick health checks

Use these dashboards for rapid health assessment:

1. **Start with the Cluster Overview** to get a bird's-eye view
2. **Drill down to Node Monitoring** if you see resource issues
3. **Check Application Performance** for workload-specific problems
4. **Review Platform Health** if there are cluster-wide issues

## View application logs

### Accessing logs

Your application logs are automatically collected and available in Grafana:

1. **Go to the Explore tab** in Grafana
2. **Select the Loki data source** for log queries
3. **Use LogQL queries** to filter and search your logs
4. **Apply time ranges** to focus on specific incidents

### Common log queries

Here are some useful LogQL queries to get you started:

```logql
# All logs from a specific cluster
{cluster_id="your-cluster-name"}

# Application logs by namespace
{cluster_id="your-cluster-name", namespace="your-app-namespace"}

# Error logs only
{cluster_id="your-cluster-name"} |= "error"

# Logs from specific pods
{cluster_id="your-cluster-name", pod=~"your-app-.*"}
```

🎓 **Want to learn more?** Check our [Advanced LogQL Tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial/index.md" >}}) for powerful log analysis techniques.

## Get alerted on issues

### Default alert rules

Your clusters come with essential alert rules already configured:

- **Node down**: Get notified when cluster nodes become unavailable
- **High resource usage**: Alerts when CPU or memory usage exceeds thresholds
- **Pod failures**: Notifications about failing or repeatedly restarting pods
- **Disk space**: Warnings when storage is running low

### Viewing active alerts

1. **Check the Alerting section** in Grafana's main menu
2. **Review Alert Rules** to see what's being monitored
3. **Check Alert Groups** to see current alert status
4. **Configure contact points** to receive notifications

### Customizing alerts

While default alerts cover essential monitoring, you can customize them for your needs:

- **Adjust thresholds** based on your applications' normal behavior
- **Add application-specific alerts** for business metrics
- **Configure notification channels** like Slack, email, or PagerDuty
- **Set up alert silences** during maintenance windows

🔧 **Ready to customize?** Learn more in our [alert management documentation]({{< relref "/overview/observability/alert-management/index.md" >}}).

## Monitor application performance

### Application metrics

If your applications expose metrics (using Prometheus format), they're automatically collected and available for monitoring:

- **HTTP request metrics**: Response times, status codes, throughput
- **Business metrics**: Custom metrics specific to your application logic
- **Runtime metrics**: Garbage collection, memory usage, thread counts (for applicable languages)

### Adding metrics to your apps

To get metrics from your applications:

1. **Expose metrics endpoint**: Configure your app to serve metrics at `/metrics`
2. **Add ServiceMonitor**: Create a Kubernetes ServiceMonitor resource to tell the platform about your metrics
3. **View in Grafana**: Your metrics will appear in the Prometheus data source within minutes

Example ServiceMonitor:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: my-app-metrics
  namespace: my-app-namespace
spec:
  selector:
    matchLabels:
      app: my-app
  endpoints:
  - port: metrics
    path: /metrics
```

🚀 **Need help with metrics?** Our [data ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion/index.md" >}}) covers this in detail.

## Next steps

Now that you're monitoring your clusters and applications, here are some next steps to get even more value from the observability platform:

### Explore deeper

- **[Learn advanced querying]({{< relref "/overview/observability/data-management/data-exploration/index.md" >}})** with PromQL and LogQL
- **[Create custom dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation/index.md" >}})** tailored to your team's needs
- **[Set up multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/index.md" >}})** to organize data by team or environment

### Integrate external data

- **[Import external logs]({{< relref "/overview/observability/data-management/data-import-export/index.md" >}})** from SaaS applications or other infrastructure
- **[Export data]({{< relref "/overview/observability/data-management/data-import-export/index.md" >}})** to external monitoring tools or analytics platforms
- **[Transform data]({{< relref "/overview/observability/data-management/data-transformation/index.md" >}})** to match your organization's standards

### Scale your monitoring

- **[Configure advanced alerting]({{< relref "/overview/observability/alert-management/alert-rules/index.md" >}})** with complex conditions and routing
- **[Manage alert routing]({{< relref "/overview/observability/alert-management/alert-routing/index.md" >}})** to ensure the right teams get notified
- **[Organize teams]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization/index.md" >}})** with separate Grafana organizations

The observability platform grows with your needs - start simple and add complexity as your monitoring requirements evolve.
