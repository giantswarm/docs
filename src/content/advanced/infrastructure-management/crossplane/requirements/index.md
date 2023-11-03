---
linkTitle: Crossplane requirements
title: Crossplane requirements
description: Resource requirements and risks Crossplane impose on the management cluster.
weight: 20
menu:
user_questions:
- What are the requirements for Crossplane?
- What are the risks of using Crossplane?
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-03-21
---

## Requirements

Crossplane has a significant impact on the management cluster, greatly depending on the used `provider(s)`.

### Resource usage

The providers require a significant amount of memory to run stable. In some cases for the largest, official AWS provider
we experienced 10+ GB of memory request to run. Seemingly this depends on the number of CRDs and CRs managed by the
provider pod.

### Deploying hundreds of CRDs

Managing cloud providers resources via Kubernetes CRs is one of the best thing of Crossplane, but also causes a lot of
issues in its current state, because most cloud providers impose hundreds of new CRDs to the management cluster:

- official AWS provider `v0.31.0` has `894` CRDs
- official Azure provider `v0.29.0` has `705` CRDs
- official GCP provider `v0.29.0` has `894` CRDs

This - depending on the number of CRDs - impose possible [performance issues](https://github.com/crossplane/crossplane/blob/10f1e90ebb4178d4773f54bd5d7f57e7137f2d77/design/one-pager-crd-scaling.md)
to the management cluster, including:

- the API servers will take up much more memory to handle the increase in CRDs (
  around [~3MB](https://github.com/crossplane/crossplane/issues/3754#issue-1578890243) and up to
  4.5MB from Giant Swarm estimation per CRD)
- other kubernetes operator - especially ones using an older `client-go` version than `v0.25.0` - might experience
  throttling and timeouts towards the API. That version an up the request burst limits were increased to 300 but in
  our experience this does not completely solve the issue (while helps) and is unreliably applied across the kubernetes
  landscape. The relevant upstream issue can be found [here](https://github.com/crossplane/crossplane/issues/3272).
- interacting with the cluster gets slower because of similar issues as the above item because of the client-side
  throttling caused by the increased number of CRDs when building the [discovery cache](https://github.com/kubernetes/client-go/blob/1517ffb8d37c99e6a3a2842bcdee0aa271f0332b/discovery/discovery_client.go)

There are currently ongoing discussion in the Crossplane community on how to mitigate these issues:

- https://github.com/crossplane/crossplane/issues/3852
- https://github.com/crossplane/crossplane/issues/2869

## Additional readings

- [The Kubernetes Discovery Cache: Blessing and Curse](https://jonnylangefeld.com/blog/the-kubernetes-discovery-cache-blessing-and-curse)
- Giant Swarm investigation on Crossplane performance issues:
    - [Impact of Crossplane on control plane nodes](https://github.com/giantswarm/roadmap/issues/2061#issuecomment-1461657937)
    - [Investigation around deleting and blocking CRDs](https://github.com/giantswarm/roadmap/issues/2061#issuecomment-1470139555)
