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
last_review_date: 2026-11-09
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

## Requirements

- A workload cluster on AWS, either CAPA with EC2 nodes ([`cluster-aws`](https://github.com/giantswarm/cluster-aws)) or EKS ([`cluster-eks`](https://github.com/giantswarm/cluster-eks)). Run all management cluster commands in the cluster's organization namespace, `org-<ORGANIZATION>`.
- On EKS, `aws-efs-csi-driver-bundle` v4.0.10 or newer. Older versions wait for a `<CLUSTER_NAME>-cloud-provider-aws` HelmRelease that EKS clusters don't have, and schedule the driver controller only on control plane nodes, which EKS doesn't expose.
- The [`kubectl gs`]({{< relref "/reference/kubectl-gs/installation" >}}) plugin, v6 or newer.
- `kubectl` access to the [management cluster]({{< relref "/getting-started/access-to-platform-api" >}}) and to the workload cluster.
- Permission to create Crossplane AWS resources on the management cluster. If you lack it, ask your Giant Swarm account engineer.

The examples use these placeholders:

- `<CLUSTER_NAME>`: the name of your workload cluster.
- `<ORGANIZATION>`: the name of your organization.
- `<REGION>`: the AWS region of your workload cluster, for example `eu-central-1`.

## Install the EFS CSI driver

The [`aws-efs-csi-driver-bundle`](https://github.com/giantswarm/aws-efs-csi-driver) chart runs on the management cluster. It creates the **IAM role** the driver needs, using Crossplane, and deploys the driver to your workload cluster.

You install the bundle with [`kubectl gs deploy chart`]({{< relref "/reference/kubectl-gs/deploy-chart" >}}). The command creates the [Flux](https://fluxcd.io/) resources that install the chart: an `OCIRepository` pointing to the chart in the Giant Swarm registry, and a `HelmRelease` that installs it.

Deploy the bundle from the management cluster:

```sh
kubectl gs deploy chart \
  --chart-name aws-efs-csi-driver-bundle \
  --version 4.0.10 \
  --organization <ORGANIZATION> \
  --target-cluster <CLUSTER_NAME> \
  --bundle
```

Check the [repository releases](https://github.com/giantswarm/aws-efs-csi-driver/releases) for the latest version, and set it in `--version`. With `--bundle`, the `HelmRelease` runs on the management cluster in the organization namespace, using the `automation` service account. The platform injects the workload cluster ID into the bundle values, so you don't need to pass any values.

To review the resources before you create them, add `--dry-run`. The command then prints them instead of applying them:

```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: OCIRepository
metadata:
  labels:
    giantswarm.io/cluster: <CLUSTER_NAME>
  name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  namespace: org-<ORGANIZATION>
spec:
  interval: 10m0s
  provider: generic
  ref:
    tag: 4.0.10
  url: oci://gsoci.azurecr.io/charts/giantswarm/aws-efs-csi-driver-bundle
---
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  labels:
    giantswarm.io/cluster: <CLUSTER_NAME>
  name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  namespace: org-<ORGANIZATION>
spec:
  chartRef:
    kind: OCIRepository
    name: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  interval: 10m0s
  releaseName: <CLUSTER_NAME>-aws-efs-csi-driver-bundle
  serviceAccountName: automation
  targetNamespace: org-<ORGANIZATION>
```

If you manage the management cluster resources with GitOps, commit this output to your repository instead of running the command without `--dry-run`.

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

Every workload cluster comes with a Crossplane `ProviderConfig` named after the cluster. It grants Crossplane access to the cluster's AWS account, so all resources below reference it by the cluster name.

The resources refer to each other by name, for example with `securityGroupIdRef` and `fileSystemIdRef`. Crossplane fills in the AWS IDs on its own, so you can create all resources at once. Only the VPC and the subnets belong to the cluster itself. You read them from the management cluster in the next step.

### Look up the network details

Set these variables in your shell. The cluster's network settings live in the `AWSCluster` resource on CAPA, and in the `AWSManagedControlPlane` resource on EKS:

{{< tabs >}}
{{< tab id="efs-network-capa-ec2" for-impl="capa_ec2" >}}

```sh
CLUSTER_NAME=<CLUSTER_NAME>
NAMESPACE=org-<ORGANIZATION>
NETWORK_RESOURCE=awscluster
```

{{< /tab >}}
{{< tab id="efs-network-capa-eks" for-impl="capa_eks" >}}

```sh
CLUSTER_NAME=<CLUSTER_NAME>
NAMESPACE=org-<ORGANIZATION>
NETWORK_RESOURCE=awsmanagedcontrolplane
```

{{< /tab >}}
{{< /tabs >}}

Read the region, the VPC ID, the VPC CIDR, and the subnets the nodes run in:

```sh
read -r REGION VPC_ID VPC_CIDR <<< "$(kubectl -n "$NAMESPACE" get "$NETWORK_RESOURCE" "$CLUSTER_NAME" \
  -o jsonpath='{.spec.region} {.spec.network.vpc.id} {.spec.network.vpc.cidrBlock}')"

NODE_SUBNETS="$(kubectl -n "$NAMESPACE" get "$NETWORK_RESOURCE" "$CLUSTER_NAME" \
  -o jsonpath='{range .spec.network.subnets[?(@.tags.giantswarm\.io/role=="nodes")]}'\
'{.resourceID} {.availabilityZone}{"\n"}{end}' | awk '!seen[$2]++')"

echo "$REGION $VPC_ID $VPC_CIDR"
echo "$NODE_SUBNETS"
```

The cluster tags the private subnets for nodes with `giantswarm.io/role: nodes`. The filter therefore skips the public subnets and, on EKS, the secondary subnets for pod IPs. EFS allows only one mount target per availability zone, so `awk` keeps the first subnet of each zone.

If `NODE_SUBNETS` is empty, the cluster was created with a chart version that doesn't set this tag yet. Upgrade the cluster, or set `NODE_SUBNETS` yourself, with one line `<SUBNET_ID> <AVAILABILITY_ZONE>` per private subnet.

### Generate the manifests

Generate `efs-filesystem.yaml` with the security group and the file system:

```sh
cat > efs-filesystem.yaml <<EOF
apiVersion: ec2.aws.upbound.io/v1beta1
kind: SecurityGroup
metadata:
  name: ${CLUSTER_NAME}-efs-sg
spec:
  forProvider:
    region: ${REGION}
    vpcId: ${VPC_ID}
    description: Allow NFS access to EFS
    tags:
      Name: ${CLUSTER_NAME}-efs-sg
  providerConfigRef:
    name: ${CLUSTER_NAME}
---
apiVersion: efs.aws.upbound.io/v1beta1
kind: FileSystem
metadata:
  name: ${CLUSTER_NAME}-efs
spec:
  forProvider:
    region: ${REGION}
    performanceMode: generalPurpose
    encrypted: true
    tags:
      Name: ${CLUSTER_NAME}-efs
  providerConfigRef:
    name: ${CLUSTER_NAME}
EOF
```

Generate `efs-network.yaml` with the rule that opens the NFS port, and one mount target per node subnet. On CAPA, the rule allows NFS traffic from the whole VPC. On EKS, it allows NFS traffic only from the cluster's nodes, using the cluster security group that EKS attaches to all nodes:

```sh
if [ "$NETWORK_RESOURCE" = awsmanagedcontrolplane ]; then
  CLUSTER_SECURITY_GROUP_ID="$(kubectl -n "$NAMESPACE" get awsmanagedcontrolplane "$CLUSTER_NAME" \
    -o jsonpath='{.status.networkStatus.securityGroups.cluster.id}')"
  if [ -z "$CLUSTER_SECURITY_GROUP_ID" ]; then
    echo "Error: AWSManagedControlPlane ${CLUSTER_NAME} has no cluster security group in its status" >&2
  fi
  NFS_SOURCE="sourceSecurityGroupId: ${CLUSTER_SECURITY_GROUP_ID}"
else
  NFS_SOURCE="cidrBlocks: [${VPC_CIDR}]"
fi

{
  cat <<EOF
apiVersion: ec2.aws.upbound.io/v1beta1
kind: SecurityGroupRule
metadata:
  name: ${CLUSTER_NAME}-efs-nfs
spec:
  forProvider:
    region: ${REGION}
    securityGroupIdRef:
      name: ${CLUSTER_NAME}-efs-sg
    type: ingress
    protocol: tcp
    fromPort: 2049
    toPort: 2049
    ${NFS_SOURCE}
  providerConfigRef:
    name: ${CLUSTER_NAME}
EOF
  while read -r SUBNET_ID ZONE; do
    cat <<EOF
---
apiVersion: efs.aws.upbound.io/v1beta1
kind: MountTarget
metadata:
  name: ${CLUSTER_NAME}-efs-${ZONE}
spec:
  forProvider:
    region: ${REGION}
    fileSystemIdRef:
      name: ${CLUSTER_NAME}-efs
    subnetId: ${SUBNET_ID}
    securityGroupsRefs:
      - name: ${CLUSTER_NAME}-efs-sg
  providerConfigRef:
    name: ${CLUSTER_NAME}
EOF
  done <<< "$NODE_SUBNETS"
} > efs-network.yaml
```

### Create the resources

Review both files, then apply them to the management cluster. Crossplane creates the security group and the file system first, and the rule and the mount targets as soon as their references resolve. Wait until all resources are ready. This usually takes a few minutes:

```sh
kubectl apply -f efs-filesystem.yaml -f efs-network.yaml
kubectl wait --for=condition=Ready --timeout=10m \
  -f efs-filesystem.yaml -f efs-network.yaml
```

Then generate `efs-storageclass.yaml`, the storage class for the workload cluster. The command reads the ID of the file system, which starts with `fs-`, from the management cluster:

```sh
cat > efs-storageclass.yaml <<EOF
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: efs
provisioner: efs.csi.aws.com
parameters:
  provisioningMode: efs-ap
  fileSystemId: $(kubectl get filesystem.efs.aws.upbound.io "${CLUSTER_NAME}-efs" -o jsonpath='{.status.atProvider.id}')
  directoryPerms: "700"
  uid: "1000"
  gid: "1000"
EOF
```

{{% notice note %}}
Give the mount targets **a few minutes** after they turn ready. Until AWS publishes the file system's DNS name in the VPC, mounts fail with `Failed to resolve "fs-....efs.<REGION>.amazonaws.com"`. Kubernetes retries the mount on its own, so pods start as soon as the name resolves.
{{% /notice %}}

## Mount the volume in your pods

Run the following steps against the **workload cluster**.

### Create a storage class

The storage class in `efs-storageclass.yaml` tells the driver which file system to use. With `provisioningMode: efs-ap`, the driver creates an [EFS access point](https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html) for each persistent volume claim.

In AWS, the root directory of an access point is optional and defaults to the root of the file system (`/`). The driver doesn't rely on that default. It always sets the root directory of each access point to a new directory named after the persistent volume, with a unique ID appended. As a result, every claim gets its own directory on the shared file system and can't see the data of other claims. To change this layout, use the `basePath`, `subPathPattern`, and `ensureUniqueDirectory` parameters of the storage class, described in the [driver documentation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/blob/master/docs/parameters.md).

```sh
kubectl apply -f efs-storageclass.yaml
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
    kubectl -n org-<ORGANIZATION> delete helmrelease,ocirepository \
      <CLUSTER_NAME>-aws-efs-csi-driver-bundle
    ```

## Further reading

- [Persistent volumes]({{< relref "/tutorials/storage/persistent-volumes" >}})
- [AWS EFS CSI driver repository](https://github.com/giantswarm/aws-efs-csi-driver)
- [EFS CSI driver upstream documentation](https://github.com/kubernetes-sigs/aws-efs-csi-driver/tree/master/docs)
- [Crossplane AWS provider for EFS](https://marketplace.upbound.io/providers/upbound/provider-aws-efs/)
