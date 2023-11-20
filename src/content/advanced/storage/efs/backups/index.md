---
linkTitle: AWS EFS backups using EBS
title: AWS EFS backup using a temporal EBS volume and Kubernetes Volume Snapshots
description: Tutorial explaining how to use a temporal EBS volume to backup your EFS filesystem without using AWS Backup.
weight: 30
menu:
  main:
    parent: advanced-storage-efs
user_questions:
  - How do I move my files from EFS to an EBS volume?
  - How do I do a EFS backup?
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
last_review_date: 2023-11-20
---

The AWS Elastic File System is a storage solution that supports NFS (v4.0) and scales automatically based on user consumption. Once you want to back up a file system you need to use AWS Backup which allows you to configure many things on how to your files will be copy and maintained in the backup system. It is advisable to use in most of the use cases but when you just want a simple copy of your files AWS Backup may be too complex.

Next we explain on how to leverage on the [built-in Kubernetes Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) to copy your file system or part of it. Since there is no EFS compatibility with that feature we need a bridge EBS volume that allow us to rely on the feature automation.

## Create a tooling Job/Pod

In this section we show you a debug container that mounts a new EBS to hold the copy of our files.

__Note__: Make sure the

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ebs-volume
spec:
  accessModes:
    - ReadWriteOnce
  storageClassName: gp3
  resources:
    requests:
      storage: 5Gi
```

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: backup-efs
spec:
  template:
    metadata:
      name: copy-pod
    spec:
      containers:
      - name: copy-container
        image: busybox:latest
        command: ["/bin/sh", "-c"]
        args: ["cp -r /efs/* /ebs/"]
        volumeMounts:
        - name: efs-volume
          mountPath: /efs
        - name: ebs-volume
          mountPath: /ebs
      volumes:
      - name: efs-volume
        persistentVolumeClaim:
          claimName: efs-volume
      - name: ebs-volume
        persistentVolumeClaim:
          claimName: ebs-volume
      restartPolicy: Never
```

First check you have a `VolumeSnapshotClass` for EBS in the cluster installed running `kubectl get volumesnapshotclass -A`. If it is not the case, please [install the controller and the class following this recipe](https://aws.amazon.com/blogs/containers/using-ebs-snapshots-for-persistent-storage-with-your-eks-cluster/).

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: backup-efs
spec:
  volumeSnapshotClassName: test-snapclass
  source:
    persistentVolumeClaimName: ebs-volume
```


You can now do a ordinary k8s volume scnapshot for the new EBS volume

## Further reading

- [AWS Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [AWS Elastic File System Access Points Example](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/access_points/README.md)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI developer documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
