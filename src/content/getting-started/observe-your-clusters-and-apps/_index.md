---
title: Observe your clusters and apps
description: Check cluster and app metrics and logs with the observability tools provided with the Giant Swarm platform.
weight: 70
last_review_date: 2024-09-27
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I observe the platform metrics and logs for my application?
  - What do I need to do to observe the platform metrics and logs for my application?
---

In the Giant Swarm platform every cluster benefits from automatic monitoring by default. It enables you to observe your application with little effort. An in-cluster agent scrapes the metrics and sends them to a central location on the management cluster, where you can interact with them through our managed Grafana instance.

Learn how to observe your application metrics and logs with the observability tools provided with the Giant Swarm platform.

## Requirements

First step, you need a running workload cluster. If you don't have one, please first [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}). Second, you need to deploy the `hello-world` application explained [in previous entry]({{< relref "/getting-started/install-an-application" >}}).

In case you are running your own application, you need to make sure that your application is already [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to export metrics.

Also, consider that ingesting new metrics into the platform impacts your costs. The central monitoring system's resource consumption is actually related to the number of metrics it has to handle, so please choose which metrics you want to ingest carefully.

## Step 1: Create a service monitor

In case of running the `hello-world` application, there is a baked-in service monitor that scrapes the metrics from the application. You can enable it by setting `serviceMonitor.enabled` to `true` in the values of the helm chart. If you are running your own application, you need to create a service monitor that scrapes the metrics from your application. This is an example of a service monitor you can use:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    application.giantswarm.io/team: team-rocket
    app.kubernetes.io/instance: my-service
  name: my-service
  namespace: my-namespace
spec:
  endpoints:
  - interval: 60s
    path: /metrics
    port: web
  selector:
    matchLabels:
      app.kubernetes.io/instance: my-service
```

An important bit to notice is the `application.giantswarm.io/team` label. This label is necessary as it is required for the Prometheus agent to discover the target. The team name is a unique identifier for your tenant or team.

Reading the manifest the application will be scraped every 60 seconds. It will read the metrics from the `/metrics` endpoint using the [port name](https://kubernetes.io/docs/concepts/services-networking/service/#field-spec-ports) as a regular service does. Also, the `app.kubernetes.io/instance` label is used to identify the application and should match application label.

After applying the service monitor, you can open the `Explore` view in the Grafana dashboard and start querying the metrics from your application.

![Explore application metrics](explore-application-metrics.png)

## Step 2: Check the built-in dashboard

To make it easier to visualize the metrics of your application, lets create a dashboard in Grafana. One logged into the [platform API]() you can create a ConfigMap with the dashboard in JSON format. It will look like this:

```yaml
apiVersion: v1
data:
  my-dashboard.json: |-
    __DASHBOARD_JSON__
kind: ConfigMap
metadata:
  annotations:
    k8s-sidecar-target-directory: /var/lib/grafana/dashboards/giant-swarm-public-dashboards
  labels:
    app.giantswarm.io/kind: dashboard
  name: my-grafana-dashboard
  namespace: my-namespace
```

It is important to have an annotation with the key `k8s-sidecar-target-directory` pointing to the location where the dashboard will be stored in the Grafana UI. Also notice the label `app.giantswarm.io/kind` has to be set to `dashboard` in order to be recognized by the platform.

## Step 3: Check the logs

## Next step

After knowing how your application behaves let's explore what is the [security baseline and how does it affect your workload]({{< relref "/vintage/getting-started/secure-your-app" >}}).
