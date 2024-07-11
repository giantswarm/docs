---
title: Ingest metrics into the Observability Platform
linkTitle: Metrics
description: How to make new metrics available in the Observability Platform in self-service
menu:
  principal:
    parent: tutorials-observability-data-ingestion
    identifier: tutorials-observability-data-ingestion-metrics
weight: 50
last_review_date: 2024-07-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is a ServiceMonitor?
  - What is a PodMonitor?
  - How do I ingest new metrics?
  - Why do my clusters run the Prometheus Operator?
---

By default, all Giant Swarm clusters are equiped with the [Prometheus Operator](https://prometheus-operator.dev/) and a set of multiple [Prometheus](https://prometheus.io/) shards in `agent mode` functioning as monitoring agents to be able to collect and forward cluster critical and workload metrics to a central [Grafana Mimir](https://grafana.com/oss/mimir/) instance running on the management cluster.

No workload is the same, especially in the way it exposes its metrics, so the Observability Platforms monitoring configuration needs to be flexible. That's why it is based on the `ServiceMonitor` and `PodMonitor` Custom Resource Definitions (CRDs) provided by the Prometheus Operator. 

Those allow you to:

- Define where the metrics you want to ingest are (for example the container or port)
- transform metrics before ingesting them (e.g. dropping unneeded data, adding extra labels)

If you want to read more about the CRDs, feel free to look at their [API](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api.md).

## Prerequisites

Before you start to ingest data from a container running in your clusters, you need to make sure that your application is already [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to export metrics and make sure the metrics it provides are useful to you.

## Creating a ServiceMonitor

Here is an example showing how to create a [ServiceMonitor](https://github.com/helm/charts/blob/master/stable/prometheus-operator/crds/crd-servicemonitor.yaml) that targets an existing service named `my-service` in the `monitoring` namespace, but the manifests should be similar with any workload as long as you deploy a service.

The bare minimum for a ServiceMonitor looks like this:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    ## This label is important as it is required for the Prometheus Agent to discover it.
    ## The team name should be the name of your internal team.
    application.giantswarm.io/team: team-name
    app.kubernetes.io/instance: my-service
  name: my-service
  namespace: monitoring
spec:
  endpoints:
  - interval: 60s   # Scrape the target every 60s
    path: /metrics  # Path that exposes the metrics
    port: web       # Named port on the service that exposes the metrics
    relabelings: [] # Any potential metric transformation that you want to apply to your metrics.
  selector:         # Label selector that matches your service
    matchLabels:
      app.kubernetes.io/instance: my-service
```

__Warning:__ The ServiceMonitor needs to be labeled with `application.giantswarm.io/team: team-name` for the Prometheus Agent to be able to discover it and start collecting metrics.

To make sure that your containers are being scraped by the monitoring agents, we can only advise you to access your management cluster Grafana and access either the `ServiceMonitors Overview` or `ServiceMonitors Details` dashboards.

## When should I use a PodMonitor?

In most cases, a ServiceMonitor should cover most of your monitoring use cases but it can happen on rare occasions that a container doesn't need a service to run and it doesn't make sense to create one just for the sake of monitoring it. That's when the PodMonitor come into action. You can find a few other examples where PodMonitor makes sense [upstream](https://github.com/prometheus-operator/prometheus-operator/issues/3119).
