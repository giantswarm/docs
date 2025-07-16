---
title: AWS architecture
description: How architecture and cluster setup look like with the AWS cloud provider specifically.
weight: 30
menu:
  principal:
    parent: overview-architecture
    identifier: overview-architecture-aws
aliases:
  - /basics/aws-architecture/
last_review_date: 2025-07-09
user_questions:
  - Why does Giant Swarm need access to my AWS account?
  - What isolation layers are available when using Giant Swarm on AWS?
  - What are best practices for workload segregation on AWS?
  - Will my AWS clusters autoscale?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

This details the AWS-specific architecture of the Giant Swarm platform. Please make sure you've read about the [overall platform architecture]({{< relref "/overview/architecture" >}}).

## Management cluster, workload clusters and workload separation via AWS accounts

The management cluster runs the software needed to create and manage workload clusters, among other operations. You only need one management cluster, but you can also have multiple if you want to separate by region, or development vs. production, for example.

The management cluster and its workload clusters can be in the same or in different AWS accounts. If you decide on different accounts, each account needs an IAM role with minimal permissions to create cluster resources (VPC, subnets, EC2 instances, etc.). Don't worry ‒ once your first account is set up, Giant Swarm engineers take care of setting up other accounts and updating IAM policies whenever needed (for example, additional permissions for new features). The IAM setup is open source and part of our documentation.

Using multiple accounts has the advantage of strictly separating development and production environments, as required for certain audits, or to separate clusters of different teams, for instance. You can read more in [Multi-account clusters]({{< relref "/overview/fleet-management/cluster-management/cluster-concepts/multi-account" >}}).

One AWS account can host many clusters, and the recommended quota/limit increases are [documented in the AWS account setup]({{< relref "/getting-started/prepare-your-provider-infrastructure/aws" >}}). The two most common reasons for customers to segregate applications over different clusters and/or accounts are security and separation of concerns.

Example: Use AWS accounts (and other AWS tools) to establish different access models based on environments. You could have an account **A** for production, where users have no rights, and audit policies and logging systems track every single action. And you could have an account **B**, where developers can get access to debug and test their applications or understand the infrastructure that holds it.

## Access by Giant Swarm

The operators running on the management cluster (Cluster API, Cluster API Provider AWS, Crossplane, etc.) need certain permissions in customer AWS accounts to manage workload clusters and their cloud resources. Also, Giant Swarm engineers need admin access to troubleshoot and resolve incidents (see [Giant Swarm support model](/support/overview)). Both of these permission sets are, as mentioned above, set up using AWS IAM policies once you become a Giant Swarm customer and start using one or more AWS accounts for Kubernetes clusters.

## AWS infrastructure of clusters

Giant Swarm workload clusters are managed by CAPA (Cluster API Provider AWS) and we offer clusters

- based directly on Kubernetes running on EC2 instances (see details below)
- _or_ based on EKS, the partially managed Kubernetes offering by AWS

### CAPA clusters running directly on EC2 instances (non-EKS)

![AWS workload cluster architecture](aws-workload-cluster-architecture.webp)

**VPC and subnets:** A cluster is deployed to a separate VPC that is normally automatically created together with the cluster. It is also possible to adopt your existing network when creating a cluster, such as existing VPC, subnets, etc.

**Node pools:** Each pool scales Kubernetes nodes as needed. By default, EC2 auto-scaling groups (ASGs) are used, controlled by cluster-autoscaler. You can provide a minimum and maximum number of workers and the number of nodes will adapt to how many pods need to be scheduled. Alternatively, Karpenter can be used to get more savings by choosing certain instance types depending on current needs in a cluster. The nodes in a pool can have different labels and properties so that you could use them for different purposes, such as having a small pool of very powerful instances on which only a specific, production-critical application is running. You can read more in [AWS Cluster scaling]({{< relref "/tutorials/fleet-management/cluster-management/aws-cluster-scaling" >}}).

**Networking:** A cluster always runs in a single VPC, and Kubernetes nodes are placed in private subnets, not exposed to the internet, but having internet access through NAT gateways. This is the default and recommended setup in _Cluster API Provider AWS_. If customization is needed, for example to access workloads in another AWS account through a fast connection, that is possible using transit gateways or VPC peering. As an option, Giant Swarm AWS clusters also support placing Kubernetes pod IPs directly on the AWS network (see [Cilium ENI mode]({{< relref "/tutorials/fleet-management/cluster-management/aws-cilium-eni-mode/" >}})) in case your network layout requires it. The default, however, is for the Cilium CNI to manage pod IPs, thereby supporting as many as possible.

**Exposing applications on the internet:** A load balancer (for example, ELB/NLB/ALB) is placed in the public subnet to balance the requests over the different backends.

**Extra IP ranges:** Clusters can optionally be extended to have multiple IP ranges (CIDRs). This may be necessary to accommodate your existing network structure or firewall rules.
