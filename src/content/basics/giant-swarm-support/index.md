+++
title = "Giant Swarm Support"
description = "Here we explain how our support service works."
date = "2019-04-16"
type = "page"
weight = 20
categories = ["basics"]
+++

# Giant Swarm Support

Our support service is one of the key differentiators from our competency. We have built a platform which lets our customer spin clusters up as they please. These clusters are then always in the same predictable state and becomes especially valuable once you need to run multiple clusters for different teams, different stages, different configurations or in different locations.

We are alwas at the side of our customer over the whole journey. For us, having a great platform is as important as having someone to nudge when problems occur. Following a brief description of our support process.

## Customer Support

Our customer support relies on close interactions via Slack, to get bi-directional feedback as quickly as possible. This our first contact line to customers, who can ask all kinds of questions, not only in relations to the platform itself, but many more around the Cloud Native journey.

Our support shifts go from 8:00 a.m. to 6 p.m. on weekdays, but often answer questions well out of those times. We have a rotating shift for support across the team, which is why we keep support focussed on those channels with clear internal handovers.

Once there is a problem that the first line support cannot resolve, it is handed over the `ops duty` engineer, again a rotating 24 hour shift, who has a deeper knowledge of the platform.

Additionally, each customer has a dedicated solution engineer as additional support and first fall back in case the person on first line support is overloaded, and for regular sync meetings. On top of that we have an SRE of the week that handles project level work (e.g. installations) and is the fall back for the ops duty engineer. 

## Operation Support

Giant Swarm platform comes with a monitoring and alert system that helps our operation team to maintain our SLAs through all customer clusters. This is the second duty for the ops duty engineer on call every day watching over all alerts coming from all different environments where our customers run their workloads. The operation shift last 24 hours/7 days per week, so we ensure nothing happens even when errors come up during night or weekends.

The monitoring stack observes the underlying infrastructure of the platform, the networking layer, DNS resolution, Kubernetes main components and another set of targets that gives us a complete view of the health of the system.

Today our mean acknowledge average is around two minutes and we usually resolved the incidents in less than two hours. Obviously, it does not mean all the alerts result in a downtime in customer environment as alerts are set to make sure we fix problems before they lead to real incidents.

Additionally, customers have a special email to reach our ops duty engineer 24/7 in case the notice problems that have not been caught by our monitoring.

## Postmortem process

When an issue appears that cannot be fully resolved by the support team, meaning only a temporary fix was applied, and could potentially affect other environments or customer, the support or ops duty engineer creates a postmortem. The `postmortem` culture [was created by Google](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/) was established in order to document the problem correctly, find the root cause and fix it across all installations permanently.

The postmortems are created during the whole week. On Mondays, the product team meets and distribute the postmortems through the teams. Afterwards, each team plans the week sprint and assign the person who will work on the postmortem. The postmortem has priority over the feature development and engineer used to arrange at least a day to work on it.

The postmortem is closed once the underlying issue is fixed and deployed to all affected environments. Additionally a postmortem comes with a new or tuned alert and ops recipe to share the knowledge through the operation team.

# Conclusion

Our support process is subject to change as we exercise it and discover how to improve or policies the process and the tools, but the goals are clear and we are committed to serving a seamlessly support to our customers.

## Further reading

- [Giant Swarm Operation Layers](https://docs.giantswarm.io/guides/giant-swarm-operation-layers/)
- [Giant Swarm Cluster Upgrades](https://docs.giantswarm.io/reference/cluster-upgrades/)
