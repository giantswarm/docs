---
linkTitle: Observability
title: Observability Features
description: Overview of the observability related platform features to help you operate and improve your platform and applications.
weight: 70
menu:
  main:
    parent: platform-overview
    identifier: platform-overview-observability
aliases:
  - /platform-overview/observability
  - /developer-platform/observability/
  - /app-platform/apps/observability/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What app do you recommend for monitoring?
  - What app do you recommend for logging?
  - What app do you recommend for tracing?
last_review_date: 2024-02-28
---

Observability is based on four main data sources: __logs__, __metrics__, __traces__ and __profiles__. To cover these needs, Giant Swarm provides its customers with a fully managed observability platform supported by 24//7 monitoring and alerting The tools included in the observabily platform are listed below.

We chose these applications based on our general principles of preferring open source over proprietary solutions, as well as simplicity, performance, and speed over complexity.

If you want to learn more about observability, we recommend that you read [this](https://opentelemetry.io/docs/concepts/observability-primer/)

To summarize, for observability, we recommend and provide these tools:

## Loki for logging

To store, index and make logs (containers, kubernetes events, audit logs) searchable. You can also install our [Loki App](https://github.com/giantswarm/loki-app/blob/master/README.md) on your clusters.

## Prometheus for monitoring

To get all your metrics, process, store and alert on them. Prometheus has become the de-facto standard monitoring tool in the kubernetes ecosystem.

## Grafana for data visualization

To analyze, visualize, and correlate any kind of observability data.

## Tempo for distributed tracing

We are currently offering Grafana Tempo a part of our observability platform on demand and without any availability garantees due to the low priority it has with our customers.

## Pyroscope for continuous profiling

Profiling is quite a new kid on the block when it comes to observability.
Same as with Grafana Tempo, we are currently offering Grafana Tempo a part of our observability platform on demand and without any availability garantees due to the low priority it has with our customers.

---

If you want to learn more about our monitoring platform, feel free to dive into our [`Getting Started`]({{< relref "/vintage/getting-started/observability" >}}) section.
