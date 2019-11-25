+++
title = "Giant Swarm Support"
description = "An explanation of how our support service works."
date = "2019-11-24"
type = "page"
weight = 20
categories = ["basics"]
+++

# Giant Swarm Support

We built and run a platform which lets our customers spin up as many clusters as they need. We always keep these clusters in the same predictable state. This becomes especially valuable once you need to run multiple clusters for different teams, on different environments, with different configurations or in multiple locations.

We accompany our customers throughout their journey. Having someone to contact when problems occur is as important to us as providing a great product. It is actually the obvious complement to our product. The following is a brief description of our support process.

## Customer Support

Our customer support relies on close interactions via Slack, to get bi-directional feedback as quickly as possible. This is our first line of contact to customers. This interaction channel is also used to ask all kinds of questions. The conversations are not limited to the platform itself, but can go broader and include the whole Cloud Native journey.

Our support shifts go from 08:00 to 18:00 on weekdays, but we also often answer questions well outside those times. We rotate support shifts across the team, which is why focus on support channels with clear internal handovers.

If there is a problem that the first line support cannot resolve, it is handed over to the `ops duty` engineer, who has deeper knowledge of the platform. This is a 24 hour rotating shift.

Each customer has a dedicated Solution Engineer who provides additional support and acts as a first backup in case the person on first line support is overloaded. Solution Engineers also hold regular sync meetings to discuss customer needs and issue.

Project level work (e.g. installations) is handled by an SRE of the week. This person also serves as backup for the Ops Duty engineer. 

## Operational Support

The Giant Swarm platform comes with a monitoring and alert system that helps our operations team to maintain our SLAs across all customer clusters. This is an additional aspect of the role of ops duty engineer. When on call, this person watches over all alerts coming in from all environments where our customers run workloads. An Ops Duty engineer is available 24/7. Thus, ensuring that issues are handled promptly, even on nights and weekends.

The monitoring stack observes the underlying infrastructure of the platform, the networking layer, DNS resolution, Kubernetes core components, cloud providers and any other targets we need to monitor to give us a complete view of the health of the system.

Today our mean time to acknowledge is around two minutes and we usually resolve incidents in less than two hours. Obviously, not all alerts result in downtime in a customer environment. As alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a dedicated email address to reach our ops duty engineer 24/7.  This is for cases in which customers notice problems that have not been caught by our monitoring.

## Postmortem process

Sometimes an issue occurs that cannot be fully resolved by the support team. Meaning only a temporary fix was applied, and could potentially affect other environments or customers. The support or ops duty engineer will create a postmortem. The `postmortem` culture [was created by Google](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/) and was established in order to document a problem correctly, find the root cause and fix it across all installations permanently.

Postmortems are created during the whole week. On Mondays, the product team meets and distributes the postmortems across teams. Afterwards, each team plans their weekly sprint and assigns the person who will work on each postmortem. Postmortems have priority over feature development and engineers are used to spending at least a day a week to work on these problems.

The postmortem is closed once the underlying issue is fixed and deployed to all affected environments. Additionally postmortems often result in new or tuned alerts and ops recipes to share knowledge through the operations team.

# Conclusion

Our support process is subject to change. As we continuously improve it as we discover how to improve our policies, process and tools, but the goals are clear and we are committed to seamlessly supporting our customers.

## Further reading

- [Giant Swarm Operation Layers](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/)
- [Giant Swarm Cluster Upgrades](https://docs.giantswarm.io/reference/cluster-upgrades/)
