---
title: Observability
description: The observability platform provides you with visibility into the Giant Swarm platform, your cluster fleet, and application workloads.
weight: 70
menu:
  principal:
    parent: overview
    identifier: overview-observability
last_review_date: 2024-12-11
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

# What is observability?

Observability is all about understanding what's happening in your systems—so you can keep things running smoothly, spot issues early, and make smart improvements. At Giant Swarm, we make observability a priority. Our platform gives you the tools to see what's going on in your clusters and applications, fix problems fast, and keep everything healthy. You'll get everything you need for data exploration, visualization, and alerting, all in a self-service way. Plus, we provide proven defaults to help you get started quickly and confidently.

## What you can do with Giant Swarm observability

- **Monitor your systems:** Continuously collect and analyze metrics to check the performance and health of your applications and infrastructure. Effective monitoring helps you spot anomalies, understand usage patterns, and make data-driven decisions.

- **Centralize your logs:** Capture detailed records of system and application events. Centralized logging makes troubleshooting and auditing easier. Search and analyze logs to find issues, track changes, and meet compliance needs—all in one place.

- **Visualize your data:** Connect the dots between different data sources. Use dashboards, visualizations, and alerts to get a clear picture of your platform. Start with our ready-made dashboards or create your own to track what matters most to you.

- **Get notified with alerts:** Don’t spend your day staring at dashboards. Set up alerting rules to get notified about important events or issues that need your attention. Our alerting features help your team avoid repetitive checks and focus on what matters.

- **Work securely with multi-tenancy:** Keep sensitive data safe by isolating it for the right teams, departments, or organizational structures. Our multi-tenant solution ensures only the right people have access to the right data.

One of the biggest benefits of using Giant Swarm is that you get the same reliable, integrated observability tools our own teams use every day. This gives you a comprehensive view of your applications and infrastructure, right out of the box.

## The technology behind our platform

- **Mimir:** An open-source, horizontally scalable, highly available, multi-tenant time series database for long-term metric storage. Mimir is at the core of our metrics system. It integrates with Kubernetes, collects and stores metrics as time series data, and enables powerful querying and alerting.

- **Loki:** An open-source, horizontally scalable, highly available log aggregation system. Loki collects logs from any source and in any format, covering everything from app and system events to audit logs. With LogQL, you can query logs and even generate metrics from log data.

- **Grafana:** A popular open-source visualization tool for exploring metrics and logs. Grafana lets you create dashboards and graphs for all your observability needs. It integrates seamlessly with Mimir and Loki, and supports other data sources like Prometheus, Elasticsearch, and InfluxDB.

- **Alertmanager:** Part of the Grafana ecosystem, Alertmanager handles all your alerts. It manages routing, grouping, and silencing, so the right people get notified at the right time. It supports notifications via email, Slack, PagerDuty, and more.

- **Alloy:** As an OpenTelemetry collector, Grafana Alloy makes it easy to collect, process, and forward metrics, logs, and events from your workload clusters. Adding new data is as simple as setting up a new service monitor or adding the right labels.

---

Ready to get started? Check out our [getting started observability page]({{< relref "getting-started/observe-your-clusters-and-apps/" >}}) to begin your journey.
