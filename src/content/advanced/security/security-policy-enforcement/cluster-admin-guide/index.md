---
linkTitle: Cluster admin policy guide
title: Policy enforcement guide for cluster admins
description: An overview of how to use Giant Swarm Policy types to enforce cluster security and best practices.
weight: 60
menu:
  main:
    parent: security-policy-enforcement
aliases:
  - /advanced/security/security-policy-enforcement/cluster-admin-guide
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

## Migrating from Pod Security Policy (PSP) to Pod Security Standards (PSS) with Kyverno

### TL;DR

To migrate a cluster from PSP to PSS, cluster admins need to:

1. Upgrade the cluster to Giant Swarm v19.1.x. This upgrade adds PSS policies in audit mode, and deploys our migration components.
    - Migration components in the cluster will automatically create `PolicyExceptionDraft` resources (reference).
2. Save the generated Giant Swarm `PolicyExceptionDrafts` in a location of your choosing (guide).
3. After any necessary security review, change the API kind of the resources from `PolicyExceptionDraft` to Giant Swarm `PolicyException`.
4. Deploy the Giant Swarm `PolicyException` resources to the cluster.
    - An operator in the cluster will automatically create Kyverno `PolicyException` resources from the Giant Swarm `PolicyExceptions`.
5. Repeat steps 2-4 until all workloads are compliant.
6. Upgrade the cluster to Giant Swarm v19.2.x. This upgrade will enable enforcement of PSS policies.
7. While the cluster is in version 19.2.x, remove all PSPs not managed by Giant Swarm from the cluster. Any Helm release which includes a PSP will fail after the next upgrade.
8. Upgrade the cluster to Giant Swarm v20.0.0. This upgrade will fully remove the PSP API.

### Migration path

The migration from PSP to PSS will span three releases:

- v19.1.x - during this phase, PSS policies are deployed in audit mode. Teams must make all workloads compliant or deploy exceptions for failing workloads.
- v19.2.x - during this phase, PSS policies are enforced. Non-compliant resources will be rejected. Teams must remove all PSPs from the cluster.
- v20.0.x - this is the target release of Kubernetes v1.25, which fully removes the PSP API. Migration is considered complete.

### Administrative decisions

Prior to starting PSS migration, teams should decide how to bring the new policy lifecycle under their existing security and change management processes.

#### Decide whether to self-manage or use the Policy API

To keep feature parity with PSPs, Giant Swarm clusters use Kyverno to enforce security policies.
Kyverno policies and exceptions are more powerful and expressive than PSPs, and thus offer many new features beyond PSP replacement.

However, many of the teams we work with would prefer not to manage Kyverno resources at all.
We understand that sentiment, and agree that standard security features should "just work".
So, to make things "just work" and hopefully make future migrations easier, we are introducing a Giant Swarm-specific abstraction called the Policy API which allows us to manage the underlying policies and exceptions which we believe are fundamental to running a healthy cluster.
You can read more about the Policy API on its dedicated docs page.

The rest of this guide assumes your migration will be done using our Policy API. However, if your team would prefer to manage Kyverno resources directly instead, that is still allowed by the platform, just with less future support.

If your team chooses to self-manage Kyverno resources, your migration path would look nearly identical, except that you will need to create Kyverno PolicyExceptions for any failing workloads instead of Giant Swarm PolicyExceptions.
(Or, let our migration tools generate them, save the resulting exceptions, and remove the migration tools).
Be aware that this means we won't be able to automatically migrate your exceptions between Kyverno or Kubernetes API versions in the future, or use them to manage other types of policies which apply to the same workloads.

#### Decide how to handle exceptions going forward

**Action item:** ensure your exception approval and creation process will still work after migration.

PSPs were bound to workloads by granting certain RBAC permissions to the workload's service account.
As the name implies, Pod Security Policies applied only to Pods, and specifically to their security context and container security context fields.
It was common practice to have a `restricted` PSP bound to all service accounts by default.
Workloads which did not comply with the `restricted` PSP could be granted an exception by granting them `use` permissions for a less restrictive PSP.
There is often a process for applying for an exception, and a workflow for creating the new, less restrictive PSP.

Using Kyverno, policies and exceptions are no longer associated with cluster resources through RBAC.
Policies can apply to any type of resource, and select those resources through a much more flexible selection syntax.
Likewise, an exception to a policy also can apply to non-Pod resources, and can be done using more expressive selection logic.
The Giant Swarm Policy API offers a simplified interface for creating these exceptions.
Any existing processes and workflows for PSP-based exceptions will need to be revisited and ensure they will still work for creating the Giant Swarm PolicyExceptions (or the Kyverno PolicyExceptions, if your team chooses to self-manage Kyverno resources).

**Important:** Creation of both Giant Swarm and Kyverno PolicyExceptions should be tightly controlled, since they allow workloads to bypass security controls.

##### Centralized and distributed models

Conway's law suggests organizations build systems which resemble their internal structures. Security processes are no exception (ha!), and our customers vary widely with regard to the level of autonomy and self-service they afford to their developers.

Organizations at the highly autonomous end of the spectrum choose to allow their application developers to manage their own PolicyExceptions from within their application repositories.
Others choose to centralize the PolicyExceptions in a single place, typically controlled by the platform/infrastructure team.
Some organizations require a mixed approach where, for example, different business units are responsible for exceptions stored in different locations.

All of these are valid and workable approaches, but it is important to be deliberate when designing the exception workflow so that only exceptions approved by trusted processes can be deployed.

For new users of the platform who do not already have an established process for handling security exceptions, we suggest keeping the PolicyExceptions controlled centrally, in a GitOps repo configured to require review from any necessary stakeholders in order to modify exceptions.

If your organization already has an automated system for exception management, we'd like to hear from you about how you currently use it, and may use it with the Policy API in the future.

##### Recommended future-proofing

Giant Swarm plans to publish more extensive guidance about optimal policy and exception workflows in the future.

For now, here are some things to consider when deciding how to structure your organization's exceptions:

- Approval: what is the process for a user to receive a security exception?
- Storage access: who has read access to the exception storage? Who can approve new or modified exception resources?
- Cluster access: which cluster entities can create / read / update / delete exceptions in the cluster?
- Duration: do you now or in the future want to impose time limits on an exception?
- Provenance: do you now or in the future want to require that exceptions be cryptographically signed in order to be valid?

We are also interested in hearing about and learning from your experience with exception workflows. If our platform can enable a better exception experience for you, please reach out.

[sec-policy-enforcement]: {{< relref "/advanced/security/security-policy-enforcement" >}}
