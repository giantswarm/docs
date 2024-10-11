---
title: Install an application using the app platform
linkTitle: Install an application
description: Add capabilities to your platform by deploying applications from our catalog.
weight: 50
last_review_date: 2024-09-06
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

The _Giant Swarm App Platform_ is built on top of [Helm](https://helm.sh/) charts and allows you to manage apps and their configurations represented by `App` custom resources (CRs) for multiple clusters, from a single place: the [Platform API]({{< relref "/overview/architecture#platform-api" >}}) on the management cluster.

In this guide, we will install a `hello-world` app together with an ingress nginx controller to serve the web application publicly. We will do this by using kubectl, to create an [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR using the platform API of your management cluster.

In general, you can manage `App` CRs with any tool that can communicate with the Kubernetes API such as Helm or GitOps tools (like Argo CD or Flux CD).

## Requirements

First of all, you need a running workload cluster. If you don't have one, please first [create a workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).

The `App` CRs are stored in an organization namespace, together with the cluster resources. Ensure you are logged into the management cluster. You can list the organizations by running the following command:

```nohighlight
kubectl gs get organizations
```

and you will see the organization that you have access to. Make sure you target the right organization where your workload cluster is running. You can switch to the organization namespace before creating the App CR by running:

```nohighlight
kubectl config set-context --current --namespace=org-namespace
```

That way you ensure that the App CR is created in the correct namespace.

## Step 1: Check applications installed in the cluster

First we will take a look to the existing applications already running in the cluster. By default the cluster has some default apps to make the cluster operational. Since you can have more than one cluster in the namespace, let's filter the apps by the cluster name.

Ensure you are logged into the management cluster.

```nohighlight
$ kubectl gs -n org-namespace get apps
NAME                                 VERSION          CREATED_AT   LAST_DEPLOYED        STATUS
test01                                 2.0.0               13m          12m             deployed
test01-app-operator                    6.11.0              12m          12m             deployed
test01-aws-ebs-csi-driver-smons        0.1.0               12m          42s             deployed
test01-aws-pod-identity-webhook        1.16.0              12m          117s            deployed
...
test01-observability-bundle            1.5.2               12m          4m28s           deployed
test01-security-bundle                 1.8.0               12m          3m32s           deployed
test01-teleport-kube-agent             0.9.2               12m          4m24s           deployed
test01-vertical-pod-autoscaler         5.2.4               12m          110s            deployed
```

__Note__: We don't enforce the cluster prefix (here: `test01-`), but it's a good practice to have it.

You can see that several applications already exist for the workload cluster `test01`. Most of the apps run directly in the workload cluster itself. The operator which actually deploys the applications to the workload clusters is running on the management cluster and is called `app-operator`. Learn more about this process [in this guide]({{< relref "/vintage/platform-overview/app-platform/" >}}).

## Step 2: Install an ingress nginx controller {#install-ingress-controller}

Before installing the `hello-world` app, an ingress controller must be running in the cluster. The ingress controller is responsible for routing the incoming traffic to the correct service in the cluster and make it available publicly.

To know which applications are available for customers we've extended the platform with two custom resources. The first resource is [`AppCatalog`]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogs.application.giantswarm.io/" >}}) which contains application definitions that are available for installation in the workload clusters. The second is the [`AppCatalogEntry`]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) which is the application definition for each application version.

By default there is a single catalog in the platform with the applications maintained by us:

```nohighlight
kubectl gs get catalogs
NAME                    CATALOG URL
giantswarm              https://giantswarm.github.io/giantswarm-catalog/
```

__Note__: You can [create your own catalog]({{< relref "/vintage/getting-started/app-platform/create-catalog/" >}}) and add your own applications to it.

To browse which applications are available in the catalog you can run the following command:

```nohighlight
kubectl get appcatalogentries -n default -l application.giantswarm.io/catalog=giantswarm
````

In our case we're interested in the ingress nginx controller, so let's check the latest version available in the catalog:

```nohighlight
kubectl get appcatalogentries -n default -l app.kubernetes.io/name=ingress-nginx
NAME                             CATALOG      APP NAME        VERSION   UPSTREAM VERSION   AGE
giantswarm-ingress-nginx-3.9.2   giantswarm   ingress-nginx   3.9.2     1.11.2             2d4h
...
```

The latest version of the ingress-nginx controller is `3.9.2` in this example. Next, template the `App` CR using the `kubectl gs template app` command, filling in the desired version:

```sh
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=test01 \
  --organization=testing \
  --app-name=test01-ingress-nginx \
  --name=ingress-nginx \
  --target-namespace=kube-system \
  --version=3.9.2 > ingress-nginx.yaml
```

You can push the generated `App` CR file to your GitOps repository, or apply it directly to the management cluster with the following command:

```sh
kubectl apply -f ingress-nginx.yaml
```

If you log into the workload cluster now, ingress controller should be running very soon:

```nohighlight
$ kubectl get app ingress-nginx
NAME            INSTALLED VERSION   CREATED AT   LAST DEPLOYED   STATUS
test01-ingress-nginx   3.9.2               16s          14s             deployed
```

## Step 3: Deploy hello-world app

The next step is deploying the `hello-world` application using the same approach as for the ingress controller.

First, list the versions with:

```nohighlight
kubectl get appcatalogentries -n default -l app.kubernetes.io/name=hello-world
NAME                           CATALOG      APP NAME      VERSION   UPSTREAM VERSION   AGE
...
giantswarm-hello-world-2.3.2   giantswarm   hello-world   2.3.2     0.2.1              72d
```

To make our app accessible from the internet, an [ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) should be defined with the right domain. By default every workload cluster comes with a default wildcard DNS record (e.g. `*.test01.capi.aws.k8s.gigantic.io`). The domain is composed by the cluster name and the management cluster's base domain.

You can find the domain of your workload cluster like this:

```sh
$ kubectl get cm -n org-testing test01-cluster-values -ojsonpath="{.data.values}" | grep baseDomain
baseDomain: test01.capi.aws.k8s.gigantic.io
```

With that information, you can extend the `hello-world` application manifest to use the right domain. Check the [application values schema](https://github.com/giantswarm/hello-world-app/blob/main/helm/hello-world/README.md) to see what values can be customized. Here, the `hosts` and `tls` sections are relevant.

Create a file containing the Helm chart values:

```sh
cat > hello-world-values.yaml <<EOF
ingress:
hosts:
- host: hello.test01.capi.aws.k8s.gigantic.io
  paths:
  - path: /
    pathType: Prefix
tls:
- secretName: hello-world-tls
  hosts:
  - hello.test01.capi.aws.k8s.gigantic.io
EOF
```

Then, template the application to target the right organization and workload cluster. Also the extra configuration is passed as argument.

```sh
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=test01 \
  --organization=testing \
  --name=test01-hello-world \
  --target-namespace=default \
  --user-configmap=hello-world-values.yaml \
  --version=2.3.2 > hello-world.yaml
```

Lets take a look at the manifests generated to learn how they look like:

```yaml
apiVersion: v1
data:
  values: |
    ingress:
      [...]
kind: ConfigMap
metadata:
  creationTimestamp: null
  name: test01-hello-world-userconfig
  namespace: org-testing
---
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: test01-hello-world
  namespace: org-testing
spec:
  catalog: giantswarm
  name: hello-world
  namespace: kube-system
  userConfig:
    configMap:
      name: test01-hello-world-userconfig
      namespace: org-testing
  version: 2.3.2
```

The `spec.name` field is the application's name in the catalog, while `metadata.name` designates the name of the `App` object in the cluster and can therefore be freely chosen. [Read more information about the properties here]({{ relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io/" }}).

Now let's push the file to your GitOps repository, or apply it directly to the platform API with the following command:

```sh
kubectl apply -f hello-world.yaml
```

```nohighlight
$ kubectl get app -n org-testing test01-hello-world
NAME                INSTALLED VERSION  CREATED AT  LAST DEPLOYED  STATUS
test01-hello-world  2.3.2              51m         8s             deployed
```

If both the ingress-nginx controller and the hello-world app are healthy in the workload cluster, you should be able to access the hello world web page at `https://hello.test01.capi.aws.k8s.gigantic.io` (please fill in your own workload cluster domain).

Based on the above `Ingress` definition in the Helm values, a TLS certificate should have been automatically generated using cert-manager, which is installed by default. Since the trusted certificate authority Let's Encrypt is used by default, your browser should show the web page as secure, without warnings.

![Hello world page](hello-world.png)

__Note__:You can read more about app platform configuration [here]({{< relref "/vintage/getting-started/app-platform/app-configuration" >}}).

After a few seconds, you should see the deployed status:

```nohighlight
$ kubectl get app -n org-testing test01-hello-world
NAME                INSTALLED VERSION   CREATED AT   LAST DEPLOYED   STATUS
test01-hello-world   2.3.2               11s          8s              deployed
```

Now you can access your workload cluster, check the app running, and see which ingress address has been generated:

```nohighlight
kubectl get ingress -n default
NAME          CLASS   HOSTS      ADDRESS      PORTS     AGE
hello-world   nginx   hello.test01.capi.aws.k8s.gigantic.io   ab49484...   80, 443   2m29s
```

It's time to try to reach the application using the ingress:

```nohighlight
$ curl -Is https://hello.test01.capi.aws.k8s.gigantic.io
/ HTTP/1.1 200 OK
/ Accept-Ranges: bytes ...
```

The `curl` request it's routed through the AWS load balancer to the ingress controller, which then forwards the request to the `hello-world` service.

## Step 4: Deleting the hello-world app and ingress-nginx controller

The deletion of an app is as simple as creating it:

```sh
kubectl delete -f hello-world.yaml

kubectl delete -f ingress-nginx.yaml
```

## Next step

After learning how to deploy an application in the workload cluster, let's dive into [in how networking works in your cluster and how to configure security hardening of your application]({{< relref "/getting-started/expose-your-app" >}}).
