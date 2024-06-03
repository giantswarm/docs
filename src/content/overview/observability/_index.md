---
title: Observability
description: Monitoring, Logging and Tracing to provide you with visibility into the Giant Swarm platform, your cluster fleet and application workloads.
weight: 70
menu:
  principal:
    parent: overview
    identifier: overview-observability
last_review_date: 2024-06-03
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Observability is a fundamental aspect of modern cloud-native environments, providing the insights needed to understand and improve the performance, reliability, and overall health of applications and infrastructure. At Giant Swarm, we prioritize observability to ensure our customers can maintain visibility into their systems, quickly identify and resolve issues, and continuously optimize their operations.

## Capabilities

- **Monitoring**: It involves the continuous collection and analysis of metrics to assess the performance and health of applications and infrastructure. Effective monitoring across all environments allows teams to detect anomalies, understand usage patterns, and make data-driven decisions to optimize their systems.

- **Logging**: It captures detailed records of system and application events, providing crucial information for troubleshooting and auditing. Centralized logging, a powerful tool that empowers teams, enables them to search, analyze, and visualize log data, helping them identify issues, track changes, and ensure compliance with security and regulatory requirements, thereby giving them a greater sense of control over their system's health.

- **Tracing**: lets you track requests' journeys through various application services and components. It also provides a detailed view of the interactions and dependencies between services, helping to pinpoint performance bottlenecks and understand request end-to-end latency.

- **Alerting**: It is crucial to be able to notify your teams about significant events or issues that require immediate attention. By making it easy to set up and configure across apps and environments, alerting helps platform teams avoid wasting time on repetitive tasks, thereby enhancing their efficiency and allowing them to focus on what matters.

- **Profiling**: Profiling analyzes applications' resource usage and performance characteristics, identifying inefficient code paths and resource bottlenecks. A standardized approach to profiling applications helps teams optimize performance, reduce costs, and deliver a better user experience.

One of the key benefits using Giant Swarm is that we provide a set of integrated observability tools that help you have a comprehensive view of your applications and infrastructure.

## Cloud-Native technologies

**Prometheus** is a leading open-source monitoring and alerting toolkit for reliability and scalability. It collects and stores metrics as time series data, enabling powerful querying and alerting capabilities. Prometheus integrates seamlessly with Kubernetes, making it a popular choice for cloud-native environments.

- **Grafana**: Grafana is a popular open-source visualization tool for creating dashboards and graphs for monitoring and observability. It supports various data sources, including Prometheus, Elasticsearch, and InfluxDB, making it versatile for visualizing metrics and logs.

- **Fluent Bit**: It is a versatile log collector that can aggregate, process, and forward logs to various destinations. It supports multiple input and output plugins, making integrating different logging backends and systems effortless.

- **Tempo**: Tempo is an open-source tracing system for monitoring and troubleshooting microservices-based architectures. It helps visualize request flows, measure latencies, and analyze the performance of distributed systems. Tempo integrates well with Kubernetes and other cloud-native tools, providing comprehensive tracing capabilities.

- **Alertmanager**: This is part of the Prometheus ecosystem and is responsible for handling Prometheus-generated alerts. It manages the routing, grouping, and silencing of alerts, ensuring that the right people are notified at the right time. At the same time, it supports various notification methods, including email, Slack, and PagerDuty.

- **Pyroscope**: This tool provides continuous profiling capabilities for cloud-native applications. It collects and visualizes profiling data, helping teams identify performance issues and optimize resource usage. Continuous profiling ensures that applications run efficiently, reducing costs and improving performance.

Learn how to start with observability on Giant Swarm by visiting our [getting started observability page]({{< relref "getting-started/observe-your-clusters-and-apps/" >}}).
