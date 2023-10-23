---
linkTitle: Azure
title: Prepare an Azure subscription to run Cluster API Giant Swarm cluster
description: This guide will walk you through all necessary steps to set up an Azure subscription with appropriate IAM roles for operating Cluster API Giant Swarm clusters.
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

Currently, the Giant Swarm Cluster API for Azure implementation supports only running the Management and Workload Clusters in a single subscription.

## Overview

This document consists of the instructions for setting up Azure subscriptions that are needed to run Cluster API for Azure with Giant Swarm.

## Prerequisites

There are two main groups of requirements to be met before going over next steps:

1. Azure subscription must be chosen from existing ones or created if needed in customer Azure account. For security reasons in terms of any sensitive data stored within customer accounts, we advise to use a subscription only designated for Giant Swarm Azure resources management.

2. An individual has to have the following permissions and tools working within the designated Azure subscription:

* An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

### Configure subscription to allow access to Giant Swarm Support

Firstly, please grant access for Giant Swarm Ops/Support to your Azure subscription. Access to the portal is important for our 24/7 support, where in some cases investigation and manual interventions have to take place.
The easiest way is to create an [Azure Deployment Environment](https://azure.microsoft.com/en-us/products/deployment-environments) to delegate the management of resources to third parties. In this case, you need to allow the Giant Swarm Staff group to manage your resources. This is beneficial as you will not have to manage access for each person separately within your subscription, but you will add a managed group that is kept up to date by Giant Swarm. Technically, an [Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer) template is used for resource delegation.

We recommend choosing Azure's [built-in role `Contributor`](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) to give Giant Swarm access and deployment permissions for resources within your subscription.

Alternatively, you can create your own role assignment with restrictions to access specific Resource Groups, however it must be kept up to date so that Giant Swarm can provide full support also for newly-created clusters.

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

__Warning__: Please remember to change the `roleDefinitionId` in case you would like to use your custom role definition. Moreover, ask your Account Engineer so he can provide you with the `GiantSwarmPrincipalID` and `GiantSwarmTenantID` values.

### Accept legal terms for the deployment of Flatcar Linux images

Giant Swarm deploys [Flatcar Linux](https://www.flatcar-linux.org/) images for Kubernetes cluster nodes. It is developed by Kinvolk and taken from the Azure Marketplace. In order to be able to run the images, it is required by Azure to accept the legal terms.

Please run the following command prior to creating a cluster on a given subscription:

```sh
az vm image terms accept --offer flatcar-container-linux-free --plan stable --publisher kinvolk
```

This acceptance needs to be performed only once for a subscription that is used to run Giant Swarm workload clusters.

### Configure Azure subscription for Management and Workload Cluster deployments

Currently implementation of management cluster's bootstrap process with Cluster API for Azure (CAPZ) requires a [Azure Service Principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals?tabs=browser#service-principal-object) which we will further refer to as _Giant Swarm Service Principal_. This service principal is required to be configured with all necessary permissions for creation and managing Azure resources.

During bootstrapping process a [User Assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp) is created that is from that point used for any interactions with the cloud resources.  

This identity can:

* Create Workload Clusters, and all the related resources, in the `same subscription` where the MC lives
* Be `authorized by the Customer` to create Workload Clusters, and all the related resources, in _other subscriptions_ belonging to the same tenant - __NOTE__ _this is not yet implemented_
* Be `authorized by the Customer` to create Workload Clusters, and all the related resources, in _subscriptions that exist in other tenants_ - __NOTE__ _this is not yet implemented_

### Create management cluster service principal for bootstrapping

After the prerequisites are satisfied, we can continue to create the _Giant Swarm Service Principal_. The creation can be performed in two different ways, either via [Azure CLI](#create-the-service-principal-using-az-cli) or [Azure Portal](#create-the-service-principal-using-the-azure-portal).

#### Step 1 - Create the service principal

##### Create the service principal using AZ CLI

```bash

MC_SUBSCRIPTION_ID=XXXX-XXXX-XXXX-XXX
MC_NAME=ZZZZ

az login
az account set -s ${MC_SUBSCRIPTION_ID}
az ad sp create-for-rbac --role contributor --scopes="/subscriptions/${MC_SUBSCRIPTION_ID}" --display-name "${MC_NAME}-bootstrap"
az role assignment create --assignee <APP_ID_FROM_COMMAND_ABOVE> --role "User Access Administrator" --scope "/subscriptions/${MC_SUBSCRIPTION_ID}"
```

Store the output of `az ad sp create-for-rbac` , this needs to be provided to Giant Swarm in step 2.

##### Create the service principal using the Azure Portal

* Login to the [Azure Portal](https://portal.azure.com/)
* Go to "Azure Active Directory" service
* From the left pane, select the "App registrations" section, then click "New registration" from the menu at the top of the page
* Enter the name `<MC_NAME>-bootstrap`
* Select "Accounts in any organizational directory (Any Azure AD directory - Multitenant)" as "Supported account types"
* Click "Register"
* Go to the "Certificates & secrets" section. Under the "Client secrets" part, create a new "Client Secret"
* Set expiration to 2 Days and click "Add"
* Store the "Value" of the new secret. This needs to be provided to Giant Swarm later.
* Add "RoleAssignment" to the newly created App

    * Select the right "Subscription" for where the management cluster (MC) should be created
    * Go to "Access control (IAM)"
    * Click "Add Role Assignment" and add the "Contributor" role and the "User Access Administrator" role to the App with the "subscription" Scope

#### Step 2 - Provide generated credentials to Giant Swarm

The following information needs to be provided to Giant Swarm using a secure transport:

* ClientID
* ClientSecret
* SubscriptionID
* TenantID

Please talk to our Account Engineer who will organize a secure, encrypted transport of your convenience. One of the possible ways is to use [Keybase](https://keybase.io/).

#### Step 3 - Post deployment cleanup

After all necessary information is provided, Giant Swarm will create the management cluster. With the provided permissions, engineers will be able to work within your subscription to automatically create and further validate the infrastructure.

As soon as all the checks from Giant Swarm as well as the customer side are done, we can clean up part of the initial setup. The _Giant Swarm Service Principal_ created in this section can be deleted as it is used only for the initial bootstrap, during which the [User Assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp) is created.

From now on this identity will be used to further manage any future or present cloud resources, hence the _Giant Swarm Service Principal_ can now be deleted.

## Further reading

* [Azure Lighthouse](https://docs.microsoft.com/en-us/azure/lighthouse/how-to/onboard-customer)
