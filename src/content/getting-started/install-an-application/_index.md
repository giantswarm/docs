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

The _Giant Swarm App Platform_ is built on top of [Helm](https://helm.sh/) charts and allows you to manage apps and their configurations represented by `App` custom resources (CRs) for multiple clusters, from a single place: the [Platform API]({{< relref "/overview/architecture#platform-api" >}}) on the management cluster.

In this guide, we will install a `hello-world` app together with an Ingress NGINX Controller to serve the web application publicly. We will do this by using kubectl, to create an [App]({{< relref "/vintage/use-the-api/management-api/crd/apps.application.giantswarm.io.md" >}}) CR using the platform API of your management cluster.

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

To know which applications are available for customers we've extended the platform with two custom resources. First resource is the [`AppCatalog`]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogs.application.giantswarm.io/" >}}) which is a recipient to collect application definitions that are available to install in the workload clusters. The second is the [`AppCatalogEntry`]({{< relref "/vintage/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) which is the representation of the application definition which has a version defined.

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

Then, template the application to target the right organization and workload cluster:

```sh
kubectl gs template app \
  --catalog=giantswarm \
  --cluster-name=test01 \
  --organization=testing \
  --name=test01-hello-world \
  --target-namespace=default \
  --version=2.3.2 > hello-world.yaml
```

Lets take a look at the `App CR` to learn main fields available:

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: test01-hello-world
  namespace: org-giantswarm
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: hello-world
  namespace: kube-system
  version: 2.3.2
```

The `name` field is the name of the app in the catalog meanwhile `--app-name` designates the name of the app instance installed in the cluster. Keep in mind that the app name is subject to different length limits, depending on how the app is deployed. Using a name under 30 characters is recommended.

After a few seconds, you should see the deployed status:

```nohighlight
$ kubectl get app -n org-testing test01-hello-world
NAME                INSTALLED VERSION   CREATED AT   LAST DEPLOYED   STATUS
test01-hello-world   2.3.2               11s          8s              deployed
```

Now you can access your workload cluster, check the app running, and see which ingress address has been generated:

```nohighlight
kubectl get ingress -n default
NAME          CLASS   HOSTS                                        ADDRESS                                                                       PORTS     AGE
hello-world   nginx   cluster.provider.k8s.giantswam.io   ab49484.cn-north-1.elb.amazonaws.com.cn   80, 443   2m29s
```

Sadly, the address isn't accessible because we've not passed the right domain on to the ingress controller.

## Step 4: Configuring the right domain

For every workload cluster there is a default wildcard record created automatically by our controllers. The domain is composed by the cluster name and the provider, the region and the base domain.

```sh
$ kubectl get cm -n org-testing test01-cluster-values -ojsonpath="{.data.values}" | grep baseDomain
baseDomain: test01.capi.aws.k8s.gigantic.io
```

With that information, you can customize the `hello-world` app to use the right domain. The [app values schema](https://github.com/giantswarm/hello-world-app/blob/main/helm/hello-world/README.md) documents which values can be changed. Here, the `hosts` and `tls` sections are relevant.

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

Now we can template the app again passing the file reference:

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

Again, push the generated `App` CR file to your GitOps repository, or apply it directly to the management cluster with the following command:

```sh
kubectl apply -f hello-world.yaml
```

```nohighlight
$ kubectl get app test01-hello-world
NAME                INSTALLED VERSION  CREATED AT  LAST DEPLOYED  STATUS
test01-hello-world  2.3.2              51m         8s             deployed
```

At this point you should be able to access the `hello-world` app using the domain you have configured. Check the `URL` value in the ingress resource has been updated to be sure the changes have been propagated. Now you should be able to see the hello world frontend.

![Hello world page](hello-world.png)

__Note__:You can read more about app platform configuration [here]({{< relref "/vintage/getting-started/app-platform/app-configuration" >}}).

## Step 5: Deleting the hello-world app and ingress-nginx controller

The deletion of an app is as simple as creating it:

```nohighlight
kubectl delete -f hello-world.yaml

kubectl delete -f ingress-nginx.yaml
```

## Next step

After learn how to deploy an application in the workload cluster, lets bump into [a different connectivity options you can rely on within the platform]({{< relref "/getting-started/expose-your-app" >}}).
