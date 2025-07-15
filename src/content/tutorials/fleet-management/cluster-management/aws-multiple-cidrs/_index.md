---
title: Multiple VPC CIDRs for AWS clusters
description: Allocate multiple CIDRs in order to scale the cluster or align a cluster with your existing network rules.
weight: 15
menu:
  principal:
    identifier: tutorials-fleet-aws-multiple-cidrs
    parent: tutorials-fleet-management-clusters
last_review_date: 2025-07-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How to assign multiple CIDRs to a cluster's VPC?
---

By default, AWS workload clusters on the Giant Swarm platform use a single VPC CIDR, for example `10.0.0.0/16`. In case of IP shortage, or if you need multiple IP ranges for other reasons, you can create a cluster with multiple CIDRs or add CIDRs to an existing cluster.

## Example (default Cilium mode)

In the cluster chart values, the connectivity properties ([reference](https://github.com/giantswarm/cluster-aws/blob/main/helm/cluster-aws/README.md#connectivity)) must be adapted to list all desired CIDRs. When extending an existing cluster, please make sure to keep the first CIDRs at the beginning of the list.

In this example, the cluster will have 3 CIDRs `10.{0,1,2}.0.0/16` and according subnets. Kubernetes worker nodes will automatically be distributed across these IP ranges.

```yaml
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        # [...]
        network:
          vpcCidrs:
            - 10.0.0.0/16
            - 10.1.0.0/16
            - 10.2.0.0/16
        subnets:
          - cidrBlocks:
              - cidr: 10.0.0.0/20
              - cidr: 10.0.16.0/20
              - cidr: 10.0.32.0/20
              - cidr: 10.1.0.0/20
              - cidr: 10.1.16.0/20
              - cidr: 10.1.32.0/20
              - cidr: 10.2.0.0/20
              - cidr: 10.2.16.0/20
              - cidr: 10.2.32.0/20
            isPublic: true
          - cidrBlocks:
              - cidr: 10.0.64.0/18
              - cidr: 10.0.128.0/18
              - cidr: 10.0.192.0/18
              - cidr: 10.1.64.0/18
              - cidr: 10.1.128.0/18
              - cidr: 10.1.192.0/18
              - cidr: 10.2.64.0/18
              - cidr: 10.2.128.0/18
              - cidr: 10.2.192.0/18
            isPublic: false
        # [...]
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: mycluster
  name: mycluster-userconfig
  namespace: org-test
```

## Example (Cilium in ENI mode)

When using [ENI mode]({{< relref "/tutorials/fleet-management/cluster-management/aws-cilium-eni-mode" >}}), meaning that pod IPs are directly mapped to AWS IPs, the configuration is very similar. You only need to list the pod IP CIDR as well and avoid overlap. Side note: having multiple pod CIDRs in ENI mode is currently not supported.

```yaml
apiVersion: v1
data:
  values: |
    global:
      connectivity:
        # [...]
        cilium:
          ipamMode: eni
        network:
          vpcCidrs:
            - 10.0.0.0/16
            - 10.1.0.0/16
            - 10.2.0.0/16
          pods:
            cidrBlocks:
              # The pod CIDR which will be added as secondary VPC CIDR,
              # putting pod IPs directly on the AWS network. No need to add
              # this CIDR to the above list since that is done automatically.
              - 10.50.0.0/16
        subnets:
          - cidrBlocks:
              - cidr: 10.0.0.0/20
              - cidr: 10.0.16.0/20
              - cidr: 10.0.32.0/20
              - cidr: 10.1.0.0/20
              - cidr: 10.1.16.0/20
              - cidr: 10.1.32.0/20
              - cidr: 10.2.0.0/20
              - cidr: 10.2.16.0/20
              - cidr: 10.2.32.0/20
            isPublic: true
          - cidrBlocks:
              - cidr: 10.0.64.0/18
              - cidr: 10.0.128.0/18
              - cidr: 10.0.192.0/18
              - cidr: 10.1.64.0/18
              - cidr: 10.1.128.0/18
              - cidr: 10.1.192.0/18
              - cidr: 10.2.64.0/18
              - cidr: 10.2.128.0/18
              - cidr: 10.2.192.0/18
            isPublic: false
        eniModePodSubnets:
          - cidrBlocks:
              - availabilityZone: a
                cidr: 10.50.0.0/18
                tags:
                  sigs.k8s.io/cluster-api-provider-aws/association: secondary
              - availabilityZone: b
                cidr: 10.50.64.0/18
                tags:
                  sigs.k8s.io/cluster-api-provider-aws/association: secondary
              - availabilityZone: c
                cidr: 10.50.128.0/18
                tags:
                  sigs.k8s.io/cluster-api-provider-aws/association: secondary
        # [...]
kind: ConfigMap
metadata:
  creationTimestamp: null
  labels:
    giantswarm.io/cluster: mycluster
  name: mycluster-userconfig
  namespace: org-test
```
