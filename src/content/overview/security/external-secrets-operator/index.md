---
linkTitle: External Secrets Operator
title: External Secrets Operator
diataxis_content_type: explanation
description: What External Secrets Operator is, how it relates to SOPS, and which risks to weigh before you depend on it for cluster secrets.
weight: 60
menu:
  principal:
    parent: overview-security
    identifier: overview-security-eso
user_questions:
- What is External Secrets Operator?
- Should I use External Secrets Operator or SOPS?
- What are the risks of running External Secrets Operator?
last_review_date: 2026-08-19
owner:
- https://github.com/orgs/giantswarm/teams/team-honeybadger
---

External Secrets Operator (ESO) is a Kubernetes operator that reads secrets from an external source and delivers them securely as Kubernetes secrets for your workloads to consume.

We make ESO available on all management clusters, and also as a managed application for you to deploy on your workload clusters. To install and use it, follow [using External Secrets Operator]({{< relref "/tutorials/security/external-secrets-operator/" >}}).

ESO binds secrets into the cluster that would otherwise have required you to commit them to source control or deploy them manually. The full upstream documentation lives on [the External Secrets Operator website](https://external-secrets.io/).

## How ESO relates to SOPS

You can run ESO either alongside, or in place of, [SOPS](https://github.com/getsops/sops). There's no hard and fast rule around choosing one over the other.

Both can coexist on the same cluster, as long as the secrets they manage are independent of one another. A secret created with SOPS shouldn't be updated or managed with ESO, and vice versa. Otherwise the two tools end up fighting each other, and neither becomes the source of truth for that secret.

Do you have many secrets currently handled by SOPS? ESO can take them over, as long as it supports the provider you want to move to. SOPS works to your advantage here, because it's embedded into Flux. You can migrate gradually, without disrupting your platform.

## Risks to weigh

Every application carries risk, and the primary one here is availability. Say ESO isn't running and credentials are rotated in your secret provider. The Kubernetes secrets ESO manages no longer match the provider, so your applications may fail on deployment or when they scale.

Plan for this the way you would for any other control-plane dependency. Monitor the operator, and keep in mind that a rotation during an ESO outage is the scenario that hurts.
