---
title: Continuous deployment
description: Continuous deployment and GitOps capabilities for deploying and upgrading your applications and clusters efficiently.
weight: 50
menu:
  principal:
    parent: overview
    identifier: overview-continuous-deployment
last_review_date: 2026-06-22
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
user_questions:
  - What is Continuous Deployment?
  - How does Giant Swarm support Continuous Deployment?
---

Continuous Deployment (CD) is a **key practice** in modern software development. It lets teams deliver features, fixes, and updates to their users **fast and reliably**. Giant Swarm has built a platform around this capability. With it, you can deploy changes to your applications **seamlessly**, while keeping high quality and security standards.

## Capabilities

- **Pull-based deployments**: The platform follows the GitOps method, which uses a **pull-based approach** to manage application deployments. This way, the desired state of the infrastructure is always reflected in the deployed applications. It promotes cost efficiency, scalability, and security.

- **Secret management**: Managing sensitive information such as API keys, passwords, and certificates is **critical** to modern application deployment. Our platform relies on an External Secrets Operator (ESO), which integrates with many secret management solutions. It makes sure secrets are **securely stored and injected** into applications, keeping sensitive data confidential and intact.

- **Infrastructure as Code**: Infrastructure as Code (IaC) is a **pivotal practice** for automating how you provision and manage infrastructure through code. With the platform, teams define, provision, and manage cloud infrastructure and services **declaratively**. This promotes consistency, repeatability, and scalability, which makes teams more efficient and effective.

## Cloud-native technologies

- **FluxCD**: FluxCD implements the GitOps method. It enables continuous deployment by **automatically synchronizing** Git repositories with Kubernetes clusters. The desired state defined in Git is always reflected in the deployed infrastructure and applications, which gives you a **reliable and secure** way to manage deployments.

- **Flux Operator**: An open-source operator that extends Flux with **self-service capabilities**, deployment windows, and preview environments for testing GitHub, GitLab, and Azure DevOps pull requests.

- **External Secrets Operator**: An open-source operator that integrates with various secret management solutions, such as AWS Secrets Manager, Azure Key Vault, and Hashicorp Vault. ESO retrieves secrets from these external sources and injects them into Kubernetes secrets. This enables **secure and dynamic** secret management in cloud-native environments.

- **Crossplane**: Crossplane lets you manage infrastructure and services using **Kubernetes-native APIs**. It supports the declarative management of cloud resources, which makes it easier to implement Infrastructure as Code (IaC) practices. Crossplane integrates seamlessly with existing Kubernetes workflows, giving you a **unified approach** to managing applications and infrastructure.

Learn how to start with continuous deployment on Giant Swarm by visiting our [getting started continuous deployment page]({{< relref "/getting-started/install-an-application/" >}}).
