---
linkTitle: Giant Swarm Policy API
title: Giant Swarm Policy API Guide
description: An overview of how to use Giant Swarm Policy types to enforce cluster security and best practices.
weight: 60
menu:
  main:
    parent: advanced
aliases:
  - /advanced/security-policy-enforcement/policy-api
user_questions:
 -  How can I exclude a workload from a Kyverno policy?
 -  What security policies are enforced in my cluster?
 -  How do I migrate from PSPs to PSS?
 -  What is the Policy API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
last_review_date: 2023-10-04
---

<!-- {{< platform_support_table aws="alpha=v17.2.0" aws="ga=v17.4.0">}} -->

__Note__: This guide is intended for cluster administrators running Giant Swarm managed Kubernetes clusters. More general information about Pod Security Standards can be found on the [Security policy enforcement][sec-policy-enforcement] page.

## Managing cluster security policies with the Giant Swarm Policy API

The Policy API is an abstraction layer which orchestrates several other types of policy-related resources.

The Giant Swarm platform is built on top of a number of independent tools, projects, and APIs supported by the CNCF and the surrounding Kubernetes ecosystem.
Among these are a number of resources designed for enforcing policies within a cluster. These include built-in types like Network Policies and RBAC as well as external CRDs like Kyverno Cluster Policies or Cilium Network Policies, among others.

We use and manage tools which we see as bringing value for customers, and which are governed and maintained in a way which aligns with our guiding principles.
We encourage our customers to optimize, experiment, and make full use of all of our platform components, but we also recognize that using many different tools comes with overhead and complexity.
We want to make that overhead optional, and be able to fully manage a feature without requiring customers to change tools, update config, or plan for complicated migrations when one of the underlying implementations changes.

For example, when the Pod Security Policy type was deprecated and removed, many workloads had to be re-evaluated and new exceptions created for them, even though neither the workload nor the risk had changed.
Some new features were gained, but the effort was primarily invested in order to maintain feature parity and avoid security regressions.
We expect that Kubernetes and third-party tooling will continue to evolve, and that we can help our customers be faster if they are not directly tied to tool-specific interfaces which they don't actually want to manage.

So, we created the Policy API in order to allow Giant Swarm to more seamlessly and transparently move clusters between policy implementations, and to reduce the overall toil of dealing with common security configuration.

### At a glance

The Policy API:

- is an interface for configuring the various types of (mostly security-related) policies which Giant Swarm manages.
- provides a way for cluster administrators to declare their intent about which policies to enforce and which resources are exempt from those policies.
- is intended to manage additional policy types in the future, including networking, vulnerability management, anomaly detection, and others.
- is _not_ a general purpose policy syntax language. Users cannot define custom policies via the Policy API. It can only be used to configure the policies Giant Swarm actively manages.
- does _not_ hide the underlying implementations. Users are free to directly use the underlying tools or APIs. The only difference is that _Giant Swarm will not manage, migrate, or adopt any policies or configuration you create using the tools' native resources_.
- generates native resources for the underlying implementations. These resources continue to function even if the Policy API controllers are removed.
  
#### Managed and un-managed policies

Giant Swarm provides a set of ready-made policies for many common cluster management use cases. The Policy API only orchestrates these standard policies, which Giant Swarm actively manages. It does not interfere with customer policies, exceptions, or configuration which are managed externally to the Policy API.

For example, Giant Swarm enforces security policies in every cluster by default, and advises customers to use the Policy API to declare exceptions for any workloads which need them.
We currently use Kyverno to enforce those policies, and the Policy API generates Kyverno PolicyExceptions based on the exceptions configured through the Policy API.

A cluster administrator might choose to use the pre-installed, managed Kyverno instance to enforce their own additional policies, for instance to enforce some business-specific logic.
They can easily do that by creating a new Kyverno `ClusterPolicy`, and creating Kyverno `PolicyException`s for any approved exceptions.

If, hypothetically, in the future, Giant Swarm chooses to stop managing Kyverno as part of our standard platform, we would use our Policy API controllers to move our managed policies and any relevant exceptions into a new implementation which maintains the desired behavior.

The custom ClusterPolicy, and any configured Kyverno PolicyExceptions, would need to be adapted by the cluster administrator, or they would need to then manage Kyverno themselves.

<!-- ### Working with the Giant Swarm Policy API -->

[sec-policy-enforcement]: {{< relref "/advanced/security-policy-enforcement" >}}
