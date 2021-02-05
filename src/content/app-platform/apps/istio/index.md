---
linkTitle: Istio
title: How to deploy Istio in your cluster
description: Tutorial on how to deploy Istio on a Giant Swarm Kubernetes cluster.
weight: 60
menu:
  main:
    parent: app-platform-apps
aliases:
  - /guides/deploying-istio/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-customer-happiness
---

# How to deploy Istio in your Cluster

After microservices have conquered the world, another dimension of concerns has arisen. The technology has allowed us to build distributed architectures thanks to tools like Kubernetes. Although the orchestrator helps us with the deployment and maintenance of our services, there are a bunch of other concerns we have to deal with. For example, most people use an insecure protocol to communicate their services. For that and many other reasons, service meshes have appeared with the goal of helping to manage these distributed scenarios.

Istio is one of the main players in the arena of service meshes. It stands out because of the project maturity and the ease of adoption. Below we describe how it can be deployed in your cluster, emphasizing how to avoid common mistakes.

## Preparation

At the present time, the recommended way to deploy Istio is using Helm. Please ensure the Kubernetes package manager is installed and running in your cluster. Go to the official [docs](https://helm.sh/docs/using_helm/#install-helm) if you need to install it. Additionally, a Helm registry plugin is used to download the app charts. Please be sure you [have it configured, too](https://github.com/app-registry/appr-helm-plugin).

Start off by [downloading the Istio project package](https://github.com/istio/istio/releases/) and include the command line interface in your path. After having it in a local folder uncompressed, make sure the `/bin` directory is under your system path.

Let's verify that the environment is ready. First check that Helm is installed correctly.

```nohighlight
$ helm version
Client: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}
Server: &version.Version{SemVer:"v2.10.0", GitCommit:"X", GitTreeState:"clean"}
```

Now, ensure `istioctl` is in your path.

```nohighlight
$ istioctl version
Version: X.X.X
...
BuildStatus: Clean
```

Secondly, in order to avoid a known issue with the sidecar security context (privileges), it is necessary to extend or create the pod security policy that will be assigned to your microservices. Istio, beyond the sidecar container, injects an init container in the app's deployment resource. It takes care of forwarding traffic between the proxy and the original container(s).

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

As a consequence, the pod now must have the right security policies configured to run in the cluster. An easy way to solve this problem is to [create a pod security policy that contains the correct capabilities]({{< relref "/getting-started/rbac-and-psp#pod-security-policies" >}}). Then, define a RBAC role and a role binding for wiring it together against the default service account for the namespace(s) where your apps are running.

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

Remember to replace the `NAMESPACE` placeholder with the desired value. As an example, when you set `default` it implies all applications running in the `default` namespace would have bound the `istio` pod security policy.

## Recommendations

The deployment is made up of a different number of components. Some of them, like `Pilot`, have a large impact in terms of memory and CPU. As a result, we recommended to have around 8GB of memory and 4 CPUs free in your cluster. Obviously, all components have `requested resources` defined, so if you don't have enough capacity you will see pods not starting.

A followed convention, not only within the Istio community but in Kubernetes too, is to define in all your app deployments the label `app` and `version` as metadata. Both labels help the tracing and metrics systems to have richer meta information.

Another good practice is to name the service ports. Istio uses the name to discover the protocol used by the end service container. Thus, you have to prefix the port name with the protocol desired. The different supported protocols (`http`, `http2`, `grpc`, `mongo`, or `redis`) leverage Istio to route traffic more intelligently. Otherwise, it will use plain TCP routing. Read more [in the official docs](https://istio.io/latest/docs/ops/deployment/requirements/).

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

Finally, you may be interested in how you can integrate Istio within your existing workloads. By default mutual TLS is not configured, mainly to avoid the downtime issues that it can cause. But recently, a new option where you can set the TLS policy as `permissive` and let the proxy accept both encrypted and unencrypted traffic has been integrated. So, to be on the safe side, you can start with this policy and slowly move your services to a `strict` mode TLS if it is required.

## Installation

Regardless of provider, the first step to install Istio is to create all cluster role definitions. The service mesh uses different Kubernetes resources to manage the variety of entities in which it relies on. For example, it defines the `gateway` resource for control on how the mesh is exposed to Internet.

```nohighlight
# Post all resources to the Kubernetes API
kubectl apply -f install/kubernetes/helm/istio/templates/crds.yaml
```

Istio is a complex system composed by several pieces. All these pieces are released to the cluster, by deafault, upon installation. However, the mesh can be created with different flavors. For instance, you can only deploy `Pilot`, which will give you the ability to enforce service policies. Let's outline the main components:

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

With exception of Mutual TLS and Certmanager, all of these are installed. As mentioned above, Mutual TLS can impact ongoing traffic. We suggest reading the [upstream docs](https://istio.io/latest/docs/tasks/security/authentication/authn-policy/#auto-mutual-tls) before enabling it. You can configure the components by tweaking the values passed to Helm. Run `helm inspect install/kubernetes/helm/istio` to display the different options available.

Although Istio can run in almost every Kubernetes cluster regardless of the underlying infrastructure, there are some quirks to consider depending on where the service mesh is deployed.

### AWS and Azure

The actual installation is quite simple thanks to Helm. The following command will deploy all Istio components in a new namespace reserved.

```nohighlight
helm install \
  install/kubernetes/helm/istio \
  --name istio \
  --namespace istio-system
```

### On premises (KVM)

The main difference from the clouds is the ingress gateway service must be type `NodePort`. Since there is no automatic mechanism to provide an endpoint, the service is exposed in the host of the underlying VM. Below, we will explain how to redirect the traffic from the management cluster to a second workload cluster ingress controller.

```nohighlight
$ helm install install/kubernetes/helm/istio --name istio --namespace istio-system \
--set gateways.istio-ingressgateway.type=NodePort --set gateways.istio-egressgateway.type=NodePort
```

Ensure all components are up-and-running, listing the pods in the Istio namespace.

```nohighlight
kubectl get pods -n istio-system -w
```

## Deploy an application

Let's verify that Istio is deployed and configured correctly. We can deploy a simple http server that returns a `200` code for the `healthz` path of the service.

### Automated Sidecar Injection

The automated injection mechanism relies on the mutate admission controllers functionality offered by Kubernetes API. It means the API server has to be deployed with the flag `enable-admission-plugins` containing `MutatingAdmissionWebhook`. Also the validate webhook (`ValidatingAdmissionWebhook`) is recommended since it used by `galley` to verify the Istio resources syntax. You can check if the admission controller flag contains the webhooks enabled running:

```nohighlight
$ kubectl -n kube-system \
  get pod <API_SERVER> \
  -o yaml | grep admission
--enable-admission-plugins=NamespaceLifecycle,LimitRanger,ServiceAccount,DefaultStorageClass,DefaultTolerationSeconds,MutatingAdmissionWebhook,ValidatingAdmissionWebhook,ResourceQuota
```

__Note:__ Contact with Giant Swarm support team in case it is disabled.

First of all, we need to label the namespace to make the sidecar injection effective.

```nohighlight
kubectl label namespace default istio-injection=enabled
```

__Warning:__ Avoid labeling the namespaces `kube-system` or `giantswarm` otherwise the entire cluster could end up shattered

And now we can install the chart containing the example app.

```nohighlight
helm registry install quay.io/giantswarm/liveness-chart -n liveness
```

### Manual Sidecar Injection

If you want the manual injection, you may find it to be a bit more tedious.

First pull the chart from the app registry.

```nohighlight
helm registry pull quay.io/giantswarm/liveness-chart --dest /tmp/
```

For AWS and Azure, transform the Helm templates into Kubernetes resources relying on the default values.

```nohighlight
helm template \
  /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart \
  /tmp/liveness.yaml
```

For an on premises installation, pass the ingress port which your ingress controller will listen. Remember it will be provided by the Giant Swarm support team. If you replace the main ingress controller it will be `30010`.

```nohighlight
helm template \
  /tmp/liveness/giantswarm_liveness-chart_XXX/liveness-chart \
  /tmp/liveness.yaml \
  --set ingress.port=30010
```

Inject the sidecar container specification in the deployment resource and submit it to Kubernetes API.

```nohighlight
istioctl kube-inject -f /tmp/liveness.yaml | kubectl apply -f -
```

It will launch a deployment and service listening on the port 80. At the same time, it will create a virtual service redirecting the traffic to the liveness service. Also, there is a gateway to wire the virtual service up with the ingress gateway.

### AWS Verification

Get the load balancer host name.

```nohighlight
kubectl -n istio-system \
  get service istio-ingressgateway \
  -o jsonpath="{.status.loadBalancer.ingress[0].hostname}"
```

This will return the URL under which the deployed app should reply. As we have set wildcard `*` in the hostname of the virtual service all `/healthz` traffic will be forwarded to the service.

Executing this curl command should give you a `200` response.

```nohighlight
curl http://<ELB_HOSTNAME>/healthz -I
```

### Azure Verification

Get the ingress controller IP assigned by Azure.

```nohighlight
kubectl -n istio-system \
  get svc istio-ingressgateway \
  -o jsonpath="{.status.loadBalancer.ingress[0].ip}"
```

And it will return the URL which the deployed app should reply to.As we have set wildcard `*` in the hostname of the virtual service all `/healthz` traffic will be forwarded to the service..

Running this curl command should give you a `200` response.

```nohighlight
curl http://<IP>/healthz -I
```

### On Premises (KVM) Verification

As you may already know, in our [`on premises installations`]({{< relref "/general/architcture/on-premises" >}}) the workload cluster pods live inside the management cluster pods. This means Giant Swarm creates a forward between the external ingress service to the ingress placed inside the workload cluster. By default, the workload cluster has an NGINX ingress controller allocated out-of-the-box. But, in case you want to use Istio ingress controller you need to ask our team to allocate a new redirection from the parent endpoint to the Istio controller. With the latter, you will have the two ingress controllers exposed to Internet.

After obtaining the ports, modify the ingress gateway to set the correct configuration.

```nohighlight
kubectl edit service istio-ingressgateway -n istio-system
```

```yaml
...
  - name: http2
    nodePort: <PORT_PROVIDED_BY_GS>
    port: 80
    protocol: TCP
    targetPort: 80
  - name: https
    nodePort: <PORT_PROVIDED_BY_GS>
    port: 443
    protocol: TCP
    targetPort: 443
...
```

After configuring it, running the next command should get you a `200` response.

```nohighlight
curl http://<LOAD_BALANCER_IP>:<PORT_TENANT_CLUSTER>/healthz -I
```

---

__Disclaimer:__ While we do not discourage installing and using Istio and are even providing a tutorial here, we currently do not support it managed by us. That means that if you run into issues with or because of Istio, this is your responsibility. Furthermore, as the complexity increases with Istio, debugging and fixing even not directly related issue will take longer.

## Troubleshooting

### Pods cannot start with injected sidecars

Looking into the deployment status you see:

```yaml
...
  message: 'pods "app-v1-XXXXXXX-" is forbidden: unable to validate against
    any pod security policy: [spec.initContainers[0].securityContext.privileged:
    Invalid value: true: Privileged containers are not allowed capabilities.add:
    Invalid value: "NET_ADMIN": capability may not be added spec.initContainers[1].securityContext.privileged:
...
```

It means the pod security policy is not bound to the service account used by the deployment. Please review the `Preparation` section.

### Requests are not routed to the ingress gateway

In some cases, the default gateway is not configured properly. If Istio has just been deployed, try to delete it and check the status again using the command below.

```nohighlight
kubectl -n istio-system \
  delete \
  gateways.networking.istio.io \
  istio-autogenerated-k8s-ingress
```

### Traffic load balancing is not working at layer seven

Ensure you don't have multiple services using different protocols (service port names) for the same pods. Remember Istio discovers the protocol getting the prefix of the port name set in the service resources.

```nohighlight
apiVersion: v1             apiVersion: v1
kind: Service              kind: Service
metadata:                  metadata:
  name: app-svc-1            name: app-svc-2
spec:                      spec:
  ports:                     ports:
  - name: http-app           - name: http2-app # WRONG should be http too
    port: 80                   port: 80
  selector:                  selector:
    app: my-app                app: my-app
```

## Further reading

- [Istio official docs](https://istio.io/latest/docs/)
- [Istio community chat](https://slack.istio.io/)
- [Istio GitHub project](https://github.com/istio/istio)
