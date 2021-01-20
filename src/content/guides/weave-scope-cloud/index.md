---
title: "Setting up Weave Scope or Weave Cloud"
description: "Recipe to spin up the Weave Scope UI or Weave Cloud on Kubernetes."
type: page
weight: 120
tags: ["recipe"]
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# Setting up Weave Scope or Weave Cloud

Weave Scope is a UI that lets you see and interact with distributed applications and their containers in your cluster in real time. Weave Cloud is a hosted version of Weave Scope.

## Weave Scope

![Screenshot of the Weave Scope UI](/img/weave_scope_topology.png)

It builds logical topologies of your applications and cluster and let's you filter and search through what is running. You get real-time app and container metrics and can manage your containers directly from within the UI.

![Screenshot of a detail view in Weave Scope](/img/weave_scope_details.png)

It is very easy to set up as it does not need any configuration or integration. It automatically bootstraps directly from your Kubernetes cluster. A single command will get you up and running:

```bash
kubectl apply --namespace kube-system -f "https://cloud.weave.works/k8s/scope.yaml?k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

This creates a service and a daemon set launching the necessary components. For more details on the installation check out the [official Weave Scope installation documentation](https://www.weave.works/docs/scope/latest/installing/#k8s) .

Once everything is running you can open the UI at `https://api.<cluster-id>.k8s.gigantic.io/api/v1/proxy/namespaces/weavescope/services/weavescope-app:80/`.

*Note*: The above URL uses your Kubernetes API to proxy to the service. As the API is guarded with your credentials, you need to [set them up in your system](/guides/accessing-services-from-the-outside/) (and/or browser). We do not recommend to set up an Ingress for the Weave Scope UI at this time, as its dashboard currently does not support any kind of authentication and thus your cluster would be open to everyone.

For an overview of what Weave Scope can do and how to use it check out the [Weave Scope User Guide](https://www.weave.works/docs/scope/latest/introducing/).

## Weave Cloud

If you want to use the hosted cloud version of this UI you can sign up for an account at [the Weave website](https://cloud.weave.works) and obtain a service-token. Using this service token you then start Weave Scope with the following command (instead of the one above):

```bash
kubectl apply --namespace kube-system -f "https://cloud.weave.works/k8s/scope.yaml?service-token=<token>&k8s-version=$(kubectl version | base64 | tr -d '\n')"
```

You can then check out Weave Cloud to see and interact with your applications.
