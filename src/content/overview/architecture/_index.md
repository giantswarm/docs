---
title: Architecture of the Giant Swarm cloud-native developer platform
linkTitle: Architecture of the platform
description: Components, capabilities, supported cloud providers, and the platform API.
weight: 20
menu:
  principal:
    parent: overview
    identifier: overview-architecture
user_questions:
  - What is the architecture of the Giant Swarm cloud-native developer platform?
owner:
  - https://github.com/orgs/giantswarm/teams/team-planeteers
last_review_date: 2024-11-04
---

Giant Swarm's cloud-native developer platform integrates open-source components that work together to provide a seamless experience for managing the lifecycle of containerized applications. The platform is based on Kubernetes and designed to be cloud-agnostic, allowing you to deploy your applications on any of the supported cloud providers, including on-premises. The interfaces allow development teams and automations to deploy applications, keep the clusters secure, and use other capabilities that we explain below. On top, you benefit from our strong support model that ensures your long-term success and stability of workloads.

## Platform architecture

![Platform architecture](./platform-architecture.png)

The platform architecture consists of the following layers:

- Interface layer: offers a set of templates, APIs, and tools that developers can use to interact with the platform.

- Capabilities layer: provides a set of capabilities to manage the lifecycle of applications, including deploying, scaling, and monitoring applications.

- Infrastructure layer: responsible for managing the underlying infrastructure, including the cloud provider resources or on-premises infrastructure. To abstract the underlying infrastructure, the platform uses the `Kubernetes`.

Along these layers, Giant Swarm provides a real support channel, incident management, and good documentation to help you get the most out of the platform. Additionally, you have a dedicated account engineer to help creating a common roadmap and to provide guidance on how to use the platform.

## Platform API

The Giant Swarm platform is build on top of `Kubernetes` thanks to [`Cluster API`](https://cluster-api.sigs.k8s.io/), a open source  project that standardize the cluster lifecycle management across different cloud providers or on-premises infrastructure.

The Platform API is the regular Kubernetes API of your central _management cluster_ and is your interface for deploying workload clusters and applications, or to reach other capabilities such as the observability and security dashboards.

In Giant Swarm, the management cluster is also used for enhancing the platform capabilities, such as monitoring, logging, and alerting. The customer platform team uses the management cluster to configure which capabilities are available to the developers, and even to create new capabilities.

Most often, you have a single management cluster that manages multiple workload clusters, but in case of running infrastructure in multiple regions, you can have multiple management clusters. The platform API isn't more than the `Kubernetes` management cluster API, but with some additional resources that allow you to manage the lifecycle of your workloads across multiple clusters or inspect the application metrics of your fleet of clusters.

[Learn how to access the platform API]({{< relref "/getting-started/access-to-platform-api" >}}).

## GitOps

Giant Swarm uses GitOps as first-class citizen to manage the lifecycle of cluster and applications. It's modern operational framework which allow managing our resources using `Git` repositories as the single source of truth. In the platform, GitOps ensures that all changes are version-controlled, auditable, and easily reversible. By leveraging Git’s robust workflows, teams can automate deployments and rollbacks while maintaining consistency and reliability across environments. This capability empowers developers to implement continuous delivery practices, facilitating faster and more secure releases.

[Learn more in our guide about GitOps]({{< relref "/tutorials/continuous-deployment" >}}).

## Developer portal

Giant Swarm uses [Backstage](https://www.cncf.io/projects/backstage/) as developer portal serving as the central hub for accessing all platform services and resources. It provides an intuitive interface where platform engineers and developers find documentation, manage their projects, and access tools necessary for application development and deployment. By consolidating resources and simplifying access, you developer portal enhances the user experience, reduces onboarding time, and fosters collaboration among teams. It acts as the gateway to the platform’s capabilities, streamlining workflows and promoting productivity.

## Observability

Observability on the Giant Swarm platform is based in Mimir, Loki and Grafana. The stack runs in the management cluster and provides a centralized view of the platform metrics, logs, and traces. You can add application metrics and logs letting the your teams detect anomalies, troubleshoot issues, and optimize resources efficiently. The platform supports customizable dashboards and alerts, enabling proactive management and a deeper understanding of application behavior and infrastructure status.

## Single sign-On

Single Sign-On (SSO) simplifies user authentication across the Giant Swarm platform by allowing users to access multiple services with your existing identity provider. It enhances security and user convenience by reducing password fatigue and centralizing identity management. You can build on top of `Kubernetes` Role-Based Access Control (RBAC) to define fine-grained access policies and permissions, ensuring that only authorized users can interact with the platform resources.

## Network and connectivity

The different technologies used in the Giant Swarm platform provides you with a secure and reliable network and connectivity between your applications and services. Platform engineers can create network policies to control traffic flow and enforce security rules, ensuring that data is protected and isolated. Relying on the built-in networking capabilities of `Kubernetes`, the platform supports many routing and load balancing strategies, enabling seamless communication between services and applications.

## Runtime security

Runtime security focuses on protecting applications and infrastructure during execution. [Falco](https://www.cncf.io/projects/falco/) project provide you with intrusion detection, vulnerability scanning, and automated threat response capabilities. The Giant Swarm platform ensures that security policies are enforced consistently, reducing the attack surface and mitigating risks.

## Cost management

Cost control is becoming increasingly important as organizations seek to optimize their cloud spending. Based on lessons learned from our experience with customers, the platform is built to help you manage costs effectively. Our solution engineers will help you to add visibility and control over your resource usage and expenses, leading to better decision-making and cost savings.

## Automatic cluster management

Leaning on the `Cluster API`, the Giant Swarm platform provides solid automation to manage the lifecycle of your clusters. On top, our team has developed additional logic cover certain aspects of the cluster lifecycle not included in the upstream project.

Our system includes automated provisioning, scaling, and upgrading of clusters, reducing the operational burden on your team. The platform ensures clusters are always running optimally and securely, allowing developers to focus on building and deploying applications without worrying about underlying infrastructure management.

## Cluster Scaling

One of the key features of the Giant Swarm platform is the ability to scale clusters automatically. It allows for dynamic adjustment of resources based on demand, supporting both horizontal and vertical scaling, ensuring applications have the necessary resources to handle varying workloads. By automating the scaling process, the platform helps maintain performance and reliability while optimizing resource utilization and cost.

## Cloud resources provisioning

Most likely, you have already external cloud resources which could be managed by the platform. Thanks to [Crossplane](https://www.cncf.io/projects/crossplane/) project, you can include all your infrastructure, such as databases, queues or buckets, as part of the platform, relying on the same principles `Kubernetes` offers. Centralizing the management of all the infrastructure in a single place, helps you to reduce the operational overhead and to have a better control over your resources.
