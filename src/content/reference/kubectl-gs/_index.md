---
title: kubectl gs Reference
description: User manual for kubectl-gs (also known as kgs), the Giant Swarm kubectl plugin.
layout: subsection
weight: 40
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `kubectl gs` Reference

`kubectl gs`, also known as `kgs`, is a [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) plugin for the Giant Swarm [Control Plane Kubernetes API](/basics/api/#cp-k8s-api).

**Note that Control Plane Kubernetes API access is currently in a preview stage.** Supported functionality depends on the provider and the tenant cluster release used. Please pay attention to the compatibility information given on the individual command reference pages.

## Commands {#commands}

| Command                    | Description                                               | Provider info
|----------------------------|-----------------------------------------------------------|----------------------
| [`login`][1]               | [Ensure an authenticated session with a control plane][1] | all providers
| [`get clusters`][2]        | [List clusters or get details on a single cluster][2]     | only AWS, Azure
| [`template app`][3]        | [Create manifests for an App][3]                          | all providers
| [`template appcatalog`][4] | [Create manifests for an AppCatalog][4]                   | all providers
| [`template cluster`][5]    | [Create manifests for a cluster][5]                       | only AWS, Azure
| [`template nodepool`][6]   | [Create manifests for a node pool][6]                     | only AWS, Azure
| `help`                     | Get help for a command                                    | provider independent

## Installing and updating {#install}

With [Krew](https://krew.sigs.k8s.io/) installed, here is a synopsis:

```nohighlight
kubectl krew install gs
alias kgs="kubectl gs"
kgs
```

Find out more details in our [installation docs](/reference/kubectl-gs/installation/).

## Contributing

See the [GitHub project](https://github.com/giantswarm/kubectl-gs) for source code, issues and pull requests.

As a Giant Swarm customer, feel free to use your Slack channel to give feedback, ask questions and suggest improvements for `kubectl gs`.

[1]: /reference/kubectl-gs/login/
[2]: /reference/kubectl-gs/get-clusters/
[3]: /reference/kubectl-gs/template-app/
[4]: /reference/kubectl-gs/template-appcatalog/
[5]: /reference/kubectl-gs/template-cluster/
[6]: /reference/kubectl-gs/template-nodepool/
