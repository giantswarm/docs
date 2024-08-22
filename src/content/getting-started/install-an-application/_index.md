---
title: Install an application using the app platform
linkTitle: Install an application
description: Add capabilities to your platform by deploying applications from our catalog.
weight: 50
last_review_date: 2024-08-23
menu:
  principal:
    parent: getting-started
    identifier: getting-started-install-app
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I configure the app platform to build my capabilities?
  - What do I need to do to configure the app platform to build my capabilities?
---

The _Giant Swarm App Platform_ is built on top of [Helm](https://helm.sh/) and allows you to manage apps and their configurations represented by App Custom Resources (CRs) for multiple clusters, from a single place: the [Platform API]({{< relref "/overview/architecture#platform-api" >}}).

In this guide, we will install a "helloworld" app together with an Ingress NGINX Controller to serve the application publicly. We will do this by using kubectl, to create an [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR using the platform API of your management cluster.

In general, you can manage App CRs with any tool that can communicate with the Kubernetes API such as Helm or GitOps tools (like Argo CD or Flux CD).

## Requirements

First of all, you need a running workload cluster. If you don't have one, you can create [following the steps describe in the previous post]({{< relref "/getting-started/create-workload-cluster" >}}).

The App CRs are stored in a organization namespace you are part of, together with the cluster resources. You can list the organizations by running the following command:

```nohighlight
kubectl gs get organizations
```

and you will see the organization that you have access to. Make sure you target the right organization where your workload cluster is running. You can switch to the organization namespace before creating the App CR by running:

```nohighlight
kubectl config set-context --current --namespace=org-namespace
```

That way you ensure that the App CR is created in the correct namespace.

## Step 1: Check applications installed in the cluster

First we will take a look to the existing applications already running in the cluster. By default the cluster has some default apps to make the cluster operational. Since you can have more than one cluster in the namespace lets filter the apps by the cluster name.

```nohighlight
kubectl gs -n org-namespace get apps | grep CLUSTER_ID

NAME                                 VERSION          CREATED_AT   LAST_DEPLOYED        STATUS
test01                                 2.0.0               13m          12m             deployed
test01-app-operator                    6.11.0              12m          12m             deployed
test01-aws-ebs-csi-driver-smons        0.1.0               12m          42s             deployed
test01-aws-pod-identity-webhook        1.16.0              12m          117s            deployed
test01-capi-node-labeler               0.5.0               12m          4m23s           deployed
test01-cert-exporter                   2.9.1               12m          112s            deployed
test01-cert-manager                    3.8.1               12m          4m4s            deployed
test01-cilium-servicemonitors          0.1.2               12m          30s             deployed
test01-cluster-autoscaler              1.29.3-gs1          12m          3m12s           deployed
test01-etcd-k8s-res-count-exporter     1.10.0              12m          28s             deployed
test01-external-dns                    3.1.0               12m          4m12s           deployed
test01-irsa-servicemonitors            0.1.0               12m          42s             deployed
test01-k8s-audit-metrics               0.10.0              12m          31s             deployed
test01-k8s-dns-node-cache              2.8.1               12m          114s            deployed
test01-kube-prometheus-stack           11.0.0              4m28s        57s             deployed
test01-metrics-server                  2.4.2               12m          115s            deployed
test01-net-exporter                    1.21.0              12m          41s             deployed
test01-node-exporter                   1.19.0              12m          43s             deployed
test01-observability-bundle            1.5.2               12m          4m28s           deployed
test01-security-bundle                 1.8.0               12m          3m32s           deployed
test01-teleport-kube-agent             0.9.2               12m          4m24s           deployed
test01-vertical-pod-autoscaler         5.2.4               12m          110s            deployed
...
```

__Note__: We don't enforce cluster prefix but it is a good practice to have it.

As you can see there are several applications already in the cluster. The one interesting for us is the `app-operator` app which is the Ingress NGINX Controller. This app is responsible for routing the traffic to the services running in the cluster.

## Step 2: Install an ingress Nginx controller

You can browse the apps in our catalog using our [web UI]({{< relref "/vintage/platform-overview/web-interface" >}})
but this information is also available in the management cluster. We create
[AppCatalogEntry]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs for the apps that are available.

First let's list the available [Catalog]({{< relref "/vintage/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
CRs.

```nohighlight
kubectl gs get catalogs

NAME                    CATALOG URL
giantswarm              https://giantswarm.github.io/giantswarm-catalog/
giantswarm-playground   https://giantswarm.github.io/giantswarm-playground-catalog/
```

Now we can list the latest version of each app in the catalog.

```nohighlight
kubectl gs get catalog giantswarm

CATALOG      APP NAME        APP VERSION   VERSION   AGE
...
giantswarm   ingress-nginx   v1.8.0        3.0.0     25d
...
```

## Step 3: Deploy hello-world app

We can use the [kubectl gs template app]({{< relref "/vintage/use-the-api/kubectl-gs/login" >}})
command to generate the App CR using the latest version from the previous command.

```nohighlight
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=${CLUSTER} \
  --name=ingress-nginx \
  --target-namespace=kube-system \
  --version=3.0.0 > ingress-nginx.yaml

kubectl apply -f ingress-nginx.yaml
cat ingress-nginx.yaml
```

Lets first see the output of the template command which shows only the
required fields.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ingress-nginx
  namespace: tm23r
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: ingress-nginx
  namespace: kube-system
  version: 3.0.0
```

The `--name` parameter is the name of the app in the catalog and the name of
the App CR. The App CR name can be changed via the `--app-name` parameter which
allows installing multiple instances of an app.
Keep in mind that the app name is subject to different length limits, depending on how the app is deployed.
Using a name under 30 characters is recommended.

Now lets check the app using the `kubectl gs get app` command.

```nohighlight
kubectl gs -n ${CLUSTER} get app ingress-nginx -o yaml
```

The labels, cluster config and kubeconfig have been all defaulted to the correct
values for your cluster. You can read more about defaulting and validation for
App CRs [here]({{< relref "/vintage/getting-started/app-platform/defaulting-validation" >}}).

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 4.4.0
    app.kubernetes.io/name: ingress-nginx
  name: ingress-nginx
  namespace: tm23r
spec:
  catalog: giantswarm
  config:
    configMap:
      name: ingress-controller-values
      namespace: tm23r
  kubeConfig:
    context:
      name: tm23r
    inCluster: false
    secret:
      name: tm23r-kubeconfig
      namespace: tm23r
  name: ingress-nginx
  namespace: kube-system
  version: 3.0.0
status:
  appVersion: v1.8.0
  release:
    lastDeployed: "2021-06-21T16:28:08Z"
    status: deployed
  version: 3.0.0
```

In the App CR status you can see that the app is deployed. The `appVersion`
shows that this version of the app is deploying `v0.45.0` of the upstream
[Ingress NGINX Controller](https://github.com/kubernetes/ingress-nginx) project.

## Step 4: Configuring the app with custom settings

The app is now deployed but what if we want to configure it with our own
settings? App platform is built on top of [Helm](https://helm.sh/docs/) and
your app is deployed as a Helm chart with values YAML. You can add custom
configuration as YAML and it will be merged with the rest of the configuration
we provide.

For this example we will do something simple and increase the log level from
notice to info. We can use `kubectl gs template app` to generate both the
updated App CR and the related Config Map.

```nohighlight
cat > ingress-values.yaml <<EOL
configmap:
  error-log-level: "info"
EOL

kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=${CLUSTER} \
  --name=ingress-nginx \
  --target-namespace=kube-system \
  --user-configmap=ingress-values.yaml \
  --version=3.0.0 > ingress-nginx.yaml

kubectl apply -f ingress-nginx.yaml
cat ingress-nginx.yaml
```

Now let's see what was generated. In the Config Map there is a values key with
the YAML and it is referenced in the App CR. You can also configure apps with
secrets for more sensitive configuration.

```yaml
apiVersion: v1
data:
  values: |
    configmap:
      error-log-level: "info"
kind: ConfigMap
metadata:
  name: ingress-nginx-userconfig-tm23r
  namespace: tm23r
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ingress-nginx
  namespace: tm23r
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: ingress-nginx
  namespace: kube-system
  userConfig:
    configMap:
      name: ingress-nginx-userconfig-tm23r
      namespace: tm23r
  version: 1.17.0
```

You can read more about app platform configuration [here]({{< relref "/vintage/getting-started/app-platform/app-configuration" >}})
and about advanced ingress configuration [here]({{< relref "/vintage/advanced/connectivity/ingress" >}}).

## Step 5: Deleting the hello-world app

This completes the guide. If you no longer need the ingress controller you can
run the commands below.

```nohighlight
kubectl delete --filename ingress-nginx.yaml
rm ingress-values.yaml ingress-nginx.yaml
```

## Next step

After learn how to deploy an application in the workload cluster, lets bump into [a different connectivity options you can rely on within the platform]({{< relref "/getting-started/expose-your-app" >}}).
