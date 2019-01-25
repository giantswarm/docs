+++
title = "Recommendations and Best Practices"
description = "Recommendations and best practices around cluster and node sizing as well as multi-tenant setups"
date = "2019-01-17"
type = "page"
weight = 50
tags = ["tutorial"]
+++

# Recommendations and Best Practices

Keep in mind that these recommendations are just basic rules-of-thumb that you should adapt to your needs.

## Creating a Cluster

### Cluster Sizing

There are a few questions that you might want to answer to determine the right size for your cluster:

1. What kind of environment are you targetting? (short test, development, QA, production)
2. What kind of workloads will be running in there and how much resources do they need?

In general a cluster that will only be short-lived and for testing purposes only can be rather small and doesn't need much buffer.
Otherwise you should always account for at least 1 node buffer, so in case one of your nodes goes down or gets rolled due to updates
 your workloads still have room to be scheduled.

Furthermore, once you want to actually use the cluster productively, we would recommend to have at least 4 worker nodes in your cluster.
"Working productively" includes working regularly with any kind of cluster, even if it's officially only a cluster for development or testing.
You don't want your development environment to be down, because of a minor node failure.

For production usage the cluster should have at least 5 nodes and a buffer of 2 nodes.

#### Worker Node Size

When it comes to sizing your worker nodes, there should generally be a preference for more smaller nodes vs less bigger ones.
However, avoid node sizes of less than 1 core and 2GB RAM.

To determine the right sizing in terms of cores and RAM, you need to know what kind of workloads will be run on the cluster
 and how much resources they need.
Note that even if average load might be low, you should also account for peak load times as well as startup-peaks (i.e. some apps need a lot of resources just for their startup).

## Multi-Cluster and Multi-Tenant Setups

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

### How many clusters?

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
 sensitive data, and/or one that holds services that need to fullfill certain compliance requirements.

Each team can still have a test cluster for themselves to be working independently.

The single production cluster is especially feasible if deployments to it can only be done through a CI/CD pipeline.
This way the deployments are automated and no one can manually interfere in the cluster.

The downside to the multi-tenant single cluster approach is that it, as mentioned above,
 needs to be secured with much more scrutiny.

## Further Reading

- [Creating clusters with gsct](/reference/gsctl/create-cluster/)
- [Cluster Size and Autoscaling](/basics/cluster-size-autoscaling/)
- [Using RBAC Authorization](https://kubernetes.io/docs/admin/authorization/rbac/)
- [Network Policies](https://kubernetes.io/docs/concepts/services-networking/networkpolicies/)
- [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/)
- [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)
