---
linkTitle: Configuring alerting
title: How to configure alerting
description: Guide explaining how to configure alerting in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-alerting-configuration
    parent: tutorials-observability-alerting
weight: 40
last_review_date: 2025-04-24
user_questions:
  - How to configure Alertmanager?
  - How to visualize the existing alerting configuration?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

The Giant Swarm Observability Platform provides an [alerting pipeline]({{< relref "/overview/observability/alerting/" >}}) that you can configure per tenant.

## Configure Alertmanager

The Observability Platform uses Mimir Alertmanager as the central tool to provide its alerting capabilities.

Once you have configured your list of tenants, you can easily create an Alertmanager configuration for that tenant by creating the following secret on your management cluster.

Here is an example
```yaml
apiVersion: v1
kind: Secret
metadata:
  labels:
    # This marks this secret as an Alertmanager configuration
    observability.giantswarm.io/kind: alertmanager-config
    # V
    observability.giantswarm.io/tenant: my-team
  name: my-alertmanager-config
  namespace: default
data:
  # This is mandatory and contains the actual Alertmanager configuration.
  alertmanager.yaml: |
    route:
      receiver: "example_receiver"
      group_by: ["example_groupby"]
    receivers:
      - name: "example_receiver"
    templates:
      - example_template.tmpl
  # The secret can also contain any number of [reusable template files](https://prometheus.io/docs/alerting/latest/notification_examples/#defining-reusable-templates) that must be in the form `filename.tmpl`. Any other entry will be ignored.
  example_template.tmpl: |
    {{ define "alert_customer_env_message" }}
    [{{ .CommonLabels.alertname }} | {{ .CommonLabels.customer }} | {{ .CommonLabels.environment }}]
    {{ end }}
type: Opaque
```

When configuring Alertmanager for your tenant, please ensure that the defined configuration under `alertmanager.yaml` is valid or it will be rejected by a validating webhook. To that end, we advise you to use [`mimirtool`](https://grafana.com/docs/mimir/latest/manage/tools/mimirtool/#validate-alertmanager-configuration), the mimir cli too in your CI pipeline.

**Warning:** As our multi-tenancy aligns tenants across our platform on Grafana Organizations please make sure that the `observability.giantswarm.io/tenant` label references an existing tenant defined in a Grafana Organization. Any Alertmanager configuration that references an non-existing tenant will be rejected by a validating webhook. Learn more about our multi-tenancy in [Multi-tenancy in the observability platform]({{< relref "/tutorials/observability/multi-tenancy/" >}})

If you want to see your configured alertmanager pipeline, you should definitely check out our guides explaining [how to visualize your alerting pipeline in Grafana]({{< relref "/tutorials/observability/alerting/visualization" >}}). More information in the [access `Grafana` page]({{< relref "/tutorials/observability/data-exploration/accessing-grafana/" >}})
