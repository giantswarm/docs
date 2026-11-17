---
title: Cluster downgrades
diataxis_content_type: explanation
description: Why Giant Swarm doesn't support downgrading a workload cluster to an older release, and how staged upgrades reduce the risk of an upgrade instead.
weight: 15
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-cluster-downgrades
last_review_date: 2026-11-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - Can I downgrade a workload cluster to a previous release?
  - Can I roll back a cluster upgrade if something goes wrong?
  - How can I reduce the risk of a cluster upgrade?
---

Before a production upgrade, you might ask if you can go back to the previous release if something breaks. The short answer is no. Giant Swarm doesn't test or support downgrading a workload cluster to an older release. Plan your upgrades so you never need to.

## Why downgrades aren't supported

A [workload cluster release]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/releases" >}}) bundles Kubernetes with many other components, like the operating system, the container runtime, and the network plugin. An upgrade changes all of them. Some of these changes are one way:

- A newer Kubernetes version can store resources in etcd in a format or API version that the older version can't read.
- Components can migrate their own state or custom resources to a new schema during the upgrade.
- Major releases follow Kubernetes minor versions. The Kubernetes project doesn't test downgrades between minor versions, so a downgrade of a major release has no upstream guarantee either.

A downgrade might work in some cases, but the result is unpredictable. A failed downgrade can leave the cluster in a worse state than the upgrade you wanted to undo. That's why it isn't an option we offer as a fallback.

## Use staged upgrades instead

Reduce the risk of an upgrade by rolling it out in stages, so a problem shows up before it reaches production:

1. Upgrade your development or staging clusters first.
2. Run your workloads on the new release for a while and check that they behave as expected.
3. Upgrade production clusters one at a time, or in small groups, rather than all at once.
4. Spread production upgrades over different days or regions, so one issue can't affect all of them.

Before you start, read the [changelog]({{< relref "/changes" >}}) for the target release and make your workloads [resilient to upgrades]({{< relref "/tutorials/fleet-management/cluster-management/cluster-upgrades#avoid-downtime-during-upgrades" >}}).

## If an upgrade goes wrong

Contact Giant Swarm support right away through your usual channel. We'll work with you to fix the issue on the current release, for example with a configuration change or a new patch release, rather than by downgrading the cluster. See the [support overview]({{< relref "/support/overview" >}}) for how to reach us.

## Further reading

- [Cluster upgrades]({{< relref "/tutorials/fleet-management/cluster-management/cluster-upgrades" >}}) explains how upgrades work and how to prepare your workloads for them.
- [Workload cluster releases]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/releases" >}}) describes how releases are versioned.
