---
linkTitle: Annotationa
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
last_review_date: 2025-01-20
---

**Notice:** Annotations on Kubernetes resources are set by many different parties, and for various reasons. In this overview we explain our reasons for using a relevant set of annotations, and which values or value format is expected. If you are missing information, please consult upstream documentation from Kubernetes etc., or ask a Giant Swarm contact for more information. Also check our corresponding [labels]({{< relref "/reference/platform-api/labels" >}}) reference page.

### network-topology.giantswarm.io/mode

Found on the Cluster (cluster.x-k8s.io/v1beta1) resource. Possible values are: `None`, `GiantSwarmManaged`, `UserManaged`.

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L25-L27)

TODO: explain meaning

### network-topology.giantswarm.io/transit-gateway

TODO: explain on which resources it occurs, explain meaning

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L33-L35)

### network-topology.giantswarm.io/prefix-list

TODO: explain on which resources it occurs, explain meaning

More information: [Source](https://github.com/giantswarm/k8smetadata/blob/v0.25.0/pkg/annotation/capa.go#L37-L39)
