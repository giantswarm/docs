---
linkTitle: What is GitOps
title: What is GitOps
description: Learn how to continuous deploy all your workloads thanks to GitOps and Kubernetes.
weight: 20
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-what-is-gitops
last_review_date: 2024-11-07
user_questions:
  - What is GitOps?
  - How to manage resources with GitOps?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

The GitOps working group [defines the term as a set of principles](https://github.com/open-gitops/documents/blob/release-v1.0.0/PRINCIPLES.md):
> GitOps is a set of principles for operating and managing software systems. These principles are derived from modern software operations, but are also rooted in pre-existing and widely adopted best practices.
> The desired state of a GitOps managed system must be:
> **Declarative**
> A system managed by GitOps must have its desired state expressed declaratively.
> **Versioned and immutable**
> The desired state is stored in a way that enforces immutability, versioning and retains a complete version history.
> **Pulled automatically**
> Software agents automatically pull the desired state declarations from the source.
> **Continuously reconciled**
> Software agents continuously observe the actual system state and attempt to apply the desired state.

These principles are manifested in popular tools, such as `Flux` or `ArgoCD`, and can be summarized as follows:

- The cluster and application configuration is kept in `Git` repositories (or `Helm` repositories, `S3` buckets) GitOps operators are deployed to clusters and configured to watch the manifests. The operators are tasked with periodically comparing the desired and actual states of the cluster's resources and reconciling them if discrepancies are found.

- If the cluster's state changes in a way that's not reflected in the code, the change will be reverted. If the code is updated with a new configuration and/or resources, the cluster will be instantly updated to match the desired state.

- This way of managing Kubernetes comes with all the benefits and best practices of a versioning system: code reviews, pull requests, versioned releases, test branches, commit history, and full accountability. Due to the almost instant deployment of committed changes, it's also a perfect tool for development and testing.

Learn more about our GitOps operator, [`Flux`]({{< relref "/tutorials/continuous-deployment/flux/" >}}).
