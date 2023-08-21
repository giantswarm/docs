---
linkTitle: Giant Swarm Release v21.0.0
title: Giant Swarm Release v21.0.0
description: Giant Swarm release v21 besides many improvements will introduce Kuberntes Release Version 1.25.x. Following handbook should be carefully read by customers upfront the upgrade to prepare the clusters and workloads accordingly.
weight: 10
menu:
  main:
    parent: advanced-upgrades
aliases:
  - /guides/gs-release-v21/
user_questions:
  - Where can I read about v21 changes?
  - What does v21 change?
  - What changes does Kubernetes Version 1.25 bring?
  - What do i have to prepare for v21?
  - How does the Kubernetes V1.25 migration work?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-turtles
last_review_date: 2023-08-02
---

{{< platform_support_table aws="alpha=v21.0.0" >}}

## Introduction

As we prepare the Giant Swarm Release v21 we want to already give you a sneak preview of the upcoming changes.
One major change will be the upgrade to the latest Kubernetes Version 1.25.x for which we already prepared our platform extensively with the Giant Swarm Version 19 and Version 20.
In this document we want to take a look at the upcoming changes and key highlights for the new Giant Swarm Version 21 and with that Kubernetes Version 1.25.

## Kubernetes v1.25: Enhancing Security and Empowering Policies

### Major Changes

There are some significant changes and enhancements that come with this release, specifically focusing on the removal of Pod Security Policy (PSP) and the introduction of Pod Security Standard (PSS).

#### Goodbye, Pod Security Policy (PSP)

Kubernetes v1.25 bids farewell to the long-standing Pod Security Policy feature. PSP has been a reliable tool for enforcing security policies at the pod level. However, it has also faced challenges with its complexity and lack of flexibility. With the continuous evolution of Kubernetes and the community's dedication to improving security, [a more adaptable and user-friendly solution has emerged](https://docs.giantswarm.io/getting-started/rbac-and-psp/#pod-security-standards-pss).

#### Introducing Pod Security Standard (PSS) with Kyverno policies

Kyverno policies for PSS take center stage in Kubernetes v1.25 as the replacement for Pod Security Policy. By using Kyverno policies, Giant Swarm empowers customers to effortlessly define and enforce policies for security and beyond. Let's explore some key features and advantages of Kyverno-based PSS:

- **Feature Parity with PSP:** Kyverno supports very granular policy control which improves both the security and the level of policy flexibility our customers currently require from PSPs. We’ve written [a blog post](https://www.giantswarm.io/blog/giant-swarms-farewell-to-psp) detailing how this impacted our decision.
- **Beyond Pods:** Cluster administrators gain a powerful way to reduce mistakes and misconfigurations in resources of any type, including Ingresses, Services, and Network Policies in addition to Pods and their controllers.
- **Custom Security Policies:** Create custom policies tailored to your organization's needs, ensuring adherence to specific security requirements not possible with PSPs.
- **Resource Mutation:** Reduce the risk of misconfiguration and ease the burden on developers by automatically applying trusted configuration to cluster resources.
- **Audit and Compliance:** Built-in reporting support helps track policy violations and maintain compliance with industry regulations and best practices.

Giant Swarm releases for Kubernetes v1.25 and above will include Kyverno and a set of managed policies which replicate the functionality offered by PSPs. For more information about these policies, or for assistance migrating from PSP to Kyverno, [see our docs](https://docs.giantswarm.io/advanced/security-policy-enforcement/#default-policies).

**Important:** In case you directly installed Helm charts in a cluster, you need to ensure to remove the PSP from the installed Helm release (revision) before upgrading to Kubernetes v1.25.

## Further notices

### Deprecated API versions 

Deprecated API versions that are no longer served (use a newer one):

```
CronJob                 batch/v1beta1
EndpointSlice           discovery.k8s.io/v1beta1
Event                   events.k8s.io/v1beta1
HorizontalPodAutoscaler autoscaling/v2beta1
PodDisruptionBudget     policy/v1beta1
PodSecurityPolicy       policy/v1beta1
RuntimeClass            node.k8s.io/v1beta1
```

### CSI Migration

In order to remove the in-tree plugins entirely, the core CSI Migration feature went GA in v1.25.
General Stability and Bug Fixes

## 🙇🏻‍♂️ Final last words

As with any new release, Kubernetes v1.25 includes general stability improvements and bug fixes. These updates address various issues reported in earlier versions, ensuring a more reliable and robust Kubernetes experience.

As always, we encourage you to explore [the official Kubernetes documentation](https://kubernetes.io/blog/2022/08/23/kubernetes-v1-25-release/) and reach out to our support teams for any assistance during the upgrade process. 

Happy upgrading!


## Further reading

- [Giant Swarm V19 Documentation](https://docs.giantswarm.io/advanced/upgrades/aws-19-release/)
- [Pod Security Standards (PSS)](https://docs.giantswarm.io/getting-started/rbac-and-psp/#pod-security-standards-pss)
- [Farewell to PSP - Blog Post](https://www.giantswarm.io/blog/giant-swarms-farewell-to-psp)
- [Default Policies in Policy Enforcement](https://docs.giantswarm.io/advanced/security-policy-enforcement/#default-policies)
- [Giant Swarm Cilium migration steps from AWS CNI](https://handbook.giantswarm.io/docs/support-and-ops/ops-recipes/upgrade-to-cilium/)
- [Kubernetes.io Blogpost to Kubernetes Version 1.25](https://kubernetes.io/blog/2022/08/23/kubernetes-v1-25-release/)
