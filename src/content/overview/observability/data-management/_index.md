---
title: Data Management
description: Learn how to manage observability data including ingestion, exploration, transformation, and export in the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview-observability
    identifier: overview-observability-data-management
last_review_date: 2025-07-08
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I manage observability data?
  - What data management capabilities are available?
---

Data management is the backbone of our observability platform, giving you complete control over how your observability data flows through the system. From collecting metrics and logs to exploring and analyzing them, our platform offers powerful capabilities to handle your data lifecycle efficiently.

Think of data management as your control center for observability - it's where you decide what data to collect, how to organize it, and how to make it useful for your teams.

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

## Data management capabilities

Our platform provides comprehensive capabilities to handle your observability data throughout its lifecycle:

### Data ingestion

Flexible collection from multiple sources:

- **[Metrics ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}#metrics-ingestion)**: Collect metrics from applications, infrastructure, and external sources using ServiceMonitors and PodMonitors
- **[Log ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}#log-ingestion)**: Gather logs from applications and infrastructure using PodLogs and automatic collection
- **External data sources**: Push data from external systems via our [Observability Platform API]({{< relref "/overview/observability/observability-platform-api" >}})

### Data exploration

Advanced querying and analysis capabilities:

- **[Interactive exploration]({{< relref "/overview/observability/data-management/data-exploration" >}})**: Use Grafana's Explore feature for ad-hoc analysis with PromQL and LogQL
- **[Dashboard management]({{< relref "overview/observability/dashboard-management/dashboard-creation/" >}})**: Build custom visualizations with GitOps workflows or through the Grafana UI
- **Query languages**: [PromQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-promql-tutorial.md" >}}) for metrics and [LogQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-logql-tutorial/" >}}) for logs with powerful filtering and aggregation

### Data transformation

Process and enrich your data during collection:

- **Relabeling rules**: modify, filter, or enrich metrics and logs before storage
- **Data validation**: ensure data quality and compliance with platform standards
- **Parsing and enrichment**: extract structured data from logs and add contextual information

### Data export

Access your data programmatically:

- **[API access]({{< relref "/overview/observability/observability-platform-api" >}})**: Programmatic data ingestion and retrieval via REST APIs
- **External integration**: Connect to external monitoring tools and data sources
- **Standard protocols**: Support for OpenTelemetry Protocol (OTLP) and Prometheus remote write
