---
linkTitle: Observability
title: Developer Platform Observability Features
description: Overview of the observability related platform features to help you operate and improve your platform and applications.
weight: 30
menu:
  main:
    parent: developer-platform
    identifier: developer-platform-observability
aliases:
  - /app-platform/apps/observability/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What app do you recommend for monitoring?
  - What app do you recommend for logging?
  - What app do you recommend for tracing?
last_review_date: 2022-11-18

Observability is based on three main data sources: logs, metrics and tracing\*. To cover these needs Giant Swarm provides its customers with a managed observability stack. The apps included in this stack are listed below. We chose these apps based on our general principles of preferring open source over proprietary solutions, as well as simplicity, performance, and speed over complexity.

**What do we mean by a "managed" app?** We mean offering similar Service Level Objectives as the rest of our offering as described in [The Radical Way Giant Swarm Handles Service Level Objectives](https://www.giantswarm.io/blog/the-radical-way-giant-swarm-handles-service-level-objectives).

In brief, super fast response times from engineers, 24//7 monitoring and alerting by us, and in general, having shared goals and responsibilities to keep services up and get them up when they go down.

In addition, we strive to uphold our "30 Day Upgrade Promise," our commitment to keep all managed apps within 30 days of latest upstream releases.

To summarize, for observability, we recommend and provide these four managed apps:

## Prometheus for monitoring/metrics

To get all your metrics, process, store and alert on them. Prometheus has become the de-facto standard monitoring tool in the kubernetes ecosystem.

## Loki for logging

To fetch logs from containers, store and index them, and make them searchable. To install, go to [Loki README](https://github.com/giantswarm/loki-app/blob/master/README.md).

In addition, we understand some customers already know and use Elasticsearch. For this reason, we also provide a managed EFK stack (Elasticsearch, Fluentd, and Kibana) for logging. To install, go to [EFK Stack README](https://github.com/giantswarm/efk-stack-app/blob/master/README.md) [Elastic Stack]({{< relref "/developer-platform/observability/elastic-stack" >}}).

## Grafana as data visualization tool

To analyze, visualize, and correlate metrics from Prometheus and Linkerd as well as logs from Loki.

These pieces can be separately or together. Adopting them together and as fully managed apps from Giant Swarm gives you the benefit of using vetted open source tools that you know work together to provide you with consistency and coverage.

We are currently not offering a fully managed app for tracing due to the low priority it has with our customers. We believe that at this time the [tracing options provided by Linkerd](https://www.giantswarm.io/blog/part-5-traces-of-your-microservices-0) (that require no code changes) are sufficient.
