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
  - /ui-api/kubectl-gs/login/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I log in with kubectl for the Management API?
  - How can I create a workload cluster client certificate?
  - How do I specify the time to live for a workload cluster client certificate?
last_review_date: 2022-12-20
---

Use this command to set up a kubectl context to work with:

1. a management cluster, using OIDC authentication

2. a workload cluster, using OIDC authentication

3. a workload cluster, using client certificate auth (Not supported on KVM)

Note that `3` implies `1`. When setting up workload cluster access via client certificate, management cluster access will be set up as well, if that is not yet done.

## Usage

The command is called with the general syntax

```nohighlight
kubectl gs login [MANAGEMENT_CLUSTER] [WORKLOAD_CLUSTER] [FLAGS]
```

Both Arguments are optional so the command can take several shapes.

### a) `kubectl gs login`

No arguments.

- By leaving the argument empty, the command will use the current selected kubectl context. In addition, an OIDC auth token will be refreshed and the name of the current context will be printed.

### b) `kubectl gs login [MANAGEMENT_CLUSTER]`
For the `MANAGEMENT_CLUSTER` argument there are several options.

1. **Management API endpoint URL:** The URL of the cluster's Kubernetes API endpoint. This can be also be a workload cluster, if OIDC has been set up for it.

2. **Web interface URL:** The URL of the management cluster's [web UI]({{< relref "/platform-overview/web-interface/" >}}) instance.

3. **Context name:** Name of a Giant Swarm kubectl context, generated via one of the two methods above. The context name normally starts with the `gs-` prefix, however that prefix can be omitted for convenience. If no OIDC context can be found, an attempt to select a client certificate will be made.

### c) `kubectl gs login [MANAGEMENT_CLUSTER] [WORKLOAD_CLUSTER]`
The `MANAGEMENT_CLUSTER` and `WORKLOAD_CLUSTER` names are used to find an existing context for a workload cluster.
- **Context name:** Name of a Giant Swarm kubectl context. If no OIDC context can be found, an attempt to select a client certificate will be made.

It is also possible to create client certificates for a workload cluster, by providing the right configuration flags. Please be aware that the recommended way to authenticate users for workload clusters is OIDC. Client certificates should only be a temporary replacement.
When selecting client certificate contexts via the method above, please be aware that they will not be refreshed if they are expired.

### Flags

- `--keep-context`: Keep the current kubectl context selected after authenticating. If this flag is not set or false, the newly created context will be selected as the current-context.

- `--self-contained`: Output file path for a self-contained kubectl configuration file. If provided, the certificate data will be written to an external kubectl configuration file instead of the default one. Please be aware that this starts the login process from the beginning regardless of existing contexts.

For **OIDC** authentication, the following flags are available:

- `--callback-port`: Specify the TCP port number on which the OIDC callback server on localhost will be listening. If not specified, a random port number will be used. Specifying the port is useful when running kubectl-gs inside a container, or behind a firewall.

- `--token`: Use a bearer token instead of OIDC authentication, e. g. a service account token.

- `--internal-api` - (AWS only) With this flag you use an internal Management API endpoint. It resolves to an internal IP address that is only accessible from within the cluster's virtual private cloud (VPC). The hostname of this endpoint is the same as the normal one, with the prefix `internal-`. Example: if your Management API host name is `g8s.example.yourdomain.tld`, the alternative hostname is `internal-g8s.example.yourdomain.tld`.

- `--connector-id` - OIDC authentication prompts the user to select an authentication provider for the login process. The connector ID flag can be used to skip the prompt by providing an identifier of a specific authentication provider.

The following flags are related to creating **client certificates** for workload cluster access:

- `--workload-cluster` - If present, `kubectl gs` will set up a kubectl context to work with a workload cluster via client certificate creation.
- `--organization` - The organization that the workload cluster belongs to. Only required if the current user has access to multiple workload clusters with the same name in the same management cluster. Can also be applied if the user does not have permission to list organizations.
- `--certificate-group` - The RBAC group name to be encoded into the X.509 field "O". It can be specified multiple times in order to set multiple groups at once.
- `--certificate-ttl` - How long the client certificate should live for. When creating client certificates, we recommend using short expiration periods. Valid time units are "s" (second), "m" (minute), "h" (hour).
- `--cn-prefix` - The CN prefix of the common name to be encoded into the X.509 field "CN".

In addition, there is one flag **only relevant to Giant Swarm staff**:

- `--cluster-admin` - This flag enables the use of a Giant Swarm identity provider instead of the customer's one when authenticating for the management cluster.

## Examples

### Management cluster

To set up a context initially, you'll have to use either the web UI URL as an argument ...

```nohighlight
kubectl gs login https://happa.g8s.example.westeurope.azure.gigantic.io
```

... or the Management API endpoint URL.

```nohighlight
kubectl gs login https://api.g8s.example.westeurope.azure.gigantic.io
```

As a result, a context will be created with prefix `gs-` and a shorthand for this installation. Watch the command's output:

```nohighlight
Switched to context 'gs-example'.
You are logged in to the cluster 'example'.
```

For subsequent logins, you can use that shorthand to easily select which installation to log in to. Example:

```nohighlight
kubectl gs login example
```
### Workload cluster

If OIDC is set up on a workload cluster, the initial login can be done via the Management API endpoint URL as well.

```nohighlight
kubectl gs login https://api.test.g8s.example.westeurope.azure.gigantic.io
```

As a result, a context will be created with prefix `gs-` and a codename consisting of management cluster and workload cluster handles.

```nohighlight
Switched to context 'gs-example-test'.
You are logged in to the cluster 'example-test'.
```

For subsequent logins, you can use that shorthand to easily select which workload cluster to log in to. Example:

```nohighlight
kubectl gs login example test
```

### Workload cluster client certificate

Given that a context `gs-example` already exists from previous management cluster log-ins to that installation, the following command would create a client certificate with specific group assignment:

```nohighlight
kubectl gs login example \
  --workload-cluster gir0y \
  --certificate-group example-group
```

#### Certificate lifetime {#certificate-ttl}

The certificate created in the above way would have the default lifetime of **one hour**.

You can use the `--certificate-ttl` flag to specify a longer lifetime, e. g. `4h` for four hours. Since client certificates cannot be revoked, we recommend to set the lifetime as short as possible.

#### Groups and users

The generated certificate will have a X.509 subject comprising an `O` field and a `CN` field.

Example:

```nohighlight
O=73ce775d904da53e,
CN=73ce775d904da53e.i94nf.k8s.example.westeurope.azure.gigantic.io
```

When presenting such client certificate to the Kubernetes API server, the `CN` field is interpreted as the user identifier, while the `O` field is interpreted as a list of groups the user is a member of.

With these values defaulting to random strings, we ensure that a client presenting this certificate does not accidentally acquire any permissions based on pre-defined group or user names in any (cluster) role bindings.

To assign specific group memberships, or in other terms, to specify additional `O` values in the created certificate, you'll have to use the `--certificate-group` flag when executing the command. This flag can be set multiple times, with one group name each, as shown in the example below.

Example command:

```nohighlight
$ kubectl gs login garlic \
  --workload-cluster i94nf \
  --certificate-group group1 \
  --certificate-group group2
```

The resulting client certificate would have a subject like this:

```nohighlight
O=group1,
O=group2,
O=5ab261600796bef7,
CN=5ab261600796bef7.i94nf.k8s.example.westeurope.azure.gigantic.io
```

#### Creating a client certificate in automation {#wc-client-cert-automation}

Creating a client certificate for a workload cluster requires access to the management cluster. This is simple for users who can first use `kubectl gs login` against the management cluster and are then authenticated.

In an automation context, an interactive login with a personal authentication, potential using multiple authentication factors, is not possible. In this case, a **service account token** can be used to authenticate against the management cluster.

Giant Swarm provides a `ClusterRole` named `write-client-certificates` which provides the permissions required to create a workload cluster certificate. Bind this role to your service account in the namespace of the organization owning the workload cluster, to grant the required permissions. The [access control]({{< relref "/platform-overview/web-interface/organizations/access-control" >}}) user interface makes this simple.

Finally, this example shows how to execute the command using a service account token via the `--token` flag to authenticate:

```nohighlight
kubectl gs login garlic \
  --token SERVICE_ACCOUNT_TOKEN \
  --workload-cluster i94nf \
  --certificate-ttl 24h \
  --certificate-group example-group \
  --self-contained kubeconfig.yaml
```

Here, `garlic` is the installation codename. `i94nf` is the workload cluster name. And `SERVICE_ACCOUNT_TOKEN` has to be replaced with the token string.
