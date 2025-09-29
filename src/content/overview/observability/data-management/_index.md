---
title: Data management
description: Learn how to manage observability data including ingestion, exploration, transformation, and export in the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview-observability
    identifier: overview-observability-data-management
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I manage observability data?
  - What data management capabilities are available?
  - What types of data can I collect?
  - How do I explore and export data?
  - How do I ingest logs, metrics and traces?
  - How do I transform or enrich my data?
  - How do I connect external tools to observability data?
---

Data management is the backbone of our observability platform, giving you complete control over how your observability data flows through the system. From collecting logs, metrics and traces to exploring and analyzing them, our platform offers powerful capabilities to handle your data lifecycle efficiently.

Think of data management as your control center for observability—it's where you decide what data to collect, how to organize it, and how to make it useful for your teams.

## Supported data types

Our observability platform handles three key types of observability data:

### Metrics

Time-series data that tracks numerical values over time, perfect for monitoring system health, performance trends, and capacity planning. We store metrics in **[Mimir](https://grafana.com/oss/mimir/)**, a horizontally scalable, multi-tenant time series database.

**Examples:**

- CPU and memory usage
- Request rates and response times
- Error counts and success rates
- Custom application metrics

### Logs

Detailed records of events and activities from your applications and infrastructure. We aggregate logs using **[Loki](https://grafana.com/oss/loki/)**, designed for efficiency and seamless integration with our metrics stack.

**Examples:**

- Application debug and error messages
- Kubernetes events and audit logs
- System and security logs
- Custom structured logs

### Traces

Detailed records of requests as they flow through distributed systems, showing the complete journey from service to service. We store traces using **[Tempo](https://grafana.com/oss/tempo/)**, built for high-volume trace ingestion and efficient storage.

**Examples:**

- HTTP request traces across microservices
- Database query spans and performance
- Service-to-service communication patterns
- Application performance bottlenecks

**Note:** Trace ingestion is available in alpha from cluster release v31 and fully supported from v33. Tracing is disabled by default and can be enabled on request through your Account Engineer.

## Data management capabilities

Our platform provides comprehensive capabilities to handle your observability data throughout its lifecycle:

### Data ingestion

Flexible collection from multiple sources:

- **[Metrics ingestion]({{< relref "/overview/observability/data-management/data-ingestion/#metrics-ingestion" >}})**: Collect metrics from applications, infrastructure, and external sources using ServiceMonitors and PodMonitors
- **[Log ingestion]({{< relref "/overview/observability/data-management/data-ingestion/#logs-ingestion" >}})**: Gather logs from applications and infrastructure using PodLogs and automatic collection
- **[Trace ingestion]({{< relref "/overview/observability/data-management/data-ingestion/#trace-ingestion" >}})**: Collect distributed traces from instrumented applications using OpenTelemetry Protocol (OTLP)
- **External data sources**: Push data from external systems via our [Data Import and Export API]({{< relref "/overview/observability/data-management/data-import-export" >}})

### Data exploration

Advanced querying and analysis capabilities:

- **[Interactive exploration]({{< relref "/overview/observability/data-management/data-exploration" >}})**: Use Grafana's Explore feature for ad-hoc analysis with PromQL, LogQL, and TraceQL
- **[Dashboard management]({{< relref "/overview/observability/dashboard-management/dashboard-creation/" >}})**: Build custom visualizations with GitOps workflows or through the Grafana UI
- **Query languages**: [PromQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial.md" >}}) for metrics, [LogQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial/" >}}) for logs, and [TraceQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-traceql-tutorial/" >}}) for traces with powerful filtering and analysis

### Data transformation

**[Transform and enrich your data]({{< relref "/overview/observability/data-management/data-transformation" >}})** during collection and visualization:

- **[Recording rules]({{< relref "/overview/observability/alert-management/alert-rules#recording-rules" >}})**: Pre-compute expensive PromQL expressions for better performance
- **Relabeling rules**: Modify, filter, or enrich metrics and logs before storage
- **Data parsing**: Extract structured data from logs and add contextual information
- **Grafana transformations**: Client-side data processing for visualization

### Data import and export

Access your data programmatically for external analysis and integration, and send external data to the platform:

- **[Data import and export capabilities]({{< relref "/overview/observability/data-management/data-import-export" >}})**: Secure API access for external tools and custom integrations, plus data import from external sources
- **External Grafana integration**: Connect self-managed Grafana instances to Giant Swarm data
- **Programmatic access**: REST APIs compatible with Loki and Prometheus standards
- **Data ingestion**: Send logs from external systems using Loki's native format
- **OpenTelemetry Protocol (OTLP)**: Native support for trace ingestion using industry-standard OTLP format
