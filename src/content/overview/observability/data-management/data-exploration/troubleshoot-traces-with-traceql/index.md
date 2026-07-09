---
title: Troubleshoot traces with TraceQL
linkTitle: Troubleshoot traces with TraceQL
diataxis_content_type: how-to-guide
description: Task-oriented workflows for debugging distributed traces with TraceQL on the Giant Swarm observability platform, from failed requests to performance regressions.
weight: 50
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-troubleshoot-traces-with-traceql
last_review_date: 2026-07-06
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I use TraceQL for troubleshooting?
  - How do I debug a failed request with traces?
  - How do I analyze a performance regression using traces?
  - How do I correlate traces with metrics and logs?
  - How do I surface traces in Grafana dashboards?
---

This guide walks through common troubleshooting workflows using TraceQL against traces in your Giant Swarm Observability Platform. It assumes you can already open the Tempo data source in Grafana Explore (see the [data exploration guide]({{< relref "/overview/observability/data-management/data-exploration" >}})) and know the basic query syntax (see the [TraceQL query reference]({{< relref "/overview/observability/data-management/data-exploration/traceql" >}})).

## Debug a failed request

Work from the broad set of failures down to the specific error pattern:

1. **Find error traces** for the affected service:

   ```traceql
   {span:status = error && resource.service.name = "payment-service"}
   ```

2. **Narrow down by time** to the window where the problem occurred. TraceQL has no time function; use Grafana's time range picker (top right of Explore) to bound the same query to the incident window.

3. **Analyze error patterns** by grouping on the status message:

   ```traceql
   {span:status = error} | by(span:statusMessage)
   ```

Open the individual traces the query returns to inspect the span where the error originated and the attributes attached to it.

## Analyze a performance regression

To confirm and localize a slowdown, select the slow traces for the affected service:

```traceql
{resource.service.name = "user-service" && trace:duration > 2s}
```

Then use Grafana's time range controls to compare the same query across different periods, such as before and after a deploy, to see whether latency shifted and which spans grew.

## Assess dependency impact

When one service is failing, find the traces where that failure propagates into a dependent service:

```traceql
{resource.service.name = "database-service" && span:status = error}
&& {resource.service.name = "user-service"}
```

This surfaces requests where a `database-service` error coincides with `user-service` activity, showing how far the impact spreads.

## Correlate traces with metrics and logs

Traces are most useful alongside the other signals for the same request.

**Correlate with metrics:**

1. Find problematic traces with TraceQL.
2. Extract the trace IDs from the results.
3. Use those trace IDs in PromQL queries via the `trace_id` label to line up trace timing with metric behavior.

**Correlate with logs:**

1. Find the trace in Tempo with TraceQL.
2. Use its trace ID in a LogQL query to pull the matching log lines:

   ```logql
   {namespace="my-app"} | json | trace_id="abc123"
   ```

See the [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql" >}}) and [LogQL query reference]({{< relref "/overview/observability/data-management/data-exploration/logql" >}}) for the corresponding query patterns.

## Surface traces in Grafana dashboards

Once a query is useful, make it reachable from your dashboards.

**Add a trace panel:**

1. Add a traces panel to your dashboard.
2. Configure the Tempo data source.
3. Write your TraceQL query in the query editor.
4. Use template variables for dynamic filtering.

**Link from metric panels:**

1. Add data links to a metric panel.
2. Include a trace ID variable in the link.
3. Point the link at the trace view in Grafana so you can jump straight from a metric spike to the trace behind it.

## See also

- [TraceQL query reference]({{< relref "/overview/observability/data-management/data-exploration/traceql" >}}): syntax and the full query catalog
- [Service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs" >}}): visualize service dependencies from trace data
- [Dashboard creation]({{< relref "/overview/observability/dashboard-management/dashboard-creation" >}}): build custom trace visualizations
