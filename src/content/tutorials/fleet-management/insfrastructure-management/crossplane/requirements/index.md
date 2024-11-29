---
linkTitle: Crossplane requirements
title: Crossplane requirements
description: Resource requirements and risks Crossplane impose on the management cluster.
weight: 20
menu:
  principal:
    identifier: tutorials-fleet-management-infrastructure-crossplane-requirements
    parent: tutorials-fleet-management-infrastructure-crossplane
last_review_date: 2024-11-29
user_questions:
  - How do I configure Crossplane in the Giant Swarm platform?
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
---

## Requirements

`Crossplane` significantly impacts the management cluster, depending on the `provider(s)` used.

### Resource usage

The providers require a significant amount of memory to run stable. For the largest, official AWS provider, we sometimes experienced 10+ GB of memory requests to run. This depends on the number of custom resource definitions (CRDs) and custom resources (CRs) managed by the provider pod.

### Deploying hundreds of CRDs

Managing cloud providers resources via Kubernetes CRs is one of the best thing of `Crossplane`, but also causes a lot of issues in its current state, because most cloud providers impose hundreds of new custom resource definitions to the management cluster:

- official AWS provider `v0.31.0` has `894` CRDs
- official Azure provider `v0.29.0` has `705` CRDs
- official GCP provider `v0.29.0` has `894` CRDs

This - depending on the number of custom resource definitions - impose possible [performance issues](https://github.com/crossplane/crossplane/blob/10f1e90ebb4178d4773f54bd5d7f57e7137f2d77/design/one-pager-crd-scaling.md)
to the management cluster, including:

- the API servers will take up much more memory to handle the increase in custom resource definitions (around [~3MB](https://github.com/crossplane/crossplane/issues/3754#issue-1578890243) and up to 4.5MB from Giant Swarm estimation per custom resource definition)
- Other `Kubernetes` operators - especially ones using an older `client-go` version than `v0.25.0` - might experience throttling and timeouts towards the API. In that version, the request burst limits were increased to 300. Still, in our experience, this only partially solves the issue (while it helps) and is unreliably applied across the Kubernetes landscape. The relevant upstream issue can be found [here](https://github.com/crossplane/crossplane/issues/3272).
- interacting with the cluster gets slower because of similar issues as the above item because of the client-side throttling caused by the increased number of CRDs when building the [discovery cache](https://github.com/kubernetes/client-go/blob/1517ffb8d37c99e6a3a2842bcdee0aa271f0332b/discovery/discovery_client.go)

There are currently ongoing discussion in the `Crossplane` community on how to mitigate these issues:

- https://github.com/crossplane/crossplane/issues/3852
- https://github.com/crossplane/crossplane/issues/2869

## Additional readings

- [The Kubernetes Discovery Cache: Blessing and Curse](https://jonnylangefeld.com/blog/the-kubernetes-discovery-cache-blessing-and-curse)
- Giant Swarm investigation on `Crossplane` performance issues:
    - [Impact of Crossplane on control plane nodes](https://github.com/giantswarm/roadmap/issues/2061#issuecomment-1461657937)
    - [Investigation around deleting and blocking CRDs](https://github.com/giantswarm/roadmap/issues/2061#issuecomment-1470139555)
