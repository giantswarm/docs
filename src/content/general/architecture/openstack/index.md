---
linkTitle: Cluster-API-Architecture
title: The Giant Swarm Platform Architecture
description: Architecture overview explaining how our Platform is built it.
weight: 30
menu:
  main:
    parent: general-architecture
last_review_date: 2022-08-12
user_questions:
  - Do you run a Developer Platform?
aliases:
  - /basics/platform-architecture/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rocket
---

The Giant Swarm Platform consists of various systems. They can be categorized into three areas: infrastructure, applications, and operations.

For managing the infrastructure we run a management cluster per provider and region wherever you want to have your workloads. From that management cluster you can spin up as many individual Kubernetes clusters, called workload clusters, as you want. Our operations team works to maintain all cluster components healthy, while we release new versions with new features and patches. On top of that, Giant Swarm offers a curated catalog with the most common Cloud Native tools that helps to monitor, secure or manage your applications. Customers can leverage those while we carry the burden of maintain and keep them up to date.

Giant Swarm's architecture is split into two logical parts. One comprehends the management cluster and all the components running there. On the other side we have the workload clusters that are created dynamically by the users and they serve to run their business workloads. In principle the management cluster and workload cluster are the equal in terms of infrastructure and configuration. The difference comes with the additional layers we deployed on top of the management cluster that helps to manage your users and permissions, workload clusters or the applications running on the workload clusters.

## Cluster Architecture

As explained previously, both the management cluster and the workload cluster have the same cluster structure and configuration. In Giant Swarm we rely on [Cluster API](https://cluster-api.sigs.k8s.io/) to bootstrap and configure the cluster infrastructure and set up all the components needed for a cluster to function.

[Cluster Architecture Image](./CAPO_architecture.png)!

By default, the machines are split into three different failure domains or zones to ensure the availability of the API and workloads running on the there. In our setup, three control plane machines hold the Kubernetes API and the other controllers, and a variable number of worker machines contain the regular services.

There is a machine created as a bastion that helps us with the operations. It is the single entry point to the running infrastructure so that way all the cluster machines can live in a private network and expose the services running on them via explicit configuration.

{{< tabs >}}
{{< tab id="flags-aws" title="AWS">}}

{{< /tab >}}
{{< tab id="flags-capz" title="Azure">}}

{{< /tab >}}
{{< tab id="flags-gcp" title="GCP">}}

{{< /tab >}}
{{< tab id="flags-openstack" title="OpenStack">}}

The setup requires an external network configured in the project to allow the machines to pull images or route requests from containers to Internet. On the other side, there is an internal network which interconnects all master and worker machines allowing the internal communication of all containers within the cluster. At the same time, it allocates the load balancers that are created dynamically as result of exposing a service in the cluster. The load balancer, in case of being external, allocates a floating IP to make possible the connection with external endpoints.

{{< /tab >}}
{{< /tabs >}}

Internally, Cluster API (CAPI) use kubeadm to configure all the machines according to the standards. It uses a template defined as yaml, part of CAPI, where we have hardened the different parameters for the API and other controllers running in the master machine.

## Giant Swarm Platform

The Giant Swarm Platform revolves around the the management cluster API. The main reason is nowadays Kubernetes is the standard defacto for managing infrastructure in a modern way. Its extensibility makes easy to transform a cluster in a Platform adding the sugar to make user experience great.

Our platform let us the customer manage (workload) clusters and applications in a Cloud Native fashion. Here we are going to explain the bootstrapping process of a cluster, how it is managed in the entire lifecycle and which components the cluster run based on the role, workload or management.

### Bootstrapping

The initial deployment entails the creation of that management cluster in a defined region. We have built a tool that performs all steps need to create a cluster and convert into a management cluster.

The process involves several steps that we resume briefly in the following list:

1. Configure the credentials for the chosen provider.
2. Add the installation details into our config management system (Github repo).
3. Create a bootstrap cluster using [kind](https://kind.sigs.k8s.io/).
4. Install the Cluster API (CAPI) controllers on it.
5. Create the management CAPI resources on the bootstrapping cluster to trigger the provision of the real infrastructure on the provider. It creates the actual Kubernetes cluster in the customer infrastructure.
6. Move the Cluster API controllers and resources to the real management cluster in the end provider.
7. Deploy our App platform on top of the management cluster.
8. Deploy our monitoring system on top of the management cluster.
9. Deploy all additional operators that enhances the API (organizations, RBAC, etc).
10. Configure and harden the cluster.
11. Run and test the management cluster functionality.

After the management cluster is ready we deliver all the details to the customer to allow them the access to the Management API. From this very moment we use the same mechanisms to control the management cluster lifecycle as we use for workload clusters.

Cluster API offers a set of custom resources that define all the details of a cluster infrastructure and its configuration. 

[Cluster API Resources](./CAPI_resources.png)!

Usually we have generic resources that define common configuration of the clusters and its components, and some infrastructure specific resources which will be tied to the provider we select. 

We have created a [kubectl plugin](https://docs.giantswarm.io/ui-api/kubectl-gs/template-cluster/) to help you template all the needed resources.

### Components

There are two type of components: generics and self-developed.

#### Generic Components

The generic components run in all of our clusters does not matter if it is a management cluster or a workload cluster.

##### Container Network Interface (CNI)

The Container Network Interface is the standard for writing plugins to configure network interfaces in Linux containers, and hence Kubernetes.

We have chosen Cilium as CNI implementation for several reasons. It is open source solution that provides connectivity between containers in reliable and secure way. Cilium operates at Layer 3/4 providing traditional networking and security services. Additionally it protects and secure applications offering different enhanced features on top. In the workload cluster is used as container network only by now.

##### Kube State Metrics

Kube State Metrics (KSM) is a upstream project that watches to the Kubernetes API and provide metrics about the state of the built-in resources. It is used by our monitoring service to scrape the metrics of the core components so we can be paged when something is not working on the cluster. At the same time the customer can scrape that metrics to create their own dashboards and alerts.

##### Cert exporter

It is a Prometheus exporter that exposes a set of metrics regarding certificates and tokens. It enables us to stay ahead of certificates expiration and take care of them in a timely fashion.

##### Net exporter

Net exporter is also a Prometheus exporter for exposing network information. It runs in every node to track network and DNS errors. We have created some dashboards to help us debug issue on the cluster and also some of our alerts are based on the metrics exported by it.

##### Metric server

Metrics Server is an upstream component that implements the [Kubernetes Metrics API](https://kubernetes.io/docs/tasks/debug/debug-cluster/resource-metrics-pipeline/#metrics-api) to provide basic data of the container running in the cluster. It gives us information about CPU and memory of every pod and it used by other components,like Horizontal Pod Autoscaler, to take scaling decisions. 

##### Node exporter

It is an upstream Prometheus exporter for tracking hardware and operating system metrics exposed by *NIX kernels. It completes our monitoring service giving us the possibility to track resources used in the nodes and let us create alerts based on that information.

#### Giant Swarm Components

Giant Swarm has developed a full fledged platform that enhances customer experience managing cluster and apps in top of Kubernetes.

There are three types of components running on top of the management clusters: the operators, the admission controllers and the operational services. The first one, operators, extend the API allowing our customers to manage new entities (like a Cluster or an App) as if they were built-in resources. The second one, admission controllers, validate and default the resources to make better the user experience. And the last one, the operational services like monitoring or security, enable our staff to maintain all the workload cluster and applications up and running securely and seamlessly.

##### Operators (Custom Resource plus controller)

<TODO: Explain Kubernetes pattern>

*Organization operator*

This operator is in charge of reconcile `Organization` custom resources. The functionality of the operator is pretty straightforward. It takes care of create and delete the organization namespace when the given resource is created.

To learn more about organizations please read [the related documentation](https://docs.giantswarm.io/general/organizations/).

*RBAC operator*

We have created an RBAC operator with the goal of maintaining up to date permissions between the different organization and users on the management cluster so [you can isolate your teams and ensure access level in granular way](https://docs.giantswarm.io/ui-api/management-api/authorization/).

*DNS operator*

*Deletion Blocker Operator*

*App operator*

The [App Platform](https://docs.giantswarm.io/app-platform/) is a system we have built to deliver cloud native apps in multi cluster fashion. App operator is the main code running in management cluster to manage App custom resource and make sure the applications and configuration are delivered correctly across the different workload clusters.

*Cluster API operators*

In [Cluster API](https://cluster-api.sigs.k8s.io/) there is a set of generic operators that all Cluster API providers run to address the common bootstrap and management actions on a Kubernetes cluster lifecycle which include:

- `Kubeadm Bootstrap`controller which is in charge of providing a cloud init configuration to turn a machine into a Kubernetes node.
- `Kubeadm Control Plane` controller that manages the lifecycle of the control plane nodes and provides access to the API.
- `CAPI manager` controller that manages cluster and machine resources.

*Cluster OpenStack controller*

As part of the generic controllers we have this special one. It acts as a bridge and reconciles the provider specific configuration to create the necessary infrastructure for a Kubernetes cluster. This controller provisions, updates and deletes all resources on the provider API. It also enriches Kubernetes node info with infrastructure relevant information. This is helpful for application administrators to implement affinity/ anti-affinity rules which reflect underlying availability zone metadata. It is mandatory for the Cluster API provisioning workflow to get known infrastructure specific machine metadata.

*Cluster apps operator*

This simple operator takes care of the default apps required for a cluster and the right configuration for their creation. Assets like the certificate authority or the domain base are provided by it via a configmap.

##### Admission controllers

<TODO: Fill it with the different admission controllers>

##### Operational services

*Authentication services*

Giant Swarm configures the clusters in a secure way. [Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) is enabled by default and our customers can create their own roles or use the ones predefined in the cluster to gain access to manage their workloads. The concept of authenticating users and groups does not exist in Kubernetes, so it relies on an external solution to authenticate the users (e.g. via X.509 certificates or [OIDC](https://en.wikipedia.org/wiki/OpenID_Connect)). Although our platform allows users to access the cluster using certificates, we recommend using an OIDC compliant Identity Provider, such as Active Directory, to provide authentication. There are several advantages to using an OIDC provider, such as short lived tokens or taking advantage of existing user and group information. Once authentication is sorted out, the authorization part is handled with RBAC. RBAC, along with namespaces, lets users define granular permissions for each user or group (given by OIDC or certs). This [guide]({{< relref "/getting-started/rbac-and-psp" >}}) will walk you through it.

*Secure services*

Within the cluster, Giant Swarm has set up a secure baseline using [Pod Security Policies (PSPs)](https://kubernetes.io/docs/concepts/policy/pod-security-policy/), currently phased out and moving to [Pod Security Admission(PSA)](https://kubernetes.io/docs/concepts/security/pod-security-admission/) and [Network Policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/). Both Pod Security Policies and Pod Security Admission are the Kubernetes resource that configures the sensitive aspects of your applications. By default, users and workloads running in Giant Swarm clusters, are assigned a restrictive policy that disallows running containers as root or mounting host path volumes (these are just two examples). Cluster operators must enable applications to have higher security privileges on a case by case basis. In the aforementioned [guide]({{< relref "/getting-started/rbac-and-psp#pod-security-policies" >}}) we also explain how to configure tailored PSPs for you applications.

In addition to the security policies, Network Policies define the communication policies to and from the applications in each namespace. All components to run a cluster provided by Giant Swarm come with strict policies by default. Our managed namespaces (“kube-system” and “giantswarm”) block all traffic in general, so only expected and specifically configured routes and ports are enabled. Customers can follow this approach and deny all communications by default in their application namespaces forcing each workload to define which communications are allowed. This [guide]({{< relref "/getting-started/network-policies" >}}) helps to understand how such a dynamic firewall works.

*Monitoring services*

Since we provide a **managed** Kubernetes platform, Giant Swarm has to be aware of state and unexpected events regarding the platform. For that reason our management clusters run a [monitoring stack](https://www.giantswarm.io/blog/monitoring-on-demand-kubernetes-clusters-with-prometheus) to watch all workload clusters and ensure all managed components are healthy. In each workload cluster there are several [exporters](https://prometheus.io/docs/instrumenting/exporters/) that gather and forward the metrics for each component.

Our on-call engineers will be paged in case anything happens to the cluster or its base components and they will respond to the incident based on the run-books we have created based on years of operating Cloud Native systems. In case there is an improvement to be made, a post mortem is created and a solution will be implemented before long. Any patch or fix added to the platform will be released to all customers.

Please note, while this document went into extensive details with regards to how Giant Swarm runs Kubernetes on OpenStack, we support [other providers]({{< relref "/general/architecture" >}}) as well. For more details, please [contact us](https://www.giantswarm.io/contact).

## Workload segregation and account model <I AM THINKING ON MOVING TO A STANDALONE PAGE AND UPDATE IT>

When starting out with our platform many of our customers are at the beginning of their journey to a distributed and highly resilient micro-service architecture. This is often a radically different approach to organizing and managing computing resources than the one used in the past. It is mostly about abstracting the complexity of cluster creation and management. It opens up new possibilities on isolating applications and gaining access to the infrastructure. The two most common reasons for customers to segregate applications over different clusters and/or accounts are security and separation of concerns.

Once Kubernetes arrived on the scene, the promise of having all your applications in a single cluster seemed invaluable, as container isolation, namespaces, and other Kubernetes features allow you to isolate the workloads. But as time passed several drawbacks were found that discourage this approach. Container isolation is not perfect, in the end workloads still share a kernel and some cluster components that can affect each other. Though it can be mitigated using Role-Based Access Control (RBAC), Network Policies or Pod Security standards (and the Pod Security Policies they are replacing), it requires expertise and knowledge. At the same time, as you continue to add more and more applications into the cluster, the traffic increases. This potentially affects DNS latency, ingress handling, or the attack surface. In addition, having multiple tenants in the cluster increases the possibility to affect each other when a central component is tuned for a specific scenario. Potentially, it can significantly impact the cluster lifecycle, i.e. upgrades, due to the extra effort in communication and planning across various teams.

All of this is not to say that segregation inside a cluster should be avoided but to emphasize that there are considerations that need to be weighed, before deciding on how to group tenants, applications and technical requirements.

Hence, the key is to find the right balance between the new Cloud Native approach and the old school hard isolation.

In order to address these concerns, we offer several isolation layers in one place:

- **Network**: Our automation creates a single VPC by cluster, with private subnets for the worker nodes and secure configuration by default.
- **Operating System**: The nodes run a container-ready operating system created with security and reliability in mind.
- **Kubernetes**: Our base Kubernetes setup provides [Network Polices](https://kubernetes.io/docs/concepts/services-networking/network-policies/) and [Pod Security Policies](https://kubernetes.io/docs/concepts/policy/pod-security-policy/) to restrict communication to core components accompanying with a very strict policy to ensure containers do not gain extended privileges unintentionally.

Having said that, there is no general rule to split workloads between Open Stack projects, clusters or namespaces. It highly depends on the customers policies in effect and access requirements among others. However, we can give some advice on where to start.

- Use OpenStack projects to establish different access models based on environments. You could have a project **A** for production, where users have no rights, and audit policies and logging systems track every single action. And you could have a project **B**, where developers can get access to debug and test their applications or understand the infrastructure that holds it.
- Segregate applications based on responsibility and volume of services included. If a team or department owns a service platform composed of several components, it makes sense to use a single cluster for it. That way, upgrades to the cluster or its shared components, like Ingress Controller or DNS servers, do not interfere with other applications which reduces overall complexity.
- Divide different services of single systems into different [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/). It allows to control resources, network communication and access to those in finer granularity.
- Automate and abstract your workload lifecycle. Defining the configuration of applications and the underlying [infrastructure as code](https://en.wikipedia.org/wiki/Infrastructure_as_code) has become the de facto standard to manage complex systems. There are plenty of tools nowadays to declare your application configuration as code, rely on them and discard manual changes. Think about the possibility of having to migrate your application from one cluster to another. Ideally, such a change should imply just a single config line change. Kubernetes helps to define [Cloud Native Applications](https://12factor.net/) but there are some parts that still reside on the developer side.

### Worker node size

When it comes to sizing your worker nodes, there should generally be a preference for more, smaller nodes vs bigger ones. However, avoid node sizes of less than 4 cores and 8 GB RAM.

To determine the right sizing in terms of cores and RAM, you need to know what kind of workloads will be run on the cluster and how much resources they need. Note that even if average load might be low, you should also account for peak load times as well as startup-peaks (i.e. some apps need a lot of resources just for their startup).

## Control resource assignment <I AM THINKING ON MOVING TO A STANDALONE PAGE AND UPDATE IT>

One of the golden rules of Kubernetes is proper resource assignment. This is hard to do, especially for developers who are not used to profiling their applications under different scenarios. Regardless, the [resource definition](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) is a key configuration part that allows Kubernetes to schedule, limit, control and scale the applications. So our recommendation [is to define resources](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) for most of your applications running in the clusters. That said, there is some controversy about defining CPU limits due to how Kernels manage the CPU quota assigned to the containers. There have been fixes in the latest Kernel versions which improve the situation. To learn more, we encourage you to [check this Kubecon video](https://www.youtube.com/watch?v=UE7QX98-kO0) or talk to your Account Engineer.

Furthermore, to enforce the definition of resources, [Limit Ranges](https://kubernetes.io/docs/concepts/policy/limit-range/) helps set the defaults if a user forgets to add those. At the same time, [Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/) enable cluster operators to assign a predetermined amount of resources to each namespace, thus, protecting other workloads.

## Further Reading

- [Giant Swarm support model]({{< relref "/general/support" >}})
- [Giant Swarm operational layers]({{< relref "/security/operational-layers" >}})
- [Giant Swarm VPN and secure cluster access]({{< relref "/security/cluster-access" >}})

