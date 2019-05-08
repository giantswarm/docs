+++
title = "The Giant Swarm Platform Access Routes"
description = "General Giant Swarm Platform Access Routes Overview"
date = "2019-05-08"
weight = 20
type = "page"
categories = ["basics"]
+++

# Giant Swarm Platform Access Routes

## Intro
Access to Giant Swarm platforms can be split into two parts. 

1. Admin Access - designated for the Giant Swarm employees for managing/development/support purposes.

2. User Access - designated for GiantSwarm customers to interact with the offered services.

Both are managed via Giant Swarm VPN hopp that enables connection through jumphost of the cluster.
Giant Swarm uses two different providers of VPN to improve the resilience of offered services.

## General VPN Connection Schema

![](/img/site-to-site-vpn.png)

## Admin Access

VPN access is managed via certificates (public/private keys) and secured connection between both VPNs.
Certificates management is handled by one of GS private components. 
The general principle is that certificate is configured for each individual Giant Swarm employee.

VPN Secured access points:

* SSH - SSH Admin access is based on the Github SSO. Only users residing in the Github GS Organization are allowed to authenticate.  
  Following process describes more in detail the procedure of SSH authentication:
  ![](/img/ssh_access_process.png)

  SSH access to CP allows Giant Swarm also to manage and connect to underlying Data Platforms of the Customer.

* CP Kubernetes API - Usage of Kuberentes API on CP also follows the authentication principles of the SSH connection. 
The Github SSO based on GS Organization is used to grant access. 

***Cloud Provider Access***

At the current stage internal GS operator components responsible for managing clusters lifecycle at Customer's Cloud 
Provider are granted the admin rights by the Customer to the given API.
This point is under discussion and might be limited in the near future to limited permissions allowing management of the clusters only.

Operator secret used for authentication with Cloud Provider is stored in k8s api. 
This means that actually etcd holds authentication credentials. 
Access to etcd or k8s-api are secured based on certificates validated in Vault, 
to which only personel in approriate Github GS organization have access to.   

***Reference docs***:  
[Github Vault auth](https://www.vaultproject.io/docs/auth/github.html)  
[Vault ssh certificate](https://www.vaultproject.io/docs/secrets/ssh/signed-ssh-certificates.html)

## User Access

### Giant Swarm API

User Access is designed for Customers over Giant Swarm API. 
Principles and usage described more in details can be found [here](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/#giant-swarm-api)

### Kubernetes API

Kubernetes API of the Tenant Cluster are exposed to the Customer. 
More details on the authentication and process of granting access to it can be found [here](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/#userspace)



