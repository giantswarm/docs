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

If you're looking to ingest custom metrics or logs for your dashboards, start with our [Data Ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion" >}}) to collect the data you want to visualize.

## Creating your own dashboard

You can create a dashboard either with our recommended GitOps approach, or through the Grafana UI. Following you can learn more about both ways.

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

__warning__: the `observability.giantswarm.io/organization` annotation's value must be equal to an existing GrafanaOrganization CR's display name. For more information on Grafana organizations, check [our documentation on multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}). Also, the dashboard's JSON must contain a unique `UID` in a given organization otherwise it won't be provisioned.

This is the preferred approach as it allows shared dashboards across all installations (if you have multiple ones) and comes with a linting job in the CI pipeline to ensure the dashboard is valid.

### Grafana UI

You can also create your dashboards directly through the Grafana UI. You can learn more about [how to create a dashboard](https://grafana.com/docs/grafana/latest/dashboards/build-dashboards/create-dashboard/) through Grafana in the official documentation.

The Observability Platforms Grafana stores its data in a [PostgreSQL](https://www.postgresql.org/) database which creates backups hourly so we can recover the state of Grafana in case of a disaster.
