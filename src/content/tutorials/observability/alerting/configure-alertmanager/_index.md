---
linkTitle: Configure alerting
title: Configure alerting
description: Learn how to configure alerting in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-alerting-configuration
    parent: tutorials-observability-alerting
weight: 40
last_review_date: 2025-06-03
user_questions:
  - How do I configure Alertmanager?
  - How do I visualize the existing alerting configuration?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

The Giant Swarm Observability Platform provides an [alerting pipeline]({{< relref "/overview/observability/alerting/" >}}) that you can configure per tenant. This tutorial explains how to configure alerting for your tenant.

## Prerequisites

Before you begin, ensure you have:

- Access to your management cluster
- A tenant defined in a [Grafana Organization]({{< relref "/tutorials/observability/multi-tenancy/" >}})

## Configure Alertmanager

The Observability Platform uses Mimir Alertmanager for alerting capabilities.

To configure Alertmanager for your tenant, create a secret on your management cluster with the required labels and configuration data.

### Example configuration

The following example shows an Alertmanager configuration for the `my-team` tenant:

```yaml
apiVersion: v1
kind: Secret
metadata:
  labels:
    # This label marks this secret as an Alertmanager configuration
    observability.giantswarm.io/kind: alertmanager-config
    # This label specifies the tenant for this configuration
    observability.giantswarm.io/tenant: my-team
  name: my-alertmanager-config
  namespace: default
stringData:
  # This field is mandatory and contains the Alertmanager configuration
  alertmanager.yaml: |
    route:
      receiver: "example_receiver"
      group_by: ["example_groupby"]
    receivers:
      - name: "example_receiver"
    templates:
      - example_template.tmpl
  # Optional: Include reusable template files with .tmpl extension
  # See: https://prometheus.io/docs/alerting/latest/notification_examples/#defining-reusable-templates
  example_template.tmpl: |
    {{ define "alert_customer_env_message" }}
    [{{ .CommonLabels.alertname }} | {{ .CommonLabels.customer }} | {{ .CommonLabels.environment }}]
    {{ end }}
type: Opaque
```

### Configuration validation

Validate your Alertmanager configuration before applying it. A validating webhook rejects invalid configurations.

**Recommendation**: Use [`mimirtool`](https://grafana.com/docs/mimir/latest/manage/tools/mimirtool/#validate-alertmanager-configuration) in your CI pipeline to validate configurations before deployment.

### Important considerations

- **Tenant validation**: The `observability.giantswarm.io/tenant` label must reference a tenant defined in an existing Grafana Organization
- **Template files**: The platform processes only files with the `.tmpl` extension as templates
- **Webhook validation**: The platform automatically rejects invalid configurations or non-existent tenants
