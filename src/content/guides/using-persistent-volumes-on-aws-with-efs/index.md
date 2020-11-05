---
title: "Using Persistent Volumes on AWS with EFS"
description: "Tutorial on how to use dynamically provisioned Persistent Volumes on a cluster running on Amazon Web Services with EFS"
date: "2020-02-06"
type: page
weight: 50
tags: ["tutorial"]
user_questions:
  - How do I install the EFS provisioner?
  - How do I provision an EFS instance on AWS?
  - How do I test the efs storage class?
  - How do I use EFS Volumes?
  - What auto-provisioner for AWS do you recommend? EFS? EBS?
---

# Using Persistent Volumes on AWS with EFS

If your cluster is running in the cloud on Amazon Web Services (AWS) the most common way to store data is using EBS volumes with the [dynamic provisioner](/guides/using-persistent-volumes-on-aws/). Sometimes EBS is not the optimal solution.

The advantages of using EFS over EBS are:

- EFS data can be accessed from all Availability Zones in the same region while EBS is tied to a single Availability Zone.
- EFS has the capability to mount the same Persistent Volume to multiple pods at the same time using the ReadWriteMany [access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes).
- EFS will not hit the [AWS Instance Volume Limit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/volume_limits.html) as it is a software mount and will avoid the [Impaired EBS](/guides/aws-impaired-volumes/) issue.
- EFS mount times are better than EBS.

If you need to use EFS to provision volumes, be advised:

- All Kubernetes Persistent Volumes will be stored in the same EFS instance. You can deploy multiple provisioners per cluster, each having its own storage-class and EFS instance.
- [EFS throughput](https://docs.aws.amazon.com/efs/latest/ug/performance.html) need to be set up accordingly in order to not have performance issues. We only recommend Provisioned Throughput, and if you need high performance you will need EBS.
- EFS backups are done with [AWS Backup](https://aws.amazon.com/backup/) and it does not have the snapshot feature of EBS.
- You cannot limit the amount of data stored in an EFS volume. The requested value in Kubernetes is ignored.
- EFS mount targets are limited to 1 subnet per Availability Zone. Each NodePool will create a different subnet per AZ, plan accordingly.

## Provision an EFS instance on AWS

Before installing the provisioner in Kubernetes we will need to create the EFS instance in the same AWS account:

1. Open the [AWS management](https://aws.amazon.com/console/) console in the account your cluster is located.
2. Select EFS from the services list.
3. Create a new EFS mount and select the VPC where your cluster is located.
4. Select the Availability Zone with the subnets your instances are located on and the security-groups of the workers.
5. Choose the throughput and performance mode, no file system policy or access points are needed.
6. Create the instance and note the EFS instance id.

## EFS provisioner configuration file

In order to configure the EFS provisioner, you will need to create a file on your local machine named `efs-provisioner.yaml` with the following content:

```yaml
global:
  deployEnv: production

efsProvisioner:
  efsFileSystemId: fs-90f935c8
  awsRegion: eu-central-1
  path: /
  provisionerName: giantswarm.io/aws-efs
  storageClass:
    name: efs
    isDefault: false
    gidAllocate:
      enabled: true
      gidMin: 40000
      gidMax: 50000
    reclaimPolicy: Delete
    mountOptions: []

rbac:
  create: true

podSecurityPolicy:
  enabled: true
```

You will need to populate the `efsFileSystemId` and `awsRegion` parameters to match the configured values of the EFS instance.

For additional configuration parameters see the [upstream documentation](https://github.com/kubernetes-retired/external-storage/tree/master/aws/efs).

## Installing EFS Provisioner

To install the provisioner you will need to follow these steps:

1. Access Giant Swarm web UI and select the cluster on which you want to install the provisioner.
2. Open the _Helm Stable_ catalog.
3. Write `efs-provisioner` in the search bar.
4. Select the _efs-provisioner_ application and then click the Configure & Install button.
5. Upload the `efs-provisioner.yaml` file created in the previous step.
6. Finally, you can click the _Install App_ button and it will be installed into your cluster.

## Using EFS Volumes

Your Kubernetes cluster will have a new Storage Class `efs` deployed, which you will have to reference when creating persistent volumes.

In order to check that the storage class exits, you should see something similar to:

```nohighlight
$ kubectl get storageclass
NAME            PROVISIONER             AGE
efs             giantswarm.io/aws-efs   23m
gp2 (default)   kubernetes.io/aws-ebs   5h31m
```

In the following example you can see the annotation `volume.beta.kubernetes.io/storage-class` matches the `efs` Storage Class:

```yaml
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: test
  annotations:
    volume.beta.kubernetes.io/storage-class: "efs"
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 100Mi
```

## Testing the new storage class

You can create a file with the example above in a file called `pvc_claim.yaml` and instantiate with the following command:

```nohighlight
kubectl apply -f pvc_claim.yaml
```

In order to check the status of the volume we can check the status of the PVC:

```nohighlight
$ kubectl get pvc test
NAME   STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
test   Bound    pvc-0d7b988e-4eed-4cf7-918b-30964774fa13   100Mi        RWX            efs            5s
```

If the status is `Bound`, everything worked as expected.

If there is an error, check the logs of the provisioner pod in the namespace where the application was deployed.

## Further reading

- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim Persistent Volumes in Pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
