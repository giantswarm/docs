---
linkTitle: Persistent Volumes data encryption with Azure Key Vault
title: Encrypting Persistent Volumes using Azure Key Vault
description: Tutorial on how to encrypt dynamically provisioned Persistent Volumes on Azure clusters using Azure Key Vault feature.
weight: 40
menu:
  main:
    parent: advanced-storage
user_questions:
  - How do I encrypt data on Persistent Volumes?
  - How do I secure data on Persistent Volumes?
aliases:
  - /guides/encrypting-persistent-volumes-on-azure-with-azure-key-vault/
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
---

# Using Persistent Volumes on Azure

If your cluster is running in Azure infrastructure, most common way to provision Persistent Volumes is by using the Azure Disks.

On Giant Swarm Workload clusters, the default Storage Classes already include definitions for Azure Disks as well as Azure Files. Those disks however are not encrypted with Customer-Managed keys but only with Platform-Managed keys.
In order to increase the security of your persistent data on PVs you can use the [Azure Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) service as an encryption key provider.

## Azure Key Vault setup

Prerequisite for next steps is to have a deployed Key Vault instance either in your clusters Resource Group or in your account. Please follow the [official docs](https://docs.microsoft.com/en-us/azure/key-vault/general/overview) to get started.

## Create first encryption key

After successful deployment we can move to creating encryption key that will be used to encrypt data on your PVs.

Add a new key with key type, RSA key size, activation or expiration date of your choosing in the Key Vault directory.

When creation is finished, the Key Identifier should look similar to:
```https://name-of-your-key-vault-instance.vault.azure.net/keys/test-vault-enc-key/xxxaaadddwww222111dddaaa23456789```

## Create Disk Encryption Set

Next step is to create a Azure Disk Encryption Set with the key generated in previous step. You can use Azure CLI or navigate in the Portal by adding a new Disk Encryption Set resource.

When creating the Set, you can specify encryption type which should use only Customer-Managed keys or provide a double encryption with additional Platform-Managed keys.
Regardless of your choice, please specify the key you have just created to be used in the Set.

Remember to add access permissions to the Key Vault instance you have created for the created Disk Encryption Set as it will need it to actually access and read the key after creation.

In the last step you will need the Resource ID of the created Disk Encryption Set looking like:
```/subscriptions/sub_id/resourceGroups/rg_where_key_vault_is/providers/Microsoft.Compute/diskEncryptionSets/name_of_your_disk_encryption_set```

## Create Storage Class with Encryption

Last step is to create your own Storage Class with the defined encryption set.

After adjusting with your Encryption Set Resource ID, you will be able to apply following code:

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
The final step is to add the Managed Identities (Service Principals) per Virtual Machine Scale Set that are created both for master and for all node pools in your cluster to also have access to the Key Vault instance in order to be able to read the encryption key.

## Further reading

- [Key Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/basic-concepts)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [BYOC with Azure disks on AKS](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys)
- [Azure Disk Encryption](https://docs.microsoft.com/en-us/azure/virtual-machines/disks-enable-customer-managed-keys-portal)
