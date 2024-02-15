---
linkTitle: Giant Swarm Policy API
title: Giant Swarm Policy API Guide
description: An overview of how to use Giant Swarm Policy types to enforce cluster security and best practices.
weight: 60
menu:
  main:
    parent: security-policy-enforcement
user_questions:
 -  How can I exclude a workload from a Kyverno policy?
 -  What security policies are enforced in my cluster?
 -  How do I migrate from PSPs to PSS?
 -  What is the Policy API?
last_review_date: 2023-11-07
aliases:
  - /guides/security-policy-enforcement/policy-api
  - /advanced/security-policy-enforcement/policy-api
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

{{< platform_support_table aws="ga=v19.1.1">}}

__Note__: This guide is intended for cluster administrators running Giant Swarm managed Kubernetes clusters. More general information about Pod Security Standards can be found on the [Security policy enforcement][sec-policy-enforcement] page.

## Managing cluster security policies with the Giant Swarm Policy API

Policy API is an abstraction layer that orchestrates other types of policy-related resources.

It is intended to be used by cluster administrators and developer platforms to configure and automate management of various policy enforcement tools in Kubernetes clusters.

### At a glance

The Policy API:

- is an interface for configuring the various types of (mostly security-related) policies that Giant Swarm manages.
- provides a way for cluster administrators to declare their intent about which policies to enforce and which resources are exempt from those policies.
- is intended to manage additional policy types in the future, including networking, vulnerability management, anomaly detection, and others.
- is _not_ a general purpose policy syntax language. Users cannot define custom policies via the Policy API. It can only be used to configure the policies Giant Swarm actively manages.
- does _not_ hide the underlying implementations. Users are free to directly use the underlying tools or APIs. The only difference is that _Giant Swarm will not manage, migrate, or adopt any policies or configuration you create using the tools' native resources_.
- generates native resources for the underlying implementations. These resources continue to function even if the Policy API controllers are removed.

### Working with Policy API

Users interact primarily with two types of resources: Policies and PolicyExceptions.

#### Policies

Giant Swarm Policy resources enable cluster administrators to control how policies are applied to their clusters.

Currently, only support for Pod Security Standards policies has been implemented. The policy names and descriptions are documented on our [security policy enforcement page][sec-policy-enforcement].

This section will be updated as we implement new policy options.

#### PolicyExceptions

The PolicyException type allows cluster administrators (and other users to whom admins have delegated this capability) to identify resources which are exempt from one or more policies.

For example, this `PolicyException` allows the `special` Deployment in the `sample` namespace to be admitted to the cluster even if it fails two named security policies:

```yaml
apiVersion: policy.giantswarm.io/v1alpha1
kind: PolicyException
metadata:
  name: my-workload-exceptions
  namespace: my-namespace
spec:
  policies:
    - disallow-host-path
    - restrict-volume-types
  targets:
    - kind: Deployment
      namespaces:
      - sample
      names:
      - special*
```

Based on this exception, the Policy API controllers will generate additional resources and make configuration changes to any tools which enforce the listed policies.

### Motivation / Historical note

The Giant Swarm platform is built upon a number of independent tools, projects, and APIs supported by the CNCF and the surrounding Kubernetes ecosystem.
Among these are a number of capabilities designed for enforcing policies within a cluster. These include built-in types like Network Policies and RBAC as well as external CRDs like Kyverno Cluster Policies or Cilium Network Policies, among others.

We use and manage tools we believe are the "right tool for the job" and add value for customers.
Over time, however, the "right tool" may change.
It can be difficult to keep up with so many rapidly evolving projects (think of all the alpha or beta version APIs currently in production!), and the simple reality is that many teams don't care what the tool is as long as their needs are met.
By decoupling our customers' intent from the underlying tooling, we can automate much of the migration work needed to smoothly transition them between policy implementations.

When Pod Security Policies were removed, for example, many workloads had to be re-evaluated and new exceptions created for them, even though neither the workload nor the inherent risk had changed.
Much effort was spent maintaining feature parity and avoiding security regressions as clusters upgraded to v1.25.
Staying up to date is an important part of maintaining a system's security posture, but many organizations could not keep up with the PSP deprecation work, so simply stopped enforcing Pod-level security policies.

The first implementation of the Giant Swarm Policy API was created to help our customers migrate automatically (to the extent possible) from PSP to a feature-equivalent implementation of Pod Security Standards without having any policy enforcement coverage gaps during the migration.
We expect that Kubernetes and third-party tooling will continue to evolve, and that we can help our customers be faster if they are not directly tied to tool-specific interfaces which they don't actually want to manage.

So, we created the Policy API in order to allow Giant Swarm to more seamlessly and transparently move clusters between policy implementations, and to reduce the overall toil of dealing with common security configuration.

### Managed versus un-managed policies

Giant Swarm provides a set of ready-made policies for many common cluster management use cases. The Policy API only orchestrates these standard policies, which Giant Swarm actively manages. It does not interfere with customer policies, exceptions, or configurations that are managed externally to the Policy API.

For example, Giant Swarm enforces security policies in every cluster by default, and advises customers to use the Policy API to declare exceptions for any workloads that need them.
We currently use Kyverno to enforce those policies, and the Policy API generates Kyverno PolicyExceptions based on the exceptions configured through the Policy API.

A cluster administrator might choose to use the pre-installed, managed Kyverno instance to enforce their own additional policies, for instance to enforce some business-specific logic.
They can easily do that by creating a new Kyverno `ClusterPolicy`, and creating Kyverno `PolicyExceptions` for any approved exceptions.

If, in the future, Giant Swarm were to choose to stop managing Kyverno as part of our standard platform, we would use our Policy API controllers to move our managed policies and any relevant exceptions into a new implementation that maintains the desired behavior.

The custom ClusterPolicy, and any configured Kyverno PolicyExceptions, would need to be adapted by the cluster administrator, or they would need to then manage Kyverno themselves.

[sec-policy-enforcement]: {{< relref "/vintage/advanced/security/security-policy-enforcement" >}}
