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

## Key includes `giantswarm.io`

### `app.giantswarm.io/branch`

Name of the branch of the source repository providing the app/chart the resource is part of. In production applications built from the default branch, the value is expected to be `HEAD`.

### `app.giantswarm.io/commit`

The commit SHA representing the state of the source repository providing the app/chart the resource is part of. The value is expected to be 40 characters long.

### `app-operator.giantswarm.io/version`

- TODO. Found on App and AppCatalog (application.giantswarm.io/v1alpha1) resources in management clusters. Value is a Semver version number. Value is sometimes `0.0.0`.

### `application.giantswarm.io/catalog`

Used on AppCatalogEntry resources, to indicate which catalog it is associated with. The value is the name of the Catalog resource.

### `application.giantswarm.io/catalog-type`

- TODO. Found on AppCatalog and AppCatalogEntry resources. Value is the type of the AppCatalog resource this entry belongs to. Value is `stable`, `test`, or `community`.

### `application.giantswarm.io/catalog-visibility`

- TODO. Found on AppCatalog and Catalog resources. Value is the visibility of the AppCatalog resource this entry belongs to. Value is `public` or `internal`.

### `application.giantswarm.io/team`

Name of the Giant Swarm team responsible for the application.

### `apps.giantswarm.io/affinity`

- TODO. Seems to be only used in cert-manager-app for pod (anti) affinity.

### `chart-operator.giantswarm.io/version`

- TODO. Found only on Chart (charts.application.giantswarm.io/v1alpha1) resources. Value is a semver version number.

### `cluster-apps-operator.giantswarm.io/watching`

- TODO. Found on management clusters on Cluster and HelmRelease resources. Value is always empty.

### `giantswarm.io/cluster`

- TODO. Found in a variety of resources in management clusters, and in workload clusters only on Chart (charts.application.giantswarm.io/v1alpha1) resources. Value is a cluster name.

### `giantswarm.io/logging`

- TODO. Found on a Cluster resource, value is "true".

### `giantswarm.io/machine-pool`

- TODO Found on CiliumNode resources, value is a string like `operations-nodepool0`.

### `giantswarm.io/managed-by`

- TODO Found on various resources in MC and WC. Value differs.
    - E. g. `rbac-operator` on RBAC resources indicates that rbac-operator created these and will reconcile/delete them.
    - Value `flux` on an App resource indicates that the App is reconciled by Flux.
    - Name of a bundle on an App resource indicates that the App has been installed by a bundle.

### `giantswarm.io/monitoring`

- TODO Seems to appear only on cilium related resources. Value is always "true".

### `giantswarm.io/monitoring_basic_sli`

- TODO Found on Cilium and ServiceMonitor resources. Value is always "true".

### `giantswarm.io/organization`

- TODO Found on a variety of resources in both MC and WC. Value is the name of the organization the resource is assigned to.

### `giantswarm.io/service-type`

- TODO Found on various resources in management and workload clusters. Value is always `managed`.

### `giantswarm.io/service_type`

- TODO Found on various resources in management clusters. Value is always `managed`.

### `giantswarm.io/service-priority`

- TODO: Explain based on https://handbook.giantswarm.io/docs/rfcs/classify-cluster-priority/ and https://docs.giantswarm.io/vintage/advanced/cluster-management/labelling-workload-clusters/#service-priority

### `policy.giantswarm.io/psp-status`

- TODO Found on App, Chart, and Cluster resources, MC and WC. On clusters with PSS the value is `disabled`.

### `policy.giantswarm.io/resource-kind`

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values are like `Deployment`, `CronJob`.

### `policy.giantswarm.io/resource-name`

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values is the name of the resource the exception is for.

### `policy.giantswarm.io/resource-namespace`

- TODO Found in PolicyException and PolicyExceptionDraft resources. Values is the namespace of the resource the exception is for.

### `ui.giantswarm.io/display`

[Source](https://github.com/giantswarm/k8smetadata/blob/v0.24.0/pkg/label/ui.go#L11)

Affects whether or not a resource is intended for display in a user interface like the Giant Swarm web UI. For example, it can be used to hide irrelevant RBAC system roles from users. The value can either be `"true"` (to display a resource) or `"false"` (for hiding it). The default behavior depends on the context.
