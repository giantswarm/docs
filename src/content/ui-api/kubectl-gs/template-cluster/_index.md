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

Usage depends on the provider, set via the `--provider` flag. Please refer to the provider-specific pages for more details.

| Provider | `--provider` flag value |
|-|-|
| [AWS]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `aws` |
| [Azure]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `azure` |
| [Cluster API provider AWS]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `capa` |
| [Cluster API provider Azure]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `azure` |
| [Cluster API provider GCP]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `gcp` |
| [Cluster API provider OpenStack]({{< relref "/ui-api/kubectl-gs/template-cluster/aws" >}}) | `capo` |

## Usage

The command to execute is `kubectl gs template cluster`.

It supports the following flags:

- `--provider` - The infrastructure provider (one of: `aws`, `azure`, or `openstack`).
- `--name` - Unique name of the cluster. If not provided, a random alphanumeric name will be generated.
- `--organization` - Name of the organization that will own the cluster. Determines the namespace where resources will be created.
- `--release` (AWS and Azure only) - Workload cluster release version.
  Can be retrieved with `kubectl get releases` for your installation.
- `--description` (optional) - User-friendly description of the cluster's purpose.
- `--pods-cidr` (optional) - CIDR applied to the pods. If this isn't provided, the installation default will be applied.
- `--label` (optional) - workload cluster label in the form of `key=value`. Can be specified multiple times.
- `--service-priority` (optional) - [Service priority]({{< relref "/advanced/labelling-workload-clusters#service-priority" >}}) of the cluster (one of: `highest`, `medium`, or `lowest`; default: `highest`).
- `--release-branch` (optional, AWS and Azure only) - The Giant Swarm [releases repository](https://github.com/giantswarm/releases) branch to use to look up the workload cluster release set via the `--release` flag (default: `master`).
- `--control-plane-az` (optional) - Availability zone(s) of the control plane instance(s).
- `--output` (optional) - The name of the file to write the output to instead of stdout.

  On AWS, it must be configured with AZ of the installation region. E.g. for region `eu-central-1`, a valid value is `eu-central-1a`.

  On Azure, it can be any of the 3 zones: `1`, `2`, `3`.

  Use the flag once with a single value to create a cluster with one control plane node (on both Azure and AWS). For high-availability control planes,
  specify three distinct availability zones instead (AWS only). This can be done by separating AZ names with comma or using the flag
  three times with a single AZ name.

