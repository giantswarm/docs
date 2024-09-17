---
title: Observe your clusters and apps
description: Check cluster and app metrics and logs with the observability tools provided with the Giant Swarm platform.
weight: 70
last_review_date: 2024-09-25
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I observe the platform metrics and logs for my application?
  - What do I need to do to observe the platform metrics and logs for my application?
---


<Explanation how monitoring works in two paragraphs>

## Requirements

First of all, you need a running workload cluster. If you don't have one, please first [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}). Second, you need to deploy the hello-world application explained [here]({{< relref "/getting-started/install-an-application" >}}).

In case you are running your own application, you need to make sure that your application is already [instrumented](https://opentelemetry.io/docs/concepts/instrumentation/) to export metrics.

Also consider that ingesting new metrics into the platform impacts your costs. The resource consumption of the central monitoring system is related to the amount of metrics it has to handle, so choose wisely which metrics you want to ingest.

## Step 1: Create a service monitor

<Adapt service monitor to hello world and add it to the repo as optional feature>

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  labels:
    ## This label is important as it is required for the Prometheus Agent to discover it.
    ## The team name should be the name of your internal team.
    application.giantswarm.io/team: my-team
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

## Step 2: Check the built-in dashboard

<screenshot of dashboard with some explanations>

## Next step

After knowing how your application behaves let's explore what is the [security baseline and how does it affect your workload]({{< relref "/vintage/getting-started/secure-your-app" >}}).
