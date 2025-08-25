---
linkTitle: Annotations
title: Kubernetes resource annotation reference
description: Overview of Kubernetes resource annotations used by Giant Swarm, and their meaning.
layout: single
menu:
  principal:
    parent: reference-platform-api
    identifier: reference-platform-api-annotations
weight: 500
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2025-02-20
user_questions:
  - What annotations are used in Kubernetes resources by Giant Swarm?
---

**Notice:** Annotations on Kubernetes resources are set by many different parties, and for various reasons. In this overview we explain our reasons for using a relevant set of annotations, and which values or value format is expected. If you are missing information, please consult upstream documentation from Kubernetes etc., or ask a Giant Swarm contact for more information. Also check our corresponding [labels]({{< relref "/reference/platform-api/labels" >}}) reference page.

### app-operator.giantswarm.io/cordon-reason

On an [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) or [Chart]({{< relref "/reference/platform-api/crd/charts.application.giantswarm.io.md" >}}) resource, this annotation indicates the reason why app-operator should currently not reconcile this app, until the `app-operator.giantswarm.io/cordon-until` date has passed.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/app.go#L14-L16)

### app-operator.giantswarm.io/cordon-until

On an [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) or [Chart]({{< relref "/reference/platform-api/crd/charts.application.giantswarm.io.md" >}}) resource, this annotation indicates a date until which app-operator should currently not reconcile this app. If specified, the `app-operator.giantswarm.io/cordon-reason` annotation should also be set.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/app.go#L18-L20)

### cluster.giantswarm.io/description

Used on the Cluster resource to provide a human-readable description of the cluster. This description is shown in Giant Swarm web interfaces.

### kustomize.toolkit.fluxcd.io/force

Can be set on any resource to control Flux reconciliation behaviour. The value can be either `Enabled` or `Disabled`. If set to `Enabled`, Flux will replace the resources in-cluster if the patching fails due to immutable field changes. More details in the [Flux docs](https://fluxcd.io/flux/components/kustomize/kustomizations/#force).

### kustomize.toolkit.fluxcd.io/prune

The value `disabled` on any resource disables Flux garbage collection for this resource. More details in the [Flux docs](https://fluxcd.io/flux/components/kustomize/kustomizations/#prune).

### kustomize.toolkit.fluxcd.io/reconcile

Used on any resource. When set to `disabled`, Flux will no longer apply changes, nor will it prune the resource. [Flux docs](https://fluxcd.io/flux/components/kustomize/kustomizations/#suspending-and-resuming).

### kustomize.toolkit.fluxcd.io/ssa

Used on any resource to control the server-side apply behaviour of Flux. The values `Override`, `Merge`, `IfNotPresent`, and `Ignore` can occur. More information on these settings is available in the [Flux docs](https://fluxcd.io/flux/components/kustomize/kustomizations/#controlling-the-apply-behavior-of-resources).

### network-topology.giantswarm.io/mode

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies how transit gateways for the cluster will get set up in AWS. Possible values are: `None`, `GiantSwarmManaged`, `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L25-L27)

### network-topology.giantswarm.io/transit-gateway

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies the ID of the transit gateway to use when the topology mode (`network-topology.giantswarm.io/mode`) is set to `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L33-L35)

### network-topology.giantswarm.io/prefix-list

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies the ID of the managed prefix list to use when the topology mode (`network-topology.giantswarm.io/mode`) is set to `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L37-L39)

### reconcile.fluxcd.io/requestedAt

On a Flux resource, this annotation indicates that a Flux reconciliation has been requested. More info in the [Flux docs on HelmReleases, for example](https://fluxcd.io/flux/components/helm/helmreleases/#triggering-a-reconcile).

### reconcile.fluxcd.io/forceAt

On a HelmRelease resource, this annotation indicates that a forceful Helm install or upgrade has been requested. More info in the [Flux docs](https://fluxcd.io/flux/components/helm/helmreleases/#forcing-a-release).
