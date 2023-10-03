---
linkTitle: Preparing VMware vSphere for Cluster API
title: Preparing VMware vSphere for Cluster API
description: How to set up your VMware vSphere Cluster tenant to run Giant Swarm management clusters and workload clusters under your jurisdiction.
weight: 80
menu:
  main:
    identifier: gettingstarted-infraprovider-vsphere
    parent: gettingstarted-infraprovider
last_review_date: 2023-10-03
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
---
In order to run the Giant Swarm platform in your VMware Cloud Director (VCD) environment, a number of prerequisites must be satisfied to support Cluster API.

## vSphere infrastructure

## vSphere User permissions

## Networking

## VM templates (node images)

Giant Swarm must have the permissions to upload VM templates to deploy kubernetes nodes from. They will be named following this convention `ubuntu-2004-kube-v1.24.11`.
