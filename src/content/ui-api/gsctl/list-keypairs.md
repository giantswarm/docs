---
linkTitle: list keypairs
title: "'gsctl list keypairs' command reference"
description: "Dokcumentation of the 'gsctl list keypairs' command, which prints a list of all key pairs currently valid for accessing a workload cluster."
weight: 140
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/list-keypairs/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl list keypairs`

The `gsctl list keypairs` command lists information on key pairs for a cluster. This is useful to
understand which key pairs have been issued when and, if details are given,
for what purpose. It is also helpful for setting up
[role based access control]({{< relref "/getting-started/rbac-and-psp" >}}) (RBAC) rules
in the cluster.

Note that key pair information can only by shown as long as the key pair has
not expired.

## Key pairs {#definition}

Giant Swarm offers [X.509](https://en.wikipedia.org/wiki/X.509) client
certificates as a means to authenticate with the Kubernetes API of a cluster.
As usual, a certificate comes in pairs with a private key, hence the name
"key pair".

gsctl allows you to issue a new key pair using the two commands
[`gsctl create keypair`]({{< relref "/ui-api/gsctl/create-keypair" >}}) and
[`gsctl create kubeconfig`]({{< relref "/ui-api/gsctl/create-kubeconfig" >}}). These commands request the
creation of a new key pair in the cluster's public key infrastructure (PKI) and
download it to the client. The PKI stores metadata about the issued key pairs,
but not the key pairs themselves.

## Usage and output {#usage}

The command requires as an argument the ID of the cluster to list key pairs for.

```nohighlight
gsctl list keypairs --cluster f01r4
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl list keypairs --cluster "Cluster name"
```

The resulting output is a table containing the following columns:

- `CREATED`: Date and time of creation
- `EXPIRES`: Date and time of expiry. The client certificate won't be accepted after that.
- `ID`: An identifier unique within the PKI
- `DESCRIPTION`: A descriptive text assigned at key pair creation
- `CN`: The certificate's CN field that is part of the _Subject_ field of the certificate
- `O`: The optional O field that, if set, also becomes part of the _Subject_ field
of the certificate. This assigns the client presenting the certificate to one or more RBAC groups.

The `CN` and `O` fields both form the _Subject_ field of the key pair. If the `O` field is empty,
the subject has the form `CN=<CN value>`. If the `O` field is not empty, the subject will have
the format `O=<O value>, CN=<CN value>`.

Output is truncated by default for a better overview. Truncation can be turned off
by adding the `--full` flag to the command.

Example output:

```nohighlight
CREATED                 EXPIRES                 ID          DESCRIPTION                                                         CN                        O
2018 Apr 09, 14:05 UTC  2018 May 09, 14:05 UTC  4f16e3ac4…  Added by user abc123@giantswarm.io using 'gsctl create kubeconfig'  abc123@giantswarm.io.us…  system:masters
2018 Apr 10, 08:24 UTC  2018 May 10, 08:24 UTC  4ce4d5469…  Added by user def456@giantswarm.io using 'gsctl create kubeconfig'  def456@giantswarm.io.us…  
```

## Related

- [`gsctl create keypair`]({{< relref "/ui-api/gsctl/create-keypair" >}})
- [`gsctl create kubeconfig`]({{< relref "/ui-api/gsctl/create-kubeconfig" >}})
- [Securing your cluster with RBAC and PSP]({{< relref "/getting-started/rbac-and-psp" >}})
- [API: Get key pairs](/api/#operation/getKeyPairs)
- [X.509 on Wikipedia](https://en.wikipedia.org/wiki/X.509)
