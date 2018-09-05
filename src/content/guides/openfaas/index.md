

# Using OpenFaaS with a Giant Swarm Cluster


## Create a Kubernetes Cluster

```
gsctl create cluster -o giantswarm -n "Marians OpenFaaS test server"
```

```
gsctl create kubeconfig --cluster=5bjgh --certificate-organizations system:masters
```

Wait until the cluster comes up. It can take more than 20 minutes.

```
$ kubectl cluster-info
Kubernetes master is running at https://api.5bjgh.k8s.gollum.westeurope.azure.gigantic.io
CoreDNS is running at https://api.5bjgh.k8s.gollum.westeurope.azure.gigantic.io/api/v1/namespaces/kube-system/services/coredns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```

## Install Helm/Tiller

This is the easiest way to deploy OpenFaaS.

We are on a Mac and do it this way:

```
brew install kubernetes-helm
```

Create permissions for tiller:

```
$ kubectl -n kube-system create sa tiller \
 && kubectl create clusterrolebinding tiller \
      --clusterrole cluster-admin \
      --serviceaccount=kube-system:tiller
serviceaccount "tiller" created
clusterrolebinding.rbac.authorization.k8s.io "tiller" created
```

Install tiller:

```
$ helm init --skip-refresh --upgrade --service-account tiller
$HELM_HOME has been configured at /Users/marian/.helm.

Tiller (the Helm server-side component) has been installed into your Kubernetes Cluster.

Please note: by default, Tiller is deployed with an insecure 'allow unauthenticated users' policy.
To prevent this, run `helm init` with the --tiller-tls-verify flag.
For more information on securing your installation see: https://docs.helm.sh/using_helm/#securing-your-helm-installation
Happy Helming!
```

## Install OpenFaaS

Create the namespaces `openfaas` and `openfaas-fn`.

```
$ kubectl apply -f https://raw.githubusercontent.com/openfaas/faas-netes/master/namespaces.yml
```

Add the OpenFaaS helm chart:

```
$ helm repo add openfaas https://openfaas.github.io/faas-netes/
```

Make sure the chart is up to date:

```
$ helm repo update
```

Deploy the chart:

```
$ helm upgrade openfaas --install openfaas/openfaas \
    --namespace openfaas  \
    --set functionNamespace=openfaas-fn \
    --set operator.create=true
```

## Understand what has been installed

Let's check out what's been installed in the `openfaas` namespace:

Deployments/Pods belonging to:

- `queue-worker`: Uses image [openfaas/queue-worker](https://hub.docker.com/r/openfaas/queue-worker/)
- `gateway`: Uses image [openfaas/gateway](https://hub.docker.com/r/openfaas/gateway/) and [openfaas/openfaas-operator](https://hub.docker.com/r/openfaas/openfaas-operator/)
- `nats`: Uses image [nats-streaming](https://hub.docker.com/_/nats-streaming/) from https://nats.io/
- prometheus
- alertmanager

TODO: Explain what the components above are doing.

The gateway has two services, one named `gateway` with type ClusterIP and one `gateway-external` with type NodePort.

There are no Ingress resources yet, so nothing will be available.

## Set up Ingress to expose functions

To have access to the API gateway and the web UI, we have to set up Ingress. Here is a manifest that exposes the two on port 80:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: openfaas
  namespace: openfaas
spec:
  rules:
  - host: openfaas.5bjgh.k8s.gollum.westeurope.azure.gigantic.io
    http:
      paths:
      - path: /
        backend:
          serviceName: gateway-external
          servicePort: 8080
```

TODO: Change this to HTTPS

The `spec.rules[].host` part has to be aligned with your cluster's ingress base domain. See [our guide](https://docs.giantswarm.io/guides/accessing-services-from-the-outside/#setting-up-ingress) for details.

Save the above manifest as `ingress.yaml` and then apply

```
$ kubectl -n openfaas apply -f ingress.yaml
```

When you then list all ingresses, it should look like this:

```
$ kc get ingress -n openfaas
NAME       HOSTS                                                    ADDRESS   PORTS     AGE
openfaas   openfaas.5bjgh.k8s.gollum.westeurope.azure.gigantic.io             80        12s
```

When opening the according HTTP URL you should be redirected to the OpenFaaS web UI.

## Deploy a pre-built function

To test-drive the OpenFaaS setup, we use the web UI to deploy one of a list of pre-built functions.

In the web UI, click the _DEPLOY NEW FUNCTION_ button.

![OpenFaaS Portal screenshot](/img/openfaas-ui-01.png)

We use the "From Store" category and select the SentimentAnalysis project.

![OpenFaaS Portal screenshot](/img/openfaas-ui-02.png)

The entry _sentimentanalysis_ will soon after appear in the left-hand menu. Click that one to get more details and a request form in the main section of the UI.

In order to give the function a test, fill in a text under _Invoke function_ and hit the _INVOKE_ button. The result will be displayed below the form.

![OpenFaaS Portal screenshot](/img/openfaas-ui-03.png)

So this is working, cool! If you're interested to see what has been deployed in your cluster, follow along.

Let's find out what's new in the `openfaas-fn` namespace we created for everything related to functions:

```
$ kubectl -n openfaas-fn get all
NAME                                     READY     STATUS    RESTARTS   AGE
pod/sentimentanalysis-5f477cb595-4bz76   1/1       Running   0          11m

NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/sentimentanalysis   ClusterIP   172.31.205.183   <none>        8080/TCP   11m

NAME                                DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/sentimentanalysis   1         1         1            1           11m

NAME                                           DESIRED   CURRENT   READY     AGE
replicaset.apps/sentimentanalysis-5f477cb595   1         1         1         11m
```

There is now a Pod, controlled by a ReplicaSet, controlled by a Deployment with names prefixed by `sentimentanalysis`, and a Service in addition.

The Pod has one container named `sentimentanalysis` using the image [`functions/sentimentanalysis`](https://hub.docker.com/r/functions/sentimentanalysis/) from the Docker hub. This is a demo image built for the purpose of tutorials like this.

Next, let's create our own function.

## Create a function

Here we'll use the OpenFaaS CLI or `faas-cli`. If you haven't done so, [install](https://github.com/openfaas/faas-cli) it.

Before creating any actual code, we make sure we have the latest version of the templated provided by the OpenFaaS project. This helps us to avoid writing boilerplate code.

```
$ faas-cli template pull

Fetch templates from repository: https://github.com/openfaas/templates.git
2018/09/05 14:48:17 Attempting to expand templates from https://github.com/openfaas/templates.git
2018/09/05 14:48:20 Fetched 13 template(s) : [csharp dockerfile go go-armhf java8 node node-arm64 node-armhf python python-armhf python3 python3-armhf ruby] from https://github.com/openfaas/templates.git
```

Now, let's create a first Python 3 function named `demo`:

```
$ faas new demo --lang python3
Folder: demo created.
  ___                   _____           ____
 / _ \ _ __   ___ _ __ |  ___|_ _  __ _/ ___|
| | | | '_ \ / _ \ '_ \| |_ / _` |/ _` \___ \
| |_| | |_) |  __/ | | |  _| (_| | (_| |___) |
 \___/| .__/ \___|_| |_|_|  \__,_|\__,_|____/
      |_|


Function created in folder: demo
Stack file written: demo.yml
```

Edit the file `demo/handler.py`:

```python
def handle(req):
    print("Hello! You said: " + req)
```

Also edit the `demo.yml` file to contain

- a fully qualified image name. For example, if you own the `acme` namespace on docker hub, you can change the `image` value like below.
- the correct OpenFaaS gateway URL in the `gateway` key, as set above in the Ingress manifest, but prefixed with `http://`.

```yaml
provider:
  name: faas
  gateway: http://openfaas.5bjgh.k8s.gollum.westeurope.azure.gigantic.io

functions:
  demo:
    lang: python3
    handler: ./demo
    image: acme/demo:latest
```

Likewise, if you are e. g. `acme` on Quay.io, change the image value to `quay.io/acme/demo:latest`.

Then invoke the build:

```
$ faas-cli build -f ./demo.yml
```

After a successful build, we want to push the image to our registry, so it can be deployed.

```
$ faas-cli push -f ./demo.yml
```

If this command does complain about denied access, please use the `docker login` command first with the registry you are about to push to (or no registry for Docker hub).

And then we finally deploy the function on our server:

```
$ faas-cli deploy -f ./demo.yml
```

The command's output contains the endpoint URL you can use to invoke the function.

Again we check what has been deployed. After the exercice above, we already know what to expect.

```
$ kubectl -n openfaas-fn get all
```

There are now a Deployment, a ReplicaSet, a Pod, and a Service named `demo`. The pod uses the image we specified in the function's YAML file.

You can also see the new function appear in the web UI.

Now let's test drive it, this time without the UI.

```
curl -is -X POST \
  http://openfaas.5bjgh.k8s.gollum.westeurope.azure.gigantic.io/function/demo \
  -d 'This is the input'

HTTP/1.1 200 OK
Server: nginx/1.14.0
Date: Wed, 05 Sep 2018 14:34:08 GMT
Content-Type: application/x-www-form-urlencoded
Content-Length: 35
Connection: keep-alive
X-Call-Id: cece634f-acc0-4b0e-8963-0de2a0ff6cac
X-Duration-Seconds: 0.051096
X-Start-Time: 1536158048270227415

Hello! You said: This is the input
```

## Auto-scaling

TODO

See https://docs.openfaas.com/architecture/autoscaling/

Decision:
- to scale based on requests per second, use the Alertmanager rules for Prometheus provided with OpenFaas
- to scale based on memory or CPU, use the Kubernetes HPA
