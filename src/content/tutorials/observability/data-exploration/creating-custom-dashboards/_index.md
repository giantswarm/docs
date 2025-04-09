---
linkTitle: Custom dashboards
title: Creating custom Grafana dashboards
description: Guide explaining how to manage custom Grafana dashboards in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-data-exploration-create-custom-dashboards
    parent: tutorials-observability-data-exploration
weight: 40
last_review_date: 2025-04-07
user_questions:
  - How to customize dashboards?
  - How to create my own dashboards?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

You can find in [your installations Grafana]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}) a set of out-of-the-box [dashboards provided by Giant Swarm](https://github.com/giantswarm/dashboards). However these default dashboards might not satisfy your specific observability requirements or your apps or clusters unique context. This is why the Observability Platform allows you to create your own dashboards in self-service.

## Creating your own dashboard

There are two possible ways to create your own dashboard :

- You can create a `configmap` resource in the management cluster in any namespace you want containing the dashboard. For example:

```yaml
apiVersion: v1
data:
  my-dashboard.json: |-
    { ... my dashboard in JSON format }
kind: ConfigMap
metadata:
  annotations:
    ## Define the organization in Grafana where the dashboard will be added
    observability.giantswarm.io/organization: Customer
  labels:
    ## Tell Grafana to load this configmap as a dashboard
    app.giantswarm.io/kind: dashboard
  name: my-grafana-dashboard
  namespace: my-namespace
```

- You can directly use the Grafana UI and save it there. As we are operating a database for Grafana, dashboards created and saved directly from the UI will be accessible even in case of disaster as long as a backup has been made after the dashboard creation and before the said disaster.

### Limitations

- the dashboard's JSON must contain an `uid` otherwise it won't be provisioned.
- the dashboard name and UID must be unique in each Grafana organization.
