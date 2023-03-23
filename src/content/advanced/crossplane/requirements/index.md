---
linkTitle: Crossplane requirements
title: Crossplane requirements
description: Crossplane requirements
weight: 20
menu:
main:
parent: advanced-crossplane
identifier: advanced-crossplane-requirements
user_questions:
- What are the requirements for Crossplane?
- What are the risks of using Crossplane?
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-03-21
---

## Requirements

Crossplane has a significant impact on the management cluster, greatly depending on the used `provider(s)`.

### Deploying thousands of CRDs

Managing cloud providers resources via Kubernetes CRs is one of the best thing of Crossplane, but also causes a lot of
issues in its current state, because most cloud providers impose hundreds of new CRDs to the management cluster:

- official AWS provider `v0.31.0` has `894` CRDs
- official Azure provider `v0.29.0` has `705` CRDs
- official GCP provider `v0.29.0` has `894` CRDs
