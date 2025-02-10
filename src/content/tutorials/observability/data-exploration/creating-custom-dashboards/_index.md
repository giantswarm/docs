---
linkTitle: Custom dashboards
title: Creating custom Grafana dashboards
description: Guide explaining how to manage custom Grafana dashboards in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-data-exploration-create-custom-dashboards
    parent: tutorials-observability-data-exploration
weight: 40
last_review_date: 2025-02-10
user_questions:
  - How to customize dashboards?
  - How to create my own dashboards?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

You can find in [your installations Grafana]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}) a set of out-of-the-box [dashboards provided by Giant Swarm](https://github.com/giantswarm/dashboards). However these default dashboards might not satisfy your specific observability requirements or your apps or clusters unique context. This is why the Observability Platform allows you to create your own dashboards in self-service.

## Creating your own dashboard

To create your own dashboard, you can create a `configmap` resource in the management cluster in any namespace you want containing the dashboard. For example:

```yaml
apiVersion: v1
data:
  my-dashboard.json: |-
    { ... my dashboard in json format }
kind: ConfigMap
metadata:
  annotations:
    ## Define the organization in grafana where the dashboard will be added
    observability.giantswarm.io/organization: Customer
  labels:
    ## Tell grafana to load this configmap as a dashboard
    app.giantswarm.io/kind: dashboard
  name: my-grafana-dashboard
  namespace: my-namespace
```

### Limitations

* the dashboard's json must contain an `uid` otherwise it won't be provisioned.
* the dashboard name and uid must be unique in each grafana organization.
