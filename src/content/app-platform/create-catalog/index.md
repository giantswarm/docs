---
linkTitle: Creating an app catalog
title: Creating an app catalog
description: How to create a custom app catalog for use with app platform
weight: 40
menu:
  main:
    parent: app-platform
last_review_date: 2021-12-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an app catalog for my apps?
  - How can I serve an app catalog using GitHub Pages?
  - How can I create a catalog CR for my app catalog?
  - How can I push an app to my app catalog?
---

# Creating an app catalog

## Overview

An app catalog is a collection of apps that can be deployed using the Giant Swarm App Platform.
We fully support Helm and an app catalog is also a Helm [Chart Repository](https://helm.sh/docs/topics/chart_repository/).
Each app catalog has its own [catalog]({{< relref "/ui-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
CR in the management cluster.

The app catalog contains a tarball for each version of an app that has been published.
As well as an index.yaml and other metadata files that are used to generate
metadata that is stored in the management cluster in [app catalog entry]({{< relref "/ui-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs.

The catalog needs to be served over HTTP and there are [multiple options](https://helm.sh/docs/topics/chart_repository/#hosting-chart-repositories)
including GitHub Pages or tools like Harbor or ChartMuseum which run in a
Kubernetes cluster. At Giant Swarm we use GitHub Pages and this is what we will
cover in this guide.

## Creating an app catalog using GitHub Pages

First you should choose a name for your catalog. We recommend using the suffix
`-catalog` to make it clear this repository hosts an app catalog.

Create the git repository in GitHub and enable [GitHub Pages](https://docs.github.com/en/pages/quickstart)
for the `main` branch.

Initialize the empty helm index.yaml with `helm repo index .` and commit it to
the repository.

## Pushing an app to an app catalog

TODO

I think we should recommend using ABS (app-build-suite) and this means the
extra metadata gets created.

But I have several questions / concerns.

- Should we link to the ABS [tutorial](https://github.com/giantswarm/app-build-suite/blob/master/docs/tutorial.md)?
- Or should we create another docs page and link them?
- ABS doesn't commit the files to the repo (which is intentional) but I think we need a solution for that.
- We could suggest architect-orb but that feels weird since its mainly internal and customer may not be using
Circle CI.
- Should we create a simple GitHub Action for this?

## Create catalog CR

Once you've created your app catalog you need to create a catalog CR in the
management cluster to register it with app platform. This can be done using
[kubectl gs template catalog]({{< relref "/ui-api/kubectl-gs/template-catalog" >}}).

You should create the catalog CR in the organization namespace where the apps
will be used.

```nohighlight
kubectl gs template catalog \
  --name example-catalog \
  --namespace org-example \
  --description "An example Catalog" \
  --url https://example.github.io/my-app-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: Catalog
metadata:
  name: example-catalog
  namespace: org-example
spec:
  description: An example Catalog
  logoURL: https://example.com/logos/example-logo.png
  storage:
    URL: https://example.github.io/my-app-catalog/
    type: helm
  title: example-catalog
```

## Referencing an app catalog in an app CR

When the catalog CR is not in the `default` namespace you need to set the catalog
namespace to the organization namespace where it is stored. This can be done using
[kubectl gs template app]({{< relref "/ui-api/kubectl-gs/template-app" >}}).

```nohighlight
kubectl gs template app \
  --catalog example-catalog \
  --catalog-namespace org-example \
  --name example-app \
  --namespace default \
  --cluster 2hr7z  \
  --version 0.1.0
```

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: example-app
  namespace: 2hr7z
spec:
  catalog: example-catalog
  catalogNamespace: org-example
  kubeConfig:
    inCluster: false
  name: example-app
  namespace: default
  version: 0.1.0
```
