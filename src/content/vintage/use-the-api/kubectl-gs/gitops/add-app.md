---
linkTitle: add app
title: "'kubectl gs gitops add app' command reference"
description: Reference documentation on how to add a new App to the GitOps repository.
weight: 30
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2024-01-18
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I add App to my Workload Cluster with the GitOps repository?
aliases:
  - /reference/kubectl-gs/gitops/add-app
  - /ui-api/kubectl-gs/gitops/add-app
---

This command adds a new App to the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/init" >}}))
- Management cluster (see [`add management-cluster`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-mc" >}}))
- Organization (see [`add organization`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-org" >}}))
- Workload cluster (see [`add workload-cluster`]({{< relref "/vintage/use-the-api/kubectl-gs/gitops/add-wc" >}}))

## Description

The structure created by this command is presented below. Resources enclosed in a square brackets `[]` are considered optional.

```nohighlight
management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters/[mapi/]apps
├── kustomization.yaml
└── APP_NAME
    ├── [kustomization.yaml]
    ├── [appcr.yaml]
    ├── [configmap.yaml]
    ├── [patch_app_userconfig.yaml]
    └── [secret.enc.yaml]
```

Application can be added to the requested cluster either directly, resulting in the `appcr.yaml` file creation, or in-directly
from a base, resulting in the `kustomization.yaml` creation, which then references the base. Note however, in order to use in-direct method user must have a
working base to reference with the `--base` flag. In any case, user may provide configuration to the application with the
`--user-configmap` and the `--user-secret` flags.

## Usage

Basic command syntax: `kubectl gs gitops add app FLAGS`.

### Flags

- `--management-cluster` -- name of the management cluster the workload cluster belongs to (required)
- `--organization` -- name of the organization the workload cluster belongs to (required)
- `--workload-cluster` -- name of the workload cluster to configure the app for (required)
- `--app` -- app name in the catalog
- `--base` -- path to the base directory; must be relative to the repository root
- `--catalog` -- catalog to install the app from
- `--name` -- name of the app to use for creating the repository directory structure
- `--target-namespace` -- namespace to install app into
- `--skip-mapi` -- skip mapi directory when adding the app
- `--user-configmap` -- values YAML to customize the app with; will get inserted into a ConfigMap.
- `--user-secret` -- values YAML to customize the app with; will get inserted into a Secret.
- `--version` -- app version to install.

{{% kubectl_gs_gitops_common_flags %}}

### Examples

{{< tabs >}}
{{< tab id="no-base" title="Direct" >}}

```nohighlight
kubectl gs gitops add app \
  --local-path /tmp/gitops-demo \
  --management-cluster demomc \
  --organization demoorg \
  --workload-cluster demowc \
  --app hello-world \
  --catalog giantswarm \
  --version 0.3.0 \
  --target-namespace default \
  --name hello-world \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/appcr.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demowc-hello-world
spec:
  catalog: giantswarm
  name: hello-world
  namespace: default
  version: 0.3.0


## MODIFY ##
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
```

{{< /tab >}}
{{< tab id="no-base-config" title="Direct & Config" >}}

When needed, application can be given configuration passed with the `--user-configmap` and the `--user-secret` flags.
**Note, files referenced by these flags should carry a valid values YAML configuration conforming the values schema of the given
the app version.**

Below is the example of `values.yaml` configuring number of replicas and overriding the app's name.

```yaml
replicaCount: 5
fullnameOverride: "gitops-demo-app"
```

After saving this into `/tmp/values.yaml`, it can be referenced when adding an app.

```nohighlight
kubectl gs gitops add app \
  --local-path /tmp/gitops-demo \
  --management-cluster demomc \
  --organization demoorg \
  --workload-cluster demowc \
  --app hello-world \
  --catalog giantswarm \
  --version 0.3.0 \
  --target-namespace default \
  --name hello-world \
  --user-configmap /tmp/values.yaml \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/appcr.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: demowc-hello-world
spec:
  catalog: giantswarm
  name: hello-world
  namespace: default
  version: 0.3.0
  userConfig:
    configMap:
      name: demowc-hello-world-user-values
      namespace: org-demoorg

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/configmap.yaml
apiVersion: v1
data:
  values: |
    replicaCount: 5
    fullnameOverride: "gitops-demo-app"
kind: ConfigMap
metadata:
  name: demowc-hello-world-user-values
  namespace: org-demoorg


## MODIFY ##
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
- hello-world/configmap.yaml
```

{{< /tab >}}
{{< tab id="base" title="Indirect" >}}

In order to add app from a base the `--base` flag should be used instead of specifying all the apps parameters separately.

```nohighlight
kubectl gs gitops add app \
  --local-path /tmp/gitops-demo \
  --management-cluster demomc \
  --organization demoorg \
  --workload-cluster demowc \
  --base bases/apps/hello-world \
  --name hello-world \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
kind: Kustomization
resources:
  - ../../../../../../../../../bases/apps/hello-world


## MODIFY ##
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
- hello-world
```

{{< /tab >}}
{{< tab id="base-config" title="Indirect & Config" >}}

When adding app from a base, it can still be customized with user configuration. **Note, files referenced by these flags should
carry a valid values YAML configuration conforming the values schema of the given the app version.**

Below is the example of `values.yaml` configuring number of replicas and overriding the app's name.

```yaml
replicaCount: 5
fullnameOverride: "gitops-demo-app"
```

After saving this into `/tmp/values.yaml`, it can be referenced when adding an app.

```nohighlight
kubectl gs gitops add app \
  --local-path /tmp/gitops-demo \
  --management-cluster demomc \
  --organization demoorg \
  --workload-cluster demowc \
  --base bases/apps/hello-world \
  --name hello-world \
  --user-configmap /tmp/values.yaml \
  --dry-run
```

Output:

```nohighlight
## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/configmap.yaml
apiVersion: v1
data:
  values: |
    replicaCount: 5
    fullnameOverride: "gitops-demo-app"
kind: ConfigMap
metadata:
  name: demowc-hello-world-user-values
  namespace: org-demoorg

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
buildMetadata: [originAnnotations]
patchesStrategicMerge:
  - patch_app_userconfig.yaml
kind: Kustomization
resources:
  - ../../../../../../../../../bases/apps/hello-world
  - configmap.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/hello-world/patch_app_userconfig.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ${cluster_name}-hello-world
  namespace: org-${organization}
spec:
  userConfig:
    configMap:
      name: demowc-hello-world-user-values
      namespace: org-demoorg


## MODIFY ##
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
- hello-world
```

{{< /tab >}}
{{< /tabs >}}

Remove the `--dry-run` flag and re-run it to apply the changes.
