---
linkTitle: Labels
title: Kubernetes resource labels reference
description: Overview of Kubernetes resource labels used by Giant Swarm, and their meaning.
layout: single
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-03-08
---

**Notice:** Labels on Kubernetes resources are set by many different parties, and for various reasons. In this overview we explain our reasons for using a relevant set of labels, and which values or value format is expected. If you are missing information, please consult upstream documentation  from Kubernetes etc., or ask a Giant Swarm contact for more information.

As an additional source, our Go library [k8smetadata](https://github.com/giantswarm/k8smetadata) contains a list of labels and annotations that we use in our Go code.

Common Kubernetes labels are explained on the upstream documentation page [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/).

### app.giantswarm.io/kind

- TODO. Found on ConfigMap and Secret resources in management clusters. Value is either "dashboard" or "datasource". Talk to Atlas.

### app-operator.giantswarm.io/version

- TODO. Found on App and AppCatalog (application.giantswarm.io/v1alpha1) resources in management clusters. Value is a Semver version number. Value is sometimes `0.0.0` which means that the "unique" operator is handling these.
- Source: https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/version.go
- TODO: link to more detailed documentation on this logic, maybe https://docs.giantswarm.io/vintage/getting-started/app-platform/app-bundle/#high-overview

### app-operator.giantswarm.io/watching

- TODO. Found on ConfigMap and Secret resources in management clusters. Value is always `"true"`.
- Source and explanation: https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/app.go#L5

### application.giantswarm.io/branch

Name of the branch of the source repository providing the app/chart the resource is part of. In production applications built from the default branch, the value is expected to be `HEAD`.

### application.giantswarm.io/catalog

Used on AppCatalogEntry resources, to indicate which catalog it is associated with. The value is the name of the Catalog resource.

### application.giantswarm.io/commit

The commit SHA representing the state of the source repository providing the app/chart the resource is part of. The value is expected to be 40 characters long.

### application.giantswarm.io/catalog-type

- TODO. Found on AppCatalog and AppCatalogEntry resources. Value is the type of the AppCatalog resource this entry belongs to. Value is `stable`, `test`, or `community`. Need documentation source for these values.

### application.giantswarm.io/catalog-visibility

- TODO. Found on AppCatalog and Catalog resources. Value is the visibility of the Catalog resource this entry belongs to. Value is `public` (deployed to `default` namespace) or `internal` (deployed to `giantswarm` namespace).

### application.giantswarm.io/team

Name of the Giant Swarm team responsible for the application.

### chart-operator.giantswarm.io/version

Used on Chart (charts.application.giantswarm.io/v1alpha1) resources to specify the chart-operator version to reconcile this resource. Value is a version string.

TODO: Source link

### cluster-apps-operator.giantswarm.io/watching

- TODO. Found on management clusters on Cluster and HelmRelease resources. Value is always empty.

### giantswarm.io/aws-ebs-limit

- TODO. Used on EBS csi-node pods. Meaning unclear. Introduced in aws-ebs-csi-driver-app via https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/37

### giantswarm.io/cluster

- TODO. Found in a variety of resources in management clusters, and in workload clusters mostly on Chart (charts.application.giantswarm.io/v1alpha1) resources. Value is a cluster name. Associates the resource with a cluster.

### giantswarm.io/logging

- TODO. Found on a Cluster resource, value is "true".

### giantswarm.io/machine-pool

Associates the resource or the node with a node pool, using the name of the node pool as the value.

### giantswarm.io/managed-by

- TODO Found on various resources in MC and WC. Value differs.
    - E. g. `rbac-operator` on RBAC resources indicates that rbac-operator created these and will reconcile/delete them.
    - Value `flux` on an App resource indicates that the App is reconciled by Flux.
    - Name of a bundle on an App resource indicates that the App has been installed by a bundle.

### giantswarm.io/monitoring

- TODO Appears on a variety of resources. Value is always "true".
- Talk to Atlas. Seem to be deprecated.

### giantswarm.io/monitoring_basic_sli

- TODO Appears on a variety of resources. Value is always "true".
- Talk to Atlas.

### giantswarm.io/organization

- TODO Found on a variety of resources in both MC and WC. Value is the name of the organization the resource is assigned to.

### giantswarm.io/prevent-deletion

Can be set on certain resource types to prevent deletion. See [Prevent accidental deletion of resources]({{< relref "/vintage/advanced/app-platform/deletion-prevention" >}}).

### giantswarm.io/service-type

- TODO Found on various resources in management and workload clusters. [fmt](https://github.com/giantswarm/fmt/blob/278eb4b3318c454e50f24413e7ef2250159f28d6/kubernetes/annotations_and_labels.md?plain=1#L49) has an explanation. Value is mostly `managed`, also found occurrence `manual` in an [ops recipe](https://github.com/giantswarm/giantswarm/blob/0d16eb4ebb0440608bb1bfd0636d34afa6352cc6/content/docs/support-and-ops/ops-recipes/cilium-rate-limit-issue.md?plain=1#L39). Value `system` is also documented.

### giantswarm.io/service-priority

Used on cluster-related resources to indicate the [service priority]({{< relref "/vintage/advanced/cluster-management/labelling-workload-clusters#service-priority" >}}), which means the relative importance in general, of the cluster.

### policy.giantswarm.io/psp-status

- TODO Found on App, Chart, and Cluster resources, MC and WC. On clusters with PSS the value is `disabled`.

### policy.giantswarm.io/resource-kind

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values are like `Deployment`, `CronJob`.

### policy.giantswarm.io/resource-name

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values is the name of the resource the exception is for.

### policy.giantswarm.io/resource-namespace

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values is the namespace of the resource the exception is for.

### ui.giantswarm.io/display

Affects whether or not a resource is intended for display in a user interface like the Giant Swarm web UI. For example, it can be used to hide irrelevant RBAC system roles from users. The value can either be `"true"` (to display a resource) or `"false"` (for hiding it). The default behavior depends on the context.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/ui.go#L11)
