---
linkTitle: Configuring installation process
title: Configure Helm execution
description: Which options for the Helm execution are currently supported by the App Platform.
weight: 60
menu:
  principal:
    parent: tutorials-app-platform
    identifier: tutorials-app-platform-config-install
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I configure custom timeouts for installations and upgrades?
last_review_date: 2024-10-21
---

As explained in the [app platform overview]({{< relref "/overview/fleet-management/app-management" >}}) all managed apps are `Helm` charts underneath. It means that at the very bottom the platform must trigger the Helm-related actions, like installation or upgrade, against the requested application. This process, mostly, can't be influenced by a user as we try to well-tune it universally to all the apps. Yet, we anticipate that apps not matching these universal rules may exist, hence we offer a way to tweak some of the `Helm's` options.

There are several options currently supported for every `Helm` action. In the next sections, you see a list of the possible customizations with code snippets to help you understand how to use them.

## Install

The installation options are exposed via the corresponding `.spec.install` field of the `App` custom resource.

### SkipCRDs

If set, no [custom resource definitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) will be installed by `Helm`. By default, those are installed if not already present. Find the example below.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  install:
    skipCRDs: true
```

### Install timeout

Time to wait for any individual `Kubernetes` operation (like `Jobs` for hooks). If not set, the default timeout of `5` minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  install:
    timeout: 10m
```

## Upgrade

The installation options are exposed via the corresponding `.spec.upgrade` field of the `App` resource.

### Upgrade timeout

Time to wait for any individual `Kubernetes` operation (like `Jobs` for hooks). If not set, the default timeout of `5` minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  upgrade:
    timeout: 10m
```

## Rollback

The installation options are exposed via the corresponding `.spec.rollback` field of the `App` resource.

### Rollback timeout

Time to wait for any individual `Kubernetes` operation (like `Jobs` for hooks). If not set, the default timeout of `5` minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  rollback:
    timeout: 10m
```

## Uninstall

The installation options are exposed via the corresponding `.spec.uninstall` field of the `App` resource.

### Uninstall timeout

Time to wait for any individual `Kubernetes` operation (like `Jobs` for hooks). If not set, the default timeout of `5` minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  uninstall:
    timeout: 10m
```
