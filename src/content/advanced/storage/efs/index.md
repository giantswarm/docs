---
linkTitle: Amazon Elastic File System (EFS)
title: Using Persistent Volumes on AWS with EFS
description: Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on Amazon Web Services with EFS
weight: 30
menu:
  main:
    parent: advanced-storage
user_questions:
  - How do I install the EFS provisioner?
  - How do I provision an EFS instance on AWS?
  - How do I test the efs storage class?
  - How do I use EFS Volumes?
  - What auto-provisioner for AWS do you recommend? EFS? EBS?
owner:
  - https://github.com/orgs/giantswarm/teams/team-firecracker
---

# Using persistent volumes on AWS with EFS

If your cluster is running in the cloud on Amazon Web Services (AWS) the most common way to store data is using EBS volumes with the [dynamic provisioner](/guides/using-persistent-volumes-on-aws-with-ebs-csi-driver/). Sometimes EBS is not the optimal solution.

The advantages of using EFS over EBS are:

- EFS data can be accessed from all availability zones in the same region while EBS is tied to a single availability zone.
- EFS has the capability to mount the same persistent volume to multiple pods at the same time using the ReadWriteMany [access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
- EFS will not hit the [AWS Instance Volume Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) as it is a software mount and will avoid the [Impaired EBS](/guides/aws-impaired-volumes/) issue.
- EFS mount times are better than EBS.
- EFS provides [encryption in transit](https://aws.amazon.com/blogs/aws/new-encryption-of-data-in-transit-for-amazon-efs/) support using TLS and it's enabled by default.

If you need to use EFS to provision volumes, be advised:

- All Kubernetes persistent volumes will be stored in the same EFS instance. You can deploy multiple provisioners per cluster, each having its own storage-class and EFS instance.
- [EFS throughput](https://docs.aws.amazon.com/efs/latest/ug/performance.html) need to be set up accordingly in order to not have performance issues. We only recommend Provisioned Throughput, and if you need high performance you will need EBS.
- EFS backups are done with [AWS Backup](https://aws.amazon.com/backup/) and it does not have the snapshot feature of EBS.
- You cannot limit the amount of data stored in an EFS volume. The requested value in Kubernetes is ignored.
- EFS mount targets are limited to 1 subnet per availability zone. Each NodePool will create a different subnet per AZ, plan accordingly.

## Provision an EFS instance on AWS

**Note:** Currently only static provisioning is supported. This means an AWS EFS file system needs to be created manually on AWS first. After that it can be mounted inside a container as a volume using the driver.

Before installing the provisioner in Kubernetes we will need to create the EFS instance in the same AWS account:

1. Open the [AWS management](https://aws.amazon.com/console/) console for the AWS account holding your cluster resources.
2. From the `Services` menu, select `EFS`.
3. Create a new file system and select the VPC where your cluster is located. The VPC can be identified by your cluster ID.
4. Select the availability zone with the subnets your instances are located on and the security groups of your node pools. Subnets and security groups can be identified by you cluster ID.
5. Choose the [throughput](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes) and [performance mode](https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes). Setting a file system policy or access points is optional.
6. Create the instance and note the EFS instance ID.

## Installing the EFS CSI driver

To install the EFS CSI driver in the workload cluster, you will need to follow these steps:

1. Access the [web interface](/reference/web-interface/) and select the cluster on which you want to install the EFS CSI driver.
2. Open the Apps tab.
3. Click the Install App button
4. Select the Giant Swarm Playground catalog.
5. Select the App named `aws-efs-csi-driver`.
6. Click the Configure & Install button. Make sure that the correct cluster is selected.
7. Click the Install App button.

## Storage classes

Once you installed the `aws-efs-csi-driver` from _Giant Swarm Playground_ catalog, you workload cluster will have a storage class `efs-csi` deployed.

## Deploy a sample application

In order to verify that the EFS CSI driver works as expected, we suggest to deploy a test workload based on the following manifests.

First we apply a persistent volume with a capacity of 5 GB storage. Make sure to apply your EFS instance ID (noted before) as `.spec.csi. volumeHandle` value!

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

**Note:** `.spec.storage.capacity` is a required field. You must specify a valid value, however that value is not used when creating the file system. It's important to note that EFS is an elastic file system, which does not enforce any file system capacity limits.

Additionally we need a persistent volume claim with a storage request matching the size of the persistent volume defined above:

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

And finally, we create a pod which repeatedly writes the current date into a file located in our EFS storage mount:

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
By default, new EFS file systems are owned by root:root. You might need to change file system permissions if your container is not running as root. To learn about exposing separate data stores with independent ownership and permissions, check the AWS guide on [working with Amazon EFS Access Points](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html).

## Further reading

- [AWS Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)
- [AWS Elastic File System Access Points Example](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/examples/kubernetes/access_points/README.md)
- [Persistent volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent volume claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- [Kubernetes CSI developer documentation](https://kubernetes-csi.github.io/docs/)
- [Container Storage Interface (CSI) for Kubernetes GA](https://kubernetes.io/blog/2019/01/15/container-storage-interface-ga/)
