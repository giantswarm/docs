---
linkTitle: Creating an app catalog
title: Creating an app catalog
description: How to create a custom app catalog for use with app platform and push helm charts to it.
weight: 40
menu:
  main:
    parent: app-platform
last_review_date: 2022-01-25
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I create an app catalog for my apps?
  - How can I serve an app catalog using GitHub Pages?
  - How can I publish an app to my app catalog?
  - How can I create a catalog CR for my app catalog?
  - How can I create an app CR for an app in the catalog?
---

# Creating an app catalog

## Overview

An app catalog is a collection of apps that can be deployed using the Giant Swarm App Platform.
We extend Helm and an app catalog is also a Helm [Chart Repository](https://helm.sh/docs/topics/chart_repository/).
Each app catalog has its own [Catalog]({{< relref "/ui-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
CR in the management cluster.

The app catalog is a Git repository that contains a Helm `index.yaml` and chart
tarballs for each version of the app that has been published. These files must
be served over HTTP.

We recommend using our [app-build-suite](https://github.com/giantswarm/app-build-suite/)
tool to publish apps to your catalog. It adds additional metadata files that
allows app platform to extend Helm. Such as only allowing an app to be
installed once in a cluster. You can learn more about the tool by reading its
[tutorial](https://github.com/giantswarm/app-build-suite/blob/master/docs/tutorial.md).

These metadata files and the Helm `index.yaml` are used to generate app metadata
that is stored in the management cluster in [App Catalog Entry]({{< relref "/ui-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs.

There are [multiple options](https://helm.sh/docs/topics/chart_repository/#hosting-chart-repositories)
for serving the catalog over HTTP including GitHub Pages or tools like Harbor or ChartMuseum which run in a
Kubernetes cluster. At Giant Swarm we use GitHub Pages and this is what we will
cover in this guide.

## Creating an app catalog hosted using GitHub Pages

First, you should choose a name for your catalog. We recommend using the suffix
`-catalog` to make it clear this Git repository hosts an app catalog.

Create the Git repository in GitHub as a public repository and enable
[GitHub Pages](https://docs.github.com/en/pages/quickstart) for the `main` branch.

## Publishing an app to the app catalog

Now you can configure your apps to be published to your catalog. We have created
a GitHub Action for `app-build-suite` that will automate this.

```yaml
# .github/workflows/push-to-app-catalog.yaml
name: 'Push to App Catalog'

on:
  push:
    tags:
      - 'v*'

jobs:
  push_to_app_catalog:
    uses: giantswarm/app-build-suite/.github/workflows/push-to-app-catalog.yaml@master
    with:
      app_catalog: example-catalog
      chart: hello-world-app
      organization: rossf7
    secrets:
      envPAT: ${{ secrets.PAT }}
```

To configure the action you need to add a secret called `PAT` to the app's git
repository. This must contain a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
that has write permission to the app catalog git repository.

## Create Catalog CR

Once you've created your app catalog and published some apps you need to create
a Catalog CR in the management cluster to register it with app platform. This
can be done using [kubectl gs template catalog]({{< relref "/ui-api/kubectl-gs/template-catalog" >}}).

You should create the Catalog CR in the [organization]({{< relref "/general/organizations" >}})
namespace where the apps will be used.

```nohighlight
kubectl gs template catalog \
  --name example \
  --namespace org-example \
  --description "An example Catalog" \
  --url https://example.github.io/example-catalog/ \
  --logo https://example.com/logos/example-logo.png
```

```yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: Catalog
metadata:
  creationTimestamp: null
  name: example
  namespace: org-example
spec:
  description: An example Catalog
  logoURL: https://example.com/logos/example-logo.png
  storage:
    URL: https://example.github.io/example-catalog/
    type: helm
  title: example
```

## Referencing an app catalog in an App CR

Since the Catalog CR is not in the `default` namespace you need to set the catalog
namespace to the organization namespace where it is stored. This can be done using
[kubectl gs template app]({{< relref "/ui-api/kubectl-gs/template-app" >}}).

```nohighlight
kubectl gs template app \
  --catalog example \
  --catalog-namespace org-example \
  --name hello-world-app \
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
  catalog: example
  catalogNamespace: org-example
  kubeConfig:
    inCluster: false
  name: example-app
  namespace: default
  version: 0.1.0
```

## Viewing app metadata

You can see the published apps for a catalog by listing its app catalog entry
CRs.

```nohighlight
kubectl get appcatalogentry -n org-example -l application.giantswarm.io/catalog=example
```

To avoid creating excessive load on the management cluster we only store the 5
most recent versions for each app according to [semantic versioning](https://semver.org/).
