---
title: Security
description: Security features and tooling integrated with the Giant Swarm platform.
weight: 60
menu:
  principal:
    parent: overview
    identifier: overview-security
last_review_date: 2024-05-21
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

Security is paramount for any organization, especially those running workloads in the fast-paced cloud-native space. Giant Swarm clusters follow a secure-by-default ideology, meaning every cluster starts with a production-ready security posture.

The platform's security features ensure that your applications and data are protected against threats, comply with industry standards, and maintain integrity throughout their lifecycle. This overview details the capabilities of our security offerings and the cloud-native technologies that enable them.

## Capabilities

- **Policy enforcement**: Implement fine-grained security policies to restrict resource access and prevent running risky workloads. This includes native Kubernetes Role-Based Access Control (RBAC), Network Policies, and Pod Security Standards (PSS), as well as platform support for a vast range of optional and custom policies.

- Image scanning and provenance: Ensure the safety of container images by scanning them for vulnerabilities, identifying improperly handled secrets, and verifying the authenticity and integrity of the image before deployment. This helps to prevent the use of compromised or malicious images in your environment, thereby reducing the risk of security threats.

- **Runtime anomalies**: Detect and respond to abnormal behaviour during runtime. This includes monitoring for unusual activity, such as unexpected process executions, file system changes, network connections, or other events that deviate from the expected or regular operation of the system and could indicate a security breach or unauthorized access.

- **Log alerting**: Enhance visibility and awareness by setting up alerts based on log data. It enables timely detection and response to security incidents, addressing suspicious activity.

- **Advanced network capabilities**: Protect data in transit with advanced network security features, including internal traffic encryption. Implement mutual TLS (mTLS) for service-to-service communication to ensure that data is always encrypted and authenticated.

## Cloud-Native technologies

Our platform leverages several cloud-native technologies to deliver these security capabilities:

- **Kyverno**: Facilitates policy enforcement by allowing you to define and enforce fine-grained security policies across all your clusters. Prevent unsafe configuration, require organization-specific best practices, and enforce supply chain security policies like image signature verification before admitting an image to the cluster.

- **Trivy**: Scans workloads (and more) for vulnerabilities, exposed secrets, insecure configurations, and performs various types of benchmarks to provide visibility into the cluster and all of its workloads.

- **Falco**: An open-source runtime security project, Falco monitors your Kubernetes environment for runtime anomalies, providing real-time detection of suspicious activities.

- **Prometheus and Grafana**: Used for log alerting and monitoring, Prometheus collects and stores metrics, while Grafana provides a customizable dashboard for visualizing and setting up alerts based on these metrics.

- **Cilium**: Container networking plugin that provides advanced network capabilities, including DNS-based network policies and traffic encryption to secure communication within your clusters.

Learn how to start with Security on Giant Swarm by visiting our [getting started security page]({{< relref "platform-overview/security/platform-security/" >}}).
