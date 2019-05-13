+++
title = "Secure access to clusters for users and Giant Swarm support"
description = "This documentation explains security measures for users and Giant Swarm support to access offered services"
date = "2019-05-09"
weight = 45
type = "page"
categories = ["basics"]
+++

# Secure access to clusters for users and Giant Swarm support

In order to provide the best service possible, Giant Swarm staff also have access to your clusters.

Therefore, we would like to explain this access, and what security measures are in place.

## Intro

Access to Giant Swarm clusters can be split into two parts. 

1. Admin Access - designated for Giant Swarm staff for management/development/support purposes.

2. User Access - designated for Giant Swarm customers to interact with the offered services.

If you would like to know more about the different parts of the Giant Swarm infrastructure, please see our [operational layers article](/basics/giant-swarm-operational-layers/)

## Admin access

Admin access is guarded by a Virtual Private Network (VPN) that is managed via certificates (public/private keys).

Certificates management is handled by combination of Vault and Giant Swarm Organization on Github. The general principle is that a certificate is configured for each individual Giant Swarm staff member.

VPN secured access points:

* **SSH** - SSH access is based on GitHub SSO. Only users in the GitHub Giant Swarm Organization are allowed to authenticate. The following diagram describes our SSH authentication in more detail:

![](./ssh_access_process.png)  

  SSH access to Control Plane allows Giant Swarm also to manage and connect to underlying Tenant Clusters of the Customer.

* **Control Plane Kubernetes API** - Usage of Kuberentes API on Control Plane also follows the authentication principles of the SSH connection.

### General VPN connection schema

Following schema illustrates how the VPN connection looks in practice. 

![](./site-to-site-vpn.png)

Cluster can be accessed by connecting to a Giant Swarm VPN server which establishes a secure connection with the jump host of the cluster.

We use two different VPN providers to provide highly resilient and available support to our customers.

### Cloud provider access

Currently, Giant Swarm operators - which are responsible for managing clusters lifecycle - are granted admin rights by the customer to the given cloud provider.

The operator secret used for authentication with the cloud provider is stored in Kubernetes' etcd.
Access to etcd or Kubernetes API are secured based on certificates signed by Vault, 
to which only personnel in the GitHub Giant Swarm organization have access to.   

## User access

User access is limited to the offered APIs for interaction with your clusters. 

### Giant Swarm API

User access is provided to you over the Giant Swarm API. 
Network access to the API endpoint is usually whitelisted to a certain range of IP addresses but it can also be configured to work over VPN.
Later case follows the security principles of the general VPN connection schema shown above under [admin access](#admin-access), where the connection to API residing in the cluster can be established only via your configured VPN.

### Kubernetes API

The Kubernetes API of the clusters are exposed to the customers. You have full control over the users that are created via the Giant Swarm API. Additionally, you can also manage users by connecting an external Identity Provider to the Kubernetes API.

## Further reading

- [GitHub Vault authentication](https://www.vaultproject.io/docs/auth/github.html) 
- [Vault SSH certificate](https://www.vaultproject.io/docs/secrets/ssh/signed-ssh-certificates.html)
- [Giant Swarm Operational Layers](/basics/giant-swarm-operational-layers/)
- [Giant Swarm API](/basics/giant-swarm-operational-layers/#giant-swarm-api)
- [Giant Swarm User Space](/basics/giant-swarm-operational-layers/#userspace): Tenant Cluster Kubernetes API
