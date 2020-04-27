---
title: App Configuration
description: Documentation on the various levels of App configuration and how they get merged into a final Values object.
date: 2020-04-27
type: subsection
---

# App Configuration Reference

Giant Swarm's [App Platform](/basics/app-platform/) allows you to easily install Apps across your entire
fleet of clusters. We fully support Helm as a general tool to deploy your applications as well as for our general app catalogue, which you can of course also use for your own applications by creating a new catalogue.

Apps are packaged as Helm charts. Helm charts rely on _values_ to be set in order to fill in placeholders in _templates_. By configuring your App you set the values that become available to the templates when they are deployed.

## Configuration levels {#levels}

There are three levels of configuration:

1. **Catalog**: Configuration provided by the publisher of the App Catalog.
2. **Cluster**: Configuration provided by the cluster admin.
3. **User**: Configuration provided by the user installing an App.

Each level can override the previous one. As a user you are not expected to edit configuration at the `catalog` or `cluster` level. However user level configuration can override both catalog and cluster level configuration.

Each level of configuration has two types of values that you can provide:

1. **Config values**: Configuration provided as a ConfigMap resource.
2. **Secret values**: Configuration and credentials provided as a Secret resource.

All values are gathered together and merged into the final values
object that will become available to the chart template.

Values are merged in the following order:

1. Catalog config values
2. Catalog secret values
3. Cluster config values
4. Cluster secret values
5. User config values
6. User secret values

If no value is provided then the default in the chart's values file (`values.yaml`) is used.

**Note:** Attempting to change configuration at any other level is risky because your changes
might be overwritten by an operator. That is why our web interface is only able to set user level configuration values.

## Example of values merging

Given a chart with a `values.yaml` that contains the following content:

```yaml
colors:
  background: "black"
  foreground: "white"

  # This is a secret, so we leave it blank in the Chart's values.yaml since
  # it is specific to the deployment and there is no sane default.
  secretColor: ""
```

Now you create an [App](/reference/cp-k8s-api/apps.application.giantswarm.io/) resource that references a user level ConfigMap and a `user`
level Secret:

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

The `hello-world-user-values` ConfigMap contains the following content:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-world-user-values
  namespace: i5h93
data:
  values: |
    color:
      background: "red"
```

The `hello-world-user-secrets` Secret contains this:

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

**Note:** when Base64-decoding the string `.data.values` field in the secret, you'll get this:

```nohighlight
color:
  secretColor: "blue"
```

Then the resulting values applied to the Helm chart will be:

```yaml
colors:
  background: "red"
  foreground: "white"
  secretColor: "blue"
```

As you can see, we made an override for `.colors.background`, changing it from
`black` to `red`, and set the `.colors.secretColor` value to `blue` using values from the Secret.

You can use these values throughout your chart using the normal templating of
Helm charts:

```yaml
# hello-world-app/helm/chart/hello-world-app/templates/colors-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-world-configmap
  namespace: {{ .Release.Namespace }}
  labels:
    app: hello-world
data:
  background: {{.Values.colors.background}}
  foreground: {{.Values.colors.foreground}}

# hello-world-app/helm/chart/hello-world-app/templates/colors-secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: hello-world-secret
  namespace: {{ .Release.Namespace }}
  labels:
    app: hello-world
data:
  secretColor: {{.Values.colors.secretColor | b64enc | quote}}
```

**Note:** If you uploaded your secret as individual plaintext values and want to use one of those values in an actual
templated Secret, then you have to base64 encode it to comply with how Kubernetes stores secrets. Our API only encodes the entire secrets value string. It does not individually encode each value.

## How configuration values are stored and referenced in the Control Plane {#storage-referencing}

Configuration for Apps are stored as ConfigMaps and Secrets, which are
referenced by `name` and `namespace` in various `spec` fields of the [App](/reference/cp-k8s-api/apps.application.giantswarm.io/) and [AppCatalog](/reference/cp-k8s-api/appcatalogs.application.giantswarm.io/) Custom Resource (CR).

Our operators act on those resources to ensure the actual state ends up
looking like the desired state. More information is available in our [general overview of the App Platform](/basics/app-platform/).

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

When setting user level configuration using the Giant Swarm API or our [web interface](/reference/web-interface/),
the fields in the App CR are edited automatically for you while creating
the `ConfigMap` or `Secret`.

## Format of values in ConfigMap and Secret {#values-format}

The `ConfigMap` and `Secret` must contain a `.data.values` key, under which all configuration
values are kept, as a String of valid YAML. For Secrets, the string must be
base64 encoded, as is required by Kubernetes. When uploading values via the
Giant Swarm API, the base64 encoding is done for you.

### Example ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: hello-world-user-values
  namespace: i5h93
data:
  values: |
    color:
      background: "red"
```

### Example Secret

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

## Setting configuration values

There are three ways to provide configuration values:

- via the web interface
- via the Giant Swarm (Rest) API
- via the Control Plane Kubernetes API

### Through the Web Interface

Our web interface allows you to upload configuration and secret values for the
user configuration level. You can do this by uploading a YAML file consisting
of just the keys and values you would like to set.

The web interface currently talks to the Giant Swarm API and will do the right
calls to create a ConfigMap or Secret and will wire it up correctly in the App CR
for you.

The hello-world-app examples shown above could be configured by the following
YAML files using the web interface. Notice that no ConfigMap or Secret metadata
is required. You only have to supply the `values` part as a valid YAML file, with
no encoding.

#### hello-world user values example

```yaml
color:
   background: "red"
```

#### hello-world user secrets example

```yaml
color:
   secretColor: "blue"
```

### Using the Giant Swarm API (Deprecated) {#giant-swarm-api}

The Giant Swarm API acts as an interface between you and the Control Plane Kubernetes
API.

It is deprecated since we are currently in the process of allowing you direct
access to the Control Plane Kubernetes API.

However for the time being, our Web Interface makes use of the Giant Swarm API.

By supplying a JSON body with the values you would like to set, the Giant Swarm API will
create a ConfigMap or Secret in the right format and wire it up correctly for you.

- [Giant Swarm API App Configs reference](https://docs.giantswarm.io/api/#tag/app-configs) for adding configuration values
- [Giant Swarm API App Secrets reference](https://docs.giantswarm.io/api/#tag/app-secrets) for adding secret values

### Using the Control Plane Kubernetes API {#cp-k8s-api}

There are many approaches to managing resources in Kubernetes, that goes beyond
the scope of this resource page.

But the simplest would probably be to `kubectl apply` a file directly to the cluster.

_Note: Depending on your installation you might not have access to the Control Plane API yet.
Please contact your SE if you would like more information about that._
