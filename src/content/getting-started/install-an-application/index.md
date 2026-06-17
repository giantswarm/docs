---
title: Install an application
linkTitle: Install an application
description: Deploy applications to your workload cluster using Flux HelmRelease.
weight: 40
last_review_date: 2026-06-17
menu:
  principal:
    parent: getting-started
    identifier: getting-started-install-app
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - How do I deploy applications on Giant Swarm?
  - How do I install an application with Flux HelmRelease?
  - How do I configure an app's Helm values?
  - How do I expose an app over HTTPS?
---

Giant Swarm runs Flux on every management cluster, and Flux HelmRelease is the recommended way to deploy applications to your workload clusters. This guide walks you through installing two apps end to end: an ingress controller (so HTTP traffic reaches your cluster) and a hello-world demo behind it.

**Note:** If you have existing deployments using the legacy Giant Swarm `App` custom resource, see [App CR deprecation]({{< relref "/overview/fleet-management/app-management/app-cr-deprecation" >}}) for the migration path. For new deployments, follow this guide.

For a deeper reference covering every flag and option, see [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).

## Requirements

First, you need a running workload cluster. If you don't have one, follow [Provision your first workload cluster]({{< relref "/getting-started/provision-your-first-workload-cluster" >}}).

You also need:

- The [Flux CLI](https://fluxcd.io/flux/cmd/) installed locally.
- Access to the management cluster (see [kubectl gs login]({{< relref "/reference/kubectl-gs/login" >}})).
- Access to the organization namespace where your cluster lives.

List the organizations you have access to:

```sh
kubectl gs get organizations
```

Then set environment variables for the org, namespace, and cluster name. We use these in every command below:

```sh
export ORGANIZATION=testing
export NAMESPACE=org-${ORGANIZATION}
export CLUSTER=test01
```

## Step 1: Check what's already installed

Before adding anything, list the HelmReleases already running in your organization namespace, filtered to your cluster:

```sh
flux get helmreleases \
  --namespace ${NAMESPACE} \
  --selector giantswarm.io/cluster=${CLUSTER}
```

You'll see the apps that ship with the cluster (default-apps bundle, observability tooling, and so on). If you already have an ingress controller running, skip ahead to Step 4.

## Step 2: Install ingress-nginx

The hello-world app needs an ingress controller so it can be reached from outside the cluster. Install one with two Flux resources: an `OCIRepository` that points at the chart in Giant Swarm's registry, and a `HelmRelease` that installs it into the workload cluster.

Create the OCIRepository first:

```sh
flux create source oci ${CLUSTER}-ingress-nginx \
  --url oci://gsoci.azurecr.io/charts/giantswarm/ingress-nginx \
  --tag 3.9.2 \
  --namespace ${NAMESPACE} \
  --interval 60m
```

Then create the HelmRelease:

```sh
flux create helmrelease ${CLUSTER}-ingress-nginx \
  --namespace ${NAMESPACE} \
  --chart-ref OCIRepository/${CLUSTER}-ingress-nginx \
  --kubeconfig-secret-ref ${CLUSTER}-kubeconfig \
  --target-namespace kube-system \
  --label giantswarm.io/cluster=${CLUSTER} \
  --release-name ${CLUSTER}-ingress-nginx \
  --interval 60m
```

What each flag does:

- `--chart-ref` points at the OCIRepository created in the previous command.
- `--kubeconfig-secret-ref` tells Flux which workload cluster to install into. The Secret is created for you alongside the cluster and follows the `<cluster>-kubeconfig` naming convention.
- `--target-namespace` is the namespace in the workload cluster where the chart's resources are created.
- `--label giantswarm.io/cluster=${CLUSTER}` makes the resource show up under the correct cluster in the developer portal.

After a few seconds, check the status:

```sh
flux get helmrelease \
  --namespace ${NAMESPACE} \
  ${CLUSTER}-ingress-nginx
```

You should see `True` under the `Ready` column.

## Step 3: Find your cluster's base domain

Every workload cluster comes with a wildcard DNS record, so apps you expose are reachable at `<name>.${CLUSTER}.<base-domain>`. Read the base domain from the cluster values ConfigMap:

```sh
kubectl get configmap \
  --namespace ${NAMESPACE} \
  ${CLUSTER}-cluster-values \
  -o jsonpath="{.data.values}" | grep baseDomain
```

You'll see something like `baseDomain: test01.capi.aws.k8s.gigantic.io`. Save that for the next step.

## Step 4: Deploy the hello-world app

Create a `values.yaml` with the ingress hostname for the hello-world app (replace the base domain with yours):

```yaml
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
```

Create the OCIRepository for the chart:

```sh
flux create source oci ${CLUSTER}-hello-world \
  --url oci://gsoci.azurecr.io/charts/giantswarm/hello-world \
  --tag 2.9.1 \
  --namespace ${NAMESPACE} \
  --interval 60m
```

Then the HelmRelease, pointing at your `values.yaml`:

```sh
flux create helmrelease ${CLUSTER}-hello-world \
  --namespace ${NAMESPACE} \
  --chart-ref OCIRepository/${CLUSTER}-hello-world \
  --values ./values.yaml \
  --kubeconfig-secret-ref ${CLUSTER}-kubeconfig \
  --target-namespace default \
  --label giantswarm.io/cluster=${CLUSTER} \
  --release-name ${CLUSTER}-hello-world \
  --interval 60m
```

Once the HelmRelease reports `Ready=True`, the app is reachable at the host you configured. Try it:

```sh
curl -Is https://hello.test01.capi.aws.k8s.gigantic.io
```

You should get back `HTTP/1.1 200 OK`. The TLS certificate is issued by cert-manager (installed by default) through Let's Encrypt, so your browser treats the site as secure.

![Hello world page](hello-world.png)

## Step 5: Clean up

To remove the demo, delete the HelmRelease and OCIRepository for each app in reverse order of creation:

```sh
flux delete helmrelease --namespace ${NAMESPACE} ${CLUSTER}-hello-world
flux delete source oci  --namespace ${NAMESPACE} ${CLUSTER}-hello-world

flux delete helmrelease --namespace ${NAMESPACE} ${CLUSTER}-ingress-nginx
flux delete source oci  --namespace ${NAMESPACE} ${CLUSTER}-ingress-nginx
```

## Next step

After learning how to deploy an application in the workload cluster, dive into [how networking works in your cluster and how to configure security hardening of your application]({{< relref "/getting-started/understand-connectivity" >}}).
