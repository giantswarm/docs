---
linkTitle: Migration to kubectl gs
title: Migrating from gsctl to kubectl gs
description: gsctl is a CLI for the deprecated Giant Swarm Rest API. As you move from the Rest API towards the Management API, you'll have to say goodby to gsctl and embrace kubectl-gs, step by step. This page should help you make the transition smoothly.
weight: 1
menu:
  main:
    parent: uiapi-gsctl
user_questions:
- What commands in kubectl-gs replace what gsctl commands?
- How can I replace gsctl with kubectl-gs?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
last_review_date: 2021-11-23
---

# Migrating from `gsctl` to `kubectl gs`

`gsctl` is a CLI for Giant Swarm's proprietary Rest API, which is no longer developed. To make full use of clusters and apps with Giant Swarm, users have to migrate to the [Management API]({{< relref "/ui-api/management-api/" >}}).

Since the Management API is the Kubernetes API of the management cluster, `kubectl` is available as a CLI to work with the API. In addition, Giant Swarm provides [kubectl-gs]({{< relref "/ui-api/kubectl-gs/" >}}), which can be run as plugin for `kubectl` with the shorthand `gs`.

Some, but not all, `gsctl` commands have direct equivalents in `kubectl-gs`.

Here is a table for all replacements:

| gsctl command           | kubectl gs command |
|-------------------------|--------------------|
| gsctl create cluster    | [kubectl gs template cluster]({{< relref "/ui-api/kubectl-gs/template-cluster.md" >}}) |
| gsctl create keypair    | [kubectl gs login]({{< relref "/ui-api/kubectl-gs/login.md" >}}) |
| gsctl create kubeconfig | [kubectl gs login]({{< relref "/ui-api/kubectl-gs/login.md" >}}) |
| gsctl create nodepool   | [kubectl gs template nodepool]({{< relref "/ui-api/kubectl-gs/template-nodepool.md" >}}) |
| gsctl list clusters     | [kubectl gs get clusters]({{< relref "/ui-api/kubectl-gs/get-clusters.md" >}}) |
| gsctl list nodepools    | [kubectl gs get nodepools]({{< relref "/ui-api/kubectl-gs/get-nodepools.md" >}}) |
| gsctl list releases     | [kubectl gs get releases]({{< relref "/ui-api/kubectl-gs/get-releases.md" >}}) |
| gsctl login             | [kubectl gs login]({{< relref "/ui-api/kubectl-gs/login.md" >}}) |
| gsctl show cluster      | [kubectl gs get clusters]({{< relref "/ui-api/kubectl-gs/get-clusters.md" >}}) |
| gsctl show nodepool     | [kubectl gs get nodepools]({{< relref "/ui-api/kubectl-gs/get-nodepools.md" >}}) |
| gsctl show release      | [kubectl gs get releases]({{< relref "/ui-api/kubectl-gs/get-releases.md" >}}) |

Below is some additional information on commands that don't have a direct replacement.

| gsctl command | Comment |
|---------------|---------|
| gsctl completion | `kubectl-gs` does not yet provide support for shell completion. |
| gsctl delete cluster | To delete a cluster, use `kubectl delete` on the cluster's main resource. |
| gsctl delete nodepool | To delete a node pool, use `kubectl delete` on the node pool's main resource. |
| gsctl delete endpoint | Handling of context, cluster, and user entries is done via `kubectl config` subcommands |
| gsctl info | Use `kubectl config current-context` and `kubectl cluster-info`. |
| gsctl list endpoints | Use `kubectl get-contexts`. |
| gsctl logout | There is no logout command for `kubectl`. |
| gsctl ping | Use e. g. `kubectl cluster-info` to test your Kubernetes API connection. |
| gsctl scale cluster | The Management API only supports clusters with node pools. Scaling clusters without node pools is not supported via the Management API. |
| gsctl select endpoint | Use `kubectl config use-context`. |
| gsctl update cluster | Use `kuebctl edit` or `kubectl patch`. |
| gsctl update organization | Use `kubectl patch` or `kubectl edit` to modify the [organizations.security.giantswarm.io]({{< relref "/ui-api/management-api/crd/organizations.security.giantswarm.io.md" >}}) resource. |
| gsctl upgrade cluster | Use `kubectl patch` to modify the `release.giantswarm.io/version` label of the cluster's main resource (`clusters.cluster.x-k8s.io`). |
