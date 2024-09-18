---
title: Continuous deployment
description: Continuous deployment and GitOps capabilities for deploying and upgrading your applications and clusters efficiently.
weight: 50
menu:
  principal:
    parent: overview
    identifier: overview-continuous-deployment
last_review_date: 2024-06-03
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

Continuous Deployment (CD) is a crucial practice in modern software development, enabling teams to deliver features, fixes, and updates to their users fast and reliably. Giant Swarm has designed a platform that embraces this capability to allow customers to deploy changes to their applications seamlessly, maintaining high quality and security standards.

## Capabilities

- **Pull-based deployments**: It follows the GitOps methodology, which leverages a pull-based approach for managing application deployments. This method ensures that the desired state of the infrastructure is always reflected in the deployed applications, promoting cost efficiency, scalability, and security.

- **Secret management**: Managing sensitive information such as API keys, passwords, and certificates is critical to modern application deployment. Our platform relies on an External Secrets Operator (ESO), which integrates with many secret management solutions to ensure that secrets are securely stored and injected into applications, maintaining the confidentiality and integrity of sensitive data.

- **Infrastructure as Code**: Infrastructure as Code (IaC) is a pivotal practice in automating the provisioning and management of infrastructure through code. By leveraging the platform for defining, provisioning, and managing cloud infrastructure and services declaratively, teams are empowered with the tools to promote consistency, repeatability, and scalability, enhancing their efficiency and effectiveness.

## Cloud-Native Technologies

- **FluxCD**: It implements the GitOps methodology, allowing continuous deployment through automated synchronization of Git repositories with Kubernetes clusters. It ensures that the desired state defined in Git is always reflected in the deployed infrastructure and applications, providing a reliable and secure way to manage deployments.

- **External Secrets Operator**: This is an open-source operator that integrates with various secret management solutions, such as AWS Secrets Manager, Azure Key Vault, and HashiCorp Vault. ESO retrieves secrets from these external sources and injects them into Kubernetes secrets, enabling secure and dynamic secret management in cloud-native environments.

- **Crossplane**: It enables the management of infrastructure and services using Kubernetes-native APIs. It supports the declarative management of cloud resources, facilitating the implementation of Infrastructure as Code (IaC) practices. Crossplane allows seamless integration with existing Kubernetes workflows, providing a unified approach to managing applications and infrastructure.

Learn how to start with continuous deployment on Giant Swarm by visiting our [getting started continuous deployment page]({{< relref "getting-started/install-an-application/" >}}).
