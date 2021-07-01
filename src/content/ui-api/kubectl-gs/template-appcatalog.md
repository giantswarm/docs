---
linkTitle: template appcatalog
title: "'kubectl gs template appcatalog' command reference"
description: This command is replaced by 'kubectl gs template catalog'.
weight: 120
menu:
  main:
    parent: uiapi-kubectlgs
aliases:
  - /reference/kubectl-gs/template-appcatalog/
last_review_date: 2021-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-batman
user_questions:
  - Why is kubectl gs template appcatalogs no longer used?
  - What is the replacement for kubectl gs template appcatalogs?
---

# `kubectl gs template appcatalog`

This command is replaced by  [`kubectl gs template catalog`]({{< relref "/ui-api/kubectl-gs/template-catalog" >}}).

The Catalog CRD is namespace scoped and replaces the [AppCatalog]({{< relref "/ui-api/management-api/crd/appcatalogs.application.giantswarm.io.md" >}})
CRD which is cluster scoped. This is to improve multi-tenancy support when used with the [Management API]({{< relref "/ui-api/management-api/overview/index.md" >}}).
