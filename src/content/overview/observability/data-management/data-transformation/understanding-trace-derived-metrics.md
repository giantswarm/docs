---
title: Understanding trace-derived metrics
linkTitle: Understanding trace-derived metrics
diataxis_content_type: explanation
description: Why the Giant Swarm observability platform derives metrics from trace data, what RED metrics are, and the monitoring patterns they enable.
weight: 20
menu:
  principal:
    parent: overview-observability-data-management-data-transformation
    identifier: overview-observability-data-management-data-transformation-understanding-trace-derived-metrics
last_review_date: 2026-07-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - Why can't I alert directly on trace data?
  - What are RED metrics?
  - Why derive metrics from traces?
  - What monitoring patterns do trace-derived metrics enable?
---

This page explains why the Giant Swarm Observability Platform derives metrics from your traces and what those metrics represent. For the catalog of metrics and how to query them, see the [trace-derived metrics reference]({{< relref "/overview/observability/data-management/data-transformation/trace-derived-metrics" >}}).

## Why trace-derived metrics exist

Traces are detailed, high-cardinality records of individual requests. That detail is invaluable when you're investigating a specific problem, but it's the wrong shape for continuous monitoring: you can't practically write an alert that watches every trace, and Tempo isn't a time-series database that alerting engines can evaluate against.

Tempo's metrics-generator bridges that gap. It watches the stream of spans and continuously aggregates them into standard Prometheus time series. The result is that the same request flows you explore trace-by-trace also show up as ordinary metrics you can chart, aggregate, and alert on with the PromQL tooling you already use, without instrumenting your applications to emit those metrics themselves.

## RED metrics

The metrics-generator organizes what it produces around the **RED** method, which describes service health with three signals:

- **Rate**: how many requests a service or operation is handling per second. Rate tells you about traffic and load.
- **Errors**: what proportion of those requests are failing. The error signal is usually the first thing you alert on, because it maps directly to user-visible breakage.
- **Duration**: how long requests take, expressed as latency percentiles rather than averages so that tail latency stays visible.

Together these three answer "is the service up, is it healthy, and is it fast?" for every service and operation, derived automatically from trace data. Because RED metrics are consistent across services, they give you a uniform way to compare and dashboard very different components.

## What monitoring patterns they enable

Because trace-derived metrics carry service, operation, and dependency dimensions, they support monitoring patterns that plain application metrics often can't:

- **Service-level monitoring**: track overall health of each service using its RED signals.
- **Dependency monitoring**: because service graph metrics record client/server pairs, you can see when an upstream service's degradation is what's hurting a downstream one.
- **Capacity planning**: watch request-rate and latency trends over time to anticipate scaling needs.
- **Quality monitoring**: track gradual degradation in error rate or latency before it becomes an outage.

These patterns are the reason the metrics exist: they turn the rich-but-unqueryable detail of traces into signals you can watch continuously and act on.

## See also

- [Trace-derived metrics reference]({{< relref "/overview/observability/data-management/data-transformation/trace-derived-metrics" >}}): the metric catalog and query patterns
- [Alert on trace-derived metrics]({{< relref "/overview/observability/data-management/data-transformation/alert-on-trace-derived-metrics" >}}): turn these signals into alerts
- [Service graphs]({{< relref "/overview/observability/data-management/data-exploration/service-graphs/" >}}): the visual topology behind service graph metrics
