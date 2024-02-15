---
title: Private clusters
description: Learn how to manage private clusters in Giant Swarm. A private cluster lets you limit the Kubernetes API access and at the same time control egress traffic of your workload using a proxy.
weight: 35
menu:
  main:
    parent: advanced-cluster-management
user_questions:
- How do I make a workload cluster private?
last_review_date: 2023-11-08
aliases:
  - /guides/private-clusters
  - /advanced/private-clusters
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

By default, Giant Swarm clusters expose the Kubernetes API endpoint publicly and the cluster workloads have internet access. In the following sections, we will explain different options to restrict inbound access to API or outbound connectivity to the internet within the clusters.

**Note**: You can skip this article unless you plan on creating clusters with strictly-limited networking.

The following options are available for restricting access:

- [Create a private cluster](#create-a-private-cluster)
- [Restrict Kubernetes API access to certain IP ranges (allowlisting)](#kubernetes-api-allowlist)

## Create a private cluster

The following implementations offer private cluster features:

- {{% impl_title "capa_ec2" %}}
- {{% impl_title "capz_vms" %}}

Private clusters have special requirements:

- Since a private workload cluster still has to be reachable by the management cluster, there must be networking peering between the two. This means that the IP ranges must not overlap.
- Access to the Kubernetes API can be restricted to an internal network. It should then be reachable both by you as customer, and by Giant Swarm for support purposes. For example, a VPN can be used.
- An HTTP proxy can be used to restrict which exact domains can be accessed at all. In this case, a precise configuration is essential or else the new cluster will not be able to fetch container images or reach other important resources such as internal communication to the Kubernetes API.

To get everything set up correctly, please get in contact with Giant Swarm. We will help creating and supporting your desired private cluster configuration within your network architecture.

At the moment, we have these [`kubectl gs template cluster` command line options]({{< relref "/vintage/use-the-api/kubectl-gs/template-cluster" >}}) to configure access to/from the cluster:

- `--cluster-type`
- `--vpc-mode`
- `--api-mode`
- `--http-proxy`/`--https-proxy`

We have a few provider-specific hints:

{{< tabs >}}
{{< tab id="private-cluster-capa-ec2-proxy" for-impl="capa_ec2" title-suffix=" (private, with proxy)" >}}

A proxy-private CAPA cluster uses a proxy to connect to the internet via HTTP/HTTPS. The cluster runs in a private VPC. The VPC CIDR (range of IPs) should be chosen such that it does not overlap with other VPCs that need to communicate with it. Please follow [Create a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}), adding certain parameters when running the cluster templating command:

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  \
  `# The following parameters are specific to creating a proxy-private cluster` \
  --cluster-type proxy-private \
  --vpc-mode private \
  --api-mode private \
  --vpc-cidr 10.226.0.0/18 `# please fill a desired, free VPC CIDR` \
  --http-proxy "http://my-http-proxy.example.com:8000" \
  --https-proxy "http://my-http-proxy.example.com:8000" \
  \
  > cluster.yaml
```

{{< /tab >}}
{{< tab id="private-cluster-capz-azure-vms" for-impl="capz_vms" title-suffix=" (private)" >}}

As getting the correct CIDR depend on the installation, please get in contact with your platform team to check for the next CIDR range to use. This step might become obsolete once a dedicated IPAM operator got implemented for private Azure clusters.

The below command will list all clusters for a given management cluster, their used CIDRs and the API server type (useful to differentiate between public and private/internal clusters):

```text
$ kubectl get azurecluster -A -o=custom-columns='NAMESPACE:.metadata.namespace,CLUSTER-NAME:.metadata.name,HOST-CIDR:.spec.networkSpec.vnet.cidrBlocks,CONTROLPLANE-CIDR:.spec.networkSpec.subnets[?(@.role=="control-plane")].cidrBlocks,WORKERS-CIDR:.spec.networkSpec.subnets[?(@.role=="node")].cidrBlocks,APISERVER-TYPE:.spec.networkSpec.apiServerLB.type'

NAMESPACE           CLUSTER-NAME   HOST-CIDR         CONTROLPLANE-CIDR   WORKERS-CIDR      APISERVER-TYPE
org-giantswarm      glippy         [10.223.0.0/24]   [10.223.0.128/26]   [10.223.0.0/25]   Public
org-multi-project   jrp45          [10.0.0.0/16]     [10.0.0.0/20]       [10.0.16.0/20]    Public
org-observability   ytc82          [10.223.2.0/24]   [10.223.2.128/27]   [10.223.2.0/25]   Internal
```

In the example output, the next usable CIDR range is `10.223.3.0/24` and therefore the cluster configuration will look like:

```yaml
# filename: cluster-private-config.yaml
metadata:
  name: bzm29
  organization: observability
providerSpecific:
  location: westeurope
  subscriptionId: 6b1f6e4a-6d0e-4aa4-9a5a-fbaca65a4711
connectivity:
  network:
    controlPlane:
      cidr: 10.223.3.128/26
    hostCidr: 10.223.3.0/24
    mode: private
    podCidr: 192.168.0.0/16
    serviceCidr: 172.31.0.0/16
    workers:
      cidr: 10.223.3.0/25
```

This will create a workload cluster in the subscription `6b1f6e4a-6d0e-4aa4-9a5a-fbaca65a4711` in Azure region `westeurope`.

As all default apps are bundled in `default-apps-azure`, its basic configuration must be also given:

```yaml
# filename: default-apps-azure-config.yaml
clusterName: "bzm29"
organization: "observability"
```

The cluster template can now be generated by running:

```sh
kubectl gs template cluster --provider capz --cluster-config cluster-private-config.yaml --default-app-config default-apps-azure-config.yaml --output cluster.yaml
```

{{< /tab >}}
{{< /tabs >}}

## Restrict Kubernetes API access to certain IP ranges (allowlisting) {#kubernetes-api-allowlist}

This feature works even if you have a public cluster. Restricting which IPs can access the Kubernetes API can be desired to limit the attack surface.

Requirements:

- The management cluster creates and manages the workload clusters. Therefore, the management cluster's outbound IPs, for example NAT Gateway IPs in AWS, must have access to the Kubernetes API of the workload clusters by adding them to the allowlist.
- Giant Swarm support engineers must have access to workload clusters in order to troubleshoot in case of alerts, incidents or customer requests. Our VPN IPs are therefore always part of the allowlist.

The following implementations support this feature:

- {{% impl_title "capa_ec2" %}}

Usage:

{{< tabs >}}
{{< tab id="cluster-capa-ec2" for-impl="capa_ec2" >}}

First of all, please [log into the management cluster]({{< relref "/vintage/getting-started/management-cluster" >}}).

As part of our guide [Create a workload cluster]({{< relref "/vintage/getting-started/create-workload-cluster" >}}) to template the cluster manifest, you will be instructed to run the command `kubectl gs template cluster [...]`. Please add the parameter `--management-cluster NAME_OF_MC` and, one or multiple times, `--control-plane-load-balancer-ingress-allow-cidr-block CIDR` to specify IP ranges (CIDRs) that should be allowed to access the Kubernetes API.

For example:

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  \
  `# Please fill in these values` \
  --management-cluster NAME_OF_MC \
  --control-plane-load-balancer-ingress-allow-cidr-block CIDR1 `# e.g. '1.2.3.4/30'` \
  --control-plane-load-balancer-ingress-allow-cidr-block CIDR2 `# e.g. '5.6.7.8/30'` \
  \
  > cluster.yaml
```

The command will automatically fetch outbound IPs of the management cluster (typically 3 NAT Gateway IPs which are permanent) and add them to the list of IP ranges you provided. You will find the output in the list [`controlPlane.loadBalancerIngressAllowCidrBlocks`](https://github.com/giantswarm/cluster-aws/blob/master/helm/cluster-aws/README.md#control-plane) of the produced YAML:

```yaml
apiVersion: v1
data:
  values: |
    # [...]
    controlPlane:
      # [...]

      # This list gets added (without the comments)
      loadBalancerIngressAllowCidrBlocks:
        # Management cluster's outbound IPs (NAT Gateway IPs).
        - a.b.c.d/32
        - e.f.g.h/32
        - i.j.k.l/32

        # Your own, provided list of IP ranges that should have access
        - m.n.o.p/xx
        - q.r.s.t/yy

    # [...]
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: mycluster
  name: mycluster-userconfig
  namespace: org-testing
# [...]
```

{{< /tab >}}
{{< /tabs >}}
