---
linkTitle: add organization
title: "'kubectl gs gitops add organization' command reference"
description: Reference documentation on how to add a new organization to a GitOps repository.
weight: 20
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2024-01-18
aliases:
  - /use-the-api/kubectl-gs/gitops
  - /reference/kubectl-gs/gitops/add-org
  - /ui-api/kubectl-gs/gitops/add-org
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I add an organization to a GitOps repository?
---

This command adds a new Organization to the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/init" >}}))
- Management cluster (see [`add management-cluster`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-mc" >}}))

## Description

The structure created by this command is presented below. Note, the initial layers are flattened for brevity.

```nohighlight
management-clusters/MC_NAME/organizations
└── ORG_NAME
    ├── ORG_NAME.yaml
    └── workload-clusters
        └── kustomization.yaml
```

## Usage

Basic command syntax: `kubectl gs gitops add organization FLAGS`.

### Flags

- `--management-cluster` -- management cluster the organization belongs to (required)
- `--name` -- organization name (required)

{{% kubectl_gs_gitops_common_flags %}}

### Examples

```nohighlight
kubectl gs gitops add organization \
  --local-path /tmp/gitops-demo \
  --name demoorg \
  --management-cluster demomc \
  --dry-run
```

Output:

```nohighlight
## CREATE##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/demoorg.yaml
apiVersion: security.giantswarm.io/v1alpha1
kind: Organization
metadata:
  name: demoorg
spec: {}

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources: []
```

Remove the `--dry-run` flag and re-run it to apply the changes.
