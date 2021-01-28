---
title: "Using Persistent Volumes on bare metal"
description: "Tutorial on how to use pre-created Persistent Volumes on a cluster running on premise (bare metal)"
type: page
weight: 50
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

# Using Persistent Volumes on your on-premise bare metal clusters

Persistent Volumes allow you to store data beyond the lifetime of a Pod. Ideally, storage is dynamically provisioned and claiming storage for your pods would not require you to pre-provision storage. However, depending on your installation, your bare metal clusters might not support dynamic storage provisioning.

This document describes how we still allow you to claim volumes for your Pods by pre-creating a known folder structure in either a NFS share or in iSCSI (iSCSI docs coming soon).

## Pre-creating Persistent Volumes via NFS

Our approach when using NFS is to use one NFS share with a set of pre-created folders.
The NFS share must be accessible from all bare metal machines.

Let's say we have a nfs export at `nfs.storageserver.internal:/k8s-storage`.
Firstly we create folders on the NFS share so we have a directory structure that looks like this:

```nohighlight
/k8s-storage/pv0001
/k8s-storage/pv0002
/k8s-storage/pv0003
...
...
/k8s-storage/pv00xy
```

Obviously you can use any naming scheme you want.
Usually you don't know the exact number of volumes you'll need, so it's a good idea to pre-provison a lot.

Once the folder structure is ready, we can create a Persistent Volume for each folder in the k8s cluster.

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0001
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  nfs:
    path: /k8s-storage/pv0001
    server: nfs.storageserver.internal
---
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv0002
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteOnce
  persistentVolumeReclaimPolicy: Recycle
  storageClassName: slow
  nfs:
    path: /k8s-storage/pv0002
    server: nfs.storageserver.internal
```

The only values you need to change on each additional Persistent Volume  is `name` and `path`.

Note that the NFS protocol can't enforce storage capacity, however, defining a capacity here is needed to match the Persistent Volume Claim with a Persistent Volume.

## Using Persistent Volumes in a Pod

Once you have a Persistent Volume you can [claim it as a Volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your Pods.

Note that these Volumes can only be used by a single Pod at the same time. Thus, the access mode of your claim must be `ReadWriteOnce`.

Under the hood the Volume stays detached from your nodes as long as it is not claimed by a Pod. As soon as a Pod claims it, it gets attached to the node that holds the Pod.

If you want to limit access to certain persistent volumes to a certain namespace, you need to also pre-create the PVCs, as those, unlike PVs, are namespaced and thus allow for access controls on a namespace level.

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

Note that the Access Mode must be defined as `ReadWriteOnce` in the manifest.

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

Now we have an NGINX Pod which serves the contents of our Volume.

## Further Reading

- [NFS Storage Volume](https://kubernetes.io/docs/concepts/storage/volumes/#nfs)
- [iSCSI Storage Volume](https://kubernetes.io/docs/concepts/storage/volumes/#iscsi)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
