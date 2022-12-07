---
linkTitle: FAQ
title: Questions and answers on kubectl-gs
description: Frequently asked questions and answers and help for troubleshooting around `kubectl-gs`.
weight: 15
menu:
  main:
    parent: uiapi-kubectlgs
last_review_date: 2022-12-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a cluster or node pool with kubectl-gs?
  - How can I install an app in a workload cluster with kubectl-gs?
  - Can kubectl-gs work without kubectl?
  - Do you provide a Docker image for kubectl-gs?
  - What commands replace my old gsctl command?
  - How can I find out my Management API endpoint for 'kubectl gs login'?
  - "What does 'Error: Token renewal failed' mean?"
  - Why does the command connect to a service called "athena"?
---

## General

### How can I create a cluster or node pool

`kubectl-gs` provides the `template` family of commands, to create manifests for clusters, node pools and more. The resulting manifests are meant to be applied by `kubectl apply` to actually resources. Check the [template cluster]({{< relref "/ui-api/kubectl-gs/template-cluster.md" >}}) and [template nodepool]({{< relref "/ui-api/kubectl-gs/template-cluster.md" >}}) reference pages. We also provide more verbose tutorials for [AWS]({{< relref "/ui-api/management-api/creating-workload-clusters/aws" >}}) and [Azure]({{< relref "/ui-api/management-api/creating-workload-clusters/azure" >}}).

### How can I install an app in a workload cluster

Check the [kubectl gs template app]({{< relref "/ui-api/kubectl-gs/template-app.md" >}}) command. It helps you create an [App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}}) resource manifest, which is what you need to express the desired state "I want app X installed in cluster Y". For more context, we provide an article to help you [get started with apps]({{< relref "/getting-started/app-platform/deploy-app/index.md" >}}).

### Can kubectl-gs work without kubectl

Yes, you can execute the binary as `kubectl-gs`, too. However, most commands expect a kubectl configuration to be present.

### Do you provide a Docker image for kubectl-gs

Yes, please check the [installation]({{< relref "/ui-api/kubectl-gs/installation.md#docker" >}}) page for details.

### What commands replace my old gsctl command

Please check the [migration]({{< relref "/ui-api/gsctl/migrate.md" >}}) page.

## `kubectl gs login`

### How can I find out my Management API endpoint

You can simply ask your Giant Swarm support contact. As an alternative, `kubectl gs login` also accepts the web UI URL as an argument. So if you happen to know that one, simply use that. (The logic behind this is quite simple: The domain prefix `happa.` simply gets removed from the web UI URL, and the result is the Management API endpoint URL.)

### What does 'Error: Token renewal failed' mean

It means that `kubectl gs login` tried to get a fresh ID-token to authenticate with against the Kubernetes API, since the existing one had expired. To resolve this, please check your `kubectl` configuration file (typically in `~/.kube/config`). Do you have several `user` entries for the same management cluster, using the same `client-id`? If yes, please edit your configuration so that there is only one.

### Why does the command connect to a service called 'athena'

The Management API uses a TLS certificate signed by a custom certificate authority (CA). In order to communicate with the API, a client (here: `kubectl`) must trust that CA, it must have the CA's certificate. Athena is a public service providing that CA certificate, plus some information on the installation, to the client.
