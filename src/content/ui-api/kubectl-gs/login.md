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
last_review_date: 2021-11-04
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

### Flags

The following flags related to creating client certificates for workload cluster access:

- `--workload-cluster` - If present, `kubectl gs` will set up a kubectl context to work with a workload cluster. Otherwise, the command attempts to set up a management cluster context.
- `--organization` - The organization that the workload cluster belongs to. Requires the `--workload-cluster` flag.
- `--certificate-group` - The RBAC group name to be encoded into the X.509 field "O". It can be specified multiple times in order to set multiple groups at once. Requires the `--workload-cluster` flag.
- `--certificate-ttl` - How long the client certificate should live for. When creating client certificates, we recommend using short expiration periods. Requires the `--workload-cluster` flag.

For management cluster access, the following option is provided:

- `--internal-api` - With this flag you switch to using an alternative host name for the Management API endpoint. That hostname, if available with your installation, is usually only accessible from within a your network or VPN.

  Example: If your Management API host name is `g8s.example.yourdomain.tld`, the alternative hostname is `internal-g8s.example.yourdomain.tld`.

In addition, there is one flag **only relevant to Giant Swarm staff**:

- `--cluster-admin` - This flag enables the use of a Giant Swarm identity provider instead of the customer's one when authenticating for the management cluster.

## Examples

### Management cluster

To set up a context initially, you'll have to use either the web UI  URL as an argument ...

```nohighlight
kubectl gs login https://happa.g8s.example.westeurope.azure.gigantic.io
```

... or the Management API endpoint URL.

```nohighlight
kubectl gs login https://g8s.example.westeurope.azure.gigantic.io
```

As a result, a context will be created with prefix `gs-` and a shorthand for this installation. Watch the command's output:

```nohighlight
Switched to context 'gs-example'.
You are logged in to the management cluster of installation 'example'.
```

For subsequent logins, you can use that shorthand to easily select which installation to log in to. Example:

```nohighlight
kubectl gs login example
```

### Workload cluster

Given that a context `gs-example` already exists from previous management cluster log-ins to that installation, the following command would create a client certificate with specific group assignment:

```nohighlight
kubectl gs login example \
  --workload-cluster gir0y \
  --organization acme \
  --certificate-group example-group
```

Without `--certificate-group` flag, you can still create a valid certificate, however the client presenting the certificate would not get any permissions in the Kubernetes API. The reason is that without that flag, both the `CN` attribute (interpreted as the user name by the Kubernetes API) and the `O` attribute of the certificate (interpreted as group name) will contain random values, so that no role bindings can match these names.
