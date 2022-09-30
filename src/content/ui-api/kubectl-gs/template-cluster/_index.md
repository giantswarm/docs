---
linkTitle: template cluster
title: "'kubectl gs template cluster' command reference"
description: Reference documentation on how to create a manifest for a Cluster using 'kubectl gs'.
weight: 90
layout: single
menu:
  main:
    parent: uiapi-kubectlgs
    identifier: uiapi-kubectlgs-templatecluster
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - How can I create a cluster manifest for the Management API?
last_review_date: 2022-09-29
---

The `template cluster` command creates manifests for all the resources required to create a workload cluster. Actual cluster creation happens after submitting the manifests to the management API, e. g. via `kubectl apply`.

## Providers

Usage depends on the provider, set via the `--provider` flag. Please refer to the following provider-specific instructions for more details.

| Provider | `--provider` flag value |
|-|-|
| [AWS]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `aws` |
| [Azure]({{< relref "/ui-api/kubectl-gs/template-cluster/azure" >}}) | `azure` |
| [Cluster API provider AWS]({{< relref "/ui-api/kubectl-gs/template-cluster/capa" >}}) | `capa` |
| [Cluster API provider Azure]({{< relref "/ui-api/kubectl-gs/template-cluster/capz" >}}) | `capz` |
| [Cluster API provider GCP]({{< relref "/ui-api/kubectl-gs/template-cluster/capg" >}}) | `capg` |
| [Cluster API provider OpenStack]({{< relref "/ui-api/kubectl-gs/template-cluster/capo" >}}) | `capo` |

On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes, specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag three times with a single AZ name.
