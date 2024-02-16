---
title: Persistent volumes
description: Basic information on using Persistent Volumes in Giant Swarm workload clusters.
weight: 90
menu:
  main:
    identifier: gettingstarted-persistentvolumes
    parent: getting-started
last_review_date: 2023-12-19
aliases:
  - /getting-started/persistent-volumes
  - /getting-started/persistent-volumes/aws/
  - /getting-started/persistent-volumes/azure/
  - /getting-started/persistent-volumes/on-premises/
  - /getting-started/persistent-volumes/vmware-cloud-director/
  - /getting-started/persistent-volumes/vmware-vsphere/
  - /guides/using-persistent-volumes-on-aws/
  - /guides/using-persistent-volumes-on-azure/
  - /guides/using-persistent-volumes-on-baremetal/
  - /guides/using-persistent-volumes-on-vSphere/
  - /ui-api/observability/prometheus/persistent-volumes/aws/
  - /ui-api/observability/prometheus/persistent-volumes/azure
  - /ui-api/observability/prometheus/persistent-volumes/on-premises
  - /ui-api/observability/prometheus/persistent-volumes/vSphere/
user_questions:
  - How can I use persistent volumes in my AWS clusters?
  - How can I use persistent volumes in my Azure clusters?
  - How can I use persistent volumes in my VMware Cloud Director clusters?
  - How can I use persistent volumes in my VMware vSphere clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

For more documentation related to persistent volumes and storage, please refer to our advanced section on [storage]({{< relref "/vintage/advanced/storage/" >}}).

## Dynamic provisioning and storage classes

{{< tabs >}}
{{< tab id="storage-classes-aws" for-impl="aws_any" >}}

If your cluster is running in the cloud on Amazon Web Services (AWS), it comes with a [dynamic storage provisioner for Elastic Block Storage (EBS)](https://github.com/giantswarm/aws-ebs-csi-driver-app). This enables you to store data beyond the lifetime of a pod.

Your Kubernetes cluster will have a default Storage Class `gp3` deployed. It is automatically selected if you do not specify the Storage Class in your Persistent Volumes.

As a cluster admin, you can create additional Storage Classes or edit the default class to use different types of EBS volumes, or add encryption, for example. For this, you need to create (or edit) [`StorageClass` objects](https://kubernetes.io/docs/concepts/storage/storage-classes/#aws-ebs).

{{< /tab >}}
{{< tab id="storage-classes-vintage-azure" for-impl="vintage_azure" >}}

If your cluster is running in the cloud on Azure, it comes with four dynamic storage provisioners using different flavors of Azure Managed Disks and Azure File shares. This enables you to store data beyond the lifetime of a pod.

The pre-installed storage classes are:

- `managed-premium` (default): Provisions a `Premium LRS` [Managed disk](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) and thus can be used only on Kubernetes nodes that run on supported VM types (those with an `s` in their name).
- `managed-standard`: Provisions a `Standard LRS` [Managed disk](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) and can be used on any VM instance type.
- `af-premium`: Provisions a volume backed by the [Azure File Share](https://azure.microsoft.com/en-us/products/storage/files/) service within a `Premium LRS` storage account.
- `af-standard`: Provisions a volume backed by the [Azure File Share](https://azure.microsoft.com/en-us/products/storage/files/) service within a `Standard LRS` storage account.

{{< /tab >}}
{{< tab id="storage-classes-capz" for-impl="capz_vms" >}}

The pre-installed and default storage class is `managed-premium`. It provisions a `Premium LRS` [Managed disk](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview) and thus can be used only on Kubernetes nodes that run on supported VM types (those with an `s` in their name).

{{< /tab >}}
{{< tab id="storage-classes-cloud-director" for-impl="vcd_any" >}}

If your cluster is running on VMware Cloud Director (VCD), it comes with a dynamic storage provisioner for Named Disks. This enables you to store data beyond the lifetime of a pod into virtual disks.

Your Kubernetes cluster will have a default storage class `csi-vcd-sc-delete` deployed, which will automatically get selected if you do not specify the storage class in your persistent volumes. On deletion of the volume, the data is deleted. In order to avoid deleting the data when the `PersistentVolume` object is deleted, you can use the storage class `csi-vcd-sc-retain` which is configured with `reclaimPolicy: Retain`.

As a cluster admin, you can create additional storage classes to use different types of VMware Storage Profiles, or add encryption, for example. For this, you need to create (or edit) [`StorageClass` objects](https://kubernetes.io/docs/concepts/storage/storage-classes/#vcp-provisioner).

{{< /tab >}}
{{< tab id="storage-classes-vsphere" for-impl="vsphere_any" >}}

If your cluster is running on VMware vSphere, it comes with a dynamic storage provisioner for Cloud Native Storage disks (CNS). This enables you to store data beyond the lifetime of a pod into virtual disks.

Your Kubernetes cluster will have a default storage class `csi-vsphere-sc-delete` deployed, which will automatically get selected if you do not specify the storage class in your persistent volumes. Another storage class `csi-vsphere-sc-retain` is also created with `reclaimPolicy: Retain` which you must explicitely specify to use.

As a cluster admin, you can create additional storage classes to use different types of VMware Storage Profiles, or add encryption, for example. For this, you need to create (or edit) [`StorageClass` objects](https://kubernetes.io/docs/concepts/storage/storage-classes/#vsphere).

{{< /tab >}}
{{< /tabs >}}

## Creating persistent volumes

The usual and most straight forward way to create a persistent volume is to create a [`PersistentVolumeClaim` object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims), which will automatically create a corresponding `PersistentVolume` (PV) for you.

A less used alternative is to first create a [`PersistentVolume` object](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes) and then claim that PV using a `PersistentVolumeClaim` (PVC) using a [selector](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#selector).

Under the hood, the Dynamic Storage Provisioner will take care that a corresponding volume with the correct parameters is created. For example, an EBS Volume if your cluster is in the AWS cloud and the corresponding storage class was chosen.

## Using persistent volumes in a pod

Once you have a `PersistentVolumeClaim`, you can [mount it as a volume](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes) in your pods.

Most storage classes, such as AWS EBS volumes, only allow mounting the volume in a single pod (`ReadWriteOnce` access mode). Depending on the storage class, you can set a different [access mode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes) in the PVC object.

{{< tabs >}}
{{< tab id="volume-specifics-aws" for-impl="aws_any" >}}

The EBS volume stays detached from your nodes as long as it is not claimed by a pod. As soon as a pod claims it, it gets attached to the node that runs the pod.

{{< /tab >}}
{{< tab id="volume-specifics-azure" for-impl="azure_any" >}}

Note that Azure Managed Disk volumes can only be used by a single pod at a time. Thus, the access mode of your PVC can only be `ReadWriteOnce`.

This limitation doesn't apply to Azure File Share volumes which can be attached with the `ReadWriteMany` policy.

{{< /tab >}}
{{< tab id="volume-specifics-vcd" for-impl="vcd_any" >}}

Do not delete virtual machines that have a Named Disk attached or it will be left in an inconsistent state and the VCD admins will need to intervene to clean it up.

{{< /tab >}}
{{< tab id="volume-specifics-vsphere" for-impl="vsphere_any" >}}

CNS disks currently only support `ReadWriteOnce` access mode with block storage-backed virtual disks but vSAN File Services (NFS in the background) supports `ReadWriteMany` as an alternative.

Under the hood, the CNS disk stays detached from the virtual machines as long as it is not claimed by a pod and you can visualize it in the vSphere client by browsing `Cluster > Monitor > Cloud Native Storage > Container volumes`. As soon as a pod claims it, it gets attached to the virtual machine running the node that holds the pod.

{{< /tab >}}
{{< /tabs >}}

### Example

First, create a PVC:

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
  # storageClassName: "xyz"
```

The storage class is commented out in the above example. Kubernetes will therefore use the default storage class. We recommend specifying the class explicitly.

Now you can create a pod that mounts the PVC:

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
          name: myvol
  volumes:
    - name: myvol
      persistentVolumeClaim:
        claimName: myclaim
```

This deploys an NGINX pod which serves the contents of the volume (which at this point is very likely still empty).

## Expanding the size of persistent volume claims

Persistent volume claims can be expanded by editing the claim and requesting a larger size. It will trigger an update in the underlying persistent volume, and the related provider object such as an AWS EBS volume. Kubernetes always uses the existing one.

In case the volume to be expanded contains a file system, the [resizing is only performed once the pod is restarted](https://kubernetes.io/blog/2018/07/12/resizing-persistent-volumes-using-kubernetes/#file-system-expansion). Not all volumes can be resized. The `StorageClass.spec.allowVolumeExpansion` field typically denotes the availability of this features. Expansion can also be time-consuming, so consider that the pod may not be available during the resizing process. Kubernetes will trigger an update in the `PersistentVolume` object and go through the events `Resizing`, `FileSystemResizeRequired` and `FileSystemResizeSuccessful`.

{{< tabs >}}
{{< tab id="expansion-specifics-aws" for-impl="aws_any" >}}

Expanding EBS volumes is a time consuming operation. Also, there is a [per-volume quota](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html) of one modification every 6 hours.

{{< /tab >}}
{{< tab id="expansion-specifics-azure" for-impl="azure_any" >}}

For Azure Managed Disk volumes, it is mandatory to release the PVC (i.e. stop the pod that is mounting it) before the resize operation begins. This is a limitation of Azure cloud that does not apply to Azure File Share volumes.

{{< /tab >}}
{{< tab id="expansion-specifics-vcd" for-impl="vcd_any" >}}

As of version 1.4.0 of the VCD Container Storage Interface (CSI), volume expansion is [currently not supported](https://github.com/vmware/cloud-director-named-disk-csi-driver/issues/27).

{{< /tab >}}
{{< tab id="expansion-specifics-vsphere" for-impl="vsphere_any" >}}

The vSphere Container Storage Plug-in supports volume expansion for block volumes that are created dynamically or statically.

Persistent volume claims can be expanded in `Offline` and `Online` mode (PVC used by a pod and mounted on a node) by editing the claim and requesting a larger size.

{{< /tab >}}
{{< /tabs >}}

## Deleting persistent volumes

If you delete a `PersistentVolumeClaim` resource, the respective `PersistentVolume` gets deleted as well.

The volume and its data will persist as long as the corresponding `PersistentVolume` resource exists. By default, deleting the resource will also delete the corresponding provider-specific volume, which means that all stored data is lost. This can be changed with the [reclaim policy](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#reclaiming). The default storage class uses `reclaimPolicy: Delete`. If you have data that must not get lost even on accidental deletion of the Kubernetes objects, consider using a storage class with `reclaimPolicy: Retain`.

Note that deleting an application that is using persistent volumes might not automatically delete its storage, so in some cases you will have to manually delete the `PersistentVolumeClaim` resources to clean up.

## Further reading

- [Storage classes](https://kubernetes.io/docs/concepts/storage/storage-classes/)
- [Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistent-volumes)
- [Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)
- [Claim persistent volumes in pods](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#claims-as-volumes)
- Provider-specific

    - [AWS EBS](https://aws.amazon.com/ebs/)
    - [Azure Managed Disks](https://learn.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview)
    - [Azure File Share](https://azure.microsoft.com/en-us/products/storage/files/)
