---
title: "Alerting with the Observability Platform"
linkTitle: Alerting
description: Documentation on the observability-platform alerting concept and architecture deployed and maintained by Giant Swarm.
weight: 80
menu:
  principal:
    identifier: overview-observability-alerting
    parent: overview-observability
user_questions:
  - How is alerting managed by the observability platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2025-04-24
---

Alerting is an important concept of any observability solution and it's thus only natural that it is available as part of the Giant Swarm Observability Platform. For more details and information on alerting please visit the [official Grafana documentation page](https://grafana.com/docs/grafana/latest/alerting/).

## How alerting works

Alerting is usually divided into two distinct concepts: the alerting pipeline (how to send alerts, to whom and what to send) and alerting/recording rules (what to alert on). This documentation will cover how those two topics work in the Observability Platform.

Learn more about our [multi-tenancy concept]({{< relref "/overview/observability/configuration/multi-tenancy/concepts" >}}).

### The alerting pipeline

![alerting pipeline](./alerting-pipeline.png)

As you can see in the image above, the alerting pipeline is quite straightforward. The Loki and Mimir rulers evaluate alerting rules and send alerts to the Mimir Alertmanager. The Mimir Alertmanager (a multi-tenant aware Alertmanager) routes those alerts to configured receivers.

If you want to learn how to configure Alertmanager for your tenants, please refer to our [dedicated documentation]({{< relref "/tutorials/observability/alerting/configure-alertmanager" >}}).

### Loading alerting and recording rules

![loading recording and alerting rules](./alerting-loading-rules.png)

The Observability Platform allows you to create and load both alerting and recording rules into:

- the Mimir ruler (*metric-based* alerts)
- the Loki ruler (*log-based alerts)
Alerting and recording rules can be loaded from both management cluster and workload clusters alike via our Grafana Alloy agents.

If you want to learn how to configure your own, please, refer to our [dedicated documentation]({{< relref "/tutorials/observability/alerting/configure-alertmanager" >}}).

## Alerting Overview in Grafana

If you want to want to learn more about the configuration of the alerting pipeline and the alerting rules for a tenant, you can find this information in the *Alerting* section of your [installation's Grafana]({{< relref "/tutorials/observability/data-exploration/accessing-grafana/" >}})

![Grafana alerting section](./grafana-alerting.png)

In this section, you have access to various features such as:

- __Alerts rules__: all (alerts and recording) rules currently available, which can be filtered by state like firing or pending. When unfolding an alert rule you can use the *see graph* link to jump to an explore page with the alert's expression pre-filled.
- __Contact points__: configured integrations (for example opsgenie or slack) to send alerts to, along with notification templates used to format alerts when sent out.
- __Notification policies__: alerts routing which defines how alerts are sent to contact points based on matching criteria.
- __Silences__: silences currently loaded and their state along with the affected alerts.
- __Active notifications__: currently firing alerts. It might be confused with the *Alerts rules* page at first, but this page differs in the fact that it only shows alert currently firing along with the notification state.
- __Settings__: general settings for the Alertmanager instance, also show the currently loaded configuration
