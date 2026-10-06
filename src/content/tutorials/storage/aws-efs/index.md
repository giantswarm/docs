---
title: Shared volumes with Amazon EFS
linkTitle: Amazon EFS volumes
diataxis_content_type: how-to-guide
description: Create an Amazon EFS file system with Crossplane and mount it as a shared ReadWriteMany volume in your AWS workload cluster.
weight: 20
menu:
  principal:
    parent: tutorials-storage
    identifier: tutorials-storage-aws-efs
last_review_date: 2026-10-06
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I share a volume between pods running on different nodes in AWS?
  - How do I use Amazon EFS volumes in my workload cluster?
  - How do I create an Amazon EFS file system with Crossplane?
  - How do I install the AWS EFS CSI driver?
---

The default `gp3` storage class in AWS clusters gives you EBS volumes, which a **single node** can mount at a time (`ReadWriteOnce`). When several pods on different nodes need the same files, a common option is to use [Amazon Elastic File System (EFS)](https://aws.amazon.com/efs/) instead. EFS volumes support the `ReadWriteMany` access mode.

In this guide, you'll:

1. Install the AWS EFS CSI driver in your workload cluster.
2. Create an EFS file system and its network plumbing with Crossplane.
3. Create a storage class and a persistent volume claim, and mount the volume in pods.

## Requirements

- A workload cluster on AWS (CAPA). Run all management cluster commands in the cluster's organization namespace, `org-<ORGANIZATION>`.
- `kubectl` access to the [management cluster]({{< relref "/getting-started/access-to-platform-api" >}}) and to the workload cluster.
- Permission to create Crossplane AWS resources on the management cluster. If you lack it, ask your Giant Swarm account engineer.

The examples use these placeholders:

- `<CLUSTER_NAME>`: the name of your workload cluster.
- `<ORGANIZATION>`: the name of your organization.
- `<REGION>`: the AWS region of your workload cluster, for example `eu-central-1`.

## Install the EFS CSI driver

The [`aws-efs-csi-driver-bundle`](https://github.com/giantswarm/aws-efs-csi-driver) chart runs on the management cluster. It creates the **IAM role** the driver needs, using Crossplane, and deploys the driver to your workload cluster.

You install the bundle with [Flux](https://fluxcd.io/), the same way your cluster's default apps are installed. An `OCIRepository` points to the chart in the Giant Swarm registry, and a `HelmRelease` installs it.

Create a file `efs-bundle.yaml` with this content:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  namespace: org-<ORGANIZATION>
spec:
  interval: 24h
  url: oci://gsoci.azurecr.io/charts/giantswarm/aws-efs-csi-driver-bundle
  ref:
    tag: 4.0.0
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  namespace: org-<ORGANIZATION>
spec:
  interval: 1m
  chartRef:
    kind: OCIRepository
    name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  releaseName: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  serviceAccountName: automation
  targetNamespace: org-<ORGANIZATION>
  storageNamespace: org-<ORGANIZATION>
  install:
    remediation:
      retries: -1
  upgrade:
    remediation:
      retries: -1
  values:
    clusterID: <CLUSTER_NAME>
```

Check the [repository releases](https://github.com/giantswarm/aws-efs-csi-driver/releases) for the latest version, and set it in `spec.ref.tag`. The `clusterID` value tells the bundle which workload cluster to deploy the driver to.

Apply it to the management cluster:

```sh
kubectl apply -f efs-bundle.yaml
```

The bundle creates a second `HelmRelease`, `<CLUSTER_NAME>-aws-efs-csi-driver`, which installs the driver itself and a Crossplane AWS IAM Role resource. Wait until both report `Ready`:

```sh
kubectl -n org-<ORGANIZATION> get helmrelease \
  <CLUSTER_NAME>-aws-efs-csi-driver-bundle \
  <CLUSTER_NAME>-aws-efs-csi-driver
```

After a few minutes, the driver runs in the `kube-system` namespace of your workload cluster. Check that the controller and the node pods are ready:

```sh
kubectl -n kube-system get deployment efs-csi-controller
kubectl -n kube-system get daemonset efs-csi-node
```

## Create the EFS file system with Crossplane

An EFS file system needs three things before nodes can mount it:

- A **security group** that allows NFS traffic (TCP port 2049) from inside the VPC.
- The **file system** itself.
- One **mount target** per availability zone, placed in the cluster's private subnets.

Every workload cluster comes with a Crossplane `ProviderConfig` named after the cluster. It grants Crossplane access to the cluster's AWS account, so you reference it as `<CLUSTER_NAME>` in all resources below.

### Look up the network details

Read the VPC ID, the VPC CIDR, and the private subnets from the cluster's `AWSCluster` resource on the management cluster:

```sh
kubectl -n org-<ORGANIZATION> get awscluster <CLUSTER_NAME> \
  -o jsonpath='{.spec.network.vpc.id} {.spec.network.vpc.cidrBlock}{"\n"}'
```

```sh
kubectl -n org-<ORGANIZATION> get awscluster <CLUSTER_NAME> \
  -o jsonpath='{range .spec.network.subnets[?(@.isPublic==false)]}'\
'{.resourceID} {.availabilityZone}{"\n"}{end}'
```

The second command prints one private subnet per line, together with its availability zone. Pick **one subnet per availability zone**.

### Create the security group and the file system

Create a file `efs-filesystem.yaml`. Replace `<VPC_ID>` with the VPC ID from the previous step:

```yaml
apiVersion: ec2.aws.upbound.io/v1beta1
kind: SecurityGroup
metadata:
  name: <CLUSTER_NAME>-efs-sg
spec:
  forProvider:
    region: <REGION>
    vpcId: <VPC_ID>
    description: Allow NFS access to EFS
    tags:
      Name: <CLUSTER_NAME>-efs-sg
  providerConfigRef:
    name: <CLUSTER_NAME>
---
apiVersion: efs.aws.upbound.io/v1beta1
kind: FileSystem
metadata:
  name: <CLUSTER_NAME>-efs
spec:
  forProvider:
    region: <REGION>
    performanceMode: generalPurpose
    encrypted: true
    tags:
      Name: <CLUSTER_NAME>-efs
  providerConfigRef:
    name: <CLUSTER_NAME>
```

Apply it to the management cluster and wait until both resources are ready:

```sh
kubectl apply -f efs-filesystem.yaml
kubectl wait --for=condition=Ready --timeout=5m \
  securitygroup.ec2.aws.upbound.io/<CLUSTER_NAME>-efs-sg \
  filesystem.efs.aws.upbound.io/<CLUSTER_NAME>-efs
```

Then read the AWS IDs that Crossplane got back:

```sh
kubectl get securitygroup.ec2.aws.upbound.io <CLUSTER_NAME>-efs-sg \
  -o jsonpath='{.status.atProvider.id}{"\n"}'
kubectl get filesystem.efs.aws.upbound.io <CLUSTER_NAME>-efs \
  -o jsonpath='{.status.atProvider.id}{"\n"}'
```

The first ID starts with `sg-`, the second one with `fs-`. You need both in the next step.

### Open the NFS port and create the mount targets

Create a file `efs-network.yaml`. Replace `<SECURITY_GROUP_ID>`, `<FILE_SYSTEM_ID>`, and `<VPC_CIDR>` with your values, and add one `MountTarget` per private subnet:

```yaml
apiVersion: ec2.aws.upbound.io/v1beta1
kind: SecurityGroupRule
metadata:
  name: <CLUSTER_NAME>-efs-nfs
spec:
  forProvider:
    region: <REGION>
    securityGroupId: <SECURITY_GROUP_ID>
    type: ingress
    protocol: tcp
    fromPort: 2049
    toPort: 2049
    cidrBlocks:
      - <VPC_CIDR>
  providerConfigRef:
    name: <CLUSTER_NAME>
---
apiVersion: efs.aws.upbound.io/v1beta1
kind: MountTarget
metadata:
  name: <CLUSTER_NAME>-efs-<AVAILABILITY_ZONE>
spec:
  forProvider:
    region: <REGION>
    fileSystemId: <FILE_SYSTEM_ID>
    subnetId: <PRIVATE_SUBNET_ID>
    securityGroups:
      - <SECURITY_GROUP_ID>
  providerConfigRef:
    name: <CLUSTER_NAME>
# Repeat the MountTarget for each availability zone.
```

Apply it to the management cluster and wait until all mount targets are ready. This usually takes one to two minutes:

```sh
kubectl apply -f efs-network.yaml
kubectl get mounttarget.efs.aws.upbound.io
```

{{% notice note %}}
Give the mount targets **a few minutes** after they turn ready. Until AWS publishes the file system's DNS name in the VPC, mounts fail with `Failed to resolve "fs-....efs.<REGION>.amazonaws.com"`. Kubernetes retries the mount on its own, so pods start as soon as the name resolves.
{{% /notice %}}

## Mount the volume in your pods

Run the following steps against the **workload cluster**.

### Create a storage class

The storage class tells the driver which file system to use. With `provisioningMode: efs-ap`, the driver creates an [EFS access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) for each persistent volume claim. Every claim gets its own directory on the shared file system.

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: efs
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap
  fileSystemId: <FILE_SYSTEM_ID>
  directoryPerms: "700"
  uid: "1000"
  gid: "1000"
```

The `uid` and `gid` parameters set the owner of the access point directory. Match them to the user your pods run as, so that **non-root containers** can write to the volume.

### Create a persistent volume claim

Request a volume with the `ReadWriteMany` access mode:

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: shared-data
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: efs
  resources:
    requests:
      storage: 5Gi
```

EFS grows and shrinks with the data you store, so the requested size isn't enforced. Kubernetes still requires a value.

The claim turns `Bound` within seconds:

```sh
kubectl get pvc shared-data
```

### Use the volume

Mount the claim like any other volume. Because the access mode is `ReadWriteMany`, all replicas of this deployment share the same files, **no matter which node** they run on:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: shared-data-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: shared-data-demo
  template:
    metadata:
      labels:
        app: shared-data-demo
    spec:
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000
        runAsGroup: 1000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: app
          image: busybox:1.36
          command:
            - sh
            - -c
            - echo "hello from $(hostname)" >> /data/log.txt && sleep 3600
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop:
                - ALL
          volumeMounts:
            - name: data
              mountPath: /data
      volumes:
        - name: data
          persistentVolumeClaim:
            claimName: shared-data
```

To check that the replicas share the volume, read the file from one of the pods. It contains a line from each replica:

```sh
kubectl exec deploy/shared-data-demo -- cat /data/log.txt
```

## Clean up

Delete the resources in reverse order, or the AWS resources get stuck on their dependencies:

1. In the workload cluster, delete the workloads, the persistent volume claims, and the storage class. With the default `reclaimPolicy: Delete`, the driver removes the access points, **including their data**.
2. On the management cluster, delete the mount targets and the security group rule:

    ```sh
    kubectl delete -f efs-network.yaml
    ```

3. On the management cluster, delete the file system and the security group:

    ```sh
    kubectl delete -f efs-filesystem.yaml
    ```

4. To remove the driver too, delete the bundle:

    ```sh
    kubectl delete -f efs-bundle.yaml
    ```

## Further reading

- [Persistent volumes]({{< relref "/tutorials/storage/persistent-volumes" >}})
- [AWS EFS CSI driver repository](https://github.com/giantswarm/aws-efs-csi-driver)
- [EFS CSI driver upstream documentation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/tree/master/docs)
- [Crossplane AWS provider for EFS](https://marketplace.upbound.io/providers/upbound/provider-aws-efs/)
