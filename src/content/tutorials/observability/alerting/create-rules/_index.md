---
linkTitle: Creating alerting rules
title: How to create alerts and recording rules
description: Guide explaining how to create alerts and recording rules in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-alerting-alerts
    parent: tutorials-observability-alerting
weight: 40
last_review_date: 2025-04-24
user_questions:
  - How to create alerts?
  - How to create recording rules?
  - What is log-based alerting?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

The Giant Swarm Observability Platform provides an [alerting pipeline]({{< relref "/overview/observability/alerting/" >}}) that [you can configure per tenant]({{< relref "/tutorials/observability/alerting/configure-alertmanager" >}}) as well as allow you to create your own alerting and recording rules per tenant.

As Giant Swarm embraces GitOps, alerting and recording rules needs to be defined via [Prometheus Operator](https://prometheus-operator.dev/) PrometheusRules. Those rules can be defined in both your management cluster and workload clusters alike.

**Warning:** As our multi-tenancy aligns tenants across our platform on Grafana Organizations please make sure that the `observability.giantswarm.io/tenant` label defined on your rules references an existing tenant defined in a Grafana Organization. Any PrometheusRules that references an non-existing tenant will be ignored. Learn more about our multi-tenancy in [Multi-tenancy in the observability platform]({{< relref "/tutorials/observability/multi-tenancy/" >}})

## How to define a recording rule

[Recording rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/#recording-rules) allow you to precompute frequently needed or computationally expensive expressions and save their result as a new set of time series.

To load a recording rule into your tenant, you should use apply the following manifest:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    # This lets Alloy know to which tenant this alert belongs to
    observability.giantswarm.io/tenant: my-team
  name: cluster-resource-usage
  namespace: my-namespace
spec:
  groups:
  - name: cluster-resource-usage
    rules:
      - expr: |
          avg by (cluster_id) (
            node:node_cpu_utilization:ratio_rate5m
          )
        record: cluster:node_cpu:ratio_rate5m
```

## How to define an alerting rule

[Alerting rules](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/) allow you to define alert conditions based on Prometheus (or Loki) expression language expressions and to send notifications about firing alerts to an external service.

Here is how you would define your alerting rule:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  labels:
    # This lets Alloy know to which tenant this alert belongs to
    observability.giantswarm.io/tenant: my-team
  name: cluster-resource-usage-too-high
  namespace: my-namespace
spec:
  groups:
  - name: reliability
    rules:
      - alert: ComponentDown
        annotations:
          # See https://grafana.com/docs/grafana/latest/alerting/alerting-rules/templates/#template-annotations for useful annotations used by Grafana.
          __dashboardUid__: my-dashboard-uid
          summary: 'Component is done.'
          description: 'Component {{ $labels.service }} is down.'
          runbook_url: https://my-pretty-runbook
        expr: count(up{job=~"component/.*"} == 0) by (cluster_id) > 0
        # Alert if the expression returns results for more than 5 minutes
        for: 5m
        labels:
          # This is a paging alert that need to wake my team up
          severity: page
```

## Differentiate between metric vs Log-based rules

Metric-based rules are evaluated by the Mimir ruler and are written using PromQL while Log-based rules are evaluated by the Loki ruler and are written using LogQL.

To be able to differentiate if your alert is a log-based alert, you should label you alert with those labels:

```yaml
# This label is marked as deprecated but still needs to be configured.
application.giantswarm.io/prometheus-rule-kind: loki
observability.giantswarm.io/rule-type: logs
```

## Cluster vs installation scoping of rules

To avoid conflicts when loading rules from multiple clusters in the same tenant (for instance, if your teams define a PrometheusRule in their application template deployed in a dev, staging and prod clusters), the Observability Platform support some level of scoping.

Any rule deployed in workload clusters is by default cluster-scoped (only targets metrics coming from this cluster) while a rule deployed in management clusters is scoped to the installation (targets all metrics of all clusters).

In practice, this means that:

- If you deploy a rule with the expression `up{job="good"} > 0` in the workload cluster named `alpha1`, then the loaded rules will have the expression `up{cluster_id="alpha1", job="good"} > 0`.
- If you deploy a rule with the expression `up{job="good"} > 0` in the _management cluster_ named `alpha1`, then the loaded rules will have the expression `up{job="good"} > 0`.

### Limitations

- Cluster-scope is only available to metric-based alerts today due to upstream limitations
- Scoping can only be used when teams deploy the same rule **once** accross multiple clusters. If you need to deploy it per app in different namespaces, you will need to manage the conflict yourself.
