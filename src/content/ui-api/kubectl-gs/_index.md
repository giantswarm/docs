---
linkTitle: kubectl-gs
title: kubectl-gs reference
description: Main page for documentation on kubectl-gs, the Giant Swarm kubectl plugin, with an overview of all commands, plus information on how to install and upgrade.
weight: 30

# layout: single avoids the listing of sub pages at the end
layout: single

menu:
  main:
    identifier: uiapi-kubectlgs
    parent: ui-api
last_review_date: 2022-09-07
user_questions:
  - Which commands does kubectl-gs offer?
aliases:
  - /reference/kubectl-gs/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

`kubectl-gs` is a CLI and a [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) plugin (invoked as `kubectl gs`) for the Giant Swarm [Management API]({{< relref "/ui-api/management-api" >}}).

**Note:** Management API support is under active development. Supported functionality depends on the provider and the workload cluster release used. Please pay attention to the compatibility information given on the individual command reference pages.

## Commands {#commands}

| Command                       | Description                                                      | Provider info        |
|-------------------------------|------------------------------------------------------------------| -------------------- |
| [`login`][1]                  | [Ensure an authenticated kubectl context][1]                     | all providers        |
| [`get apps`][2]               | [List apps or get details on a single app][2]                    | all providers        |
| [`get catalogs`][3]           | [List catalogs or get details on a single catalog][3]            | all providers        |
| [`get clusters`][4]           | [List clusters or get details on a single cluster][4]            | only AWS, Azure      |
| [`get nodepools`][5]          | [List node pools or get details on a single node pool][5]        | only AWS, Azure      |
| [`get organizations`][15]     | [List organizations or get details on a single organization][15] | all providers        |
| [`get releases`][11]          | [List releases or get details on a single release][11]           | all providers        |
| [`gitops`][14]                | [Gathers GitOps related subcommand][11]                          | N/A                  |
| [`template app`][6]           | [Create manifests for an app][6]                                 | all providers        |
| [`template catalog`][7]       | [Create manifests for a catalog][7]                              | all providers        |
| [`template cluster`][8]       | [Create manifests for a cluster][8]                              | only AWS, Azure      |
| [`template nodepool`][9]      | [Create manifests for a node pool][9]                            | only AWS, Azure      |
| [`template organization`][10] | [Create manifest for an organization][10]                        | all providers        |
| [`update app`][12]            | [Update given App][12]                                           | all providers        |
| [`update cluster`][13]        | [Schedule a cluster update][13]                                  | only AWS, Azure      |
| `help`                        | Get help for a command                                           | provider independent |

Deprecated commands:

- [`get appcatalogs`][100] -- replaced by [`get catalogs`][3]
- [`template appcatalog`][101] -- replaced by [`template catalog`][7]

## Installing and updating {#install}

With [Krew](https://krew.sigs.k8s.io/), simply install and upgrade the `gs` plug-in:

```nohighlight
kubectl krew install gs
```

```nohighlight
kubectl krew upgrade gs
```

Find out more details in our [installation docs]({{< relref "/ui-api/kubectl-gs/installation" >}}).

## Troubleshooting

Otherwise, your Giant Swarm support staff is available for you in case you run into an issue. Also feel free to check our [frequently asked questions]({{< relref "/ui-api/kubectl-gs/faq.md" >}}) on `kubectl-gs`.

## Contributing

See the [GitHub project](https://github.com/giantswarm/kubectl-gs) for source code, issues and pull requests.

As a Giant Swarm customer, feel free to use your Slack channel to give feedback, ask questions and suggest improvements for `kubectl-gs`.

[1]: {{< relref "/ui-api/kubectl-gs/login" >}}
[2]: {{< relref "/ui-api/kubectl-gs/get-apps" >}}
[3]: {{< relref "/ui-api/kubectl-gs/get-catalogs" >}}
[4]: {{< relref "/ui-api/kubectl-gs/get-clusters" >}}
[5]: {{< relref "/ui-api/kubectl-gs/get-nodepools" >}}
[6]: {{< relref "/ui-api/kubectl-gs/template-app" >}}
[7]: {{< relref "/ui-api/kubectl-gs/template-catalog" >}}
[8]: {{< relref "/ui-api/kubectl-gs/template-cluster" >}}
[9]: {{< relref "/ui-api/kubectl-gs/template-nodepool" >}}
[10]: {{< relref "/ui-api/kubectl-gs/template-organization" >}}
[11]: {{< relref "/ui-api/kubectl-gs/get-releases" >}}
[100]: {{< relref "/ui-api/kubectl-gs/get-appcatalogs" >}}
[101]: {{< relref "/ui-api/kubectl-gs/template-appcatalog" >}}
[12]: {{< relref "/ui-api/kubectl-gs/update-app" >}}
[13]: {{< relref "/ui-api/kubectl-gs/update-cluster" >}}
[14]: {{< relref "/ui-api/kubectl-gs/gitops" >}}
[15]: {{< relref "/ui-api/kubectl-gs/get-organizations" >}}
