---
linkTitle: Target namespace metadata
title: Configure an app's target namespace via its App CR
description: How to configure metadata for the target namespace of an app via its app CR. So it can be used by other tools.
weight: 60
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-namespace-config
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I label an app CR's target namespace?
  - How can I annotate an app CR's target namespace?
last_review_date: 2024-10-28
---

When installation apps through the app platform, you might want to add specific labels or annotations to an app's target namespace (for example to allow `loki` to scrape logs from a specific namespace).

The [`App` custom resource]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) allows you to configure the target namespace via the spec.

## Configuring labels and annotations

You can use `.spec.namespaceConfig` to configure the namespace metadata. When setting `.spec.namespaceConfig.annotations` or `spec.namespaceConfig.labels` you provide the values as a key/value map. Later the app platform will ensure the namespace is updated with the provided metadata.

For example, to enable logs in your namespace you set the annotation `ownership.my-org.com/responsible: my-team` in the `App` custom resource.

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
      ownership.my-org.com/responsible: my-team
```

Now you can check the namespace and it will be the same as below.

```yaml
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    ownership.my-org.com/responsible: my-team
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

The [validation logic]({{< relref "/tutorials/app-platform/defaulting-validation" >}}) in app admission controller checks whether multiple `App` resources are updating the same namespace with different values. The validation webhook will prevent the conflicting value from being added.
