---
linkTitle: Vertical Pod Autoscaler
title: Vertical Pod Autoscaler
description: Guide explaining how to use the Vertical Pod Autoscaler to automatically adjust your pod resources.
menu:
  main:
    identifier: getting-started-operations-autoscaling-verticalpodautoscaler
    parent: getting-started-operations-autoscaling
weight: 100
aliases:
  - /operations/autoscaling/vertical-pod-autoscaler
last_review_date: 2023-08-16
user_questions:
  - What is the Vertical Pod Autoscaler?
  - How can I reduce resource usage of my pods?
  - How does the Vertical Pod Autoscaler works?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

## Introduction

Giant Swarm workload clusters provide the [Vertical Pod Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler) (VPA) by default, to either recommend or automatically increase or reduce your pod's resource requests and limits based on the current resource usage.

## Architecture overview

![Architecture diagram of the Vertical Pod Autoscaler](vpa-architecture.png)
<!-- Source: https://github.com/kubernetes/design-proposals-archive/blob/main/autoscaling/images/vpa-architecture.png -->
(credit: [upstream design proposal](https://github.com/kubernetes/design-proposals-archive/blob/main/autoscaling/vertical-pod-autoscaler.md#architecture-overview))

## Common pitfalls

### VPA sets the container's requests

The container's limits will be defined according to its original ratio.

Let's see it with an example:
* my original fluentbit pod was set with `requests: 200Mi` and `limits: 300Mi`.
* VPA increases it to `requests: 400Mi`, it also sets `limits: 600Mi`.
* Notice that now the RAM limit can be higher than the VPA's `maxAllowed`.

See [upstream doc](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler#keeping-limit-proportional-to-request) for more information.

### Containers grow bigger than available resources

There's 2 things that you may aim for with VPA:
- reserve guaranteed minimum available resources for your container (`requests` management)
- limit maximum resource usage for your container (`limits` management)

When a container uses too much resources, keep in mind that [VPA sets the container's requests](#vpa-sets-the-containers-requests) and `limits` proportionally, keeping the original requests/limits ratio.

When setting `maxAllowed` (max allowed requests) values:
- make sure that the requests won't go over the node's resources, which would make the container unschedulable.
- watch out for the max VPA computed limits. While it won't lead to an unschedulable container it may kill your node.

If you want to make sure your container won't use more resources than `maxAllowed`, set `limits`=`requests` at container creation.

### CPU and RAM strategies

Scaling down resources is made according to the past usage.
But scaling up is a bit more complex. Especially when `limits`=`requests`.

#### CPU settings

If your limit is higher than your requests, and your container uses more CPU than the requests, VPA will scale it up.

But if `limits`=`requests`, your container will never use more CPU than its `limit/requests`, so CPU exhaustion must be checked another way.
CPU throttling is a good signal for VPA to scale up the container, but this does not always work.

So, you should keep some room above the `requests` for CPU to grow, to ease VPA scaling up your container.

#### RAM settings

For RAM, VPA monitors Out Of Memory (OOM) errors.
When a containers dies OOM, VPA knows that it should bump up RAM requests/limits.

So, for RAM, there should be no big problem with setting `limits`=`requests`.



## Further reading

- [Vertical Pod Autoscaler design proposals](https://github.com/kubernetes/design-proposals-archive/blob/main/autoscaling/vertical-pod-autoscaler.md) 
- [Vertical Pod Autoscaler App](https://github.com/giantswarm/vertical-pod-autoscaler-app)
