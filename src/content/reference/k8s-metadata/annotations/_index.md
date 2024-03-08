---
linkTitle: Annotations
title: Kubernetes resource annotations reference
description: Overview of Kubernetes resource annotations used by Giant Swarm, and their meaning.
layout: single
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

**Disclaimer:** Annotations on Kubernetes resources can have many meanings. In this overview we make an attempt to describe our reasons for using certain annotations, and which values or value format is expected. Please be aware that this effort cannot be complete, since there could always be one missing tool that uses or expects a certain label on a certain type of resource.

As an additional source, our Go library [k8smetadata](https://github.com/giantswarm/k8smetadata) contains a list of labels and annotations that we use in our Go code.

Please also refer to the Kubernetes [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/) documentation section for upstream information.
