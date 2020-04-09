---
title: "Using Persistent Volumes on AWS"
description: Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on Amazon Web Services"
date: "2018-07-09"
type: page
weight: 50
tags: ["tutorial"]
---

# Using Persistent Volumes on AWS

If your cluster is running in the cloud on Amazon Web Services (AWS), it comes with a dynamic storage provisioner for Elastic Block Storage (EBS). This enables you to store data beyond the lifetime of a Pod.

## Storage Classes

Your Kubernetes cluster will have a default Storage Class `gp2` deployed, which will automatically get selected if you do not specify the Storage Class in your Persistent Volumes.

As a Cluster Admin you can create additional Storage Classes or edit the default class to use different types of EBS or for example add encryption.

For this you just need to create (or edit) [Storage Class objects](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#aws).

## Creating Persistent Volumes

The most straight forward way to create a Persistent Volume is to create a [Persistent Volume Claim object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding Persistent Volume (PV) for you.

Alternatively, to be able to set more specific parameters on your PV you can first create a [Persistent Volume object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a Persistent Volume Claim (PVC).

Under the hood, the Dynamic Storage Provisioner will take care that a corresponding EBS Volume with the correct parameters is created.

The EBS Volume and its data will persist as long as the corresponding PV resource exists. Deleting the resource will also delete the corresponding EBS volume, which means that all stored data will be lost at that point.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume Claim you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

Note that an EBS Volume can only be used by a single Pod at the same time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

Under the hood the EBS Volume stays detached from your nodes as long as it is not claimed by a Pod. As soon as a Pod claims it, it gets attached to the node that holds the Pod.

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

Note that the Access Mode while being fixed with EBS still needs to be defined as `ReadWriteOnce` in the manifest.

Further, as we are not defining a Storage Class the Kubernetes cluster will just take the default storage class (here `gp2`).

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

Now we have an NGINX Pod which serves the contents of our EBS Volume.

## Expanding Persistent Volume Claims

Starting with Kubernetes v1.9 Persistent Volume Claims can be expanded by simply editing the claim and requesting a larger size. It will trigger an update in the underlying Persistent Volume and EBS Volume (Kubernetes always uses the existing one).

In case the volume to be expanded contains a file system, the resizing is only performed when a new Pod is started using the Persistent Volume Claim in `ReadWrite` mode. In other words, if a volume being expanded is used in a Pod or Deployment, you will need to delete and recreate the pod for file system resizing to take place. File system resizing is only supported for XFS, Ext3, and Ext4.

__Warning__: Expanding the filesystem is fully supported in Giant Swarm clusters starting from Kubernetes 1.10. Clusters with 1.9 have an issue with the `lsblk` utility that is used by Kubernetes to detect filesystem type. See below how to resize filesystem manually in that case.

__Warning__: Expanding EBS volumes is a time consuming operation. Also, there is a per-volume quota of one modification every 6 hours.

## Resizing filesystem for Kubernetes 1.9

This procedure is only required for Kubernetes 1.9. Newer clusters support filesystem resizing "out-of-the-box".

Make sure that the EBS volume was successfully resized and the PVC has been detached from other pods.

Create priviliged pod for filesystem resizing. Replace `namespace` and `claimName` with proper values.
```yaml
kind: Pod
apiVersion: v1
metadata:
  name: resize-pvc-pod
  namespace: <claim namespace>
spec:
  containers:
    - name: resize-pvc-pod
      image: ubuntu:xenial
      command:
        - sleep
        - "3600"
      volumeMounts:
      - mountPath: "/data"
        name: claim
      - mountPath: "/dev"
        name: dev
      securityContext:
        privileged: true
  volumes:
    - name: claim
      persistentVolumeClaim:
        claimName: <claim name here>
    - name: dev
      hostPath:
        path: /dev
```

Then `exec` inside the pod:

```nohighlight
$ kubectl exec -ti resize-pvc-pod -n <claim namespace> bash
```

Determine the attached PV block device:

```nohighlight
$ df -h | grep '/data' | awk '{print $1}'
```

Finally resize the filsystem:

```nohighlight
$ resize2fs /dev/<disk>
```

Delete the pod.

```nohighlight
$ kubectl delete pod resize-pvc-pod -n <claim namespace>
```

## Deleting Persistent Volumes

By default the Reclaim Policy of Persistent Volumes in your cluster is set to `Delete`. Thus, deleting the `PersistentVolume` resource will also delete the respective EBS Volume. Similarly, by default if you delete a `PersistenVolumeClaim` resource the respective Persistent Volume and EBS will get deleted.

Note that deleting an application that is using Persistent Volumes might not automatically also delete its storage, so in most cases you will have to manually delete the `PersistenVolumeClaim` resources to clean up.

## Further reading

- [AWS Storage Classes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#aws)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
