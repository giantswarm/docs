---
linkTitle: get appcatalogs
title: "'kubectl gs get appcatalogs' command reference"
description: Reference documentation for 'kubectl gs get appcatalogs' which is replaced by 'kubectl gs get catalogs'.
weight: 110
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/get-appcatalogs/
last_review_date: 2021-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - Why is kubectl gs get appcatalogs no longer used?
  - What is the replacement for kubectl gs get appcatalogs?
---

# `kubectl gs get appcatalogs`

This command is replaced by  [`kubectl gs get catalogs`]({{< relref "/ui-api/kubectl-gs/get-catalogs" >}}).

The Catalog CRD is namespace scoped and replaces the [AppCatalog]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}})
CRD which is cluster scoped. This is to improve multi-tenancy support when used with the [Management API]({{< relref "/ui-api/management-api/overview/index.md" >}}).
