+++
title = "Details on Kubernetes on Giant Swarm"
description = "Here you learn how we set up things for you and what we manage, so you don't have to."
date = "2017-02-16"
type = "page"
weight = 10
categories = ["basics"]
+++

# Details on Kubernetes on Giant Swarm

With Giant Swarm you get a fully-managed Kubernetes cluster, which you can then use to deploy your containers as you see fit. You have full admin rights to the cluster through its API, so you can change anything that is accessible through the Kubernetes API. Changes that require configuration of the Kubernetes components themselves (e.g. starting the API server or kubelets with specific arguments) need to be set by the Giant Swarm Ops team. If you have specific needs or feedback, don't hesitate to [get in touch](mailto:support@giantswarm.io)

## What is included

Your cluster comes out-of-the-box as follows:

- Single Master with resilient etcd
- Resiliently deployed worker nodes
- Full end-to-end encryption between Kubernetes components
- Regularly rolling keys for above-mentioned encryption
- Calico networking plugin installed (supports Network Policies)
- KubeDNS installed
- Most alpha resources enabled (talk to us if you need more)
- Nginx Ingress Controller (running inside your cluster)

## What is not included

There are some things not included in the cluster as managed by us:

- Additional userspace services like Dashboard, Monitoring, Logging, Registry, etc. are not installed (Getting them running is [really easy](/guides/), though)
- Persistent storage is not set up (Coming soon)
- TLS & custom domains for Ingress (Coming soon)

## High Availability and Resilience

As mentioned above your cluster has a single running master. However, the cluster is set up in a way that your cluster keeps running even if the master is unavailable for a while (e.g. due to planned upgrades, failure, etc.), the only slight degradation you might notice is that while the master is down, you cannot change the state of your pods and other resources. As soon as the master is up again, you regain full control.

Further, Kubernetes takes care of syncing your cluster with your desired state, so even when a node goes down (again e.g. due to planned upgrades, failure, etc.), pods will get restarted/rescheduled if they are not running once it comes up again. If the node was away due to a netsplit, the pods might still be running. In that case the scheduler might have added more pods to other nodes while the node was away so it will remove some pods again to be consistent with your desired number of replicas.

## Specifities of your cluster

As we are taking care of your cluster, we need to run some agents (e.g. for monitoring or storage) in your cluster. Due to this fact some host ports might be already in use. Currently, that is limited to port `91`, which is used by the monitoring agent. If you run into issues with that, please [get in touch](mailto:support@giantswarm.io) and we will find a solution.

Similarly, some parts of the DNS, Ingress Controller, and Calico setups are visible to you inside your cluster. To ensure that your cluster runs without problems, please refrain from manipulating the `kube-system` and `calico-system` namespaces as well as the pods and other resources running in them if they are not documented.
