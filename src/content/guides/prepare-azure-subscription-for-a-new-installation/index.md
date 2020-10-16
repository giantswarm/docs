---
title: "Prepare an Azure subscription to run a Giant Swarm installation"
description: "This guide will walk you through all necessary steps to set up an Azure subscription to run a Giant Swarm installation."
date: "2020-10-14"
type: page
weight: 100
tags: ["tutorial"]
---

# Prepare an Azure subscription to run a Giant Swarm intallation

In a Giant Swarm installation the software managing tenant clusters (the kubernetes clusters that run your workloads)
is installed in a separate Kubernetes cluster, called `control plane`.

This document will guide you through the setup process for your Azure Subscription to make it possibile to install, operate and upgrade
the Giant Swarm's control plane.

## Overview

In order to run a Giant Swarm control plane, you will need:

- to invite Giant Swarm's service principal to the Active Directory your `Subscription` belongs to;
- to assign Giant Swarm's service principal the `Owner` role in the `Subscription`.

## Procedure

The process of enabling a service principal involves 3 steps, described below.

### 1. Prerequisites

To create and assign the role to Giant Swarm's Service Principal you need:

- An account with [Owner](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#owner) or [User Access Administrator](https://docs.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#user-access-administrator) role.
- [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli) installed.

### 2. Invite Giant Swarm's service principal to your Active Directory. 

By visiting the following link you can invite GiantSwarm's Service Principal and authorize it to the Tenant AD on behalf 
of your organization. You just need to replace `${TENANT_ID}` with your Tenant ID, and `${SERVICE_PRINCIPAL_ID}` with the 
Service Principal ID provided by Giant Swarm.

```nohighlight
https://login.microsoftonline.com/${TENANT_ID}/oauth2/authorize?client_id=${SERVICE_PRINCIPAL_ID}&response_type=code&redirect_uri=https%3A%2F%2Fwww.microsoft.com%2F
```

Please note that the above URL will forward you to the `microsoft.com` home page on success. This is intended.

### 3. Assign the owner role to the Giant Swarm service principal.

Now you need to give Giant Swarm's Service Principal permission to access resources belonging to your subscription. 
In your subscription, go to "Access Control (IAM)" and click the "Add Role" button, then select "Add role assignment".
In the right sidebar that pops up, please select the `Owner` role.
