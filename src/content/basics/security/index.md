+++
title = "Security reference"
description = "Documentation of the Giant Swarm cluster security"
date = "2017-10-12"
type = "page"
weight = 15
+++

# Security reference

This reference gives you details on security-related measures in a Giant Swarm installation.

## Encryption

### Kubernetes {#k8s}

#### Encryption of Secrets {#k8s-secrets}

Secret encryption is ensured by running the Kubernetes `api-server` with the flag `--experimental-encryption-provider-config`. This means that all secrets are stored in Etcd in encrypted form and decrypted when accessed.

The `AES-CDC` 32 Byte encryption key used is created by a custom management service (`kubernetesd`) during cluster creation. The operator component that creates the cluster retrieves this encryption key and provides it to the `EncryptionConfig` resource for `api-server`..

To learn more about secret encryption, look up [Encrypting data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) in the official Kubernetes documentation.

### AWS

This section applies to AWS-based installations only.

#### Encryption of Local Storage {#local-storage}

Non-persistent volumes as well as docker images and logs are stored under `/var/lib/docker`. On AWS, `/var/lib/docker` is an Elastic Block Storage (EBS) volume. This volume is encrypted via AWS EBS Encryption. The key is created, stored and deleted using AWS Key Management Service (KMS).

#### Encryption of Persistent Storage {#persistent-storage}

Persistent storage is managed by the `StorageClass` resource in Kubernetes. By default, the `StorageClass` resource is provided as an Elastic Block Storage (EBS) volumes. These volumes are encrypted via AWS EBS Encryption. The key is created, stored and deleted using AWS Key Management Service (KMS).

