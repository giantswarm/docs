---
title: Observe your clusters and apps
description: Start monitoring your clusters and applications with Giant Swarm's observability platform - from basic metrics and logs to distributed tracing, custom dashboards and alerts.
weight: 60
last_review_date: 2025-07-17
menu:
  principal:
    parent: getting-started
    identifier: getting-started-observe
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I start monitoring my applications?
  - What observability data is available out of the box?
  - How do I access Grafana dashboards?
  - How do I set up custom metrics collection?
  - How do I create my first custom dashboard?
  - How do I monitor application logs?
  - What should I monitor first in my cluster?
---

Giant Swarm's observability platform gives you immediate visibility into your clusters and applications. Every cluster comes with automatic monitoring configured out of the box, collecting metrics and logs that help you understand system health and application performance. Distributed tracing is also available to help you understand request flows across your microservices.

This guide will walk you through your first steps with the observability platform, from accessing pre-built dashboards to setting up custom monitoring for your applications.

## What you get automatically

Every Giant Swarm cluster includes:

- **Platform metrics**: CPU, memory, disk, and network metrics from all cluster nodes
- **Kubernetes metrics**: Pod status, deployments, services, and cluster events
- **Application logs**: Automatic collection from all pods in your cluster
- **Distributed tracing**: Trace collection for understanding request flows. To enable on your clusters, ask your account engineer.
- **Pre-built dashboards**: Ready-to-use visualizations for infrastructure and platform components
- **Default alerts**: Proactive notifications for common infrastructure issues
- **Secure access**: Integration with your organization's identity provider

## Prerequisites

Before you start:

1. **Running workload cluster**: If you don't have one, [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}) first
2. **Sample application**: Deploy the [`hello-world` application]({{< relref "/getting-started/install-an-application" >}}) or use your own instrumented application
3. **Local tools**: Install [`jq`](https://jqlang.github.io/jq/download/) for command-line JSON processing

**Important**: If you're using your own application, ensure it's [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to export metrics. Adding new metrics impacts platform costs, so choose your metrics thoughtfully.

## Step 1: Access your observability platform

Start by accessing Grafana, your main interface for observability data:

1. **Find your Grafana URL**: Check the ingress resource in the `monitoring` namespace of your management cluster
2. **Log in**: Use your organization's identity provider credentials
3. **Explore pre-built dashboards**: Navigate to `Dashboards` → `Giant Swarm Public Dashboards`

You'll immediately see dashboards showing:

- **Cluster overview**: Resource usage, node health, and capacity
- **Kubernetes metrics**: Pod status, deployment health, and service performance
- **Infrastructure metrics**: CPU, memory, disk, and network across all nodes
- **Platform components**: Ingress controllers, DNS, and other system services

## Step 2: Set up application metrics collection

To monitor your specific applications, you need to configure metrics collection. For the `hello-world` application, enable the built-in service monitor by setting `serviceMonitor.enabled` to `true` in your Helm values.

For custom applications, create a `ServiceMonitor` resource:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    observability.giantswarm.io/tenant: my-team
    app.kubernetes.io/instance: my-service
  name: my-service
  namespace: my-namespace
spec:
  endpoints:
  - interval: 60s
    path: /metrics
    port: web
  selector:
    matchLabels:
      app.kubernetes.io/instance: my-service
```

**Key configuration points:**

- **Tenant label**: The `observability.giantswarm.io/tenant: my-team` label is required for metrics routing and data isolation
- **Scrape interval**: Metrics are collected every 60 seconds (adjust based on your needs)
- **Metrics endpoint**: The `/metrics` path should expose Prometheus-format metrics
- **Port reference**: Use the [port name](https://kubernetes.io/docs/concepts/services-networking/service/#field-spec-ports) from your service definition
- **Label selector**: Must match your application's labels for discovery

Apply this configuration to start collecting metrics from your application.

⚠️ **Need more advanced ingestion?** See our comprehensive [Data Ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion" >}}) for logs, metrics, and traces.

## Step 3: Explore your metrics

Once metrics collection is configured, explore your data using Grafana's Explore view:

1. **Open Explore**: In Grafana, click `Explore` in the left sidebar
2. **Select data source**: Choose the appropriate Prometheus data source
3. **Query your metrics**: Use PromQL to query application metrics

![Explore application metrics](explore-application-metrics.png)

Try these sample queries to get started:

- `rate(http_requests_total[5m])` - Request rate over the last five minutes
- `histogram_quantile(0.95, http_request_duration_seconds_bucket)` - 95th percentile response time
- `up{job="my-service"}` - Check if your service is up and running

**New to PromQL?** Check our [Advanced PromQL Tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial" >}}) for detailed guidance.

## Step 4: Monitor application logs

Giant Swarm automatically collects logs from all pods. To access your application logs:

1. **Navigate to Explore**: Select the Loki data source
2. **Use LogQL queries**: Search and filter your logs

Try these sample queries:

- `{namespace="my-namespace"}` - All logs from your namespace
- `{app="my-app"} |= "error"` - Error messages from your application
- `{namespace="my-namespace"} | json | level="error"` - Structured log parsing for error levels

**Want to learn more?** Our [Advanced LogQL Tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial" >}}) covers complex log queries and analysis.

## Step 5: Set up distributed tracing (Optional)

Distributed tracing helps you understand how requests flow through your microservices architecture. Giant Swarm's observability platform supports tracing through Tempo and OpenTelemetry.

**Important**: Tracing is available in alpha from cluster release v31 and fully supported from v33. It's disabled by default and must be enabled by your account engineer.

### Prerequisites for tracing

- **Cluster version**: v31+ (alpha) or v33+ (full support)
- **Tracing enabled**: Contact your account engineer to enable tracing for your cluster
- **Application instrumentation**: Your applications must be instrumented with OpenTelemetry

### Configure trace collection

Once tracing is enabled, configure your applications to send traces to the cluster-local OpenTelemetry (OTLP) endpoint. Note that here this example make use of environment variables to configure the OLTP endpoint but your app might need to be configured via another mean.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-traced-app
spec:
  template:
    metadata:
      labels:
        # Required for trace data routing
        observability.giantswarm.io/tenant: my-team
        app: my-traced-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        env:
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otlp-gateway.kube-system.svc:4318" # 4318 for http, or 4317 for grpc
        - name: OTEL_RESOURCE_ATTRIBUTES
          value: "service.name=my-traced-app"
```

### Explore traces with TraceQL

Once traces are flowing, explore them in Grafana:

1. **Navigate to Explore**: Select the Tempo data source
2. **Use TraceQL queries**: Search and analyze your traces

Try these example queries:

- `{resource.service.name = "my-traced-app"}` - All traces from a specific service
- `{trace.duration > 5s}` - Find slow requests
- `{status = error}` - Find failed traces
- `{span.http.method = "POST" && span.http.status_code >= 400}` - Failed HTTP requests

### Service graph insights

Tempo automatically generates service graphs from your trace data, showing:

- **Service topology**: How your services communicate
- **Request rates**: Traffic between services
- **Error rates**: Failed requests between services
- **Performance metrics**: Response times and throughput

Access the service graph in Grafana under the Tempo data source's "Service Graph" tab.

**Want to learn more?** Our [Advanced TraceQL Tutorial]({{< relref "/overview/observability/data-management/data-exploration/advanced-traceql-tutorial" >}}) covers complex trace queries and analysis.

## Step 6: Review pre-built dashboards

The platform provides comprehensive pre-built dashboards for immediate insights. Access them in Grafana under `Dashboards` → `Giant Swarm Public Dashboards`:

**Infrastructure dashboards:**

- **Cluster overview**: High-level cluster health and resource usage
- **Node metrics**: Individual node performance and capacity
- **Kubernetes resources**: Pod, deployment, and service status

**Platform component dashboards:**

- **Ingress controller**: Request rates, response times, and error rates
- **DNS performance**: Query success rates and response times
- **Flux GitOps**: Deployment status and reconciliation metrics

**Application insights:**
Below is an example showing `hello-world` application metrics, including the cardinality of the `promhttp_metric_handler_requests_total` metric:

![Service monitor metrics](service-monitor-metrics.png)

These dashboards give you instant visibility into system health and help identify patterns or issues quickly.

## Step 7: Create your first custom dashboard

While pre-built dashboards provide great starting points, you'll likely want custom visualizations for your specific applications and workflows.

### Method 1: Create in Grafana UI (Quick start)

1. **Create new dashboard**: In Grafana, click `+` → `Dashboard`
2. **Add panels**: Choose visualization types (graphs, tables, stats)
3. **Configure queries**: Use PromQL for metrics, LogQL for logs, or TraceQL for traces
4. **Save dashboard**: Name and organize your dashboard

Your dashboard automatically persists in the platform's PostgreSQL storage with regular backups.

### Method 2: GitOps approach (Recommended)

For production environments, treat dashboards as code:

1. **Export dashboard JSON**: Use `Share` → `Export` from any dashboard
2. **Store in Git**: Version control your dashboard definitions
3. **Deploy via ConfigMaps**: Use Kubernetes resources to deploy dashboards
4. **Automate updates**: Integrate with your CI/CD pipeline

[Download our example dashboard](./dashboard.json) or check our [comprehensive dashboard creation guide]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}) for detailed instructions.

### Import the example dashboard

To quickly get started with a custom dashboard:

- **Open import**: Go to `Dashboards` → `New` → `Import`

![dashboard-import-new](dashboard-import.png)

- **Upload JSON**: Load the [example dashboard file](./dashboard.json)

![dashboard-import-panel](dashboard-import-json.png)

- **Explore the result**: Your new dashboard shows application-specific metrics

![custom-dashboard](custom-dashboard.png)

The example dashboard demonstrates key application metrics like error rates, success rates, and request distribution by HTTP status code.

## What's next

Now that you're monitoring your clusters and applications, explore these advanced capabilities:

### Enhance your observability

- **[Set up alerting]({{< relref "/overview/observability/alert-management/" >}})**: Get notified before issues impact users
- **[Learn advanced querying]({{< relref "/overview/observability/data-management/data-exploration/" >}})**: Master PromQL and LogQL for deeper insights
- **[Configure data ingestion]({{< relref "/overview/observability/data-management/data-ingestion/" >}})**: Collect custom logs, metrics, and traces
- **[Explore data transformation]({{< relref "/overview/observability/data-management/data-transformation/" >}})**: Optimize metrics storage and processing

### Integrate external tools

- **[Import/export data]({{< relref "/overview/observability/data-management/data-import-export/" >}})**: Connect external systems and analysis tools
- **[Set up multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: Organize data access for teams and environments

Ready to explore platform security? Learn more [in the security overview]({{< relref "/overview/security" >}}).
