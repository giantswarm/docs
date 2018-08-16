+++
title = "Prepare an Azure subscription to run Giant Swarm tenant clusters"
description = "This guide will walk you through all necessary steps to set up an Azure subscription with approriate Role definition and Service Principal for operating Giant Swarm tenant clusters."
date = "2018-08-16"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Prepare an Azure subscription to run Giant Swarm tenant clusters

In a Giant Swarm installation the tenant clusters (the clusters running your Kubernetes workloads) can run in a separate Azure subscription from the host cluster. This gives greater flexibility depending on the requirements and the use case. For example, it allows the host cluster to be running in one Azure subscription, while tenant clusters operate in different Azure subscriptions, depending on a customer’s department using them.

Giant Swarm operates tenant clusters using a service called `azure-operator` which runs on the host cluster.

## Overview

In order to run Giant Swarm tenant clusters, an Azure subscription needs the following elements:

- Role definition: a set of permission to operate tenant clusters in the Azure subscription.
- Service Principal: an identity (bound to the previously defined Role definition) to access the Azure subscription.

## Create Azure Role definition and Service Principal

In order to perform necessary actions to deploy and maintain tenant clusters in your Azure subscription, `azure-operator` needs to access the subscription using a Service Principal.
Here we describe all the steps to set it up.

#### 1. Prerequisites

To create a Service Principal you need:

- An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](User Access Administrator) role.
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

#### 2. Role definition

Download our [Role definition template](https://raw.githubusercontent.com/giantswarm/azure-operator/master/policies/guest.tmpl.json).

Open it and replace `${SUBSCRIPTION_ID}` with your subscription id.

To find out your subscription ID you can use [the Azure portal](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade), as shown in the screenshot below:

![Azure Subscriptions list](/img/azure-subscriptions-list.png)

Alternatively you can use the Azure CLI like so:

```nohighlight
$ az account list --output table
Name     CloudName    SubscriptionId                        State    IsDefault
-------  -----------  ------------------------------------  -------  -----------
Example  AzureCloud   6ec148b8-8bea-4dd3-82bc-1787c8260e4a  Enabled  True
```

With the edited role definition in the file `guest.json`, create the role definition using the Azure CLI:

```nohighlight
$ az role definition create --role-definition @guest.json
```

On success this command prints the created role definition.

#### 3. Service Principal

Create the service principal using the Azure CLI:

```nohighlight
$ az ad sp create-for-rbac --name "azure-operator-sp" --role "azure-operator" --query '{client_id:appId, secret_key:password, tenant_id:tenant, subscription_id:""}'
{
    "client_id": "72bc3de4-3cf8-46c5-bd2b-243368ed0622",
    "secret_key": "d6b2cb93-cae9-44b3-8ec5-dc5feb8c28ba",
    "subscription_id": null,
    "tenant_id": "31f75bf9-3d8c-4691-95c0-83dd71613db8"
}
```

## Configure the Giant Swarm organization

In the previous section, we explained how to create the Service Principal in the Azure subscription in order to run Giant Swarm tenant clusters.

Giant Swarm tenant clusters are owned by organizations, which allows to control access to clusters, since only members of the owner organization have access to the management functions of a cluster.

In order to run a tenant cluster in your Azure subscription, the organization owning your cluster has to know about the Service Principal you just created.

In the output from step 3 of the previous section you need to replace the `null` value in front of `subscription_id:` with your actual subscription ID. This document is the credential which needs to be registered within Giant Swarm API.

```json
{
    "client_id": "72bc3de4-3cf8-46c5-bd2b-243368ed0622",
    "secret_key": "d6b2cb93-cae9-44b3-8ec5-dc5feb8c28ba",
    "subscription_id": "6ec148b8-8bea-4dd3-82bc-1787c8260e4a",
    "tenant_id": "31f75bf9-3d8c-4691-95c0-83dd71613db8"
}
```

If you have direct access to the Giant Swarm API, please follow the [documentation](https://docs.giantswarm.io/api/#operation/addCredentials) to set the credentials of your organization via the API.

```nohighlight
$ curl -X POST -H "Authorization: giantswarm ${TOKEN}" https://api.g8s.example.westeurope.azure.gigantic.io/v4/organizations/giantswarm/credentials -d \
'{
  "provider": "azure",
  "azure": {
    "credential": {
      "client_id": "72bc3de4-3cf8-46c5-bd2b-243368ed0622",
      "secret_key": "d6b2cb93-cae9-44b3-8ec5-dc5feb8c28ba",
      "subscription_id": "6ec148b8-8bea-4dd3-82bc-1787c8260e4a",
      "tenant_id": "31f75bf9-3d8c-4691-95c0-83dd71613db8"
    }
  }
}'
```

The response should look similar to this:

```json
{
  "code": "RESOURCE_CREATED",
  "message": "A new set of credentials has been created with ID 'hdc2m1'"
}
```

In case you work with a Giant Swarm partner, it might be that you don’t have access to the Giant Swarm API. In that case, please hand over the credential to your partner contact.
