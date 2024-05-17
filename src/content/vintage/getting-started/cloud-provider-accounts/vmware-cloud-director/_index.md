---
linkTitle: Preparing VMware Cloud Director for CAPI
title: Preparing VMware Cloud Director for Cluster API
description: How to set up your VMware Cloud Director Cluster tenant to run Giant Swarm management clusters and workload clusters under your jurisdiction.
weight: 40
user_questions:
  - What are the VMware Cloud Director prerequisites for use with Giant Swarm?
  - What do I need to configure in VMware Cloud Director in order to run Giant Swarm clusters?
  - What user permissions do I need to run Giant Swarm clusters in VMware Cloud Director?
aliases:
  - /getting-started/cloud-provider-accounts/vmware-cloud-director
menu:
  main:
    identifier: gettingstarted-infraprovider-clouddirector
    parent: gettingstarted-infraprovider
last_review_date: 2023-10-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---
In order to run the Giant Swarm platform in your VMware Cloud Director (VCD) environment, a number of prerequisites must be satisfied to support Cluster API Provider VMware Cloud Director (CAPVCD).

## Cloud Director infrastructure

VMware Cloud Director must run at least with API version v36.0 compatibility (minimum version VCD v10.3). It is highly recommended to run VCD v10.4 or above as it includes shared virtual service IPs.

## VCD User permissions

The CAPVCD controller doesn’t require to authenticate directly with the VCD API. This is done on a “per cluster” level as the user will specify a secret containing their credentials in the cluster manifest/app. This is so the VCD Resource quotas of each user apply when deploying clusters. After preparing all requirements, you will read about these details in [Creating a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}).

The user configured for CAPVCD must have at least the following permissions. In order to do this, create a new role by browsing to `Administration > Access Control > Roles > Check vApp Author and click Clone` that you can name `CAPVCD`.

Ensure the role has the same rights as the default vApp Author role by cloning it as described above and add the following permissions to it:

* `User > Manage user's own API token`
* `vApp > Preserve All ExtraConfig Elements During OVF Import and Export`
* `Gateway > View Gateway`
* `Gateway Services > NAT Configure, LoadBalancer Configure`
* `Organization VDC => Create a Shared Disk`
* `User > Manage user's own API token`

## Networking

The infrastructure backing the OVDC (Organization Virtual Datacenter) where the clusters will be deployed must be backed by VMware NSX-T and NSX Advanced Load Balancer (ALB). The deprecated NSX-V is not supported.

The Load Balancer section must be enabled on the Edge gateway with a Service Engine Group (SEG). Note that it is recommended to set a dedicated SEG to properly isolate tenants from each other. A pool of external IPs must be available on the Edge gateway to create load balancers.

For creating Kubernetes nodes, at least one network with DHCP or a static IP pool enabled is required to obtain an IP. They must have access to the VCD API endpoint for the controllers to work (CAPVCD, cloud provider interface and container storage interface). Note that we support connecting multiple networks to the nodes with static routes.

Access to the internet is required for things like Flux (our continuous delivery tooling) pulling artifacts from GitHub, reaching out to Let's Encrypt for certificate issuing, or containerd pulling container images. We support HTTP proxies and can provide the list of domains to allowlist on the corporate firewall.

## vApp templates (node images)

A vApp template catalog named `giantswarm` must be accessible to the CAPVCD user with vAPP templates for the nodes to deploy. The templates must be named following this convention `ubuntu-2004-kube-v1.24.11`. We will upload the vApp templates to the catalog or we will provide them to you as uploads can fail over WAN connection in some VCD environments.

## VM Sizing Policies

VM Sizing Policies must be available to specify the flavour of the nodes when deploying VMs. You can find the procedure on how to create VM Sizing Policies [here](https://docs.vmware.com/en/VMware-Cloud-Director/10.4/VMware-Cloud-Director-Service-Provider-Admin-Portal-Guide/GUID-F6719175-7A29-42CA-BB00-A6BDC22B3EEC.html).

Each customer can choose how to name and size these policies but we propose the following ones as a starting point:

| Name | vCPU | Memory |
|------|------|--------|
| m1.small | 1 | 2GB |
| m1.medium | 2 | 4GB |
| m1.large | 4 | 8GB |
| m1.xlarge | 8 | 16GB |
| m1.2xlarge | 16 | 64GB |
