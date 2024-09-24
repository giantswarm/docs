---
linkTitle: Defaulting and validation
title: Defaulting and validation of App CRs
description: How defaulting and validation of app CRs is implemented by app-admission-controller.
weight: 50
menu:
  principal:
    parent: tutorials-app-platform
    identifier: tutorials-app-platform-default-validation
last_review_date: 2023-06-26
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /getting-started/app-platform/defaulting-validation
  - /reference/app-defaulting-validation/
  - /app-platform/defaulting-validation
  - /developer-platform/app-platform/defaulting-validation
user_questions:
  - Is App CR defaulting and validation logic enabled for my cluster?
  - How can I use App CR defaulting logic when installing Managed Apps?
  - What fields are validated in App CRs when installing or updating Managed Apps?
  - How can I ensure Flux is not blocked by the validating webhook?
last_review_date: 2024-09-25
---

## Overview

For Giant Swarm releases using app-operator version 3.0.0 and upwards the
defaulting and validation logic of [App CRs]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) is enabled.
This is the following releases:

- AWS >= v14.0.0
- Azure >= v13.1.0
- KVM >= v13.1.0

This logic is provided by
[app-admission-controller](https://github.com/giantswarm/app-admission-controller).
You can check if your cluster has this version of app-operator by checking the release details in the web interface.

We've not enabled the defaulting and validation for existing App CRs to avoid disrupting your current usage of the app platform.

## Defaulting

The defaulting logic is implemented using a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook). It currently defaults the following settings in the App CR if they're not specified.

- The `app-operator.giantswarm.io/version` label - It determines which instance of app operator processes the App CR. The value is set based on the release version of the cluster. For example `3.0.0`.
- The cluster values configmap - It contains per cluster values like the base domain for your cluster. For example `x7jwz-cluster-values`.
- The kubeconfig secret - It lets app-operator connect to your cluster. For example `x7jwz-kubeconfig`

Here is an example App CR with only the settings you need to provide. The user values configmap is optional, in case you wish to configure the app with your own values.

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
- The catalog has a matching Catalog CR.
- There is no App CR with a conflicting annotation or label value for the [target namespace]({{< relref "/tutorials/app-platform/namespace-configuration" >}}).

If app-operator finds a matching [AppCatalogEntry]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) CR, it will use this to run more validation checks.

- Cloud provider compatibility (For example you can’t install the azure-ad-pod-identity app in AWS).
- Namespace restriction (cluster singleton, namespace singleton, fixed namespace).

## Skipping Configuration Validation

If you are managing your `App` CRs by the means of a third party tool (For example Flux) then the
validating webhook may block creation of the App CR if it's created before the referenced configmap or secret.

To prevent this you can add the label `giantswarm.io/managed-by` and set the value to the tool you're using for example `flux` or `helm`. If you aren't using a particular tool to deploy your resources but find the validation blocking you, you may also set this to some other value, for example `external`, to allow your CRs to be created regardless. See example below, note, some fields have been removed for brevity.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: my-app
  namespace: w0xyz
  labels:
    giantswarm.io/managed-by: flux
spec:
  userConfig:
    configMap:
      name: my-app-userconfig
      namespace: w0xyz
```

The `app-admission-controller` will now allow the App CR to be created despite the referenced `my-app-userconfig` doesn't exist. The app operator will still perform the validation checks and once the referenced ConfigMap or secret exists the app will be installed.

## Retry Logic

During cluster creation there can a short delay while the kubeconfig
secret and cluster values configmap are generated.

So if you have an automated process for creating App CRs please ensure
it retries and the App CRs will be created once these resources exist.
