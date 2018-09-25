+++
title = "How to deploy Istio in your cluster"
description = "Tutorial on how to deploy Istio on a Giant Swarm Kubernetes cluster."
date = "2018-09-27"
type = "page"
weight = 60
tags = ["tutorial"]
+++

# How to deploy Istio in your cluster

After microservices has conquered the world, another dimension of concerns has arisen. The technology has allowed us to build distributed architectures thanks to tools like Kubernetes. Although the orchestrator helps us with the deployment and maintenance of our services there a bunch of other concerns we have to deal. As an example, most people use an insecure protocol to communicate their services. For that and many other reasons, the service meshes have appeared with the goal of helping to manage these distributed scenarios.

Istio is one of the main players and it stands out because of the project maturity and the easiness of adoption. Below it is described how it can be deployed in your cluster, emphasizing how to avoid usual mistakes.

## Preparation

Nowadays, the recommended way to deploy Istio is using Helm. Please ensure the Kubernetes package manager is installed and running in your cluster. Go to the official [docs](https://docs.helm.sh/using_helm#install-helm) in case you need to install it.

Now, it is time to [download the Istio project package](https://github.com/istio/istio/releases/) and include the command line interface in your path. After having it in a local folder uncompressed, make sure the `/bin` directory is under your system path.

Let's verify the environment is ready. First check helm is installed correctly.

```nohighlight
$ helm version
Client: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}
```

Now, ensure Istio `cli` is in your path.

```nohighlight
$ istioctl version
Version: X.X.X
...
BuildStatus: Clean
```

Secondly, in order to avoid a known issue with the sidecar security context (privileges), it is needed to extend or create the pod security policy that will be assigned to your microservices. Istio, beyond the sidecar container, injects an init container in the app's deployment resource. It takes care of forwarding traffic between the proxy and the original container(s).

```yaml
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

As consequence, the pod now must have the right security policies configured to run in the cluster. An easy way to solve the problem is to [create a pod security policy that contains the correct capabilities](https://docs.giantswarm.io/guides/securing-with-rbac-and-psp#pod-security-policies/). Then, define a RBAC role and a role binding for wiring it together against the default service account for the namespace(s) where your apps are running. 

__Warning:__ If your apps are using a custom service account then you need to create the binding for each of them.

```yaml
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
  namespace: <NAMESPACE>
```

Remember replace the `NAMESPACE` placeholder with the value desired. As ax example, when you set `default` it implies all application running in the `default` namespace would have bound the `istio` pod security policy.

## Recommendations 

The deployment is made up of a different number of components. Some of them, as pilot, have a large impact in terms of memory and CPU,so it is recommended to have around 8GB of memory and 4 CPUs free in your cluster. Obviously, all components have `requested resources` defined, so in case you don't have enough capacity you will see pods not starting.

A followed convention, not only within Istio community but Kubernetes too, is to define in all your app deployments the label `app` and `version` as metadata. Both labels help the tracing and metric system to have richer meta information. 

Another good practice is to name the service ports. Istio uses the name to discover the protocol used by the end service container. Thus you have to prefix the port name with the protocol desired. The different supported protocols (`http`, `http2`, `grpc`, `mongo`, or `redis`) leverage Istio to route traffic more intelligently. Otherwise, it will use plain TCP routing. Read more [in the official docs](https://istio.io/docs/setup/kubernetes/spec-requirements/).

```yaml
apiVersion: v1
kind: Service
metadata:
  name: myapp
spec:
  ports:
  - name: http-myapp
    port: 80
```

If you have multiple services exposing port of the same pods, you have to use the same kind of traffic for the ports defined in the service.

```yaml
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

Finally you may be interested in how you can integrate Istio within your existing workloads. By default mutual TLS is not configured, mainly for avoiding downtime issues it can provoke. But lately, there has appeared a new option where you can set the TLS policy as `permissive` and let the proxy accept both encrypted and unencrypted traffic. Thus, to be on the safe side, you can start with this policy and slowly move your services to a `strict` mode TLS in case it is required.

## Installation

Regardless of the provider, the first step to install Istio is to create all cluster role definitions. The service mesh uses different Kubernetes resources to manage the variety of entities in which it relies on. For example, it defines the `gateway` resource for control how the mesh is exposed to Internet.

```nohighlight
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

With exception of Mutual TLS and Certmanager, all of those are installed. As it is mentioned above mutual TLS can impact ongoing traffic, read the [upstream docs](https://istio.io/docs/tasks/security/mutual-tls/) before enable it. You can configure the components tweaking the values passed to helm. Run `helm inspect install/kubernetes/helm/istio` to display the different options available.

Although Istio can run in almost every Kubernetes cluster regardless of the underlying infrastructure, there are some quirks to consider depending on where the service mesh is deployed.

### AWS and Azure

The actual installation is quite simple thanks to helm. The following command will deploy all Istio components in a new namespace reserved.

```nohighlight
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system
```

### On premises (KVM)

The main difference with clouds is the ingress gateway service must be type `NodePort`. Since there is no automatic mechainism to provide an endpoint, the service is exposed in the host underlaying machine. Later, it is explained how to redirect the traffic from the control plane to a second tenant cluster ingress controller.

```nohighlight
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system \
--set gateways.istio-ingressgateway.type=NodePort --set gateways.istio-egressgateway.type=NodePort 
```

Ensure all components are up and running listing the pods in the istio namespace.

```nohighlight
$ kubectl get pods -n istio-system -w
```

## Deploy an application

Let's verify Istio is deployed and configure correctly. We can deploy a simple http server that returns `200` code for the `healthz` path of the service.

### Automated sidecar injection

First of all we need to label the namespace to make effective the sidecar injection.

```nohighlight
$ kubectl label namespace default istio-injection=enabled
```

And now we can install the chart containing the example app.

```nohighlight
$ helm registry install quay.io/giantswarm/liveness-chart -n liveness
```

### Manual sidecar injection

In case you want the manual injection, pull the chart and use Istio command line utility to parse the deployment and insert the proxy.

```nohighlight
# Pulling the chart to your local
$ helm registry pull quay.io/giantswarm/liveness-chart --dest /tmp/

# (CLOUD) Parse the chart template to Kubernetes resources
$ helm template /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart /tmp/liveness.yaml

# (GIANTNETES) Parse the chart template to Kubernetes resources (use the ingress port given by support)
$ helm template /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart /tmp/liveness.yaml --set ingress.port=30010

# Inject the sidecar in the deployment and submit the resources to Kubernetes API
$ istioctl kube-inject -f /tmp/liveness.yaml | k apply -f -
```

It will launch a deployment and service listening on the port 80. At the same time, it will create a virtual service redirecting the traffic to the liveness service. Also, there is a gateway to wire the virtual service up with the ingress gateway.

### AWS verification

Get the load balancer hostname. 

```nohighlight
$ kubectl get service istio-ingressgateway -n istio-system -o jsonpath="{.status.loadBalancer.ingress[0].hostname}"
```

This will return the URL under which the deployed app should reply. As we have set wildcard `*` in the hostname of the virtual service all `/healthz` traffic will be forwarded to the service.

Executing this curl command should give you a `200` response.

```nohighlight
$ curl http://<ELB_HOSTNAME>/healthz -I
```

### Azure verification

Get the ingress controller IP assigned by Azure.

```nohighlight
$ kubectl get svc istio-ingressgateway -n istio-system -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```

And it will return the URL which the deployed app should reply to. Same as AWS, the wildcard `*` set as the hostname in the virtual service will send all traffic from `/healthz` path to the liveness service.

Running this curl command should give you a `200` response.

```nohighlight
$ curl http://<IP>/healthz -I
```

## On premise (KVM)

As you may probably know, in our [`on premise installations`](https://docs.giantswarm.io/basics/onprem-architecture/) the tenant pods live inside the control plane pods. It means Giant Swarm creates a forwarding between the external ingress service to the ingress placed inside the tenant cluster. By default, the tenant clusters has an nginx ingress controller allocated out of the box. But, in case you want to use Istio ingress controller you need to change the current ingress controller (remember it will affect all current traffic for that tenant cluster). Another option is asking our team to allocate a new redirection from the parent endpoint to the Istio controller. With the latter, you will have the two ingress controllers exposed to Internet.

After obtaining the ports, modify the ingress gateway to set the correct configuration.

```nohighlight
$ kubectl edit service istio-ingressgateway -n istio-system
```

```yaml
...
  - name: http2
    nodePort: <PORT_PROVIDED_BY_GS_OR_DEFAULT_ONE>
    port: 80
    protocol: TCP
    targetPort: 80
  - name: https
    nodePort: <PORT_PROVIDED_BY_GS_OR_DEFAULT_ONE>
    port: 443
    protocol: TCP
    targetPort: 443
...
```

After configured it, running the next command you should get a `200` response.

```nohighlight
$ curl http://<LOAD_BALANCER_IP>:<PORT_TENANT_CLUSTER>/healthz -I
```

Giant Swarm encourages you to leave this liveness app up and running in order to make our monitoring happy. By default, nginx ingress controller provides a `/healthz` endpoint to check ICs are up, but the Istio controller lacks of this functionality. For that reason, the liveness app will give us the health signal required to have the correct observability of your istio clusters.

## Troubleshooting

- The pods cannot start with injected sidecars. Looking in the deployment status you see:

```yaml
...
  message: 'pods "app-v1-XXXXXXX-" is forbidden: unable to validate against
    any pod security policy: [spec.initContainers[0].securityContext.privileged:
    Invalid value: true: Privileged containers are not allowed capabilities.add:
    Invalid value: "NET_ADMIN": capability may not be added spec.initContainers[1].securityContext.privileged:
...
```

It means the pod security policy is not bound to the service account used by the deployment. Please review the `Preparation` section.

- Requests are not routed to the ingress gateway. In some cases, the default gateway is not configured properly. If istio has just been deployed, try to delete it and check the status again using the command below.

```nohighlight
$ kubectl delete gateways.networking.istio.io istio-autogenerated-k8s-ingress -n istio-system
```
