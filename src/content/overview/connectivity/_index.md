---
title: Connectivity
description: Public or private access to your workload applications through ingress. Secure connections between your distributed applications or microservices through a service mesh or API gateway.
weight: 70
menu:
  principal:
    parent: overview
    identifier: overview-connectivity
last_review_date: 2024-06-07
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

In today's digital landscape, efficient and secure connectivity is crucial for any enterprise. At Giant Swarm, we understand this necessity and offer a comprehensive solution designed to meet your networking needs. Whether managing public and private clusters, enforcing network policies, or routing traffic, our platform provides the tools and capabilities to ensure robust and secure connectivity.

## Capabilities

Our platform offers a range of capabilities to address your networking requirements:

- **Public and private clusters**: you can choose to make the API and ingress endpoints publicly available or close down all access to them to protect workloads and services running in your clusters.
- **Network policies**: implement granular control over the cluster network traffic by defining policies restricting or allowing communication between pods.
- **Ingress traffic management**: manage your ingress traffic using an API gateway, ingress controllers, or native load balancers to ensure reliable and efficient external traffic routing to your services.
- **Egress proxy add-on**: safeguard your outbound traffic with an egress proxy. Our system allows you to plug in your own proxy to control the egress traffic from your clusters.
- **Scalable container network**: the container network layer relies on Cilium, a high-performance container network interface that provides reliable and secure communication between pods and scales with your cluster.
- **Internal DNS**: the platform comes with CoreDNS and node local DNS as DNS solutions, which provide a flexible and scalable DNS system for efficient service discovery within your clusters.
- **Encrypted traffic**: secure your communication with mTLS (mutual Transport Layer Security) encryption, ensuring that all traffic between services is encrypted.
- **Manage your DNS configuration**: take advantage of the declarative approach to define your DNS records within the cluster, close to your services, and manage them efficiently same way you manage your other infrastructure.
- **Resilience:**: improve resilience by providing features such as circuit breakers, retries, timeouts, and rate limiting. These help in mitigating issues related to network failures and service overloads.

## Cloud-native technologies

Our platform leverages various projects under the cloud-native initiative that help us offer the aforementioned capabilities:

- **Kubernetes**: the backbone of our platform, Kubernetes give a good foundation for container communication and networking discovery.
- **Cilium**: a container network interface providing reliable and secure communication between your pods and scales with your cluster.
- **Kong**: an open-source API gateway that helps you manage your API traffic efficiently and ensures reliable external traffic routing to your services.
- **Nginx**: an ingress controller that helps to manage and route external traffic to your services with robustness and stability.
- **CoreDNS**: flexible DNS server improves service discovery within your clusters, aiding in efficient internal DNS management.
- **Node Local DNS**: an extension to CoreDNS that provides a scalable DNS solution regardless of the cluster's size. It improves the speed and reliability of DNS resolution for your workloads while reducing the load on CoreDNS.
- **External DNS**: extends Kubernetes resources, adding the option to manage DNS records for external services.

Learn how to expose your workloads on Giant Swarm by visiting our [getting started page]({{< relref "getting-started/expose-your-app/" >}}).
