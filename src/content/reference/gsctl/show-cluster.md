---
title: "gsctl Command Reference: show cluster"
description: "The 'gsctl show cluster' command displays details of a cluster."
date: 2020-05-11
type: page
weight: 52
---

# `gsctl show cluster`

The `gsctl show cluster` command displays details on a cluster.

## Usage

```nohighlight
gsctl show cluster f0r14
```

You can also use the cluster's name for identifying the cluster:

```nohighlight
gsctl show cluster "Cluster name"
```

## Output details

Example output for an AWS based cluster featuring node pools:

```nohighlight
Cluster ID:                ggf8v
Name:                      Testing - Team upstate
Created:                   2020 May 04, 16:54 UTC
Organization:              acme
Kubernetes API endpoint:   https://api.ggf8v.REDACTED.aws.gigantic.io
Release version:           11.2.1
Labels:                    usage=testing
                           team=upstate
                           locked=false
Web UI:                    https://happa.ggf8v.REDACTED.aws.gigantic.io/organizations/acme/clusters/ggf8v
Master availability zones: eu-central-1b
Masters:                   1
Masters ready:             1
Size:                      3 nodes in 1 node pool
CPUs in nodes:             12
RAM in nodes (GB):         48

This cluster has node pools. For details, use

    gsctl list nodepools ggf8v

For details on a specific node pool, use

    gsctl show nodepool ggf8v/<nodepool-id>
```

Example output for a KVM based cluster:

```nohighlight
ID:                            tjjm7
Name:                          Staging Cluster
Created:                       2018 Mar 06, 14:23 UTC
Organization:                  acme
Kubernetes API endpoint:       https://api.tjjm7.REDACTED.kvm.gigantic.io
Release version:               2.2.1
Worker node scaling:           pinned to 2
Worker nodes running:          2
CPU cores in workers:          4
RAM in worker nodes (GB):      4
Storage in worker nodes (GB):  80
Ingress port for http:         30020
Ingress port for https:        30021
```

The output lines in detail:

- **ID:** unique cluster identifier
- **Name:** cluster name
- **Created:** date and time of cluster creation
- **Organization:** organization owning the cluster
- **Kubernetes API endpoint:** URL of the Kubernetes API for this cluster
- **Masters:** (_only for AWS_) Number of master nodes in the cluster
- **Master availability zones:** (_only for AWS_) Availability zone(s) of the master node(s)
- **Release version:** Version number of the release used in this cluster
- **Worker node scaling**: Scaling limits. Shows either `autoscaling between <min> and <max>` for an autoscaling cluster, or `pinned to <num>` where autoscaling is disabled or where it's not available.
- **Desired worker node count**: Only shown for autoscaling clusters. The number of worker nodes the autoscaler intends to have running.
- **Worker nodes running:** The current number of worker nodes running in this cluster.
- **Worker EC2 instance type:** (_only on AWS_) EC2 instance type used for worker nodes
- **Worker VM size:** (_only on Azure_) VM size used for worker nodes
- **CPU cores in workers:** total number of CPU cores in all worker nodes in this cluster
- **RAM in worker nodes (GB):** total amount of memory in all worker nodes in this cluster
- **Storage in worker nodes (GB):** (_only for KVM_) total amount of local storage in all worker nodes in this cluster
- **Ingress port for &lt;protocol&gt;:** (_only for KVM_) the port to forward traffic to from your data center's load balancer(s) to this cluster's ingress controller for that specific protocol
- **AWS account:** (_only on AWS_) If the cluster is running using non-default provider credentials, here we show the AWS account ID
- **Azure subscription:** (_only on Azure_) If the cluster is running using non-default provider credentials, here we show the subscription ID
- **Azure tenant:** (_only on Azure_) If the cluster is running using non-default provider credentials, here we show the tenant ID
- **Labels** (_only on AWS_) user defined labels. Only available for clusters with release version {{% first_aws_nodepools_version %}} and above on AWS

Note that some dynamic pieces of information, like the current number of workers, and the desired worker count, may take up to five minutes to be updated.

## Related

- [`gsctl list clusters`](../list-clusters/)
- [`gsctl scale cluster`](../scale-cluster/)
- [`gsctl delete cluster`](../delete-cluster/)
- [API: Get cluster details](/api/#operation/getCluster)
