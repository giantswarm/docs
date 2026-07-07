---
title: Metrics monitoring concepts
linkTitle: Metrics monitoring concepts
diataxis_content_type: explanation
description: The concepts behind metrics monitoring on the Giant Swarm observability platform, including how to approach PromQL query construction, the label model, and service level indicators.
weight: 35
menu:
  principal:
    parent: overview-observability-data-management-data-exploration
    identifier: overview-observability-data-management-data-exploration-metrics-monitoring-concepts
last_review_date: 2026-07-06
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How should I approach building a PromQL query?
  - What are SLIs, SLOs, and error budgets?
  - How does Giant Swarm label its metrics?
---

This page explains the ideas that sit behind the metrics queries you write against the Giant Swarm Observability Platform. It's background reading rather than a task list: understanding these concepts helps you build queries that answer the right question and interpret the results correctly. For the queries themselves, see the [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql" >}}).

## How to approach query construction

Effective monitoring queries are rarely written in one go. A reliable way to arrive at the query you actually need is to build it up in stages rather than reaching for the final expression immediately:

1. **Define the question**: State precisely what you are measuring. For example, "what fraction of requests to the web API returned a 5xx status in the last five minutes?"
2. **Identify the metrics**: Work out which time series carry that data, and which labels distinguish the dimension you care about.
3. **Construct progressively**: Start from a bare metric selector, confirm it returns the series you expect, then layer on rate calculations, aggregations, and arithmetic one step at a time.
4. **Test and optimize**: Validate the result against something you can independently verify, then tighten label selectors and time ranges so the query stays fast.

For example, a service error-rate query grows from a plain selector, to a rate, to a ratio:

```promql
# Step 1: Basic selection
http_requests_total{service="web-api"}

# Step 2: Add rate calculation
rate(http_requests_total{service="web-api"}[5m])

# Step 3: Calculate error percentage
sum(rate(http_requests_total{service="web-api", status=~"5.."}[5m])) /
sum(rate(http_requests_total{service="web-api"}[5m])) * 100
```

Building queries this way makes each layer's contribution visible, which makes mistakes easier to spot than in a single dense expression.

## The Giant Swarm label model

Metrics collected by the platform are enriched with a consistent set of contextual labels, such as `cluster_id`, `cluster_type`, `installation`, `namespace`, and `job`, among others. These labels are what let a single query distinguish one cluster, environment, or workload from another, so choosing the right label selectors is usually more important than the metric name itself.

Because every series carries this context, you can start broad and narrow down: a query written against all workload clusters can be scoped to a single namespace simply by adding a label matcher, without changing its structure. For the full list of labels and how to combine them in selectors, see the [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql#giant-swarm-label-structure" >}}).

## Service level indicators, objectives, and error budgets

Service Level Indicators (SLIs) provide objective, measurable definitions of service quality that correlate directly with user experience. A well-chosen SLI takes a user-facing question such as "were requests served successfully?" or "were they served quickly enough?" and expresses it as a number you can track over time.

- An **SLI** is the measurement itself, usually expressed as a ratio of good events to total events (for example, the fraction of non-5xx responses).
- An **SLO** (Service Level Objective) is the target you hold that SLI to over a window, such as 99.9% availability over 30 days.
- An **error budget** is the complement of the SLO, meaning the small fraction of failures you can tolerate before breaching the objective. Tracking how fast you consume that budget turns reliability into a quantity you can manage rather than a vague aspiration.

These definitions are what make reliability decisions data-driven: instead of debating whether a service is "healthy," you compare its SLI against its SLO and see how much error budget remains. The [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql#service-level-and-reliability-queries" >}}) shows how to express availability SLIs, latency SLIs, and error-budget consumption as concrete queries.

## See also

- [PromQL query reference]({{< relref "/overview/observability/data-management/data-exploration/promql" >}}): the query catalog these concepts underpin
- [Alerting rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}): turn SLIs into alerts and recording rules
- [Data exploration]({{< relref "/overview/observability/data-management/data-exploration" >}}): access Grafana and start querying
