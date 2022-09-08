---
linkTitle: Shared installations
title: Getting started on a shared installation
description: Giant Swarm customers usually work with their own installation(s). However, we also provide shared installations for trials and proof of concept (PoC) projects. This article explains the differences and what to do as a customer to get started on a shared installation.
weight: 10
menu:
  main:
    parent: getting-started
user_questions:
  - How is a shared installation different from normal Giant Swarm installations?
  - What do I have to do to use a shared installation?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2021-07-15
---

Giant Swarm customers usually work with their own installation(s). However, we also provide shared installations for trials and proof of concept (PoC) projects. This article explains the differences and what to do as a customer to get started on a shared installation.

## Differences

### Cloud provider account

**Note:** Shared installations are available both on AWS and Azure. While we use the term _account_ here for the sake of simplicity, on Azure the according concept is called a _subscription_.

A Giant Swarm installation normally is used by only one customer. Both management cluster and workload clusters run in cloud provider account owned by the customer.

In a shared installation, the management cluster runs in an account owned by Giant Swarm. The workload clusters however are created using the customer's account.

Find instructions regarding the setup below.

### Organizations

In a normal Giant Swarm installation, [organizations]({{< relref "/general/organizations" >}}) are used to isolate different concerns, teams, business units from each other. Admin users can create as many organizations as they need and use the organization's namespace in the management clusters and role-based access control (RBAC) to control access to these resources.

In a shared installation, each customer is mapped to exactly one organization. You cannot create additional organizations.

### Access control

For normal Giant Swarm installations, the customer can decide which identity provider to use for [authentication]({{< relref "/ui-api/management-api/authentication" >}}) to the Management API.

In a shared installation, all customers use GitHub as an identity provider and configure a team in a Github organization to include all the users who need access to the Giant Swarm Management API and user interfaces. Find instructions regarding the setup of your organization and team below.

### Monitoring

A shared installation is monitored and managed by Giant Swarm staff, just like any other installation. However, we currently do not provide access to our [Monitoring]({{< relref "/ui-api/monitoring" >}}) for users of a shared installation.

## Getting started

### Kick-off

We talked. Together, you and Giant Swarm agree on a project. You have an Account Engineer at Giant Swarm responsible for you.

### Pick an organization name

It's up to you to decide for an organization name that represents you as a company, business unit, or team. Please take our [naming conventions]({{< relref "/general/organizations#naming-conventions" >}}) into account.

### Prepare a cloud provider account

To create and manage workload clusters on your behalf, we ask you to prepare some configuration, roles, and quotas in your cloud provider account.

We provide detailed guides both for [AWS]({{< relref "/getting-started/cloud-provider-accounts/aws" >}}) and [Azure]({{< relref "/getting-started/cloud-provider-accounts/azure" >}}). Note that we **only need an account for the workload clusters**, but not for a management cluster in the case of a shared installation.

When done, hand the account information to your Account Engineer at Giant Swarm.

### Create your GitHub team

For access management, a shared installation uses GitHub as an identity provider. All members who need access to Giant Swarm resources, via the Management API or the user interfaces, must be a member of the same GitHub team.

To create a team, follow these steps:

1. Log in at [GitHub](https://github.com/).
2. If a GitHub organization does not yet exist:
    - Click the `+` link in the top right.
    - Select `New organization`.
    - Fill in the name and additional details
3. Go to the organization's teams list at `https://github.com/orgs/<org-name>/teams`.
4. Select a team, or create a new one.
5. Make sure the team has the expected members at `https://github.com/orgs/<org-name>/teams/<team-name>/members`.
6. Copy the details URL of the team, like `https://github.com/orgs/<org-name>/teams/<team-name>`, and hand it to your Account Engineer at Giant Swarm.

### Let us take care of the rest

Once you have gone through the steps outlined above, let us set up your organization in the selected shared installation. We'll let you know when you can access our web user interface and start your first clusters.
