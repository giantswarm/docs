---
title: App Configuration
description: Documentation on the various levels of App configuration and how they get merged into a final Values object.
date: 2020-04-02
type: subsection
---

# App Configuration Reference

Giant Swarm's App Catalog allows you to easily install Apps across your entire
fleet of clusters. Currently, Apps are packaged as Helm charts. By configuring
your App you set the `Values` that become available to the templates when they
are deployed.

There are three levels of configuration:

`catalog`, `app`, and `user`.

Each level of configuration has two types of values that you can provide:

`config-values` and `secret-values`.

All values are gathered together and merged into the final `Values`
object that will become available to the Chart template.

Values are merged in the following order:

1. `catalog-config-values`
2. `catalog-secret-values`
3. `app-config-values`
4. `app-secret-values`
5. `user-config-values`
6. `user-secret-values`

If no value is provided then the default in the Chart's `values.yaml` is used.

As a user of the App Catalog you will most likely not come into contact with
the `catalog` and `app` level of configuration. Our interfaces make it
easiest to set `user` level configuration values.

## Example of Values merging

Given a chart with a `values.yaml` that contains the following

```
colors:
  background: "black"
  foreground: "white"

  # This is a secret, so we leave it blank in the Chart's values.yaml since
  # it is specific to the deployment and there is no sane default.
  secretColor: ""
```

If you create an `App CR` that references a `user` level ConfigMap and a `user`
level Secret:

```
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

And the `hello-world-user-values` ConfigMap contains:

```
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

And the `hello-world-user-secrets` Secret contains:

```
apiVersion: v1
kind: Secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

The `values` field contains a base64 encoded yaml string:

```
$ echo -n "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo=" | base64 -D
color:
  secretColor: "blue"
```

Then the resulting `Values` will be:

```
colors:
  background: "red"
  foreground: "white"
  secretColor: "blue"
```

As you can see, we made an override for the background color, changing it from
`black` to `red`, and set the `secretColor` to `blue` using values from the Secret.

And you can use these values throughout your chart using the normal templating of
Helm charts:

```
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

_Note: If you uploaded your secret as individual plaintext values and want to use one of those values in an actual
templated Secret, then you have to base64 encode it to comply with how Kubernetes stores secrets._

_Our API only encodes the entire secrets value string. It does not individually encode each
value_


## How are configuration values stored and referenced in the Control Plane?

Configuration for `Apps` are stored as `ConfigMaps` and `Secrets`, which are
referenced by `name` and `namespace` in various `spec` fields of the `App` and `AppCatalog` Custom Resource.

Our operators act on those resources to ensure the actual state ends up
looking like the desired state. More information is available in a [general overview of the App Catalog](/basics/app-catalog/).

|Configuration Level|Where to set it|Fields to set|
|---|---|---|
|`catalog`|`Catalog CR`|`spec.config.configMap.name`|
|||`spec.config.configMap.namespace`|
|||`spec.config.secret.name`|
|||`spec.config.secret.namespace`|
|-|-|-|
|`app`|`App CR`|`spec.config.configMap.name`|
|||`spec.config.configMap.namespace`|
|||`spec.config.secret.name`|
|||`spec.config.secret.namespace`|
|-|-|-|
|`user`|`App CR`|`spec.userConfig.configMap.name`|
|||`spec.userConfig.configMap.namespace`|
|||`spec.userConfig.secret.name`|
|||`spec.userConfig.secret.namespace`|

When setting user level configuration using the Giant Swarm API or our Web Interface,
the fields in the `App CR` are edited automatically for you while creating
the `ConfigMap` or `Secret`.

## What is the right format for values in the ConfigMap and Secret?

The `ConfigMap` and `Secret` must contain a `values` key, under which all configuration
values are kept, as a String of valid YAML. For Secrets, the string must be
base64 encoded, as is required by Kubernetes. When uploading values via the
Giant Swarm API, the base64 encoding is done for you.

#### Example ConfigMap:

```
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


#### Example Secret:

```
apiVersion: v1
kind: Secret
metadata:
  name: hello-world-user-secrets
  namespace: i5h93
data:
  values: "Y29sb3I6CiAgc2VjcmV0Q29sb3I6ICJibHVlIgo="
```

## How to provide configuration values

There are 3 ways to provide configuration values.

### Through the Web Interface

Our web interface allows you to upload configuration and secret values for the
`user` configuration level. You can do this by uploading a yaml file consisting
of just the keys and values you would like to set.

The web interface currently talks to the Giant Swarm API and will do the right
calls to create a ConfigMap or Secret and will wire it up correctly in the `App CR`
for you.

The previous hello-world-app examples could be configured by the following
yaml files using the Web Interface. Notice that no ConfigMap or Secret metadata
is required. You only have to supply the `values` part as a valid yaml file, with
no encoding.

#### hello-world user values example:

```
color:
   background: "red"
```

#### hello-world user secrets example:

```
color:
   secretColor: "blue"
```

### Using the Giant Swarm API (Deprecated)

The Giant Swarm API acts as an interface between you and the Control Plane Kubernetes
API.

It is deprecated since we are currently in the process of allowing you direct
access to the Control Plane Kubernetes API.

However for the time being, our Web Interface makes use of the Giant Swarm API.

By supplying a JSON body with the values you would like to set, the Giant Swarm API will
create a ConfigMap or Secret in the right format and wire it up correctly for you.

- See our API for adding configuration values: https://docs.giantswarm.io/api/#tag/app-configs
- See our API for adding secret values: https://docs.giantswarm.io/api/#tag/app-secrets

### Applying ConfigMaps and Secrets directly to the Control Plane

There are many approaches to managing resources in Kubernetes, that goes beyond
the scope of this resource page.

But the simplest would probably be to `kubectl apply` a file directly to the cluster.

_Note: Depending on your installation you might not have access to the Control Plane API yet.
Please contact your SRE if you would like more information about that._