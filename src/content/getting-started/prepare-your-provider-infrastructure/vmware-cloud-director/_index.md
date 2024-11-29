---
title: Prepare your provider environment for VMware Cloud Director
linkTitle: Prepare your VCD environment
description: Prepare your VMware Cloud Director setup to start building your cloud-native developer platform with Giant Swarm.
weight: 30
last_review_date: 2024-11-28
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I prepare my VMware Cloud Director environment for the cloud-native developer platform?
  - What do I need to do to prepare my VCD environment for the cloud-native developer platform?
---

In order to run the Giant Swarm platform in your VMware Cloud Director (VCD) environment, several prerequisites must be satisfied to support Cluster API Provider VMware Cloud Director (CAPVCD).

## Requirements

The solution has some requirements from the VCD environment, and at the same time, the controllers that provision the infrastructure need some permissions again from the VCD API.

### VMware Cloud Director

VMware Cloud Director must run at least with API version v36.0 compatibility (minimum version VCD v10.3). It's highly recommended to run VCD v10.4 or above as it includes shared virtual service IPs.

## Step 1: Networking

In terms of virtual networking, the following requirements must be met:

- Your Organization Virtual Data Center (oVDC), where the clusters will run, must be backed by VMware NSX-T and NSX Advanced Load Balancer (ALB). The deprecated NSX-V isn't supported.

- The load balancer section must be enabled on the Edge Gateway with a Service Engine Group (SEG). A dedicated SEG is recommended to isolate tenants from each other. A pool of external IPs must be available on the Edge Gateway to create load balancers.

![VCD Networking](vcd-networking.png)

- Though the platform allows multiple networks on the cluster nodes using static routes, at least one network with a static IP pool enabled is required to get an IP.

- The virtual machines (VMs) must have access to the VCD API endpoint for the controllers to work.

- Access to the Internet is required for some of our automation to pull artifacts from the registry or get new certificates from Let's Encrypt. It's possible to configure an egress HTTP proxy to control the traffic. You can check the list of domains that need to be accessible [here]({{< relref "/vintage/platform-overview/security/cluster-security/domain-allowlist/#on-premise-installations" >}}).

## Step 2: Permissions

The credentials for authentication against the VCD API are configured by cluster. The controller that interacts with the VCD API uses those credentials from a secret provided in the cluster app definition.

__Warning__: Take into account that every user is tied to its own VCD Resource quotas which may affect when deploying the infrastructure.

To obtain the credentials, you need to create a new role by browsing to `Administration > Access Control > Roles > Check vApp Author` and then click `Clone`. The suggestion is to name the role `CAPVCD`. Apart of the default permissions inherit from `vApp Author` role, the controller requires the following permissions:

- `User > Manage user's API token`
- `vApp > Preserve All ExtraConfig Elements During OVF Import and Export`
- `Gateway > View Gateway`
- `Gateway Services > NAT Configure, LoadBalancer Configure`
- `Organization VDC => Create a Shared Disk`
- `User > Manage user's API token`

## Step 3: Virtual machine templates

To provision the virtual machines (VMs) for the cluster nodes, the necessary `vApp templates` must be provided in the `giantswarm` organization's catalog. The templates use a convention with the Linux distribution and Kubernetes version on the name (for example `flatcar-stable-xxxx.y.z-kube-x.yy.zz-tooling-x.yy.1-gs`).

__Note__: Our engineers can upload the `vApp templates` to the `giantswarm` catalog, or they can provide them to you if uploads fail over a WAN connection like in some VCD environments.

## Step 4:  Virtual machine sizing

To define the set of instance types available to the users when deploying clusters, you need to prepare the [virtual machine sizing policies](https://docs.vmware.com/en/VMware-Cloud-Director/10.4/VMware-Cloud-Director-Service-Provider-Admin-Portal-Guide/GUID-F6719175-7A29-42CA-BB00-A6BDC22B3EEC.html). You can choose the name and sizes of these policies, but we propose the following ones as a starting point

| Name | vCPU | Memory |
|------|------|--------|
| m1.small | 1 | 2GB |
| m1.medium | 2 | 4GB |
| m1.large | 4 | 8GB |
| m1.xlarge | 8 | 16GB |
| m1.2xlarge | 16 | 64GB |

After all requirements are met, you can [create your first cluster following this guide]({{< relref "/getting-started/provision-your-first-workload-cluster/" >}}).

## Next step

If you are running these steps for the first time and still don't have a management cluster, Giant Swarm will provide it in the next few days. For sharing any secret with us please read [this article]({{< relref "/overview/security/sharing-secrets" >}}) first.

If you already have a management cluster, you can proceed with the next step and learn how to [access to platform API]({{< relref "/getting-started/access-to-platform-api" >}}).
