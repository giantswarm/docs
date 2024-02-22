---
linkTitle: Azure volume encryption
title: Encrypting Persistent Volumes using Azure Key Vault
description: Tutorial on how to encrypt dynamically provisioned Persistent Volumes on Azure clusters using Azure Key Vault feature.
weight: 40
menu:
  main:
    parent: advanced-storage
user_questions:
  - How do I encrypt data on Persistent Volumes?
  - How do I secure data on Persistent Volumes?
  - How do I use Azure Key Vault?
aliases:
  - /advanced/storage/azure-pvc-encryption
  - /guides/encrypting-persistent-volumes-on-azure-with-azure-key-vault/
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2024-02-16
---

If your cluster is running in Azure infrastructure, the most common way to provision Persistent Volumes (PVs) is by using Azure Disks.

On Giant Swarm Workload clusters, the default Storage Classes already include definitions for Azure Disks as well as Azure Files. Those disks however are not encrypted with Customer-Managed keys but only with Platform-Managed keys.
In order to increase the security of your persistent data on PVs you can use the [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) service as an encryption key provider.

## Azure Key Vault setup

A prerequisite for following steps is to have a deployed Key Vault instance either in your cluster's Resource Group, or in your account. Please follow the [official docs](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) to get started.

## Create first encryption key

After successful deployment, we can move to creating the encryption key which will be used to encrypt data on your PVs.

Add a new key with a key type, RSA key size, and activation or expiration date of your choosing in the Key Vault directory.

When the creation is finished, the Key Identifier should look similar to:
`https://name-of-your-key-vault-instance.vault.azure.net/keys/test-vault-enc-key/xxxaaadddwww222111dddaaa23456789`

## Create Disk Encryption Set

The next step is to create an Azure Disk Encryption Set with the key generated in the previous step. You can use the Azure CLI or navigate in the Portal by adding a new Disk Encryption Set resource.

When creating the Set, you can specify an encryption type to use only Customer-Managed keys or provide a double encryption with additional Platform-Managed keys.
Regardless of your choice, please specify the key you have just created to be used in the Set.

Remember to add access permissions to the Key Vault instance you have created for the created Disk Encryption Set as it will need it to actually access and read the key after creation.

In the last step you will need the Resource ID of the created Disk Encryption Set looking like:
`/subscriptions/sub_id/resourceGroups/rg_where_key_vault_is/providers/Microsoft.Compute/diskEncryptionSets/name_of_your_disk_encryption_set`

## Create Storage Class with Encryption

The last step is to create your own Storage Class with the defined encryption set.

After replacing the placeholder below with your Encryption Set Resource ID, you will be able to apply the following snippet:

```yaml
kind: StorageClass
apiVersion: storage.k8s.io/v1
metadata:
  name: EncryptedDisks
provisioner: kubernetes.io/azure-disk
parameters:
  skuname: Standard_LRS
  kind: managed
  diskEncryptionSetID: "/subscriptions/sub_id/resourceGroups/rg_where_key_vault_is/providers/Microsoft.Compute/diskEncryptionSets/name_of_your_disk_encryption_set"
```

From now on, your Persistent Volumes using this storage class will have encrypted data with your Customer-Managed key.
The final step is to add the Managed Identities (Service Principals) to every Virtual Machine Scale Set which is created (both for control plane nodes and for all node pools in your cluster). This is to enable them to have access to the Key Vault instance in order to be able to read the encryption key.

## Further reading

- [Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/basic-concepts)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [BYOC with Azure disks on AKS](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys)
- [Azure Disk Encryption](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal)
