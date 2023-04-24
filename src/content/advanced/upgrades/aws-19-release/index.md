---
linkTitle: Giant Swarm Release v19.0.0 for AWS
title: Giant Swarm Release v19.0.0 for AWS
description: AWS release v19 besides many improvements will introduce migration of Cilium as well as replacement of kiam with IRSA. Following handbook should be carefully read by customers upfront the upgrade to prepare the clusters and workloads accordingly.
weight: 10
menu:
  main:
    parent: advanced-upgrades
aliases:
  - /guides/aws-release-v19/
user_questions:
  - Where can I read about v19 changes?
  - What does v19 change?
  - What changes does Cilium bring?
  - What do i have to prepare for v19?
  - Whad do i have to do before IRSA migration?
  - How does the Cilium migration work?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-04-13
---

{{< platform_support_table aws="alpha=v19.0.0" >}}

## Introduction

We have been preparing for a long time to introduce release v19 on AWS. Besides upgrade of components and Kubernetes version to 1.24, this release will involve two major changes for customers, namely the migration from the AWS VPC CNI to Cilium and the replacement of Kiam with IAM Roles for Service Accounts(IRSA) for authenticating pods against the AWS API.
Next sections are describing important changes we will introduce with the new release, the key benefits, what customers can do to prepare and how to avoid downtime during this crucial upgrade. 

## Cilium

Say goodbye to slow network initialization times and hello to lightning-fast performance with [Cilium](https://github.com/cilium/cilium), our new Kubernetes CNI solution!

### Key Highlights

- Service Mesh integration: `Cilium` is designed to work seamlessly with popular service meshes like `Istio`, `Linkerd`, and `Envoy`. This allows for more advanced networking and security features, such as mTLS encryption and observability.
- `Cilium` uses a virtual network which provides more flexibility, faster network initialization, and more advanced networking features compared to `AWS CNI` affecting the IP addresses.
- Advanced networking features: `Cilium` supports advanced networking features such as load balancing, network segmentation, and eBPF-based packet filtering. These features allow for more granular control over network traffic and improve security. 
- Scalability: `Cilium's` eBPF-based data plane is highly scalable and performs well even at scale. It is also highly efficient, reducing overhead and maximizing performance.

### What changes with Cilium?

With `Cilium`, you'll no longer be using the `AWS CNI` Pod subnets, so be sure to add custom routes with the `Node subnet(s) CIDR(s)` instead. 

Additionally, while `Cilium's Network Policy` provides powerful security features, support for setting `ipBlock` with `Pod IPs` is not implemented in Cilium, so be sure to inspect your workloads and configure `Network Policies` carefully. The Account Engineers will reach out to you and help to provide the `CiliumNetworkPolicies` before the upgrade in order to have no downtime during the switch. [Cilium-prerequisites](https://github.com/giantswarm/cilium-prerequisites) app that installs the `CiliumNetworkPolicy` CRD is available in the catalog as well as will be installed with GS version `v18.4.0` to provide seemless upgrade experience.

It's important to note that due to changes to `Cluster CR's` during the upgrade process, `GitOps` automation will have to be suspended and any applied changes backported to the repos before resuming. Keep this in mind as you prepare for the upgrade. This needs to be evaluated on a case-by-case basis, since different GitOps implementations might only keep _some_ parts of `Cluster` CRs in Git. Feel free to reach out to your Account Engineer to understand more about these changes.

To ensure a smooth transition to `Cilium`, we've prepared a [comprehensive upgrade process](https://handbook.giantswarm.io/docs/support-and-ops/ops-recipes/upgrade-to-cilium/) that explains every migration step in detail, so you can feel confident in following the process and avoid any potential issues.

#### Cilium and AWS Load Balancer Controller

If you are running `aws-load-balancer-controller` inside your clusters for managing [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) and you did set the annotation `service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: ip`, you need to change it to `service.beta.kubernetes.io/aws-load-balancer-nlb-target-type: instance`.

For further information, please checkout the [documentation](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/service/annotations/#traffic-routing)

#### Cilium and pod CIDR

While switching to Cilium we are forced to change the CIDR used to assign IPs to Pods (192.168.0.0/16 by default).
The process is automated for the vast majority of the clusters, but if you had set up custom networking settings in your cluster the upgrade might be blocked by admission controllers. If that is the case, reach out to your SA and you'll receive guidance how to move on with the upgrade. Same thing applies uf you don't want to stick with the default value and prefer to change it.

## IAM roles for service accounts (IRSA)

By switching from `KIAM` to `IAM Roles for Service Accounts (IRSA)`, we're making it easier and more secure for your Kubernetes workloads to interact with AWS services. 

### Key Highlights

- Official AWS way to authenticate pods to AWS API.
- Reduced complexity: IRSA eliminates the need for a separate service like KIAM, streamlining your Kubernetes clusters.
- Regional STS (Security Token Service) rather than using global STS

### What changes with IRSA?

During the upgrade, we are removing `KIAM` as a default app in your workload clusters but it is possible to install it optionally. If you need to keep using KIAM in v19 clusters, please reach out to your SA.

Additionally, we are creating a `Cloudfront Domain Alias` (except China) for each cluster which is used as the [OpenID Connect (OIDC) identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) to improve predictability and simplify IAM role creation. 

To ensure that your applications can assume the appropriate IAM roles, you need to add the `Cloudfront Domain Alias` to those roles as a [trust entity]({{< relref "/advanced/iam-roles-for-service-accounts/index.md#aws-release-v19" >}}).

We have also adjusted the `external-dns` IRSA trust policy to facilitate externalDNS role being assumed by any Service Account containing "external-dns" to allow multiple app deployments.

To help make your transition to `IRSA` as easy as possible, we've added more context on our [official docs]({{< relref "/advanced/iam-roles-for-service-accounts/index.md#aws-release-v19" >}}).

## Other release highlights

### 🎣 DNS Node Cache

To improve the DNS performance of your cluster [k8s-dns-node-cache-app](https://github.com/giantswarm/k8s-dns-node-cache-app) will be deployed by default.

#### Key Highlights

- Faster DNS lookups: The app caches DNS lookups on each node, reducing the time it takes to resolve domain names.
- Lower latency: By caching DNS requests locally on each node, the app reduces the need to query external DNS servers, which can improve latency.
- Reducing network traffic: By caching DNS responses locally on each node, the app reduces the need for repeated queries to external DNS servers, which can reduce network traffic.

If you previously deployed `k8s-dns-node-cache-app` through the managed catalog, you can delete the application after the upgrade, as it will be automatically re-installed.

### Prometheus Blackbox Exporter

The [prometheus-blackbox-exporter](https://github.com/giantswarm/prometheus-blackbox-exporter-app) is a new monitoring component installed by default with release `v19`. 

#### Key Highlights

- Flexible monitoring: The blackbox exporter allows users to monitor endpoints from various protocols like HTTP, HTTPS, DNS, TCP, ICMP, and more.
- Real-time monitoring: The exporter provides real-time monitoring of the endpoints and helps detect issues before they turn into major problems.
- Customizable checks: The blackbox exporter can be customized to perform specific checks on the endpoints, which helps in identifying problems quickly.
- Integration with Prometheus: The exporter integrates seamlessly with Prometheus, allowing users to visualize and analyze data collected from the endpoints.

We're aiming to provide a comprehensive blackbox monitoring tool that can validate internal, DNS and external connectivity.

### 🔭 Cilium Hubble

`Cilium` will have [Hubble](https://github.com/cilium/hubble) enabled by default for troubleshooting and observability.

#### Key Highlights

- Provides real-time visibility into network traffic with advanced filtering and aggregation capabilities.
- Helps troubleshoot connectivity issues with its network flow and DNS query analysis features.

#### Caveats and know limitations

- Hubble's UI is not exposed by default, but can be reached using port forwarding.

## 🙇🏻‍♂️ Final last words

We're thrilled to release v19.0.0, packed with exciting updates and improvements. We believe customers will greatly benefit from these new features and enhancements, and we're committed to supporting you every step of the way. 

If you have any questions or run into any issues, please don't hesitate to reach out to our customer support or your Account Engineer.

## Further reading

- [Giant Swarm Cilium migration steps from AWS CNI](https://handbook.giantswarm.io/docs/support-and-ops/ops-recipes/upgrade-to-cilium/)
- [Cilium missing features in Network Policies](https://docs.cilium.io/en/stable/network/kubernetes/policy/#networkpolicy-state)
- [Cilium Network Policy](https://docs.cilium.io/en/stable/network/kubernetes/policy/#ciliumnetworkpolicy)
- [Cilium](https://github.com/cilium/cilium)
- [Hubble](https://github.com/cilium/hubble)
