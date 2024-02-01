---
linkTitle: The new Cluster API
title: The new Cluster API
description: Benefits of the new Cluster API (based on CAPI)
weight: 5
menu:
  main:
    parent: advanced-cluster-management
user_questions:
  - What kind of changes are coming with the new Cluster API (CAPI)?
  - What are the benefits of Cluster API (CAPI)?
last_review_date: 2024-01-26
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

{{< platform_support_table aws="ga=v21.0.0,ga=v21.0.0" azure="ga=v21.0.0" >}}

## Embracing Kubernetes Cluster API

### A Journey to a Unified Cluster Management Platform

Two years ago, we embarked on a significant journey to transition our Kubernetes cluster management infrastructure from our own custom operators to the upstream Cluster API (CAPI) implementation. This decision was driven by a number of compelling factors, including the broader adoption and development of CAPI within the Kubernetes community, its ability to provide greater flexibility and configurability, and its commitment to future-proofing our platform.

## Motivations for Transitioning to CAPI

 * **Community-Driven Development**: CAPI is a widely adopted and actively developed project within the Kubernetes community. By embracing CAPI, we benefit from the collective expertise of many contributors, ensuring the continued advancement and reliability of our cluster management solution.
 * **Vendor-Neutrality and Future-Proofing**: CAPI adheres to a neutral and open API, shielding our customers from vendor lock-in and ensuring their ability to seamlessly integrate with the evolving cloud landscape. This open approach also facilitates faster innovation and integration with new technologies.
 * **Greater Flexibility and Customization**: CAPI provides a more expressive and flexible API for defining and managing Kubernetes clusters. With CAPI, we can cater to diverse customer requirements, enabling them to deploy into existing infrastructure and customize cluster configurations to suit their specific needs.
 * **Expanded Tooling Ecosystem**: CAPI is compatible with a vast array of tools and solutions developed by the community. By adopting CAPI, we gain access to a rich toolkit for cluster management, automation, and orchestration.

## Benefits of CAPI

* **Enhanced Flexibility**: CAPI empowers us to provide our customers with greater control over their infrastructure, enabling them to deploy into existing networks, customize cluster configurations, and integrate with a wider range of infrastructure providers.
* **Future-Proofed API**: CAPI's open and vendor-neutral API ensures our platform's viability in the long term, allowing us to adapt to evolving cloud architectures and technologies without being constrained by proprietary solutions.
* **Broad Tooling Compatibility**: Leveraging CAPI allows us to leverage a multitude of tools developed by the community, enhancing our ability to automate, manage, and orchestrate Kubernetes clusters effectively.
* **Support for Managed Control Planes**: CAPI enables us to seamlessly integrate with managed control planes like EKS and AKS, providing customers with a choice of deployment options.
* **Simplified Provider Addition**: CAPI's composable architecture makes it easier to add new infrastructure providers, expanding our offerings beyond AWS, Azure, and our current on-premises solutions.
* **Multi-Cloud Capabilities**: CAPI supports managing workload clusters from multiple providers under a single management cluster, enabling true multi-cloud deployment scenarios.

## Differences between CAPI and Legacy Cluster Management

The transition to Kubernetes Cluster API (CAPI) introduces several noteworthy differences compared to our legacy cluster management infrastructure. These changes aim to enhance flexibility, expand tooling compatibility, and streamline cluster management operations.

### Cluster CRs Packaged as Helm Charts

CAPI-based cluster configuration is now encapsulated within Helm charts, providing a more controlled and maintainable approach. This approach offers several benefits:

* **Limited Configuration Exposure:** Only tested and stable configuration options are exposed, ensuring a consistent and reliable cluster experience.

* **Ease of Configuration Enabling:** Most CAPI features can be easily enabled by updating the Helm chart, enabling rapid adoption of new capabilities.

* **Inspectable Cluster Assembly:** The Helm chart details clearly outline how the cluster is assembled, providing transparency and diagnostic capabilities.

* **Documented Configuration Options:** Comprehensive documentation is provided as part of the JSON schema, ensuring easy understanding and reference.

* **Happa UI-Based Cluster Creation:** The Happa UI streamlines cluster creation from the JSON schema, enhancing user experience.

### Configurable Registries with Credentials and Mirrors

CAPI enables the flexibility to specify custom registries with credentials and mirrors, allowing customers to utilize their preferred container repositories. This flexibility enhances the portability and adaptability of customer environments.

### Removal of Cluster Management Operators

The legacy cluster management operators have been removed due to several limitations and drawbacks:

* **Incompatibility with Multi-Version CAPI:** Upstream CAPI doesn't support running multiple versions of operators on the same management cluster, creating operational challenges.

* **Lack of On-Demand Updates:** Operator bug fixes required a full release and upgrade cycle for both GS and customers, hindering timely remediation.

CAPI addresses these limitations with a new approach:

* **Cross-Version Compatibility:** New operator versions can manage all previously provisioned clusters, ensuring ongoing support for existing deployments.

* **On-Demand Upgrades:** Cluster upgrades are triggered explicitly per cluster, preventing unplanned or unintended upgrades.

* **Enhanced Testing for Operators:** Thorough testing ensures the quality and reliability of the operators.

### Flexible Network Configuration

CAPI introduces greater flexibility in defining network configurations, allowing for more granular control over cluster topology:

* **Similar Defaults to Vintage:** The default network setup aligns with the familiar Vintage approach.

* **Separate Subnets for Key Components:** The API Load Balancer (LB), Ingress LB, control plane nodes, and worker nodes can be deployed on distinct subnets, enhancing isolation and security.

* **Transit Gateway Support**

CAPI fully integrates with Transit Gateway, enabling seamless connectivity across multiple AWS accounts and regions. This flexibility expands the range of deployment options.

### Removal of Initiator App

The legacy Initiator app has been removed due to its limitations and potential security risks. Cluster configuration is now solely managed through the configurable options provided by the `cluster-aws` Helm chart. This approach ensures better testing and quality control.

### Private Clusters with Limitations

CAPI supports private clusters with the following limitations:

* **Private Kubernetes API LB:** The Kubernetes API LB can be configured to be private, restricting external access.

* **No Bastion Hosts:** Bastion hosts are no longer used for secure access to private clusters.

* **HTTP/HTTPS Proxy Required:** A HTTP/HTTPS proxy is necessary for communication with the CAPA API.

### Teleport for Secure Cluster Access

CAPI introduces Teleport as the primary method for secure cluster access, replacing bastion hosts. Teleport offers several advantages:

* **Removal of Bastion Hosts:** Bastion hosts are no longer required, reducing attack surfaces and simplifying security management.

* **SSH and kubectl Audit Logs:** Session recording capabilities for SSH and kubectl commands provide comprehensive audit logs.

* **SSO for SSH and Kubernetes API Access:** Single sign-on (SSO) simplifies access and enhances security.

* **Private Cluster Enablement:** Teleport enables private clusters without publicly exposed endpoints.

* **Reduction in VPN Usage:** GS VPN may no longer be needed, except for Grafana, Prometheus, and Happa (if deployed externally).

### Cluster IP CIDRs Manually Allocated

In CAPI, cluster IP CIDRs are manually allocated to new clusters, allowing for more controlled assignment of network resources.

### Multi-Region MCs and IAM Role Access

CAPI supports multi-region management clusters, enabling the creation of clusters in multiple AWS regions. Additionally, IAM roles can be used to delegate access across AWS accounts, streamlining access management for large deployments.
