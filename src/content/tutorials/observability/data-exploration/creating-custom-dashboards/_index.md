---
linkTitle: Creating custom Grafana dashboards
title: Creating custom Grafana dashboards
description: Guide explaining how to manage custom Grafana dashboards in the Observability Platform.
menu:
  main:
    identifier: tutorials-observability-data-exploration-create-custom-dashboards
    parent: tutorials-observability-data-exploration-create-observability-visualization
weight: 40
aliases:
  - /advanced/observability/visualization/custom-dashboards
  - /observability/grafana/custom-dashboards
  - /observability/visualization/custom-dashboards
  - /ui-api/observability/grafana/custom-dashboards
  - /ui-api/observability/visualization/custom-dashboards
last_review_date: 2024-07-17
user_questions:
  - How to customize dashboards?
  - How to create my own dashboards?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

As explained in our guide explaining [how to access Grafana]({{< relref "../accessing-grafana" >}}), we provide a subset of dashboards accessible by our customers.

Sometimes, the dashboards we provide aren't enough for your use case so we offer you the capability of creating your own (for example, you are deploying your own apps on the management cluster, or you want custom dashboards for your clusters).

## Creating your own dashboard

To create your own dashboard, you can create a `configmap` resource in the management cluster in any namespace you want (preferably the one you use for automation) containing the dashboard. For example:

```yaml
apiVersion: v1
data:
  my-dashboard.json: |-
    { ... my dashboard in json format }
kind: ConfigMap
metadata:
  annotations:
    ## Define the directory in grafana where the dashboard will be added to the grafana container
    k8s-sidecar-target-directory: /var/lib/grafana/dashboards/customer
  labels:
    ## Tell grafana to load this configmap as a dashboard
    app.giantswarm.io/kind: dashboard
  name: my-grafana-dashboard
  namespace: my-namespace
```

### Limitations

__Beware__ that the dashboard name must be unique so don't override one of your own.

## How's this feature implemented

We install Grafana through [our fork](https://github.com/giantswarm/grafana-app) of the [upstream Grafana helm chart](https://github.com/grafana/helm-charts/tree/main/charts/grafana)

The chart supports the use of [sidecar containers](https://github.com/grafana/helm-charts/blob/dcc1c7d1b830259c4d208fcddb6fd8ec7e56682f/charts/grafana/values.yaml#L740) to load dashboards, data sources, plugins and notifiers dynamically.

We're using this feature internally to deploy our dashboards alongside the applications we use.
