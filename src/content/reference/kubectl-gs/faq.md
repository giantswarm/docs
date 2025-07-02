---
linkTitle: FAQ
title: Questions and answers on kubectl-gs
description: Frequently asked questions and answers and help for troubleshooting around `kubectl-gs`.
weight: 140
menu:
  principal:
    parent: reference-kubectlgs
last_review_date: 2024-11-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create a cluster or node pool with kubectl-gs?
  - How can I install an app in a workload cluster with kubectl-gs?
  - Can kubectl-gs work without kubectl?
  - Do you provide a container image for kubectl-gs?
  - What commands replace my old gsctl command?
  - How can I find out my platform API endpoint for 'kubectl gs login'?
  - "What does 'Error: Token renewal failed' mean?"
  - Why does the command connect to a service called "athena"?
aliases:
  - /vintage/use-the-api/kubectl-gs/faq/
---

## General

### How can I create a cluster or node pool

`kubectl-gs` provides the `template` family of commands, to create manifests for clusters, node pools and more. The resulting manifests are meant to be applied by `kubectl apply` to actually create resources. Check the [template cluster]({{< relref "/reference/kubectl-gs/template-cluster.md" >}}) and [template nodepool]({{< relref "/reference/kubectl-gs/template-cluster.md" >}}) reference pages. You can find more information in [the getting started page]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).

### How can I install an app in a workload cluster

Check the [kubectl gs template app]({{< relref "/reference/kubectl-gs/template-app.md" >}}) command. It helps you create an [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) resource manifest, which is what you need to express the desired state "I want app X installed in cluster Y". For more context, we provide an article to help you [get started with apps]({{< relref "/tutorials/fleet-management/app-platform/deploy-app" >}}).

### Can kubectl-gs work without kubectl

Yes, you can execute the binary as `kubectl-gs`, too. However, most commands expect a kubectl configuration to be present.

### Do you provide a container image for kubectl-gs

Yes, please check the [installation]({{< relref "/reference/kubectl-gs/installation.md#docker" >}}) page for details.

### Why do I see "API rate limit exceeded" errors

kubectl-gs accesses the GitHub API to check whether the user is running the latest version of kubectl-gs. If the user, or someone in their network, has been executing many requests against the GitHub API already within a certain time window, the network might get blocked due to [rate limiting](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28).

To circumvent this problem, you can execute every command with the `--disable-version-check` flag. As an alternative, you can set the `GITHUB_TOKEN` environment variable to a GitHub token, and make the request count towards your personal rate limit, not the (lower) IP based one.

## `kubectl gs login`

### How can I find out my platform API endpoint

You can simply ask your Giant Swarm support contact. The endpoint is generated with the base domain plus the prefix `api`. For example, if your base domain is `snorkel.gigantic.io`, the endpoint would be `api.snorkel.gigantic.io`.

### What does 'Error: Token renewal failed' mean

It means that `kubectl gs login` tried to get a fresh ID-token to authenticate with against the Kubernetes API, since the existing one had expired. To resolve this, please check your `kubectl` configuration file (typically in `~/.kube/config`). Do you have several `user` entries for the same management cluster, using the same `client-id`? If yes, please edit your configuration so that there is only one.

### Why does the command connect to a service called 'athena'

The platform API uses a TLS certificate signed by a custom certificate authority (CA). In order to communicate with the API, a client (here: `kubectl`) must trust that CA, it must have the CA's certificate. Athena is a public service providing that CA certificate, plus some information on the installation, to the client.
