---
title: Fleet management
description: Supported cloud providers and management of clusters on the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview
    identifier: overview-fleet-management
last_review_date: 2024-06-03
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Based on our extensive experience, we understand that orchestrating a large-scale microservices platform poses significant challenges. Ideally, workloads should be designed for seamless execution in cloud and containers. However, this becomes exponentially more complex when juggling multiple infrastructure providers, regions, clusters and environments.

With such complexity, you need to streamline the management of your platform in a declarative and simplified way. You will want to manage your fleet coherently and transparently, relying on capabilities that help you define standards and implement governance globally.

Recognizing this, we've developed abstractions to help manage and tackle this complexity effectively.

## Capabilities

Our product is designed to offer a comprehensive set of features to support the construction of robust cloud-native platforms. Key features include:

- **Multi-environment support**: Every enterprise has unique requirements and constraints, influencing how they design their developer platforms. Platform engineers often struggle to align their organization's structure and processes with the platform while maintaining the system's ability to foster speed and quality, all in compliance with company standards. Our solution, the Giant Swarm platform, simplifies this process. It empowers you to provide developers with various environments, across different regions and infrastructures, flexibly adapted to your organization's needs.

- **Robust configuration management**: Our bullet-proof configuration management system allows you to manage your clusters, environments, and workloads with flexibility and precision. The system facilitates structured platform configuration with multiple control layers, all from a single repository. It's crafted to adhere to the principles of GitOps, ensuring seamless and efficient management.

- **Standardized cluster lifecycle management**: Experience a standardized approach to managing your clusters' lifecycle. Giant Swarm leverages the Cluster API implementation, a Kubernetes sub-project developed by the open-source community, which includes Giant Swarm engineers as regular contributors. Giant Swarm adds enterprise-grade features, an out-of-the-box configuration, and a battle-tested versioned package that provides all the base functionality a production-ready cluster needs. This allows consistent and reliable cluster lifecycle management, enabling versioning and configuring clusters as code.

## Cloud-native technologies

Our solution is built on top of cloud-native technologies and best practices. We leverage [Kubernetes](https://kubernetes.io/docs/concepts/overview/), the de facto standard for container orchestration, to provide a robust and scalable platform for your workloads. At the same time, Kubernetes is cloud-agnostic, allowing us serve the same interfaces to target multiple cloud providers. For managing the cluster lifecycle, as we mentioned above, we rely on [Cluster API]({{< relref "/overview/fleet-management/cluster-management/introduction-cluster-api" >}}) since it's a Kubernetes sub-project driven by the community in order to bring declarative, Kubernetes-style APIs to cluster creation, configuration, and management.

On the other side we run [Flux](https://www.giantswarm.io/blog/gitops-with-flux-giant-swarm) to bring GitOps to the platform. Giant Swarm has built a convention to help you manage all your infrastructure and configuration in a single source of truth. Enjoy the benefits of a fully automated and auditable platform, where changes are made through pull requests and automatically applied to your clusters and applications.
