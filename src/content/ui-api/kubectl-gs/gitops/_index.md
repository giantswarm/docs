---
linkTitle: gitops
title: "The 'kubectl gs gitops' command family reference"
description: Main page for documentation on the 'kubectl' GitOps support, with an overview of all commands.
weight: 50
layout: single
menu:
  main:
    identifier: kubectlgs-gitops
    parent: uiapi-kubectlgs
last_review_date: 2022-08-31
user_questions:
  - Which GitOps commands does the kubectl-gs offer?
aliases:
  - /reference/kubectl-gs/gitops/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

The `gitops` command groups all the GitOps-targeted operations supported by the `kubectl-gs` plugin.

It implements the same basic operations the [gitops-template repository](https://github.com/giantswarm/gitops-template#using-this-repository) supports and respects [the recommended GitOps structure](https://github.com/giantswarm/gitops-template/blob/main/docs/repo_structure.md).

## Caveats

The command is expected to run against a local clone of the GitOps repository and does not go beyond creating
requested files and directories. Hence, **all git-related operations**, like cloning or pushing, must be perform by
the user prior to or after the plugin execution. By default command targets the current working directory, this
behaviour can be controlled with the `--local-path <path_to_repository_dir>` flag.

The command supports the dry-run mode of operation that offers a preview of the changes that are going to be applied to the
repository. The behaviour can be controlled with the `--dry-run` flag. In this mode the command solely prints the list of
directories, files in these directories, and content of the files, that are to be created and modified, as indicated by
the `## CREATE ##` and `## MODIFY ##` sections of the output respectively.

The commands will not re-create already existing files to prevent overriding users, or other commands, changes.
It is often that one command creates a file with an initial content, and some other command updates it with content important
to its context. Without preventing re-creation, running the first command again would result in restoring the original content
and possibly damaging the user environment, by for example accidental removal of resources. **This also implies that doing
updates with the `kubectl-gs` is currently not possible**, meaning, if user first runs a command with limited set of flags,
to re-run it later with a new set of flags, outcome of the first command will not be replaced. User will have to manually put
the needed changes, or to remove the directory and then re-run the command. This may get changed in the future.

## Usage {#usage}

The command to execute is the `kubectl gs gitops`.

The command itself does not perform any actions on the filesystem, it instead gives a handy shorthand of this
document.

## Subcommands {#subcommands}

| Command                       | Description                                                        |
| ----------------------------- | ------------------------------------------------------------------ |
| [`init`][1]                   | [Pre-configure GitOps repository with basic structure][1]          |
| [`add mc`][2]                 | [Adds a new management cluster to the repository structure][2]     |
| [`add org`][3]                | [Adds a new Organization to the repository structure][3]           |
| [`add wc`][4]                 | [Adds a new workload cluster to the repository structure][4]       |
| [`add app`][5]                | [Adds a new Application to your GitOps directory structure][5]     |
| [`add update`][6]             | [Enable automatic updates for an app.][6]                          |
| [`add enc`][7]                | [Adds a new GPG key pair to the SOPS repository configuration.][7] |


[1]: {{< relref "/ui-api/kubectl-gs/gitops/init" >}}
[2]: {{< relref "/ui-api/kubectl-gs/gitops/add-mc" >}}
[3]: {{< relref "/ui-api/kubectl-gs/gitops/add-org" >}}
[4]: {{< relref "/ui-api/kubectl-gs/gitops/add-wc" >}}
[5]: {{< relref "/ui-api/kubectl-gs/gitops/add-app" >}}
[6]: {{< relref "/ui-api/kubectl-gs/gitops/add-update" >}}
[7]: {{< relref "/ui-api/kubectl-gs/gitops/add-enc" >}}
