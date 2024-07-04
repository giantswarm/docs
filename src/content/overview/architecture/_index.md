---
title: Architecture of the Giant Swarm cloud-native developer platform
linkTitle: Architecture of the platform
description: Components, capabilities, supported cloud providers, and the platform API.
weight: 20
menu:
  principal:
    parent: overview
    identifier: overview-architecture
user_questions:
  - What is the architecture of the Giant Swarm cloud-native developer platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-horizon
last_review_date: 2024-06-27
---

Giant Swarm's cloud-native developer platform is a collection of open-source components that work together to provide a seamless experience for managing the lifecycle of containerized applications. The platform is designed to be cloud-agnostic, allowing you to deploy your applications on any of the supported cloud providers. Besides, the platform offers a rich set of APIs that our customers can use to offer a set of self-service capabilities to their developers.

Platform architecture diagram from https://docs.google.com/presentation/d/1LoyfqmmgIJV2AJo46Ofv3a3hCnbkN4C3ujHM-t3VJko/edit#slide=id.g25bea7591a5_0_0

<!-- DO WE WANT TO SLICE IT BY OUR OWN AREAS INSTEAD? -->

With this premise, we have built a solution consisting of various distinct areas: access management, observability, security, continuous delivery, and connectivity. Each of these areas is composed of multiple components that work together to provide the desired functionality. On top of these areas, we have built a set of APIs that allow our customers to automate tasks. <!-- we mentino developer portal too? -->

## Platform architecture

For technical reasons we are creating a management cluster per region. Explain those reasons.

Show a diagram of the management cluster and components.

## Access management

<!--
Proposed outline:

- Intro paragraph
- Main diagram with description of the layers -> I added a review to the main diagram in miro https://miro.com/app/board/uXjVO2Dh15w=/
- One or two paragraph section for each layer/section of the diagram

Ensure during the description of each layer/section we link to the relevant documentation page that goes into more detail.
-->