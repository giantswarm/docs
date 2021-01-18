---
title: Defaulting and Validation of App CRs
description: How defaulting and validation of app CRs is implemented by app-admission-controller
weight: 110
type: page
last_review_date: 2020-12-16
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
---

## Overview

For Giant Swarm releases using app-operator version 3.0.0 and upwards the
defaulting and validation logic of [App CRs]({{< relref "/content/reference/management-api/apps.application.giantswarm.io.md" >}}) is enabled. This logic is provided by
[app-admission-controller](https://github.com/giantswarm/app-admission-controller).
You can check if your cluster has this version of app-operator by checking the
release details in the web interface.

We have not enabled the defaulting and validation for existing App CRs to avoid
disrupting your current usage of the App Platform.

## Defaulting

The defaulting logic is implemented using a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook). It currently
defaults the following settings in the App CR if they are not specified.

- The `app-operator.giantswarm.io/version` label that determines which instance
of app-operator processes the App CR. The value is set based on the release
version of the cluster. e.g. `3.0.0`
- The cluster values configmap that contains per cluster values like the base
domain for your cluster. e.g. `x7jwz-cluster-values`
- The kubeconfig secret that lets app-operator connect to your cluster. e.g. `x7jwz-kubeconfig`

Here is an example App CR with only the settings you need to provide. The user
values configmap is optional, in case you wish to configure the app with your
own values.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: my-kong
  namespace: x7jwz
spec:
  catalog: giantswarm
  name: kong-app
  namespace: kong
  version: 0.7.2
  userConfig:
    configMap:
      name: kong-user-values
      namespace: x7jwz
```

Here is the App CR with the defaults added by the mutating webhook.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: my-kong
  namespace: x7jwz
  labels:
    app-operator.giantswarm.io/version: 3.0.0
spec:
  catalog: giantswarm
  name: kong-app
  namespace: kong
  version: 0.7.2
  config:
    configMap:
      name: x7jwz-cluster-values
      namespace: x7jwz
  kubeConfig:
    context:
      name: x7jwz
     inCluster: false
     secret:
      name: x7jwz-kubeconfig
      namespace: x7jwz
  userConfig:
    configMap:
      name: kong-user-values
      namespace: x7jwz
```

## Validation

The validation logic is implemented using a [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook).
It checks for common problems with App CRs.

Currently we validate:

- The `app-operator.giantswarm.io/version` label is present.
- All referenced configmaps and secrets exist.
- The catalog has a matching AppCatalog CR.

## Retry Logic

During cluster creation there can a short delay while the kubeconfig
secret and cluster values configmap are generated.

So if you have an automated process for creating App CRs please ensure
it retries and the App CRs will be created once these resources exist.
