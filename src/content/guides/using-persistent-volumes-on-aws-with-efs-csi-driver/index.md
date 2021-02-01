---
title: "Using persistent volumes with the EFS CSI driver on AWS"
description: "Tutorial on how to use persistent volumes with the EFS CSI driver on a cluster running on Amazon Web Services with EFS"
type: page
weight: 50
tags: ["tutorial"]
user_questions:
  - How do I install the EFS CSI driver?
  - How do I provision an EFS instance on AWS?
  - How do I test the EFS CSI storage class?
  - How do I use EFS CSI Volumes?
  - What auto-provisioner for AWS do you recommend? EFS? EBS?
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Using Persistent Volumes on AWS with EFS

If your cluster is running in the cloud on Amazon Web Services (AWS) the most common way to store data is using EBS volumes with the [dynamic provisioner](/guides/using-persistent-volumes-on-aws-with-ebs-csi-driver/). Sometimes EBS is not the optimal solution.

The advantages of using EFS over EBS are:

- EFS data can be accessed from all Availability Zones in the same region while EBS is tied to a single Availability Zone.
- EFS has the capability to mount the same Persistent Volume to multiple pods at the same time using the ReadWriteMany [access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
- EFS will not hit the [AWS Instance Volume Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) as it is a software mount and will avoid the [Impaired EBS](/guides/aws-impaired-volumes/) issue.
- EFS mount times are better than EBS.
- EFS provides [encryption in transit](https://aws.amazon.com/blogs/aws/new-encryption-of-data-in-transit-for-amazon-efs/) support using TLS and it's enabled by default.

If you need to use EFS to provision volumes, be advised:

- All Kubernetes Persistent Volumes will be stored in the same EFS instance. You can deploy multiple provisioners per cluster, each having its own storage-class and EFS instance.
- [EFS throughput](https://docs.aws.amazon.com/efs/latest/ug/performance.html) need to be set up accordingly in order to not have performance issues. We only recommend Provisioned Throughput, and if you need high performance you will need EBS.
- EFS backups are done with [AWS Backup](https://aws.amazon.com/backup/) and it does not have the snapshot feature of EBS.
- You cannot limit the amount of data stored in an EFS volume. The requested value in Kubernetes is ignored.
- EFS mount targets are limited to 1 subnet per Availability Zone. Each NodePool will create a different subnet per AZ, plan accordingly.

## Provision an EFS instance on AWS

**Note:** Currently only static provisioning is supported. This means an AWS EFS file system needs to be created manually on AWS first. After that it can be mounted inside a container as a volume using the driver.

Before installing the provisioner in Kubernetes we will need to create the EFS instance in the same AWS account:

1. Open the [AWS management](https://aws.amazon.com/console/) console in the account your cluster is located.
2. Select EFS from the services list.
3. Create a new file system and select the VPC where your cluster is located.
4. Select the Availability Zone with the subnets your instances are located on and the security-groups of your node pools.
5. Choose the throughput and performance mode, no file system policy or access points are needed.
6. Create the instance and note the EFS instance id.

## Installing the EFS CSI driver

To install the EFS CSI driver you will need to follow these steps:

1. Access the [web interface](/reference/web-interface/) and select the cluster on which you want to install the EFS CSI driver.
2. Open the Apps tab.
3. Click the Install App button
4. Select the Giant Swarm Playground catalog.
5. Select the App named aws-efs-csi-driver.
6. Click the Configure & Install button. Make sure that the correct cluster is selected.
7. Click the Install App button.

## Storage classes

Once you installed the `aws-efs-csi-driver` from _Giant Swarm Playground_ catalog, Kubernetes cluster will have a storage class `efs-csi` deployed.

## Deploy a sample application

In order to see if all works out we need to create some manifests:

First we apply a PersistentVolume with a capacity of 5 GB storage, here you need to provide EFS instance id:

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: efs-pv
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  persistentVolumeReclaimPolicy: Retain
  storageClassName: efs-csi
  csi:
    driver: efs.csi.aws.com
    volumeHandle: fs-xxxxxxxx
```

**Note:** Storage capacity is a required field, you need to specify a valid value but is not used when creating the file system. It's important to note EFS is an elastic file system, it does not enforce any file system capacity limits.

Additionally we need a PerstentVolumeClaim with a request of 5 GB storage:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: efs-claim
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: efs-csi
  resources:
    requests:
      storage: 5Gi
```

And finally, we apply a Pod which writes every 5 seconds the current date in UTC time in a file located in our EFS storage mount:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: efs-app
spec:
  containers:
  - name: linux
    image: amazonlinux:2
    command: ["/bin/sh"]
    args: ["-c", "while true; do echo $(date -u) >> /efs-data/out.txt; sleep 5; done"]
    volumeMounts:
    - name: efs-storage
      mountPath: /efs-data
  volumes:
  - name: efs-storage
    persistentVolumeClaim:
      claimName: efs-claim
```

**Warning:**
By default, new EFS file systems are owned by root:root. You might need to change file system permissions if your container is not running as root.

## Further reading

- [AWS Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI developer documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
