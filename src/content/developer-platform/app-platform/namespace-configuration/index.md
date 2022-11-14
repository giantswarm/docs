---
linkTitle: Target namespace metadata
title: Configure an app's target namespace via its App CR
description: How to configure metadata for the target namespace of an app via its app CR. So it can be used by other tools such as service meshes.
weight: 60
menu:
  main:
    parent: developer-platform-app-platform
aliases:
  - /app-platform/namespace-configuration
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2021-07-07
user_questions:
  - How can I label an app CR's target namespace?
  - How can I annotate an app CR's target namespace?
---

## Overview

At some point, you might want to add specific labels or annotations to an app's target namespace to enable other tools such as `linkerd` or `kiam`. For example, to include all pods in a namespace in the `linkerd` service mesh. Or, to tell `kiam` you do allow Loki to get logs from pods running in this namespace.
This feature enables you to add labels and annotations to the app's target namespace via its [App CR]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}).
This is simpler and easier than using other solutions such as triggering a Kubernetes job via a Helm hook.

## Configuring labels / annotations

You can use `.spec.namespaceConfig` to configure the namespace metadata. You can set `.spec.namespaceConfig.annotations` and / or
`spec.namespaceConfig.labels` and provide the values as a key/value map. App platform then ensures the namespace exists and has this metadata.

For example, if you want to add an annotation `linked.io/inject: enabled` to the target namespace `loki1` add this to the app CR.

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

Now you can check the namespace and it will be the same as below.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    linkerd.io/inject: "enabled"
  name: loki
```

If you want to set labels on the namespace, use `spec.namespaceConfig.labels`.

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

### Validation

The [validation logic]({{< relref "/developer-platform/app-platform/defaulting-validation" >}}) in app-admission-controller checks whether multiple app CRs are updating the same namespace
with different values. The validation webhook will prevent the conflicting value from being added.
