---
linkTitle: Installation names
title: Picking an installation name
description: Every Giant Swarm installation has a unique name. Learn here how to select a name for your new installation.
weight: 10
menu:
  main:
    parent: getting-started
user_questions:
  - How do I determine the name for my Giant Swarm installation?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
last_review_date: 2022-09-08
---

A Giant Swarm installation includes a Management Cluster, bastion hosts, the workload clusters (depending on your viewpoint) and a few more components specific to the cloud provider used.

## Why an installation name

Every Giant Swarm installation has a unique name. This name is part of the DNS zone used for all endpoints of this installation.

When we set up a new installation for you, we want you to pick a name for it. Think of this name as your handy alias for everything you do with Giant Swarm in a specific cloud provider region, e.g. _Google Cloud Finland (europe-north1)_.

Once a name is decided on, you will use it often in your communication with Giant Swarm. Of course, we encourage you to also use it in internal communication.

## Criteria for good installation names

Besides being usable in DNS, there are many criteria which distinguish a good installation name. It should be easy to pronounce in an English language context, easy to type, and ideally easy to memorize. On the other hand, it should not reveal information about you as a customer.

Installation names cannot be changed. So the best names are long-lasting, even in the case of context changes. For example, changing the purpose of the installation, or even a company name change.

We provide a GitHub repository with [installation name candidates](https://github.com/giantswarm/installation-names) available for you to pick from. The names offered there should fulfill all of our criteria for a name.

## How to select a name

To select a name for your new installation, please

1. Browse the available names in the `.txt` files within the [installation-names](https://github.com/giantswarm/installation-names) repository and decide on a name. Feel free to pick the one you like best, for whatever reason.
2. Fork the repository.
3. In your fork, remove the name you decided for.
4. Provide a pull request to our source repository. Please inform your Giant Swarm account engineer (AE) or site reliability engineer (SRE) about the pull request.

A Giant Swarm staff member will eventually merge your pull request and thus remove your claimed name from the repository.
