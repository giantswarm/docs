---
title: Cluster naming
description: The specifications for naming workload clusters in the Giant Swarm platform.
weight: 10
menu:
  principal:
    parent: overview-fleet-management-cluster-concepts
    identifier: overview-fleet-management-cluster-concepts-naming
last_review_date: 2024-06-14
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are the main concepts of cluster management in the Giant Swarm platform?
---

When creating a new workload cluster in the Giant Swarm platform, you need to choose a name. We recommend you choose a naming scheme that suits your organization and stick to it. This helps you and your team members quickly identify clusters and avoid confusion.

There are some rules and recommendations for naming clusters:

- The maximum cluster name length is 20 characters.
- Letters, digits and dashes are allowed. Dashes are not possible at the beginning or end. For example, `dev-eu-central-1-a`, `dev-a`, `prod-b`, `e-commerce-dev-eu`, `prod-us` or `staging01` are all valid names.
- The cluster name will be part of domain names like `api.<cluster name>.<base domain>` (for instance: `api.mycluster.eu-west-1.aws.gigantic.io` or `ingress.mycluster.mycompany.com`). Since DNS records can normally be resolved publicly by anyone, you should avoid encoding sensitive information into the cluster name (`mycluster` in our examples).
- You cannot rename clusters after creation.
- Keep cluster names unique across your whole company for these reasons:
    - All workload cluster names must be unique within one management cluster, even across namespaces. This allows the tooling and operators to look up workload clusters by their names without the chance of confusion.
    - Multiple management clusters can share the same base domain, so workload cluster names should be unique across your company since their domains would otherwise clash.
    - Using identical workload cluster names creates problems and risks. Imagine asking for support or trying to resolve an incident, and Giant Swarm or your team members confuse two clusters of the same name. Hence, cluster names should be unique, easily spellable, and pronounceable by humans – for example, during incident calls and in chat – and follow a somewhat consistent naming scheme.
- When using CLI plugin it is recommended specifying a cluster name explicitly using the `--name` parameter, as in the below instructions. If you really want a randomly generated name, you can use `--generate-name` instead.
