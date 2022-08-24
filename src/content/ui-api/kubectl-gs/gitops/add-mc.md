---
linkTitle: add management-cluster
title: "'kubectl gs gitops add mc' command reference"
description: Reference documentation on how to add a new Management Cluster to the GitOps repository.
weight: 100
menu:
  main:
    parent: kubectlgs-gitops
aliases:
  - /reference/kubectl-gs/gitops/add-mc/
last_review_date: 2022-08-16
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I configure Management Cluster in the GitOps repository?
---

This command configures the GitOps repository with a new Management Cluster.

Depends on:
- [gitops init](init.md)

## Description

The structure created by this command is presented below. Resources enclosed in a square brackets `[]` are considered optional.

```nohighlight
management-clusters
└── MC_NAME
    ├── .sops.keys
    |   └── [master.KEY_FINGERPRINT.asc]
    ├── secrets
    |   └── MC_NAME.gpgkey.enc.yaml
    ├── organizations
    └── MC_NAME.yaml

```

**Note**, in a default mode creation of the SOPS GPG key pair is skipped by the command. It is because in its most basic
form GitOps repository can be driven without encryption. To enable the keys creation pass the `--gen-master-key` flag
when running `kubectl-gs`.

## Flags

| Name              | Description                                          |
| ----------------- | ---------------------------------------------------- |
| `name`            | Codename of the Management Cluster.                  |
| `repository-name` | Name of the GitOps repository.                       |
| `gen-master-key`  | Generate Management Cluster master GPG key for SOPS. |


## Usage

The command to execute is `kubectl gs gitops add mc`.

To preview the objects to be created by the command, run it with the `--dry-run` flag. Example:

```nohighlight
kubectl gitops add mc \
--local-path /tmp/gitops-demo \
--name demomc \
--repository-name gitops-demo \
--dry-run

/tmp/gitops-demo/management-clusters/demomc
/tmp/gitops-demo/management-clusters/demomc/demomc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-gitops
  namespace: default
spec:
  interval: 1m
  path: ./management-clusters/demomc
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/management-clusters/demomc/secrets
/tmp/gitops-demo/management-clusters/demomc/secrets/demomc.gpgkey.enc.yaml
apiVersion: v1
kind: Secret
metadata:
    name: sops-gpg-master

/tmp/gitops-demo/management-clusters/demomc/.sops.keys
/tmp/gitops-demo/management-clusters/demomc/organizations
```

Upon passing the `--gen-master-key` flag, the output will be also enriched with a GPG key pairs, see example:

```nohighlight
kubectl gitops add mc \
--local-path /tmp/gitops-demo \
--name demomc \
--repository-name gitops-demo \
--gen-master-key \
--dry-run

/tmp/gitops-demo/management-clusters/demomc
/tmp/gitops-demo/management-clusters/demomc/demomc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-gitops
  namespace: default
spec:
  decryption:
    provider: sops
    secretRef:
      name: sops-gpg-master
  interval: 1m
  path: ./management-clusters/demomc
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/management-clusters/demomc/secrets
/tmp/gitops-demo/management-clusters/demomc/secrets/demomc.gpgkey.enc.yaml
apiVersion: v1
data:
  master.e11262662a86090ea64c8b137235e9a0582989cc.asc: LS0tLS1CRUdJTiBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQpDb21tZW50OiBodHRwczovL2dvcGVucGdwLm9yZwpWZXJzaW9uOiBHb3BlblBHUCAyLjQuOAoKeFZnRVl3WllWeFlKS3dZQkJBSGFSdzhCQVFkQVF0d3JLWjJ5MzZzaXZ4TXlMR0ZXTExlUmFlWGQzNHAxampNRgpWbUZLOHRBQUFRREZzWWlZU0ZrcjBHTzc4aDFrOGs0OGZHbVpibWgxVjZjWEtDV3Y0dlhnTnhBSXpSSmtaVzF2CmJXTWdSbXgxZUNCdFlYTjBaWExDakFRVEZnZ0FQZ1VDWXdaWVZ3bVFjalhwb0ZncGljd1dJUVRoRW1KbUtvWUoKRHFaTWl4TnlOZW1nV0NtSnpBSWJBd0llQVFJWkFRTUxDUWNDRlFnREZnQUNBaUlCQUFDOStnRUFzSy85bjBZTwpnRytFaWJsdmdDMnRtc0wwUlAxRXRKNWNBYnhxMDNTNk5Rd0JBTDk1STBkeFByblFwN3NOUzhacnVrL3lKalpECldvbnhQOTROekRndHNaNER4MTBFWXdaWVZ4SUtLd1lCQkFHWFZRRUZBUUVIUUptZmpJNW8zenJqWnhDdWVhK0gKcTh5UXRXWjBSQTM2RWRsTUM4cG9IUzRHQXdFS0NRQUEvMEl3NUw1NVlkc05zRGkrQzlrV1c4V1lIWGRSbGxTVwphcXlwT21MeDVtSUFFQ2JDZUFRWUZnZ0FLZ1VDWXdaWVZ3bVFjalhwb0ZncGljd1dJUVRoRW1KbUtvWUpEcVpNCml4TnlOZW1nV0NtSnpBSWJEQUFBSU9jQS8wc2Fib0xIUzRQWENTWVU3c3VQZ01vbjk2S3U0WGt2aUZnRUxzZS8KU3hxdkFRQ2lBZHIxQkZLZ1pGR2wyZ1dkUWZySklXQjhKVHZFK3ZnV1d4SEJZVkgyQUE9PQo9QXErRwotLS0tLUVORCBQR1AgUFJJVkFURSBLRVkgQkxPQ0stLS0tLQ==
kind: Secret
metadata:
    name: sops-gpg-master

/tmp/gitops-demo/management-clusters/demomc/.sops.keys
/tmp/gitops-demo/management-clusters/demomc/.sops.keys/master.e11262662a86090ea64c8b137235e9a0582989cc.asc
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GopenPGP 2.4.8
Comment: https://gopenpgp.org

xjMEYwZYVxYJKwYBBAHaRw8BAQdAQtwrKZ2y36sivxMyLGFWLLeRaeXd34p1jjMF
VmFK8tDNEmRlbW9tYyBGbHV4IG1hc3RlcsKMBBMWCAA+BQJjBlhXCZByNemgWCmJ
zBYhBOESYmYqhgkOpkyLE3I16aBYKYnMAhsDAh4BAhkBAwsJBwIVCAMWAAICIgEA
AL36AQCwr/2fRg6Ab4SJuW+ALa2awvRE/US0nlwBvGrTdLo1DAEAv3kjR3E+udCn
uw1Lxmu6T/ImNkNaifE/3g3MOC2xngPOOARjBlhXEgorBgEEAZdVAQUBAQdAmZ+M
jmjfOuNnEK55r4erzJC1ZnREDfoR2UwLymgdLgYDAQoJwngEGBYIACoFAmMGWFcJ
kHI16aBYKYnMFiEE4RJiZiqGCQ6mTIsTcjXpoFgpicwCGwwAACDnAP9LGm6Cx0uD
1wkmFO7Lj4DKJ/eiruF5L4hYBC7Hv0sarwEAogHa9QRSoGRRpdoFnUH6ySFgfCU7
xPr4FlsRwWFR9gA=
=nBrl
-----END PGP PUBLIC KEY BLOCK-----

/tmp/gitops-demo/management-clusters/demomc/organizations
/tmp/gitops-demo/.sops.yaml
creation_rules:
- encrypted_regex: ^(data|stringData)$
  path_regex: management-clusters/demomc/secrets/.*\.enc\.yaml
  pgp: e11262662a86090ea64c8b137235e9a0582989cc
```

Remove the `--dry-run` flag and re-run it to apply the changes.
