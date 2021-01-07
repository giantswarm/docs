---
title: Creating workload clusters via the Management Cluster API
description: This guide will walk you through the process of workload cluster creation via Control Plane Kubernetes.
type: page
weight: 100
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
---

# Creating workload clusters via the Management Cluster API

Here we explain how to create clusters using the [Control Plane Kuebernetes API](/basics/api/#cp-k8s-api). This API lets you work directly with custom resources (CRs), which are specific for the cloud provider you are running on.

**Note:** At this point, bare metal (KVM) is not supported yet.

## Select your cloud provider

- [Amazon Web Servics (AWS)](/guides/creating-clusters-via-crs-on-aws/)
- [Azure](/guides/creating-clusters-via-crs-on-azure/)
