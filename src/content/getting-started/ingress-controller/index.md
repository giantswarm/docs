---
title: Installing an ingress controller
description: How to install the NGINX ingress controller using the Giant Swarm web user interface.
weight: 50
menu:
  main:
    parent: getting-started
user_questions:
- Which workload clusters do not ship with a pre-installed ingress controller?
- How do I install my own ingress controller?
- Which ingress controller is available for installation via Giant Swarm app catalog?
owner:
  - https://github.com/orgs/giantswarm/teams/team-halo
---

# Installing an ingress controller

An ingress controller helps you expose your services to the outside world.

## Which workload cluster releases do not ship with an ingress controller

Clusters on our AWS, Azure, and KVM (On-premises) installations that have a workload cluster release version newer than `10.0.0` (AWS), `12.0.0` (Azure), and `12.2.0` (KVM) ship without an ingress controller by default. (Related: [Preinstalled and optional apps in workload clusters]({{< relref "/general/releases/index.md#apps" >}}))

That allows you full control to choose which and how many ingress controllers you
want to run on your cluster.

## How do I Install my own ingress controller

Using our Web UI you can install an NGINX ingress controller using our App Catalog.

1. Click "Install App" from the "Apps" tab when viewing your cluster
  ![Cluster detail screen showing install app button](cluster-detail.png)

2. Click "Browse Apps" from the "Giant Swarm Catalog"
  ![List of app catalogs including the Giant Swarm Catalog](catalog-list.png)

3. Click "nginx-ingress-controller-app" from the list of apps.
  ![List of apps in the Giant Swarm Catalog](app-list.png)

4. Click "Configure & Install"

5. Click "Install App" (In case you want any special configuration, this is where you can also provide a 'values.yaml' with your customized settings)
  ![App installation modal](install-app-modal.png)

After a few moments, the NGINX ingress controller should be running on your cluster.
