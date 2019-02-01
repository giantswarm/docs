+++
title = "gsctl Command Reference: create keypair"
description = "The 'gsctl create keypair' command creates a key pair and stores the related files in your certificate folder."
date = "2018-10-12"
type = "page"
weight = 32
+++

# `gsctl create keypair`

The `gsctl create keypair` command creates a key pair and stores the related files in your certificate folder.

If you intend to use the created key pair with the `kubectl` program, we recommend you take a look at the [`create kubeconfig`](../create-kubeconfig/) command. It creates a new key pair and adds the according user, server, and context entries to your `kubectl` configuration.

## Examples {#example}

Given you have a cluster with the ID `w6wn8`, this command would create a new key pair for that cluster:

```nohighlight
$ gsctl create keypair --cluster w6wn8
```

The output will look similar to the one below:

```nohighlight
New key pair created with ID 114e2de892b2dcfdf96c92f3c69f39e564ecec1e and expiry of 30 days
CA certificate stored in: /Users/myself/.config/gsctl/certs/pmb9q-ca.crt
Client certificate stored in: /Users/myself/.config/gsctl/certs/pmb9q-114e2de892-client.crt
Client private key stored in: /Users/myself/.config/gsctl/certs/pmb9q-114e2de892-client.key
```

This informs you that a new key pair has been created. It will expire after a default time of 30 days.

Three files will be placed in the `certs` folder, which is a subfolder of your gsctl configuration folder:

- The CA certificate file (name schema: `<cluster_id>-ca.crt`), which technically is not really a part of your personal key pair, but required to access the Kubernetes API for the cluster.

- Your private key (file ending `.key`)

- Your client certificate (file ending `.crt`).

## Full argument reference {#arguments}

- `--cluster`, `-c`: Used to specify the cluster ID to create a key pair for.
- `--cn-prefix`: The common name prefix for the issued certificates 'CN' field.
  Note that only the charactes `a-z`, `0-9` and `-` can be used.
- `--certificate-organizations`: A comma separated list of organizations for the issued certificate's 'O' fields.
- `--description`, `-d`: Can be used to specify a description. If not given, a description like `Added by user email@example.com using 'gsctl create kubeconfig'` is set.
- `--ttl`: Allows to set the key pair expiry, in days. Defaults to 30 days.

## Key pair expiry {#expiry}

Each key pair has a limited lifetime, which you can affect only on creation. In general, we suggest using short-lived key pairs for security reasons.

Depending on the installation, there might be a minimum and maximum key pair lifetime configured, to enforce security policies. If you'd like to find out about effective limits of your installation, please ask our support team.

## Kubernetes RBAC and the certificate's subject common name and organization fields.

Using the `--certificate-organizations` and `--cn-prefix` flags you can influence the common name (CN) and organization (O) fields of the issued certificate.

Kubernetes will take these values and map them to the username and group memberships respectively. This will let you set up fine grained permissions for the certificates that you issue by applying [RBAC authorization](https://kubernetes.io/docs/admin/authorization/rbac/) resources to your cluster.

__Warning:__ Setting `system:masters` as an organization means the user who uses the issued keypair has `cluster-admin` rights in the selected cluster. It is a good practice to use finer grained roles, only giving the least privileges possible to the users ([PoLP](https://en.wikipedia.org/wiki/Principle_of_least_privilege)). Please consider using existing roles like `admin`, `edit` or `view` instead, or creating new custom roles with needed permission.

## Related

- [`gsctl create kubeconfig`](../create-kubeconfig/): Create a key pair and prepare your kubectl configuration to access the cluster.
- [API: Create key pair](/api/#operation/addKeyPair)
