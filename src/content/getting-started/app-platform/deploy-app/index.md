---
linkTitle: Deploying an app
title: Getting started deploying an app with the App Platform
description: Guide to deploying apps using kubectl gs and the Giant Swarm Management API.
weight: 20
menu:
  main:
    parent: getting-started-app-platform
    identifier: getting-started-app-platform-deploy-app
last_review_date: 2022-12-08
aliases:
  - /developer-platform/app-platform/getting-started
  - /app-platform/getting-started
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy an app using an App CR?
  - How can I configure an App CR?
  - How can I see which apps are available using the Management API?
---

## Overview

The _Giant Swarm App Platform_ is built on top of [Helm](https://helm.sh/) and allows you to manage apps and their configurations represented by App Custom Resources (CRs) for multiple clusters, from a single place: the [Management API]({{< relref "/platform-overview/management-api" >}}).

In this guide, we will install the Ingress NGINX Controller app. We will do this by using kubectl, to create
an [App]({{< relref "/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR using the Kubernetes API of your management cluster.

App CRs can be created this way via your automation or our Web UI (See: [guide]({{< relref "/getting-started/connectivity/ingress-controller" >}})).

In general, you can manage App CRs with any tool that can communicate with the Kubernetes API such as Helm or GitOps tools (like Argo CD or Flux CD).

## Setting up

You can access your management cluster using the [kubectl gs login]({{< relref "/use-the-api/kubectl-gs/login" >}})
command of our kubectl plugin. See [here]({{< relref "/use-the-api/kubectl-gs/installation" >}})
for how to install it.

In the management cluster your App CRs are stored in a namespace with the same
name as your workload cluster ID. Let's set an environment variable for this
which we will use in the later steps.

```nohighlight
export CLUSTER=CLUSTER_ID
```

## Checking if your cluster has an Ingress Controller

First we will check if there is already an Ingress Controller deployed.

We can see the apps that were pre-installed in the cluster but there is no
`ingress-nginx` App CR so we can continue with the guide.

In some older releases the ingress controller is pre-installed. If this is the
case please use another cluster.

```nohighlight
kubectl gs -n ${CLUSTER} get apps

NAME                 VERSION   LAST DEPLOYED          STATUS
app-operator-tm23r   4.4.0     07 Jul 21 14:20 CEST   deployed
cert-exporter        1.6.1     07 Jul 21 14:39 CEST   deployed
cert-manager         2.7.1     07 Jul 21 14:37 CEST   deployed
chart-operator       2.14.0    07 Jul 21 14:39 CEST   deployed
cluster-autoscaler   1.19.3    07 Jul 21 14:39 CEST   deployed
coredns              1.4.1     07 Jul 21 14:39 CEST   deployed
external-dns         2.3.1     07 Jul 21 14:39 CEST   deployed
kiam                 1.7.1     07 Jul 21 14:41 CEST   deployed
kube-state-metrics   1.3.1     07 Jul 21 14:39 CEST   deployed
metrics-server       1.3.0     07 Jul 21 14:39 CEST   deployed
net-exporter         1.10.1    07 Jul 21 14:39 CEST   deployed
node-exporter        1.7.2     07 Jul 21 14:39 CEST   deployed
```

app-operator is running in the management cluster and the rest of the apps are
installed in your workload cluster.

## Finding the ingress controller version

You can browse the apps in our catalog using our [web UI]({{< relref "/platform-overview/web-interface" >}})
but this information is also available in the management cluster. We create
[AppCatalogEntry]({{< relref "/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs for the apps that are available.

First let's list the available [Catalog]({{< relref "/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
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

## Creating an App CR

We can use the [kubectl gs template app]({{< relref "/use-the-api/kubectl-gs/login" >}})
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

## Defaulting and App Status

Now lets check the app using the `kubectl gs get app` command.

```nohighlight
kubectl gs -n ${CLUSTER} get app ingress-nginx -o yaml
```

The labels, cluster config and kubeconfig have been all defaulted to the correct
values for your cluster. You can read more about defaulting and validation for
App CRs [here]({{< relref "/getting-started/app-platform/defaulting-validation" >}}).

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

## Configuring an App CR

The app is now deployed but what if we want to configure it with our own
settings? App platform is built on top of [Helm](https://helm.sh/docs/) and
your app is deployed as a Helm chart with values YAML. You can add custom
configuation as YAML and it will be merged with the rest of the configuation
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

You can read more about app platform configuration [here]({{< relref "/getting-started/app-platform/app-configuration" >}})
and about advanced ingress configuration [here]({{< relref "/advanced/connectivity/ingress" >}}).

## Deleting an App CR

This completes the guide. If you no longer need the ingress controller you can
run the commands below.

```nohighlight
kubectl delete --filename ingress-nginx.yaml
rm ingress-values.yaml ingress-nginx.yaml
```
