---
linkTitle: Customizing default apps
title: Customizing default apps
description: How to customize preinstalled apps configuration using ConfigMap or Secrets resources.
weight: 50
aliases:
  - /getting-started/app-platform/configuring-default-apps
  - /vintage/getting-started/app-platform/configuring-default-apps
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-app-default-apps
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I customize preinstalled apps configuration?
  - How can I customize default apps configuration?
last_review_date: 2025-11-28
---

In a Giant Swarm platform, every workload cluster has a set of apps that are installed automatically at creation time, called default apps. Default apps are defined in the [cluster app](https://github.com/giantswarm/cluster) and the list includes important applications that are mandatory to make the cluster work correctly. Examples of these apps are CoreDNS or Cilium.

Normally it's advisable to stick to the default values for the configuration of default apps. Sometimes though, some level of customization is needed. This page explains how to customize the configuration of default apps.

## Find out what configuration can be changed

Customizing the app's configuration means providing overrides to the Helm chart's default values for that app.

In order to find out what options you can customize for each app, you can refer to the app's default values file in the GitHub repository.

For example, for the [app providing CoreDNS](https://github.com/giantswarm/coredns-app) you can refer to the file [helm/coredns-app/values.yaml](https://github.com/giantswarm/coredns-app/blob/master/helm/coredns-app/values.yaml) in the repository.

If you can't find the default values file for the app you need to customize the configuration for, please reach out to your account engineer.

## Prepare the configuration file

Let's say for example you want to decrease the cache lifetime for CoreDNS. The relevant setting in the values file is:

```yaml
configmap:
  cache: 30
```

To change the default value of 30 seconds to 15 seconds, you need to prepare a file with the same structure, such as:

```yaml
configmap:
  cache: 15
```

For the sake of this example, let's call the file `coredns-config-override.yaml`.

## Create a ConfigMap

Once you have your configuration override file ready, you need to create a ConfigMap in the management cluster. The ConfigMap has to be created in the namespace of the organization that owns the workload cluster.

```shell
export NAMESPACE=org-<organization name>

kubectl --namespace $NAMESPACE \
  create configmap coredns-override-default \
  --from-file=values=coredns-config-override.yaml
```

After you created the ConfigMap, you need to label it to associate the configuration with the app you want to override the configuration to. In our example, the label value is `coredns`.

```sh
kubectl --namespace $NAMESPACE \
  label configmap coredns-override-default \
  app.kubernetes.io/name=coredns
```

## Confidential data

In case the configuration change involves confidential data, you might want to provide the setting as a secret rather than a ConfigMap. Example:

```sh
kubectl --namespace $NAMESPACE \
  create secret generic coredns-override-default \
  --from-file=values=coredns-config-override.yaml
```

You still need to label the secret with the app name:

```sh
kubectl --namespace $NAMESPACE \
  label secret coredns-override-default \
  app.kubernetes.io/name=coredns
```

## Multiple configurations and priority

Please note it's possible to override multiple configuration fields in the same ConfigMap or Secret and it's possible to have multiple ConfigMaps and Secrets for the same app.

To specify a priority order in case of multiple ConfigMaps or Secrets, you can use the `cluster-operator.giantswarm.io/app-config-priority` annotation.

Please refer to the [app configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration#extra-configs" >}}) page for more details.
