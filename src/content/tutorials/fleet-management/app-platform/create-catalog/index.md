---
linkTitle: Creating an app catalog
title: Creating an app catalog
description: How to create a custom app catalog for use with app platform and push helm charts to it.
weight: 50
aliases:
  - /getting-started/app-platform/create-catalog
  - /vintage/getting-started/app-platform/create-catalog
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-app-catalog
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I install an app from a community helm repository?
  - How can I create an app catalog for my apps?
  - How can I serve an app catalog using GitHub Pages?
  - How can I publish an app to my app catalog?
  - How can I register an app catalog with app platform?
  - How can I hide or show an app catalog in the web UI?
  - How can I install an apps from an app catalog?
  - How can I inspect the apps in an app catalog?
last_review_date: 2024-10-28
---

An app catalog is a collection of apps that can be deployed using the Giant Swarm app platform.
It's an extension of `helm` [chart repository](https://helm.sh/docs/topics/chart_repository/).

Every app catalog has its own [`Catalog`]({{< relref "/reference/platform-api/crd/catalogs.application.giantswarm.io.md" >}}) custom resource defined in the platform API.

The app catalog is a `Git` repository that contains:

- A `helm` repository index (`index.yaml`).
- A chart tarballs for every version of the app that has been published.

These files must be served over HTTP. You can register community `helm` chart repositories with app platform or create your own app catalog.

You can search for `helm` charts from the community using [Artifact Hub](https://artifacthub.io/). Not all community chart repositories are currently supported. If you encounter a problem installing an app please let us know. If you're registering a community catalog you can skip to the section [`Register the catalog`]({{< relref "#register-the-catalog" >}}).

When creating your own app catalog we recommend using our [app-build-suite](https://github.com/giantswarm/app-build-suite/) tool to publish apps to your catalog. It adds additional metadata files that
allows app platform to extend `helm`. Such as only allowing an app to be installed once in a cluster. You can learn more about the tool by reading its [tutorial](https://github.com/giantswarm/app-build-suite/blob/master/docs/tutorial.md).

These metadata files and the `helm` `index.yaml` are used to generate app metadata that's stored in the platform  as an [`AppCatalogEntry`]({{< relref "/reference/platform-api/crd/appcatalogentries.application.giantswarm.io.md" >}}) resource.

There are [multiple options](https://helm.sh/docs/topics/chart_repository/#hosting-chart-repositories) for serving the catalog over HTTP including GitHub pages or tools like `harbor` or `chartMuseum` which run in a `kubernetes` cluster. At Giant Swarm we use GitHub pages and this is what we will cover in this guide.

## Create an app catalog hosted using GitHub pages

First, you should choose a name for your catalog Git repository. At Giant Swarm, we follow the convention to have the name end with the `-catalog` suffix, however any name will work.

Create the `Git` repository in GitHub as a public repository and enable [GitHub Pages](https://docs.github.com/en/pages/quickstart) for the `main` branch.

## Publish an app to the app catalog

Now you can configure your apps to be published to your catalog. There is a GitHub [action](https://github.com/giantswarm/app-build-suite/blob/master/.github/workflows/push-to-app-catalog.yaml) for `app-build-suite` which automate the process.

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

To configure the action you need to add a secret called `PAT` to the app's `Git` repository. This must contain a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) that has write permission to the app catalog git repository.

The recommendation is to use [`dependabot`](https://docs.github.com/en/code-security/supply-chain-security/keeping-your-dependencies-updated-automatically/keeping-your-actions-up-to-date-with-dependabot) to keep the GitHub action up to date.

## Register the catalog {#register-the-catalog}

To register the catalog with app platform you need to create a `Catalog` resource in the platform. This can be done using [`kubectl gs template catalog`]({{< relref "/reference/kubectl-gs/template-catalog" >}}).

For community catalogs the address should match the address used for the `helm repo add` command and is the location of the `helm` `index.yaml`.

When registering your own app catalog served using GitHub Pages the address is the same address as the GitHub Pages website.

You should create the `Catalog` resource in the [organization]({{< relref "/overview/fleet-management/multi-tenancy/" >}}) namespace where the apps will be used. Or if it needs to be used in multiple organizations it can be created in the `default` namespace.

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
If its value is `public` it will appear in the [developer portal]({{< relref "/overview/developer-portal" >}}). Otherwise it will be hidden.

## Install an app from the catalog

If the `Catalog` resource isn't in the `default` namespace you need to set the catalog namespace to the organization namespace where it's stored. This can be done using [`kubectl gs template app`]({{< relref "/reference/kubectl-gs/template-app" >}}).

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

You can see the published apps for a catalog by listing its `AppCatalogEntry` resources.

```sh
kubectl get appcatalogentry -n org-example -l application.giantswarm.io/catalog=example
```

To avoid creating excessive load on the platform, only the latest five recent versions (according to [semantic versioning](https://semver.org/)) will be stored in the platform as entries.
