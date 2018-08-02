+++
title = "Prepare an Azure subscription to run Giant Swarm guest clusters"
description = "This guide will walk you through all necessary steps to set up an Azure subscription with approriate role definition and service principal for operating Giant Swarm guest clusters."
date = "2018-08-09"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Prepare an Azure subscription to run Giant Swarm guest clusters

In a Giant Swarm installation the guest clusters (the clusters running your Kubernetes workloads) can run in a separate Azure subscription from the host cluster. This gives greater flexibility depending on the requirements and the use case. For example, it allows the host cluster to be running in one Azure subscription, while guest clusters operate in different Azure subscriptions, depending on a customer’s department using them.

Giant Swarm operates guest clusters using a service called `azure-operator` which runs on the host cluster.

## Overview

In order to run Giant Swarm guest clusters, an Azure subscription needs the following elements:

- Role definition: a set of permission to operate guest clusters in the Azure subscription.
- Service Principal: an identity (bound to the previous defined role definition) to access the Azure subscription.

## Create Azure Role definition and Service Principal

In order to perform necessary actions to deploy and maintain guest clusters in your Azure subscription, `azure-operator` needs to access the subscription using a service principal.
Here we describe all the steps to set it up.

#### 1. Prerequisites

To create a service principal you need:

- An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](User Access Administrator) role.
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

#### 2. Role definition

Download our [role definition](https://raw.githubusercontent.com/giantswarm/azure-operator/38caa99efac9db440433c73646de54a5478f8cb6/policies/guest.json).

Open it and replace `${SUBSCRIPTION_ID}` with your subscription id.

You can find it:

- [here](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade) using the portal
![Azure Subscriptions list](/img/azure-subscriptions-list.png)

- using Azure cli
```
$ az account list --output table
Name                         CloudName    SubscriptionId                        State    IsDefault
---------------------------  -----------  ------------------------------------  -------  -----------
Example                      AzureCloud   6ec148b8-8bea-4dd3-82bc-1787c8260e4a  Enabled  True
```

Create the role definition

```
$ az role definition create --role-definition @guest.json
{
  "assignableScopes": [
    "/subscriptions/6ec148b8-8bea-4dd3-82bc-1787c8260e4a"
  ],
  "description": "Role for github.com/giantswarm/azure-operator",
  "id": "/subscriptions/6ec148b8-8bea-4dd3-82bc-1787c8260e4a/providers/Microsoft.Authorization/roleDefinitions/70969f8f-eab5-4db7-87bf-5c8053431a85",
  "name": "70969f8f-eab5-4db7-87bf-5c8053431a85",
  "permissions": [
    {
      "actions": [
        "*"
      ],
      "dataActions": [],
      "notActions": [
        "Microsoft.Authorization/elevateAccess/Action"
      ],
      "notDataActions": []
    }
  ],
  "roleName": "azure-operator",
  "roleType": "CustomRole",
  "type": "Microsoft.Authorization/roleDefinitions"
}
```

#### 3. Service Principal

Create the service principal

```
$ az ad sp create-for-rbac --name "azure-operator-sp" --role "azure-operator" --query '{client_id:appId, secret_key:password, tenant_id:tenant, subscription_id:""}'
{
    "client_id": "72bc3de4-3cf8-46c5-bd2b-243368ed0622",
    "secret_key": "d6b2cb93-cae9-44b3-8ec5-dc5feb8c28ba",
    "subscription_id": null,
    "tenant_id": "31f75bf9-3d8c-4691-95c0-83dd71613db8"
}
```

## Configure the Giant Swarm organization

In the previous section, we explained how to create the service principal in the Azure subscription in order to run Giant Swarm guest clusters.

Giant Swarm guest clusters are owned by organizations, which allows to control access to clusters, since only members of the owner organization have access to the management functions of a cluster.

In order to run a guest cluster in your Azure subscription, the organization owning your cluster has to know about the service principal you just created.

In the output from step 3 of the previous section you need to replace the `null` value in front of `subscription_id:` with your actual subscription ID. This document is the credential which needs to be registered within Giant Swarm API.

```
{
    "client_id": "72bc3de4-3cf8-46c5-bd2b-243368ed0622",
    "secret_key": "d6b2cb93-cae9-44b3-8ec5-dc5feb8c28ba",
    "subscription_id": "6ec148b8-8bea-4dd3-82bc-1787c8260e4a",
    "tenant_id": "31f75bf9-3d8c-4691-95c0-83dd71613db8"
}
```

- If you have direct access to the Giant Swarm API, please follow the [documentation](https://docs.giantswarm.io/api/#operation/addCredentials) to set the credentials of your organization via the API.
- In case you work with a Giant Swarm partner, it might be that you don’t have access to the Giant Swarm API. In that case, please hand over the credential to your partner contact.
