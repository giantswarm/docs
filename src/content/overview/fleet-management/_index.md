---
title: Fleet management
description: Supported cloud providers and management of clusters on the Giant Swarm platform.
weight: 40
menu:
  principal:
    parent: overview
    identifier: overview-fleet-management
last_review_date: 2024-05-10
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Based on our extensive experience, we understand that orchestrating a large-scale microservices platform poses significant challenges. Ideally, workloads should be designed for seamless execution in the cloud, tailor-made to optimize the container lifecycle. However, the task becomes exponentially more complex when juggling multiple providers, regions, and environments. Recognizing this, we've developed several abstraction layers to help streamline management and tackle this complexity more effectively.

## Features

Our product is designed to offer a comprehensive set of features to support the construction of robust Cloud Native Platforms. Key features include:

- **Multi-Environment Support**: Every enterprise has unique requirements and constraints, influencing how they design their developer platforms. Platform engineers often struggle to align their organization's structure and processes with the platform while maintaining the system's ability to foster speed and quality, all in compliance with company standards. Our solution, Giant Swarm, simplifies this process. It empowers you to provide developers with various environments, across different regions and providers, tailored to your organization's needs.

- **Robust Configuration Management**: Manage your clusters, environments, and workloads with flexibility and precision using our robust configuration management framework. This framework facilitates structured platform configuration with multiple layers of control, all from a single repository. It's crafted to adhere to the principles of GitOps, ensuring seamless and efficient management.

- **Standardized Cluster Lifecycle Management**: Experience a standardized approach to managing the lifecycle of your clusters. Developed in collaboration with the community, Giant Swarm offers a cloud-native solution for cluster lifecycle management. We leverage the Cluster API implementation to streamline lifecycle management, enabling versioning and configuration of clusters as code, thus ensuring consistency and reliability.

## Cloud-native applications

The platform is heavily relying on [Cluster API implementation]({{< relref "/overview/fleet-management/introduction_cluster-api" >}}) to manage the lifecycle of your clusters. It opens up the possibility to manage your clusters in many providers adapting to the infrastructure nuances of each solution while keeping a consistent experience for the user.

Every company requires a different level of control over their infrastructure and its configuration. We work with upstream to offer you a platform that is compliant with all the standards and processes your company imposes.
