---
linkTitle: Accessing Grafana
title: How to access Grafana dashboards
description: Guide explaining how to get access to the data collected and stored by the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-data-exploration-accessing-grafana
    parent: tutorials-observability-data-exploration
weight: 40
last_review_date: 2024-12-12
user_questions:
  - How to access Grafana?
  - How to access metrics from my clusters?
  - How to access logs from my clusters?
  - Where to find cluster metrics?
  - Where to find cluster logs?
  - Which dashboards exists?
  - Which metrics are gathered from my clusters?
  - Which logs are gathered from my clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

Giant Swarm provides an Observability Platform in each installation, based on [Grafana Mimir](https://grafana.com/oss/mimir/) for metrics, and [Grafana Loki](https://grafana.com/oss/loki/) for logs, collecting data from the system and apps managed by Giant Swarm, as well as any source of data you configure according to [the data ingestion tutorial]({{< relref "/tutorials/observability/data-ingestion" >}}).

These metrics and logs are available to be explored in your [Grafana](https://grafana.com/) instance on the installation.

![Home dashboard](home-dashboard.png)

We aim to provide a useful set of dashboards for you to quickly explore all observability data relevant to you, giving you access to the same information that we use for operations, support, and billing.

## Accessing dashboards

The address for your installation's `grafana` instance is composed of the base domain plus the `grafana` subdomain.

If you don't know the base domain for your installation, you can ask your Giant Swarm support contact for the address.

## Authentication and authorization

Access to `grafana` is controlled via `single sign-on` (SSO), using the same identity provider you use for the [platform API]({{< relref "/tutorials/access-management/authentication" >}}).

In order to access Grafana as a customer, you must be a member of the admin group. Specifically, that's a group in your identity provider selected to specify which users have admin permissions in the Giant Swarm installation.

__Note__: If you don't have `single sign-on` (SSO) configured yet or have any questions regarding the admin group, please contact your Account engineer.

Once you open the Grafana address for your installation, you will be able to login via the Giant Swarm SSO. The screenshot below shows an example.

![Selecting an OIDC provider](access.png)

There is one identity provider configured for Giant Swarm staff and one for you as a customer admin. Depending on the type of identity provider used for you as a customer, the label for the button to click can look slightly different.

After selecting the right identity provider, you may run through an authentication workflow. However, if you are already authenticated within the current browser, this will be skipped and you should see the Home dashboard as a result.

When you log in, you will be logged into the Shared Org. which contains a curated set of provided dashboards that we manage and that is accessible to everyone. If you want to learn more about organizations and multi-tenancy, we can only advise you to read the related [documentation]{{< relref "/tutorials/observability/multi-tenancy" >}}).

## Limitations

Grafana access is currently not available in shared installations, where several customer's observability data would be available from the same Grafana instance.
