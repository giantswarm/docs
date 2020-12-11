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

The Container Storage Interface (CSI) has been promoted to general availability (GA) in Kubernetes v1.13 and is becoming the standard to replace the current Kubernetes `in-tree` storage plugin to handle volumes for different providers.

The aws-ebs-csi-driver-app, offered via our [App Platform](/basics/app-platform/) in the Giant Swarm Playground catalog, provides a CSI interface to manage the lifecycle of Amazon EBS volumes.

## Installing the EBS CSI driver

To install the EBS CSI driver you will need to follow these steps:

1. Access the [web interface](/reference/web-interface/) and select the cluster on which you want to install the EBS CSI driver.
2. Open the Apps tab.
3. Click the Install App button
4. Select the Giant Swarm Playground catalog.
5. Select the App named aws-ebs-csi-driver-app.
6. Click the Configure & Install button. Make sure that the correct cluster is selected.
7. Click the Install App button.

## Storage classes

Your Kubernetes cluster will have a Storage Class `ebs-csi` deployed, once you installed the `aws-ebs-csi-driver-app` from _Giant Swarm Playground_ catalog.

The storage class offers volume encryption and allows resizing by default.

## Creating persistent volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding Persistent Volume (PV) for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the EBS CSI driver will take care that a corresponding EBS Volume with the correct parameters is created.

The EBS Volume and its data will persist as long as the corresponding PV resource exists. Deleting the resource will also delete the corresponding EBS volume, which means that all stored data will be lost at that point.

## Using persistent volumes in a pod

Once you have a Persistent Volume Claim you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

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

## Expanding Persistent Volume Claims

Starting with Kubernetes v1.16, CSI volumes can be expanded by simply editing the claim (the `PersistentVolumeClaim` resource) and requesting a larger size. This will trigger an update of the associated `PersistentVolume` resource and the underlying EBS volume.

Resizing a PersistentVolumeClaim resource in use is enabled by default with Kubernetes v1.15, so there is no need to delete and recreate a pod.

**Note:** You can only resize volumes formatted with one of the file systems XFS, Ext3, or Ext4.

__Warning__: Expanding EBS volumes is a time-consuming operation. Also, there is a per-volume quota of 1 modification every 6 hours.

## Deleting persistent volumes

The Reclaim Policy is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective EBS volume. Similarly, by default if you delete a `PersistentVolumeClaim` resource, the respective `PersistentVolume` and EBS volume will get deleted.

Note that deleting an application that is using persistent volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistentVolumeClaim` resources to clean up.

## Further reading

- [AWS Storage Classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#aws)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI Developer Documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
