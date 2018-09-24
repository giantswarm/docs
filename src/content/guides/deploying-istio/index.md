+++
title = "How to deploy Istio in your cluster"
description = "Tutorial on how to deploy Istio in the differnet providers."
date = "2018-09-27"
type = "page"
weight = 30
tags = ["tutorial"]
+++

# Preparation

Nowadays, the recommended way to deploy Istio is using Helm. Please ensure the Kubernetes package manager is installed and running in your cluster. Go to the official [docs](https://docs.helm.sh/using_helm#install-helm) in case you need to install it.

Now, it is time to [download the project package](https://github.com/istio/istio/releases/) and include the istio command line interface in your path. After having in your local the uncompressed package, enter in the istio folder and make sure the `/bin` directory is under your system path.

Verify you are ready running these commands
```
# Check helm client and tiller are running
$ helm version
Client: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}

# Check istioctl is available
$ istioctl version
Version: X.X.X
...
BuildStatus: Clean
```

Secondly, in order to avoid a known issue with the sidecar security context (privileges), it is needed to extend or create the pod security policy assigned to your services. Istio beyond the sidecar container injects a init container in the deployment resource of your apps. It takes care of proxy the traffic between the proxy and the original container(s).
```
initContainers:
  - args:
    ...
    image: docker.io/istio/proxy_init:0.6.0
    name: istio-init
    securityContext:
      capabilities:
        add:
        - NET_ADMIN
      privileged: true
```

As consequence, the pod now must have the right security policies configured to run in the cluster. An easy way to solve the problem is to create a pod security policy with the privileges for the containers in your deployment plus the init container ones, and then define an istio role for binding it together with the psp created before, and the default service account for the namespace where you run your services. 
```
apiVersion: extensions/v1beta1
kind: PodSecurityPolicy
metadata:
  name: istio
spec:
  privileged: true
  allowedCapabilities:
  - 'NET_ADMIN'
  fsGroup:
    rule: RunAsAny
  runAsUser:
    rule: RunAsAny
  seLinux:
    rule: RunAsAny
  supplementalGroups:
    rule: RunAsAny
  volumes:
  - '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: istio
rules:
- apiGroups:
  - extensions
  resourceNames:
  - istio
  resources:
  - podsecuritypolicies
  verbs:
  - use
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: istio
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: istio
subjects:
- kind: ServiceAccount
  name: default
  namespace: <NAMESPACE_OF_YOUR_SERVICES>
```

## Recomendations 

The deployment is made up of a different number of components. Some of them, as pilot, have a large impact in terms of memory and CPU, so it is recommended to have around 8GB and 4CPUs free in your cluster. Obviously, all components have `requested resources` defined, so in case you don't have enough capacity you will see pods not starting.

A followed convention, not only within Istio community but Kubernetes too, is to define in all your app deployments the label `app` and `version`. Both labels help the tracing and metric system to have richer meta information. 

Another good practice is to name the service ports. Istio uses the name to discover the protocol used by the end service container. Thus you have to prefix the port name with the protocol desired. The different supported protocols (http, http2, grpc, mongo, or redis) leverage Istio to route traffic more intelligently. Otherwise, it will use plain TCP routing.
```
apiVersion: v1
kind: Service
metadata:
  name: app
spec:
  ports:
  - name: http-app
    port: 80
    protocol: TCP
    targetPort: 80
```

In the strange case, you use multiple services laying over the same pods, you have to use the same kind of traffic for the ports defined in the service.

```
# WRONG because the protocol is different and same port
apiVersion: v1             apiVersion: v1
kind: Service              kind: Service
metadata:                  metadata:
  name: app-svc-1            name: app-svc-2
spec:                      spec:
  ports:                     ports:
  - name: http-app           - name: http2-app
    port: 80                   port: 80
    protocol: TCP              protocol: TCP
  selector:                  selector:    
    app: my-app                app: my-app
```

Finally, it is good to mention how you can integrate Istio within your existing workloads. By default mutual TLS is not configured, mainly avoiding downtime issues it can provoke. But lately, there is a new option which you can set the TLS policy as `permissive` and let the proxy accept traffic encrypted and unencrypted. Thus safe wise you can start with this policy and slowly move your services to a `strict` mode TLS in case it is required.

## Installation

Regardless of the provider, the first step to install Istio is to create all cluster role definitions. The service mesh uses different Kubernetes resources to manage the variety of entities in which it relies on. For example, it defines the `gateway` resource for control how the mesh is exposed to Internet.

```
# Post all resources to the Kubernetes API
$ kubectl apply -f install/kubernetes/helm/istio/templates/crds.yaml
```

Istio is a complex system composed by several pieces, by default the installation release all components to the cluster. However, the mesh can be created with different flavors. As an example, you can only deploy `Pilot`, which will give you the ability to enforce service policies. Let's enumerate the different main components:

- Ingress / Egress gateways 
- Sidecar injector webhook
- Galley
- Mixer
- Pilot
- Grafana
- Prometheus
- Tracing (Jaeger) 
- Kiali
- Mutual TLS
- Certmanager

By default, all are deployed but mutual TLS and certmanager. You can configure the components tweaking the values passed to helm. Run `helm inspect install/kubernetes/helm/istio` to display the different options available.

Although Istio can run in almost every Kubernetes cluster no matter the provider, there are some quirks to consider depending on where the service mesh is deployed.

### AWS and Azure

```
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system
```

### Giantnetes

```
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system \
--set gateways.istio-ingressgateway.type=NodePort --set gateways.istio-egressgateway.type=NodePort 
```

## Deploy an application

Let's verify Istio is deployed and configure correctly. We can deploy a simple http server that returns `200` code for the `healthz` path of the service.

### Automated sidecar injection

First of all we need to label the namespace to make easier the sidecar injection.
```
kubectl label namespace default istio-injection=enabled
```
And now we can install the chart containing the example app
```
$ helm registry install quay.io/giantswarm/liveness-chart
```

### Manual sidecar injection

In case you want the manual injection, pull the chart and use istio command line to parse the deployment and insert the proxy.
```
# Pulling the chart to your local
$ helm registry pull quay.io/giantswarm/liveness-chart --dest /tmp/

# (CLOUD) Parse the chart template to Kubernetes resources
$ helm template /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart /tmp/liveness.yaml

# (GIANTNETES) Parse the chart template to Kubernetes resources
$ helm template /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart /tmp/liveness.yaml --set ingress.port=30010

# Inject the sidecar in the deployment and submit the resources to Kubernetes API
$ istioctl kube-inject -f /tmp/liveness.yaml | k apply -f -
```

It will launch a deployment and service listening in the port 80. At the same time, it will create a virtual service redirecting the traffic to the liveness service. Also, there is a gateway to wire the virtual service up with the ingress gateway.

### AWS verification

Get service hostname given by the cloud provider. Run
```
$ kubectl get svc istio-ingressgateway -n istio-system -o jsonpath="{.status.loadBalancer.ingress[0].hostname}"
```
And it will return the URL which the deployed app should reply. As we have set wildcard `*` in the hostname of the virtual service
all `/healthz` will be forwarded to the service.

This curl command should return it `200`
```
curl http://<ELB_HOSTNAME>/healthz -I
```

### Azure verification

Get the ingress controller IP given by the cloud provider. Run
```
$ kubectl get svc istio-ingressgateway -n istio-system -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```
And it will return the URL which the deployed app should reply to. As we have set wildcard `*` in the hostname of the virtual service
all `/healthz` will be forwarded to the service.

This curl command should return it `200`
```
curl http://<IP>/healthz -I
```

## On premise (Giantnetes)

As probably you may know our [`giantnetes`](https://docs.giantswarm.io/basics/onprem-architecture/) tenant pods live inside the control plane pods. It means Giant Swarm creates a forwarding between the external ingress service to the ingress placed inside the tenant cluster. By default, the tenant clusters has a nginx ingress controller allocated out of the box. But, in case you want to use istio ingress controller you need to change the current ingress controller (remember it will affect all current traffic for that tenant cluster) or ask our team to allocate a new redirection from the parent endpoint to the Istio controller.


Modifying the port for the ingress gateway
```
kubectl edit svc istio-ingressgateway -n istio-system
----
  - name: http2
    nodePort: <PORT_PROVIDED_BY_GS_OR_DEFAULT_ONE>
    port: 80
    protocol: TCP
    targetPort: 80
  - name: https
    nodePort: <PORT_PROVIDED_BY_GS_OR_DEFAULT_ONE>
    port: 443
    protocol: TCP
    targetPort: 443å
----
```

This curl command should return it `200`
```
curl http://<LOAD_BALANCER_IP>:<PORT_TENANT_CLUSTER>/healthz -I
```

Giant Swarm encourages you to leave this liveness app up and running in order to make our monitoring happy. By default, nginx ingress controller provides with the `/healthz` endpoint to check ICs are up, but Istio controller lack of this functionality. For that reason, the liveness app will give us the health signal solving the observability issue.

## Troubleshooting

- The pods cannot start with injected sidecars. Looking in the deployment status you see
```
message: 'pods "details-v1-7986ddbd99-" is forbidden: unable to validate against
   any pod security policy: [spec.initContainers[0].securityContext.privileged:
   Invalid value: true: Privileged containers are not allowed capabilities.add:
   Invalid value: "NET_ADMIN": capability may not be added spec.initContainers[1].securityContext.privileged:
```
It means the pod security policy is not bind to the service account used by the deployment. Please review the `Preparation` section.

- The request are not routed to the ingress gateway. In some cases, the default gateway is not proper configured. If istio has just been deployed, try to delete it and check now the status.
```
$ kubectl delete gateways.networking.istio.io istio-autogenerated-k8s-ingress -n istio-system
```
