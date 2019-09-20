+++
title = "gsctl Command Reference: create kubeconfig"
description = "The 'gsctl create kubeconfig' command creates a key pair and adds cluster, user, and context settings to your kubectl configuration."
date = "2018-10-12"
type = "page"
weight = 30
+++

# `gsctl create kubeconfig`

The `gsctl create kubeconfig` command is used to configure [kubectl](https://kubernetes.io/docs/reference/kubectl/overview/) for access to
a cluster in your Giant Swarm installation. It can operate in two different
modes:

- By default, **your standard kubectl configuration file will be modified**. A
  cluster, user, and context entry are added. A client certificate together
  with a private key and the CA certificate of the cluster are placed in
  your gsctl configuration directory.

- Alternatively, a **self-contained kubectl configuration file can be created**.
  This is useful when you would like to keep things separate, or if you want to
  hand the file to someone. Here, certificate, key, and CA certificate are
  stored inline in the file. To enable this behaviour, use the flag
  `--self-contained` and set it's value to the desired output file path.

In both cases, a new key pair will be created in your installation, just as it
is the case with the [`gsctl create keypair`](../cerate-keypair/) command.

As a prerequisite, you need to be logged in to `gsctl` and you have to be
a member of the organization owning the cluster. If you can find the cluster
using [`gsctl list clusters`](../list-clusters/), this is the case.

## Command Line Examples {#example}

To create a new key pair with default settings and modify your kubectl
configuration, you can execute the command like here (where `w6wn8` is
an example for a cluster ID):

```nohighlight
$ gsctl create kubeconfig --cluster w6wn8
```

The output of the command gives details on what exactly happens.

- A new key pair is created and downloaded to files. This consists of a client
  certificate and the according private key. This key pair has an expiry. When
  not set specifically using the `--ttl` flag, a default is used. **Note:**
  Since client certificates in Kubernetes cannot be revoked, we recommend to
  set short expiry periods.
- The kubectl configuration file is altered to add a cluster, a user and a
  context entry. The context is named in the form `giantswarm-<cluster_id>`,
  but this can be overwritten using the `--context` flag.
- The new context is selected so that you can directly start using kubectl
  with the cluster.

The next example shows creation of a self-contained configuration file:

```nohighlight
$ gsctl create kubeconfig -c w6wn8 --self-contained kubeconfig.yaml
```

Here, the file `kubeconfig.yaml` will be created and it will contain the
credentials data. If the file already exists, an interactive confirmation to
overwrite this file will be required. The confirmation can be suppressed using
`--force`.

The next example shows the creation of a self-contained configuration file with
internal Kubernetes API endpoint.


```nohighlight
$ gsctl create kubeconfig -c w6wn8 --self-contained kubeconfig.yaml \
  --tenant-internal=true
```

Here , the file `kubeconfig.yaml` will be created and will container internal
Kubernetes API fqdn reference in `server` field. Currently, only AWS supports
internal Kubernetes API access.

To conclude the examples sections, here is a more complex example showing how
to create admin access (valid for one day only) in a self-contained file:

```nohighlight
$ gsctl create kubeconfig --cluster w6wn8 \
  --description "Admin certificate for Jane" \
  --ttl 1 \
  --self-contained kubeconfig-w6wn8-jane.yaml \
  --certificate-organizations system:masters
```

## Argument reference {#arguments}

- `--cluster`, `-c`: Used to specify the cluster ID to create a key pair for.
- `--ttl`: Allows to set the key pair expiry, in days. Defaults to 30 days.
- `--description`, `-d`: Can be used to specify a description. If not given, a
  description like `Added by user email@example.com using 'gsctl create
  kubeconfig'` is set.
- `--self-contained`: This option sets the path for a self-contained kubectl
  config file. Credentials will be included. The file will contain only one
  user, one cluster, and one context. When this option is used, the default
  kubectl config file is not altered.
- `--tenant-internal`: This option sets whether internal endpoint should be used
  to access Kubernetes API.
- `--force`: Always overwrite existing files without prompt when using `--self-contained`.
- `--context`: Allows to set the context name to be used in the config file.
  Defaults to `giantswarm-` plus the cluster ID. This name is used with the
  `kubectl config use-context` command to select the context.
- `--cn-prefix`: The common name prefix for the issued certificates 'CN' field.
  Note that only the charactes `a-z`, `0-9` and `-` can be used.
- `--certificate-organizations`: A comma separated list of organizations for the
  issued certificate's 'O' fields.

## Key pair expiry {#expiry}

A key pair has a limited lifetime, which you can affect only on creation. In
general, we suggest using short-lived key pairs for security reasons, since
Kubernetes does not allow to revoke certificates.

Depending on the installation, there might be a minimum and maximum key pair
lifetime configured, to enforce security policies. If you'd like to find out
about effective limits of your installation, please ask our support team.

## Manipulation of your kubectl configuration {#kubectl-manipulation}

When not using the `--self-contained` flag, your kubectl configuration file is
modified just as if you would manually apply the following commands:

- `kubectl config set-credentials [flags] giantswarm-<cluster-id>-user`
- `kubectl config set-cluster [flags] giantswarm-<cluster-id>`
- `kubectl config set-context [flags] <context-name>`
- `kubectl config use-context <context-name>`

kubectl has its ways to decide which configuration file to use and modify. By
default, the location `$HOME/.kube/config` is used. This can be overwritten
using the `KUBECONFIG` environment variable.

Whenever you execute the `create kubeconfig` command again for the same cluster,
existing entries with this name get overwritten. Should you ever manually edit
one of these entries, be aware that these changes might be overwritten by gsctl.

Once your key pair has expired, the re-execution of `gsctl create kubeconfig`
with the according flags will request and download a fresh key pair and update
the paths to certificates and the key in the user and cluster entry.

Old certificates and keys are not removed when new key pairs are fetched.

## Kubernetes RBAC and the certificate's subject common name and organization fields {#rbac}

Using the `--certificate-organizations` and `--cn-prefix` flags you can
influence the common name (CN) and organization (O) fields of the issued
certificate.

Kubernetes will take these values and map them to the username and group
memberships respectively. This will let you set up fine grained permissions for
the certificates that you issue by applying
[RBAC authorization](https://kubernetes.io/docs/admin/authorization/rbac/)
resources to your cluster.

## Related

- [`gsctl create keypair`](../cerate-keypair/): Create and download a key pair
- [kubectl reference](https://kubernetes.io/docs/user-guide/kubectl-overview/)
- [API: Create key pair](/api/#operation/addKeyPair)
