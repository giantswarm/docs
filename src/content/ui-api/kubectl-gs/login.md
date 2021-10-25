---
linkTitle: login
title: "'kubectl gs login' command reference"
description: Reference documentation on how to ensure an authenticated kubectl context for a Giant Swarm management or workload cluster, using 'kubectl gs'.
weight: 60
menu:
  main:
    identifier: uiapi-kubectlgs-login
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/login/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I log in with kubectl for the Management API?
  - How can I create a workload cluster client certificate?
last_review_date: 2021-10-25
---

# `kubectl gs login`

Use this command to set up a kubectl context to work with:

1. a management cluster, using OIDC authentication

2. a workload cluster on AWS or Azure, using client certificate auth

Note that `2` implies `1`. When setting up workload cluster access, management cluster access will be set up as well, if that is not yet done.

## Usage

The command is called with the general syntax

```nohighlight
kubectl gs login <management-cluster> [flags]
```

where `management-cluster` can be either:

- **Empty:** If the current kubectl context is a Giant Swarm management cluster, this ensures that the OIDC auth token will be refreshed and show the name of the current context.

- **Web interface URL:** The URL of the management cluster's [web UI]({{< relref "/ui-api/web/" >}}) instance.

- **Management API endpoint:** The URL of the management cluster's Kubernetes API endpoint.

- **Context name:** Name of a Giant Swarm kubectl context, with or without `gs-` prefix.

It is also possible to create client certificates for a workload cluster, by providing the right configuration flags. Please be aware that the recommended way to authenticate users for workload clusters is OIDC. Client certificates should only be a temporary replacement.

## Flags {#flags}

Here we document the flags that have a particular meaning for the `login` command. Use `kubectl gs login --help` for a full list.

### `--workload-cluster` {#flags-workload-cluster}

If present, `kubectl gs` will set up a kubectl context to work with a workload cluster.

### `--organization` {#flags-organization}

The organization that the workload cluster belongs to.

Requires the `--workload-cluster` flag.

### `--certificate-group` {#flags-certificate-group}

The RBAC group name to be encoded into the X.509 field "O".
It can be specified multiple times in order to set multiple groups at once.

Requires the `--workload-cluster` flag.

### `--certificate-ttl` {#flags-certificate-ttl}

How long the client certificate should live for. When creating client certificates, we recommend using short expiration periods.

Requires the `--workload-cluster` flag.

## Examples

### Management cluster

Using the Web UI URL as an argument:

```nohighlight
kubectl gs login https://happa.g8s.mymc.westeurope.azure.gigantic.io
```

### Workload cluster

```nohighlight
kubectl gs login mymc \
  --workload-cluster gir0y \
  --organization acme \
  --certificate-group admins \
  --certificate-ttl 3h
```
