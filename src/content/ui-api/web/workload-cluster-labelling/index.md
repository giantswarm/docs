---
linkTitle: Labelling clusters
title: Labelling workload clusters using the web interface
description: Here we explain how you can manage labels for workload cluster in our web user interface.
last_review_date: 2020-05-29
weight: 20
menu:
  main:
    identifier: uiapi-web-labelling
    parent: uiapi-web
aliases:
  - /reference/web-interface/tenant-cluster-labelling/
  - /reference/web-interface/workload-cluster-labelling/
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Labelling workload clusters using the web interface

Labels are a mechanism to assign short pieces of additional information to your Giant Swarm workload clusters.
For more information about this feature, check out the [labelling workload clusters]({{< relref "/advanced/labelling-workload-clusters" >}}) user guide.

## Viewing workload cluster labels

The cluster details page shows the labels currently attached to the current cluster in the "General" tab below the workload cluster release information.

![A screenshot of our web interface, showing cluster details with list of cluster labels](cluster-labelling-detail.png)

## Editing workload cluster labels

Each label is editable by clicking on its key or label part.
Doing so opens a tooltip where you can make changes and confirm them.

![A screenshot of our web interface, showing a cluster label edit tooltip](cluster-labelling-edit.png)

Your changes will be validated to match the [Kubernetes labels syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
It is not possible to save invalid changes.

![A screenshot of our web interface, showing a cluster label edit tooltip with invalid input](cluster-labelling-edit-error.png)

## Deleting workload cluster labels

It it possible to remove a cluster label by clicking the `×` right of a label.
A confirmation tooltip will allow you to confirm your action.

![A screenshot of our web interface, showing a cluster label delete tooltip](cluster-labelling-delete.png)
