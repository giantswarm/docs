---
linkTitle: gitops
title: "The 'kubectl gs gitops' command family reference"
description: Main page for documentation on the 'kubectl' GitOps support.
weight: 30
layout: single
menu:
  main:
    identifier: kubectl-gs-gitops
    parent: kubectl-gs
last_review_date: 2022-08-16
user_questions:
  - Which GitOps commands does the kubectl-gs offer?
aliases:
  - /reference/kubectl-gs/gitops/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
---

The `gitops` command groups all the GitOps-targeted operations supported by the `kubectl-gs` plugin.

The command implements the same operations the [gitops-template repository](https://github.com/giantswarm/gitops-template#using-this-repository) supports and respects [the recommended GitOps structure](https://github.com/giantswarm/gitops-template/blob/main/docs/repo_structure.md).

The command is expected to run against a local clone of the GitOps repository and does not go beyond creating
requested files and directories. Hence, **all git-related operations**, like cloning or pushing, must be perform by
the user prior to or after the plugin execution. By default, command targets the current working directory, this
behaviour can be controlled with the `--local-path <path_to_repository_dir>` flag.

The command supports the dry-run mode that offers a preview of the changes that are going to be applied to the
repository. The behaviour can be controlled with the `--dry-run` flag. In this mode the command prints list of
directories, files in these directories, and content of the files, that are to be craeted.

**Important note**, commands will not re-create already existing files to prevent overriding user's, or other
commands, changes. It is often that one command creates a file with initial content, and some other command updates
it with content important to its context. Without preventing re-creation, running the first command again would
result in restoring the original content and possibly breaking the repository.

## Usage {#usage}

The command to execute is the `kubectl gs gitops`.

The command itself does not perform any actions on the filesystem, it instead gives a handy shorthand of this
document.

## Subcommands {#subcommands}

| Command                       | Description                                                    |
| ----------------------------- | -------------------------------------------------------------- |
| [`init`][1]                   | [Pre-configure GitOps repository with basic structure][1]      |
| [`add mc`][2]                 | [Adds a new Management Cluster to the repository structure][2] |


[1]: {{< relref "/ui-api/kubectl-gs/gitops/init" >}}
[1]: {{< relref "/ui-api/kubectl-gs/gitops/add-mc" >}}
