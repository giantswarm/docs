---
linkTitle: Defaulting and validation
title: Defaulting and validation of App CRs
diataxis_content_type: explanation
description: How defaulting and validation of app CRs is implemented by app-admission-controller.
weight: 40
aliases:
  - /getting-started/app-platform/defaulting-validation
  - /vintage/getting-started/app-platform/defaulting-validation
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-default-validation
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - Is App custom resource defaulting and validation logic enabled for my cluster?
  - How can I use App custom resource defaulting logic when installing Managed Apps?
  - What fields are validated in App custom resources when installing or updating Managed Apps?
  - How can I ensure flux is not blocked by the validating webhook?
last_review_date: 2024-10-28
---

The Giant Swarm applications use a defaulting and validation logic for the [`App` custom resources]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) to enhance the user experience and prevent common mistakes.

This logic is provided by [`app-admission-controller`](https://github.com/giantswarm/app-admission-controller). When you create or update an `App` resource, the controller will ensure that the resource is correctly configured and will default some fields based on the cluster configuration.

**Deprecated:** This page documents webhook-based defaulting and validation for the legacy `App` custom resource. Flux HelmRelease has no equivalent webhook layer. Every field the App CR webhook would default has to be set on the HelmRelease. In exchange you get more flexibility and fewer moving parts. See the [HelmRelease equivalent](#helmrelease) section below.

## HelmRelease equivalent {#helmrelease}

There is no `app-admission-controller` for HelmRelease. Flux's helm-controller and source-controller handle basic admission through OpenAPI schemas, but Giant Swarm-specific defaulting (cluster values, kubeconfig, operator-version routing) doesn't apply. What changes for HelmRelease users:

- **Cluster values.** The `<cluster>-cluster-values` `ConfigMap` is created in the organization namespace alongside the cluster. To consume it from a HelmRelease, reference it in `spec.valuesFrom`:

  ```yaml
  spec:
    valuesFrom:
      - kind: ConfigMap
        name: dev01-cluster-values
  ```

- **`kubeconfig`.** The `<cluster>-kubeconfig` Secret is created for you alongside the cluster. Reference it from the HelmRelease via `spec.kubeConfig.secretRef.name` so Flux installs the chart into the workload cluster.
- **App-operator version label.** Not applicable. Flux's helm-controller handles all releases, so there's no per-cluster operator routing to default.
- **Catalog match.** Not applicable. Your HelmRelease's `chartRef` points at an `OCIRepository`, `HelmRepository`, or other Flux source. There's no separate `Catalog` resource to validate against.
- **Skipping validation (`giantswarm.io/managed-by: flux` label).** Not needed. There's no validating webhook on HelmRelease that needs bypassing for Flux-managed resources.
- **Order-of-creation issues.** Flux retries on missing dependencies. If a HelmRelease references a `ConfigMap` that doesn't exist yet, Flux waits and reconciles when it appears. Use `dependsOn` for explicit ordering between releases. See [Group multiple HelmReleases together]({{< relref "/tutorials/continuous-deployment/helm-releases/multiple-releases" >}}).

For a worked HelmRelease example with all these fields wired up, see [Add a HelmRelease to a workload cluster]({{< relref "/tutorials/continuous-deployment/helm-releases/add-helmrelease" >}}).

The remainder of this page covers the App CR defaulting and validation webhook in detail.

## Defaulting

The defaulting logic is implemented using a [mutating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#mutatingadmissionwebhook). It currently defaults the following settings in the `App` resource if they're not specified.

- The `app-operator.giantswarm.io/version` label - It determines which instance of app operator processes the `App` resource. The value is set based on the release version of the cluster.
- The cluster values `ConfigMap` - It contains per cluster values like the base domain for your cluster.
- The `kubeconfig` `Secret` - It lets app operator connect to your cluster.

In the following example, there is an `App` resource only with the basic settings you need to provide. The user values `ConfigMap` is optional, in case you wish to configure the app with your own values.

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

Next is the `App` resource with the defaults added by the mutating webhook.

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

The validation logic is implemented using a [validating admission webhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook). It checks for common problems with `App` resources.

Currently we validate:

- The `app-operator.giantswarm.io/version` label is present.
- All referenced `ConfigMaps` and `Secrets` exist.
- The catalog has a matching `Catalog` custom resource.
- There is no `App` resource with a conflicting annotation or label value for the [target namespace]({{< relref "/tutorials/fleet-management/app-platform/namespace-configuration" >}}).

If app operator finds a matching [`AppCatalogEntry`]({{< relref "/reference/platform-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) custom resource, it will use this to run more validation checks.

- Cloud provider compatibility (For example you can’t install the `azure-ad-pod-identity` app in AWS cluster).
- Namespace restriction (cluster singleton, namespace singleton, fixed namespace).

## Skipping configuration validation

If you are managing your `App` resource by the means of a third party tool (for example `flux`) then the
validating webhook may block creation of the `App` resource if it's created before the referenced `ConfigMap` or `Secret`.

To prevent this you can add the label `giantswarm.io/managed-by` and set the value to the tool you're using for example `flux` or `helm`. If you aren't using a particular tool to deploy your resources but find the validation blocking you, you may also set this to some other value, for example `external`, to allow your custom resource to be created regardless. See example below, note, some fields have been removed for brevity.

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

The `app-admission-controller` will now allow the `App` resource to be created despite the referenced `my-app-userconfig` doesn't exist. The app operator will still perform the validation checks and once the referenced `ConfigMap` or `Secret` exists the app will be installed.

## Retry Logic

During cluster creation there can a short delay while the `kubeconfig` `Secret` and cluster values `ConfigMap` are generated.

So if you have an automated process for creating `App` resources please ensure it retries till the infrastructure is provisioned.
