---
linkTitle: gitops
title: "The 'kubectl gs gitops' command family reference"
description: Main page for documentation on the 'kubectl' GitOps support, with an overview of all commands.
weight: 50
layout: single
menu:
  main:
    identifier: kubectlgs-gitops
    parent: reference-kubectlgs
last_review_date: 2024-10-29
user_questions:
  - Which GitOps commands does the kubectl-gs plugin offer?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
aliases:
  - /use-the-api/kubectl-gs/gitops
  - /reference/kubectl-gs/gitops
  - /ui-api/kubectl-gs/gitops
---

The `gitops` command family provides operations to set up a GitOps repository as required to manage Giant Swarm infrastructure, as well as add and modify resources in this repository.

It implements the same basic operations the [gitops-template repository](https://github.com/giantswarm/gitops-template#using-this-repository) supports and respects [the recommended GitOps structure](https://github.com/giantswarm/gitops-template/blob/main/docs/repo_structure.md).

## Important remarks

- The subcommands are expected to run against a local clone of the GitOps repository and does not go beyond creating
requested files and directories. Hence, **all git-related operations**, like cloning or pushing, must be performed by
the user prior to or after the plugin execution.

- The commands provide a **dry-run mode**, to preview the changes that will be applied to the
repository. Add the `--dry-run` flag to activate this mode.

- The commands **will not overwrite already existing files** to prevent overriding users, or other commands, changes.
It is often that one command creates a file with an initial content, and some other command updates it with content important
to its context. Without preventing re-creation, running the first command again would result in restoring the original content
and possibly damaging the user environment, by for example accidental removal of resources.

- The above also implies that **these commands cannot be used for modifications of resources**. This means that if you first run a command with limited set of flags,
and later re-run it with a new set of flags, the outcome of the first command will not be replaced. You will either have to make
the required changes manually, or remove the directory and then re-run the command. **Note:** this behavior may change in a future release of kubectl-gs.

## Usage {#usage}

The normal assumption is that commands are **executed from the root folder of the GitOps repository**.
This behavior can be modified using the `--local-path PATH_TO_ROOT` flag.

The general syntax is `kubectl gs gitops SUBCOMMAND [FLAGS]`.

Refer to the subcommand documentation for details.

### Subcommands {#subcommands}

| Command                       | Description                                                             |
| ----------------------------- | ----------------------------------------------------------------------- |
| [`init`][1]                   | [Set up a GitOps repository with its basic structure][1]                |
| [`add management-cluster`][2] | [Add a new management cluster to the GitOps repository][2]              |
| [`add organization`][3]       | [Add a new organization to the GitOps repository][3]                    |
| [`add workload-cluster`][4]   | [Add a new workload cluster to the GitOps repository][4]                |
| [`add app`][5]                | [Add a new app to the GitOps repository][5]                             |
| [`add automatic-update`][6]   | [Enable automatic updates for an app][6]                                |
| [`add encryption`][7]         | [Add a new GPG key pair to the SOPS repository configuration][7]        |
| [`add base`][8]               | [Add a new base to create workload clusters for different providers][8] |

[1]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/init" >}}
[2]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-mc" >}}
[3]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-org" >}}
[4]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-wc" >}}
[5]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-app" >}}
[6]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-update" >}}
[7]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-enc" >}}
[8]: {{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-base" >}}
