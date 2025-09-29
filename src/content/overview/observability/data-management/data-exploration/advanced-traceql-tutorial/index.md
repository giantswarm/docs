---
title: Advanced TraceQL tutorial
description: Learn how to use TraceQL to query and analyze distributed traces in Giant Swarm's observability platform.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-advanced-traceql-tutorial
last_review_date: 2025-09-29
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I query traces with TraceQL?
  - What TraceQL syntax should I use?
  - How do I filter traces by service or operation?
  - How do I analyze trace performance with TraceQL?
  - What are common TraceQL query patterns?
  - How do I use TraceQL for troubleshooting?
---

TraceQL is Grafana Tempo's native query language designed specifically for distributed trace analysis. Unlike traditional log or metrics queries, TraceQL lets you search and filter across the complex, hierarchical structure of traces and spans.

This tutorial builds on the concepts from [data exploration]({{< relref "/overview/observability/data-management/data-exploration" >}}) and assumes you have traces flowing into your Giant Swarm observability platform.

## Prerequisites

Before starting this tutorial:

- **Tracing enabled**: Your cluster must have tracing enabled (contact your Account Engineer)
- **Instrumented applications**: Your applications should be sending traces to `otlp-gateway.kube-system.svc`
- **Grafana access**: You can access your Grafana instance and the Tempo data source

## Understanding TraceQL basics

### Trace structure hierarchy

Traces consist of spans organized in a tree structure:

- **Trace**: The complete journey of a request through your system
- **Span**: Individual operations within the trace (service calls, database queries, etc.)
- **Root span**: The entry point of the trace
- **Child spans**: Operations triggered by parent spans

### TraceQL syntax fundamentals

TraceQL queries follow this basic pattern:

```traceql
{span.attribute = "value"}
```

Basic elements:

- **Scope selectors**: `span.`, `resource.`, `trace.`
- **Attribute names**: The specific attribute you want to filter on
- **Operators**: `=`, `!=`, `>`, `<`, `>=`, `<=`, `=~` (regex)
- **Values**: Strings, numbers, or durations

## Essential TraceQL queries

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

Find the slowest traces:

```traceql
{trace.duration > 95th percentile}
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

## Combining TraceQL with other observability data

### Correlating with metrics

Use trace IDs in metric queries to correlate performance:

1. Find problematic traces with TraceQL
2. Extract trace IDs
3. Use trace IDs in PromQL queries with `trace_id` label

### Correlating with logs

Link traces to logs using trace correlation:

1. Find traces in Tempo with TraceQL
2. Use the trace ID in LogQL: `{namespace="my-app"} | json | trace_id="abc123"`

## Service graph exploration

Tempo generates service graphs from trace data. Use TraceQL to understand service interactions:

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

## Troubleshooting workflows

### Debugging failed requests

1. **Find error traces**:

   ```traceql
   {status = error && resource.service.name = "payment-service"}
   ```

2. **Narrow down by time**:
   ```traceql
   {status = error && resource.service.name = "payment-service"} 
   | select(trace.start_time > now() - 1h)
   ```

3. **Analyze error patterns**:
   ```traceql
   {status = error} | by(span.status.message)
   ```

### Performance regression analysis

Compare performance across time periods:

```traceql
{resource.service.name = "user-service" && trace.duration > 2s}
```

Then use Grafana's time range controls to compare different periods.

### Dependency impact analysis

Find traces affected by a specific service issue:

```traceql
{resource.service.name = "database-service" && status = error} 
&& {resource.service.name = "user-service"}
```

## Advanced TraceQL features

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

1. **Error investigation workflow**:
   ```traceql
   {status = error} | by(resource.service.name) | count()
   ```

2. **Performance analysis workflow**:
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
- **Use appropriate time ranges**: Very long time ranges can timeout

## Integration with Grafana dashboards

### Creating trace panels

1. **Add a traces panel** to your dashboard
2. **Configure the Tempo data source**
3. **Write TraceQL queries** in the query editor
4. **Use template variables** for dynamic filtering

### Linking from metrics

Create drill-down links from metric panels:

1. **Add data links** to metric panels
2. **Include trace ID variables** in the link
3. **Link directly to trace view** in Grafana

## Next steps

Now that you understand TraceQL:

- **Explore service graphs**: Use Tempo's service graph feature to visualize dependencies
- **Set up trace-derived metrics**: Configure Tempo's metrics-generator for alerting
- **Create trace dashboards**: Build custom visualizations for your distributed systems
- **Integrate with alerts**: Use metrics generated from traces for proactive monitoring

For more complex scenarios, consider exploring [Grafana's TraceQL documentation](https://grafana.com/docs/tempo/latest/traceql/) and the [OpenTelemetry instrumentation guides](https://opentelemetry.io/docs/instrumentation/).
