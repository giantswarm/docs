---
linkTitle: Azure
title: Using Persistent Volumes on Azure
description: Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on Azure Cloud
weight: 20
menu:
  main:
    identifier: gettingstarted-persistentvolumes-azure
    parent: gettingstarted-persistentvolumes
aliases:
  - /guides/using-persistent-volumes-on-azure/
owner:
  - https://github.com/orgs/giantswarm/teams/team-celestial
---

# Using Persistent Volumes on Azure

If your cluster is running in the cloud on Azure, it comes with four dynamic storage provisioners using different flavours of Azure Disks and Azure File shares. This enables you to store data beyond the lifetime of a Pod.

## Storage Classes

The default `Storage Classes` are:

- **managed-premium** (the default one): Provisions a `Premium LRS` [`Managed disk`](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) and thus can be used only on kubernetes nodes that run on supported VM types (those with an `s` in their name).
- **managed-standard**: Provisions a `Standard LRS` [`Managed disk`](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) and can be used on any VM instance type.
- **af-premium**: Provisions a volume backed by the [`Azure File Share`](https://azure.microsoft.com/en-us/services/storage/files/) service within a `Premium LRS` storage account.
- **af-standard**: Provisions a volume backed by the [`Azure File Share`](https://azure.microsoft.com/en-us/services/storage/files/) service within a `Standard LRS` storage account.

## Creating Persistent Volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims).
Please ensure to specify the right `Storage Class` to have the desired type of volume automatically provisioned for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the Dynamic Storage Provisioner will take care that a corresponding `Azure File Share` or `Managed Disk` gets created.

The Volume and its data will persist as long as the corresponding PV resource exists. Deleting the resource will also delete the corresponding volume, which means that all stored data will be lost at that point.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume Claim you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

Note that an `Azure Disk` volumes can only be used by a single Pod at a time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

This limitation doesn't apply to `Azure File Share` volumes, that can be attached with the `ReadWriteMany` policy.

## Example

First we create a PVC:

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 6Gi
  storageClassName: managed-standard
```

Now we can create a Pod that uses our PVC:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: mypod
spec:
  containers:
    - name: myfrontend
      image: nginx
      volumeMounts:
      - mountPath: "/var/www/html"
        name: mypd
  volumes:
    - name: mypd
      persistentVolumeClaim:
        claimName: myclaim
```

Now we have an NGINX Pod which serves the contents of our Azure Managed Disk Volume.

## Expanding Persistent Volume Claims

Starting with volumes created on clusters using workload cluster release v{{% first_azure_nodepools_version %}} for Azure, Persistent Volume Claims can be expanded by simply editing the claim and requesting a larger size.
It will trigger an update in the underlying Persistent Volume and Azure Volume (Kubernetes always uses the existing one).

Please note that for `Managed Disk`-based volumes, it is mandatory to release the PVC (i.e. stop the Pod that is mounting it) before the resize operation begins.
This is a limitation of Azure Cloud that does not apply to `Azure File Share`-based volumes.

## Deleting Persistent Volumes

By default the Reclaim Policy of Persistent Volumes in your cluster is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective Azure Disk or Azure File Share.
Similarly, by default if you delete a `PersistenVolumeClaim` resource the respective Persistent Volume and Azure resource will get deleted.

Note that deleting an application that is using Persistent Volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistenVolumeClaim` resources to clean up.

## Further reading

- [Azure Managed Disks](https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
- [Azure File Share](https://azure.microsoft.com/en-us/services/storage/files/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
