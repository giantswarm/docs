---
title: Using persistent volumes with the EBS CSI driver on AWS
description: Tutorial on how to use dynamically provisioned persistent volumes with the EBS CSI driver on a cluster running on Amazon Web Services (AWS)."
type: page
weight: 50
tags: ["tutorial"]
user_questions:
  - How do I install the EBS CSI driver?
  - How do I provision an EBS instance on AWS?
  - How do I test the EBS CSI storage class?
  - How do I use EBS CSI volumes?
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Using Persistent Volumes on AWS with Container Storage Interface (CSI)

CSI has been promoted to GA in Kubernetes v1.13 and is becoming the standard to replace the current Kubernetes `in-tree` storage plugin to handle Volumes for different provider.

The aws-ebs-csi-driver-app, offered via our [App Platform](/basics/app-platform/) in the Giant Swarm Playground catalog, provides a CSI interface to manage the lifecycle of Amazon EBS volumes.

## Installing the EBS CSI driver

To install the EBS CSI driver you will need to follow these steps:

1. Access Giant Swarm web UI and select the cluster on which you want to install the EBS CSI driver.
2. Open the _Giant Swarm Playground_ catalog.
3. Write `aws-ebs-csi-driver-app` in the search bar.
4. Click the _Configure & Install_ button, select the cluster and it will be installed.

## Storage Classes

Your Kubernetes cluster will have a Storage Class `ebs-csi` deployed, once you installed the `aws-ebs-csi-driver-app` from _Giant Swarm Playground_ catalog.

The storage class offers volume encryption and allows resizing by default.

## Creating Persistent Volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding Persistent Volume (PV) for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the EBS CSI driver will take care that a corresponding EBS Volume with the correct parameters is created.

The EBS Volume and its data will persist as long as the corresponding PV resource exists. Deleting the resource will also delete the corresponding EBS volume, which means that all stored data will be lost at that point.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume Claim you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

Note that an EBS Volume can only be used by a single Pod at the same time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

Under the hood the EBS Volume stays detached from your nodes as long as it is not claimed by a Pod. As soon as a Pod claims it, it gets attached to the node that holds the Pod.

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

Note that the Access Mode while being fixed with EBS still needs to be defined as `ReadWriteOnce` in the manifest.

Further, we need to define the Storage Class `ebs-csi` because it is not the default storage class (default `gp2`).

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

Now we have an NGINX Pod which serves the contents of our EBS Volume.

## Expanding Persistent Volume Claims

Starting with Kubernetes v1.16 CSI Volume can be expanded by simply editing the claim and requesting a larger size. It will trigger an update in the underlying Persistent Volume and EBS Volume (Kubernetes always uses the existing one).

Resizing an in-use PersistentVolumeClaim is enabled by default with Kubernetes v1.15, there is no need to delete and recreate a Pod. You can only resize volumes containing a file system if the file system is XFS, Ext3, or Ext4.

__Warning__: Expanding EBS volumes is a time consuming operation. Also, there is a per-volume quota of one modification every 6 hours.

## Deleting Persistent Volumes

The Reclaim Policy is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective EBS Volume. Similarly, by default if you delete a `PersistentVolumeClaim` resource the respective Persistent Volume and EBS will get deleted.

Note that deleting an application that is using Persistent Volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistentVolumeClaim` resources to clean up.

## Further reading

- [AWS Storage Classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#aws)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI Developer Documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
