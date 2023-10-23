---
linkTitle: VMware Cloud Director
title: Using persistent volumes on VMware Cloud Director
description: Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on VMware Cloud Director.
weight: 40
menu:
  main:
    identifier: gettingstarted-persistentvolumes-clouddirector
    parent: gettingstarted-persistentvolumes
user_questions:
  - How can I use persistent volumes in my VMware Cloud Director clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
last_review_date: 2023-10-05
---

If your cluster is running on VMware Cloud Director (VCD), it comes with a dynamic storage provisioner for Named Disks. This enables you to store data beyond the lifetime of a Pod into virtual disks.

## Storage Classes

Your Kubernetes cluster will have a default Storage Class `csi-vcd-sc-delete` deployed, which will automatically get selected if you do not specify the Storage Class in your Persistent Volumes. On deletion of the volume, the data is deleted. In order to avoid deleting the data when the `PersistentVolume` object is deleted, you can use the Storage Class `csi-vcd-sc-retain` which is configured with `reclaimPolicy: Retain`.

As a Cluster Admin, you can create additional Storage Classes to use different types of VMware Storage Profiles or for instance, add encryption. For this, you need to create or edit [Storage Class objects](https://kubernetes.io/docs/concepts/storage/persistent-volumes).

## Creating Persistent Volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding Persistent Volume (PV) for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the Dynamic Storage Provisioner will take care that a corresponding Named Disk with the correct parameters is created in the VMware Cloud Director OVDC.

__Note__: Do not delete virtual machines that have a Named Disk attached or it will be left in an inconsistent state and the VCD admins will need to intervene to clean it up.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume Claim you can [mount the volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your pods.

Note that a Named Disk can only be used by a single Pod at the same time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

Under the hood the Named Disk stays detached from the virtual machines as long as it is not claimed by a Pod. As soon as a Pod claims it, it gets attached to the virtual machine running the node that holds the Pod.

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
```

Note that the Access Mode, while being fixed with Named Disks, still needs to be defined as `ReadWriteOnce` in the manifest.

Further, as we are not defining a Storage Class the Kubernetes cluster will use the default storage class (here `csi-vcd-sc-delete`).

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
        name: myvol
  volumes:
    - name: myvol
      persistentVolumeClaim:
        claimName: myclaim
```

Now we have an NGINX Pod which serves the contents of our Named Disks.

## Expanding Persistent Volume Claims (not supported)

As of version 1.4.0 of the VCD Container Storage Interface (CSI), volume expansion is [currently not supported](https://github.com/vmware/cloud-director-named-disk-csi-driver/issues/27).

## Deleting Persistent Volumes

The default storage class uses `reclaimPolicy: Delete`. Thus, deleting a `PersistentVolume` resource will also delete the respective Named Disk. Similarly, if you delete a `PersistentVolumeClaim` resource, the respective `PersistentVolume` and Named Disk will get deleted.

Note that deleting an application that is using Persistent Volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistentVolumeClaim` resources to clean up.

## Further reading

- [Storage Classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
