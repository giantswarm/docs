---
linkTitle: add workload-cluster
title: "'kubectl gs gitops add wc' command reference"
description: Reference documentation on how to add a new Workload Cluster to the GitOps repository.
weight: 25
menu:
  main:
    parent: kubectlgs-gitops
last_review_date: 2022-08-31
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I configure Workload Cluster in the GitOps repository?
---

This command adds a new Workload Cluster to the GitOps repository.

Other command this commad depends on:
- [gitops init]({{< relref "/ui-api/kubectl-gs/gitops/init" >}})
- [gitops add mc]({{< relref "/ui-api/kubectl-gs/gitops/add-mc" >}})
- [gitops add org]({{< relref "/ui-api/kubectl-gs/gitops/add-org" >}})

## Description

The structure created by this command is presented below. Note, the initial layers are flattened for brevity. Resources enclosed
in a square brackets `[]` are considered optional.

```nohighlight
management-clusters/MC_NAME/secrets
└── WC_NAME.gpgkey.enc.yaml
management-clusters/MC_NAME/organizations/ORG_NAME/workload-clusters
├── kustomization.yaml
├── WC_NAME.yaml
└── WC_NAME
    └── [mapi]
        ├── apps
        │   ├── kustomization.yaml
        │   └── patch_cluster_config.yaml
        └── cluster
            ├── [kustomization.yaml]
            ├── [cluster_userconfig.yaml]
            ├── [patch_cluster_userconfig.yaml]
            ├── [default_apps_userconfig.yaml]
            └── [patch_default_apps_userconfig.yaml]
```

Content of the `cluster` directory is optional because in its most basic form the GitOps repository does not oblige user to
put the cluster definition in there, this can be added later by re-running the command with additional flags. Re-running works
in such case, because `cluster` directory is initially empty. Note however, in order to populate it user must have a
working base and reference it by the `--base` flag when running the command. User may customize the referenced base with
the `--cluster-user-config` and `--default-apps-user-config` flags when needed.

**Note**, the latest recommendation mandates creation of the `mapi` directory. However, users who have not yet migrated to it,
but still want to use automation for their repositories, may skip `mapi` layer by using the `--skip-mapi` flag. Migration is
nevertheless mandatory, and hence this flag is planned to be removed from `kubectl-gs` at some point.

## Flags

| Name                       | Description                                                             | Required |
| -------------------------- | ----------------------------------------------------------------------- | -------- |
| `base`                     | Path to the base directory. It must be relative to the repository root. | false    |
| `cluster-release`          | Cluster app version.                                                    | true     |
| `cluster-user-config`      | Cluster app user configuration to patch the base with.                  | false    |
| `default-apps-release`     | Default apps app version.                                               | true     |
| `default-apps-user-config` | Default apps app user configuration to patch the base with.             | false    |
| `management-cluster`       | Codename of the Management Cluster the Workload Cluster belongs to.     | true     |
| `name`                     | Name of the Workload Cluster.                                           | true     |
| `organization`             | Name of the Organization the Workload Cluster belongs to.               | true     |
| `repository-name`          | Name of the GitOps repository.                                          | true     |
| `skip-mapi`                | Skip mapi directory when adding the app.                                | false    |


## Usage

The command to execute is the `kubectl gs gitops add wc`.
{{% kubectl_gs_gitops_common_flags %}}

To preview the objects to be created by the command, run it with the `--dry-run` flag. Fine example below.

{{< tabs >}}
{{< tab id="no-definition" title="No Definition" >}}

In the most basic form the GitOps repository may be populated with Workload Cluster-related structure, yet
without the cluster-related CRs.

```nohighlight
kubectl gs gitops add wc \
--local-path /tmp/gitops-demo \
--name demowc \
--management-cluster demomc \
--organization demoorg \
--repository-name gitops-demo \
--dry-run

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/secrets/demowc.gpgkey.enc.yaml
apiVersion: v1
kind: Secret
metadata:
    name: sops-gpg-demowc

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: "./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi"
  postBuild:
    substitute:
      cluster_name: demowc
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster
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
resources: []

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/patch_cluster_config.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ignored
spec:
  kubeConfig:
    context:
      name: ${cluster_name}-admin@${cluster_name}
    inCluster: false
    secret:
      name: ${cluster_name}-kubeconfig
      namespace: org-${organization}


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml
```

{{< /tab >}}
{{< tab id="with-definition" title="Definition" >}}

When desired to manage cluster definition from GitOps repository, it can be added by the `--base`,
`--cluster-release`, and the `--default-apps-release` flags.

```nohighlight
kubectl gs gitops add wc \
--local-path /tmp/gitops-demo \
--name demowc \
--management-cluster demomc \
--organization demoorg \
--repository-name gitops-demo \
--base bases/cluster/capi \
--cluster-release 1.0.0 \
--default-apps-release 2.0.0 \
--dry-run

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/secrets/demowc.gpgkey.enc.yaml
apiVersion: v1
kind: Secret
metadata:
    name: sops-gpg-demowc

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: "./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi"
  postBuild:
    substitute:
      cluster_name: demowc
      cluster_release: 1.0.0
      default_apps_release: 2.0.0
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster
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
resources: []

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/patch_cluster_config.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ignored
spec:
  kubeConfig:
    context:
      name: ${cluster_name}-admin@${cluster_name}
    inCluster: false
    secret:
      name: ${cluster_name}-kubeconfig
      namespace: org-${organization}

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/managed-by: flux
kind: Kustomization
resources:
  - ../../../../../../../../bases/cluster/capi


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: ./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
  postBuild:
    substitute:
      cluster_name: demowc
      cluster_release: 1.0.0
      default_apps_release: 2.0.0
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m
```

{{< /tab >}}
{{< tab id="with-definition-config" title="Definition and Configuration" >}}

Cluster definition coming from a base may also be customized with a user configuration passed by the
`--cluster-user-config` and the `--default-apps-user-config` flags. **Note, files referenced by these flags
should carry a valid values YAML configuration conforming the values schema of the given cluster- and default-apps- apps versions.**

Below is the example of `values.yaml` configuring cluster description and name of the cloud config ConfigMap.

```yaml
clusterDescription: GitOps Demo Cluster
cloudConfig: demo-cloud-config
```

After saving this into `/tmp/values.yaml`, it can be referenced when adding a cluster.

```nohighlight
kubectl gs gitops add wc \
--local-path /tmp/gitops-demo \
--name demowc \
--management-cluster demomc \
--organization demoorg \
--repository-name gitops-demo \
--base bases/cluster/capi \
--cluster-release 1.0.0 \
--default-apps-release 2.0.0 \
--cluster-user-config /tmp/values.yaml
--dry-run

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/secrets/demowc.gpgkey.enc.yaml
apiVersion: v1
kind: Secret
metadata:
    name: sops-gpg-demowc

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: "./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi"
  postBuild:
    substitute:
      cluster_name: demowc
      cluster_release: 1.0.0
      default_apps_release: 2.0.0
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster
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
resources: []

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/apps/patch_cluster_config.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ignored
spec:
  kubeConfig:
    context:
      name: ${cluster_name}-admin@${cluster_name}
    inCluster: false
    secret:
      name: ${cluster_name}-kubeconfig
      namespace: org-${organization}

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/managed-by: flux
kind: Kustomization
patchesStrategicMerge:
  - patch_cluster_userconfig.yaml
resources:
  - ../../../../../../../../bases/cluster/capi
  - cluster_userconfig.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/cluster_userconfig.yaml
apiVersion: v1
data:
  values: |
    clusterDescription: GitOps Demo Cluster
    cloudConfig: demo-cloud-config
kind: ConfigMap
metadata:
  name: demowc-cluster-userconfig
  namespace: org-demoorg

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/patch_cluster_userconfig.yaml
apiVersion: application.giantswarm.io/v1alpha1
kind: App
metadata:
  name: ${cluster_name}
  namespace: org-${organization}
spec:
  userConfig:
    configMap:
      name: demowc-cluster-userconfig
      namespace: org-demoorg


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: ./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
  postBuild:
    substitute:
      cluster_name: demowc
      cluster_release: 1.0.0
      default_apps_release: 2.0.0
      organization: demoorg
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m
```

{{< /tab >}}
{{< /tabs >}}

Remove the `--dry-run` flag and re-run the command it to apply the changes.
