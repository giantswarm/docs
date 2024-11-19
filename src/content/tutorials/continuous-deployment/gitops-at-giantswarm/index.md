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
last_review_date: 2024-11-07
---

One of the goals at Giant Swarm is to ensure you have a successful GitOps journey.

To achieve it, our team has built this tutorial together with presentations and workshops to help get you started. Moreover, we offer an [opinionated template](https://github.com/giantswarm/gitops-template) crafted around our environments, and additional tooling to generate and validate your resource manifests before they're applied.

You can start reading from top to bottom or jump to the section you are interested in. The content is structured to guide you through the process of setting up your environment, managing your resources, and deploying your applications.

Be conscious that you maintain the full ownership of your resources, our engineers most of the times have no visibility of any  manifests or configuration. These will always remain your responsibility to create and manage. In case of emergencies, you can provide us with access to your resources, but only with your explicit consent.

Giant Swarm is committed to your success and understands that tracing issues at the beginning can be challenging. To assist, our platform provides you with tools to emulate the behavior of `Flux`, allowing to test against your repository before committing any change. If further assistance is needed, reaching out through the support system is encouraged.

Read the next chapter, [`what's GitOps?`]({{< relref "/tutorials/continuous-deployment/what-is-gitops/" >}}).
