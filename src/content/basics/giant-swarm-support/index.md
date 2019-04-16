+++
title = "Giant Swarm Support"
description = "Here we explain how our support service works."
date = "2019-04-16"
type = "page"
weight = 20
categories = ["basics"]
+++

# Giant Swarm Support

Our support service is one of the key differentiators from our competency. We have built a platform which lets our customer spin clusters up as they please. But to be honest, installing a Kubernetes cluster today is not such a difficult endeavour anymore. The problems arrive in the two and three when customer run several production workloads with different requirements and configurations.

Our take is going along with the customer over the whole journey. For us, have a great platform is the same important as having someone to nudge when a problem comes. Here we will describe in a brief how our support process is defined.

## Customer Support

Our customer support relies on a close interaction channel, Slack, to get feedback from customer sort out as quick as possible. This our first contact line to the customer. Customer engineers usually ask question all types, not only problem with the platform itself but any question related to Cloud Native ecosystem. 

Our customer shifts go from 8:00 a.m. to 6 p.m. in weekly days, but as we have colleagues working around the world questions coming out of business hours are sort out most of the times.

Once there is a problem that the first line support cannot resolve, it is handed over the `ops duty` engineer who has a deeper knowledge of the platform. At the same time there is an SRE every week to assist the support team in case something goes wrong (luckily it only happens on rare occassions).

## Operation Support

Giant Swarm platform comes with a monitoring and alert system that helps our operation team to maintain our SLAs on shape through all customer clusters. Together there is on-call engineer every day watching over all alerts come from all different environments where our customers run their workloads. The operation shift last 24 hours/7 days per week, so we ensure nothing happen even errors come during night or weekends.

The monitoring stack observes the underlying infrastructure of the platform, the networking layer, DNS resolution, Kubernetes main components and another set of targets that gives us a complete view of the health of the system.

Today our mean acknowledge average is around two minutes and we usually resolved the incidents in less than two hours. Obviously, it does not mean all the alerts triggered mean downtime in customer environment as alert could cover from storage problems to overload nodes.

## Postmortem process

When appears an issue that cannot be resolved by the support team and it could potentially affect other environments or customer, the person on support creates a postmortem. The `postmortem` culture [was created by Google](https://landing.google.com/sre/sre-book/chapters/postmortem-culture/), in order to document the problem correctly and find lately a proven solution for the root cause. 

The postmortems could be created during the whole week but on Mondays, the product team meets and distribute the postmortems through the teams. Afterwards, each team plans the week sprint and assign the person who will work on the postmortem. The postmortem has priority over the feature development and engineer used to arrange at least a day to work on it.

The postmortem is closed once the back issue is fixed and deployed to all affected environments. But most of the times a postmortem comes with a new or tuned alert and ops recipe to share the knowledge through the operation team.

# Conclusion

Our support process is subject to change as we exercise it and discover how to improve or policies the process and the tools, but the goals are clear and we are committed to serving a seamlessly support to our customers.

## Further reading

- [Giant Swarm Operation Layers](https://docs.giantswarm.io/guides/giant-swarm-operation-layers/)
- [Giant Swarm Cluster Upgrades](https://docs.giantswarm.io/reference/cluster-upgrades/)