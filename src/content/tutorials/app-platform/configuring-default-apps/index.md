---
linkTitle: Customizing default apps
title: Customizing default apps
description: How to customize preinstalled apps configuration using configmaps or secrets.
weight: 50
menu:
  principal:
    parent: tutorials-app-platform
    identifier: tutorials-app-platform-app-default-apps
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I customize preinstalled apps configuration?
  - How can I customize default apps configuration?
last_review_date: 2024-10-21
---

In a Giant Swarm platform, every cluster has a set of apps that are installed automatically at creation time. This set of apps is defined in the [cluster app](https://github.com/giantswarm/cluster) and the list includes important applications that are mandatory to make the cluster work correct. Example of these apps are `coredns` or `cilium`.

Normally it's advisable to stick to the default values for the configuration of those apps. Sometimes, though, some level of customization is needed. This page explains how to customize the configuration of such apps.

## Find out what configuration can be changed

Customizing the app's configuration means providing overrides to the `Helm` chart's default values for that app.

In order to find out what options you can customize for each app, you can refer to the app's default values file in the GitHub repository.

For example, for the `coredns` app you can refer to this file: https://github.com/giantswarm/coredns-app/blob/master/helm/coredns-app/values.yaml

If you can't find the default values file for the app you need to customize the configuration for, please reach out to your account engineer.

## Prepare the configuration file

Let's say for example you want to decrease the cache TTL for `coredns`. The relevant setting in the values file is:

```yaml
configmap:
  cache: 30
```

In order to change the default value of `30` seconds, you need to prepare a file with the same structure, such as:

```yaml
configmap:
  cache: 15
```

For the sake of this example, let's call the file `coredns-config-override.yaml`.

## Create a configmap

Once you have your configuration override file ready, you need to create a configmap in the management cluster. The configmap has to be created in the workload cluster namespace.

```sh
export ORG=<organization name>
kubectl -n $ORG create configmap coredns-override-default --from-file=values=coredns-config-override.yaml
```

After you created the configmap, you need to label it in order to associate the configuration with the app you want to override the configuration to. In our example this is `coredns`.

```sh
kubectl -n $ORG label configmap coredns-override-default app.kubernetes.io/name=coredns
```

## Confidential data

In case the configuration change involves confidential data, you might want to provide the setting as a secret rather than a configmap. Example:

```sh
kubectl -n $ORG create secret generic coredns-override-default --from-file=values=coredns-config-override.yaml
```

You still need to label the secret with the app name:

```sh
kubectl -n $ORG label secret coredns-override-default app.kubernetes.io/name=coredns
```

## Multiple configurations and priority

Please note it's possible to override multiple configuration fields in the same configmap or secret and it's possible to have multiple configmaps and secrets for the same app.

In order to specify a priority order in case of multiple configmaps or secrets, you can use the `cluster-operator.giantswarm.io/app-config-priority` annotation.

Please refer to the [app configuration]({{< relref "/tutorials/app-platform/app-configuration#extra-configs" >}}) page for more details.
