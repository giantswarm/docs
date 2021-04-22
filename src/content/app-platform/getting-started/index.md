---
linkTitle: Getting started
title: Getting started with App Platform
description: Guide to deploying apps using kubectl and the Giant Swarm Management API.
weight: 20
menu:
  main:
    parent: app-platform
last_review_date: 2021-04-21
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - How can I deploy an app using an App CR?
  - How can I configure an App CR?
  - How can I see which apps are available using the Management API?
---

# Getting started with App Platform

## Overview

In this guide we will install an ingress controller which helps you expose your
services to the outside world.

We already have a [guide]({{< relref "/getting-started/ingress-controller" >}})
for doing this using our web UI. For this guide we will use kubectl to create
[App]({{< relref "/ui-api/management-api/crd/apps.application.giantswarm.io.md" >}})
custom resources (CRs) using the Kubernetes API of your
[management cluster]({{< relref "/general/management-clusters" >}}).

However you can manage the App CRs with any tool that can communicate
with the Kubernetes API such as Helm or GitOps tools (like Argo CD or Flux).

## Setting up

You can access your management cluster using the [kubectl gs login]({{< relref "/ui-api/kubectl-gs/login" >}})
command of our kubectl plugin. See [here]({{< relref "/ui-api/kubectl-gs/installation" >}})
for how to install it.

In the management cluster your App CRs are stored in a namespace with the same
name as your workload cluster ID. Let's set an environment variable for this
which we will use in the later steps.

```sh
export NAMESPACE=** your cluster id**
```

## Checking if your cluster has an ingress controller

First we will check if there is already an ingress controller deployed.

We can see the apps that were pre-installed in the cluster but there is no
`nginx-ingress-controller` or `nginx-ingress-controller-app` App CR so we can
continue with the guide.

In some older releases the ingress controller is pre-installed. If this is the
case please use another cluster.

```sh
kubectl -n ${NAMESPACE} gs get apps

NAME                       VERSION   LAST DEPLOYED   STATUS
cert-exporter              1.6.1     69m             deployed
cert-manager               2.4.3     68m             deployed
chart-operator             2.13.0    68m             deployed
cluster-autoscaler         1.19.2    69m             deployed
coredns                    1.4.1     67m             deployed
external-dns               2.3.0     69m             deployed
grafana                    0.2.0     46m             deployed
kiam                       1.7.1     67m             deployed
kube-state-metrics         1.3.1     69m             deployed
metrics-server             1.2.2     69m             deployed
net-exporter               1.9.3     69m             deployed
node-exporter              1.7.2     68m             deployed
```

## Finding the ingress controller version

You can browse the apps in our catalog using our [web UI]({{< relref "/ui-api/web" >}})
but this information is also available in the management cluster. We create
[AppCatalogEntry]({{< relref "/ui-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs for the apps that are available.

In this example we are filtering using the `latest=true` label to show only the
latest version according to semantic versioning.

We are also filtering using the catalog label. You can change this to
`giantswarm-playground` to show our more experimental apps which we encourage
you to try but do not offer as a managed service.

```sh
kubectl get appcatalogentry -l latest=true,application.giantswarm.io/catalog=giantswarm

NAME                                             CATALOG      APP NAME                       APP VERSION   VERSION        AGE
...
giantswarm-nginx-ingress-controller-app-1.16.1   giantswarm   nginx-ingress-controller-app   v0.45.0       1.16.1         25h
...
```

## Creating an App CR

We can use the [kubectl gs template app]({{< relref "/ui-api/kubectl-gs/login" >}})
command to generate the App CR using the latest version from the previous command.

```sh
kubectl gs template app \
  --catalog=giantswarm \
  --cluster=${NAMESPACE} \
  --name=nginx-ingress-controller-app \
  --namespace=kube-system \
  --version=1.16.1 > nginx-ingress-controller-app.yaml

kubectl apply -f nginx-ingress-controller-app.yaml
```

Lets first see the output of the template command which shows only the
required fields.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: nginx-ingress-controller-app
  namespace: s2wf9
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: nginx-ingress-controller-app
  namespace: kube-system
  version: 1.16.1
```

## Defaulting and App Status

Now lets check the app using the `kubectl gs get app` command which filters
the output to show only the most important fields.

```sh
kubectl -n ${NAMESPACE} gs get app nginx-ingress-controller-app -o yaml
```

The labels, cluster config and kubeconfig have been all defaulted to the correct
values for your cluster. You can read more about defaulting and validation for
App CRs [here]({{< relref "/app-platform/defaulting-validation" >}}).

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 3.2.1
    app.kubernetes.io/name: nginx-ingress-controller-app
  name: nginx-ingress-controller-app
  namespace: s2wf9
spec:
  catalog: giantswarm
  config:
    configMap:
      name: ingress-controller-values
      namespace: s2wf9
  kubeConfig:
    context:
      name: s2wf9
    inCluster: false
    secret:
      name: s2wf9-kubeconfig
      namespace: s2wf9
  name: nginx-ingress-controller-app
  namespace: kube-system
  version: 1.16.1
status:
  appVersion: v0.45.0
  release:
    lastDeployed: "2021-04-21T16:28:08Z"
    status: deployed
  version: 1.16.1
```

In the App CR status you can see that the app is deployed. The `appVersion`
shows that this version of the app is deploying `v0.45.0` of the upstream
[Nginx Ingress Controller](https://github.com/kubernetes/ingress-nginx) project.

## Configuring an App CR

The app is now deployed but what if we want to configure it with our own
settings? App platform is built on top of [Helm](https://helm.sh/docs/) and
your app is deployed as a Helm chart with values YAML. You can add custom
configuation as YAML and it will be merged with the rest of the configuation
we provide.

For this example we will do something simple and ensure we always run 2 replicas
for the ingress controller. We can use `kubectl gs template app` to generate
both the App CR and the related Config Map.

```sh
cat > ingress-values.yaml <<EOL
controller:
  replicas: 2
autoscaling:
  enabled: false
EOL

kubectl gs template app \
  --catalog=giantswarm \
  --cluster=${NAMESPACE} \
  --name=nginx-ingress-controller-app \
  --namespace=kube-system \
  --user-configmap=ingress-values.yaml \
  --version=1.16.1 > nginx-ingress-controller-app.yaml
cat nginx-ingress-controller-app.yaml
```

Now let's see what was generated. In the Config Map there is a values key with
the YAML and it is referenced in the App CR. You can also configure apps with
secrets for more sensitive configuration.

```sh
apiVersion: v1
data:
  values: |
    controller:
      replicas: 2
    autoscaling:
      enabled: false
kind: ConfigMap
metadata:
  name: nginx-ingress-controller-app-userconfig-s2wf9
  namespace: s2wf9
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: nginx-ingress-controller-app
  namespace: s2wf9
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: nginx-ingress-controller-app
  namespace: kube-system
  userConfig:
    configMap:
      name: nginx-ingress-controller-app-userconfig-s2wf9
      namespace: s2wf9
  version: 1.16.1
```

You can read more about app platform configuration [here]({{< relref "/app-platform/app-configuration" >}})
and about advanced ingress configuration [here]({{< relref "/advanced/ingress" >}}).

## Deleting an App CR

This completes the guide. If you no longer need the ingress controller you can
run the commands below.

```sh
kubectl delete -f nginx-ingress-controller-app.yaml
rm ingress-values.yaml nginx-ingress-controller-app.yaml
```
