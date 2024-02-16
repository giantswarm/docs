---
linkTitle: AWS EFS backups using EBS
title: AWS EFS backup using a temporal EBS volume and Kubernetes Volume Snapshots
description: Tutorial explaining how to use a temporal EBS volume to backup your EFS filesystem without using AWS Backup.
weight: 30
aliases:
  - /advanced/storage/efs/backups
menu:
  main:
    parent: advanced-storage-efs
user_questions:
  - How do I move my files from EFS to an EBS volume?
  - How do I do a EFS backup?
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
last_review_date: 2023-12-12
---

The AWS Elastic File System is a storage solution that supports NFS (v4.0) and scales automatically based on user consumption. According to official documentation, when you want to back up a file system you need to use AWS Backup. It allows you to configure many things on how your files will be copied and maintained in the backup system. It is the recommended approach, but in case you just want a simple copy of your files then AWS Backup may be too complex.

Next, we explain how to leverage the [built-in Kubernetes Snapshots](https://kubernetes.io/docs/concepts/storage/volume-snapshots/) to copy your file system or part of it. Since there is no EFS compatibility with that feature we need a bridge EBS volume that allows us to rely on the feature automation.

## Create a tooling Job/Pod

In this section we define a debug container that will mount the existing EFS filesystem path and a new EBS to transfer a copy of our files.

__Note__: Make sure the EBS volume has enough space to hold all of your files.

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

## Creating a Volume Snapshot

As requirement you need to have a valid `VolumeSnapshotClass` for EBS in the cluster to be able to create the backup automatically. The quickest way to check is running this command:

```bash
kubectl get volumesnapshotclass -A
```

__Note__: In the case there is not class installed, please [follow this tutorial from step 3 to deploy one](https://aws.amazon.com/blogs/containers/using-ebs-snapshots-for-persistent-storage-with-your-eks-cluster/). Optionally, you can use the AWS console to take a snapshot directly from the EBS volume. Maybe worthy in case it is a single action task.

Once the controller class is there, taking a snapshot is as easy as creating a resource with the class and the persistent volume claim name.

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

__Note__: After the task is completed you may want to delete the job and the persistent volume.

## Further reading

- [AWS Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI developer documentation](https://kubernetes-csi.github.io/docs/)
