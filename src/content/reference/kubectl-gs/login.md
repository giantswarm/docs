---
linkTitle: login
title: "'kubectl gs login' command reference"
diataxis_content_type: reference
description: Reference documentation on how to ensure an authenticated kubectl context for a Giant Swarm management or workload cluster, using 'kubectl gs'.
weight: 60
menu:
  principal:
    identifier: reference-kubectlgs-login
    parent: reference-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/team-bumblebee
user_questions:
  - How can I log in with kubectl for the platform API?
  - How can I create a workload cluster client certificate?
  - How do I specify the time to live for a workload cluster client certificate?
last_review_date: 2026-06-08
aliases:
  - /vintage/use-the-api/kubectl-gs/login/
  - /vintage/use-the-api/management-api/wc-key-pairs/
  - /use-the-api/management-api/wc-key-pairs/
  - /ui-api/management-api/wc-key-pairs/
---

Use this command to set up a kubectl context to work with:

1. a management cluster, using OIDC authentication

2. a workload cluster, using OIDC authentication

3. a workload cluster, using client certificate authentication

4. a workload cluster, using AWS IAM authentication (EKS clusters only)

5. a workload cluster, using direct OIDC authentication (Kubernetes structured authentication)

The appropriate workload cluster mode (2–5) is selected automatically based on the cluster's configuration. Mode 3 implies mode 1: when setting up workload cluster access via client certificate, management cluster access will be set up as well, if that is not yet done.

## Usage

The command is called with the general syntax

```nohighlight
kubectl gs login [MANAGEMENT_CLUSTER] [WORKLOAD_CLUSTER] [FLAGS]
```

Both arguments are optional, so the command can take several shapes.

### a) `kubectl gs login`

No arguments.

By leaving the argument empty, the command will use the current selected kubectl context. In addition, an OIDC auth token will be refreshed and the name of the current context will be printed.

### b) `kubectl gs login [MANAGEMENT_CLUSTER]`

For the `MANAGEMENT_CLUSTER` argument there are several options.

1. **Platform API endpoint URL:** The URL of the cluster's Kubernetes API endpoint. This can also be a workload cluster, if OIDC has been set up for it.

2. **Context name:** Name of a Giant Swarm kubectl context, generated via one of the two methods above. The context name normally starts with the `gs-` prefix, however that prefix can be omitted for convenience. If no OIDC context can be found, an attempt to select a client certificate will be made.

### c) `kubectl gs login [MANAGEMENT_CLUSTER] [WORKLOAD_CLUSTER]`

The `MANAGEMENT_CLUSTER` and `WORKLOAD_CLUSTER` names are used to find an existing context for a workload cluster.

It is also possible to create client certificates for a workload cluster by providing the right configuration flags. Please be aware that the recommended way to authenticate users for workload clusters is OIDC. Client certificates should only be a temporary replacement. When selecting client certificate contexts via the method above, please be aware that they will not be refreshed if they are expired.

## Flags

### General flags

- `--keep-context`: Keep the current kubectl context selected after authenticating. If not set, the newly created context will be set as the current context. Can also be set via the `KUBECTL_GS_LOGIN_KEEP_CONTEXT` environment variable.

- `--self-contained`: Path to write a self-contained kubectl configuration file with embedded credentials. When provided, certificate data is written to this external file instead of the default kubeconfig. This always starts the login process from scratch, regardless of existing contexts.

### OIDC authentication flags

- `--callback-port`: TCP port for the OIDC callback server on localhost. If not specified, a random free port is used. Useful when running inside a container or behind a firewall.

- `--callback-host`: Address the OIDC callback server listens on. Defaults to `localhost`. Set to an empty value or `0.0.0.0` to listen on all interfaces. Note: the redirect URL always contains `http://localhost`, as that is the registered allowed URL.

- `--login-timeout`: How long to wait for the OIDC browser-based login to complete before failing. Defaults to `1m`. Valid time units are `s`, `m`, `h`.

- `--token`: Use a bearer token instead of the interactive OIDC flow, e.g. a service account token.

- `--connector-id`: Skip the authentication provider selection prompt by providing a specific provider (Dex connector) identifier.

- `--device-auth`: Use the Device authentication flow. Instead of opening a browser automatically, the authentication URL is printed to standard output. This is suitable for headless environments where no browser is available. More details in the [example](#device-authentication-flow) below.

- `--internal-api`: (AWS only) Use the internal platform API endpoint instead of the public one. The internal endpoint resolves to an IP address accessible only from within the cluster's VPC.

- `--oidc-scope`: Additional OIDC scopes to request from the issuer, on top of the defaults (`openid`, `profile`, `email`, `offline_access`). The flag can be repeated or given a comma-separated list. Example: `--oidc-scope=groups` to receive group memberships from Okta into the ID token.

### Client certificate flags

The following flags are used when creating client certificates for workload cluster access (`--workload-cluster` implies a certificate will be created):

- `--workload-cluster`: Name of the workload cluster to create a client certificate for.
- `--organization`: The organization that owns the workload cluster. Required if multiple workload clusters share the same name in the same management cluster. Can also be used if the user does not have permission to list organizations.
- `--certificate-group`: RBAC group name to encode into the X.509 `O` field. Can be specified multiple times to assign multiple groups.
- `--certificate-ttl`: Lifetime of the client certificate. Defaults to `1h`. Valid time units are `ms`, `s`, `m`, `h`. Since client certificates cannot be revoked, we recommend keeping this as short as possible.
- `--cn-prefix`: Prefix for the common name encoded in the X.509 `CN` field.
- `--proxy`: Enable a SOCKS proxy entry in the generated kubeconfig. Only supported for client certificate authentication.
- `--proxy-port`: Port for the SOCKS proxy. Defaults to `9000`.

### Direct OIDC (structured authentication) flags

When a workload cluster uses Kubernetes structured authentication, the OIDC issuer URL, client ID, and API server CA are auto-discovered from the management cluster. The following flags override the discovered values:

- `--oidc-issuer`: Override the OIDC issuer URL.
- `--oidc-client-id`: Override the OIDC client ID. When both `--oidc-issuer` and `--oidc-client-id` are set, the management cluster is not contacted for auto-discovery.
- `--api-ca-file`: Path to a CA certificate file for the workload cluster API server. When set, skips fetching the CA from the management cluster.

### EKS (AWS IAM) flags

- `--aws-profile`: AWS profile name to embed in the generated kubeconfig. The profile is set as `AWS_DEFAULT_PROFILE` in the credential exec plugin. Only applicable to EKS clusters.

### Giant Swarm staff flags

- `--cluster-admin`: Enables use of a Giant Swarm identity provider instead of the customer's one when authenticating for the management cluster.

## Examples

### Management cluster

To set up a context initially, use the platform API endpoint URL:

```nohighlight
kubectl gs login https://api.example.yourdomain.tld
```

As a result, a context will be created with the `gs-` prefix and a shorthand for this installation:

```nohighlight
A new kubectl context 'gs-example' has been created and selected.
You are logged in to the cluster 'example'.
```

For subsequent logins, use the shorthand:

```nohighlight
kubectl gs login example
```

### Device authentication flow {#device-authentication-flow}

Run the `login` command with the `--device-auth` flag to authenticate using the device flow:

```nohighlight
kubectl gs login example --device-auth
```

The command prints the authentication URL instead of opening a browser automatically:

```nohighlight
Open this URL in the browser to log in:
https://dex.example.yourdomain.tld/device?user_code=USER-CODE

The process will continue automatically once the in-browser login is completed
```

Copy the URL, open it in a browser and follow the on-screen steps. Once complete, `kubectl gs` finishes automatically:

```nohighlight
Logged in successfully as 'your-user' on cluster 'example'.

A new kubectl context 'gs-example' has been created and selected. To switch back to this context later, use either of these commands:

  kubectl gs login example
  kubectl config use-context gs-example
```

**Note:** If you use a shorthand with an existing valid context, `--device-auth` is ignored. The command will output a warning in this case.

### Workload cluster

For subsequent logins to a workload cluster with an existing context:

```nohighlight
kubectl gs login example mywc
```

To create a client certificate for a workload cluster:

```nohighlight
kubectl gs login example \
  --workload-cluster mywc \
  --organization acme \
  --certificate-group example-group
```

#### Certificate lifetime {#certificate-ttl}

The certificate created in the above way has a default lifetime of **one hour**.

Use `--certificate-ttl` to specify a longer lifetime, e.g. `4h` for four hours. Since client certificates cannot be revoked, we recommend setting the lifetime as short as possible.

#### Groups and users

The generated certificate has an X.509 subject with an `O` field (groups) and a `CN` field (user identifier). Both default to random strings to avoid accidental permission grants from pre-existing role bindings.

To assign specific group memberships, use `--certificate-group`. The flag can be set multiple times:

```nohighlight
kubectl gs login example \
  --workload-cluster mywc \
  --certificate-group group1 \
  --certificate-group group2
```

#### Creating a client certificate in automation {#wc-client-cert-automation}

In an automation context where interactive login is not possible, use a service account token via `--token`:

Giant Swarm provides a `ClusterRole` named `write-client-certificates` with the permissions required to create a workload cluster certificate. Bind this role to your service account in the namespace of the organization that owns the workload cluster.

```nohighlight
kubectl gs login example \
  --token SERVICE_ACCOUNT_TOKEN \
  --workload-cluster mywc \
  --certificate-ttl 24h \
  --certificate-group example-group \
  --self-contained kubeconfig.yaml
```

### Direct OIDC (structured authentication)

For workload clusters configured with Kubernetes structured authentication, the OIDC parameters are auto-discovered from the management cluster. No extra flags are needed in most cases:

```nohighlight
kubectl gs login example \
  --workload-cluster mywc \
  --organization acme
```

To override the discovered values (e.g. for scripted use without management cluster access):

```nohighlight
kubectl gs login example \
  --workload-cluster mywc \
  --organization acme \
  --oidc-issuer https://login.example.com/tenant-id \
  --oidc-client-id my-client-id \
  --api-ca-file /path/to/ca.crt
```
