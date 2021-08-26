---
linkTitle: Labelling clusters
title: Labelling workload clusters using the web interface
description: Here we explain how you can manage labels for workload cluster in our web user interface.
last_review_date: 2021-08-25
weight: 30
menu:
  main:
    identifier: uiapi-web-labelling
    parent: uiapi-web
aliases:
  - /reference/web-interface/tenant-cluster-labelling/
  - /reference/web-interface/workload-cluster-labelling/
user_questions:
  - How can I manage cluster labels via the web interface?
owner:
  - https://github.com/orgs/giantswarm/teams/team-biscuit
---

# Labelling workload clusters using the web interface

Labels are a mechanism to assign short pieces of additional information to your workload clusters.
For more information about this feature, check out the [labelling workload clusters]({{< relref "/advanced/labelling-workload-clusters" >}}) user guide.

## Viewing workload cluster labels

The cluster details page shows the labels set on the cluster in the _Overview_ tab.

![A screenshot of our web interface, showing cluster details with list of cluster labels](view-cluster-labels.png)

## Editing workload cluster labels

Each label is editable by clicking on its key or label part.
Doing so opens a tooltip where you can make changes and confirm them.

![A screenshot of our web interface, showing a cluster label edit tooltip](edit-cluster-labels.png)

Your changes will be validated to match the [Kubernetes labels syntax and character set](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
It is not possible to save invalid changes.

## Deleting workload cluster labels

It it possible to remove a cluster label by clicking the `×` icon on a label.
A confirmation tooltip will allow you to confirm your action.

![A screenshot of our web interface, showing a cluster label delete tooltip](delete-cluster-label.png)
