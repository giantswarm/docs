---
title: Data ingestion
description: Learn how to ingest metrics, logs, and traces into the Giant Swarm observability platform.
weight: 20
menu:
  principal:
    parent: overview-observability-data-management
    identifier: overview-observability-data-management-data-ingestion
last_review_date: 2026-03-16
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I ingest data into the observability platform?
  - What data sources are supported?
  - How do I configure logs, metrics, and traces ingestion?
  - How do I use ServiceMonitors and PodMonitors?
  - How do I configure tracing with OpenTelemetry?
  - How do I send metrics via OTLP?
  - How do I send logs via OTLP?
  - How do I use the OTLP gateway?
  - How do I configure multi-tenancy for OTLP ingestion?
  - What is the X-Scope-OrgID header and how do I use it?
---

The Giant Swarm Observability Platform provides flexible, self-service data ingestion capabilities for logs, metrics, and traces. By default, all clusters are equipped with the necessary components to collect and forward observability data to the central platform.

## Architecture overview

Each Giant Swarm cluster comes pre-configured with:

- **[Prometheus Operator](https://prometheus-operator.dev/)**: Manages Prometheus instances and provides CRDs for metric collection configuration
- **[Grafana Alloy](https://grafana.com/oss/alloy-opentelemetry-collector/)**: Acts as the observability agent for metrics, logs, and traces collection
- **OTLP Gateway** (`otlp-gateway.kube-system.svc`): Accepts OpenTelemetry Protocol (OTLP) data for metrics, logs, and traces and forwards it to the central storage
- **Central storage**: Metrics are stored in [Grafana Mimir](https://grafana.com/oss/mimir/), logs in [Grafana Loki](https://grafana.com/docs/loki/latest/), and traces in [Grafana Tempo](https://grafana.com/oss/tempo/)

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
        observability.giantswarm.io/tenant: my_tenant
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

## OTLP ingestion

Starting from cluster release v31 (alpha) and fully supported from v33, the observability platform supports ingesting metrics, logs, and traces via the OpenTelemetry Protocol (OTLP) through a cluster-local gateway.

**Important**: OTLP ingestion must be enabled through your Account Engineer before use.

### Endpoint

Send OTLP data to:

- **gRPC**: `otlp-gateway.kube-system.svc:4317`
- **HTTP**: `http://otlp-gateway.kube-system.svc:4318`

### SDK configuration

Before sending data, ensure your application is [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) with OpenTelemetry libraries for your programming language.

The OpenTelemetry SDK supports configuration via [standard environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration). Common options include:

| Variable | Description |
|---|---|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP gateway endpoint (e.g. `http://otlp-gateway.kube-system.svc:4318`) |
| `OTEL_METRICS_EXPORTER` | Set to `otlp` to enable metrics export |
| `OTEL_LOGS_EXPORTER` | Set to `otlp` to enable log export |
| `OTEL_TRACES_EXPORTER` | Set to `otlp` to enable trace export (usually the SDK default) |
| `OTEL_RESOURCE_ATTRIBUTES` | Resource attributes such as `service.name`, `deployment.environment` |
| `OTEL_TRACES_SAMPLER` | Trace sampling strategy (e.g. `always_on`, `parentbased_always_on`) |
| `OTEL_TRACES_SAMPLER_ARG` | Additional arguments for the sampler |

### Tenancy

OTLP data is routed to a tenant using one of two mechanisms:

**Option 1 — HTTP header** (OTLP/HTTP only, port 4318):

Set the `X-Scope-OrgID` header via the `OTEL_EXPORTER_OTLP_HEADERS` environment variable:

```yaml
env:
  - name: OTEL_EXPORTER_OTLP_HEADERS
    value: "X-Scope-OrgID=my_tenant"
```

**Option 2 — Pod label** (works with both gRPC and HTTP):

Add the tenant label to the pods sending OTLP data:

```yaml
metadata:
  labels:
    observability.giantswarm.io/tenant: my_tenant
```

The `X-Scope-OrgID` header takes precedence over the pod label when both are present.

### Example

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: example-namespace
spec:
  template:
    metadata:
      labels:
        observability.giantswarm.io/tenant: my_tenant
        app: my-app
    spec:
      containers:
      - name: app
        image: my-app:latest
        env:
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otlp-gateway.kube-system.svc:4318"
        - name: OTEL_METRICS_EXPORTER
          value: "otlp"
        - name: OTEL_LOGS_EXPORTER
          value: "otlp"
        - name: OTEL_RESOURCE_ATTRIBUTES
          value: "service.name=my-app"
```

### Supported formats

- **OTLP/gRPC**: port 4317
- **OTLP/HTTP**: port 4318

### Trace-specific considerations

- **Service graphs**: Tempo automatically generates service topology maps from trace data
- **Metrics generation**: Tempo can generate rate, error, and duration (RED) metrics from spans
- **Alerting limitation**: Direct alerting on trace data isn't supported; use metrics generated by Tempo's metrics-generator instead

## Multi-tenancy considerations

All observability data types use tenant-based routing to ensure data isolation:

- **Metrics (Prometheus)**: Use `observability.giantswarm.io/tenant` label on ServiceMonitors/PodMonitors
- **Logs**: Use `observability.giantswarm.io/tenant` pod label or `giantswarm_observability_tenant` relabeling in PodLogs
- **Metrics, logs, and traces (OTLP)**: Use `X-Scope-OrgID` HTTP header (OTLP/HTTP) or `observability.giantswarm.io/tenant` pod label (gRPC and HTTP). The header takes precedence when both are set.

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
