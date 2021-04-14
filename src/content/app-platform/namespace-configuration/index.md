---
linkTitle: App namespace metadata
title: App's namespace metadata
description: Documentation on how to labelling, annotating the app CR's namespace
menu:
  main:
    parent: app-platform
weight: 20
aliases:
- /reference/app-configuration/
  owner:
- https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I label the app CR's namespace?
  - How can I annotate the app CR's namespace?
---

# App CR's namespace configuration

At some point, you might want to put the specific labels or annotations to the app's namespace to bring benefits from `linkerd` or `kiam`.
This feature enables you to add labels and annotations to the app's namespace by updating [App CRs]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}).

## Configuring the App CR's namespace

### Updating labels/annotations

You can use `.spec.namespaceConfig` to update the namespace metadata. You can either choose `.spec.namespaceConfig.lables` or
`spec.namespaceConfig.lables` and give values as a key/value map. App platform would ensure this metadata into the namespace.

For example, if you want to add an annotation `linked.io/inject: enabled` into the namespace `loki1`, try as below.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: loki-app
  namespace: loki0
spec:
  catalog: giantswarm
  name: loki
  namespace: loki
  namespaceConfig:
    annotations:
      linkerd.io/inject: "enabled"
```

Now you can check the namespace and the namespace `loki0` would be the same as below.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    linkerd.io/inject: "enabled"
  name: giantswarm
```

If you want to update annotations in the namespace, use `spec.namespaceConfig.annotation` as below.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: kiam-app
  namespace: kiam0
spec:
  catalog: giantswarm
  name: kiam
  namespace: kiam
  namespaceConfig:
    labels:
      monitoring: "enabled"
```

### Validation in App CR's Namespace Config

In [default validation logic]({{< relref "/app-platform/default-validation" >}}), app-admission-controller checks whether multiple app CRs are updating the same namespace with the same key,
but different values. This logic would avoid the situation where the same namespace keeps changing at each app CR's reconciliation.
