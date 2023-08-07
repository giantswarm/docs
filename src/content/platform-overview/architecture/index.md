---
linkTitle: Platform architecture
title: Platform architecture
description: Architecture overview explaining how our platform is built and what services we offer in the Platform.
weight: 30
menu:
  main:
    parent: platform-overview
    identifier: platform-architecture
last_review_date: 2023-07-11
user_questions:
  - How does a developer platform look like?
  - How has Giant Swarm built a platform to allow customers enhance developer experience?
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
  - https://github.com/orgs/giantswarm/teams/team-phoenix
  - https://github.com/orgs/giantswarm/teams/team-horizon
---

Giant Swarm's mission is to offer a developer platform to our customers. We work with companies which usually have their systems and teams managing their existing infrastructure and applications. For that reason, we have created a composable system where customers can opt in or out of the services available. 

All platforms teams are trying to solve the same set of problems. How developers securely build their applications, how to deploy these applications in an ephemeral environment easily or how to observe the behavior of these applications with the minimal configuration. For that reason we want to build a platform that relies on the [good principles](https://www.giantswarm.io/blog/platform-engineering-its-not-about-a-tool-stack-its-a-set-of-capabilities) exposed by the community:

- Treat the platform as product
- Minimize cognitive load for developers
- Enable fast-flow software delivery

![Platform architecture](platform-architecture.png)

Starting from this premise we have built a solution that consists in various systems. They can be categorized into three areas: infrastructure, applications, platform interfaces and operations.

## Platform architecture

### Interfaces

The entrypoint to the platform is our interfaces. We leverage in the Kubernetes and its extension capabilities to expose the main functionality. The [management API]({{< relref "/platform-overview/management-api" >}}) is just a Kubernetes API enriched to enable to serve complete golden paths for developers.

Beyond the API our bet is [GitOps](https://www.giantswarm.io/blog/what-is-gitops) to ensure the customers use solid principles for managing their workloads. Most of the actions in our platform can be described and stored in your repositories becoming the source of truth.

Along with GitOps we have a [Web interface]({{< relref "/platform-overview/web-interface" >}}), that simplifies the life of the platform engineering teams in order to visualize infrastructure, apps and permissions across the entire platform. 

In addition to, we offer a set of [templates](https://github.com/giantswarm/gitops-template) to start with the platform and a [documentation hub]({{< relref "/getting-started" >}}) where you can go across a step-by-step guide to complete a Dev Platform Journey. 

### Applications

The capabilities of the platform are exposed thanks to the different Cloud Native tools available. In Giant Swarm we use a set of open-source tooling backup by the community but we do not force you to stick to it. 

There are a set of capabilities that customer can rely today, but we are open also for new use cases. Every customer has different necessities and it can vary over time. 

Today we can offer on a set of different features for building your platform:

- Access Management: Configure which user or groups can have access to the platform.
- Secret Management: Store securely the secrets your apps need to access other services.
- CI/CD: Create your pipelines to build and deploy the applications.
- Registry: Store the applications artifacts in a secure place. 
- Smart Routing: Configure the ingress/egress access to your applications trusting in service mesh capabilities.
- Policy enforcement: Ensure a set of constraints through the platform based on the company policies.
- Resource provisioning: Easy the way of providing and configuring external resources.

### Infrastructure

For managing the infrastructure we run a management cluster per provider and region wherever you want to have your workloads. From that management cluster you can spin up as many individual Kubernetes clusters, called workload clusters, as you want. Our operations team works to maintain all cluster components' health, while we release new versions with new features and patches.

Giant Swarm's architecture is split into two logical parts. One encompasses the management cluster and all the components running there. The second part refers to the workload clusters that are created dynamically by the users to run their business workloads. In principle the management cluster and workload cluster(s) are analogous in terms of infrastructure and configuration. The difference comes with the additional layers we deployed on top of the management cluster that helps manage your users and permissions, workload clusters or the applications running on the workload clusters.

As explained previously, both the management cluster and the workload cluster(s) have the same structure and configuration. In Giant Swarm we collaborate on [Cluster API](https://cluster-api.sigs.k8s.io/) to make easy the bootstrap and configuration of the cluster infrastructure and all the components needed for a cluster to function.

![Cluster architecture image](CAPI_architecture.png)

By default, the machines are split into three different failure domains or zones to ensure the availability of the API and workloads running on top. In our setup, three control plane machines hold the Kubernetes API and the other controllers, and a variable number of worker machines contain the workloads.

Besides the Kubernetes machines, we run a bastion host that helps us with the operations. It is the single entry point to the running infrastructure. That way all the cluster machines can live in a private network and reduce the exposure of the services running on them via explicit configuration. We are working in a [Teleport](https://goteleport.com/) solution to replace the necessity of the bastions and centralize the cluster access through a single tool.

#### Providers

Thought we tried to treat all the providers the same way, offering the same features on top and having same configuration, there are some subtle differences depending on the provider functionality.

{{< tabs >}}
{{< tab id="flags-clouddirector" title="VMware Cloud Director">}}

*Compatibility*

The setup supports organization virtual datacenters (OVCDs) running on VMware Cloud Director 10.3 and above. It must be backed by backed with NSX-T and NSX advanced load balancer (ALB) with the load balancer feature enabled on the Edge gateway. 

*Authentication*

Cluster API Provider VMware Cloud Director (CAPVCD), along with the associated Cloud Provider interface (CPI) and Container Storage interface (CSI), authenticate against the VMware Cloud Director API using an API Token (sometimes also referred to as Refresh Token) which is stored in a secret. Such token can be created by any user with the right permission and can be revoked at any time should there be suspicion of it being compromised.

*Networking*

The kubernetes API and services of type `LoadBalancer` get IPs from a pool of external IPs available in the edge gateway. It can be set statically or takes the next available IP if unspecified. A virtual service is then created with the required IP/port and is associated with a load balancer pool that contains the relevant node IPs as members. For the CPI, we support the virtual service shared feature which was introduced in VCD 10.4 as well as the legacy method based on a single internal IP and multiple DNAT rules.

A network needs to be specified in the cluster definition to identify where the default gateway will be and where to connect the virtual machines (VMs). It is also possible to add additional networks in order to connect multiple virtual interfaces to the nodes along with a list of static routes. The nodes must have internet access which is usually achieved with a SNAT rule or via an HTTP proxy. Note that it is also possible to specify NTP servers and pools (Ubuntu based nodes running `chrony`) in the cluster definition, which is particularly useful in air-gapped environments.

*Compute*

The Kubernetes cluster is represented in VMware Cloud Director by a vAPP of the same name that contains one virtual machine for each node. Note that our setup also supports naming conventions for virtual machine names based on go templates. When a node is created, a virtual machine is provisioned in the cluster's vAPP using a vAPP template stored in a specific catalog. When configuring the control plane nodes or a node class for a node pool, several parameters can be set for the virtual machines such as the sizing policy, placement policy, virtual disk size and storage profile.

*Storage*

In order to offer persistent storage that is decoupled from the virtual machines, the container storage interface creates a Named Disk that can be attached or detached from the VM according to whether or not the persistent volume claim (PVC) is bound to a pod or not. Named disks currently only support Read-Write-Only (RWO) with block storage backed named disks.

{{< /tab >}}
{{< tab id="flags-aws" title="AWS">}}

The setup uses a standalone VPC (though you can bring your own VPC) and creates private subnets for the machine in each availability zone. It uses NAT gateways for allowing machines to pull images or route requests from containers to the Internet. On the other side, it needs an Internet Gateway to route traffic from Internet to the containers. It leverages route tables to configure the routing for each subnet and gateways.

{{< /tab >}}
{{< tab id="flags-capz" title="Azure">}}

{{< /tab >}}
{{< /tabs >}}

Internally, Cluster API (CAPI) uses kubeadm to configure all the machines according to current standards. It uses a template defined as yaml, part of CAPI, where we have hardened the different parameters for the API and other controllers running in the master machine.

### Operations

Aside from infrastructure and customer-facing applications we also deploy a set of tooling that ensure we have a nice delivery system, good hardening and clear observability.  

*Authentication Features of the Platform*

Giant Swarm configures the clusters in a secure way. [Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) is enabled by default and our customers can create their own roles or use the ones predefined in the cluster to gain access to manage their workloads. The concept of authenticated users and groups does not exist in Kubernetes, so it relies on an external solution to retrieve user/group information (e.g. via X.509 certificates or [OIDC](https://en.wikipedia.org/wiki/OpenID_Connect)). Although our platform allows users to access their clusters using certificates, we recommend using an OIDC compliant Identity Provider, such as Active Directory, to provide authentication. There are several advantages to using an OIDC provider, such as short lived tokens or taking advantage of existing user and group information. Once authentication is sorted out, the authorization part is handled with RBAC. RBAC, along with namespaces, lets users define granular permissions for each user or group. This [guide]({{< relref "/getting-started/rbac-and-psp" >}}) will walk you through it.

*Secure Features of the Platform*

From our first versions, Giant Swarm has set up a secure baseline in all our customer clusters. In the early days, Kubernetes released [Pod Security Policies (PSPs)](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) to enforce pod security providing a new built-in resource where user can define the user group permissions or volume types allowed. In Kubernetes `1.25` this implementation is phased out instead of [Pod Security Admission(PSA)](https://kubernetes.io/docs/concepts/security/pod-security-admission/). We have not found an equivalent set of policies using that technology so for now we have decided to leverage on Kyverno to enforce our same restricted policies](https://www.giantswarm.io/blog/giant-swarms-farewell-to-psp). By default, users and workloads running in Giant Swarm clusters, are assigned a restrictive policy that disallows running containers as root or mounting host path volumes (these are just two examples). Cluster operators must enable applications to have higher security privileges on a case by case basis. 

In addition to the security policies, [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/) define the communication policies to and from the applications in each namespace. All components to run a cluster provided by Giant Swarm come with strict policies by default. Our managed namespaces (“kube-system” and “giantswarm”) block all traffic in general, so only expected and specifically configured routes and ports are enabled. Customers can follow this approach and deny all communications by default in their application namespaces forcing each workload to define which communications are allowed. This [guide]({{< relref "/getting-started/network-policies" >}}) helps to understand how such a dynamic firewall works.

Currently we run [Cilium](https://cilium.io/) as CNI in all our clusters which brings new powerful features to increase the security of our setups. Cilium extends Kubernetes network policies to allow us filter out based on domains and

*Monitoring Features of the Platform*

Since we provide a **managed** Kubernetes platform, Giant Swarm has to be aware of state and unexpected events regarding the platform. For that reason our management clusters run a [monitoring stack](https://www.giantswarm.io/blog/monitoring-on-demand-kubernetes-clusters-with-prometheus) to watch all workload clusters and ensure all managed components are healthy. In each workload cluster there are several [exporters](https://prometheus.io/docs/instrumenting/exporters/) that gather and forward the metrics for each component.

Our on-call engineers are paged in case anything happens to the cluster or its base components. They respond to the incident based on our run-books, the ones we have written (and continue to update) over years operating Cloud Native systems. In case there is an improvement to be made, a post mortem is created and a solution will be implemented before long. Any patch or fix added to the platform is released to all customers.

*CI/CD Features of the Platform*

Since the appearance of [GitOps](https://www.giantswarm.io/blog/what-is-gitops) we have been enthusiastic about it. It provides many benefits while relying on the same principles we were already advocating for. In Giant Swarm, we use [Flux](https://www.giantswarm.io/blog/gitops-with-flux-giant-swarm) to control the configuration and definition of infrastructure and the software on top of it.

In our setup we have two Flux instances running, one managing the resources specific to the overall operation of the management cluster (`flux-giantswarm`) and the second for handling resources generated by the customer (`flux-system`).

To support customers in their use of Flux and the CI/CD features available to the platform, we provide a common template structure [gitops-template](https://github.com/giantswarm/gitops-template/) which presents structures, ideas and best practices on how to use flux within the Giant Swarm eco-system.

## Further Reading

- [Giant Swarm Management API]({{< relref "/platform-overview/management-api" >}})
- [Giant Swarm support model]({{< relref "/support" >}})
- [Giant Swarm operational layers]({{< relref "/platform-overview/security/operational-layers" >}})


