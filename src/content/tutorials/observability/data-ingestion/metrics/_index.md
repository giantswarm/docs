---
title: Ingest metrics into the Observability Platform
linkTitle: Metrics
description: How to make new metrics available in the Observability Platform in self-service.
menu:
  principal:
    parent: tutorials-observability-data-ingestion
    identifier: tutorials-observability-data-ingestion-metrics
weight: 50
last_review_date: 2024-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is a ServiceMonitor?
  - What is a PodMonitor?
  - How to ingest new metrics?
  - Why do my clusters run the Prometheus Operator?
---

By default, all Giant Swarm clusters are equiped with [Prometheus Operator](https://prometheus-operator.dev/) and a set of [Alloy](https://grafana.com/oss/alloy-opentelemetry-collector/) monitoring agents. They are used that collect and forward critical cluster and workload metrics to a central [Grafana Mimir](https://grafana.com/oss/mimir/) instance running on the management cluster.

No workload is the same, especially in the way it exposes its metrics, so the Observability Platform's monitoring configuration needs to be flexible. That's why it's based on the ServiceMonitor and PodMonitor Custom Resource Definitions (CRD) provided by the Prometheus Operator.

Those allow you to:

- Define where the metrics you want to ingest are (for example the container or port)
- Transform metrics before ingesting them (for example dropping unneeded data, adding extra labels)

You can learn more about the ServiceMonitor and PodMonitor CRD by checking the [Prometheus Operator API Docs](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md).

## Prerequisites

Before you start to ingest data from a running container, you need to make sure that your application is already [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to export metrics.

Keep in mind that ingesting new metrics into the Observability Platform comes with a cost. The resource consumption of the central Mimir is related to the amount of metrics it has to handle. This means ingesting more metrics also leads to higher resource consumption of the Observability Platform overall.

You can check the resource usage related to your ServiceMonitor and PodMonitor in the _ServiceMonitors Overview_ dashboard in your installation's Grafana.

## Creating a ServiceMonitor

Here is an example showing how to create a [ServiceMonitor](https://github.com/prometheus-community/helm-charts/blob/main/charts/kube-prometheus-stack/charts/crds/crds/crd-servicemonitors.yaml).

This one targets a service named `my-service` in the `monitoring` namespace, and will route alerts to the `my-tenant` tenant in Mimir. The manifests should be similar with any workload as long as you have a service that exposes the app's metrics.

The bare minimum for a ServiceMonitor looks like this:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    ## This label is important as it is required for the metrics agent to discover it.
    ## The tenant name should be the name of your internal team.
    observability.giantswarm.io/tenant: my-tenant
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

No matter if you are using Helm Charts or GitOps and Kustomize, just put the ServiceMonitor CR next to your app and apply it in the same way. Once it's applied you can check either the _ServiceMonitors Overview_ or _ServiceMonitors Details_ dashboards, or just search for the new metrics ingested in your installation's Grafana to make sure that your containers are being scraped by the new monitoring agents.

__Warning:__ The ServiceMonitor needs to be labeled with `observability.giantswarm.io/tenant: <YOUR-TENANT-NAME>` for the metrics agent to be able to discover it and start collecting metrics. Also, please make sure that the tenant you're setting with the label does actually exist in one of the [Grafana organization CRs](https://docs.giantswarm.io/tutorials/observability/multi-tenancy/creating-grafana-organization/).

If you also want to collect logs in a similar manner, you can use [PodLogs](https://docs.giantswarm.io/tutorials/observability/data-ingestion/logs/#using-podlogs) which are the equivalent resource for log ingestion.

## ServiceMonitor vs. PodMonitor

In most cases, a ServiceMonitor should cover most of your monitoring use cases but it can happen on rare occasions that a container doesn't need a service to run and it doesn't make sense to create one just for the sake of monitoring it. That's when the PodMonitor comes into action. You can find a few other examples where PodMonitor makes sense [in this discussion](https://github.com/prometheus-operator/prometheus-operator/issues/3119) in the Prometheus Operator Project.

## Deprecated team label

As we now support multi-tenancy for metrics, you __need__ to attribute a tenant name to your servicemonitors and podmonitors to have those routed to the adequate tenant. This means that you will have to replace the `application.giantswarm.io/team: <YOUR-TEAM-NAME>` label by the `observability.giantswarm.io/tenant: <YOUR-TENANT-NAME>` one.

For now, servicemonitors and podmonitors that only have the `application.giantswarm.io/team` label are routed to the "Giant Swarm" tenant by default.