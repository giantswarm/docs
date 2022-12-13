---
linkTitle: Configuring installation process
title: Configuring Helm execution
description: Which options for the Helm execution are currently supported by the App Platform.
weight: 60
menu:
  main:
    parent: getting-started-app-platform
    identifier: getting-started-app-platform-config-install
aliases:
  - /developer-platform/app-platform/installation-configuration
  - /app-platform/installation-configuration
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2022-11-18
user_questions:
  - How can I configure custom timeouts for installations and upgrades?
---

## Overview

As stated in the [App Platform overview]({{< relref "/platform-overview/app-platform/index.md" >}}) all managed apps are
Helm Charts underneath. This of course means that at the very bottom the platform must trigger the Helm-related
actions, like installation or upgrade, against the requested application. This process, mostly, cannot be
influenced by a user as we try to well-tune it universally to all the apps. Yet, we anticipate that apps not
matching these universal rules may exist, hence we offer a way to tweak some of the Helm's options.

Next paragraphs introduce the options currently supported for each of the major Helm action, along the version of
App Operator and Chart Operator they have started to be supported with. Each paragraph comes with a short
explanation and [App CR]({{< relref "/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) code snippet with most of the fields removed for brevity.

## Install

The installation options are exposed via the corresponding `.spec.install` field of the App CR.

### SkipCRDs

#### Description

If set, no CRDs will be installed by the Helm. By default, CRDs are installed if not already present. Find the
example below.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  install:
    skipCRDs: true
```

#### Support

| Operator         | Version  |
| ---------------- | -------- |
| `app-operator`   | `v4.4.0` |
| `chart-operator` | `v2.8.0` |

### Timeout

#### Description

Time to wait for any individual Kubernetes operation (like Jobs for hooks). If not set, the default timeout of
5 minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  install:
    timeout: 10m
```

#### Support

| Operator         | Version   |
| ---------------- | --------- |
| `app-operator`   | `v6.4.0`  |
| `chart-operator` | `v2.30.0` |

## Upgrade

The installation options are exposed via the corresponding `.spec.upgrade` field of the App CR.

### Timeout

#### Description

Time to wait for any individual Kubernetes operation (like Jobs for hooks). If not set, the default timeout of
5 minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  upgrade:
    timeout: 10m
```

#### Support

| Operator         | Version   |
| ---------------- | --------- |
| `app-operator`   | `v6.4.0`  |
| `chart-operator` | `v2.30.0` |

## Rollback

The installation options are exposed via the corresponding `.spec.rollback` field of the App CR.

### Timeout

#### Description

Time to wait for any individual Kubernetes operation (like Jobs for hooks). If not set, the default timeout of
5 minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  rollback:
    timeout: 10m
```

#### Support

| Operator         | Version   |
| ---------------- | --------- |
| `app-operator`   | `v6.4.0`  |
| `chart-operator` | `v2.30.0` |

## Uninstall

The installation options are exposed via the corresponding `.spec.uninstall` field of the App CR.

### Timeout

#### Description

Time to wait for any individual Kubernetes operation (like Jobs for hooks). If not set, the default timeout of
5 minutes is used.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demo
spec:
  uninstall:
    timeout: 10m
```

#### Support

| Operator         | Version   |
| ---------------- | --------- |
| `app-operator`   | `v6.4.0`  |
| `chart-operator` | `v2.30.0` |
