---
linkTitle: How to ship audit logs
title: How to ship audit logs to a remote location
description: This article explains how to forward your audit logs to a remote location.
weight: 50
menu:
  main:
    identifier: advanced-observability-logging-logshipping
    parent: advanced-observability-logging
user_questions:
  - How do I ship audit logs to a remote location?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-02-28
aliases:
  - /advanced/observability/logging/log-shipping
---

In this article you will learn how to forward audit logs to external storage, like a Security Information and Event Management (SIEM) system.

If you want to learn about the audit logs Giant Swarm provides, take a look [here]({{< relref "/vintage/getting-started/observability/logging/audit-logs" >}})

## How to ship your audit logs to a remote location

Giant Swarm provides a [Logging Infrastructure]({{< relref "/vintage/getting-started/observability/logging" >}}) that you can use to take a look at the logs of the components we manage, but it is highly possible that you need to store audit logs to a remote location for compliance reasons.

__Note__: You can also access and ship the audit logs for the management clusters, but this is not something we provide by default (at least for now). Please contact your Account Engineer to sort out the details.

To that end, you can use one of the following solutions:

### Fluent bit

Giant Swarm provides a custom [Fluent-bit](https://fluentbit.io/) configuration packaged as a Managed App named [`fluent-logshipping-app`](https://github.com/giantswarm/fluent-logshipping-app)

Fluent-bit's main advantage is that it can be used for all kinds of cases (shipping to rsyslog, elasticsearch, loki, and so on) and provides a lot of configurability with its plugin system.

### Promtail

[Promtail](https://github.com/giantswarm/promtail-app) can only be used with Loki. It provides a better integration with Kubernetes via its discovery mechanism and enriches logs with metadata by default. It can also be used to read files on the machines like the audit logs described [here](https://github.com/giantswarm/promtail-app#configuration).
