---
linkTitle: App configuration
title: App configuration reference
description: Documentation on the various levels of App configuration and how they get merged into a final values object.
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-app-config
weight: 30
aliases:
  - /getting-started/app-platform/app-configuration
  - /vintage/getting-started/app-platform/app-configuration
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What tool is used to deploy applications?
  - What configurations are required on an App in order to make it ready to deploy?
  - What app configuration levels exist?
  - Why are there multiple app configuration levels?
  - What are the configuration values that I can change for Apps?
  - What is the logic behind setting the final configuration of an App?
  - What happens if I don't customize configurations?
  - What is the correct App configuration level to use?
  - What are the limitations around secrets when configuring them for an App?
  - How are configuration values stored and referenced in the Control Plane?
  - How can I provide configuration values for apps?
last_review_date: 2024-10-28
---

The Giant Swarm's [app platform]({{< relref "/overview/fleet-management/app-management" >}}) allows you to easily install apps across your entire fleet of clusters. The platform fully support [`helm`](https://helm.sh/) as a general tool to deploy your applications as well as the official Giant Swarm app catalog.

The apps are packaged as `helm` charts. Those charts rely on _values_ to be set in order to fill in placeholders in _templates_. By configuring your app you set the values that become available to the templates when they're deployed.

## Configuration levels {#levels}

There are three levels of configuration:

1. **Catalog**: Configuration provided by the publisher of the `App` catalog.
2. **Cluster**: Configuration provided by the cluster admin.
3. **User**: Configuration provided by the user installing an `App`.

Each level overrides the previous one. As a user you aren't expected to edit configuration at the `catalog` or `cluster` level. However, user level configuration can override both catalog and cluster level configuration.

Besides, there is a list of extra configuration layers with special `priority` field that you can control the level around which they will be applied to the core configurations. Head to the [extra configuration layers](#extra-configs) section to learn more about them.

Each level of configuration - same applies to extra configuration layers - has two types of values that you can provide:

1. **Configuration values**: Configuration provided as a `ConfigMap` resource.
2. **Secret values**: Configuration and credentials provided as a `Secret` resource.

All values are gathered together and merged into the final values object that will become available to the chart template.

Values are merged in the following order:

1. `Catalog` configuration values
2. `Catalog` secret values
3. `Cluster` configuration values
4. `Cluster` secret values
5. `User` configuration values
6. `User` secret values

If no value is provided then the default in the chart's values file (`values.yaml`) is used.

**Note**: Attempting to change configuration at any other level is risky because your changes might be overwritten by an operator.

## General notes about app configuration

When using app platform, it's important to remember, that most of the configuration changes in `kubernetes` are asynchronous and only eventually consistent. This also applies to `App` resources and theirs configuration. To better understand that, let's use an example where you update the application version in the `App` resource from version `v1.0.0` to `v2.0.0` and the same time you update the `ConfigMap` referenced by the `App` resource (let's call the `ConfigMap` before the change `configMap v1` and after the change `configMap v2`).

As these changes are completely independent for `kubernetes`, the following scenario is possible:

- The `App` resource is in version `v1.0.0` and `ConfigMap` is in `v1`
- Both `App` resource and the referenced `ConfigMap` are edited
- The application's version change is already processed, so the application runs in `v2.0.0` with a `ConfigMap` `v1`
- After some time, the `ConfigMap` change is processed, the application will now run in `v2.0.0` with a `ConfigMap` in version `v2`

Obviously, it can also happen that the `ConfigMap` is updated first, then the application version. The time between one and the other change being processed is usually very short, still it's important to understand, that such situations might and will happen.

## Example of values merging {#basic-values-merging-example}

Given a chart with a `values.yaml` that contains the following content:

```yaml
colors:
  background: "black"
  foreground: "white"

  # This is a secret, so we leave it blank in the Chart's values.yaml since
  # it's specific to the deployment and there is no sane default.
  secretColor: ""
```

Now you create an [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) resource that references a user level `ConfigMap` and a user level secret:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: hello-world
  namespace: i5h93
spec:
  catalog: giantswarm-playground
  ...
  name: hello-world-app
  namespace: hello-world-app
  userConfig:
    configMap:
      name: hello-world-user-values
      namespace: i5h93
    secret:
      name: hello-world-user-secrets
      namespace: i5h93
  ...
```

The `hello-world-user-values` `ConfigMap` contains the following content:

```yaml
apiVersion: v1
kind: configmap
metadata:
  name: hello-world-user-values
  namespace: i5h93
data:
  values: |
    colors:
      background: "red"
```

The `hello-world-user-secrets` secret contains this:

```yaml
apiVersion: v1
kind: secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

**Note**: when `Base64` decoding the string `.data.values` field in the secret, you'll get this:

```text
colors:
  secretColor: "blue"
```

Then the resulting values applied to the `helm` chart will be:

```yaml
colors:
  background: "red"
  foreground: "white"
  secretColor: "blue"
```

As you can see, we made an override for `.colors.background`, changing it from `black` to `red`, and set the `.colors.secretColor` value to `blue` using values from the secret.

You can use these values throughout your chart using the normal templating of `helm` charts:

```yaml
# hello-world-app/helm/chart/hello-world/templates/colors-configmap.yaml
apiVersion: v1
kind: configmap
metadata:
  name: hello-world-configmap
  namespace: {{ .Release.Namespace }}
  labels:
    app: hello-world
data:
  background: {{.Values.colors.background}}
  foreground: {{.Values.colors.foreground}}
```

```yaml
# hello-world-app/helm/chart/hello-world/templates/colors-secret.yaml
apiVersion: v1
kind: secret
metadata:
  name: hello-world-secret
  namespace: {{ .Release.Namespace }}
  labels:
    app: hello-world
data:
  secretColor: {{.Values.colors.secretColor | b64enc | quote}}
```

**Note**: If you uploaded your secret as individual plain  values and want to use one of those values in an actual templated secret, then you have to `base64` encode it to comply with how `kubernetes` stores secrets. Our API only encodes the entire secrets value string. It doesn't individually encode each value.

## How configuration values are stored {#storage-referencing}

Configuration for apps are stored as `ConfigMaps` and `Secrets`, which are referenced by `name` and `namespace` in various `spec` fields of the [`App`]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) and [`Catalog`]({{< relref "/reference/platform-api/crd/catalogs.application.giantswarm.io.md" >}}) custom resource.

Our operators act on those resources to ensure the actual state ends up looking like the desired state. More information is available in our [general overview of the app platform]({{< relref "/overview/fleet-management/app-management" >}}).

|Configuration Level|Where to set it|Fields to set|
|---|---|---|
|`catalog`|`Catalog CR`|`.spec.config.configMap.name`|
|||`.spec.config.configMap.namespace`|
|||`.spec.config.secret.name`|
|||`.spec.config.secret.namespace`|
|-|-|-|
|`app`|`App CR`|`.spec.config.configMap.name`|
|||`.spec.config.configMap.namespace`|
|||`.spec.config.secret.name`|
|||`.spec.config.secret.namespace`|
|-|-|-|
|`user`|`App CR`|`.spec.userConfig.configMap.name`|
|||`.spec.userConfig.configMap.namespace`|
|||`.spec.userConfig.secret.name`|
|||`.spec.userConfig.secret.namespace`|

## Extra configuration layers {#extra-configs}

You can set a list of extra configuration layers via `.spec.extraConfigs`. For example:

```yaml
spec:
  catalog: giantswarm-test
  extraConfigs:
    - name: hello-world-extra-values-pre-cluster
      namespace: i5h93
    - kind: secret
      name: hello-world-extra-secrets-pre-cluster
      namespace: i5h93
    - name: hello-world-extra-values-pre-user
      namespace: i5h93
      priority: 75
    - kind: secret
      name: hello-world-extra-secrets-post-user
      namespace: i5h93
      priority: 125
```

The `name` and `namespace` fields are required for each entry. However, note that it's optional to set `kind`. It defaults to `configMap`. It's also optional to set `priority`. It defaults to `25`.

The three configuration levels all have an assigned priority value bound to them behind the scenes:

1. **Catalog** has priority `0`.
2. **Cluster** has priority `50`.
3. **User** has priority `100`.

The `priority` field for `spec.extraConfigs` entries must be set to a numerical value between (inclusively) `1` and `150`.

This extends the [example of values merging](#basic-values-merging-example) section.

The base upon we merge all other layers is always the `Catalog` layer. That's why it has `priority` set to `0` and you can only set `priority` value starting from `1`.

Then for each `kind` (`configMap`, `secret`) we look up each entry and merge them in the following way:

1. The **Catalog** is the base.
2. All `spec.extraConfigs` entry with `priority` greater than the **Catalog** level and lower than or equal to the **Cluster** level are merged.
3. The **Cluster** level configurations are merged.
4. All `spec.extraConfigs` entry with `priority` greater than the **Cluster** level and lower than or equal to the **User** level are merged.
5. The **User** level configurations are merged.
6. All `spec.extraConfigs` entry with `priority` greater than the **User** level and lower than or equal to the maximum level of `150` are merged.

In case of multiple `spec.extraConfigs` entries with the same `priority` level, the order on the list is binding, with the item lower on the list being merged later (overriding those higher on the list).

### Example of merging extra configuration {#complex-values-merging-example}

Let's take the following example with just `ConfigMaps` to make it simple. The same merging algorithm applies for secrets as well.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: hello-world
  namespace: i5h93
spec:
   name: hello-world-app
   namespace: kube-system
   catalog: giantswarm
   config:
      configMap:
         name: hello-world-values
         namespace: i5h93
   extraConfigs:
      - kind: configMap
        name: hello-world-post-user
        namespace: i5h93
        priority: 125
      - kind: configMap
        name: hello-world-pre-user
        namespace: i5h93
        priority: 75
      - kind: configMap
        name: hello-world-pre-cluster
        namespace: i5h93
      - kind: configMap
        name: hello-world-final
        namespace: i5h93
        priority: 125
      - kind: configMap
        name: hello-world-high-priority
        namespace: i5h93
        priority: 10
   userConfig:
      configMap:
         name: hello-world-app-user-values
         namespace: i5h93
```

The merge order for `ConfigMaps` (with `P` as the indicated or calculated priority) will be:

1. `Catalog` (P = 0)
2. `Configmap`: `hello-world-high-priority` (P = 10)
3. `Configmap`: `hello-world-pre-cluster` (P = 25)
4. `Configmap`: `hello-world-values` (P = 50)
5. `Configmap`: `hello-world-pre-user` (P = 75)
6. `Configmap`: `hello-world-app-user-values` (P = 100)
7. `Configmap`: `hello-world-post-user` (P = 125, position in the list: `1)
8. `Configmap`: `hello-world-final` (P = 125, position in the list: 4)

## Format of values in ConfigMap and Secret {#values-format}

The `ConfigMap` and `Secret` must contain a `.data.values` key, under which all configuration values are kept, as a string of valid YAML. For secrets, the string must be `base64` encoded, as is required by `kubernetes`.

> In this context, the secret is used to populate the values file with secret information, it's not used to create secrets on the workload cluster.

### Example ConfigMap

```yaml
apiVersion: v1
kind: configmap
metadata:
  name: hello-world-user-values
  namespace: i5h93
data:
  values: |
    colors:
      background: "red"
```

### Example secret

```yaml
apiVersion: v1
kind: secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

## Applying configuration values

There are many approaches to apply resources in `kubernetes`, which go beyond the scope of this article. You can test the examples by running `kubectl apply` to the platform API. For more advanced use cases, we advocate using [GitOps]({{< relref "/tutorials/continuous-deployment/what-is-gitops" >}}) to maintain your configuration in a `Git` repositories always in sync with your clusters.

**Note**: Depending on your installation you might not have access to the platform API yet. Please contact your account engineer if you would like more information about that or follow [the getting started page to learn how to configure it]({{< relref "/getting-started/access-to-platform-api" >}}).
