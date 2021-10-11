---
linkTitle: Managing workload clusters with GitOps
title: Managing workload clusters with GitOps
description: An explanation of the GitOps principles and a guide to managing GiantSwarm platform resources with FluxCD.
weight: 50
menu:
  main:
    parent: advanced
user_questions:
  - What is GitOps?
  - What is FluxCD?
  - How to manage resources with GitOps?
  - How to prepare repositories for use with FluxCD?
  - How to ensure security by combining FluxCD with Management API permission model?
aliases:
  - /advanced/fluxcd/
  - /advanced/gitops/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2021-01-01
---

# Managing workload clusters with GitOps

TODO(kuba):

- Is `platform_support_table` applicable here? FluxCD is running on
all MCs, but we don't support managing clusters with it on KVM
- Mention how to integrate with MAPI by adopting `serviceAccount`
- How to use Flux with private repositories and/or Mozilla SOPS
- Node pools for cluster section
- Test Azure cluster creation

You can manage infrastructure and applications by utilizing FluxCD - a set of GitOps operators installed in Giant Swarm Management Clusters.

## What is GitOps

Put simply, GitOps is a way of managing infrastructure as code. It is a Continuous Delivery solution with the premise of code repositories being the ultimate sources of truth about Kubernetes clusters at its core.

Cluster's desired state, or manifest, is kept in Git repositories (or Helm repositories, S3 buckets, and so on). GitOps operators are deployed to clusters and configured to watch the manifest. The operators are tasked with periodically comparing the desired and actual states of the cluster's resources and reconciling them in case any discrepancies are found.

If the cluster's state changes in a way that is not reflected in the code, the change will be reverted. If the code is updated with a new configuration and/or resources, the cluster will be instantly updated to match the desired state.

This way of managing Kubernetes comes with all benefits and best practices of a versioning system: code reviews, pull requests, versioned releases, test branches, commit history, and full accountability. Due to the almost instant deployment of committed changes, it is also a perfect tool for development and testing.

## What is FluxCD

[FluxCD](https://fluxcd.io) website says:
> Flux is a set of continuous and progressive delivery solutions for Kubernetes that are open and extensible.

What it is from a developer perspective is a set of operators and Custom Resources designed to apply GitOps in Kubernetes environment. The operators, configured with the Custom Resources, will be watching Git repositories, Helm repositories, or even S3 buckets and reconciling their contents with the state of the cluster to make sure they both match.

To get started with FluxCD, you will need to bootstrap FluxCD to your cluster of choice and create at least one of each:

1. `source.toolkit.fluxcd.io` resources - they tell the `source-controller` whereto look for the manifests
2. `helmrelease.helm.toolkit.fluxcd.io` or `kustomization.kustomize.toolkit.fluxcd.io` resources - they are meant for `helm-controller` and `kustomize-controller` respectively and govern how the manifests found in sources will be applied

Luckily, FluxCD is bootstrapped and running in Giant Swarm Management Clusters, so you can start using it immediately.

If want to learn more about FluxCD and its capabilities, here are a couple of useful links:

- [FluxCD documentation homepage](https://fluxcd.io/docs/)
- [Get Started with Flux](https://fluxcd.io/docs/get-started/) is a great way to get familiar with Flux on a test cluster or even Kind cluster
- [GitOps Toolkit components](https://fluxcd.io/docs/components/) is where you can browse Flux Custom Resources and their use cases.

## Managing resources with Flux

In this section, we will guide you through an example Flux setup on Giant Swarm Management Cluster. Every mention of _example resources_ or _example repository_ refers to [giantswarm/flux-demo](https://github.com/giantswarm/flux-demo), where you can find all resources used in this section in full, unabbreviated forms.

We will be using [Flux CLI](https://fluxcd.io/docs/cmd/) and [kubectl-gs](https://github.com/giantswarm/kubectl-gs), but neither is strictly required to complete this guide.

### Setting up sources

First things first - create a bare-bones `GitRepository` resource that points to [giantswarm/flux-demo](https://github.com/giantswarm/flux-demo).

```yaml
# 01-source.yaml
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: GitRepository
metadata:
  name: flux-demo
  namespace: flux-system
spec:
  interval: 30s # How often Flux checks for repository updates (new commits)
  ref:
    branch: main
  url: https://github.com/giantswarm/flux-demo
```

This is very straightforward and does not do anything to the cluster's state just yet. You can see if the change was applied using `kubectl`:

```nohiglight
~ kubectl get gitrepositories -n flux-system flux-demo
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f   27s

```

or Flux CLI - `flux`:

```nohighlight
~  flux get sources git flux-demo
NAME            READY   MESSAGE                                                         REVISION                                        SUSPENDED
flux-demo       True    Fetched revision: main/74f8d19cc2ac9bee6f45660236344a054c63b71f main/74f8d19cc2ac9bee6f45660236344a054c63b71f   False
```

### Managing organizations

The first Giant Swarm resource you can create is an Organization. We will use `Kustomization` resource to tell Flux where to find YAML files defining resources and where to install them.

File structure

```nohighlight
.
├── 02-organization.yaml    # contains Kustomization CR
├── 02-organization
│   ├── kustomization.yaml  # kustomize manifest
│   └── resources.yaml      # contains Organization CR
```

```yaml
# 02-organization.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta1
kind: Kustomization
metadata:
  name: install-organization
  namespace: flux-system
spec:
  interval: 30s
  path: ./02-organization
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-demo
  validation: client
```

```yaml
# 02-organization/kustomization.yaml
resources:
- resources.yaml
```

```yaml
# 02-organization/resources.yaml
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  creationTimestamp: null
  name: flux-demo
spec: {}
status: {}
```

You can use `kubectl gs template organization --name flux-demo` to generate contents of `02-organization/resources.yaml` on your own.

For Flux to manage this piece of code, you just have to create the `Kustomization` resource. Contents of `02-organization` will be reconciled automatically.

```nohighlight
~ kubectl create -f 02-organization.yaml
kustomization.kustomize.toolkit.fluxcd.io/install-organization created
~ kubectl get kustomizations -n flux-system install-organization
NAME                   READY   STATUS                                                            AGE
install-organization   True    Applied revision: main/17c3d4eac3ffde575c0a799c2bd67bf025389289   61s
~ flux get kustomizations
NAME                    READY   MESSAGE                                                         REVISION                                        SUSPENDED
install-organization    True    Applied revision: main/17c3d4eac3ffde575c0a799c2bd67bf025389289 main/17c3d4eac3ffde575c0a799c2bd67bf025389289   False
```

Let's see if the Organization and the namespace that comes with it are present:

```nohighlight

~ kubectl get organizations flux-demo
NAME        AGE
flux-demo   2m25s
~ kubectl get namespaces org-flux-demo
NAME            STATUS   AGE
org-flux-demo   Active   2m29s
```

Now, if you add any more Organization CRs to `02-organization/resources.yaml` (or change anything else in that kustomization), it will be picked up by Flux automatically once it's committed and pushed. Of course, you can't do that with the demo repository, but you can try with your own, or take a look at [Test or development branches](#test-or-development-branches) section.

### Managing workload clusters

Let's try managing clusters. Pick a directory which matches your cloud platform provider: AWS or Azure. The file structure will stay exactly the same. This tutorial will follow with AWS examples.

As in previous example, we will create a single Flux resource, namely a `HelmRelease`. This resource will contain configuration telling Flux to reconcile a path in the demo repository (`flux-demo/03-cluster-aws`) as a Helm release.

File structure

```nohighlight
.
├── 03-cluster-aws.yaml     # contains HelmRelease CR
├── 03-cluster-aws          # Helm release directory
│   ├── Chart.yaml
│   ├── templates
│   │   └── resources.yaml  # contains Giant Swarm cluster CRs
│   └── values.yaml
```

You can use `kubectl gs template cluster --provider aws --name demo0 --organization flux-demo --description flux-demo` to generate contents of `03-cluster-aws/templates/resources.yaml` on your own.

```yaml
# 03-cluster-aws.yaml
apiVersion: helm.toolkit.fluxcd.io/v2beta1
kind: HelmRelease
metadata:
  name: install-cluster-aws-chart
  namespace: flux-system
spec:
  interval: 15s
  chart:
    spec:
      chart: "./03-cluster-aws"
      sourceRef:
        kind: GitRepository
        name: flux-demo
        namespace: flux-system
      interval: 15s
  upgrade:
    remediation:
      remediateLastFailure: true
  test:
    enable: true
```

```yaml
# 03-cluster-aws/Chart.yaml
apiVersion: v1
name: flux-demo-cluster
home: https://github.com/giantswarm/flux-demo
description: ""
version: v1.0.0
```

```yaml
# 03-cluster-aws/values.yaml
clusterid: demo0
organization: flux-demo
namespace: org-flux-demo
controlplaneid: tj0a6
description: flux-demo
```

```yaml
# 03-cluster-aws/templates/resources.yaml
apiVersion: cluster.x-k8s.io/v1alpha3
kind: Cluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/clusters.cluster.x-k8s.io/
    helm.sh/hook: pre-install
    helm.sh/hook-weight: "-1"
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: ""
    giantswarm.io/cluster: {{ .Values.clusterid }}
    giantswarm.io/organization: {{ .Values.organization }}
    release.giantswarm.io/version: ""
  name: {{ .Values.clusterid }}
  namespace: {{ .Values.namespace }}
spec:
  controlPlaneEndpoint:
    host: ""
    port: 0
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha3
    kind: AWSCluster
    name: {{ .Values.clusterid }}
    namespace: {{ .Values.namespace }}
status:
  controlPlaneInitialized: false
  infrastructureReady: false
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSCluster
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: ""
    cluster.x-k8s.io/cluster-name: {{ .Values.clusterid }}
    giantswarm.io/cluster: {{ .Values.clusterid }}
    giantswarm.io/organization: {{ .Values.organization }}
    release.giantswarm.io/version: ""
  name: {{ .Values.clusterid }}
  namespace: {{ .Values.namespace }}
spec:
  cluster:
    description: {{ .Values.description }}
    dns:
      domain: ""
    kubeProxy: {}
    oidc:
      claims: {}
  provider:
    credentialSecret:
      name: ""
      namespace: giantswarm
    master:
      availabilityZone: ""
      instanceType: ""
    nodes: {}
    pods:
      externalSNAT: false
    region: ""
status:
  cluster: {}
  provider:
    network: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: G8sControlPlane
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/g8scontrolplanes.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    cluster-operator.giantswarm.io/version: ""
    giantswarm.io/cluster: {{ .Values.clusterid }}
    giantswarm.io/control-plane: {{ .Values.controlplaneid }}
    giantswarm.io/organization: {{ .Values.organization }}
    release.giantswarm.io/version: ""
  name: {{ .Values.controlplaneid }}
  namespace: {{ .Values.namespace }}
spec:
  infrastructureRef:
    apiVersion: infrastructure.giantswarm.io/v1alpha3
    kind: AWSControlPlane
    name: {{ .Values.controlplaneid }}
    namespace: {{ .Values.namespace }}
status: {}
---
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSControlPlane
metadata:
  annotations:
    giantswarm.io/docs: https://docs.giantswarm.io/ui-api/management-api/crd/awscontrolplanes.infrastructure.giantswarm.io/
  creationTimestamp: null
  labels:
    aws-operator.giantswarm.io/version: ""
    giantswarm.io/cluster: {{ .Values.clusterid }}
    giantswarm.io/control-plane: {{ .Values.controlplaneid }}
    giantswarm.io/organization: {{ .Values.organization }}
    release.giantswarm.io/version: ""
  name: {{ .Values.controlplaneid }}
  namespace: {{ .Values.namespace }}
spec:
  instanceType: m5.xlarge
```

Let's install the `HelmRelease` resource and watch the cluster come up.

```nohighlight
~ kubectl get gitrepository -n flux-system flux-demo
NAME        URL                                       READY   STATUS                                                            AGE
flux-demo   https://github.com/giantswarm/flux-demo   True    Fetched revision: main/192bb1a25ea0504fe1ee5cafda128f79a00bce40   2m37s
~ kubectl get kustomizations -n flux-system install-organization
NAME                   READY   STATUS                                                            AGE
install-organization   True    Applied revision: main/192bb1a25ea0504fe1ee5cafda128f79a00bce40   11s
~ kubectl create -f 03-cluster-aws.yaml
helmrelease.helm.toolkit.fluxcd.io/install-cluster-aws-chart created
~ kubectl get helmreleases -n flux-system
NAME                        READY     STATUS                       AGE
install-cluster-aws-chart   Unknown   Reconciliation in progress   2s
~ kubectl get helmreleases -n flux-system install-cluster-aws-chart
NAME                        READY   STATUS                             AGE
install-cluster-aws-chart   True    Release reconciliation succeeded   9s
~ kubectl get clusters.cluster.x-k8s.io -n org-flux-demo demo0
NAME    PHASE
demo0
```

### Installing managed applications

It is just as easy to install managed applications in existing workload clusters. In this part of the guide we will assume you have completed previous steps and have both an organization and a cluster running.

File structure

```nohighlight
.
├── 04-managed-app.yaml     # contains Kustomization CR
├── 04-managed-app
│   ├── kustomization.yaml
│   └── resources.yaml      # contains Giant Swarm App CR
```

```yaml
# 04-managed-app.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta1
kind: Kustomization
metadata:
  name: install-managed-app
  namespace: flux-system
spec:
  interval: 30s
  path: ./04-managed-app
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-demo
  validation: client
```

```yaml
# 04-managed-app/kustomization.yaml
resources:
- resources.yaml
```

```yaml
# 04-managed-app/resources.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: flux-app
  namespace: demo0
spec:
  catalog: giantswarm
  kubeConfig:
    inCluster: false
  name: flux-app
  namespace: flux-system
  version: 0.4.0
```

You can create the App CR on your own using `kubectl gs template app --cluster demo0 --catalog giantswarm --name flux-app --namespace flux-system --version 0.4.0`.

Install the `Kustomization`:

```nohighlight
~ kubectl create -f 04-managed-app.yaml
kustomization.kustomize.toolkit.fluxcd.io/install-managed-app created
~ kubectl get apps -n demo0 flux-app
NAME                 VERSION      LAST DEPLOYED   STATUS
flux-app             4.0.0        31s             deployed
```

Now the managed application will be installed in your workload cluster.

### Test or development branches

Flux enables developers to deploy work-in-progress code in many ways, one of the most useful is deploying code from development branches. To do that, we will create a new `GitRepository` resource. It will be pointing to `development` branch of demo repository, instead of `main` branch. Then we will patch the `Kustomization` created in [Managing organizations](#managing-organizations) section so that it uses the new source instead.

The `development` branch contains an extra Organization in `02-organization/resources.yaml`, which will be instantly created. The same would have happened if we just pushed new commits to a source Flux is already watching - they would have been picked up immediately and reconciled against the cluster.

File structure

```nohighlight
.
├── 05-development
│   ├── organization-patch.yaml
│   └── source.yaml
```

```yaml
# 05-development/organization-patch.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta1
kind: Kustomization
metadata:
  name: install-organization
  namespace: flux-system
spec:
  interval: 30s
  path: ./02-organization
  prune: true
  sourceRef:
    kind: GitRepository
    name: flux-demo-development
  validation: client
```

```yaml
# 05-development/source.yaml
apiVersion: source.toolkit.fluxcd.io/v1beta1
kind: GitRepository
metadata:
  name: flux-demo-development
  namespace: flux-system
spec:
  interval: 30s
  ref:
    branch: development
  url: https://github.com/giantswarm/flux-demo
  timeout: 30s
```

Please, note the differences

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
   namespace: flux-system
 spec:
   interval: 30s
   ref:
-    branch: main
+    branch: development
   url: https://github.com/giantswarm/flux-demo
   timeout: 30s
```

After applying the changes, `install-organization` `Kustomization` will switch to watching `development` branch and create new organization found there:

```nohighlight
~ kubectl get organizations flux-demo
NAME        AGE
flux-demo   74s
~ kubectl get organizations flux-demo-development
Error from server (NotFound): organizations.security.giantswarm.io "flux-demo-dev" not found

~ kubectl apply -f 05-development/
kustomization.kustomize.toolkit.fluxcd.io/install-organization configured
gitrepository.source.toolkit.fluxcd.io/flux-demo-development created

~ kubectl get organizations flux-demo
NAME        AGE
flux-demo   104s
~ kubectl get organizations flux-demo-dev
NAME            AGE
flux-demo-dev   20s
```

