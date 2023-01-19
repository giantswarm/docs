---
linkTitle: What is GitOps
title: What is GitOps
description: An explanation of the GitOps principles.
weight: 10
menu:
  main:
    parent: advanced-gitops
    identifier: advanced-gitops-what-is-gitops
user_questions:
  - What is GitOps?
  - How to manage resources with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2022-12-20
---

## What is GitOps

The GitOps Working Group [defines GitOps as a set of principles](https://github.com/open-gitops/documents/blob/release-v1.0.0/PRINCIPLES.md):
> GitOps is a set of principles for operating and managing software systems. These principles are derived from modern software operations, but are also rooted in pre-existing and widely adopted best practices.
> The desired state of a GitOps managed system must be:
> **Declarative**
> A system managed by GitOps must have its desired state expressed declaratively.
> **Versioned and Immutable**
> The desired state is stored in a way that enforces immutability, versioning and retains a complete version history.
> **Pulled Automatically**
> Software agents automatically pull the desired state declarations from the source.
> **Continuously Reconciled**
> Software agents continuously observe the actual system state and attempt to apply the desired state.

The way these principles manifest in popular tools, such as FluxCD or ArgoCD can be summarized as follows:

The cluster's desired state, or manifest, is kept in Git repositories (or Helm repositories, S3 buckets, and so on). GitOps operators are deployed to clusters and configured to watch the manifest. The operators are tasked with periodically comparing the desired and actual states of the cluster's resources and reconciling them in case discrepancies are found.

If the cluster's state changes in a way that is not reflected in the code, the change will be reverted. If the code is updated with a new configuration and/or resources, the cluster will be instantly updated to match the desired state.

This way of managing Kubernetes comes with all the benefits and best practices of a versioning system: code reviews, pull requests, versioned releases, test branches, commit history, and full accountability. Due to the almost instant deployment of committed changes, it is also a perfect tool for development and testing.
