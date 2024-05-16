---
title: Connectivity
description: Public or private access to your workload applications through ingress. Secure connections between your distributed applications or microservices through a service mesh or API gateway.
weight: 70
menu:
  principal:
    parent: overview
    identifier: overview-connectivity
last_review_date: 2024-05-13
owner:
  - https://github.com/orgs/giantswarm/teams/sig-product
---

<!-- OUTLINE SUGGESTION STARTS -->

In today's digital landscape, efficient and secure connectivity is crucial for any enterprise. At Giant Swarm, we understand this necessity and offer a comprehensive solution designed to meet your networking needs. Whether it's managing public and private clusters, enforcing network policies, or routing traffic, our platform provides the tools and capabilities to ensure robust and secure connectivity.

## Capabilities

Our platform offers a range of capabilities to address your networking requirements:

- **Public and private clusters**: you can either choose to have the API and/or the ingress endpoints publicly available to closing down all the access to the workloads and services running in your clusters and same time API is only accessible from your private network.
- **Network policies**: implement granular control over the cluster network traffic by defining network policies that restrict or allow communication between pods.
- **Ingress traffic management**: manage your ingress traffic using an API gateway, ingress controllers, or native load balancers to ensure reliable and efficient routing of external traffic to your services.
- **Egress proxy add-on**: safeguard your outbound traffic with an egress proxy. Our system allows to plug in your own proxy for controlling the egress traffic from your clusters.
- **Scalable container network**: the container network layer relies on Cilium, a high-performance container network interface that provides secure communication between your pods and scales reliably with your cluster.
- **Internal DNS**: the platform comes with CoreDNS as DNS solution, which provides a flexible and scalable DNS server for efficient service discovery within your clusters.
- **Encrypted traffic**: secure your communication with mTLS (mutual Transport Layer Security) encryption, ensuring that all traffic between services is encrypted.
- **Traffic management**: manage traffic routing within your clusters using service mesh technologies like Linkerd, which provide advanced features like circuit breakers, retries, timeouts, and rate limiting.
- **Resilience:**:It improves resilience by providing features such as circuit breakers, retries, timeouts, and rate limiting. These help in mitigating issues related to network failures and service overloads.

## Cloud-native technologies

Our platform leverages various projects under the Cloud Native initiative that help us offer aforementioned capabilities:

- **Kubernetes**: As the backbone of our platform, Kubernetes give robust orchestration capabilities for managing containerized workloads and services.
- **Cilium**: This container network interface provides secure communication between your pods and scales reliably with your cluster.
- **Nginx**: Ingrees controller that helps in managing your ingress traffic efficiently, ensuring reliable routing of external traffic to your services.
- **CoreDNS**: Flexible DNS server improves service discovery within your clusters, aiding in efficient internal DNS management.
- **Linkerd**: As leading service mesh options, they enhance the security, reliability, and observability of microservices communication within your clusters.

Thanks to that services Giant Swarm's platform enables robust, secure, and efficient management of your networking needs, ensuring your applications run smoothly and securely.
<!-- OUTLINE SUGGESTION ENDS-->
