---
linkTitle: Deploying an app
title: Getting started deploying an app with the App Platform
description: Guide to deploying apps using kubectl gs and the Giant Swarm platform API.
weight: 20
aliases:
  - /getting-started/app-platform/deploy-app
  - /vintage/getting-started/app-platform/deploy-app
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-deploy-app
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I deploy an app using an App CR?
  - How can I configure an App CR?
  - How can I see which apps are available using the platform API?
last_review_date: 2025-11-27
---

The _Giant Swarm App Platform_ is built on top of [Helm](https://helm.sh/) and allows you to manage apps and their configurations represented by [App]({{< relref "/reference/platform-api/crd/apps.application.giantswarm.io.md" >}}) resources for multiple clusters, from a single place: the [platform API]({{< relref "/overview/architecture/#platform-api" >}}).

In this guide, we will install an ingress controller app. You will do this by using `kubectl`, creating
an App custom resource (CR) using the cluster API of your management cluster (also known platform API).

In general, you can manage App resources with any tool that can communicate with the cluster API such as `helm` or GitOps tools (like Argo CD or Flux CD).

## Setting up

You can access your management cluster using the [`kubectl gs login`]({{< relref "/reference/kubectl-gs/login" >}}) command of our kubectl plugin. See [here]({{< relref "/reference/kubectl-gs/installation" >}}) for how to install it.

In the management cluster, your App custom resources are stored in the namespace of the organization that owns the workload cluster you're installing to. Let's set environment variables for the organization name, namespace and cluster name, as we are going to need those in later commands.

```nohighlight
export ORGANIZATION=myteam
export NAMESPACE="org-${ORGANIZATION}"
export CLUSTER=mycluster
```

## Check if an ingress controller is installed

First we will check if there is already an ingress controller deployed.

In a fresh cluster, there shouldn't be any ingress controller, but we better list apps to make sure. If an ingress controller is installed already, please use another cluster.

```nohighlight
$ kubectl gs -n ${NAMESPACE} get apps

NAME                                             VERSION    LAST DEPLOYED   STATUS
mycluster                                        6.2.0      7d2h            deployed
mycluster-alloy-events                           0.15.1     3d3h            deployed
mycluster-alloy-logs                             0.15.1     3d3h            deployed
mycluster-alloy-metrics                          0.15.1     3h38m           deployed
mycluster-app-operator                           7.5.0      28d             deployed
mycluster-auth-bundle                            0.2.3      211d            deployed
mycluster-aws-ebs-csi-driver-smons               0.1.0      534d            deployed
mycluster-aws-load-balancer-controller           2.2.1      8d              deployed
mycluster-aws-pod-identity-webhook               2.0.0      29d             deployed
```

## Finding the ingress controller version

You can browse the apps in our catalog using [the developer portal UI]({{< relref "/overview/developer-portal/" >}}) but this information is also available in the management cluster in form of resources. The [AppCatalogEntry]({{< relref "/reference/platform-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) custom resources show the apps that are available.

First let's list the available [Catalog]({{< relref "/reference/platform-api/crd/catalogs.application.giantswarm.io.md" >}}) custom resources.

```nohighlight
kubectl gs get catalogs

NAME                    CATALOG URL
giantswarm              https://giantswarm.github.io/giantswarm-catalog/
giantswarm-playground   https://giantswarm.github.io/giantswarm-playground-catalog/
```

Now we can list the latest version of each app in the catalog.

```nohighlight
kubectl gs get catalog giantswarm

CATALOG      APP NAME        APP VERSION   VERSION    AGE
...
giantswarm   ingress-nginx   4.2.0         1.14.0     22d
...
```

## Creating an App resource

We can use the [`kubectl gs template app`]({{< relref "/reference/kubectl-gs/login" >}})
command to generate the `App` resource using the latest version from the previous command.

```nohighlight
kubectl gs template app \
  --catalog=giantswarm \
  --orgnanization=${ORGANIZATION} \
  --cluster-name=${CLUSTER} \
  --name=ingress-nginx \
  --target-namespace=kube-system \
  --version=4.2.0 > ingress-nginx.yaml

kubectl apply -f ingress-nginx.yaml
cat ingress-nginx.yaml
```

Lets first see the output of the template command which shows only the required fields.

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: mycluster-ingress-nginx
  namespace: org-myteam
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: ingress-nginx
  namespace: kube-system
  version: 4.2.0
```

The `--name` parameter is the name of the app in the catalog and the name of the App resource. The App resource name can be changed via the `--app-name` parameter which allows installing multiple instances of an app. Keep in mind that the app name is subject to different length limits, depending on how the app is deployed. Using a name under 30 characters is recommended.

## Defaulting and app status

Now lets check the app using the `kubectl gs get app` command.

```nohighlight
kubectl gs -n ${NAMESPACE} get app ${CLUSTER}-ingress-nginx -o yaml
```

The labels, cluster configuration and kubeconfig have been all defaulted to the correct values for your cluster. You can read more about defaulting and validation for App resources [here]({{< relref "/tutorials/fleet-management/app-platform/defaulting-validation" >}}).

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  labels:
    app-operator.giantswarm.io/version: 4.4.0
    app.kubernetes.io/name: ingress-nginx
  name: mycluster-ingress-nginx
  namespace: org-myteam
spec:
  catalog: giantswarm
  config:
    configMap:
      name: mycluster-ingress-controller-values
      namespace: org-myteam
  kubeConfig:
    context:
      name: mycluster
    inCluster: false
    secret:
      name: mycluster-kubeconfig
      namespace: org-myteam
  name: ingress-nginx
  namespace: kube-system
  version: 4.2.0
status:
  appVersion: v1.14.0
  release:
    lastDeployed: "2021-06-21T16:28:08Z"
    status: deployed
  version: 4.2.0
```

In the App resource status you can see that the app is deployed. The `appVersion` shows that this version of the app is deploying `v1.14.0` of the upstream [ingress nginx controller](https://github.com/kubernetes/ingress-nginx) project.

## Configuring an app

The app is now deployed but how to configure it with your custom settings? App platform is built on top of [Helm](https://helm.sh/docs/) and your app is deployed as a Helm chart with values YAML. You can add custom configuration as YAML and it will be merged with the rest of the configuration.

For this example we will do something simple and increase the log level from notice to info. We can use `kubectl gs template app` to generate both the updated App resource and the related ConfigMap.

```nohighlight
cat > ingress-values.yaml <<EOL
configmap:
  error-log-level: "info"
EOL

kubectl gs template app \
  --catalog=giantswarm \
  --organization=${ORGANIZATION} \
  --cluster-name=${CLUSTER} \
  --name=ingress-nginx \
  --target-namespace=kube-system \
  --user-configmap=ingress-values.yaml \
  --version=3.0.0 > ingress-nginx.yaml

kubectl apply -f ingress-nginx.yaml
cat ingress-nginx.yaml
```

Now let's see what was generated. In the ConfigMap there is a values key with the YAML and it's referenced in the App resource. You can also configure apps with secrets for more sensitive configuration.

```yaml
apiVersion: v1
data:
  values: |
    configmap:
      error-log-level: "info"
kind: ConfigMap
metadata:
  name: mycluster-ingress-nginx-userconfig
  namespace: org-myteam
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: mycluster-ingress-nginx
  namespace: org-myteam
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: ingress-nginx
  namespace: kube-system
  userConfig:
    configMap:
      name: mycluster-ingress-nginx-userconfig
      namespace: org-myteam
  version: 1.17.0
```

You can read more about app platform configuration [here]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}) and about advanced ingress configuration [here]({{< relref "/tutorials/connectivity/ingress/configuration" >}}).

## Deleting an App CR

This completes the guide. If you no longer need the ingress controller you can run the commands below.

```nohighlight
kubectl delete --filename ingress-nginx.yaml
```
