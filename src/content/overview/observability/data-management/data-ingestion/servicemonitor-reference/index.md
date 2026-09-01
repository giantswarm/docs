---
title: ServiceMonitor and PodMonitor reference
linkTitle: ServiceMonitor and PodMonitor reference
diataxis_content_type: reference
description: Reference for the Prometheus ServiceMonitor and PodMonitor resources used to collect metrics on the Giant Swarm observability platform, including the required tenant label and their key fields.
weight: 40
menu:
  principal:
    parent: overview-observability-data-management-data-ingestion
    identifier: overview-observability-data-management-data-ingestion-servicemonitor-reference
last_review_date: 2026-07-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - Which labels must a ServiceMonitor or PodMonitor have to be discovered?
  - Which ServiceMonitor fields does the metrics agent use?
  - Which PodMonitor fields does the metrics agent use?
  - When should I use a PodMonitor instead of a ServiceMonitor?
---

This page describes the [Prometheus Operator](https://github.com/prometheus-operator/prometheus-operator) `ServiceMonitor` and `PodMonitor` custom resources as used to collect metrics on the Giant Swarm Observability Platform. The metrics agent on each cluster discovers these resources and scrapes the targets they select.

For the task-oriented steps to set up metrics collection, see the [data ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion" >}}). For the complete upstream schema, see the [Prometheus Operator API documentation](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md).

## Discovery requirements

For a `ServiceMonitor` or `PodMonitor` to be picked up by the platform:

- **Tenant label**: the resource must carry the `observability.giantswarm.io/tenant` label. It routes the collected metrics to that [tenant]({{< relref "/overview/observability/configuration/multi-tenancy" >}}).
- **Tenant existence**: the named tenant must already exist in a [Grafana Organization]({{< relref "/overview/observability/configuration/creating-grafana-organization" >}}). Metrics routed to a non-existent tenant are dropped.

## ServiceMonitor

A [`ServiceMonitor`](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#monitoring.coreos.com/v1.ServiceMonitor) collects metrics from applications that expose them through a Kubernetes Service. It's the primary way to configure metric collection.

| Field | Description |
|-------|-------------|
| `metadata.labels."observability.giantswarm.io/tenant"` | Required. The tenant the collected metrics are routed to (see [discovery requirements](#discovery-requirements)). |
| `spec.selector.matchLabels` | Selects the Services to scrape by their labels. |
| `spec.endpoints[].port` | Named Service port that exposes metrics. |
| `spec.endpoints[].path` | HTTP path that exposes metrics. Defaults to `/metrics`. |
| `spec.endpoints[].interval` | Scrape interval, for example `60s`. |

## PodMonitor

A [`PodMonitor`](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#monitoring.coreos.com/v1.PodMonitor) collects metrics directly from Pods, without requiring a Service. Use a `PodMonitor` when:

- Your application doesn't need a Service for its primary function.
- You need to collect metrics from specific Pod instances.
- You want more granular control over Pod selection.

| Field | Description |
|-------|-------------|
| `metadata.labels."observability.giantswarm.io/tenant"` | Required. The tenant the collected metrics are routed to (see [discovery requirements](#discovery-requirements)). |
| `spec.selector.matchLabels` | Selects the Pods to scrape by their labels. |
| `spec.podMetricsEndpoints[].port` | Named Pod port that exposes metrics. |
| `spec.podMetricsEndpoints[].path` | HTTP path that exposes metrics. Defaults to `/metrics`. |
| `spec.podMetricsEndpoints[].interval` | Scrape interval, for example `60s`. |

## See also

- [Data ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}): how to configure metrics collection, with working ServiceMonitor and PodMonitor examples
- [Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}}): how tenants isolate observability data
