---
title: "Scheduling Constraints and Resource Quality of Service"
description: "How you can constrain resource usage and define Quality of Service classes in Kubernetes"
type: page
weight: 70
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Scheduling Constraints and Resource Quality of Service

Kubernetes provides resource Quality of Service (QoS) to Pods based on what resources they request and what limits are set for them.

The QoS is enforced automatically based on the constraints you set for your Pods in their specification.

## Defining resource constraints for Pods

You can specify requests and limits for CPU and RAM usage for each container of a Pod by setting:

- `spec.container[].resources.limits.cpu`
- `spec.container[].resources.limits.memory`
- `spec.container[].resources.requests.cpu`
- `spec.container[].resources.requests.memory.`

If request values are not set, they default to the value set as limit. Note that limits must always be equal to or greater than requests.

The requests and limits of a Pod are defined by the sum of the respective values of all its containers (unset values are treated as zero depending on your cluster configuration).

### CPU

CPU resoures are measured in (v)Core equivalents. You can specify them in decimals (e.g. `0.5` meaning half a core) or in `milicpu` (e.g. `500m` meaning half a core).

### Memory

Memory resources are measured in bytes. You specify them as decimals with one of SI suffixes (E, P, T, G, M, K) or their power-of-two equivalents (Ei, Pi, Ti, Gi, Mi, Ki). For example, the following represent roughly the same value: 128974848, 129e6, 129M, 123Mi.

## How Pods are scheduled

When a pod is created, the Kubernetes scheduler selects a node for the Pod to run on. Each node has a maximum capacity for RAM and CPU. The scheduler ensures that, for each resource type, the sum of the resource requests (not limits!) of the containers scheduled to the node is less than the capacity of the node.

Note that even when actual memory or CPU usage might be low, the scheduler will still refuse to place pods onto nodes if the capacity check fails. This protects against a resource shortage when resource usage increases, e.g. due to a daily peak or other kind of load increase.

## Resource guarantees

Kubernetes differentiates between compressible and incompressible resources. Former currently supports CPU and latter currently only Memory.

For compressible resources, Pods are guaranteed to get the amount they requested, they might or might not get additional resources. If Pods exceed their limits they will be throttled accordingly. If no limit is set they may use as much of the compressible resource as available.

For incompressible resources, Pods are guaranteed to get the amount they requested. If they exceed their request they might get killed (e.g. when another pod requests more of the resource). If Pods use more than their limit, the process that is using the most amount of memory, inside one of the Pod's containers, will be killed by the kernel.

## Quality of service classes

There are three QoS classes for Pods: Guaranteed, Burstable, and Best-Effort.

If `limits` and optionally `requests` (not equal to `0`) are set for all resources across all containers and they are equal, then the pod is classified as __Guaranteed__.

If `requests` and optionally `limits` are set (not equal to `0`) for one or more resources across one or more containers, and they are not equal, then the pod is classified as __Burstable__. When `limits` are not specified, they default to the node capacity.

If `requests` and `limits` are not set for all of the resources, across all containers, then the pod is classified as __Best-Effort__.

## Further reading

- [Managing Resources for Containers](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/)
- [Pod Quality of Service in Kubernetes](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/)
