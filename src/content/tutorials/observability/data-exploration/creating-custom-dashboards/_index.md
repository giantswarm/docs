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

There are two possible ways to create your own dashboard:

### GitOps

You can create a `configmap` resource in the management cluster in any namespace you want containing the dashboard. For example:

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

__warning__: the `observability.giantswarm.io/organization` annotation's value must be equal to an existing GrafanaOrganization CR's display name. For more information on Grafana organizations, check the [related page](https://docs.giantswarm.io/tutorials/observability/multi-tenancy/creating-grafana-organization/). Also, the dashboard's JSON must contain a unique `uid` and name (for a given organization) otherwise it won't be provisioned.

This is the preferred approach as it allows shared dashboards across all installations (if you have multiple ones) and comes with a linting job in the CI pipeline to ensure the dashboard is valid.

### Grafana UI

You can also create your dashboards directly through the Grafana UI. Grafana data is stored in a Postgresql database which is backed up hourly so we can recover the state of Grafana in case of a disaster.
