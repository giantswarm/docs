---
title: Continuous deployment
description: Continuous deployment and GitOps capabilities for deploying and upgrading your applications and clusters efficiently.
weight: 50
menu:
  principal:
    parent: overview
    identifier: overview-continuous-delivery
last_review_date: 2024-04-18
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Outline suggested
```

```

Can anyone help me understand why would i do the transition in deploying our microservices with flux too?

pull vs push 
- Reducing costs
- Scale across clusters without limitations
- Improving security (you do not need to manage keys for all targets in a single location)
IAC
- Define all reqs together within your app (separate concerns, platform team vs dev)


<!-- AUDIENCE: HIGH LEVEL, like a C-level person intro -->

Check first the template (https://github.com/giantswarm/docs/pull/2180/files) it is still in development and your feedback is welcome, but you can take it as a reference.

Concepts come to my mind when I think of continuous delivery (worthy to mention here without going deep):

- GitOps (declarative approach)
- Pull versus push
- You can define apps but also configuration or infrastructure too
- Automation always helps (templating we offer)
- secret mgmt


The main idea is to write a brief description of continuous delivery in general from an introductory point of view setting the high-level goals we would like to achieve.

## Features

Describe what use cases are covered by our continuous delivery features.

## Cloud-native technologies

- What technologies are used to provide cd successfully? (Flux, ESO, ...)
