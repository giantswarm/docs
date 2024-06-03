---
title: Prepare your provider account for Azure
linkTitle: Prepare your Azure account
description: Prepare your Azure account to start building your cloud-native developer platform with Giant Swarm.
weight: 20
last_review_date: 2024-05-28
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I prepare my Azure account for the cloud-native developer platform?
  - What do I need to do to prepare my Azure account for the cloud-native developer platform?
---

When running the Giant Swarm platform in your Azure subscription, several prerequisites must be satisfied to support Cluster API Provider for Azure (CAPZ). In the current implementation, management and workload clusters must run in the same subscription.

In addition to the following prerequisites, your account engineer will provide you with a pre-installation checklist that you must complete before starting the installation process.

## Requirements

1. The Azure subscription must be chosen from existing ones or created if needed in the customer's Azure account. For security reasons regarding sensitive data stored within customer accounts, the advice is to use a subscription-only designated for Giant Swarm Azure resources management.

2. An individual has to have the following permissions and tools working within the designated Azure subscription:

* An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
* [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured to point to chosen subscription via [az account set](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-set) command.

### Service quotas {#quotas}

Azure enforces [service quota through all the cloud services](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits). The following overview lists the usual resources you may adjust depending on number of clusters and their size planned to be deployed:

Access to the [Quotas portal service](https://portal.azure.com/#view/Microsoft_Azure_Capacity/QuotaMenuBlade/~/myQuotas) to check and adjust quotas as required. You can also use the Azure CLI to check quotas like:

```sh
az vm list-usage --location <region>
```

If your current quotas are insufficient, you can request an increase. In the portal, there is no cli command, follow the steps below:

* Go to the **Quotas** section in the [Azure portal](https://portal.azure.com/#view/Microsoft_Azure_Capacity/QuotaMenuBlade/~/myQuotas).
* Click on pencil button to **request an adjustement**.
* Fill the new limit and submit the request.

You can follow the request status in the **Quotas** section.

### Permissions

#### Controller permissions {#iam-azure-operator-role}


### Staff permissions {#iam-staff-role}







