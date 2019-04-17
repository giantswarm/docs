+++
title = "Giant Swarm Support"
description = "An explanation of how our support service works."
date = "2019-04-16"
type = "page"
weight = 20
categories = ["basics"]
+++

# Giant Swarm Support

Our support service is one of the key differentiators from our competitors. We have built a platform which lets our customer spin up as many clusters as they need. These clusters are then always in the same predictable state. This becomes especially valuable once you need to run multiple clusters for different teams, environments, configurations or in multiple locations.

We are always at the side of our customers during their whole journey. For us, having a great platform is as important as having someone to contact when problems occur. The following is a brief description of our support process.

## Customer Support

Our customer support relies on close interactions via Slack, to get bi-directional feedback as quickly as possible. This is our first line of contact to customers, who can ask all kinds of questions, not only in relations to the platform itself, but many more around their whole Cloud Native journey.

Our support shifts go from 08:00 to 18:00 on weekdays, but we also often answer questions well outside those times. We have a rotating shift for support across the team, which is why we keep support focused on those channels with clear internal handovers.

If there is a problem that the first line support cannot resolve, it is handed over to the `ops duty` engineer, again a rotating 24 hour shift, who has deeper knowledge of the platform.

Additionally, each customer has a dedicated Solution Engineer as additional support and a first backup in case the person on first line support is overloaded, and for regular sync meetings. On top of that we also have an SRE of the week who handles project level work (e.g. installations) and is the backup for the Ops Duty engineer. 

## Operational Support

The Giant Swarm platform comes with a monitoring and alert system that helps our operations team to maintain our SLAs through all customer clusters. This is the second duty for the ops duty engineer on call every day watching over all alerts coming in from all environments where our customers run their workloads. The Ops Duty shift is 24/7, so we ensure issues are handled even when they occur during the night or at weekends.

The monitoring stack observes the underlying infrastructure of the platform, the networking layer, DNS resolution, Kubernetes core components, cloud providers and any other targets we need to monitor to give us a complete view of the health of the system.

Today our mean time to acknowledge is around two minutes and we usually resolve incidents in less than two hours. Obviously, it does not mean all alerts result in downtime in a customer environment. As alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a special email address to reach our ops duty engineer 24/7.  In case they notice problems that have not been caught by our monitoring.

## Postmortem process

Sometimes an issue occurs that cannot be fully resolved by the support team. Meaning only a temporary fix was applied, and could potentially affect other environments or customers. The support or ops duty engineer will create a postmortem. The `postmortem` culture [was created by Google](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/) and was established in order to document the problem correctly, find the root cause and fix it across all installations permanently.

The postmortems are created during the whole week. On Mondays, the product team meets and distributes the postmortems through the teams. Afterwards, each team plans their weekly sprint and assigns the person who will work on the postmortem. The postmortem has priority over feature development and engineers are used to spending at least a day a week to work on these problems.

The postmortem is closed once the underlying issue is fixed and deployed to all affected environments. Additionally postmortems often result in new or tuned alerts and ops recipes to share knowledge through the operations team.

# Conclusion

Our support process is subject to change. As we continuously improve it as we discover how to improve our policies, process and tools, but the goals are clear and we are committed to seamlessly supporting our customers.

## Further reading

- [Giant Swarm Operation Layers](https://docs.giantswarm.io/basics/giant-swarm-operational-layers/)
- [Giant Swarm Cluster Upgrades](https://docs.giantswarm.io/reference/cluster-upgrades/)
