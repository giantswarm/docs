---
linkTitle: Exposing workloads
title: Accessing pods and services from the outside
description: You can access pods and services from outside your cluster either through the API proxy or through ingress.
weight: 60
menu:
  main:
    parent: getting-started
user_questions:
  - How can I connect to a pod running in a cluster?
  - How can I expose a TCP port of a pod to the internet?
  - How can I expose a service to the internet?
  - How to configure the host name in ingress?
  - What is the right URL format for the Kubernetes API proxy?
owner:
  - https://github.com/orgs/giantswarm/teams/team-ludacris
---

# Accessing pods and services from the outside

Once you have a pod or service running on your cluster, you might want to access it from outside your cluster. There are currently three ways to do that:

- [Public access to a service through ingress](#public-ingress): This is the right method to publish an application, defined through a service in Kubernetes, for access by everybody.
- [Authenticated access to a pod through `kubectl port-forward`](#port-forward): This gives you direct network access to a port of a pod, for test purposes.
- [Authenticated access to a service through the API proxy](#api-access): This gives you access to a Kubernetes service, for test purposes.

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

Your workload cluster needs an ingress controller installed. If you haven't done that yet, see [installing an ingress controller]({{< relref "/getting-started/ingress-controller" >}}) for instructions.

You can expose services publicly by setting up a simple ingress. You can do this with an ingress manifest.

Let's look at the following YAML, which you can use as a template for your ingress manifest:

```yaml
apiVersion: networking.k8s.io/v1beta1
kind: Ingress
metadata:
  name: INGRESS_NAME
  namespace: NAMESPACE
spec:
  rules:
  - host: PREFIX.CLUSTER_ID.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: SERVICE_NAME
          servicePort: SERVICE_PORT
```

All parts in uppercase letters are placeholders, to be replaced according to your individual requirements. In detail:

- `INGRESS_NAME`: This name identifies the ingress within your namespace. As with all other kubernetes, it's up to you how you name it.
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
http://PREFIX.CLUSTER_ID.k8s.gigantic.io
```

Currently, this is limited to exposing by default on port `80`. Support for TLS will be added soon.

For additional features and options, please see our documentation around [advanced ingress configuration]({{< relref "/advanced/ingress/configuration" >}}).

## Forwarding an authenticated port with `kubectl port-forward` {#port-forward}

Forwarding a port with `kubectl` is fairly easy, however, it only works with single pods and not with services. Thus you need the exact pod name. You can either get this manually by running

```nohighlight
kubectl -n NAMESPACE get pods
```

and looking for the right pod name. Or by running following script.

```nohighlight
POD=$(kubectl get pods -n NAMESPACE --selector <label-key>=<label-value> \
    -o template --template '{{range .items}}{{.metadata.name}} {{.status.phase}}{{"\n"}}{{end}}' \
    | grep Running | head -1 | cut -f1 -d' ')
```

Be sure to have your pod labeled accordingly so you can find it with the above selector.

After this you can run

```nohighlight
kubectl port-forward -n NAMESPACE ${POD} <local-port>:<pod-port>
```

or to have it running in the background

```nohighlight
kubectl port-forward -n NAMESPACE $POD <local-port>:<pod-port> &
```

Now you can access your pod locally via `localhost:<local-port>`.

## Access any service from through the API proxy {#api-access}

The Kubernetes API comes with an inbuilt proxy, which you can use to access services deployed on your cluster. The URL schema is

```nohighlight
https://api.CLUSTER_ID.k8s.gigantic.io/api/v1/proxy/namespaces/NAMESPACE/services/SERVICE_NAME:PORT_NAME/proxy/
```

If the service does not use a named port, `PORT_NAME` must be the port number.

Access will only be granted to clients which

- trust the API's server certificate, which means they trust the Certificate Authority (CA) that signed it and
- provide a valid client certificate.

The Giant Swarm [web user interface]({{< relref "/ui-api/web/" >}}) shows you how to obtain the certificate files.

To make these certificates available to HTTP clients/browsers, see our guide [Establishing Trust to Your Cluster's CA and Importing Certificates]({{< relref "/getting-started/ca-certificate" >}}) which explains this for different clients on various platforms.

### Example

Assuming you have a service `elasticsearch` with a port named `es` in the `logging` namespace, you could
access the Elasticsearch index stats API like this:

```nohighlight
curl -v -u username:password \
  --cacert ./ca.pem \
  --cert ./crt.pem \
  --key ./key.pem \
  https://api.CLUSTER_ID.k8s.gigantic.io/api/v1/namespaces/logging/services/elasticsearch:es/proxy/_stats
```

## Further reading

- [Establishing Trust to Your Cluster's CA and Importing Certificates]({{< relref "/getting-started/ca-certificate" >}})
- [Official Kubernetes documentation for the ingress resource](https://kubernetes.io/docs/concepts/services-networking/ingress/)
- [Official Kubernetes documentation for the kubectl port-forward](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#port-forward/)
- [Official Kubernetes documentation for accessing services running on the cluster](https://kubernetes.io/docs/tasks/access-application-cluster/access-cluster/#accessing-services-running-on-the-cluster)
