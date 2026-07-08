---
title: Understanding alert silences
linkTitle: Understanding alert silences
diataxis_content_type: explanation
description: How alert silences work on the Giant Swarm observability platform, when to use them, the two management approaches, and how they fit into the alerting pipeline.
weight: 25
menu:
  principal:
    parent: overview-observability-alert-management
    identifier: overview-observability-alert-management-understanding-silences
last_review_date: 2026-07-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is an alert silence?
  - When should I use a silence?
  - What is the difference between CRD-based and Grafana UI silences?
  - Where do silences sit in the alerting pipeline?
  - How do overlapping silences resolve?
---

This page explains what alert silences are and how they behave on the Giant Swarm Observability Platform, so you can decide when and how to use them. For the step-by-step mechanics of creating and managing silences, see the [silences how-to]({{< relref "/overview/observability/alert-management/silences" >}}).

## What a silence is

A silence temporarily prevents alerts from generating notifications without stopping alert evaluation. When an alert matches an active silence, Alertmanager suppresses its notifications but the underlying alert rule keeps evaluating. The alert still exists and still reflects the real state of your system. Only the outbound notification is held back.

This distinction matters: a silence isn't a way to "turn off" an alert or hide a problem. It's a way to acknowledge that you already know about a condition and don't need to be paged about it for a while.

Silences are most useful for:

- **Planned maintenance**: prevent noise during scheduled downtime.
- **Investigation periods**: focus on troubleshooting without a stream of repeat notifications.
- **Known issues**: temporarily suppress alerts for a problem you've already acknowledged.

## Two ways to manage silences

The platform supports two complementary approaches, and the right choice depends on whether the silence is planned or reactive:

- **CRD-based (GitOps)**: you declare silences as Kubernetes `Silence` resources (the `observability.giantswarm.io/v1alpha2` API). Because they live in Git, they're version-controlled, reviewable, and repeatable. This is the recommended approach for anything planned, such as recurring maintenance windows.
- **Grafana UI**: you create silences interactively in the Grafana Alerting interface. This is immediate and needs no deployment, which makes it the natural fit for emergencies during an active incident or quick, ad-hoc silences while developing alert rules.

Both approaches integrate with the platform's [multi-tenancy model]({{< relref "/overview/observability/configuration/multi-tenancy" >}}): a silence affects only alerts within its own tenant, and it must carry a tenant label referencing an existing Grafana Organization. Silences referencing a non-existent tenant are ignored.

## Where silences sit in the alerting pipeline

Silences act at the Alertmanager level, after alert rules are evaluated but before [alert routing]({{< relref "/overview/observability/alert-management/alert-routing" >}}) delivers notifications. Three consequences follow from that position:

- **Alert rules keep evaluating**: silences don't touch rule evaluation, so the data behind an alert is unaffected.
- **State stays visible**: silenced alerts still appear in Grafana in a suppressed state, so you can see what's currently muted.
- **Routing is bypassed**: matching alerts don't reach their receivers, so no notifications are sent while the silence is active.

## How overlapping silences resolve

When more than one silence could apply to the same alert, the platform resolves it predictably:

- **Most specific wins**: a silence with more matchers takes precedence over a broader one.
- **Newest wins**: among equally specific silences, the most recently created one applies.
- **All matchers must match**: an alert is only suppressed by a silence if it matches every matcher in that silence.

## Protection for critical alerts

A broad silence is easy to over-scope, so the platform keeps a safety net by default. Every silence automatically excludes the most critical, system-wide alerts (those targeting all notification pipelines) and the `Heartbeat` alert. This means an over-broad silence won't take down the alerts you most need to keep flowing.

That protection can be waived for a genuine full-maintenance window (see [forcing complete silence]({{< relref "/overview/observability/alert-management/silences#forcing-complete-silence" >}}) in the how-to), but the `Heartbeat` alert is always preserved. Waiving the net removes the very alerts that would page you if something went wrong, so it should stay narrowly scoped and short-lived.

## See also

- [Silences how-to]({{< relref "/overview/observability/alert-management/silences" >}}): create, update, and remove silences via CRDs and the Grafana UI
- [Silence CRD reference]({{< relref "/reference/platform-api/crd/silences.observability.giantswarm.io" >}}): the full `Silence` v1alpha2 field schema
- [Alert routing]({{< relref "/overview/observability/alert-management/alert-routing" >}}): how notifications reach receivers once they pass the silence stage
- [Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}}): how tenants isolate observability data, including silences
