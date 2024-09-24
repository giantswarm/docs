---
linkTitle: Creating and using `App Sets`
title: Creating and using `App Sets`
description: Learn how to create and use `App Sets` for applications deployed with GitOps.
weight: 50
aliases:
  - /advanced/gitops/apps
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-sets
    parent: tutorials-continuous-deployment-apps
last_review_date: 2024-09-25
user_questions:
  - How can I create and use `App Sets` in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [App Platform in our docs]({{< relref "overview/fleet-management/app-management/" >}}).

# Creating and using app sets

It's often desirable to deploy a group of apps together, as a single deployment step. We call such groups `App Sets`. There's nothing special about `App Sets`: they aren't a separate API entity, but rather just a configuration pattern enabled by [Kustomize](https://kustomize.io/) and [Flux](https://fluxcd.io/flux/). The purpose of such an approach can vary, but it's usually to meet the following benefits:

- Apps within the set have strong relationship and dependency on versions and you want to be sure that the correct versions are used and deployed together.
- The configuration of apps in an `App Set` could be shared. By placing them together it's possible to simplify the configuration of one app by providing values known to depend on another. As a result, it's easier to deploy an `App Set` than each of the apps individually. That way a specialized team might deliver a pre-configured `App Set` so that it's easy and understandable to deploy be a less proficient end user.

## Limitations

Even though `App Sets` have a lot of benefits, their implementation with `kustomize` and `flux` is pretty limited. Please make sure that you read this section before deciding to implement `App Sets` the way they're described here.

In general, the whole problem can be summarized as `kustomize` isn't a templating engine. It can override some values, even in bulks, but it can't put the same value in any arbitrary place.

In the common case, it's impossible to configure a variable once and use it with multiple apps. There are only two choices here: either each pair of apps shares exactly the same configmap or secret as a `config:` attribute of an App CR or they use two separate configmaps. In the latter case, it's your responsibility to provide exactly the same value in both configmaps or secrets. In the former, it means that your apps share the same configuration input and must be able to handle this situation correctly: there can be no conflicting options and each shared option must be understood exactly the same by each app. In practice, it means that the apps must be prepared on the Helm chart layer to work together.

If none of these two solutions is applicable, you might want to solve the problem of bundling the apps together elsewhere. One of possible routes is to create a new umbrella Helm Chart that includes all the necessary apps as [sub-charts](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

## Example

### App set template

An example of an `App Set` template is available in the [gitops-template repository in `bases/app_sets/hello-web-app`](https://github.com/giantswarm/gitops-template/tree/main/bases/app_sets/hello-web-app/). This `App Set` assumes, that it's impossible to build a shared configmap for both Apps and as such does full configuration override on `App Set` template level and override using `userConfig:` field in `App Set` instance.

### Using app sets

An example showing how to use an `App Set` is available in the [gitops-template repository in `WC_NAME/app_sets/hello-web-app-1`](https://github.com/giantswarm/gitops-template/tree/main//management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME/app_sets/hello-web-app-1).

## Creating an app set template

Creating an `App Set` template isn't much different than [creating an spp template](/advanced/gitops/apps/add_app_template/). Please make sure to read the documentation first.

To get started, go to the `bases` directory and create a subdirectory for your `App Set` template. In this directory, create a `kustomization.yaml` similar to the one below:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
commonLabels:
  gitops.giantswarm.io/appSet: hello-web-app # this label will be applied to all resources included in the `App Set`
# (optional) replace default config of apps included in the set
configMapGenerator:
  - behavior: replace
    files:
    - values=default_config_simple_db.yaml
    name: ${cluster_name}-simple-db-values # has to be in sync with the name used by included app
  - behavior: replace
    files:
    - values=default_config_hello_world.yaml
    name: ${cluster_name}-hello-world-values # has to be in sync with the name used by included app
# block end
kind: Kustomization
namespace: hello-web # (optional) enforce the same namespace for all the apps in the set
# (optional) here we can enforce versions for both apps that we know work well together
patches:
  - patch: |-
      - op: replace
        path: /spec/version
        value: 0.1.9
    target:
      kind: App
      name: hello-world
  - patch: |-
      - op: replace
        path: /spec/version
        value: 0.1.1
    target:
      kind: App
      name: simple-db
# block end
resources:
  - ../../apps/hello-world
  - ../../apps/simple-db
```

Please note the following in the example above:

- We use the `gitops.giantswarm.io/appSet: YOUR_NAME` that will identify all the components included in the `App Set`. This makes debugging easier later, as you can easily find what belongs to the Set after it's deployed.
- One of the key benefits of `App Sets` is to be able to provide a specific set of app versions, that's known to make the apps work well together. Over here, we do that as a set of in-line patches, so it's immediately visible in the `kustomization.yaml` file which versions are used.
- When using `App` CRs, we've two configuration slots available: `config` and `userConfig`. Since we always want to leave `userConfig` at the end users disposal, we're left with overriding the whole configmap coming from the base application as the only option.
- It's recommended to re-use App Templates to create `App Set` Templates. That's exactly what we do here: apps defined in the `resources:` block are App Templates, that, if needed, can be also used standalone.
- The example above doesn't cover handling secrets - we do that for brevity. secrets can be created the same way as in normal [App Templates](./add_app_template.md) and overrode the same as configmaps or secrets when creating [App from a Template](/advanced/gitops/apps/add_appcr/#adding-app-using-app-template).

## Using an app set

Using an `App Set` Template is once again very similar to using a single [App Set](/advanced/gitops/apps/add_appcr/#adding-app-using-app-template). To create one, save a path that contains your desired `App Set` Template in the [gitops-template repository in "bases/app_sets"](https://github.com/giantswarm/gitops-template/tree/main/bases/app_sets/) directory. Then, create a new directory in the `app_sets` directory of your Working Cluster. In that directory, create a `kustomization.yaml` file based on the following pattern:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
configMapGenerator:
  - files:
      - values=override_config_hello_world.yaml
    name: ${cluster_name}-hello-world-user-values
generatorOptions:
  disableNameSuffixHash: true
kind: Kustomization
namespace: hello-web-team1
patchesStrategicMerge:
  - config_patch.yaml
resources:
  - ../../../../../../../../../bases/app_sets/hello-web-app
```

Over here, we're overriding the configuration of the `hello-world` app, which was already defined in the `App Set` Template. Since here we're using the `userConfig` property, we don't have to override the whole configuration, but only the YAML keys we need to change. One more important fact is that we're setting a custom Namespace for the whole deployment of an app. If you want to learn more about how configuration overrides work, please consult our [docs about creating apps](/advanced/gitops/apps/add_appcr/), as in general `App Set` is just a bundle of them.
