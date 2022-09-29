---
linkTitle: add automatic-update
title: "'kubectl gs gitops add update' command reference"
description: Reference documentation on how to configure automatic updates for an App to the GitOps repository.
weight: 35
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2022-08-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I configure automatic updates for an App with the GitOps repository?
---

This command adds a new App to the GitOps repository.

Other command this commad depends on:
- [gitops init]({{< relref "/ui-api/kubectl-gs/gitops/init" >}})
- [gitops add mc]({{< relref "/ui-api/kubectl-gs/gitops/add-mc" >}})
- [gitops add org]({{< relref "/ui-api/kubectl-gs/gitops/add-org" >}})
- [gitops add wc]({{< relref "/ui-api/kubectl-gs/gitops/add-wc" >}})
- [gitops add app]({{< relref "/ui-api/kubectl-gs/gitops/add-app" >}})

## Description

The structure created by this command is presented below. Resources enclosed in square brackets `[]` are considered optional.

```nohighlight
management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/[mapi/]
├── automatic-updates
│   └── imageupdate.yaml
└── apps
    ├── kustomization.yaml
    └── APP_NAME
        ├── appcr.yaml
        ├── imagepolicy.yaml
        └── imagerepository.yaml

```

**Note, automatic update requires the `appcr.yaml` file and hence can only be configured for directly added apps**. For apps
coming from a base updates must be configured in the base instead, what is outside of the command's scope.

## Flags

| Name                 | Description                                                         | Required |
| -------------------- | ------------------------------------------------------------------- | -------- |
| `app`                |  App in the repository to configure automatic update for.           | true     |
| `management-cluster` | Codename of the Management Cluster the Workload Cluster belongs to. | true     |
| `organization`       | Name of the Organization the Workload Cluster belongs to.           | true     |
| `skip-mapi`          | Skip mapi directory when adding the app.                            | false    |
| `version-repository` | The OCR repository to update the version from.                      | true     |
| `workload-cluster`   | Name of the Workload Cluster to configure the app for.              | true     |

## Usage

The command to execute is the `kubectl gs gitops add update`.

To preview the objects to be created by the command, run it with the `--dry-run` flag. Find examples below.

{{< tabs >}}
{{< tab id="direct" title="Direct App" >}}

```nohighlight
kubectl gs gitops add update \
--local-path /tmp/gitops-demo \
--management-cluster demomc \
--organization demoorg \
--workload-cluster demowc \
--app hello-world \
--version-repository giantswarmpublic.azurecr.io/giantswarm-catalog/hello-world-app \
--repository gitops-demo \
--dry-run

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/automatic-updates
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/automatic-updates/imageupdate.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageUpdateAutomation
metadata:
  name: demomc-updates
  namespace: default
spec:
  git:
    checkout:
      ref:
        branch: main
    commit:
      author:
        email: fluxcdbot@users.noreply.github.com
        name: fluxcdbot
      messageTemplate: |
        automated app upgrades:
        {{ range $image, $_ := .Updated.Images -}}
        - {{ $image.Repository }} to {{ $image.Identifier }}
        {{ end -}}
    push:
      branch: main
  interval: 1m0s
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  update:
    path: ./management-clusters/demomc
    strategy: Setters

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/imagepolicy.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImagePolicy
metadata:
  name: demowc-hello-world
spec:
  imageRepositoryRef:
    name: demowc-hello-world
  policy:
    semver:
      range: '>=0.0.0'

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/imagerepository.yaml
apiVersion: image.toolkit.fluxcd.io/v1beta1
kind: ImageRepository
metadata:
  name: demowc-hello-world
spec:
  image: giantswarmpublic.azurecr.io/giantswarm-catalog/hello-world-app
  interval: 10m0s


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/appcr.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demowc-hello-world
spec:
  catalog: giantswarm
  name: hello-world
  namespace: default
  version: 0.3.0 # {"$imagepolicy": "org-demoorg:demowc-hello-world:tag"}

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/cluster: ${cluster_name}
  giantswarm.io/managed-by: flux
kind: Kustomization
namespace: org-${organization}
patches:
- path: patch_cluster_config.yaml
  target:
    kind: App
resources:
- hello-world/appcr.yaml
- hello-world/imagepolicy.yaml
- hello-world/imagerepository.yaml
```

{{< /tab >}}
{{< tab id="indirect" title="Indirect App" >}}

Upon trying to configure automatic updates for app coming from a base, the command will return an error.

```nohighlight
kubectl gs gitops add update \
--local-path /tmp/gitops-demo \
--management-cluster demomc \
--organization demoorg \
--workload-cluster demowc \
--app hello-world \
--version-repository giantswarmpublic.azurecr.io/giantswarm-catalog/hello-world-app \
--repository gitops-demo \
--dry-run

validation error: Operation cannot be fulfilled on directory missing the `appcr.yaml` file.
```

{{< /tab >}}
{{< /tabs >}}

Remove the `--dry-run` flag and re-run it to apply the changes.
