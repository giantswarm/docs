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
    parent: use-the-api
last_review_date: 2024-01-25
user_questions:
  - Which commands does kubectl-gs offer?
aliases:
  - /reference/kubectl-gs/
  - /ui-api/kubectl-gs/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

`kubectl-gs` is a CLI and a [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) plugin (invoked as `kubectl gs`) for the Giant Swarm [Management API]({{< relref "/vintage/use-the-api/management-api" >}}).

**Note:** Management API support is under active development. Supported functionality depends on the provider and the workload cluster release used. Please pay attention to the compatibility information given on the individual command reference pages.

## Commands {#commands}

| Command                       | Description                                                      |
|-------------------------------|------------------------------------------------------------------|
| [`login`][1]                  | [Ensure an authenticated kubectl context][1]                     |
| [`get apps`][2]               | [List apps or get details on a single app][2]                    |
| [`get catalogs`][3]           | [List catalogs or get details on a single catalog][3]            |
| [`get clusters`][4]           | [List clusters or get details on a single cluster][4]            |
| [`get nodepools`][5]          | [List node pools or get details on a single node pool][5]        |
| [`get organizations`][15]     | [List organizations or get details on a single organization][15] |
| [`get releases`][11]          | [List releases or get details on a single release][11]           |
| [`gitops`][14]                | [Gathers GitOps related subcommand][14]                          |
| [`template app`][6]           | [Create manifests for an app][6]                                 |
| [`template catalog`][7]       | [Create manifests for a catalog][7]                              |
| [`template cluster`][8]       | [Create manifests for a cluster][8]                              |
| [`template nodepool`][9]      | [Create manifests for a node pool][9]                            |
| [`template organization`][10] | [Create manifest for an organization][10]                        |
| [`update app`][12]            | [Update given App][12]                                           |
| [`update cluster`][13]        | [Schedule a cluster update][13]                                  |
| `help`                        | Get help for a command                                           |

## Flags {#flags}

| Name               | Description             |
|--------------------|-------------------------|
| `--v`, `--version` | Version for kubectl gs. |

## Global flags {#global-flags}

| Name                         | Description                                                                                                                                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `--as`                       | Username to impersonate for the operation. User could be a regular user or a service account in a namespace.                                                                                                    |
| `--as-group`                 | Group to impersonate for the operation, this flag can be repeated to specify multiple groups.                                                                                                                   |
| `--as-uid`                   | UID to impersonate for the operation.                                                                                                                                                                           |
| `--cache-dir`                | Default cache directory.                                                                                                                                                                                        |
| `--certificate-authority`    | Path to a cert file for the certificate authority.                                                                                                                                                              |
| `--client-certificate`       | Path to a client certificate file for TLS.                                                                                                                                                                      |
| `--client-key`               | Path to a client key file for TLS.                                                                                                                                                                              |
| `--cluster`                  | The name of the kubeconfig cluster to use.                                                                                                                                                                      |
| `--context`                  | The name of the kubeconfig context to use.                                                                                                                                                                      |
| `--debug`                    | Toggle debug mode, for seeing full error output.                                                                                                                                                                |
| `--disable-version-check`    | Disable self-update version check.                                                                                                                                                                              |
| `-h`, `--help`               | Help for kubectl gs.                                                                                                                                                                                            |
| `--insecure-skip-tls-verify` | If true, the server's certificate will not be checked for validity. This will make your HTTPS connections insecure.                                                                                             |
| `--kubeconfig`               | Path to the kubeconfig file to use for CLI requests.                                                                                                                                                            |
| `-n`, `--namespace`          | If present, the namespace scope for this CLI request.                                                                                                                                                           |
| `--request-timeout`          | The length of time to wait before giving up on a single server request. Non-zero values should contain a corresponding time unit (e.g. 1s, 2m, 3h). A value of zero means don't timeout requests. (default "0") |
| `-s`, `--server`             | The address and port of the Kubernetes API server                                                                                                                                                               |
| `--tls-server-name`          | Server name to use for server certificate validation. If it is not provided, the hostname used to contact the server is used                                                                                    |
| `--token`                    | Bearer token for authentication to the API server                                                                                                                                                               |
| `--user`                     | The name of the kubeconfig user to use                                                                                                                                                                          |

## Installing and updating {#install}

With [Krew](https://krew.sigs.k8s.io/), simply install and upgrade the `gs` plug-in:

```nohighlight
kubectl krew install gs
```

```nohighlight
kubectl krew upgrade gs
```

Find out more details in our [installation docs]({{< relref "/vintage/use-the-api/kubectl-gs/installation" >}}).

## Troubleshooting

Otherwise, your Giant Swarm support staff is available for you in case you run into an issue. Also feel free to check our [frequently asked questions]({{< relref "/vintage/use-the-api/kubectl-gs/faq.md" >}}) on `kubectl-gs`.

## Contributing

See the [GitHub project](https://github.com/giantswarm/kubectl-gs) for source code, issues and pull requests.

As a Giant Swarm customer, feel free to use your Slack channel to give feedback, ask questions and suggest improvements for `kubectl-gs`.

[1]: {{< relref "/vintage/use-the-api/kubectl-gs/login" >}}
[2]: {{< relref "/vintage/use-the-api/kubectl-gs/get-apps" >}}
[3]: {{< relref "/vintage/use-the-api/kubectl-gs/get-catalogs" >}}
[4]: {{< relref "/vintage/use-the-api/kubectl-gs/get-clusters" >}}
[5]: {{< relref "/vintage/use-the-api/kubectl-gs/get-nodepools" >}}
[6]: {{< relref "/vintage/use-the-api/kubectl-gs/template-app" >}}
[7]: {{< relref "/vintage/use-the-api/kubectl-gs/template-catalog" >}}
[8]: {{< relref "/vintage/use-the-api/kubectl-gs/template-cluster" >}}
[9]: {{< relref "/vintage/use-the-api/kubectl-gs/template-nodepool" >}}
[10]: {{< relref "/vintage/use-the-api/kubectl-gs/template-organization" >}}
[11]: {{< relref "/vintage/use-the-api/kubectl-gs/get-releases" >}}
[12]: {{< relref "/vintage/use-the-api/kubectl-gs/update-app" >}}
[13]: {{< relref "/vintage/use-the-api/kubectl-gs/update-cluster" >}}
[14]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops" >}}
[15]: {{< relref "/vintage/use-the-api/kubectl-gs/get-organizations" >}}
