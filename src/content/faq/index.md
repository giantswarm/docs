---
title: FAQ
description: Frequently Asked Questions
date: 2019-10-24
type: page
---

# FAQ

## In what data centers does Giant Swarm run clusters?

Giant Swarm runs on AWS, Microsoft Azure, and on bare metal or virtualized hardware using KVM.

## How can I create backups or snapshots from volumes?

We currently don't provide this as a service. You have to take care of it yourself. You can use S3 or other storage solutions.

If your cluster is running on AWS using your own AWS account, you can use the [EBS Snapshot](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) function.

## Can I run a database?

Yes, for most databases there are ready built containers in the [Docker Hub](https://hub.docker.com/). If you can't find one for your database of choice, you should be able to easily build one. However, currently persistent volumes are only available on AWS. With a bare metal (KVM) based cluster, volumes are not persistent and won't survive rescheduling of their pods.

Check out our guide on [using persistent volumes on AWS](https://docs.giantswarm.io/guides/using-persistent-volumes-on-aws/).

## Can I use TLS/HTTPS/SSL?

Yes. Take a look at our [advanced ingress guide](https://docs.giantswarm.io/guides/advanced-ingress-configuration/#tls).

## Can I use websockets?

Currently not, but we are working on it.

## Can I use a third party private registry?

Yes, you just need to set up an [ImagePullSecret](http://kubernetes.io/docs/user-guide/images/#specifying-imagepullsecrets-on-a-pod) for your pod.

For AWS-based clusters, using the [AWS EC2 Container Registry](https://aws.amazon.com/ecr/) (ECR) requires specific configuration of the worker nodes. The EC2 instance policies need specific permissions, which are listed in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/containers/images/#using-aws-ec2-container-registry).

## How can I run a container periodically?

The [Cron Job](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/) resource is available to you.

## Which IP Block do I need to reserve for my full Giant Swarm installation on AWS?

There are different answers to this, and some depend on your requirements. We advise that you think about where you want to go with your Giant Swarm Platform in light of the limits you might impose based on a smaller IP Block. The following is a hopefully well argued possible solution. 

First we need IP space for our control plane and tenant clusters, meaning the underlying EC2 machines. We currently suggest taking a Class C IP Block per tenant cluster, as this would allow some 240 machines or 120 if spread over two Availability Zones. While taking a full Class B IP Block would mean you can start well over 200 clusters, or e.g. 80 in three different Amazon Locations, you might be ok with using a smaller IP Range. These IPs, in case you somehow want IP to IP connections to those machines, need to be routable inside your old environment. Normally these can run over a NAT but still, the IPs should not be used inside your existing network in case systems inside the cluster need to talk to some of your old IPs, e.g. a database.

Then we need a class B IP Block for the internal Calico based network between containers, that will be reused within each cluster as the will not bleed out. These do not need to be routed, but reserved internally and use nowhere else in case we need to talk to IPs outside the cluster.

Lastly, we need internal IP space for K8s services and we advise 172.31.0.0 for it because that is what is used as a default on many of the examples out there. Otherwise we can also split up a few from the Class B for the containers.
