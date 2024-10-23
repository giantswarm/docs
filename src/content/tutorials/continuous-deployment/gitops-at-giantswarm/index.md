---
linkTitle: At Giant Swarm
title: GitOps at Giant Swarm
description: A brief explanation of how Giant Swarm supports the GitOps journey for our customers.
weight: 10
menu:
  principal:
    parent: tutorials-continuous-deployment
    identifier: tutorials-continuous-deployment-gitops
user_questions:
  - GitOps at Giant Swarm?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2024-10-22
---

One of the goals at Giant Swarm is to ensure you have a successful GitOps journey.

To achieve this, our team run presentations and workshops with you to help get you started. Moreover, we offer an [opinionated template](https://github.com/giantswarm/gitops-template) crafted around our environments, and additional tooling to generate and validate your resource manifests before they are applied.

The goal is for you to have complete ownership of the resources applied to your clusters. To ensure this, our engineers generally have no visibility of your source manifests or configuration. These will always remain your responsibility to create and manage.

Giant Swarm is committed to your success and understands that tracing issues with the process can sometimes be challenging. To assist, we provide you with tools to emulate the behavior of `Flux` within the environment, allowing to test against your repository before committing changes. If further assistance is needed, reaching out through the support system is encouraged.
