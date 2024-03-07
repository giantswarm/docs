---
linkTitle: Labels
title: Kubernetes resource labels reference
description: Overview of Kubernetes resource labels used by Giant Swarm, and their meaning.
---

**Disclaimer:** Labels on Kubernetes resources can have many meanings. In this overview we make an attempt to describe our reasons for using certain labels, and which values or value format is expected. Please be aware that this effort cannot be complete, since there could always be one missing tool that uses or expects a certain label on a certain type of resource.

As an additional source, our Go library [k8smetadata](https://github.com/giantswarm/k8smetadata) contains a list of labels and annotations that we use in our Go code.

Please also refer to the Kubernetes [Well-Known Labels, Annotations and Taints](https://kubernetes.io/docs/reference/labels-annotations-taints/) documentation section for upstream information.

## `ui.giantswarm.io`

In this label namespace we define labels that exist in order to affect the user experience in user interfaces, like the Giant Swarm web UI or CLIs.

### `ui.giantswarm.io/display`

Affects whether or not a resource is intended for display in a user interface like the Giant Swarm web UI. For example, it can be used to hide irrelevant system roles from users by default. The value can either be `"true"` or `"false"`. If the label is not present, the assumed default value is `"true"`.
