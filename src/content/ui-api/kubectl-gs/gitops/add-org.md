---
linkTitle: add organization
title: "'kubectl gs gitops add org' command reference"
description: Reference documentation on how to add a new Organization to the GitOps repository.
weight: 20
menu:
  main:
    parent: kubectlgs-gitops
aliases:
  - /reference/kubectl-gs/gitops/add-org/
last_review_date: 2022-08-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I configure Organization in the GitOps repository?
---

This command adds a new Organization to the GitOps repository.

Other command this commad depends on:
- [gitops init]({{< relref "/ui-api/kubectl-gs/gitops/init" >}})
- [gitops add mc]({{< relref "/ui-api/kubectl-gs/gitops/add-mc" >}})

## Description

The structure created by this command is presented below. Note, the initial layers are flattened for brevity.

```nohighlight
management-clusters/MC_NAME/organizations
└── ORG_NAME
    ├── ORG_NAME.yaml
    └── workload-clusters
        └── kustomization.yaml
```

## Flags

| Name              | Description                                        | Required |
| ----------------- | -------------------------------------------------- | -------- |
| `management-cluster` | Management Cluster the Organization belongs to. | true     |
| `name`            | Organization name.                                 | true     |

## Usage

The command to execute is the `kubectl gs gitops add org`.

To preview the objects to be created by the command, run it with the `--dry-run` flag. Example:

```nohighlight
kubectl gs gitops add org \
--local-path /tmp/gitops-demo \
--name demoorg \
--management-cluster demomc \
--dry-run

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
