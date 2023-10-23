---
linkTitle: VMware vSphere
title: Using persistent volumes on VMware vSphere
description: Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on VMware vSphere.
weight: 50
menu:
  main:
    identifier: gettingstarted-persistentvolumes-vSphere
    parent: gettingstarted-persistentvolumes
aliases:
  - /guides/using-persistent-volumes-on-vSphere/
  - /ui-api/observability/prometheus/persistent-volumes/vSphere/
user_questions:
  - How can I use persistent volumes in my VMware vSphere clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
last_review_date: 2023-10-05
---

If your cluster is running on VMware vSphere, it comes with a dynamic storage provisioner for Cloud Native Storage disks (CNS). This enables you to store data beyond the lifetime of a Pod into virtual disks.

## Storage Classes

Your Kubernetes cluster will have a default Storage Class `csi-vsphere-sc-delete` deployed, which will automatically get selected if you do not specify the Storage Class in your Persistent Volumes. Another Storage Class `csi-vsphere-sc-retain` is also created with `reclaimPolicy: Retain` which you must explicitely specify to use.

As a Cluster Admin you can create additional Storage Classes or edit the default class to use different types of VMware Storage Profiles or for instance, add encryption.

For this you just need to create (or edit) [Storage Class objects](https://kubernetes.io/docs/concepts/storage/persistent-volumes).

## Creating Persistent Volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding Persistent Volume (PV) for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the Dynamic Storage Provisioner will take care that a corresponding CNS disk with the correct parameters is created in VMware vSphere.

The CNS disk and its data will persist as long as the corresponding PV resource exists. Deleting the resource will also delete the corresponding virtual disk, which means that all stored data will be lost at that point.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume Claim you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

Note that a Named Disk can only be used by a single Pod at the same time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

Under the hood the CNS disk stays detached from the virtual machines as long as it is not claimed by a Pod and you can visualize it in the vSphere client by browsing `Cluster > Monitor > Cloud Native Storage > Container volumes`. As soon as a Pod claims it, it gets attached to the virtual machine running the node that holds the Pod.

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

Further, as we are not defining a Storage Class the Kubernetes cluster will just take the default storage class (here `csi-vsphere-sc-delete`).

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

Now we have an NGINX Pod which serves the contents of our CNS disk.

## Expanding Persistent Volume Claims

vSphere Container Storage Plug-in supports volume expansion for block volumes that are created dynamically or statically.

Persistent Volume Claims can be expanded in `Offline` and `Online` mode (PVC used by a pod and mounted on a node) by simply editing the claim and requesting a larger size.

It will trigger an update in the underlying Persistent Volume and go through the events `Resizing` to `FileSystemResizeRequired` to `FileSystemResizeSuccessful`.

## Deleting Persistent Volumes

By default the Reclaim Policy of Persistent Volumes in your cluster is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective CNS disk. Similarly, by default if you delete a `PersistenVolumeClaim` resource the respective Persistent Volume and CNS disk will get deleted.

Note that deleting an application that is using Persistent Volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistenVolumeClaim` resources to clean up.

## Further reading

- [Storage Classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)