---
linkTitle: Best practices
title: Recommendations and best practices
description: Recommendations and best practices around cluster and node sizing as well as multi-tenant setups.
weight: 110
menu:
  main:
    parent: getting-started
aliases:
  - /guides/recommendations-and-best-practices/
  - /kubernetes/best-practices/
owner:
  - https://github.com/orgs/giantswarm/teams/team-teddyfriends
user_questions:
  - How should I size my control plane nodes?
  - How should I size my worker nodes?
  - How should I separate concerns using several clusters?
  - How many worker nodes should my clusters have?
  - How many control plane nodes should I run?
last_review_date: 2022-12-07
---

Keep in mind that these recommendations are just basic rules-of-thumb that you should adapt to your needs.

## Creating a cluster

### Cluster sizing

There are a few questions that you might want to answer to determine the right size for your cluster:

1. What kind of environment are you targeting? (short test, development, QA, production)
2. What kind of workloads will be running in there and how much resources do they need?

In general a cluster that will only be short-lived and for testing purposes only can be rather small and doesn't need much buffer.
Otherwise you should always account for at least 1 node buffer, so in case one of your nodes goes down or gets rolled due to updates
 your workloads still have room to be scheduled.

Furthermore, once you want to actually use the cluster productively, we would recommend to have at least 4 worker nodes in your cluster.
"Working productively" includes working regularly with any kind of cluster, even if it's officially only a cluster for development or testing.
You don't want your development environment to be down, because of a minor node failure.

For production usage the cluster should have at least 5 nodes and a buffer of 2 nodes.

#### Control plane nodes

Control plane nodes are more critical than worker nodes in achieving better availability and performance. Several worker nodes can be replaced at the same time with no downtime but the failure of a control plane node could cause a major issue if it is your only control plane node. [High-availability control planes]({{< relref "/advanced/high-availability/control-plane/index.md" >}}) can be used on AWS to reduce downtime to a minimum but still need to be sized correctly to avoid performance issues.

The control plane nodes host critical components like the API, scheduler, Etcd, and many more. The load of these components will directly depend on the amount of resources they are managing, the number of API requests being served, and the events being generated in the cluster.

In order to size the control plane nodes sufficiently, we recommend:

- Clusters with 50 nodes or 1000 pods should use `m5.2xlarge` (on AWS) or `Standard_D4s_v3` (on Azure) instance types or higher.
- Clusters with 100 nodes or 2000 pods using single control plane nodes should use `m5.4xlarge` (on AWS) or `Standard_D8s_v3` (on Azure) and with high-availability control planes (AWS only) use `m5.2xlarge`.

#### Worker node size

When it comes to sizing your worker nodes, there should generally be a preference for a greater number of smaller nodes vs. a smaller number of larger nodes.
However, avoid node sizes of less than 1 core and 2GB RAM.

To determine the right sizing in terms of cores and RAM, you need to know what kind of workloads will be run on the cluster
 and how much resources they need.
Note that even if the average load might be low, you should also account for peak load times as well as startup-peaks (i.e. some apps need a lot of resources just for their startup).

## Multi-cluster and multi-tenant setups

There are two ways to separate environments, teams, and in general deployments from each other:

1. Multiple clusters
2. Single clusters with multi-tenancy setup

While the first offers the highest possible isolation, it is also the most resource-intensive.
Still, at least with the current state of multi-tenancy, multiple clusters are the easiest way to separate environments.
It further offers you the flexibility to have differing configurations in each cluster,
 including running different Kubernetes versions in different clusters.

The complexity of using a single cluster in a multi-tenant setup depends on the amount of isolation needed between the people working on it.
If trust is high, namespaces alone can be enough. However, if you want real isolation between those namespaces, you need to use them together with strictly set up RBAC, network policies, service accounts, and other minor security mechanisms, to make sure there is no escalation of privileges
 as well as no interference between the tenants.

### How many clusters

In most cases, you will need several clusters at some point.
This opens up the question as to how many clusters should be created.

While you might have a variable amount of short-lived clusters (e.g. for testing or playgrounds),
 you also want to have a specific amount of clusters that are fixed.
Typically, these would be 1 cluster per stage. Example:

- One for development
- One for testing or quality assurance
- One for staging
- One for production

This setup is often repeated for each team, so that each team has 2-5 clusters.

However, with a lot of teams it might lead to a lot of wasted resources,
 especially if the products of these teams should be working together anyway.
In these cases it might be better to have a single (or few) production (and a staging) cluster for everyone.
The classification of these clusters should be rather by workloads then by teams.
Thus, you could for example have a separate cluster for services that handle
 sensitive data, and/or one that holds services that need to fulfill certain compliance requirements.

Each team can still have a test cluster for themselves to be working independently.

The single production cluster is especially feasible if deployments to it can only be done through a CI/CD pipeline.
This way the deployments are automated and no one can manually interfere in the cluster.

The downside to the multi-tenant single cluster approach is that it, as mentioned above,
 needs to be secured with much more scrutiny.

## Further reading

- [Creating clusters with gsctl]({{< relref "/ui-api/gsctl/create-cluster" >}})
- [Cluster Size and Autoscaling]({{< relref "/getting-started/cluster-size-autoscaling" >}})
- [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/)
- [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
