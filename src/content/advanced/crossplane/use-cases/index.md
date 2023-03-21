---
linkTitle: Crossplane overview
title: Crossplane overview
description: A brief overview of Crossplane and the main features they provide.
weight: 10
menu:
main:
parent: advanced-crossplane
identifier: advanced-crossplane-overview
user_questions:
- What is Crossplane?
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2023-03-21
---

## Overview

[Crossplane](https://www.crossplane.io/) is a platform to manage - primarily - infrastructure in a Kubernetes native way.

It creates [Kubernetes Custom Resource Definitions](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/) (CRDs)
to represent the external resources as native Kubernetes objects. As native Kubernetes objects, you can use standard commands
like `kubectl create` and `kubectl describe`. The full Kubernetes API is available for every Crossplane resource.

Crossplane also acts as a Kubernetes Controller to monitor the state of the external resources and provide state enforcement.
If something modifies or deletes a resource outside of Kubernetes, Crossplane reverses the change or recreates the deleted resource.

It [officially supports](https://marketplace.upbound.io/providers?tier=official) major cloud providers like `aws`, `azure`, `gcp`.

An example of creating - and maintaining the state of - an AWS S3 bucket via the official AWS provider:

```yaml
apiVersion: s3.aws.upbound.io/v1beta1
kind: Bucket
metadata:
  name: example
spec:
  forProvider:
    region: eu-central-1
```

There are also an increasing number of [community providers](https://marketplace.upbound.io/providers?tier=community) getting available.

### Notable features

- [Provider Configs](https://docs.crossplane.io/v1.11/concepts/providers/#configuring-providers) is an excellent way to
  manage the actor (access keys, roles, identities) handling given resources down to the individual level
- [Composite Resources](https://docs.crossplane.io/latest/concepts/composition/) is collection of other resources that can be offered by your devops team
  to developers to make it easier to bring up common infrastructure for application

## Architecture

Crossplane itself is a core set of [Kubernetes operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/)
that managed so called `providers`.

Providers are the cloud provider specific extensions to core Crossplane that offer a set of Kubernetes CRDs that
describe cloud resources as Kubernetes CRDs and the operators to create, update, maintain the state and delete these resources.

Giant Swarm offers experimental, [managed application](https://github.com/giantswarm/crossplane/) for core Crossplane,
and supports managed solutions for running the following Crossplane `providers` on management clusters:

- the [official AWS provider](https://marketplace.upbound.io/providers/upbound/provider-aws/latest)
- the [official Azure provider](https://marketplace.upbound.io/providers/upbound/provider-azure/latest)
- the [official GCP provider](https://marketplace.upbound.io/providers/upbound/provider-gcp/latest)
