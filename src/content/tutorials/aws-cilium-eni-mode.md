---
title: Cilium ENI IPAM mode for AWS
description: Allocate pod IPs directly on the AWS network using a second VPC CIDR.
weight: 10
last_review_date: 2024-05-02
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How to assign AWS-allocated IPs to pods?
  - How do I change the pod network CIDR?
---

<!--

A workload cluster can be configured to choose pod IPs from an AWS-allocated IP range (CIDR). In this mode, the Cilium CNI [allocates ENIs (Elastic Network Interfaces) and pod IPs](https://docs.cilium.io/en/latest/network/concepts/ipam/eni/).

## Advantages

- Pods get directly assigned IPs, belong to an AWS subnet and are assigned to a separate security group. This allows handling pod traffic separately, for example firewalling or peering.
- Pod traffic is not translated by NAT. The pod IPs can be visible in a peered VPC or behind a transit gateway.

## Disadvantages

- Strong limitation for number of pods – each AWS EC2 instance type has a certain maximum number of ENIs (Elastic Network Interfaces) and each of those has a maximum number of assignable IPs (see [AWS documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html#AvailableIpPerENI)). For example, instance type XXX can host up to YYY ENIs and therefore ZZZ pods (TODO). This can lead to higher costs because fewer pods can be run on each node, given this networking restriction, even if more would fit based on available CPU and memory.
- A large CIDR is recommended for the pod network, as each pod will use one IP. This could be a problem if your chosen CIDR must not overlap with others in your network, and you don't have enough CIDRs left to choose from.

## Creating an AWS workload cluster with Cilium ENI IPAM mode

- Must be enabled at creation of the workload cluster.
- When templating the cluster using the `cluster-aws` chart

  - Set value [`global.connectivity.cilium.ipamMode=eni`](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#connectivity)
  - Set value [`global.connectivity.network.pods.cidrBlocks`](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#connectivity) to the CIDR you want for the pods. This will be associated as secondary CIDR to the VPC. We recommend the value `10.1.0.0/16`. If you need a different CIDR, please also set [`global.connectivity.eniModePodSubnets`](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#connectivity), for example by copy-pasting the documented default list of subnets and changing the CIDR split (default: `10.1.0.0/16` split into three subnet blocks `10.1.0.0/18`, `10.1.64.0/18`, `10.1.128.0/18`).

Template a regular cluster (refer to (TODO link to "Creating a workload cluster" getting-started guide)):

```sh
kubectl gs template cluster \
  --provider capa \
  --name mycluster \
  --organization testing \
  > cluster.yaml
```

Open the YAML file in an editor. It should look roughly like this:

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        availabilityZoneUsageLimit: 3
        network: {}
        topology: {}
      controlPlane: {}
      metadata:
        name: mycluster
        organization: testing
      # [...]
kind: ConfigMap
metadata:
  # [...]
  name: mycluster-userconfig
  namespace: org-testing
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  # [...]
  name: mycluster
  namespace: org-testing
spec:
  catalog: cluster
  # [...]
  name: cluster-aws
  namespace: org-testing
  userConfig:
    configMap:
      name: mycluster-userconfig
      namespace: org-testing
  version: # [...]
```

Choose a CIDR for the pod network.

Edit the values in the YAML file:

TODO highlight the changed lines (Hugo supports it: https://gohugo.io/content-management/syntax-highlighting/#highlight-shortcode)

```yaml
---
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        availabilityZoneUsageLimit: 3
        cilium:
          ipamMode: eni
        # eniModePodSubnets: <list of subnets> # see above hint - you only need to fill this if the pod CIDR isn't `10.1.0.0/16`
        network:
          pods:
            cidrBlocks:
              - 10.1.0.0/16
        topology: {}
      controlPlane: {}
      metadata:
        name: mycluster
        organization: testing
      # [...]
kind: ConfigMap
# [...]
```

Create the workload cluster as usual (TODO link to "Creating a workload cluster" getting-started guide):

```sh
kubectl apply -f cluster.yaml
```

After a few minutes, the cluster should be up. In the AWS EC2 console, you will find the secondary VPC CIDR (pod network), and EC2 instances having secondary network interfaces which list their currently allocated pod IPs:

TODO screenshot(s)

-->
