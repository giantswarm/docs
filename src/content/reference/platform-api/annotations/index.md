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

### cluster.giantswarm.io/description

Used on the Cluster resource to provide a human-readable description of the cluster. This description is shown in Giant Swarm web interfaces.

### network-topology.giantswarm.io/mode

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies how transit gateways for the cluster will get set up in AWS. Possible values are: `None`, `GiantSwarmManaged`, `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L25-L27)

### network-topology.giantswarm.io/transit-gateway

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies the ID of the transit gateway to use when the topology mode (`network-topology.giantswarm.io/mode`) is set to `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L33-L35)

### network-topology.giantswarm.io/prefix-list

Found on the AWSCluster resource for Cluster API provider AWS (CAPA) clusters. Specifies the ID of the managed prefix list to use when the topology mode (`network-topology.giantswarm.io/mode`) is set to `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L37-L39)
