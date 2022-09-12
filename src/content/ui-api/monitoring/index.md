---
linkTitle: Monitoring
title: Monitoring and dashboards
description: Giant Swarm runs a monitoring stack in each installation, comprising Prometheus, Grafana, and more. Learn how to get access to the data we collect.
menu:
  main:
    identifier: uiapi-monitoring
    parent: ui-api
weight: 40
last_review_date: 2021-06-28
user_questions:
  - How can I access Grafana for my installation?
  - How can I access metrics from my installation?
  - Where can I find workload cluster metrics?
  - Which dashboards do I have access to?
  - Which metrics are gathered in my installation?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

Giant Swarm runs a monitoring stack in each installation, based on [Prometheus](https://prometheus.io/), collecting data from most management cluster components, as well as many workload cluster metrics.

For accessing these metrics, both for you as customers and for our staff we provide a [Grafana](https://grafana.com/) instance per installation.

![Home dashboard](home-dashboard.png)

We aim to provide a useful set of dashboards for you to quickly explore all metrics relevant to you, giving you access to the same information that we use for operations, support, and billing.

## Accessing dashboards

If you have access to the Giant Swarm [web interface]({{< relref "/ui-api/web" >}}), the easiest way to get to Grafana is to click the **Monitoring** link in the top menu when logged in.

In case you don't have access to the Giant Swarm web interface, you can ask your Giant Swarm support contact for the URL.

In case you want to construct the URL to the Grafana web application in your installation yourself, it follows the same pattern as the one for our web interface and many other services.

For example, if your web interface URL is

    https://happa.g8s.example.westeurope.azure.gigantic.io/

then simply replace `happa` with `grafana` to get to your Grafana URL:

    https://grafana.g8s.example.westeurope.azure.gigantic.io/

## Authentication and authorization

Access to Grafana is controlled via **single sign-on** (SSO), using the same identity provider you use for the [Management API]({{< relref "/ui-api/management-api/authentication" >}}).

In order to access Grafana as a customer, you must be a member of the admin group. Specifically, that's a group in your identity provider selected to specify which users have admin permissions in the Giant Swarm installation.

**Note**: If you don't have SSO configured yet or have any questions regarding the admin group, please contact your Account Engineer.

Once you open the Grafana URL for your installation, you will be greeted by a page titled "Log in to Dex", where you are prompted to select the identity provider to authenticate with. The screenshot below shows an example.

![Selecting an OIDC provider](access.png)

There is one identity provider configured for Giant Swarm staff and one for you as a customer admin. Depending on the type of identity provider used for you as a customer, the label for the button to click can look slightly different.

After selecting the right identity provider, you may run through an authentication workflow. However, if you are already authenticated within the current browser, this will be skipped and you should see the Home dashboard as a result.

## Repository

Dashboard are defined in the [giantswarm/dashboards](https://github.com/giantswarm/dashboards) repository. As an example, [this link](https://github.com/giantswarm/dashboards/blob/2be49ef09bccdb65c4fd62c835567bc0794617da/helm/dashboards/dashboards/shared/home.json) takes you to the _Home_ dashboard definition as of June 28, 2021.

You can easily track changes in that repository directly from the Home dashboard in Grafana or via the [changes and releases](/changes/dashboards/) section.

## Limitations

Grafana access is currently not available in shared installations, where several customer's metrics would be available from the same Grafana instance.
