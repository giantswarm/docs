+++
title = "Prepare an Azure subscription to run Giant Swarm guest clusters"
description = "This guide will walk you through all necessary steps to set up an Azure subscription with approriate role definition and service principal for operating Giant Swarm guest clusters."
date = "2018-08-09"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Prepare an Azure subscription to run Giant Swarm guest clusters

In a Giant Swarm installation the guest clusters (the clusters running your Kubernetes workloads) can run in a separate Azure subscription from the host cluster. This gives great flexibility depending on the requirements and the use case. For example, it allows the host cluster to be running in an Azure subscription owned by Giant Swarm, while guest clusters operate in different Azure subscriptions each, depending on a customer’s department using them.
Giant Swarm operates guest clusters using a service called `azure-operator` which runs on the host cluster.

## Overview

In order to run Giant Swarm guest clusters, an Azure subscription needs the following elements :

- Role definition: a set of permission to operate guest clusters in the Azure subscription.
- Service principal: an identity (bound to the previoulsy defined role definition) to access the Azure subscription.

## Create Azure role definition and service principal

In order to perform necessary actions to deploy and maintain guest clusters in your Azure subscription, `azure-operator` needs to access the subscription using a service principal.
Here we describe all the steps to set it up.

#### 1. Prerequisites

To create a service principal you need:

- An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](User Access Administrator) role
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed

#### 2. Role definition

Download our [role definition](https://raw.githubusercontent.com/giantswarm/azure-operator/38caa99efac9db440433c73646de54a5478f8cb6/policies/guest.json).

Open it and replace `${SUBSCRIPTION_ID}` with your subscription id, you can find it [here](https://portal.azure.com/#blade/Microsoft_Azure_Billing/SubscriptionsBlade) using the portal, or using Azure cli `az account list --output table`.

Create the role definition : `az role definition create --role-definition @/path/to/guest.json`.

#### 3. Service principal

Create the service principal : `az ad sp create-for-rbac --name "azure-operator-sp" --role "azure-operator" --query '{client_id:appId, secret_key:password, tenant_id:tenant, subscription_id:""}'`

## Configure the Giant Swarm organization

In the previous section, we explained how to create the service principal in the Azure subscription in order to run Giant Swarm guest clusters.

Giant Swarm guest clusters are owned by organizations, which allows to control access to clusters, since only members of the owner organization have access to the management functions of a cluster.

In order to run a guest cluster in your Azure subscription, the organization owning your cluster has to know about the service principal you just created.

In the output from step 3 of the previous section you need to replace the `null` value in front of `subscription_id:` with your actual subscription ID. This document is the credential which needs to be registered within Giant Swarm API.

- If you have direct access to the Giant Swarm API, please follow the [documentation](https://docs.giantswarm.io/api/#operation/addCredentials) to set the credentials of your organization via the API.
- In case you work with a Giant Swarm partner, it might be that you don’t have access to the Giant Swarm API. In that case, please hand over the credential to your partner contact.
