---
linkTitle: Preparing VMware Cloud Director for Cluster API
title: Preparing VMware Cloud Director for Cluster API
description: How to set up your VMware Cloud Director Cluster tenant to run Giant Swarm management clusters and workload clusters under your jurisdiction.
weight: 80
menu:
  main:
    identifier: gettingstarted-infraprovider-clouddirector
    parent: gettingstarted-infraprovider
last_review_date: 2023-10-03
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
---
In order to run the Giant Swarm platform in your VMware Cloud Director (VCD) environment, a number of prerequisites must be satisfied to support Cluster API Provider Vmware Cloud Director (CAPVCD).

## VCD infrastructure

VMware Cloud Director must run with API version 36 compatibility at least. However, it is highly recommended to run VCD 10.4 or above as it includes shared virtual service IPs.

## VCD User permissions

The CAPVCD controller doesn’t require to authenticate directly with the VCD API. This is done on a “per cluster” level as the user will specify a secret containing his/her credentials in the cluster manifest/app. This is so the VCD Resource quotas of each user apply when deploying clusters. 

The user configured for CAPVCD must have at least the following permissions attached to its user role in VCD:

* Rights from the default vApp Author role
* User > Manage user's own API token
* vApp > Preserve All ExtraConfig Elements During OVF Import and Export
* Gateway > View Gateway
* Gateway Services > NAT Configure, LoadBalancer Configure
* Organization VDC => Create a Shared Disk
* User > Manage user's own API token

## Networking

The infrastructure backing the OVDC where the clusters will be deployed must be backed by VMware NSX-T and NSX Advanced Load Balancer (ALB). The deprecated NSX-V is not supported.

The Load Balancer section must be enabled on the Edge gateway with a Service Engine Group (SEG). Note that it is recommended to set a dedicated SEG to properly isolate tenants from each other. A pool of external IPs must be available on the Edge gateway to create load balancers.

The nodes need at least one network with DHCP or a static IP pool enabled  to obtain an IP when spinning up. They must have access to the VCD API endpoint for the controllers to work (CAPVCD, cloud provider interface and container storage interface). Note that we support connecting multiple networks to the nodes with static routes.

Access to the internet is required for things like FluxCD pulling artifacts from Github, reaching out to Lets Encrypt to validate DNS01 challenges or containerd pulling container images. We support HTTP proxies and we can provide the list of domains to whitelist on the corporate firewall.

## vApp templates (node images)

A catalog named `giantswarm` must be accessible to the CAPVCD user with vAPP templates for the nodes to deploy. The templates must be named following this convention `ubuntu-2004-kube-v1.24.11`.

## VM Sizing Policies

VM Sizing Policies must be available to specify the flavour of the nodes when deploying VMs. Each customer can choose how to name and size these policies but we propose the following ones as a starting point:

| Name | vCPU | Memory |
|------|------|--------|
| m1.small | 1 | 2GB |
| m1.medium | 2 | 4GB |
| m1.large | 4 | 8GB |
| m1.xlarge | 8 | 16GB |
| m1.2xlarge | 16 | 64GB |

