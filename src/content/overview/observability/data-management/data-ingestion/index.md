---
title: Data ingestion
description: Learn how to ingest metrics and logs into the Giant Swarm observability platform.
weight: 20
menu:
  principal:
    parent: overview-observability-data-management
    identifier: overview-observability-data-management-data-ingestion
last_review_date: 2025-10-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I ingest data into the observability platform?
  - What data sources are supported?
  - How do I configure logs, metrics, and traces ingestion?
  - How do I use ServiceMonitors and PodMonitors?
  - How do I configure tracing with OpenTelemetry?
---

The Giant Swarm Observability Platform provides flexible, self-service data ingestion capabilities for logs, metrics, and traces. By default, all clusters are equipped with the necessary components to collect and forward observability data to the central platform.

## Architecture overview

Each Giant Swarm cluster comes pre-configured with:

- **[Prometheus Operator](https://prometheus-operator.dev/)**: Manages Prometheus instances and provides CRDs for metric collection configuration
- **[Grafana Alloy](https://grafana.com/oss/alloy-opentelemetry-collector/)**: Acts as the monitoring agent for metrics, logs, and traces collection
- **Central storage**: Metrics are stored in [Grafana Mimir](https://grafana.com/oss/mimir/), logs in [Grafana Loki](https://grafana.com/docs/loki/), and traces in [Grafana Tempo](https://grafana.com/oss/tempo/)

This architecture allows you to configure data collection declaratively using Kubernetes Custom Resources, making it easy to integrate into your existing deployment workflows.

## Metrics ingestion

### Application instrumentation

Before ingesting metrics, ensure your application is properly [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to expose metrics in Prometheus format.

### Using ServiceMonitors

[ServiceMonitors](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/charts/crds/crds/crd-servicemonitors.yaml) are the primary way to configure metric collection for applications that expose metrics through a Kubernetes Service.

Here's a basic ServiceMonitor example:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    # Required for discovery by the metrics agent
    observability.giantswarm.io/tenant: my_tenant
    app.kubernetes.io/instance: my-service
  name: my-service
  namespace: monitoring
spec:
  endpoints:
  - interval: 60s   # Collection frequency
    path: /metrics  # Metrics endpoint path
    port: web       # Named port exposing metrics
  selector:         # Service label selector
    matchLabels:
      app.kubernetes.io/instance: my-service
```

### Using PodMonitors

[PodMonitors](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#podmonitorspec) are useful for collecting metrics directly from pods when a Service isn't necessary or doesn't exist.

Use PodMonitors when:

- Your application doesn't require a Service for its primary function
- You need to collect metrics from specific pod instances
- You want more granular control over pod selection

### Key requirements

- **Tenant labeling**: All ServiceMonitors and PodMonitors must include the `observability.giantswarm.io/tenant` label
- **Tenant existence**: The specified tenant must exist in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization/" >}})
- **Resource considerations**: Monitor resource usage in the _ServiceMonitors Overview_ dashboard

For detailed configuration options and advanced use cases, refer to the [Prometheus Operator API documentation](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md).

## Log ingestion

### Overview

Starting from CAPA v29.2.0 and CAPZ v29.1.0, clusters automatically collect system logs and forward them to the central Loki instance. You can also configure collection of application logs using two approaches:

### Method 1: Pod labels (Recommended)

The simplest way to enable log collection is by adding a tenant label to your pods:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  namespace: example-namespace
spec:
  template:
    metadata:
      labels:
        # Enable automatic log collection
        observability.giantswarm.io/tenant: my_team
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
```

### Method 2: PodLogs resources

[PodLogs](https://grafana.com/docs/alloy/latest/reference/components/loki/loki.source.podlogs/#podlogs-custom-resource) provide more flexibility for advanced log collection scenarios:

```yaml
apiVersion: monitoring.grafana.com/v1alpha2
kind: PodLogs
metadata:
  name: example-podlog
  namespace: example-namespace
spec:
  namespaceSelector:
    matchLabels:
      kubernetes.io/metadata.name: example-namespace
  relabelings:
  # Configure tenant for data routing
  - action: replace
    replacement: myteam
    targetLabel: giantswarm_observability_tenant
  selector:
    matchLabels:
      app: nginx
```

Use PodLogs when you need to:

- Filter pods using complex label selectors
- Apply custom relabeling rules
- Collect from multiple namespaces
- Transform log metadata before ingestion

### Default log collection

System logs are automatically collected from these namespaces:

- `kube-system`
- `giantswarm`

These are managed through predefined PodLogs resources and shouldn't be modified.

## Trace ingestion

Starting from cluster release v31 (alpha) and fully supported from v33, the observability platform supports distributed tracing through OpenTelemetry Protocol (OTLP). Traces help you understand request flow and performance across your distributed applications.

**Important**: Distributed tracing must be enabled through your Account Engineer before configuration.

### OpenTelemetry instrumentation

Before ingesting traces, ensure your application is [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) with OpenTelemetry libraries for your programming language.

#### SDK configuration options

The OpenTelemetry SDK supports configuration via [standard environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration), making it easy to control trace export and resource attributes without code changes. Common options include:

- `OTEL_EXPORTER_OTLP_ENDPOINT`: Sets the OTLP endpoint for trace export (for example `http://otlp-gateway.kube-system.svc:4318`)
- `OTEL_RESOURCE_ATTRIBUTES`: Defines resource attributes such as `service.name`, `deployment.environment`, etc. Example:

  ```yaml
  env:
    - name: OTEL_RESOURCE_ATTRIBUTES
      value: "service.name=shoot"
  ```

- `OTEL_TRACES_SAMPLER`: Controls trace sampling strategy (for example `always_on`, `parentbased_always_on`, etc.)
- `OTEL_TRACES_SAMPLER_ARG`: Additional arguments for the sampler

Refer to the [OpenTelemetry Environment Variable Specification](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration) for a full list of supported options.

### Configuration

Once tracing is enabled for your cluster, configure your OpenTelemetry instrumentation to send traces to the cluster-local OTLP endpoint:

**Endpoint**: `otlp-gateway.kube-system.svc:4317` (gRPC) or `otlp-gateway.kube-system.svc:4318` (HTTP)

### Pod labeling for traces

Similar to metrics and logs, traces require proper tenant labeling for data isolation and routing. Add the tenant label to pods that send traces:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: traced-app
  namespace: example-namespace
spec:
  template:
    metadata:
      labels:
        # Required for trace data routing
        observability.giantswarm.io/tenant: my_team
        app: traced-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        env:
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otlp-gateway.kube-system.svc:4318"
        - name: OTEL_RESOURCE_ATTRIBUTES
          value: "service.name=traced-app"
```

### Supported trace formats

The platform supports traces in the following formats:

- **OTLP/gRPC**: Native OpenTelemetry protocol over gRPC (port 4317)
- **OTLP/HTTP**: OpenTelemetry protocol over HTTP (port 4318)

### Trace data considerations

- **Service graphs**: Tempo automatically generates service topology maps from trace data
- **Metrics generation**: Tempo can generate rate, error, and duration (RED) metrics from spans
- **Alerting limitation**: Direct alerting on trace data isn't supported; use metrics generated by Tempo's metrics-generator instead

## Multi-tenancy considerations

All observability data types use tenant-based routing to ensure data isolation:

- **Metrics**: Use `observability.giantswarm.io/tenant` label on ServiceMonitors/PodMonitors
- **Logs**: Use `observability.giantswarm.io/tenant` pod label or `giantswarm_observability_tenant` relabeling in PodLogs
- **Traces**: Use `observability.giantswarm.io/tenant` pod label on trace-producing pods

**Important**: Data sent to non-existent tenants will be dropped. Ensure your tenant exists in a Grafana Organization before configuring data collection.

## Performance and cost considerations

Data ingestion affects platform resource consumption:

- **Metrics**: More metrics increase Mimir resource usage
- **Logs**: More logs increase Loki resource usage and Kubernetes API server load
- **Traces**: More traces increase Tempo resource usage and network overhead
- **Network**: Log tailing and trace collection use Kubernetes API and network resources

Monitor your usage through:

- _ServiceMonitors Overview_ dashboard for metrics
- _Kubernetes / Compute Resources / Pod_ dashboard for API server impact

## Next steps

- Learn more about [data exploration]({{< relref "/overview/observability/data-management/data-exploration/" >}}) to query your ingested data
- Set up [multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}) for your teams
- Explore [dashboard creation]({{< relref "/overview/observability/dashboard-management/" >}}) to visualize your data
