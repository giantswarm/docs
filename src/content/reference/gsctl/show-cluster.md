+++
title = "gsctl Command Reference: show cluster"
description = "The 'gsctl show cluster' command displays details of a cluster."
date = "2018-03-07"
type = "page"
weight = 52
+++

# `gsctl show cluster`

The `gsctl show cluster` command displays details on a cluster.

## Usage

```nohighlight
gsctl show cluster <cluster-id>
```

## Output details

Example output for an AWS based cluster:

```nohighlight
ID:                            vxvc7
Name:                          Staging cluster for Frontend
Created:                       2017 Sept 29, 09:26 UTC
Organization:                  giantswarm
Kubernetes API endpoint:       https://api.vxvc7.REDACTED.aws.gigantic.io
Release version:               n/a
Workers:                       3
Worker instance type:          m3.large
CPU cores in workers:          6
RAM in worker nodes (GB):      22.5
Storage in worker nodes (GB):  96
```

Example output for a KVM based cluster:

```nohighlight
ID:                            tjjm7
Name:                          Staging Cluster
Created:                       2018 Mar 06, 14:23 UTC
Organization:                  giantswarm
Kubernetes API endpoint:       https://api.tjjm7.REDACTED.kvm.gigantic.io
Release version:               2.2.1
Workers:                       2
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
- **Release version:** Release used in this cluster
- **Workers:** Number of worker nodes in this cluster
- **Worker instance type:** (_only on AWS_) EC2 instance type used for worker nodes
- **Worker VM size:** (_only on Azure_) VM size used for worker nodes
- **CPU cores in workers:** total number of CPU cores in all worker nodes in this cluster
- **RAM in worker nodes (GB):** total amount of memory in all worker nodes in this cluster
- **Storage in worker nodes (GB):** total amount of local storage in all worker nodes in this cluster
- **Ingress port for &lt;protocol&gt;:** the port to forward traffic to from your data center's load balancer(s) to this cluster's ingress controller for that specific protocol

## Related

- [`gsctl list clusters`](../list-clusters/)
- [`gsctl scale cluster`](../scale-cluster/)
- [`gsctl delete cluster`](../delete-cluster/)
- [API: Get cluster details](/api/#operation/getCluster)
