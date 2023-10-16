---
linkTitle: Azure
title: Prepare an Azure subscriptions to run Cluster API Giant Swarm cluster
description: This guide will walk you through all necessary steps to set up an Azure subscriptions with appropriate IAM roles for operating Cluster API Giant Swarm clusters.
menu:
  main:
    identifier: gettingstarted-cloudprovider-clusterapi-azure
    parent: gettingstarted-cloudprovider-clusterapi
weight: 20
user_questions:
  - How do I prepare my Azure subscription for Cluster API?
  - What do I need to configure in Azure in order to run Cluster API Giant Swarm clusters?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-10-16
---

Currently the Giant Swarm Cluster API for Azure implementation supports only running the Management and Workload Clusters in a single subscription.

## Overview

This document consists of the instructions for setting up Azure subscriptions that are needed to run Cluster API for Azure with Giant Swarm.

## Procedure for Azure subscription configuration

Currently implemented Management Clusters bootstrap process [`mc-bootstrap`](https://github.com/giantswarm/mc-bootstrap)  with Cluster API for Azure (CAPZ) requires a `bootstrap Service Principal` to authenticate the `local capz` running in `kind` onto Azure. This is required to create the final result, that is the Management Cluster in the cloud provider and delegate the `capz controller responsabilities` to it.

After the initial bootstrap is completed the `capz-controller` will use a `User Assigned managed identity` , created during the `mc-bootstrap` process for all further cloud interaction.

This identity can:

* Create Workload Clusters , and all the related resources, in the `same subscription` where the MC lives
* Be `authorized by the Customer` to create Workload Clusters, and all the related resources, in _other subscriptions_ belonging to the same tenant - **NOTE** _this is not yet implemented_
* Be `authorized by the Customer` to create Workload Clusters, and all the related resources, in _subscriptions that exist in other tenants_ - **NOTE** _this is not yet implemented_

### 1. Prerequisites

To create and assign the role to Giant Swarm's Service Principal you need:

* An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

### 2. Create management cluster service principal for bootstrapping

First step is to create a `subscription` to host the `MC Cluster` and a `bootstrap SP` that will be used for the initial creation of the Cluster.

#### Step 1a - Create the `bootstrap sp` using AZ CLI

**NOTE** Using `az add app create`, `az ad app credential reset`, `az ad sp create --id` we should be able to create a set of credential with a much shorter expiration date.

```bash

MC_SUBSCRIPTION_ID=XXXX-XXXX-XXXX-XXX
MC_NAME=ZZZZ

az login
az account set -s ${MC_SUBSCRIPTION_ID}
az ad sp create-for-rbac --role contributor --scopes="/subscriptions/${MC_SUBSCRIPTION_ID}" --display-name "${MC_NAME}-bootstrap" --years 1
az role assignment create --assignee <APP_ID_FROM_COMMAND_ABOVE> --role "User Access Administrator" --scope "/subscriptions/${MC_SUBSCRIPTION_ID}"
```

Store the output of `az ad sp create-for-rbac` , this needs to be provided to Giant Swarm in step 2.

#### Step 1b - Create the `bootstrap sp` using the `Azure Portal`

* Login to [Azure Portal](https://portal.azure.com/)
* Go to `Azure Active Directory` service
* From the left pane, select the `App registrations` section then click `New registration` from the menu at the top of the page
* Enter the name `<MC_NAME>-bootstrap`
* Select `Accounts in any organizational directory (Any Azure AD directory - Multitenant)` as Supported account types
* Click `Register`
* Go to the `Certificates & secrets` section. Under the `Client secrets` part, create a new `Client Secret`
* Set expiration to 2 Days and click `Add`
* Store the `Value` of the new secret , this needs to be provided to GiantSwarm later
* Add RoleAssignment ot the newly created App
  - Select the right `Subscription` for where the MC Should be created
  - go to `Access control (IAM)`
  - click `Add Role Assignment` and add the `Contributor` role and the `User Access Administrator` role to the APP with the `subscription` Scope

#### Step 2 - Provide generated credentials to Giant Swarm

At the end of this process the following information need to be provided to Giant Swarm using a secure transport. 

* ClientID
* ClientSecret
* SubscriptionID
* TenantID

In order to deliver this information to Giant Swarm securely:

* go to https://keybase.io/encrypt
* Add as a `recipient` the handle for the GiantSwarm employees that are performing the mc-bootstrap
* Add the Informations above into the `Message to encrypt` and click `Encrypt`
* A GPG Encrypted message should appear , click on `Done - nuke the plaintext`
* Send the whole GPG Message to GiantSwarm

## Configure Subscription to allow access for Giant Swarm Support

Last step while configuring your Subscription is to grant access for Giant Swarm Ops/Support to your subscription in order to provide 24/7 support. Access to the portal is important part of the provided support, where in some cases manual interventions have to take place.
Easiest way is to use the Azure Lighthouse service, that allows to delegate the management of resources to third parties. While following this part of the guide, you will allow the Giant Swarm Staff group to manage your resources. This is beneficial as you will not have to manage access for each person separately within your subscription, but you will be adding a managed group that is kept up to date with the current active Giant Swarm Staff from our side.

We require a built in role `Contributor` to access the resources that Giant Swarm is deploying and it can be used by default from the [Azure RBAC](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles).

You can also create your own role assignment with restrictions to access specific Resource Groups, however it needs to be remembered to refresh the role with every newly created cluster so we can provide full support starting from the clusters creation.

When all is set you can simply run this command:

```nohighlight
az deployment create --name <deploymentName (unique by subscription)> \
                     --location <AzureRegion> \
                     --template-file delegatedResourceManagement.json \
                     --parameters delegatedResourceManagement.parameters.json \
                     --verbose
```

You will have to supply a general Delegated Resource Management [template file](https://raw.githubusercontent.com/giantswarm/azure-operator/master/docs/delegatedResourceManagement.json).

The Delegated Resource Management template uses a [parameters file](https://raw.githubusercontent.com/giantswarm/azure-operator/master/docs/delegatedResourceManagement.parameters.json) to supply the needed variables for configuration.
Please remember to change the `roleDefinitionId` in case you would like to use your custom role definition. Moreover ask your Account Engineer so he can provide you the `GiantSwarmPrincipalID` and `GiantSwarmTenantID`

This command should be run for all subscriptions that are used for Giant Swarm workload clusters as well as the management cluster that orchestrates it all.  

## Accept legal terms for deployment of Flatcar image

Giant Swarm deploys [Flatcar](https://www.flatcar-linux.org/) image developed by Kinvolk from Azure Marketplace. In order to be able to run the image, it is required by Azure to accept the legal terms.
Please run the following command prior to creating a cluster on a given subscription:

```nohighlight
az vm image terms accept --offer flatcar-container-linux-free --plan stable --publisher kinvolk
```

This acceptance should be performed once for all subscriptions that are used to run Giant Swarm workload clusters.

## Further reading

* [Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer)
