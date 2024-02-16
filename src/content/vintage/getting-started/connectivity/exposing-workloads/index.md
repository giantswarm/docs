---
title: Exposing workloads
description: You can access pods and services from outside your cluster either through the API proxy or through ingress.
weight: 80
menu:
  main:
    parent: gettingstarted-connectivity
user_questions:
  - How can I connect to a pod running in a cluster?
  - How can I expose a TCP port of a pod to the internet?
  - How can I expose a service to the internet?
  - How to configure the host name in ingress?
aliases:
  - /getting-started/connectivity/exposing-workloads
  - /guides/accessing-services-from-the-outside/
  - /getting-started/exposing-workloads/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2023-11-27
---

Once you have some workload running on your cluster, you might want to access it from outside your cluster. Creating an Ingress resource is the canonical way to do that:

## Setting up a public ingress {#public-ingress}

Before we explain how to set up ingress for a service, please read the next section carefully to make sure the guide matches your situation as a Giant Swarm user.

### Knowing your ingress base domain {#base-zone}

Setting up ingress means to make services publicly available via DNS names. For an application facing the public, you will eventually want to set up names ending in your own domain.

However, for development or test purposes, you can use the fact that every Giant Swarm installation maps to a DNS zone. We call this the **ingress base domain**.

In our cloud installation, for example, the ingress base domain is

<pre class="placeholder-immutable">
<code class="language-nohighlight">.k8s.gigantic.io</code>
</pre>

So ingresses can automatically use the following DNS name schema:

<pre class="placeholder-immutable">
<code class="language-nohighlight">PREFIX.CLUSTER_ID.k8s.gigantic.io</code>
</pre>

We'll explain in a minute what `PREFIX` and `CLUSTER_ID` are.

### Adapt this tutorial for you {#adapt}

To make the rest of the tutorial match your situation, please set your ingress base domain in the field below:

<form action="./" method="GET" class="form-inline placeholder-immutable">
  <div class="form-group">
    <label for="ingressBaseDomainInput">Ingress base domain</label>:
    <input name="basedomain" class="placeholder-immutable form-control" id="ingressBaseDomainInput" type="text" autocomplete="on" placeholder=".k8s.gigantic.io" />
  </div>
  <button id="ingressBaseDomainApplyButton" type="submit" class="btn btn-default">Apply</button>
</form>

### Setting up ingress {#setting-up-ingress}

Your workload cluster needs an ingress controller installed. If you haven't done that yet, see [installing an ingress controller]({{< relref "/vintage/getting-started/connectivity/ingress-controller" >}}) for instructions.

You can expose services publicly by setting up a simple ingress. You can do this with an ingress manifest.

Let's look at the following YAML, which you can use as a template for your ingress manifest:

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: INGRESS_NAME
  namespace: NAMESPACE
spec:
  ingressClassName: nginx
  rules:
  - host: PREFIX.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: SERVICE_NAME
            port:
              number: SERVICE_PORT
```

All parts in uppercase letters are placeholders, to be replaced according to your individual requirements. In detail:

- `INGRESS_NAME`: This name identifies the ingress within your namespace. As with all other Kubernetes resources, it's up to you how you name it though the advice is to align with your service name.
- `NAMESPACE`: The namespace of the service you'd like to expose. The ingress must reside in the same namespace, so it's useful to make it part of the metadata in the manifest.
- `PREFIX`: A subdomain name of your choice. This must be unique among all ingresses of this cluster. If you like, you can make this the same as `INGRESS_NAME`.
- `CLUSTER_ID`: The ID of the Kubernetes cluster the service you'd like to expose is running on. This should be a string consisting of five letters and numbers.
- `SERVICE_NAME`: The name of your service, as defined in the `metadata.name` attribute of your service's manifest.
- `SERVICE_PORT`: The port of your service to connect to, as defined in the `spec.ports` array of your service's manifest.

The `host` attribute defines the fully qualified host name via which your service will be accessible. As you can see, it consists of your self-chosen prefix, your cluster ID, and finally the ingress base domain.

Once you adapted the template above to according to your requirements and stored it to a file named e. g. `ingress.yaml`, you can create your ingress using `kubectl`:

```nohighlight
kubectl apply -f ingress.yaml
```

It will take a moment for the ingress to be created. You can look up the new ingress using `kubectl` like this (replacing `NAMESPACE` and `INGRESS_NAME`):

```nohighlight
kubectl -n NAMESPACE describe ing/INGRESS_NAME
```

Once the ingress is up, you will be able to access your service publicly at a URL like this (again replacing the placeholders):

```nohighlight
https://PREFIX.CLUSTER_ID.k8s.gigantic.io
```

For additional features and options, please see our documentation around [advanced ingress configuration]({{< relref "/vintage/advanced/connectivity/ingress/configuration" >}}).

## Forwarding ports with `kubectl port-forward` {#port-forward}

Forwarding a port with `kubectl` is fairly easy, however, it should be only used for debugging purposes.

To know more about forwarding TCP ports using `kubectl port-forward`, you should read the ["Use Port Forwarding to Access Applications in a Cluster"](https://kubernetes.io/docs/tasks/access-application-cluster/port-forward-access-application-cluster/) page in the official Kubernetes documentation.

## Further reading

- [Establishing Trust to Your Cluster's CA and Importing Certificates]({{< relref "/vintage/getting-started/ca-certificate" >}})
- [Official Kubernetes documentation for the ingress resource](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Official Kubernetes documentation for the kubectl port-forward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward/)
- [Official Kubernetes documentation for accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#accessing-services-running-on-the-cluster)
