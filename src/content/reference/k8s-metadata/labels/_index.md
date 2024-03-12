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

Labels in the form `OPERATOR_NAME.giantswarm.io/version` are used to specify the version of the operator that should reconcile the resource. The operator name is the name of the operator that should reconcile the resource, and the version is the version of the operator that should reconcile the resource.

If the operator name is `app-operator`, the label is `app-operator.giantswarm.io/version`. The value of the label is a Semver version number. The special value `0.0.0` means that the resource is handled by the "unique" operator, which is an instance of the operator deployed to the `giantswarm` namespace of the cluster.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/version.go#L7)

### app-operator.giantswarm.io/watching

The label of the format `OPERATOR_NAME.giantswarm.io/watching` is used on ConfigMap and Secret resources to enable the operator to watch the resource. The operator name is the name of the operator that should watch the resource. If the operator name is `app-operator`, the label is `app-operator.giantswarm.io/watching`. The value of the label must be `true`.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/app.go#L5)

### application.giantswarm.io/branch

Name of the branch of the source repository providing the app/chart the resource is part of. In production applications built from the default branch, the value is expected to be `HEAD`.

### application.giantswarm.io/catalog

Used on AppCatalogEntry resources, to indicate which catalog it is associated with. The value is the name of the Catalog resource.

### application.giantswarm.io/commit

The commit SHA representing the state of the source repository providing the app/chart the resource is part of. The value is expected to be 40 characters long.

### application.giantswarm.io/catalog-type

Used on Catalog resources and on AppCatalogEntry resources to indicate the type of source for this catalog or app. Value is either `stable`, `test`, or `community`.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/catalog.go#L9)

### application.giantswarm.io/catalog-visibility

Used on Catalog resources to indicate the target audience of the catalog. Value is `public` (deployed to `default` namespace) or `internal` (deployed to `giantswarm` namespace).

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/catalog.go#L13)

### application.giantswarm.io/team

Name of the Giant Swarm team responsible for the application.

### chart-operator.giantswarm.io/version

Labels in the form `OPERATOR_NAME.giantswarm.io/version` are used to specify the version of the operator that should reconcile the resource. The operator name is the name of the operator that should reconcile the resource, and the version is the version of the operator that should reconcile the resource.

If the operator name is `chart-operator`, the label is `chart-operator.giantswarm.io/version`. The value of the label is a Semver version number. The special value `0.0.0` means that the resource is handled by the "unique" operator, which is an instance of the operator deployed to the `giantswarm` namespace of the cluster.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/version.go#L13)

### cluster-apps-operator.giantswarm.io/watching

The label of the format `OPERATOR_NAME.giantswarm.io/watching` is used on resources to enable the operator to watch the resource. The operator name is the name of the operator that should watch the resource. If the operator name is `cluster-apps-operator`, the label is `cluster-apps-operator.giantswarm.io/watching`. The value of the label must be `true`.

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/app.go#L9)

### giantswarm.io/aws-ebs-limit

- TODO. Used on EBS csi-node pods. Meaning unclear. Introduced in aws-ebs-csi-driver-app via https://github.com/giantswarm/aws-ebs-csi-driver-app/pull/37
- Ask Nick

### giantswarm.io/cluster

Used on a variety of resources to associate the resource with a specific cluster. The value is the name of the cluster.

### giantswarm.io/logging

- TODO. Found on a Cluster resource, value is "true".
- Ask Atlas

### giantswarm.io/machine-pool

Associates the resource or the node with a node pool, using the name of the node pool as the value.

### giantswarm.io/managed-by

- TODO Found on various resources in MC and WC. Value differs.
    - E. g. `rbac-operator` on RBAC resources indicates that rbac-operator created these and will reconcile/delete them.
    - Value `flux` on an App resource indicates that the App is reconciled by Flux.
    - Name of a bundle on an App resource indicates that the App has been installed by a bundle.

### giantswarm.io/monitoring

- TODO Appears on a variety of resources. Value is always "true".
- Talk to Atlas. Seems to be deprecated.

### giantswarm.io/monitoring_basic_sli

- TODO Appears on a variety of resources. Value is always "true".
- Talk to Atlas.

### giantswarm.io/organization

An organization is a key concept in the Giant Swarm platform, used to isolate [tenants]({{< relref "/vintage/platform-overview/multi-tenancy" >}}). This label is used on a variety of resources to associate them with one organization. The value is the name of the organization.

### giantswarm.io/prevent-deletion

Can be set on certain resource types to prevent deletion. See [Prevent accidental deletion of resources]({{< relref "/vintage/advanced/app-platform/deletion-prevention" >}}).

### giantswarm.io/service-type

- TODO Found on various resources in management and workload clusters. [fmt](https://github.com/giantswarm/fmt/blob/278eb4b3318c454e50f24413e7ef2250159f28d6/kubernetes/annotations_and_labels.md?plain=1#L49) has an explanation. Value is mostly `managed`, also found occurrence `manual` in an [ops recipe](https://github.com/giantswarm/giantswarm/blob/0d16eb4ebb0440608bb1bfd0636d34afa6352cc6/content/docs/support-and-ops/ops-recipes/cilium-rate-limit-issue.md?plain=1#L39). Value `system` is also documented.
- Ask Atlas

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
