---
linkTitle: Using the EBS CSI driver
title: Using persistent volumes with the EBS CSI driver on AWS
description: Tutorial on how to use dynamically provisioned persistent volumes with the EBS CSI driver on a cluster running on Amazon Web Services (AWS)."
weight: 20
menu:
  main:
    parent: advanced-storage
user_questions:
  - How do I install the EBS CSI driver?
  - How do I provision an EBS instance on AWS?
  - How do I test the EBS CSI storage class?
  - How do I use EBS CSI volumes?
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Using persistent volumes with the EBS CSI driver on AWS

The Container Storage Interface (CSI) has been promoted to general availability (GA) in Kubernetes v1.13 and is becoming the standard to replace the current Kubernetes `in-tree` storage plugin to handle volumes for different providers.

The aws-ebs-csi-driver-app, offered via our [App Platform]({{< relref "/app-platform" >}}) in the Giant Swarm Playground catalog, provides a CSI interface to manage the lifecycle of Amazon EBS volumes.

## Installing the EBS CSI driver

To install the EBS CSI driver you will need to follow these steps:

1. Access the [web interface]({{< relref "/ui-api/web/" >}}) and select the cluster on which you want to install the EBS CSI driver.
2. Open the Apps tab.
3. Click the Install App button
4. Select the Giant Swarm Playground catalog.
5. Select the App named aws-ebs-csi-driver-app.
6. Click the Configure & Install button. Make sure that the correct cluster is selected.
7. Click the Install App button.

## Storage classes

Once you installed the `aws-ebs-csi-driver-app` from _Giant Swarm Playground_ catalog, your Kubernetes cluster will have a storage class `ebs-csi` deployed.

The storage class offers volume encryption and allows resizing by default.

## Creating persistent volumes

The most straight forward way to create a persistent volume is to create a [PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims) resource with the storage class `ebs-csi`, which will automatically create a corresponding `PersistentVolume` (PV) resource for you.

Alternatively, to be able to set more specific parameters on your PV, you can first create a [PersistentVolume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) resource and then claim that PV using a `PersistentVolumeClaim` (PVC).

Under the hood, the EBS CSI driver will take care that a corresponding EBS volume with the correct parameters is created.

The EBS volume and its data will persist as long as the corresponding PV resource exists. Deleting the PV resource will also delete the corresponding EBS volume, which means that all stored data will be lost at that point.

## Using persistent volumes in a pod

Once you have a PersistentVolumeClaim you can [claim it as a volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your pods.

Note that an EBS volume can only be used by a single pod at the same time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

Under the hood the EBS volume stays detached from your nodes as long as it is not claimed by a pod. As soon as a pod claims it, it gets attached to the EC2 instance of the node that holds the pod.

## Example

First we create a PVC:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-claim
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: ebs-csi
  resources:
    requests:
      storage: 5Gi
```

Note that the access mode, while being fixed with EBS, still needs to be defined as `ReadWriteOnce` in the manifest (see the `accessModes` property).

Further, we need to define the storage class `ebs-csi` because it is not the default storage class (default `gp2`).

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
        claimName: my-claim
```

Now we have an NGINX pod which serves the content of our EBS volume.

## Increasing storage capacity of a volume

Starting with Kubernetes v1.16, CSI volumes can be expanded by simply editing the claim (the `PersistentVolumeClaim` resource) and requesting a larger size. This will trigger an update of the associated `PersistentVolume` resource and the underlying EBS volume.

Resizing a `PersistentVolumeClaim` resource in use is enabled by default with Kubernetes v1.15, so there is no need to delete and recreate a pod.

**Note:** You can only resize volumes formatted with one of the file systems XFS, Ext3, or Ext4.

**Warning:** Expanding EBS volumes is a time-consuming operation. Also, there is a per-volume quota of 1 modification every 6 hours.

## Deleting persistent volumes

The reclaim policy, which tells the cluster what to do with the volume after it has been released of its claim, is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective EBS volume. Similarly, by default if you delete a `PersistentVolumeClaim` resource, the respective `PersistentVolume` and EBS volume will get deleted.

Note that deleting a pod that is using persistent volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistentVolumeClaim` resources to clean up.

## Further reading

- [AWS storage classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#aws)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI developer documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
