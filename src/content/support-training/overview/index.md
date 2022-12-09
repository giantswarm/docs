---
linkTitle: Overview
title: Customer support
description: The support we provide is an essential part of our offering. Here we explain various support service processes and workflows.
weight: 10
last_review_date: 2022-12-07
user_questions:
  - What should I know when working with Giant Swarm's support staff?
  - How is Giant Swarm organizing support?
menu:
  main:
    parent: support-training
aliases:
  - /general/support
  - /basics/giant-swarm-support/
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
---


We build and run a platform which lets our customers manage as many clusters as they need with a given set of (managed) applications they decide. We ensure these clusters and applications stay in the same predictable state. This becomes especially important once you need to run multiple clusters and applications for different teams, on different environments, with different configurations or in multiple locations.

## Direct Support Slack

## Project Management

We build the platform together, since you are the best expert in your company domain we help you to build the optimal developer platform together. We have opinions but dont block you...

## Operational support

### Fully monitor platform

### Incident handling

### Postmortem process



Our customer support relies on close interactions via Slack, to ensure bi-directional feedback as quickly as possible. This is our first line of contact to customers. This interaction channel is also used to answer a variety of questions. The conversations are not limited to the platform itself, but can go broader and include the anything cloud-native.

Our support shifts run from 08:00 to 18:00 (CET) on Monday-Friday. While production support goes without saying, we  often answer questions well outside those times. We rotate support shifts across our team, which is why we focus on support channels with clear internal handovers.

If there is a problem that the first line support cannot resolve, it is handed over to an engineer who is part of the team responsible for the component or application that is failing. This is a 24 hour rotating shift.

Each customer has a dedicated Account Engineer who holds regular sync meetings to discuss customer needs and issues. This go-to person provides additional support and acts as a first backup in case the person on first line support is overloaded.

Project level work (e.g. installations) is handled by an SRE of the week. This person also serves as backup for the on-call engineer.

In short, you have three layers of support, at your fingertips. Without the hassle of help-desk tickets and rigid escalation processes.

## Operational support

The Giant Swarm platform comes with a monitoring and alerting system that helps our operations team maintain our SLAs across all customer clusters and managed applications. This is an additional aspect of the role of our on-call engineers. When on call, these engineers watch over all alerts coming in from all environments where our customers run workloads. The on-call engineers are available 24/7. Thus, ensuring that issues are handled promptly, even on nights and weekends.

The monitoring stack observes the underlying infrastructure of the platform. This includes the networking layer, DNS resolution, Kubernetes core components, cloud providers and any other targets we need to monitor to give us a complete view of the health of the system.

Today our mean time to acknowledge is around two minutes and we usually resolve incidents in less than two hours. Obviously, not all alerts result in downtime in a customer environment. As alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a dedicated email address to reach our on-call engineer 24/7.  This is for cases in which customers notice problems that have not been caught by our monitoring.

## Postmortem process

Sometimes an issue occurs that cannot be fully resolved by the support team. Meaning only a temporary fix was applied, and could potentially affect other environments or customers. Support person or on-call engineer will create a postmortem. The `postmortem` culture [was created by Google](https://sre.google/sre-book/postmortem-culture/) and was established in order to document a problem correctly, find the root cause and fix it across all installations permanently.

Postmortems are created during the whole week. On Mondays, the product team meets and distributes the postmortems across our product teams. As each team plans their weekly sprint they assign a specific engineer to each postmortem. Postmortems have priority over feature development and engineers are used to spending at least a day a week to solve these problems.

The postmortem is closed only once the underlying issue is fixed and deployed to all affected environments. Additionally postmortems often result in new or tuned alerts and ops recipes to share knowledge through the operations team.

## Conclusion

Our support process is subject to change. As we continuously improve it we discover how to improve our policies, process and tools. But the goals are clear and unchanging. We are committed to seamlessly supporting our customers.

## Further reading

- [Giant Swarm Operation Layers]({{< relref "/platform-overview/security/operational-layers" >}})
- [Giant Swarm Cluster Upgrades]({{< relref "/platform-overview/cluster-management/cluster-upgrades" >}})
- [Giant Swarm Training Catalog]({{< relref "/support-training/training-catalog" >}})
