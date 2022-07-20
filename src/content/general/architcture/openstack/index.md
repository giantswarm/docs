---
linkTitle: Openstack
title: The Giant Swarm Openstack architecture
description: Architecture overview explaining how OpenStack Cluster API implementation is done.
weight: 30
menu:
  main:
    parent: general-architecture
last_review_date: 2022-02-02
user_questions:
  - Do you run Openstack?
aliases:
  - /basics/openstack-architecture/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

The Giant Swarm Platform consists of various systems. They can be categorized into three areas: infrastructure, operations, and applications.

For managing all the infrastructure we run a management cluster per cloud and region where you want run your workloads. From that management cluster you can spin up as many individual Kubernetes clusters, called workload clusters, as you want. Our operations team works to keep all cluster components healthy, while we release new versions with new features and patches. On top of that, Giant Swarm offers a curated catalog with common Cloud Native tools that helps to monitor, secure or manage your applications. Customers can leverage those while we carry the burden of maintain and keep them up to date.

Giant Swarm's architecture is split into two logical parts. One comprehends the management cluster and all the components running there which enhance the user experience when it comes to manage clusters and applications. On the other side we have the workload clusters that are created dynamically by the users and they serve to run their business workloads. In principle the management cluster and workload cluster are the equal in terms of infrastructure and configuration. The difference comes with the additional layers on top that help to manage your user and permissions, the workload clusters or the applications running on those clusters.

## Cluster Architecture

As explained previously, both management cluster and workload cluster has the same cluster structure and configuration. In Giant Swarm we rely on [Cluster API]() to bootstrap and configure the cluster infrastructure and set up all the components needed for a cluster to function. 

[Cluster Architecture Image]()!

By default the machines are split in three different failure domains or zones to ensure availability in the API and workloads. 

There is a machine created as bastion that help us with the operations. It is the single entrypoint to the running infrastructure so that way all cluster machines can live in a private network and expose the services running on them via explicit configuration.

The setup requires a external network configured in the project to allow the machines to pull images or route requests from containers to Internet.

We used an internal network which interconnects all master and worker hosts allowing internal communication of all containers in the cluster. At the same time it allocates the load balancers that are created dinamically as result of exposing a service in the cluster. The load balancer, in case of being external, allocates a floating IP to make possible the connection with external endpoints.

Internally Cluster API (CAPI) use kubeadm to configure all the machines according to the standards. It use a template defined as yaml, part of CAPI, where we have harden the different parameters for the API and other controllers running in the master machine.

## Giant Swarm Management Cluster

As we are fully convinced of Kubernetes as a platform for building platforms, we build all our management clusters based on Kubernetes.

### Bootstrapping

The initial deployment entails the creation of that management cluster in a defined region. After the management cluster is ready we deploy all our automation taking advantage of Kubernetes primitives and using the same philosophy we advocate to our customers.

### Components

Giant Swarm leverages the concept of “Operators" to control all resources that clusters need as “Custom Resources”. At the same time customers can also use the Kubernetes Control Plane API to manage their clusters and/or applications.

#### RBAC operator

#### App operator

#### Cluster operators

#### Cluster app operator


## Giant Swarm on-premises workload cluster(s)

### Components

#### CPI

#### Kube State Metrics

#### Cillium

#### Cert exporter

#### Net exporter

#### Metric server

#### Node exporter


## Workload segregation and account model

When starting out with our platform many of our customers are at the beginning of their journey to a distributed and highly resilient micro-service architecture. This is often a radically different approach to organizing and managing computing resources. This is mostly about abstracting the complexity of cluster creation and management. It opens up new possibilities on how to isolate applications and access to the infrastructure. The two most common reasons for customers to segregate applications over different clusters and/or accounts are security and separation of concerns.

Once Kubernetes arrived on the scene, the promise of having all your applications in a single cluster seemed invaluable, as container isolation, namespaces, and other Kubernetes features allow you to isolate the workloads. But as time passed several drawbacks were found that discourage this approach. Container isolation is not perfect, in the end workloads still share a kernel and some cluster components that can affect each other. Though it can be mitigated using Role-Based Access Control (RBAC), Network Policies or Pod Security Policies, it requires expertise and knowledge. At the same time, as you continue to add more and more applications into the cluster, the traffic increases. This potentially affects DNS latency, ingress handling, or the attack surface. In addition, having multiple tenants in the cluster increases the possibility to affect each other when a central component is tuned for a specific scenario. Potentially, it can significantly impact the cluster lifecycle, i.e. upgrades, due to the extra effort in communication and planning across various teams.

All of this is not to say that segregation inside a cluster should be avoided but to emphasize that there are considerations that need to be weighed, before deciding on how to group tenants, applications and technical requirements.

Hence, the key is to find the right balance between the new Cloud Native approach and the old school hard isolation.

Above, we see several isolation layers in one place. Our automation creates a single VPC by cluster, with private subnets for the worker nodes and secure configuration by default. At the same time, the nodes run a container-ready operating system created with security and reliability in mind. Next, our base Kubernetes setup provides [Network Polices](https://kubernetes.io/docs/concepts/services-networking/network-policies/) and [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) to restrict communication to core components accompanying with a very strict policy to ensure containers do not gain extended privileges unintentionally.

Having said that, there is no general rule to split workloads between AWS accounts, clusters or namespaces. It highly depends on the customers policies in effect and access requirements among others. However, we can give some advice on where to start.

- Use AWS accounts (and other AWS tools) to establish different access models based on environments. You could have an account **A** for production, where users have no rights, and audit policies and logging systems track every single action. And you could have an account **B**, where developers can get access to debug and test their applications or understand the infrastructure that holds it.
- Segregate applications based on responsibility and volume of services included. If a team or department owns a service platform composed of several components, it makes sense to use a single cluster for it. That way, upgrades to the cluster or its shared components, like Ingress Controller or DNS servers, do not interfere with other applications which reduces overall complexity.
- Divide different services of single systems into different [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/). It allows to control resources, network communication and access to those in finer granularity.
- Automate and abstract your workload lifecycle. Defining the configuration of applications and the underlying [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) has become the de facto standard to manage complex systems. There are plenty of tools nowadays to declare your application configuration as code, rely on them and discard manual changes. Think about the possibility of having to migrate your application from one cluster to another. Ideally, such a change should imply just a single config line change. Kubernetes helps to define [Cloud Native Applications](https://12factor.net/) but there are some parts that still reside on the developer side.


### Worker node size

When it comes to sizing your worker nodes, there should generally be a preference for more, smaller nodes vs less, bigger ones. However, avoid node sizes of less than 4 cores and 8 GB RAM.

To determine the right sizing in terms of cores and RAM, you need to know what kind of workloads will be run on the cluster and how much resources they need. Note that even if average load might be low, you should also account for peak load times as well as startup-peaks (i.e. some apps need a lot of resources just for their startup).

## Control resource assignment

One of the golden rules of Kubernetes is proper resource assignment. This is hard to do, especially for developers which are not used to profiling their applications under different scenarios. But the resource definition is a [key configuration](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) part that allows Kubernetes to schedule, limit, control and scale the applications. So our recommendation [is to define resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for most of your applications running in the clusters. That said, there is some controversy about defining CPU limits due to how Kernels manage the CPU quota assigned to the containers. There have been some fixes in the latest Kernel versions which improve the situation. To learn more, we encourage you to [check this Kubecon video](https://www.youtube.com/watch?v=UE7QX98-kO0) or talk to your Account Engineer.

Further, to enforce the definition of resources, [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/) helps to set the defaults once a user forgets to add those. At the same time, [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) enables cluster operators to assign a predetermined amount of resources to each namespace. Thus, protecting other workloads.

## Cluster authentication

Giant Swarm configures the clusters in a secure way. [Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) is enabled by default and our customers can create their own roles or use the ones predefined in the cluster to gain access to manage their workloads. The concept of authenticating users and groups does not exist in Kubernetes, so it relies on an external solution to authenticate the users (e.g. via X.509 certificates or [OIDC](https://en.wikipedia.org/wiki/OpenID_Connect)). Although our platform allows users to access the cluster using certificates, we recommend using an OIDC compliant Identity Provider, such as Active Directory, to provide authentication. There are several advantages to using an OIDC provider, such as short lived tokens or taking advantage of existing user and group information. Once authentication is sorted out, the authorization part is handled with RBAC. RBAC, along with namespaces, lets users define granular permissions for each user or group (given by OIDC or certs). This [guide]({{< relref "/getting-started/rbac-and-psp" >}}) will walk you through it.

## Secure your workloads

Within the cluster, Giant Swarm has set up a secure baseline using [Pod Security Policies (PSPs)](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) and [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). Pod Security Policies are the Kubernetes resource that configures the sensitive aspects of your applications. By default, users and workloads running in Giant Swarm clusters, are assigned a restrictive policy that disallows running containers as root or mounting host path volumes (these are just two examples). Cluster operators must enable applications to have higher security privileges on a case by case basis. In the aforementioned [guide]({{< relref "/getting-started/rbac-and-psp#pod-security-policies" >}}) we also explain how to configure tailored PSPs for you applications.

In addition to the security policies, Network Policies define the communication policies to and from the applications in each namespace. All components to run a cluster provided by Giant Swarm come with strict policies by default. Our managed namespaces (“kube-system” and “giantswarm”) block all traffic in general, so only expected and specifically configured routes and ports are enabled. Customers can follow this approach and deny all communications by default in their application namespaces forcing each workload to define which communications are allowed. This [guide]({{< relref "/getting-started/network-policies" >}}) helps to understand how such a dynamic firewall works.

## Observability

Since we provide a **managed** Kubernetes platform, Giant Swarm has to be aware of state and unexpected events regarding the platform. For that reason our management clusters run a [monitoring stack](https://www.giantswarm.io/blog/monitoring-on-demand-kubernetes-clusters-with-prometheus) to watch all workload clusters and ensure all managed components are healthy. In each workload cluster there are several [exporters](https://prometheus.io/docs/instrumenting/exporters/) that gather and forward the metrics for each component.

Our on-call engineers will be paged in case anything happens to the cluster or its base components and they will respond to the incident based on the run-books we have created based on years of operating Cloud Native systems. In case there is an improvement to be made, a post mortem is created and a solution will be implemented before long. Any patch or fix added to the platform will be released to all customers.

Please note, while this document went into extensive details with regards to how Giant Swarm runs Kubernetes on AWS, we support [Azure]({{< relref "/general/architecture/azure" >}}) as well as [Bare Metal]({{< relref "/general/architecture/on-premises" >}}). For more details, please [contact us](https://www.giantswarm.io/contact).

## Further Reading

- [Giant Swarm support model]({{< relref "/general/support" >}})
- [Giant Swarm operational layers]({{< relref "/security/operational-layers" >}})
- [Giant Swarm VPN and secure cluster access]({{< relref "/security/cluster-access" >}})