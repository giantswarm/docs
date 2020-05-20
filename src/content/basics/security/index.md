---
title: Security
description: Documentation of the Giant Swarm cluster security
date: 2020-05-18
type: page
weight: 20
categories: ["basics"]
last-review-date: 2020-05-18
---

# Security

Regardless of provider, clusters start with restrictive settings already in place. All internal and external network traffic is denied by default, role-based access control prevents unauthorized access to Kubernetes resources, and Pod security policies are in place to prevent Pods from running with root users, risky volume configurations, or additional privileges. All of these can be adapted by the customer to fit their needs. 

We regularly test our configurations against the CIS Kubernetes Benchmark as well as other CIS and industry benchmarks for Docker, Linux, and cloud providers to ensure our platform remains compliant with industry best-practices.

Additionally, each cluster is completely isolated, running inside its own VPC (AWS) or Virtual Network (Azure) within your account. They can be further isolated by keeping clusters in different accounts. On-premises we achieve similar isolation by running the nodes in hypervisors (KVM, VMWare) and isolating clusters' networks within separate VXLAN bridges. We encourage separation of workloads over several clusters to limit the blast radius of incidents.

## Encryption at Rest

### Kubernetes {#k8s}

#### Encryption of secrets {#k8s-secrets}

Secret encryption is ensured by running the Kubernetes `api-server` with the flag `--encryption-provider-config`. This means that all secrets are stored in Etcd in encrypted form and decrypted when accessed.

The `AES-CDC` 32 Byte encryption key used is created by a custom management service (`kubernetesd`) during cluster creation. The operator component that creates the cluster retrieves this encryption key and provides it to the `EncryptionConfig` resource for `api-server`..

To learn more about secret encryption, look up [Encrypting data at rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) in the official Kubernetes documentation.

### AWS

This section applies to AWS-based installations only.

#### Encryption of local storage {#local-storage}

Non-persistent volumes as well as docker images and logs are stored under `/var/lib/docker`. On AWS, `/var/lib/docker` is an Elastic Block Storage (EBS) volume. This volume is encrypted via AWS EBS Encryption. The key is created, stored and deleted using AWS Key Management Service (KMS).

#### Encryption of persistent storage {#persistent-storage}

Persistent storage is managed by the `StorageClass` resource in Kubernetes. By default, the `StorageClass` resource is provided as an Elastic Block Storage (EBS) volumes. These volumes are encrypted via AWS EBS Encryption. The key is created, stored and deleted using AWS Key Management Service (KMS).

### Azure

This section applies to Azure-based installations only.

#### Encryption of local storage {#azure-local-storage}

kubelet data is stored under `/var/lib/kubelet`, Docker images under `/var/lib/docker` and for master nodes etcd data is stored under `/var/lib/etcd`. On Azure, `/var/lib/kubelet`, `/var/lib/docker` and `/var/lib/etcd` are Azure Managed disks (Premium SSD). Azure managed disk automatically encrypts data by default with platform-managed keys (managed by Microsoft). See more details in [Azure managed disk documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/disk-encryption).

#### Encryption of persistent storage {#azure-persistent-storage}

Persistent storage is managed by the `StorageClass` resource in Kubernetes. By default, storage class is provided by Azure Managed disks (Premium SSD). Azure managed disk automatically encrypts data by default with platform-managed keys (managed by Microsoft). See more details in [Azure managed disk documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/disk-encryption).
