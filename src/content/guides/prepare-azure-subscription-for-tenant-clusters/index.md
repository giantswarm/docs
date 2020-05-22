---
title: "Prepare an Azure subscription to run Giant Swarm tenant clusters"
description: "This guide will walk you through all necessary steps to set up an Azure subscription for operating Giant Swarm tenant clusters."
date: "2020-05-22"
type: page
weight: 100
tags: ["tutorial"]
---

# Prepare an Azure subscription to run Giant Swarm tenant clusters

In a Giant Swarm installation, the tenant clusters (the clusters running your Kubernetes workloads) can run in a separate
Azure subscription from the control plane.
This gives greater flexibility depending on the requirements, and the use case.
For example, it allows the control plane to be running in one Azure subscription, while tenant clusters operate in
different Azure subscriptions, depending on a customer’s department using them.

Giant Swarm operates tenant clusters using a service called `azure-operator` which runs on the control plane.

## Overview

In order to run Giant Swarm tenant clusters, an Azure subscription needs the following elements:

- Service Principal: the credentials that will be used to talk to Azure.
- Role assignment: a set of permission to operate tenant clusters in the Azure subscription.

## Giving GiantSwarm's Service Principal permissions on your subscription

In order to perform necessary actions to deploy and maintain tenant clusters in your Azure subscription,
`azure-operator` needs to access the subscription using GiantSwarm's Service Principal.
Here we describe all the steps to set it up.

#### 1. Prerequisites

You will need:

- An account in your Active Directory with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
- (Optional) [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

#### 2. Service Principal

Your subscription must be linked with a Tenant Active Directory (AD) which has the GiantSwarm Service Principal in it.

If the subscription where you want to run the tenant cluster is linked to the same Tenant AD than the subscription running the control plane,
you don't need to do anything else.

On the other hand, if the subscription where you want to run the tenant cluster is linked to a different Tenant AD than
the subscription running the control plane, you need to invite GiantSwarm's Service Principal to that Tenant AD.
If you don't know your Tenant ID, you can use [the Azure portal](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade),
as shown in the screenshot below:

![Azure Subscriptions list](/img/azure-subscriptions-list.png)

Alternatively you can use the Azure CLI like so:

```nohighligh
$ az account show -o table
EnvironmentName    HomeTenantId                          IsDefault    Name         State    TenantId
-----------------  ------------------------------------  -----------  -----------  -------  ------------------------------------
AzureCloud         12345678-1bcd-ef2g-8a89-987ze9087a2a  True         example      Enabled  12345678-abcd-ef2g-8a89-987ze9087a2a
```

By visiting the following link you can invite GiantSwarm's Service Principal and authorize it to the Tenant AD on behalf of your organization.
You just need to replace `${TENANT_ID}` with your Tenant ID, and `${SERVICE_PRINCIPAL_ID}` with the Service Principal ID provided by GiantSwarm.

```
https://login.microsoftonline.com/${TENANT_ID}/oauth2/authorize?client_id=${SERVICE_PRINCIPAL_ID}&response_type=code&redirect_uri=https%3A%2F%2Fwww.microsoft.com%2F
```

#### 3. Role assignment

You need to give GiantSwarm's Service Principal permission to access resources belonging to your subscription.
In your subscription, go to "Access Control (IAM)" and click the "Add Role" button, then select "Add role assignment".
In the right sidebar that pops up, please select the "Owner" role to the GiantSwarm's Service Principal.
This will give the right permissions to GiantSwarm's Service Principal.


## Configure the Giant Swarm organization

In the previous section, we explained how to invite GiantSwarm's Service Principal to your Tenant AD,
and how to give it permissions in order to run Giant Swarm tenant clusters.

Giant Swarm tenant clusters are owned by Organizations, which allow you to control access to clusters,
since only members of the owner organization have access to the management functions of a cluster,
but also allows you to select the subscription where the tenant cluster will be created.

In order to run a tenant cluster in your Azure subscription, the organization owning your cluster has to know about it.

If you have direct access to the Giant Swarm API, please set the subscription ID and Tenant ID of your organization with our [gsctl](/reference/gsctl/) CLI.
Look for the [`update organization set-credentials`](/reference/gsctl/update-org-set-credentials/#azure) command.

In case you work with a GiantSwarm partner, it might be that you don’t have access to the GiantSwarm API.
In that case, please hand over your Azure subscription ID and Tenant ID to your partner contact.

After the organization is configured, you can create clusters owned by that organization.
These clusters' resources will be created in your Azure subscription.

## Further reading

- [Basics and Concepts: Bring Your Own Cloud](/basics/byoc/)
- [gsctl Reference: `update organization set-credentials`](/reference/gsctl/update-org-set-credentials/)
- [API: Set credentials](https://docs.giantswarm.io/api/#operation/addCredentials)
