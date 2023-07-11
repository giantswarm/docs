---
title: Installing an ingress controller
description: How to install the Ingress NGINX Controller using the Giant Swarm web user interface.
weight: 70
menu:
  main:
    parent: getting-started
user_questions:
- Which workload clusters ship with a pre-installed ingress controller?
- How do I install my own ingress controller?
- Which ingress controller is available via the Giant Swarm app platform?
aliases:
  - /guides/installing-optional-ingress-controller/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2023-03-28
---

An ingress controller helps you expose your services to the outside world.

## How do I Install my own ingress controller

Using our Web UI you can install an Ingress NGINX Controller using our App Catalog.

1. Click "Install app" from the "Apps" tab when viewing your cluster
  ![Cluster detail screen showing install app button](cluster-detail.png)

2. Search for "ingress-nginx" in the list of apps
  ![List of app catalogs including the Giant Swarm Catalog](app-list.png)

3. Select "ingress-nginx" from the "Giant Swarm Catalog"
  ![List of apps in the Giant Swarm Catalog](app-search-result.png)

4. Click "Install in cluster"

5. Click "Install app" (In case you want any special configuration, this is where you can also provide a 'values.yaml' with your customized settings)
  ![App installation modal](install-app-modal.png)

After a few moments, the Ingress NGINX Controller should be running on your cluster.

More information about the Ingress NGINX Controller can be found in the [ingress-nginx-app](https://github.com/giantswarm/ingress-nginx-app) repository.

## Further reading

- [Accessing pods and services from the outside]({{< relref "/getting-started/exposing-workloads/index.md" >}})
- [Running multiple Ingress NGINX Controllers]({{< relref "/advanced/ingress/multi-nginx-ic/index.md" >}})
- [Advanced ingress configuration]({{< relref "/advanced/ingress/configuration/index.md" >}})
