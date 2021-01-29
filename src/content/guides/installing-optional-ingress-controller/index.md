---
title: Installing an Ingress Controller
description: How to install the nginx-ingress-controller using our Web UI
type: page
weight: 50
tags: ["tutorial"]
owner:
  - https://github.com/orgs/giantswarm/teams/team-halo
---

# Installing an Ingress Controller

An ingress controller helps you expose your services to the outside world.

## Which workload cluster releases do not ship with an ingress controller

Currently clusters on our AWS and Azure installations that have a workload cluster release version
newer than `10.0.0` (AWS) or `12.0.0` (Azure) ship without an ingress controller by default. That
allows you full control to choose which and how many ingress controllers you
want to run on your cluster.

Clusters on KVM (On-premises) continue to include `nginx-ingress-controller`
as a default component.

## How do I Install my own Ingress Controller

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
