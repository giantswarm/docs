---
linkTitle: FAQ
title: Questions and answers on kubectl gs
description: Frequently asked questions and answers and help for troubleshooting around `kubectl gs`.
weight: 15
menu:
  main:
    parent: uiapi-kubectlgs
last_review_date: 2021-11-22
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - Why is kubectl gs get appcatalogs no longer used?
  - What is the replacement for kubectl gs get appcatalogs?
---

# Frequently asked questions (FAQ) and troubleshooting

## General

### How can I create a cluster, node pool, etc.?

`kubectl gs` provides the `template` family of commands, to create manifests for clusters, node pools and more. The resulting manifests are meant to be applied by `kubectl apply` to actually resources.

### Can `kubectl gs` work without `kubectl`?

Yes, you can execute the binary as `kubectl-gs`, too.

However, most commands expect a kubectl configuration to be present.

### Do you provide a Docker image for `kubectl gs`?

Yes, please check the [installation]({{< relref "/ui-api/kubectl-gs/installation.md#docker" >}}) page.

### What commands replace my old `gsctl` command?

Coming from `gsctl` and the deprecated Giant Swarm Rest API, you can rely ony some direct replacement commands in `kubectl gs`. However, not all concepts are comparable, and for some commands, there are ways in `kubectl which don't require a plugin.

Here is a table for all replacements:

| gsctl command | kubectl gs command |
|---------------|--------------------|
| gsctl create cluster | kubectl gs template cluster |
| gsctl create keypair | kubectl gs login |
| gsctl create kubeconfig | kubectl gs login |
| gsctl create nodepool | kubectl gs template nodepool |
| gsctl list clusters | kubectl gs get clusters |
| gsctl list nodepools | kubectl gs get nodepools |
| gsctl list releases | kubectl gs get releases |
| gsctl login | kubectl gs login |
| gsctl show cluster | kubectl gs get cluster |
| gsctl show nodepool | kubectl gs get cluster |
| gsctl show release | kubectl gs get release |

Below is some additional information on commands that don't have a direct replacement.

| gsctl command | Comment |
|---------------|---------|
| gsctl completion | `kubectl gs` does not yet provide support for shell completion. |
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
| gsctl update organization | |
| gsctl upgrade cluster | Use `kubectl patch` to modify the `release.giantswarm.io/version` label of the cluster's main resource (`clusters.cluster.x-k8s.io`). |

## `kubectl gs login`

### How can I find out my Management API endpoint?

You can simply ask your Giant Swarm support contact.

`kubectl gs login` also the web UI URL as an alternative to the Management API URL. So if you happen to know that one, simply use that. (The logic behind this is quite simple: The domain prefix `happa.` simply gets removed, and the result is the Management API URL.)

### What does `Error: Token renewal failed` mean?

It means that `kubectl gs login` tried to get a fresh ID-token to authenticate with against the Kubernetes API, since the existing one had expired.

Please check your `kubectl` configuration file (typically in `~/.kube/config`). Do you have several `user` entries for the same management cluster, using the same `client-id`? If yes, please edit your configuration so that there is only one.

### Why does the command connect to a service called `athena...`?

The Management API uses a TLS certificate signed by a custom certificate authority (CA). In order to communicate with the API, a client (here: `kubectl`) must trust that CA, it must have the CA's certificate. Athena is a public service providing that CA certificate to the client.
