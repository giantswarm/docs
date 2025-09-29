---
title: Service graphs
description: Visualize and analyze service topology and communication patterns using Tempo's service graph feature.
weight: 40
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-service-graphs
last_review_date: 2025-09-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What are service graphs?
  - How do I access service graphs in Grafana?
  - How are service graphs generated from traces?
  - What metrics are available in service graphs?
  - How do I troubleshoot service communication issues?
  - How do I analyze service dependencies?
---

Service graphs provide an automatic visual representation of your distributed system's architecture, generated directly from your trace data. They show how services communicate, traffic patterns, and performance characteristics - giving you instant insight into your system's topology without any additional configuration.

## What are service graphs?

Service graphs are automatically generated visualizations that show:

- **Service topology**: How your services connect and depend on each other
- **Communication patterns**: Request flows and traffic volume between services  
- **Performance indicators**: Response times and error rates for each interaction
- **System health**: Visual indicators of service and connection health

The graphs are created automatically as Tempo processes your traces, analyzing span relationships to understand service dependencies.

## How to access service graphs

1. **Navigate to Explore**: Click the compass icon in Grafana's left sidebar
2. **Select Tempo data source**: Choose your Tempo data source from the dropdown
3. **Switch to Service Graph**: Click the "Service Graph" tab at the top of the query interface
4. **View the graph**: The service graph will automatically load showing your system's topology

![Service Graph in Grafana](../service-graph.png)

**Time range tip**: Use longer time ranges (1+ hours) to see comprehensive service topology, or shorter ranges (15-30 minutes) for current service interactions.

## Reading service graphs

### Nodes (services)

Each circle represents a service, showing:

- **Service name**: From the `service.name` attribute in traces
- **Color coding**: Green (healthy), yellow (warnings), red (errors)
- **Request rate**: Requests per second handled by the service

### Edges (Connections)

Arrows between services show:

- **Direction**: Who calls whom
- **Thickness**: Request volume (thicker = more traffic)
- **Color**: Health status (red for high error rates)

### Key metrics displayed

- **Request rates**: Traffic volume between services
- **Error rates**: Failed request percentages  
- **Response times**: Latency for service interactions

## Common use cases

### Identifying issues

- **Red nodes/edges**: Services or connections with high error rates
- **Missing services**: Services that should be present but aren't showing up
- **Thick edges with slow response**: High-traffic paths that are performing poorly
- **Isolated services**: Services that aren't communicating as expected

### Understanding architecture

- **Hub services**: Central services that many others depend on
- **Service chains**: Long paths of service-to-service calls
- **External dependencies**: Services that call external systems
- **Traffic patterns**: Which services handle the most requests

### Troubleshooting workflows

1. **Start with the service graph** to get an overview of system health
2. **Identify problematic connections** (red or slow edges)
3. **Click on connections** to drill down to individual traces
4. **Use service names** to filter logs and metrics for deeper analysis

## Best practices

### For better service graphs
- **Use consistent service names**: Avoid including instance IDs or dynamic values
- **Instrument all service boundaries**: Ensure traces capture all service-to-service calls
- **Include meaningful operation names**: Help differentiate between different types of calls

### For effective analysis

- **Start with recent time ranges** for current system state
- **Use longer ranges** to understand overall architecture and patterns
- **Combine with other data**: Use service names to query metrics and logs

## Next steps

To get the most value from service graphs:

- **[Configure comprehensive tracing]({{< relref "/overview/observability/data-management/data-ingestion/#trace-ingestion" >}})**: Ensure all critical services are instrumented
- **[Learn TraceQL]({{< relref "/overview/observability/data-management/data-exploration/advanced-traceql-tutorial/" >}})**: Use advanced queries to complement service graph insights
- **[Set up trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/trace-derived-metrics/" >}})**: Configure alerting based on service graph metrics

- **[Create service dashboards]({{< relref "/overview/observability/dashboard-management/dashboard-creation/" >}})**: Build custom visualizations for service health

For more information about Tempo's service graph feature, see the [Grafana Tempo documentation](https://grafana.com/docs/tempo/latest/metrics-generator/service-graphs/).
