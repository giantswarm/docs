---
linkTitle: FAQ
title: Questions and answers on kubectl-gs
description: Frequently asked questions and answers and help for troubleshooting around `kubectl-gs`.
weight: 15
menu:
  main:
    parent: uiapi-kubectlgs
last_review_date: 2024-01-18
aliases:
  - /reference/kubectl-gs/faq
  - /ui-api/kubectl-gs/faq
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create a cluster or node pool with kubectl-gs?
  - How can I install an app in a workload cluster with kubectl-gs?
  - Can kubectl-gs work without kubectl?
  - Do you provide a container image for kubectl-gs?
  - What commands replace my old gsctl command?
  - How can I find out my Management API endpoint for 'kubectl gs login'?
  - "What does 'Error: Token renewal failed' mean?"
  - Why does the command connect to a service called "athena"?
---

## General

### How can I create a cluster or node pool

`kubectl-gs` provides the `template` family of commands, to create manifests for clusters, node pools and more. The resulting manifests are meant to be applied by `kubectl apply` to actually create resources. Check the [template cluster]({{< relref "/use-the-api/kubectl-gs/template-cluster.md" >}}) and [template nodepool]({{< relref "/use-the-api/kubectl-gs/template-cluster.md" >}}) reference pages. We also provide more verbose tutorials for [AWS]({{< relref "/use-the-api/management-api/creating-workload-clusters/aws" >}}) and [Azure]({{< relref "/use-the-api/management-api/creating-workload-clusters/azure" >}}).

### How can I install an app in a workload cluster

Check the [kubectl gs template app]({{< relref "/use-the-api/kubectl-gs/template-app.md" >}}) command. It helps you create an [App]({{< relref "/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) resource manifest, which is what you need to express the desired state "I want app X installed in cluster Y". For more context, we provide an article to help you [get started with apps]({{< relref "/getting-started/app-platform/deploy-app/index.md" >}}).

### Can kubectl-gs work without kubectl

Yes, you can execute the binary as `kubectl-gs`, too. However, most commands expect a kubectl configuration to be present.

### Do you provide a container image for kubectl-gs

Yes, please check the [installation]({{< relref "/use-the-api/kubectl-gs/installation.md#docker" >}}) page for details.

### Why do I see "API rate limit exceeded" errors

kubectl-gs accesses the GitHub API to check whether the user is running the latest version of kubectl-gs. If the user, or someone in their network, has been executing many requests against the GitHub API already within a certain time window, the network might get blocked due to [rate limiting](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api?apiVersion=2022-11-28).

To circumvent this problem, you can execute every command with the `--disable-version-check` flag. As an alternative, you can set the `GITHUB_TOKEN` environment variable to a GitHub token, and make the request count towards your personal rate limit, not the (lower) IP based one.

### What commands replace my old gsctl command

Please check the [migration]({{< relref "/use-the-api/gsctl/migrate.md" >}}) page.

## `kubectl gs login`

### How can I find out my Management API endpoint

You can simply ask your Giant Swarm support contact. As an alternative, `kubectl gs login` also accepts the web UI URL as an argument. So if you happen to know that one, simply use that. (The logic behind this is quite simple: The domain prefix `happa.` simply gets removed from the web UI URL, and the result is the Management API endpoint URL.)

### What does 'Error: Token renewal failed' mean

It means that `kubectl gs login` tried to get a fresh ID-token to authenticate with against the Kubernetes API, since the existing one had expired. To resolve this, please check your `kubectl` configuration file (typically in `~/.kube/config`). Do you have several `user` entries for the same management cluster, using the same `client-id`? If yes, please edit your configuration so that there is only one.

### Why does the command connect to a service called 'athena'

The Management API uses a TLS certificate signed by a custom certificate authority (CA). In order to communicate with the API, a client (here: `kubectl`) must trust that CA, it must have the CA's certificate. Athena is a public service providing that CA certificate, plus some information on the installation, to the client.
