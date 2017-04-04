+++
title = "Accessing Pods and Services from the outside"
description = "You can access Pods and services from outside your cluster either through the API proxy or through an Ingress."
date = "2017-02-23"
type = "page"
weight = 50
tags = ["tutorial"]
+++

# Accessing Pods and Services from the Outside

Once you have a Pod or Service running on your cluster, you might want to access it from outside your cluster. There's currently three ways to do that:

- [Public access to a Service through an Ingress](#public-ingress)
- [Authenticated access to a Pod through `kubectl port-forward`](#port-forward)
- [Authenticated access to a Service through the API proxy](#api-access)

## Setting up a Public Ingress {#public-ingress}

Your Giant Swarm cluster comes with an Ingress Controller based on [NGINX](https://github.com/kubernetes/ingress/blob/master/controllers/nginx/), which we run for you in your cluster. You can expose Services publicly by setting up a simple Ingress. You can do this with an ingress manifest (e.g. `myingress.yaml`) that looks like following template (replace <fields> accordingly) in the same namespace as the service you want to expose. 

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: <ingress-name>
  namespace: <namespace-name>
spec:
  rules:
  - host: <yourchoice>.<cluster-id>.k8s.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: <service-name>
          servicePort: <service-port>
```

You can apply the ingress resource with `kubectl apply -f myingress.yaml`. You can also leave out the `namespace` line in the yaml and instead use `kubectl apply --namespace <namespace> --filename myingress.yaml`.

A few moment later you will be able to access your service publicly at:

```nohighlight
http://<yourchoice>.<cluster-id>.k8s.gigantic.io
```

Currently, this is limited to exposing by default on port `80`. Support for TLS will be added soon.

For additional features and options, please see our documentation around [Advanced Ingress Configuration](../advanced-ingress-configuration/).

## Forwarding an authenticated port with `kubectl port-forward` {#port-forward}

Forwarding a port with `kubectl` is fairly easy, however, it only works with single Pods and not with Services. Thus you need the exact pod name. You can either get this manually by running

```nohighlight
kubectl --namespace=<namespace> get pods
```

and looking for the right pod name. Or by running following script.

```nohighlight
POD=$(kubectl get pods --namespace <namespace> --selector <label-key>=<label-value> \
    -o template --template '{{range .items}}{{.metadata.name}} {{.status.phase}}{{"\n"}}{{end}}' \
    | grep Running | head -1 | cut -f1 -d' ')
```

Be sure to have your Pod labeled accordingly so you can find it with the above selector.

After this you can run

```nohighlight
kubectl port-forward --namespace <namespace> $POD <local-port>:<pod-port>
```

or to have it running in the background

```nohighlight
kubectl port-forward --namespace <namespace> $POD <local-port>:<pod-port> &
```

Now you can access your Pod locally via `localhost:<local-port>`.

### Access any Service from through the API proxy {#api-access}

The Kubernetes API comes with an inbuilt proxy, which you can use to access Services deployed on your cluster. The URL schema is

```nohighlight
https://api.<cluster-id>.k8s.gigantic.io/api/v1/proxy/namespaces/<namespace>/services/<service-name>:<port>/
```

Access will only be granted to clients which

- trust the API's server certificate, which means they trust the Certificate Authority (CA) that signed it and
- provide a valid client certificate.

The Giant Swarm [web user interface](https://happa.giantswarm.io/getting-started/configure) shows you how to obtain the certificate files.

To make these certificates available to HTTP clients/browsers, see our guide [Establishing Trust to Your Cluster's CA and Importing Certificates](../importing-certificates/) which explains this for different clients on various platforms.

## Further reading

- [Establishing Trust to Your Cluster's CA and Importing Certificates](../importing-certificates/)
- [Official Kubernetes documentation for the Ingress Resource](http://kubernetes.io/docs/user-guide/ingress/)
- [Official Kubernetes documentation for the kubectl port-forward](http://kubernetes.io/docs/user-guide/kubectl/kubectl_port-forward/)
