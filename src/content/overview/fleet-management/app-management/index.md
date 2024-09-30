---
linkTitle: App management
title: App management
description: The app platform allows to manage app catalogs and apps, for simple and standardized deployment across the platform.
weight: 40
aliases:
  - /platform-overview/app-platform
  - /app-platform
  - /app-platform/overview
menu:
  principal:
    parent: overview-fleet-management
    identifier: overview-fleet-management-app-platform
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What does App Platform do?
  - What is an App Catalog?
  - What is a Managed App?
  - Does Giant Swarm provide app catalogs out of the box?
  - How is App Platform implemented?
  - How does the App Platform relate to Helm?
  - What are the components of App Platform?
  - What are the app catalogs that Giant Swarm provides out of the box?
  - How can I create an organizational app catalog?
  - How can I interact with the Giant Swarm App Platform?
  - Can I create an app catalog?
last_review_date: 2024-09-30
---

The _Giant Swarm App Platform_ refers to a set of features and concepts that allow you to browse, install and manage the configurations of apps (such as Prometheus) from a single place; the [platform API]({{< relref "/overview/architecture#platform-api" >}}).

Giant Swarm fully support [Helm](https://helm.sh/) as a general tool to deploy your applications as well as for our general `App Catalog`. Apps are packaged as Helm charts and can be configured with _values_. A recommended [app configuration]({{< relref "/tutorials/app-platform/app-configuration" >}}) is provided which you can override to meet your needs.

The app platform then, underneath, installs these Helm Charts whenever an app installation is requested by you.
The Helm execution is mostly not configurable for you, with the exception to the options presented in
[installation configuration]({{< relref "/tutorials/app-platform/installation-configuration" >}}).

This feature of the platform provides a collection of curated managed apps. These managed apps are grouped into app catalogs, which can be browsed through our web interface. may also install their own catalogs using the platform API. Finally, it's worth noting that Giant Swarm uses the app platform to install the apps that are pre-installed in your clusters, such as `coredns` or `cluster-autoscaler`.

In short: the _Giant Swarm App Platform_ refers to the whole feature, and an app catalog is a collection of apps.

Giant Swarm provides an app catalog with our offered set of cloud-native applications which are operated and pre-configured by us. You are able to set up your own [additional catalog(s)]({{< relref "/tutorials/app-platform/create-catalog" >}}) to provide for any needs you have at the enterprise level.

### What makes up the Giant Swarm app platform {#what-makes-up-the-app-platform}

Technically the app platform is implemented as a set of operators
running on your management cluster and workload clusters. These operators watch various
Custom Resources, some created by us, and others created by you. Together, they make up
the desired state of the app platform.

For example, this `App` custom resource indicates that you want `Kong` installed
on a specific workload cluster. Some values are [defaulted]({{< relref "/tutorials/app-platform/defaulting-validation" >}}) for the workload cluster you select.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: "my-kong"
  namespace: "x7jwz"
spec:
  catalog: "giantswarm"
  config:
    configMap:
      name: "x7jwz-cluster-values"
      namespace: "x7jwz"
  name: "kong-app"
  namespace: "kong"
  version: "0.7.2"
  kubeConfig:
     inCluster: false
  userConfig:
    configMap:
      name: "kong-user-values"
      namespace: "x7jwz"
```

Below you can see a high level overview of the components and resources that work together to enable the features of the Giant Swarm app platform:

![A diagram showing an overview of various components and concepts that make up the Giant Swarm App Platform](app-platform-overview.png)
<!-- Original version: https://docs.google.com/drawings/d/1V3KcUImxRdrrb2v_nIQnkapHiRkRM6t8PoYGCqWebYY/edit -->

#### The Giant Swarm app catalog

This catalog contains our stable, fully managed apps, with SLA (for example the ingress nginx controller).

The maturity levels of apps in this catalog are expressed through semantic versioning as follows:

- Version with `-alpha` or `-beta` suffix - the application is only at a basic maturity level. There is no stable release. It's supported on a best effort basis,
- Version with `-rc*` suffix - the application is at a preview maturity level. This allows customers to preview a new release of an application and evaluate new features. It's supported on a best effort basis.
- version >= `v1.0.0` with no suffix - the specified version of the application is at a stable maturity level. It's available to our customers as a managed offering with support and SLA.

### Managed app definition

A `managed app` is an app in our Giant Swarm catalog that provides:

- Safe and tested deployment

Helm chart are ready to use and tested, either sanitizing the upstream forked applications or creating good defaults for our maintained ones. [It is offered a common way of building apps](https://github.com/giantswarm/app-build-suite) and a [testing framework](https://github.com/giantswarm/app-test-suite) which ensure the application is deployable and works as expected. Security and upgrade viability are checked too during the integration process.

- Monitoring

Giant Swarm makes sure all the main components of the app are running and that the app is working as expected. At the same time, our automation set up monitoring and alerting on necessary metrics to ensure our service level agreements.

In case of an alert, operations team perform an Root Cause Analysis (RCA) to understand if it's a Giant Swarm or customer-inflicted issue that broke the application.

__Note__: Giant Swarm don't fix bugs upstream when they involve significant code changes. That said, our team always try to find a workaround or the root cause of the issue and submit a ticket to the upstream project. In some cases, our engineers fix the bug ourselves where it’s necessary and possible for us, and provide the fix to the upstream project. This might result in temporarily running a non-upstream patch version from Giant Swarm until upstream merges our patch. Customers can, in general, expect the same level of service for a managed optional app as they get with "default" apps such as `coredns`.

- Configurations and Plugins

The customer can do unlimited configurations to the app. The customer can also install unlimited plugins to the app. The application configuration is the customer's responsibility. In other words, configurations that derail from the default ones have to be tested and maintained by the customer. Giant Swarm is always happy to help in validating whether those configurations adhere to best-practices and test them together with the customer, but it's the latter's responsibility to actually deploy those configurations in their environments according to their deployment processes and maintenance windows.

__Note__: Giant Swarm only perform tests for upgrades with the default values, so in case you have customized configuration you need to ensure that the upgrade procedure works as expected in a lower environment and reach out to our support in case of problems.

- Upgrades

Our team following the common semantic versioning (`semver`) use in cloud-native projects to release our apps:

1. Patch releases (for example, 2.1.1 -> 2.1.2 -> 2.1.3): those are rolled automatically, add them to the change logs, and communicate the changes to the customer.
2. Minor versions: upgrade to minor versions, add them to the change logs, and communicate the changes to the customer.
3. Major versions: the customer decides when to do a major upgrade. Similar to our managed Kubernetes, it only supports one major version back.

All changes are in the change logs and communicated them to customers weekly.

It's the responsibility of the customer to upgrade the applications they run. Whereas Giant Swarm provides updated charts and the relative changelogs and is always willing to help customers understand the impact of upgrades, the responsibility of actually triggering upgrades resides on the customer. This ensures that no changes happen outside of customer-defined maintenance windows and gives customers all the time they need to validate upgrades in low environments before applying them to production ones. That said, Giant Swarm provides tooling to automate upgrades for the apps and customers can adopt it to automate changes on the platform.

- Dependencies

If a managed app requires secondary apps to run, charts are adapted to run a "standard" deployment of the secondary app. However, these are not managed and maintained in the same terms as a primary app.

__Note__: Overall, it adapts the chart to make sure the app works with the customer’s custom configurations and plugins.

### Installing your own App Catalog

It’s possible to create your own App Catalog. This is useful if you want to create a set of apps available to your company. Currently, this functionality is only available through direct access to the Giant Swarm platform API. You can request access from your account engineer. Prerequisite for this is a standard Helm chart repository. It should be served through HTTP and accessible to the management cluster and your workload clusters.

### How interact with the Giant Swarm app platform

You can interact with the Giant Swarm app platform through creating `App` custom resources using the platform API or the developer portal.

- [App CRD reference]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}})
- [The Giant Swarm developer portal]({{< relref "/overview/developer-portal/" >}})

As you have direct access to the platform API you can also interact with the above mentioned resources using `kubectl`, and automate them just as you have been automating other parts of your stack. And as Kubernetes resources and especially some custom resource definitions require lots of boilerplate and conventions, our team built a [kubectl plugin]({{< relref "/vintage/use-the-api/kubectl-gs" >}}) to help you with that.
