+++
title = "FAQ"
description = "Frequently Asked Questions"
date = "2017-02-16"
type = "page"
+++

# FAQ

## Can I use my own domain?

Currently, you can only setup an [ingress](/guides/accessing-services-from-the-outside/) that exposes a sub-domain of `<cluster-id>.k8s.gigantic.io`. Full (personal) custom domains will be available soon.

## How can I create backups or snapshots from volumes?

We currently don't provide this as a service. You have to take care of it yourself. You can use S3 or other storage solutions.

## Can I run a database?

Yes, for most databases there are ready built containers in the [Docker Hub](https://hub.docker.com/). If you can't find one for your database of choice, you should be able to easily build one. However, currently persistent volumes are not available so your volumes won't survive rescheduling of their pods.

## How do I make pods talk to each other?

For pods to be available to other pods or to the outside you need to expose them through a service. See [Kubernetes Fundamentals](/basics/kubernetes-fundamentals/) for more details.

## How can I provide environment variables for the containers?

You can either define environment variables in your deployment or better use ConfigMaps and/or Secrets. See [Kubernetes Fundamentals](/basics/kubernetes-fundamentals/) for more details.

## Can I use TLS/HTTPS/SSL?

TLS will be available for [ingress](/guides/accessing-services-from-the-outside/) soon.

## Can I use websockets?

Currently not, but we are working on it.

## Can I use a third party private registry?

Yes, you just need to set up an [ImagePullSecret](http://kubernetes.io/docs/user-guide/images/#specifying-imagepullsecrets-on-a-pod) for your pod.

## How can I run a container periodically?

Currently, Scheduled Jobs are still in Alpha, but there's a workaround: Create a dedicated container running a script in an endless loop that triggers the actual job to be run periodically.
