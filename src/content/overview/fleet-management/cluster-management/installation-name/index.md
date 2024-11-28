---
linkTitle: Installation names
title: Picking an installation name
description: Every Giant Swarm installation has a unique name. Learn the rules to select a proper name for a new installation.
weight: 100
menu:
  principal:
    parent: overview-fleet-management-clusters
    identifier: overview-fleet-management-clusters-installation-name
user_questions:
  - How do I determine the name for my Giant Swarm installation / management cluster?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2024-11-28
---

A Giant Swarm installation is the management cluster where all our platform components run. It's attached to a cloud provider account and region, or an on-premise data center, and it's the central point and API to use the platform capabilities.

## Why an installation name

Once a name is decided on, you will use it often in your communication with Giant Swarm. Of course, you can
also use it in your internal communication.

For example, if the installation is called `panda`, it's easy to refer to a concrete workload cluster called `prod-eu1` as follows in chat:

> Dear Giant Swarm support, we see this problem on panda/prod-eu1 

## Criteria for good installation names

There are many criteria which distinguish a good installation name. It should be easy to pronounce in an English language context, easy to type, and ideally easy to memorize. On the other hand, it shouldn't reveal information about you as a customer.

The installation name can't be changed. So the best names are long-lasting, even in the case of context changes. Be aware you can change the purpose of the installation, or even a company name change.

There is a GitHub repository with [installation name candidates](https://github.com/giantswarm/installation-names) available for you to pick from. The names offered there should fulfill all of our criteria for a name.

## How to claim a name

To claim a name for your new installation, please

1. Browse the available names in the `.txt` files within the [installation-names](https://github.com/giantswarm/installation-names) repository and decide on a name. Feel free to pick the one you like best, for whatever reason.
2. Contact Giant Swarm support to ensure the name is still available and our team will reserve it for you.
3. Our team will remove the name from the list in the repository.
