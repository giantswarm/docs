---
title: Observability
description: The Observability Platform provides you with visibility into the Giant Swarm platform, your cluster fleet and application workloads.
weight: 70
menu:
  principal:
    parent: overview
    identifier: overview-observability
last_review_date: 2024-06-06
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Observability is a fundamental aspect of modern cloud-native environments, providing the insights needed to understand and improve the performance, reliability, and overall health of applications and infrastructure. At Giant Swarm, we prioritize observability to ensure our customers can maintain visibility into their systems, quickly identify and resolve issues, and continuously optimize their operations. With our Observability Platform we aim to empower you to fulfill all of your observability needs from Data Exploration, over Visualisation to Alerting in a self-service fashion, while providing you useful and battle-proven out-of-the-box defaults.

## Capabilities

- **Monitoring**: The heart of our Observability Platform is the continuous collection and analysis of metrics to assess the performance and health of applications and infrastructure. Effective monitoring across all environments allows teams to detect anomalies, understand usage patterns, and make data-driven decisions to optimize their systems.

- **Logging**: Our Observability Platform also captures detailed records of system and application events, providing crucial information for troubleshooting and auditing. Centralized logging, a powerful tool that empowers teams, enables them to search and analyze log data, helping them identify issues, track changes, and ensure compliance with security and regulatory requirements, thereby giving them a greater sense of control over their system's health.

- **Visualisation**: At Giant Swarm we believe that the real power of observability comes from not only exploring isolated data but also "connecting the dots" - we aim to provide you not just with data, but knowledge. For this our Observability Platform offers a wide range of visualisations and dashboards for metrics and logs and enables you to create and add your own dashboards to empower your teams to learn the insights they need to know to run their systems and apps efficiently in just a glance. 

- **Alerting**: To not just look at dashboards all day it is crucial to be able to get notified about significant events or issues that require immediate attention. By making it easy to set up and configure alerting rules across apps and environments, our Observability Platforms alerting helps your teams avoid wasting time on repetitive tasks, thereby enhancing their efficiency and allowing them to focus on what matters.

One of the key benefits using Giant Swarm is that we provide a set of battle-tested and highly integrated observability tools that our own teams already use on a daily basis and will help you have a comprehensive view of your applications and infrastructure. 

## Cloud-Native technologies

- **Mimir** is an open source, horizontally scalable, highly available, multi-tenant time series database for long-term storage for metrics and serves as central core component for storing and analyzing metrics on all our managed clusters. Think of it as Prometheus on Steroids. Like Prometheus it integrates seamlessly with Kubernetes and collects, but also stores metrics for a longer period of time as time series data, enabling powerful querying and alerting capabilities.

- **Loki** is an open source, horizontally scalable, highly available, multi-tenant log aggregation system inspired by Prometheus. It is designed to be very efficient and cost effective and integrates all sorts of logs in any format from any source, covering everything from app and system events to audit logs. With LogQL Loki also offers an easy Query Language simplifying querying logs. Additionally the language facilitates the generation of metrics from log data, a powerful feature that goes well beyond log aggregation.

- **Grafana** is a popular open-source visualization tool for exploring metrics and logs and creating dashboards and graphs for all observability needs. It perfectly integrates Mimir and Loki but also supports various other data sources, including Prometheus, Elasticsearch, InfluxDB, and others, making it versatile for visualizing all observability data in just one single place. 

- **Alertmanager** is part of the Grafana ecosystem and is responsible for handling all alerts. It manages the routing, grouping, and silencing of alerts, ensuring that the right people are notified at the right time. At the same time, it supports various notification methods, including email, Slack, and PagerDuty.

- **Various Agents** like Grafana-Agent, Fluent-bit and others help the Observability Platform collect and integrate relevant data from Workload Clusters, making the process to add new data as simple as just setting up a new service monitor or add the right labels.

Learn how to start with observability on Giant Swarm by visiting our [getting started observability page]({{< relref "getting-started/observe-your-clusters-and-apps/" >}}).
