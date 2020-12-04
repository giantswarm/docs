---
title: Giant Swarm Tenant Cluster Labelling in The Web Interface
description: How to manage tenant cluster labels in our Web Interface.
last_review_date: 2020-05-29
layout: subsection
weight: 20
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Giant Swarm Tenant Cluster Labelling in The Web Interface

Labels are a mechanism to assign short pieces of additional information to your Giant Swarm tenant clusters.
For more information about this feature, check out the [Labelling tenant clusters](/guides/tenant-cluster-labelling/) user guide.

## Viewing tenant cluster labels

The cluster details page shows the labels currently attached to the current cluster in the "General" tab below the tenant cluster release information.

![A screenshot of our web interface, showing cluster details with list of cluster labels](/img/cluster-labelling-detail.png)

## Editing tenant cluster labels

Each label is editable by clicking on its key or label part.
Doing so opens a tooltip where you can make changes and confirm them.

![A screenshot of our web interface, showing a cluster label edit tooltip](/img/cluster-labelling-edit.png)

Your changes will be validated to match the [Kubernetes labels syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
It is not possible to save invalid changes.

![A screenshot of our web interface, showing a cluster label edit tooltip with invalid input](/img/cluster-labelling-edit-error.png)

## Deleting tenant cluster labels

It it possible to remove a cluster label by clicking the `×` right of a label.
A confirmation tooltip will allow you to confirm your action.

![A screenshot of our web interface, showing a cluster label delete tooltip](/img/cluster-labelling-delete.png)
