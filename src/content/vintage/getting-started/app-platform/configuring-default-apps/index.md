---
linkTitle: Customizing Preinstalled Apps config
title: Customizing Preinstalled Apps configuration using configmaps
description: How to customize preinstalled apps configuration using configmaps or secrets.
weight: 40
menu:
  main:
    parent: getting-started-app-platform
    identifier: getting-started-app-platform-app-default-apps
last_review_date: 2022-09-26
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
aliases:
  - /getting-started/app-platform/configuring-default-apps
  - /developer-platform/app-platform/configuring-default-apps
  - /app-platform/configuring-default-apps
user_questions:
  - How can I customize preinstalled apps configuration?
  - How can I customize default apps configuration?
---

## Overview

This document applies to pre-CAPI Giant Swarm clusters starting from release v19:

- AWS >= v19.0.0 < v20.0.0
- Azure >= v19.0.0 < v20.0.0

Every cluster has a set of Apps that are installed automatically at cluster creation time.
This set of apps is defined in the `Release CR` in the management cluster and the list includes important applications
that are mandatory to make the cluster work properly. Example of these apps are coreDNS and Cilium.

Normally it is advisable to stick to the default values for the configuration of those apps.
Sometimes, though, some level of customization is needed.

This page explains how to customize the configuration of such apps.

## Find out what configs can be changed

Customizing the app's configuration ultimately means providing overrides to the helm chart's default values for that app.

In order to find out what options you can customize for each app, you can refer to the app's default values file in the github repo.

For example, for the coredns app you can refer to this file: https://github.com/giantswarm/coredns-app/blob/master/helm/coredns-app/values.yaml

If you can't find the default values file for the app you need to customize the config for, please reach out to your account engineer.

## Prepare the config file

Let's say for example you want to decrease the cache TTL for coredns. The relevant setting in the vaules file is:

```yaml
configmap:
  cache: 30
```

In order to change the default value of 30 seconds, you need to prepare a file with the same structure, such as:

```yaml
configmap:
  cache: 15
```

For the sake of this example, we'll call this file `coredns-config-override.yaml`.

## Create a configmap

Once you have your config override file ready, you need to create a configmap in the `management cluster`.
The configmap has to be created in the workload cluster namespace.

```sh
kubectl -n <workload cluster name> create configmap coredns-override-default --from-file=values=coredns-config-override.yaml
```

After you created the configmap, you need to label it in order to associate the configuration with the app you want to
override the config to. In our example this is `coredns`.

```sh
kubectl -n <workload cluster name> label configmap coredns-override-default app.kubernetes.io/name=coredns
```

## Confidential data

In case the configuration change involves confidential data, you might want to provide the setting as a Secret rather than a configmap.
This is possible. Here's an example:

```sh
kubectl -n <workload cluster name> create secret generic coredns-override-default --from-file=values=coredns-config-override.yaml
```

You still need to label the secret with the app name:

```sh
kubectl -n <workload cluster name> label secret coredns-override-default app.kubernetes.io/name=coredns
```

## Multiple configs and priority

Please note it is possible to override multiple config fields in the same configmap or secret and it is possible to
have multiple configmaps and secrets for the same app.

In order to specify a priority order in case of multiple configmaps or secrets, you can use the `cluster-operator.giantswarm.io/app-config-priority` annotation.

Please refer to the [App configuration]({{< relref "/vintage/getting-started/app-platform/app-configuration#extra-configs" >}}) page for more details.
