---
title: TraceQL query reference
linkTitle: TraceQL query reference
diataxis_content_type: reference
description: Reference for TraceQL, Grafana Tempo's query language, on the Giant Swarm observability platform, covering syntax, query patterns, and best practices.
weight: 45
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-traceql
last_review_date: 2025-09-29
aliases:
  - /overview/observability/data-management/data-exploration/advanced-traceql-tutorial/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I query traces with TraceQL?
  - What TraceQL syntax should I use?
  - How do I filter traces by service or operation?
  - How do I analyze trace performance with TraceQL?
  - What are common TraceQL query patterns?
---

TraceQL is Grafana Tempo's native query language for distributed trace analysis. Unlike log or metrics queries, TraceQL searches and filters across the hierarchical structure of traces and spans. This page is a reference for its syntax and the query patterns most useful on the Giant Swarm Observability Platform.

Tracing must be enabled on your cluster and your applications must be instrumented to send traces to `otlp-gateway.kube-system.svc` before these queries return data. See the [data ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion" >}}) for setup, and the [data exploration guide]({{< relref "/overview/observability/data-management/data-exploration" >}}) for accessing the Tempo data source in Grafana. For task-oriented troubleshooting with these queries, see [troubleshoot traces with TraceQL]({{< relref "/overview/observability/data-management/data-exploration/troubleshoot-traces-with-traceql" >}}). The authoritative language specification is the [Grafana TraceQL documentation](https://grafana.com/docs/tempo/latest/traceql/).

## Trace data model

Traces consist of spans organized in a tree structure. Understanding this hierarchy is what makes TraceQL's scope selectors meaningful:

- **Trace**: The complete journey of a request through your system
- **Span**: An individual operation within the trace (a service call, database query, etc.)
- **Root span**: The entry point of the trace
- **Child spans**: Operations triggered by parent spans

## Syntax fundamentals

TraceQL queries follow this basic pattern:

```traceql
{span.attribute = "value"}
```

Basic elements:

- **Scope selectors**: `span.`, `resource.`, `trace.`
- **Attribute names**: The specific attribute you want to filter on
- **Operators**: `=`, `!=`, `>`, `<`, `>=`, `<=`, `=~` (regex)
- **Values**: Strings, numbers, or durations

## Essential queries

### Finding traces by service

Query traces involving a specific service:

```traceql
{resource.service.name = "user-service"}
```

Find traces involving multiple services:

```traceql
{resource.service.name = "user-service"} && {resource.service.name = "payment-service"}
```

### Filtering by operation name

Find specific operations within services:

```traceql
{span.name = "GET /api/users"}
```

Use regex for pattern matching:

```traceql
{span.name =~ "GET /api/.*"}
```

### Performance-based filtering

Find slow traces (duration in nanoseconds):

```traceql
{trace.duration > 5s}
```

Find traces with errors:

```traceql
{status = error}
```

Combine conditions:

```traceql
{trace.duration > 2s && status = error}
```

## Advanced filtering techniques

### HTTP-specific queries

Find traces for specific HTTP methods:

```traceql
{span.http.method = "POST"}
```

Filter by HTTP status codes:

```traceql
{span.http.status_code >= 400}
```

Find slow HTTP requests:

```traceql
{span.http.method = "GET" && span.duration > 1s}
```

### Database operation analysis

Find database queries:

```traceql
{span.db.system = "postgresql"}
```

Analyze slow database operations:

```traceql
{span.db.system = "postgresql" && span.duration > 500ms}
```

Find specific database operations:

```traceql
{span.db.operation = "SELECT" && span.db.name = "users"}
```

### Custom attribute filtering

Many applications add custom attributes to spans. Filter using these:

```traceql
{span.custom.user_id = "12345"}
```

Find traces for specific customers or tenants:

```traceql
{span.tenant.id = "customer-abc"}
```

## Performance analysis patterns

### Identifying bottlenecks

Find the slowest traces by setting a concrete duration threshold, then sort the result list by duration in Grafana:

```traceql
{trace.duration > 10s}
```

Find services with high error rates:

```traceql
{resource.service.name = "payment-service" && status = error}
```

### Capacity planning queries

Count spans per service:

```traceql
{resource.service.name = "api-gateway"} | count()
```

Analyze request patterns:

```traceql
{span.http.method = "POST" && span.http.route = "/api/orders"}
```

## Service graph exploration

Tempo generates service graphs from trace data. Use TraceQL to understand service interactions. For the service graph feature itself, see [service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs" >}}).

### Analyze service dependencies

Find all services called by a specific service:

```traceql
{resource.service.name = "api-gateway"} | by(resource.service.name)
```

### Identify service communication patterns

Find cross-service calls:

```traceql
{span.kind = "client"} && {resource.service.name != parent.resource.service.name}
```

## Aggregation and structural queries

### Aggregation functions

Count traces matching criteria:

```traceql
{resource.service.name = "api-service"} | count()
```

Calculate percentiles:

```traceql
{resource.service.name = "api-service"} | quantile(0.95)
```

### Structural queries

Find traces with specific span relationships:

```traceql
{span.name = "database-query" && parent.span.name = "user-lookup"}
```

Query trace topology:

```traceql
{trace.root.service.name = "api-gateway" && span.kind = "server"}
```

## Best practices

### Query optimization

- **Start specific**: Begin with service or operation names before adding duration filters
- **Use time ranges**: Always specify time ranges to improve query performance
- **Limit results**: Use `| limit(100)` for exploratory queries

### Common patterns

1. **Error investigation**:

   ```traceql
   {status = error} | by(resource.service.name) | count()
   ```

2. **Performance analysis**:

   ```traceql
   {trace.duration > 5s} | by(resource.service.name) | quantile(0.95)
   ```

3. **Service dependency mapping**:

   ```traceql
   {resource.service.name = "my-service"} | by(span.kind, resource.service.name)
   ```

### Avoiding common mistakes

- **Don't over-filter**: Too many conditions can return no results
- **Mind the hierarchy**: Remember that traces have spans, not the other way around
- **Use appropriate time ranges**: Excessively long time ranges can time out

## See also

- [Troubleshoot traces with TraceQL]({{< relref "/overview/observability/data-management/data-exploration/troubleshoot-traces-with-traceql" >}}): task-oriented workflows for debugging with these queries
- [Service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs" >}}): visualize service dependencies from trace data
- [Data exploration]({{< relref "/overview/observability/data-management/data-exploration" >}}): access Grafana and the Tempo data source
- [Grafana TraceQL documentation](https://grafana.com/docs/tempo/latest/traceql/): the complete language specification
