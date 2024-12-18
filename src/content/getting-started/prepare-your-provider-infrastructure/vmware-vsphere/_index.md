---
title: Prepare your provider environment for VMware vSphere
linkTitle: VMware vSphere
description: Prepare your VMware vSphere setup to start building your cloud-native developer platform with Giant Swarm.
weight: 40
last_review_date: 2024-11-28
menu:
  principal:
    parent: getting-started-prepare-provider-infrastructure
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I prepare my vSphere environment for the cloud-native developer platform?
  - What do I need to do to prepare my vSphere environment for the cloud-native developer platform?
aliases:
  - /getting-started/cloud-provider-accounts/vmware-vsphere
  - /vintage/getting-started/cloud-provider-accounts/vmware-vsphere
---

In order to run the Giant Swarm platform in your VMware vSphere environment, several prerequisites must be satisfied to support Cluster API Provider VMware Cloud Director (CAPVCD).

## Requirements

The solution has some requirements from the vCenter side, and at the same time, the controllers that provision the infrastructure need some permissions again from the vCenter server API.

### VMware vSphere

The minimum version of vSphere required is 6.7 Update 3. It's recommended to run vSphere 7.0 or above. That versions support the `Cloud Native Storage` (CNS) feature needed for PersistentVolumes (PV) in Kubernetes.

| VMware product | Required version |
|------|------|
| VMware virtual hardware | 13 or later |
| vSphere ESXi hosts | 6.7 Update 3 or later |
| vCenter host | 6.7 Update 3 or later |

### Resource pool

It's recommended to create one resource pool across the hosts where the workload cluster virtual machines will run. However, in case of inconvenience, it's possible to run the virtual machines in the implicit root resource pool located at the vSphere cluster level.

## Step 1: Networking

The network must have:

- DHCP enabled.
- Access to vCenter endpoint on port `443` so the controllers can manage the cluster's lifecycle.
- Access to internet on port `443` to pull artifacts from our repositories, download CVE databases, pull container images, etc. You can whitelist the domains in this [domain allow list]({{ relref "/overview/security/domain-allowlist" }}). Note that we also support authenticated HTTP proxies.

**Warning**: In case you plan to use several networks on the cluster please contact Giant Swarm support to discuss the network configuration.

A vSphere environment has no concept of load balancer, which Kubernetes requires to expose services of type load balancer, and the API in a highly available mode. As a result, we include `kube-vip`, a layer-2 load balancer to address all environments. The other option is to use NSX Advanced Load Balancer when available in your environment.

{{< tabs >}}
{{< tab id="flags-kubevip" title="kube-vip">}}
Since vSphere has no concept of load balancers out of the box, Cluster API ships with [kube-vip]({{< relref "/vintage/advanced/cluster-management/vsphere-kubevip" >}}), a layer two load balancer that works with [ARP](https://en.wikipedia.org/wiki/Address_Resolution_Protocol) requests. By default, `kube-vip` only handles the Kubernetes API access. Still, at Giant Swarm, we also deploy the `kube-vip` provider to offer the capability to create services of type load balancer.

The ARP layer two protocol informs the network of the location of a new host address. `kube-vip` runs in-cluster as opposed to a more traditional external load-balancer that will forward IP packets to its upstream servers.

![CAPV kube-vip](capv-kubevip-excalidraw.png)

Due to the in-cluster operation of `kube-vip`, the cluster network where this component is deployed must have a dedicated subnet range outside of the DHCP scope. To avoid IP conflicts, we recommend having one subnet per management cluster.

![CAPV kube-vip IPAM](capv-kubevip-ipam-excalidraw.png)

When deploying a Cluster API cluster, it automatically selects an IP from the IP pool by default. However, to have available IPs for services of type load balancer in the workload cluster, you must explicitly set a CIDR in the nodes' subnet.

Learn more about how to configure `kube-vip` in the [advanced documentation]({{< relref "/vintage/advanced/cluster-management/vsphere-kubevip" >}}).
{{< /tab >}}

{{< tab id="flags-nsxalb" title="NSX ALB">}}
When using NSX Advanced Load Balancer (NSX ALB), [there are several components](https://docs.vmware.com/en/VMware-vSphere/7.0/vmware-vsphere-with-tanzu/GUID-A247F5F2-AC7E-48E7-B615-F8D361C7292A.html) involved to enable load balancer capabilities in Kubernetes.

The `controller` in NSX ALB plays a pivotal role. It's responsible for communicating the operations requested to the vCenter Server, ensuring the smooth functioning of the load balancer. Additionally, there is a `service engine` to manage virtual IP addresses and a Kubernetes `operator` to reconcile the NSX ALB resources in the clusters.

![CAPV kube-vip](capv-nsxalb-excalidraw.png)

{{< /tab >}}
{{< /tabs >}}

## Step 2: Permissions

The Cluster API controller that provisions the infrastructure in the vSphere environment needs a role with a set of permissions. To follow the principle of least privilege, it's recommended that a specific user and role be created for the controller.

**Warning**: The password may not contain `\` (backslash) characters. Ideally restrict special characters to ` . , ! ? - `

**Note**: The user creation is out of the scope of this document, but you can follow the [official VMware documentation](https://docs.vmware.com/en/VMware-vSphere/8.0/vsphere-authentication/GUID-31F302A6-D622-4FEC-9007-EE3BA1205AEA.html) in case you need help.

Create the user role browsing to `Administration > Access Control > Roles`and clicking `NEW`. The role must have at least the following permissions:

| Category | permissions |
| -------- | -------- |
| `CNS`    | `Searchable` |
| `Datastore` | `Allocate space`<br>`Browse datastore`<br>`Low level file operations` |
| `Global` | `Disable methods`<br>`Enable methods`<br>`Licenses` |
| `Network` | `Assign network` |
| `Resource` | `Assign virtual machine to resource pool` |
| `Sessions` | `Message`<br>`Validate session` |
| `Profile driven storage` _(vSphere 7)_<br>`VM storage policies` _(vSphere 8)_ | `Profile-driven storage view`<br>`View VM storage policies` |
| `vApp` | `Import` |
| `vSphere Tagging` | `Assign or Unassign vSphere Tag`<br>`Assign or Unassign vSphere Tag on Object` |
| `Virtual machine` | `Change Configuration`<br>`- Add existing disk`<br>`- Add new disk`<br>`- Add or remove device`<br>`- Advanced configuration`<br>`- Change CPU count`<br>`- Change Memory`<br>`- Change Settings`<br>`- Configure Raw device`<br>`- Extend virtual disk`<br>`- Modify device settings`<br>`- Remove disk`<br>`-Rename`<br>`Edit inventory`<br>`- Create from existing`<br>`- Create new`<br>`- Remove`<br>`Interaction`<br>`- Console interaction`<br>`- Power off`<br>`- Power on`<br>`Provisioning`<br>`- Clone template`<br>`- Customize guest`<br>`- Deploy template`<br>`- Mark as template`<br>`- Mark as virtual machine` |

Apart of the permissions you need to assign the role to the following objects:

| Resource to apply role to | Propagate to children |
| ------------------------- | --------------------- |
| vCenter Server | |
| Data centers or data center folders | |
| Hosts and clusters | |
| VM templates | |
| Resource pools | Yes |
| Distributed Port Group | |
| Distributed Switch | |
| VM and Template folders | Yes |

**Warning**: In case you want to use failure domains at the host level where a group of hosts is a failure domain (data centers, racks, PDU distribution, Etcd), Cluster API implementation needs permissions to work with `anti-affinity` rules. As a result the role requires the following permissions: `Host > Edit > Modify cluster`.

## Step 3: Virtual machine templates

To provision the virtual machines (VMs) for the cluster nodes, Giant Swarm needs permissions to upload `VM templates` to vCenter Server (included in the table above). The templates use a convention with the Linux distribution and Kubernetes version on the name (for example `flatcar-stable-xxxx.y.z-kube-x.yy.zz-tooling-x.yy.1-gs`).

## Next step

If you are running these steps for the first time and still don't have a management cluster, Giant Swarm will provide it in the next few days.

If you already have a management cluster, you can proceed with the next step and learn how to [access to platform API]({{< relref "/getting-started/access-to-platform-api" >}}).
