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
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-11-26
---

A Giant Swarm installation is the management cluster where all our platform components run. It's attached to a cloud provider account and region, or an on-premise data center, and it's the central point and API to use the platform capabilities.

## Why an installation name

Every Giant Swarm installation has an unique name. This name is part of the DNS zone used for all endpoints of the central platform.

When setting up a new installation for you, a name is needed. Think of this name as your handy alias for everything you do with Giant Swarm in a specific infrastructure provider region, for example _Google Cloud Finland (europe-north1)_.

Once a name is decided on, you will use it often in your communication with Giant Swarm. Of course, you can also use it in your internal communication.

## Criteria for good installation names

Besides being usable in DNS, there are many criteria which distinguish a good installation name. It should be easy to pronounce in an English language context, easy to type, and ideally easy to memorize. On the other hand, it shouldn't reveal information about you as a customer.

The installation name can't be changed. So the best names are long-lasting, even in the case of context changes. Be aware you can change the purpose of the installation, or even a company name change.

There is a GitHub repository with [installation name candidates](https://github.com/giantswarm/installation-names) available for you to pick from. The names offered there should fulfill all of our criteria for a name.

## How to claim a name

To claim a name for your new installation, please

1. Browse the available names in the `.txt` files within the [installation-names](https://github.com/giantswarm/installation-names) repository and decide on a name. Feel free to pick the one you like best, for whatever reason.
2. Fork the repository.
3. In your fork, remove the name you decided for.
4. Provide a pull request to our source repository. Please inform your Giant Swarm account engineer or site reliability engineer about the pull request.

A Giant Swarm staff member will eventually merge your pull request and thus remove your claimed name from the repository.
