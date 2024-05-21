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

<!-- OUTLINE SUGGESTION STARTS -->
Security is paramount for any organization, especially those running workloads in the fast-paced cloud-native space. As you will see, Giant Swarm prioritizes security at every platform layer. The security features ensure that your applications and data are protected against threats, comply with industry standards, and maintain integrity throughout their lifecycle. This overview will detail the capabilities of our security offerings and the cloud-native technologies that enable them.

## Capabilities

- **Policy enforcement**: Implement fine-grained security policies to control and restrict resource access. It includes Role-Based Access Control (RBAC), network policies, and Pod Security Standards (PSS) to ensure that only authorized users and approved applications can run on the platform.

- Image scanning and provenance: Ensure the safety and integrity of container images by scanning them for vulnerabilities using tools like Clair or Trivy, and verifying their provenance by checking their source and history before deployment. This helps to prevent the use of compromised or malicious images in your environment, thereby reducing the risk of security threats.

- **Cloud security posture**: Maintain a strong security posture by continuously monitoring your cloud infrastructure for compliance with security best practices and standards. Identify and remediate misconfigurations and vulnerabilities to reduce the attack surface.

- **Runtime anomalies**: Detect and respond to abnormal behavior during runtime, which refers to any action detected that deviates from the expected or normal operation of the system. This includes monitoring for unusual activity, such as unexpected process executions, file system changes, and network connections, which could indicate a security breach or unauthorized access.

- **Log alerting**: Enhance visibility and awareness by setting up alerts based on log data. It enables timely detection and response to security incidents, promptly addressing suspicious activity.

- **Advanced network capabilities**: Protect data in transit with advanced network security features, including internal traffic encryption. Implement mutual TLS (mTLS) for service-to-service communication to ensure that data is always encrypted and authenticated.

## Cloud-Native technologies

Our platform leverages several cloud-native technologies to deliver these security capabilities:

- **Kyverno**: Facilitates policy enforcement by allowing you to define and enforce fine-grained security policies across all your clusters.

- **Trivy and Sigstore**: Rely on our ready-to-use apps to provide image scanning and provenance, ensuring that container images are free from vulnerabilities and their sources are verified.

- **Falco**: An open-source runtime security project, Falco monitors your Kubernetes environment for runtime anomalies, providing real-time detection of suspicious activities.

- **Prometheus and Grafana**: Used for log alerting and monitoring, Prometheus collects and stores metrics, while Grafana provides a customizable dashboard for visualizing and setting up alerts based on these metrics.

- **Cilium**: These container networking solutions provide advanced network capabilities, including network policies and internal encryption to secure communication within your clusters.

Learn how to start with Security on Giant Swarm by visiting our [getting started security page]({{< relref "overview/security/platform-security/" >}}).

<!-- OUTLINE SUGGESTION ENDS-->