---
linkTitle: Creating an app catalog
title: Creating an app catalog
description: How to create a custom app catalog for use with app platform and push helm charts to it.
weight: 40
menu:
  main:
    parent: getting-started-app-platform
    identifier: getting-started-app-platform-app-catalog
last_review_date: 2023-10-17
aliases:
  - /app-platform/create-catalog
  - /developer-platform/app-platform/create-catalog
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I install an app from a community Helm repository?
  - How can I create an app catalog for my apps?
  - How can I serve an app catalog using GitHub Pages?
  - How can I publish an app to my app catalog?
  - How can I register an app catalog with app platform?
  - How can I hide or show an app catalog in the web UI?
  - How can I install an apps from an app catalog?
  - How can I inspect the apps in an app catalog?
---

## Overview

An app catalog is a collection of apps that can be deployed using the Giant Swarm App Platform.
We extend Helm and an app catalog is also a Helm [chart repository](https://helm.sh/docs/topics/chart_repository/).
Each app catalog has its own [`Catalog`]({{< relref "/use-the-api/management-api/crd/catalogs.application.giantswarm.io.md" >}})
CR in the management cluster.

The app catalog is a Git repository that contains

- a Helm repository index (`index.yaml`),
- chart tarballs for each version of the app that has been published.

These files must be served over HTTP(S).

You can register community Helm chart repositories with app platform or create
your own app catalog.

You can search for Helm charts from the community using [Artifact Hub](https://artifacthub.io/).
Not all community chart repositories are currently supported. If you encounter a
problem installing an app please let us know. If you're registering a community
catalog you can skip to the section `Register the catalog`.

When creating your own app catalog we recommend using our [app-build-suite](https://github.com/giantswarm/app-build-suite/)
tool to publish apps to your catalog. It adds additional metadata files that
allows app platform to extend Helm. Such as only allowing an app to be
installed once in a cluster. You can learn more about the tool by reading its
[tutorial](https://github.com/giantswarm/app-build-suite/blob/master/docs/tutorial.md).

These metadata files and the Helm `index.yaml` are used to generate app metadata
that is stored in the management cluster in [App Catalog Entry]({{< relref "/use-the-api/management-api/crd/appcatalogentries.application.giantswarm.io.md" >}})
CRs.

There are [multiple options](https://helm.sh/docs/topics/chart_repository/#hosting-chart-repositories)
for serving the catalog over HTTP(S) including GitHub Pages or tools like Harbor or ChartMuseum which run in a
Kubernetes cluster. At Giant Swarm we use GitHub Pages and this is what we will
cover in this guide.

## Create an app catalog hosted using GitHub Pages

First, you should choose a name for your catalog Git repository. At Giant Swarm, we follow the convention to have the name end with the `-catalog` suffix, however any name will work.

Create the Git repository in GitHub as a public repository and enable
[GitHub Pages](https://docs.github.com/en/pages/quickstart) for the `main` branch.

## Publish an app to the app catalog

Now you can configure your apps to be published to your catalog. We have created
a GitHub [action](https://github.com/giantswarm/app-build-suite/blob/master/.github/workflows/push-to-app-catalog.yaml)
for `app-build-suite` that will automate this.

```yaml
# .github/workflows/push-to-app-catalog.yaml
name: 'Push to App Catalog'

on:
  push:
    tags:
      - 'v*'

jobs:
  push_to_app_catalog:
    uses: giantswarm/app-build-suite/.github/workflows/push-to-app-catalog.yaml@v1.2.1
    with:
      app_catalog: example-catalog
      chart: hello-world-app
      organization: example-org
    secrets:
      envPAT: ${{ secrets.PAT }}
```

To configure the action you need to add a secret called `PAT` to the app's Git
repository. This must contain a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
that has write permission to the app catalog git repository.

We recommend using [Dependabot](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/keeping-your-actions-up-to-date-with-dependabot)
to keep the GitHub action up to date.

## Register the catalog

To register the catalog with app platform you need to create a Catalog CR in the
management cluster. This can be done using [kubectl gs template catalog]({{< relref "/use-the-api/kubectl-gs/template-catalog" >}}).

For community catalogs the URL should match the URL used for the `helm repo add`
command and is the location of the Helm `index.yaml`.

When registering your own app catalog served using GitHub Pages the URL is the
same URL as the GitHub Pages website.

You should create the Catalog CR in the [organization]({{< relref "/platform-overview/multi-tenancy" >}})
namespace where the apps will be used. Or if it needs to be used in multiple
organizations it can be created in the `default` namespace.

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
  labels:
    application.giantswarm.io/catalog-visibility: public
spec:
  description: An example Catalog
  logoURL: https://example.com/logos/example-logo.png
  storage:
    URL: https://example.github.io/example-catalog/
    type: helm
  repositories:
  - URL: https://example.github.io/example-catalog/
    type: helm
  title: example
```

The `--visibility` flag is used to set the label `application.giantswarm.io/catalog-visibility`.
If its value is `public` it will appear in the web UI. If the label is missing or
has any other value it will be hidden in the web UI.

## Install an app from the catalog

If the Catalog CR is not in the `default` namespace you need to set the catalog
namespace to the organization namespace where it is stored. This can be done using
[kubectl gs template app]({{< relref "/use-the-api/kubectl-gs/template-app" >}}).

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

## Inspect the catalog

You can see the published apps for a catalog by listing its app catalog entry
CRs.

```nohighlight
kubectl get appcatalogentry -n org-example -l application.giantswarm.io/catalog=example
```

To avoid creating excessive load on the management cluster we only store the 5
most recent versions for each app according to [semantic versioning](https://semver.org/).
