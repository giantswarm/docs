+++
title = "Secured access to clusters for users and Giant Swarm support"
description = "This documentation explains security measures for users and Giant Swarm support accessing offered services"
date = "2019-05-09"
weight = 45
type = "page"
categories = ["basics"]
+++

# Secured access to clusters for users and Giant Swarm support

In order to provide the best service possible besides you having access to your clusters, also Giant Swarm staff will be able to connect.

Thus it should be explained how this access differs and what security measures are brought into place so that your data is saved with us. 

## Intro

Access to Giant Swarm clusters can be split into two parts. 

1. Admin Access - designated for Giant Swarm staff for managing/development/support purposes.

2. User Access - designated for Giant Swarm customers to interact with the offered services.

If you would like to know more on the different parts of the Giant Swarm infrastructure, please see our [operational layers article](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/)

## Admin Access

Admin access is guarded by Virtual Private Network (VPN) that is managed via certificates (public/private keys) and secured connection between both VPNs.

Certificates management is handled by one of Giant Swarm's private components. The general principle is that a certificate is configured for each individual Giant Swarm staff member.

VPN Secured access points:

* *SSH* - SSH Admin access is based on the Github SSO. Only users residing in the Github Giant Swarm Organization are allowed to authenticate. Following process describes more in detail the procedure of SSH authentication:
  ![](./ssh_access_process.png)  
  SSH access to Control Plane allows Giant Swarm also to manage and connect to underlying Data Platforms of the Customer.

* *Control Plane Kubernetes API* - Usage of Kuberentes API on Control Plane also follows the authentication principles of the SSH connection.

***General VPN Connection Schema***

Following schema illustrates how the VPN connection looks in practice. 

![](./site-to-site-vpn.png)

Cluster can be accessed by connecting to Giant Swarm VPN server which establishes secure connection with jump host of the cluster.

We use two different VPN providers in order to bring the best and fastest support possible.

***Cloud Provider Access***

At the current stage internal Giant Swarm operator components responsible for managing clusters lifecycle at Customer's Cloud Provider are granted the admin rights by the customer to the given API.
This point is under discussion and might be limited in the near future to limited permissions allowing management of the clusters only.

The operator secret used for authentication with Cloud Provider is stored in Kubernetes API. 
This means that actually etcd holds authentication credentials. 
Access to etcd or Kubernetes API are secured based on certificates validated in Vault, 
to which only personel in approriate Github Giant Swarm organization have access to.   

***Reference docs***:  
[Github Vault auth](https://www.vaultproject.io/docs/auth/github.html)  
[Vault SSH certificate](https://www.vaultproject.io/docs/secrets/ssh/signed-ssh-certificates.html)

## User Access

User access is limited to the offered API's for interaction with your clusters. 

### Giant Swarm API

User Access is provided to you over Giant Swarm API. 
Access to API itself is usually whitelisted to certain range of IP addresses but it can be a also configured to work over VPN. 
Later case follows the security principles of General VPN Connection Schema which was explained in Admin Access case.   

Principles and usage described more in details can be found [here](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/#giant-swarm-api)

### Kubernetes API

Kubernetes API of the Tenant Cluster are exposed to the customer. You have full control over the users that are created via Giant Swarm API. Additionally you can also manage users via external Identity Provider by connecting the API to it.  

More details on the authentication and process of granting access to it can be found [here](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/#userspace)


