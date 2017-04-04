+++
title = "Installing the Kubernetes Dashboard"
description = "The Dashboard is a general-purpose administrative web UI for Kubernetes, running in Kubernetes itself. It's easy to install."
date = "2016-10-14"
type = "page"
weight = 50
tags = ["recipe"]
+++

# Installing the Kubernetes Dashboard

[Kubernetes Dashboard](https://github.com/kubernetes/dashboard/) is the official general purpose web UI for Kubernetes clusters. It can show you all running workloads in your cluster and even includes some functionality to control and change those workloads. It can show logs of your pods and if you have Heapster monitoring installed also some basic resource usage.

![Kubernetes Dashboard](/img/dashboard-ui.png)

Keep in mind that Dashboard despite it 1.x version number is still an early-stage effort and might miss certain functionality (e.g. no cascaded deletes like `kubectl`).

## Deploying Dashboard

Deploying dashboard is easy and straight forward.

```nohighlight
kubectl create -f https://rawgit.com/kubernetes/dashboard/master/src/deploy/kubernetes-dashboard.yaml
```

Once the pod is running you can open Dashboard at `https://api.<cluster-id>.k8s.gigantic.io/ui`.

*Note*: The above URL uses your Kubernetes API to proxy to the service. As the API is guarded with your credentials, you need to [set them up in your system](/guides/accessing-services-from-the-outside/) (and/or browser). We do not recommend to set up an Ingress for the Dashboard at this time, as Dashboard currently does not support any kind of authentication and thus your cluster would be open to everyone.

If you want to have some simple metrics (as shown in the screenshot above) integrated in your Dashboard, you can additionally [install Heapster](/guides/kubernetes-heapster/).

Check out the [official user guide](http://kubernetes.io/docs/user-guide/ui/) for details on how to use Dashboard.
