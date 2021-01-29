---
linkTitle: Support
title: Giant Swarm support
description: An explanation of how our support service works.
weight: 50
menu:
  main:
    parent: general
last_review_date: 2020-01-20
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Giant Swarm support

We build and run a platform which lets our customers spin up as many clusters as they need. We ensure these clusters stay in the same predictable state. This becomes especially important once you need to run multiple clusters for different teams, on different environments, with different configurations or in multiple locations.

We accompany our customers throughout their cloud-native journey. Having someone to contact when problems occur is as important to us as providing a great product. Regardless of where you are in the journey. To us, it is actually the obvious complement to our product. The following is a brief description of our support process.

## Customer support

Our customer support relies on close interactions via Slack, to ensure bi-directional feedback as quickly as possible. This is our first line of contact to customers. This interaction channel is also used to answer a variety of questions. The conversations are not limited to the platform itself, but can go broader and include the anything cloud-native.

Our support shifts run from 08:00 to 18:00 (CET) on Monday-Friday. While production support goes without saying, we  often answer questions well outside those times. We rotate support shifts across our team, which is why we focus on support channels with clear internal handovers.

If there is a problem that the first line support cannot resolve, it is handed over to the Ops Duty engineer, who has deeper knowledge of the platform. This is a 24 hour rotating shift.

Each customer has a dedicated Solution Engineer who holds regular sync meetings to discuss customer needs and issues. This go-to person provides additional support and acts as a first backup in case the person on first line support is overloaded.

Project level work (e.g. installations) is handled by an SRE of the week. This person also serves as backup for the Ops Duty engineer.

In short, you have three layers of support, at your fingertips. Without the hassle of help-desk tickets and rigid escalation processes.

## Operational support

The Giant Swarm platform comes with a monitoring and alerting system that helps our operations team maintain our SLAs across all customer clusters. This is an additional aspect of the role of Ops Duty engineer. When on call, this person watches over all alerts coming in from all environments where our customers run workloads. An Ops Duty engineer is available 24/7. Thus, ensuring that issues are handled promptly, even on nights and weekends.

The monitoring stack observes the underlying infrastructure of the platform. This includes the networking layer, DNS resolution, Kubernetes core components, cloud providers and any other targets we need to monitor to give us a complete view of the health of the system.

Today our mean time to acknowledge is around two minutes and we usually resolve incidents in less than two hours. Obviously, not all alerts result in downtime in a customer environment. As alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a dedicated email address to reach our Ops Duty engineer 24/7.  This is for cases in which customers notice problems that have not been caught by our monitoring.

## Postmortem process

Sometimes an issue occurs that cannot be fully resolved by the support team. Meaning only a temporary fix was applied, and could potentially affect other environments or customers. Support person or Ops Duty engineer will create a postmortem. The `postmortem` culture [was created by Google](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/) and was established in order to document a problem correctly, find the root cause and fix it across all installations permanently.

Postmortems are created during the whole week. On Mondays, the product team meets and distributes the postmortems across our product teams. As each team plans their weekly sprint they assign a specific engineer to each postmortem. Postmortems have priority over feature development and engineers are used to spending at least a day a week to solve these problems.

The postmortem is closed only once the underlying issue is fixed and deployed to all affected environments. Additionally postmortems often result in new or tuned alerts and ops recipes to share knowledge through the operations team.

## Conclusion

Our support process is subject to change. As we continuously improve it we discover how to improve our policies, process and tools. But the goals are clear and unchanging. We are committed to seamlessly supporting our customers.

## Further reading

- [Giant Swarm Operation Layers]({{< relref "/security/operational-layers" >}})
- [Giant Swarm Cluster Upgrades](/reference/cluster-upgrades/)
