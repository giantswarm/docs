---
linkTitle: Managing workload clusters with GitOps
title: Managing workload clusters with GitOps
description: An explanation of the GitOps principles and a guide to managing Giant Swarm platform resources with FluxCD.
weight: 50
menu:
  main:
    parent: advanced
user_questions:
  - What is GitOps?
  - What is FluxCD?
  - How to manage resources with GitOps?
  - How to prepare repositories for use with FluxCD?
  - How to ensure security by combining FluxCD with the Management API permission model?
aliases:
  - /advanced/fluxcd/
  - /advanced/gitops/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2022-07-11
---

In this document you will learn how to manage infrastructure and applications by utilizing FluxCD - a set of GitOps operators installed in Giant Swarm management clusters.

## What is GitOps

The GitOps Working Group [defines GitOps as a set of principles](https://github.com/open-gitops/documents/blob/release-v1.0.0/PRINCIPLES.md):
> GitOps is a set of principles for operating and managing software systems. These principles are derived from modern software operations, but are also rooted in pre-existing and widely adopted best practices.
> The desired state of a GitOps managed system must be:
> **Declarative**
> A system managed by GitOps must have its desired state expressed declaratively.
> **Versioned and Immutable**
> The desired state is stored in a way that enforces immutability, versioning and retains a complete version history.
> **Pulled Automatically**
> Software agents automatically pull the desired state declarations from the source.
> **Continuously Reconciled**
> Software agents continuously observe the actual system state and attempt to apply the desired state.

The way these principles manifest in popular tools, such as FluxCD or ArgoCD can be summarized as follows:

The cluster's desired state, or manifest, is kept in Git repositories (or Helm repositories, S3 buckets, and so on). GitOps operators are deployed to clusters and configured to watch the manifest. The operators are tasked with periodically comparing the desired and actual states of the cluster's resources and reconciling them in case discrepancies are found.

If the cluster's state changes in a way that is not reflected in the code, the change will be reverted. If the code is updated with a new configuration and/or resources, the cluster will be instantly updated to match the desired state.

This way of managing Kubernetes comes with all the benefits and best practices of a versioning system: code reviews, pull requests, versioned releases, test branches, commit history, and full accountability. Due to the almost instant deployment of committed changes, it is also a perfect tool for development and testing.

## What is FluxCD

The [FluxCD](https://fluxcd.io) website states:
> Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.

What it is from a developer perspective is a set of operators and Custom Resources designed to apply GitOps in a Kubernetes environment. The operators, configured with the Custom Resources, will be watching Git repositories, Helm repositories, or even S3 buckets and reconciling their contents with the state of the cluster to make sure they both match.

To get started with FluxCD, you will need to bootstrap FluxCD to your cluster of choice and create at least one of each of the following:

1. `source.toolkit.fluxcd.io` resources - they tell the `source-controller` where to look for the manifests
2. `helmrelease.helm.toolkit.fluxcd.io` or `kustomization.kustomize.toolkit.fluxcd.io` resources - they are meant for `helm-controller` and `kustomize-controller` respectively and govern how the manifests found in sources will be applied

Luckily, FluxCD is bootstrapped and running in Giant Swarm management clusters, so you can start using it immediately.

If want to learn more about FluxCD and its capabilities, here are a couple of useful links:

- [FluxCD documentation homepage](https://fluxcd.io/docs/)
- [Get Started with Flux](https://fluxcd.io/docs/get-started/) is a great way to get familiar with Flux on a test cluster or even a [Kind](https://kind.sigs.k8s.io/) cluster
- [GitOps Toolkit components](https://fluxcd.io/docs/components/) is where you can browse Flux Custom Resources and their use cases.

## Managing resources with Flux

In this section, we will guide you through an example Flux setup on a Giant Swarm Management Cluster. You will create resources locally. Mentions of _example resources_ or _example repository_ refers to [giantswarm/flux-demo](https://github.com/giantswarm/flux-demo), where you can find all resources used in this section in full, unabbreviated forms and Flux will use these to sync with.

In order to follow the [Watching for new commits](#watching-for-new-commits) section, you should fork the repository and work on your fork instead.

We will be using [Flux CLI](https://fluxcd.io/docs/cmd/) and [kubectl-gs](https://github.com/giantswarm/kubectl-gs). Please make sure you have both installed on your machine. If you would rather follow the guide without them, use the example resources provided.

## Restrictions in the web UI {#web-ui-restrictions}

The [Giant Swarm web UI]({{<relref "/ui-api/web">}}) allows editing and deleting resources like clusters and apps in an interactive way. However, for resources managed through GitOps, these capabilities are restricted. Otherwise changes and even deletions would get reverted through FluxCD.

The UI will indicate this by showing something like this:

<img src="managed-through-gitops.png" alt="" width="339" height="47" />

The restrictions in particular are:

- **Organizations** managed by FluxCD cannot be deleted via the web UI.

- **Clusters** managed by FluxCD cannot be edited, upgraded, or deleted via the web UI.

- **Node pools** managed by FluxCD cannot be edited or deleted via the web UI.

- **Apps** managed by FluxCD cannot be edited or uninstalled via the web UI.

As a signal that a resource is managed through FluxCD, the web UI relies on the existence of these two resource labels:

- `kustomize.toolkit.fluxcd.io/name`
- `kustomize.toolkit.fluxcd.io/namespace`

## Access control for organizations

To proceed with this tutorial, you need to use a ServiceAccount with a set of permissions that allows you to create and reconcile Flux resources. All the examples are using `default` namespace and `automation` ServiceAccount in that namespace. You will find them in every Management Cluster and they are already assigned with the required privileges.

If you wish to proceed by creating the resources in one of the Organization namespaces (`org-*`), you will need to create a ServiceAccount there and assign the following roles to it:

- `read-all-customer`
- `write-client-certificates-customer`
- `write-flux-resources-customer`
- `write-nodepools-customer`
- `write-organizations-customer`
- `write-silences-customer`

To learn how to view and assign roles, please refer to [Access control for organizations in the web user interface]({{< relref "/ui-api/web/organizations/access-control/index.md" >}}).

## GiantSwarm Management Cluster security policies

If you are creating any of the resources we talk about in this document on a GiantSwarm Management Cluster, you may see the following error:

```nohighlight
resource Kustomization... was blocked due to the following policies

flux-multi-tenancy:
  serviceAccountName: 'validation error: .spec.serviceAccountName is required. Rule
    serviceAccountName failed at path /spec/serviceAccountName/'
  sourceRefNamespace: preconditions not met
```

Due to extra security policies enforced by Kyverno, setting `.spec.serviceAccountName` for `Kustomization`/`HelmRelease` resources in our Management Clusters is mandatory. Usually, you will want to use `serviceAccountName: "automation"`.

### Setting up sources

First thing's first - create a bare-bones `GitRepository` resource that points to [giantswarm/flux-demo](https://github.com/giantswarm/flux-demo).

```nohighlight
flux create source git flux-demo \
        --url=https://github.com/giantswarm/flux-demo \
        --branch=main \
        --interval=30s \
        --namespace=default \
        --export > 01-source.yaml
```

This command creates the Custom Resource for you and exports it to `01-source.yaml`. You can also use the `01-source.yaml` file from the example repository - they are identical. All resources generated in this document are stored there as well.

Time to apply the generated YAML:

```nohighlight
kubectl create -f 01-source.yaml
```

You can see if the change was applied using `kubectl`:

```nohiglight
kubectl get gitrepositories -n default flux-demo
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f   27s

```

or Flux CLI - `flux`:

```nohighlight
 flux get sources git flux-demo
NAME            READY   MESSAGE                                                         REVISION                                        SUSPENDED
flux-demo       True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f main/74f8d19cc2ac9bee6f45660236344a054c63b71f   False
```

### Managing organizations

The first Giant Swarm custom resource you can create is an [Organization]({{< relref "/ui-api/management-api/crd/organizations.security.giantswarm.io.md" >}}). We will use `Kustomization` resource to tell Flux where to find YAML files defining resources and where to install them.

File structure

```nohighlight
.
├── 02-organization.yaml    # contains Kustomization CR
├── 02-organization
│   ├── kustomization.yaml  # kustomize manifest
│   └── resources.yaml      # contains Organization CR
```

First, let's create the kustomize directory:

```nohighlight
mkdir 02-organization
```

```nohighlight
echo -e 'resources:\n- resources.yaml' > 02-organization/kustomization.yaml
```

```nohighlight
kubectl gs template organization --name flux-demo > 02-organization/resources.yaml
```

> Note: To learn more about Giant Swarm's kubectl plugin, visit [kubectl-gs documentation]({{< relref "/ui-api/kubectl-gs/" >}}).

This is enough to create the Organization on our own. Let's add a `Kustomization` CR, so that Flux knows how to work with `02-organization/` directory.

```nohighlight
flux create kustomization install-organization \
        --source=GitRepository/flux-demo.default \
        --service-account=automation \
        --path="./02-organization" \
        --prune=true  \
        --interval=30s \
        --export > 02-organization.yaml
```

For Flux to manage this piece of code, you need to create the `Kustomization` resource. The contents of `02-organization` will be reconciled automatically.

```nohighlight
kubectl create -f 02-organization.yaml
kustomization.kustomize.toolkit.fluxcd.io/install-organization created

kubectl get kustomizations -n default install-organization
NAME                   READY   STATUS                                                            AGE
install-organization   True    Applied revision: main/17c3d4eac3ffde575c0a799c2bd67bf025389289   61s

flux get kustomizations
NAME                    READY   MESSAGE                                                         REVISION                                        SUSPENDED
install-organization    True    Applied revision: main/17c3d4eac3ffde575c0a799c2bd67bf025389289 main/17c3d4eac3ffde575c0a799c2bd67bf025389289   False
```

Let's see if the Organization and the namespace that comes with it are present:

```nohighlight
kubectl get organizations flux-demo
NAME        AGE
flux-demo   2m25s

kubectl get namespaces org-flux-demo
NAME            STATUS   AGE
org-flux-demo   Active   2m29s
```

Now, if you add any more Organization CRs to `02-organization/resources.yaml` (or change anything else in that kustomization), it will be picked up by Flux automatically once it's committed and pushed. This is covered in the [Watching for new commits](#watching-for-new-commits) section.

### Managing workload clusters

Let's try managing clusters. Pick a directory which matches your cloud platform provider: AWS or Azure. The file structure will stay exactly the same. This tutorial will use the AWS examples.

As in the previous example, we will create a single Flux resource, namely a `HelmRelease`. This resource will contain configuration telling Flux to reconcile a path in the demo repository (`flux-demo/03-cluster-aws`) as a Helm release.

File structure

```nohighlight
.
├── 03-cluster-aws.yaml     # contains HelmRelease CR
├── 03-cluster-aws          # Helm release directory
│   ├── Chart.yaml          # Helm chart definition
│   ├── templates
│   │   └── resources.yaml  # contains Giant Swarm cluster CRs
│   └── values.yaml         # Helm chart values
```

```nohighlight
mkdir -p 03-cluster-aws/templates
```

```nohighlight
kubectl gs template cluster --provider aws --name demo0 --organization flux-demo --description flux-demo > 03-cluster-aws/templates/cluster-resources.yaml
```

> Note: There are some parameterization and hooks already added in the demo repository. You can copy from there if you don't want to create your own.
> Otherwise please:
>
> - parameterize common variables and put them in `values.yaml`: cluster ID, organization name, namespace, control plane ID, etc.
> - add hook annotations to `Cluster` CR: `helm.sh/hook: pre-install` and `helm.sh/hook-weight: "-1"`

The cluster will still need a NodePool to reach full functionality. To learn more, visit [NodePool documentation]({{< relref "/advanced/node-pools/index.md" >}}). We will be creating one using `kubectl gs template` command.

```nohighlight
kubectl gs template nodepool \
        --provider aws \
        --cluster-name demo0 \
        --description demo0 \
        --organization flux-demo \
        --availability-zones eu-west-1a > 03-cluster-aws/templates/nodepool-resources.yaml
```

Please note that `kubectl gs template nodepool` requires you to specify availability zones by name and they may vary depending on your region.

Add `Chart.yaml` and `values.yaml` from the example repository or create your own.

```nohighlight
curl -s https://raw.githubusercontent.com/giantswarm/flux-demo/main/03-cluster-aws/Chart.yaml > 03-cluster-aws/Chart.yaml
```

```nohighlight
curl -s https://raw.githubusercontent.com/giantswarm/flux-demo/main/03-cluster-aws/values.yaml > 03-cluster-aws/values.yaml
```

```nohighlight
flux create helmrelease install-cluster-aws-chart \
        --source=GitRepository/flux-demo.default \
        --service-account=automation \
        --chart="./03-cluster-aws" \
        --interval=15s \
        --export > 03-cluster-aws.yaml
```

Let's install the `HelmRelease` resource and watch the cluster come up.

```nohighlight
kubectl get gitrepository -n default flux-demo
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/192bb1a25ea0504fe1ee5cafda128f79a00bce40   2m37s

kubectl get kustomizations -n default install-organization
NAME                   READY   STATUS                                                            AGE
install-organization   True    Applied revision: main/192bb1a25ea0504fe1ee5cafda128f79a00bce40   11s

kubectl create -f 03-cluster-aws.yaml
helmrelease.helm.toolkit.fluxcd.io/install-cluster-aws-chart created

kubectl get helmreleases -n default
NAME                        READY     STATUS                       AGE
install-cluster-aws-chart   Unknown   Reconciliation in progress   2s

kubectl get helmreleases -n default install-cluster-aws-chart
NAME                        READY   STATUS                             AGE
install-cluster-aws-chart   True    Release reconciliation succeeded   9s

kubectl get clusters.cluster.x-k8s.io -n org-flux-demo demo0
NAME    PHASE
demo0
```

### Installing managed apps

It is just as easy to install managed apps in existing workload clusters. In this part of the guide we will assume you have completed the previous steps and have both an organization and a cluster running.

File structure

```nohighlight
.
├── 04-managed-app.yaml     # contains Kustomization CR
├── 04-managed-app
│   ├── kustomization.yaml
│   └── resources.yaml      # contains Giant Swarm App CR
```

```nohighlight
mkdir 04-managed-app
```

```nohighlight
echo -e 'resources:\n- resources.yaml' > 04-managed-app/kustomization.yaml
```

```nohighlight
kubectl gs template app \
        --cluster "demo0" \
        --catalog giantswarm \
        --name nginx-ingress-controller-app \
        --namespace default \
        --version 2.4.0 > 04-managed-app/resources.yaml
```

```nohighlight
flux create kustomization install-managed-app \
        --source=GitRepository/flux-demo.default \
        --service-account=automation \
        --path="./04-managed-app" \
        --prune=true  \
        --interval=30s \
        --export > 04-managed-app.yaml
```

Install the `Kustomization`:

```nohighlight
kubectl create -f 04-managed-app.yaml
kustomization.kustomize.toolkit.fluxcd.io/install-managed-app created

kubectl get kustomizations -n default install-organization
NAME                  READY   STATUS                                                            AGE
install-managed-app   True    Applied revision: main/070c352f4949ecaad0d43e31744adf7e864cc754   23s

kubectl get apps -n demo0 nginx-ingress-controller-app
NAME                                VERSION      LAST DEPLOYED   STATUS
nginx-ingress-controller-app        2.4.0        31s             deployed
```

Now the managed application will be installed in your workload cluster. To learn more about how to utilize and configure Managed Apps, please refer to [the documentation]({{< relref "/app-platform/overview">}}).

### Watching for new commits

If you have forked the repository, you can test if Flux is watching it for new commits. We are assuming you have completed at least the [Managing organizations](#managing-organizations) section.

Let's create a new Organization CR and add it to `02-organization/resources.yaml`

```nohighlight
echo '---' >> 02-organization/resources.yaml && \
    kubectl gs template organization --name new-commit >> 02-organization/resources.yaml
```

Create a commit and push it to your repository's origin.

```nohighlight
git add . && \
    git commit -m 'add new organization "new-commit"' && \
    git push
```

Flux will pick it up after the interval you  set up in `Kustomization` and you should see the following result:

```nohighlight
kubectl get organizations
NAME        AGE
flux-demo   3h
new-commit  17s
...
```

### Test or development branches

Flux enables developers to deploy work-in-progress code in many ways. One of the most useful ways is deploying code from development branches. To do that, we will create a new `GitRepository` resource. It will be pointing to `development` branch of demo repository, instead of `main` branch. Then we will patch the `Kustomization` created in [Managing organizations](#managing-organizations) section so that it uses the new source instead.

The `development` branch contains an extra Organization in `02-organization/resources.yaml`, which will be instantly created.

File structure

```nohighlight
.
├── 05-development
│   ├── organization-patch.yaml
│   └── source.yaml
```

Note the differences:

```diff
--- a/02-organization.yaml
+++ b/05-development/organization-patch.yaml
@@ -9,5 +9,5 @@ spec:
   prune: true
   sourceRef:
     kind: GitRepository
-    name: flux-demo
+    name: flux-demo-development
   validation: client
```

```diff
--- a/01-source.yaml
+++ b/05-development/source.yaml
@@ -1,13 +1,11 @@
 apiVersion: source.toolkit.fluxcd.io/v1beta1
 kind: GitRepository
 metadata:
-  name: flux-demo
+  name: flux-demo-development
   namespace: default
 spec:
   interval: 30s
   ref:
-    branch: main
+    branch: development
   url: https://github.com/giantswarm/flux-demo
   timeout: 30s
```

After applying the changes, `install-organization` `Kustomization` will switch to watching the `development` branch and create the new organization found there:

```nohighlight
kubectl apply -R -f 05-development
```

```nohighlight
kubectl get organizations flux-demo
NAME        AGE
flux-demo   74s

kubectl get organizations flux-demo-development
Error from server (NotFound): organizations.security.giantswarm.io "flux-demo-dev" not found


kubectl apply -R -f 05-development/
kustomization.kustomize.toolkit.fluxcd.io/install-organization configured
gitrepository.source.toolkit.fluxcd.io/flux-demo-development created

kubectl get organizations flux-demo
NAME        AGE
flux-demo   104s

kubectl get organizations flux-demo-dev
NAME            AGE
flux-demo-dev   20s
```

This completes the guide. If you no longer need them you can delete the organization and cluster.
