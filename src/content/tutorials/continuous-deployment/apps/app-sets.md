---
linkTitle: Creating and using App Sets
title: Creating and using App Sets
description: Learn how to create and use App Sets for applications deployed with GitOps.
weight: 50
menu:
  principal:
    identifier: tutorials-continuous-deployment-apps-sets
    parent: tutorials-continuous-deployment-apps
user_questions:
  - How can I create and use `App Sets` in GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-19
---

This document is part of the documentation to use GitOps with Giant Swarm app platform. You can find more information about the [app platform in our docs]({{< relref "/overview/fleet-management/app-management/" >}}).

# Creating app sets

It's often desirable to deploy a group of apps together, as a single deployment step. In Giant Swarm, it's called `App Sets`. There's nothing special about `App Sets`: they aren't a separate API entity, but rather just a configuration pattern enabled by [`Kustomize`](https://kustomize.io/) and [`Flux`](https://fluxcd.io/flux/). The purpose brings you the following benefits:

- Apps within the set have strong relationship and dependency on versions and you want to be sure that the correct versions are used and deployed together.
- The configuration of apps in an `App Set` could be shared. By placing them together it's possible to simplify the configuration of one app by providing values known to depend on another. As a result, it's easier to deploy an `App Set` than each of the apps individually. That way a specialized team might deliver a pre-configured `App Set` so that it's easy and understandable to deploy be a less proficient end user.

## Limitations

Even though `App Sets` have a lot of benefits, their implementation with `Kustomize` and `Flux` is limited. The main limitation is that `Kustomize` isn't a templating engine. It can't replace a value in an arbitrary place in a YAML file. It can only replace whole values or whole blocks of YAML.

In general, it's impossible to configure a variable once and use it with multiple apps. You have two choices:

- Every app within the set shares exactly the same `ConfigMap` or `Secret` as a `config` attribute.
- Use two separate `ConfigMaps`. In this case, it's your responsibility to provide exactly the same value in both places. It means the apps will receive same configuration layout and must avoid conflict options. In practice, the apps must be prepared on the `Helm` chart layer to work together.

__Note__: As an alternative, you can use `Helm` umbrella chart to deploy multiple apps together, also known as [`Helm` chart dependencies](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/).

## Example

### App set template

An example of an `App Set` template is available in the [gitops-template repository in `bases/app_sets/hello-web-app`](https://github.com/giantswarm/gitops-template/tree/main/bases/app_sets/hello-web-app/). In this example, the `App Set` takes the second approach, and creates two different `ConfigMap` files for each app and replace the `ConfigMap` name in the `App` resource.

### Using app sets

An example showing how to use an `App Set` is available in the [gitops-template repository in `WC_NAME/app_sets/hello-web-app-1`](https://github.com/giantswarm/gitops-template/tree/main/management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/WC_NAME_OUT_OF_BAND_NO_FLUX_APP/mapi/app_sets/hello-web-app-1). You can observe how a `ConfigMap` is automatically created using a override configuration file. Also, you see `patchesStrategicMerge` that replaces the `ConfigMap` name in the `App` resource.

## Creating an app set template

Creating an `App Set` template isn't much different than [creating an app template]({{< relref "/tutorials/continuous-deployment/apps/add-app-template" >}}). Please make sure to read the documentation first.

To get started, go to the `bases` directory and create a subdirectory for your `App Set` template. In the directory, create a `kustomization.yaml` similar to the one below:

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

- You can use the `gitops.giantswarm.io/appSet: YOUR_NAME` label to  identify all the components included in the `App Set`. It makes debugging easier later, as you can easily find what belongs to the Set after it's deployed.
- One of the key benefits of `App Sets` is to be able to provide a specific set of app versions, that's known to make the apps work well together. To achieve that you see a set of in-line patches exposing the versions of the apps.
- When using `App` resources, you have three configuration slots available: `config`, `extraConfigs` and `userConfig`. Learn more about them in the [app configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}) documentation.
- It's recommended to re-use app templates to create `App Set` templates. You can observe the apps defined in the `resources:`  are `App` templates, that can be also used standalone.
- Secrets can be created the same way as explained in the [app templates]({{< relref "/tutorials/continuous-deployment/apps/add-app-template" >}}) and override the same as `ConfigMaps` or secrets when creating [App from a Template]({{< relref "/tutorials/continuous-deployment/apps/add-appcr/#adding-app-using-app-template" >}}).

## Use an app set

Using an `App Set` template is similar to use a single [`App Set`]({{< relref "/tutorials/continuous-deployment/apps/add-appcr#adding-app-using-app-template" >}}). To create one, save a path that contains your desired `App Set` template in the [gitops-template repository in "bases/app_sets"](https://github.com/giantswarm/gitops-template/tree/main/bases/app_sets/) directory. Then, create a new directory in the `app_sets` directory of your working cluster. In that directory, create a `kustomization.yaml` file based on the following pattern:

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

Above you can see how it's override the configuration of the `hello-world` app from the original template. The configuration replaces the `extraConfigs` property using the values from `override_config_hello_world` YAML file. This modifies the keys that match from original template definition. Notice the example overwrites the `namespace` as well for the whole app deployment. If you want to learn more about how configuration overrides work, please read our [docs about creating apps]({{< relref "/tutorials/continuous-deployment/apps/add-appcr" >}}).
