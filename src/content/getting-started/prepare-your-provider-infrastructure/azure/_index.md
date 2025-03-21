---
title: Prepare your provider account for Azure
linkTitle: Azure
description: Prepare your Azure account to start building your cloud-native developer platform with Giant Swarm.
weight: 20
last_review_date: 2024-11-28
layout: single
menu:
  principal:
    parent: getting-started-prepare-provider-infrastructure
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How do I prepare my Azure account for the cloud-native developer platform?
  - How must I prepare my Azure account for the cloud-native developer platform?
aliases:
  - /getting-started/cloud-provider-accounts/cluster-api/azure
  - /vintage/getting-started/cloud-provider-accounts/cluster-api/azure
---

When running the Giant Swarm platform in your Azure subscription, several prerequisites must be satisfied to support Cluster API Provider Azure (CAPZ). In the current implementation, management and workload clusters must run in the same subscription.

In addition to the following prerequisites, your account engineer will provide you with a pre-installation checklist that you must complete before starting the installation process.

## Requirements

1. The Azure subscription must be chosen from existing ones or created if needed in the customer's Azure account. For security reasons regarding sensitive data stored within customer accounts, the advice is to use a subscription-only designated for Giant Swarm Azure resources management.

2. An individual has to have the following permissions and tools working within the designated Azure subscription:

    * An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
    * [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured to point to chosen subscription via [`az account set`](https://learn.microsoft.com/en-us/cli/azure/account?view=azure-cli-latest#az-account-set) command.

## Step 1: Service quotas {#quotas}

Azure enforces [service quota through all cloud services](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits). The following overview lists the usual resources you may adjust, depending on the number and size of clusters planned to be deployed:

![Azure quotas list](./quotas_general.png)

Access to the [Quotas portal service](https://portal.azure.com/#view/Microsoft_Azure_Capacity/QuotaMenuBlade/~/myQuotas) to check and adjust quotas as required. You can also use the Azure CLI to check quotas like:

```sh
az vm list-usage --location <region>
```

If your current quotas are insufficient, you can request an increase. In the Azure portal, follow the steps below:

1. Go to the **Quotas** section in the [Azure portal](https://portal.azure.com/#view/Microsoft_Azure_Capacity/QuotaMenuBlade/~/myQuotas).
2. Click on the pencil button to **request an update**.
3. Fill the new limit and submit the request.

![Azure quotas edit](quota_editing.png)

You can follow the request status in the **Quotas** section.

## Step 2: Permissions

Two permission roles need to be created in the Azure subscription: one for the Giant Swarm controller used by the CAPZ controller in the management cluster to provision all infrastructure to manage workload clusters and the other for Giant Swarm engineers to access the Azure account for support purposes.

### Staff permissions {#iam-staff-role}

Firstly, you need to grant access to Giant Swarm ops/support to your Azure subscription. Access to the portal is essential for our everyday support, where investigation and manual interventions are sometimes necessary.

The easiest way is to create an [Azure Deployment Environment](https://azure.microsoft.com/en-us/products/deployment-environments) to delegate resource management to third parties. In this case, you must allow the `Giant Swarm Staff` group to manage your resources. This is beneficial as you don't have to manage access for each person separately within your subscription, instead you add a managed group that's kept up to date by Giant Swarm. There is a solution available called [Azure Lighthouse](https://learn.microsoft.com/en-us/azure/lighthouse/overview), which allows resource management to be delegated to service providers such as Giant Swarm.

The recommendation is to choose Azure's [built-in role `Contributor`](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles) to give Giant Swarm access and deployment permissions for resources within your subscription.

Alternatively, you can create your role assignment with restricted access to specific Resource Groups. However, it must be kept up to date so that Giant Swarm can also provide full support for newly created clusters.

#### Create a Deployment Environment

* Download the template file [delegatedResourceManagement](https://raw.githubusercontent.com/giantswarm/azure-operator/master/docs/delegatedResourceManagement.json). This file is left unchanged.
* Download the parameters example file [delegatedResourceManagement.parameters](https://raw.githubusercontent.com/giantswarm/azure-operator/master/docs/delegatedResourceManagement.parameters.json) and fill in the required fields:

    * Replace `<GiantSwarmTenantID>` and `<GiantSwarmPrincipalID>` with the values provided by Giant Swarm's Account Engineer
    * Keep the value of `roleDefinitionId` if you are fine assigning the `Contributor` role. If a custom role is desired, please replace the value.

* Now you can run this command to create the Deployment Environment:

    ```sh
    $ az deployment create --name "giantswarm-access" \
                          --location <AzureRegion> \
                          --template-file delegatedResourceManagement.json \
                          --parameters delegatedResourceManagement.parameters.json \
                          --verbose
    ```

    The `--name` value can be freely chosen if you prefer another name.

### Controller permissions {#iam-azure-operator-role}

On the other hand, the automation requires an [Azure Service Principal](https://learn.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals?tabs=browser#service-principal-object), let's call it `Giant Swarm Service Principal`, to enable CAPZ controller to control the Azure resources.

#### Create the service principal

The _Giant Swarm Service Principal_ can be created in two different ways: via the `az` CLI or the Azure portal.

##### Using the Azure CLI

Please run the following command and keep the output for later usage.

```text
# Please fill in the details of the management cluster (MC) and Azure subscription
MC_SUBSCRIPTION_ID=XXXX-XXXX-XXXX-XXX
MC_NAME=ZZZZ

az login
az account set -s ${MC_SUBSCRIPTION_ID}
az ad sp create-for-rbac --role contributor --scopes="/subscriptions/${MC_SUBSCRIPTION_ID}" --display-name "${MC_NAME}-bootstrap"
az role assignment create \
    --assignee "<please fill in the app ID from the previous command output>" \
    --role "User Access Administrator" \
    --scope "/subscriptions/${MC_SUBSCRIPTION_ID}"
```

**Note**: Store the output of `az ad sp create-for-rbac`. This needs to be provided to Giant Swarm in step 2.

##### Using Azure Portal

* Login to the [Azure Portal](https://portal.azure.com/)
* Go to the "Azure Active Directory" service
* From the left pane, select the "App registrations" section, then click "New registration" from the menu at the top of the page
* Enter the name `<MC_NAME>-bootstrap`. Replace `<MC_NAME>` with the name of the management cluster
* Select "Accounts in any organizational directory (Any Azure AD directory - Multi-tenant)" as "Supported account types"
* Click "Register"
* Go to the "Certificates & secrets" section. Under the "Client secrets" part, create a new "Client Secret"
* Set expiration to `2 Days` and click "Add"
* Store the new secret's `Value`. Later, this needs to be provided to Giant Swarm.
* Add "RoleAssignment" to the newly created App

    * Select the right "Subscription" where the management cluster should be created
    * Go to "Access control (IAM)"
    * Click "Add Role Assignment" and add the "Contributor" role and the "User Access Administrator" role to the App with the "subscription" Scope

#### Provide generated credentials to Giant Swarm

The following information needs to be provided to Giant Swarm:

```text
* ClientID
* ClientSecret
* SubscriptionID
* TenantID
```

**Note**: Contact your Account Engineer, who will help you find a secure way to share this information. Our recommended tool is [Keybase](https://keybase.io/).

#### Post deployment cleanup

Once all necessary information is provided, our engineers create the management cluster. The provided permissions work within your subscription to provision and validate the infrastructure, ensuring a seamless and efficient process.

When Giant Swarm completes the management cluster provisioning, our engineers can clean up part of the initial setup. The _Giant Swarm Service Principal_ can be deleted as it's used only for the initial bootstrap, during which an [Azure user-assigned managed identity](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/how-manage-user-assigned-managed-identities?pivots=identity-mi-methods-azp) is created.

## Step 3: Virtual machine templates

### Accept legal terms for Flatcar Linux

Giant Swarm deploys [Flatcar Linux](https://www.flatcar-linux.org/) images for Kubernetes cluster nodes. It's developed by Kinvolk and taken from the Azure Marketplace. In order to be able to run the images, Azure requires customers to accept the legal terms.

Please run the following command before creating a cluster on a given subscription:

```sh
az vm image terms accept --offer flatcar-container-linux-free --plan stable --publisher kinvolk
```

**Note**: This acceptance needs to be performed only once for a subscription that's used to run Giant Swarm workload clusters.

### Enable encryption at host

If your security requirements demand this, you can enable [encryption of data stored on virtual machine hosts](https://learn.microsoft.com/en-us/azure/virtual-machines/linux/disks-enable-host-based-encryption-cli). With this enabled, your data will be encrypted when stored and transferred between storage and host, adding additional protection from unauthorized access.

Please run the following command before creating a cluster on a given subscription:

```sh
az feature register --name EncryptionAtHost  --namespace Microsoft.Compute --subscription $YOUR_SUBSCRIPTION_ID
```

## Step 4: Configure the cluster role identity {#configure-cluster-role-identity}

The last step involves storing the Azure credentials in the platform to allow the CAPZ controller to manage the infrastructure in your account. In Cluster API, there is a custom resource called `AzureClusterIdentity` that stores the Azure credentials. This resource is namespaced.

By default, the controller uses a `default` configuration, which points to the role in the management cluster account. If you want to create a new workload cluster in a new Azure subscription, you need to create a new `AzureClusterIdentity` resource that references the role of that Azure subscription. Example:

```yaml
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureClusterIdentity
metadata:
  labels:
    cluster.x-k8s.io/watch-filter: capi
  name: <SUBSCRIPTION_NAME>
spec:
  type: WorkloadIdentity
  tenantID: <TENANT_ID>
  clientID: <CLIENT_ID>
```

The `<SUBSCRIPTION_NAME>` is a short unique name referencing Azure subscription (`development`, `sandbox` or `staging2`). We advocate using the same name as the [organization]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/organizations" >}}) to help map the resources and the accounts. The `<TENANT_ID>` and `<CLIENT_ID>` is the Azure client ID and tenant ID that represent the subscription where the workload cluster will be provisioned.

**Note**: The [official documentation](https://capz.sigs.k8s.io/topics/workload-identity) provides more information about configuring Azure credentials.

In the [next step]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}) you define which role the `AzureCluster` uses to provision the cluster adjusting the value `providerSpecific.azureClusterIdentity.name`.

**Note**: If you are working with a Giant Swarm partner, you might not have access to the platform API. Please provide the credentials, CAPZ controller, and staff to your partner contact.

## Next steps

Contact your Giant Swarm account engineer to verify the setup and proceed with the management cluster provisioning. For sharing any secret with us please read [this article]({{< relref "/overview/security/sharing-secrets" >}}) first. In case you have already set up the management cluster and you have just configured a new Azure subscription, you can proceed with the [creation of the workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).
