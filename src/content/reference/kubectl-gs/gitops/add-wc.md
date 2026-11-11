---
linkTitle: add workload-cluster
title: "'kubectl gs gitops add workload-cluster' command reference"
diataxis_content_type: reference
description: Reference documentation on how to add a new workload cluster to a GitOps repository.
weight: 25
menu:
  principal:
    parent: kubectlgs-gitops
last_review_date: 2026-11-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How do I add a workload cluster to a GitOps repository?
aliases:
  - /vintage/use-the-api/kubectl-gs/gitops/add-wc/
---

This command adds a new workload cluster to the GitOps repository.

## Prerequisites

Your GitOps repository should provide the following structural layers:

- Basic structure (see [`init`]({{< relref "/reference/kubectl-gs/gitops/init" >}}))
- Management cluster (see [`add management-cluster`]({{< relref "/reference/kubectl-gs/gitops/add-mc" >}}))
- Organization (see [`add organization`]({{< relref "/reference/kubectl-gs/gitops/add-org" >}}))

## Description

The structure created by this command is presented below. Note, the initial layers are flattened for brevity. Resources enclosed
in a square brackets `[]` are considered optional.

```nohighlight
management-clusters/MC_NAME
└── organizations
    └── ORG_NAME
        └── workload-clusters
            ├── kustomization.yaml
            ├── WC_NAME.yaml
            └── WC_NAME
                └── [mapi]
                    ├── apps
                    │   └── kustomization.yaml
                    └── cluster
                        ├── [kustomization.yaml]
                        ├── [cluster_userconfig.yaml]
                        └── [patch_cluster_userconfig.yaml]
```

The content of the `cluster` directory is optional because in its most basic form, the GitOps repository does not require you to
put the cluster definition in there. It can be added later by re-running the command with additional flags. Re-running works
in such case, because `cluster` directory is initially empty. Note however, in order to populate it, you must have a
working base and reference it by the `--base` flag when running the command. You may customize the referenced base with
the `--cluster-user-config` flag when needed.

With `--base`, use a base that deploys a `release-<provider>` chart, such as `release-aws`, with a Flux
`OCIRepository` and `HelmRelease`. The
[CAPA cluster base](https://github.com/giantswarm/gitops-template/tree/main/bases/clusters/capa/template) in
gitops-template is one, and the [`add base`]({{< relref "/reference/kubectl-gs/gitops/add-base" >}}) command creates
one for other providers. The chart version of a `release-<provider>` chart is the Giant Swarm release version. The
`--release` flag sets the `release` variable of the Flux Kustomization, and the base uses it as the tag of the
`OCIRepository`. The release is then stored in Git, and you upgrade the cluster by changing that variable. Pass the
version without the `v` prefix, for example `36.2.0`. The command checks that the release is published as a chart in
the `gsoci.azurecr.io` registry.

The chart sets `global.release.version` in its default values. Don't set it in the values you pass with
`--cluster-user-config`. A copy in your values would stay at the old release when you upgrade the cluster.

The command refuses a base that deploys an App CR, also when the App CR comes from a base below an overlay. Releases
before v34 have no `release-<provider>` chart, so they can't be added with a base. See the
[App Platform deprecation]({{< relref "/overview/fleet-management/app-management/app-platform-deprecation" >}}).

**Note:** this needs kubectl-gs v6.0.0 or newer. Older versions generate an App CR for the cluster.

The command doesn't create the workload cluster's SOPS key Secret. The
[`add encryption`]({{< relref "/reference/kubectl-gs/gitops/add-enc" >}}) command creates it when you add encryption to the
cluster.

**Note:** the latest recommendation mandates creation of the `mapi` directory. However, users who have not yet migrated to it,
but still want to use automation for their repositories, may skip the `mapi` layer by using the `--skip-mapi` flag. Migration is
nevertheless mandatory, and hence this flag is planned to be removed from `kubectl-gs` at some point.

## Usage

Basic command syntax: `kubectl gs gitops add workload-cluster <FLAGS>`

### Flags

- `--management-cluster` -- name of the management cluster the workload cluster belongs to (required)
- `--name` -- name of the workload cluster (required)
- `--organization` -- name of the organization the workload cluster belongs to (required)
- `--repository-name` -- name of the GitOps repository (required)
- `--base` -- path to the base directory; must be relative to the repository root
- `--release` -- [workload cluster release](https://github.com/giantswarm/releases) version without the `v` prefix, for example `36.2.0`; required when `--base` is set
- `--cluster-user-config` -- path to a values file for the cluster chart. Its values come after the base's values, so they win
- `--skip-mapi` -- skip mapi directory when adding the app

{{% kubectl_gs_gitops_common_flags %}}

### Examples

{{< tabs >}}
{{< tab id="no-definition" title="No Definition" >}}

In the most basic form the GitOps repository may be populated with Workload Cluster-related structure, yet
without the cluster-related CRs.

```nohighlight
kubectl gs gitops add workload-cluster \
  --local-path /tmp/gitops-demo \
  --name demowc \
  --management-cluster demomc \
  --organization demoorg \
  --repository-name gitops-demo \
  --dry-run
```

Output:

```nohighlight

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
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
resources: []


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml


## METADATA ##
/tmp/gitops-demo/.gitops-metadata.yaml
# This file is managed by `kubectl gs gitops`. Do not edit it by hand.
# It records which version of the repository structure each part of this
# repository was generated with, so that `kubectl gs gitops check` can tell
# you when the repository has fallen behind.
apiVersion: gitops.giantswarm.io/v1alpha1
generatedWith: kubectl-gs/6.0.3
kind: RepositoryMetadata
layers:
- generatedWith: kubectl-gs/6.0.3
  kind: management-cluster
  path: management-clusters/demomc
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: organization
  path: management-clusters/demomc/organizations/demoorg
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: workload-cluster
  path: management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
  structureVersion: 2
structureVersion: 2
```

{{< /tab >}}
{{< tab id="with-definition" title="Definition" >}}

When desired to manage cluster definition from GitOps repository, it can be added by the `--base`
and `--release` flags. This example uses the CAPA cluster base, so the `HelmRelease` installs `release-aws` 36.2.0.

```nohighlight
kubectl gs gitops add workload-cluster \
  --local-path /tmp/gitops-demo \
  --name demowc \
  --management-cluster demomc \
  --organization demoorg \
  --repository-name gitops-demo \
  --base bases/clusters/capa/template \
  --release 36.2.0 \
  --dry-run
```

Output:

```nohighlight

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
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
      cluster_description: "demowc managed by GitOps"
      release: 36.2.0
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
resources: []

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/managed-by: flux
kind: Kustomization
resources:
  - ../../../../../../../../bases/clusters/capa/template


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: ./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
  postBuild:
    substitute:
      cluster_description: demowc managed by GitOps
      cluster_name: demowc
      organization: demoorg
      release: 36.2.0
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m


## METADATA ##
/tmp/gitops-demo/.gitops-metadata.yaml
# This file is managed by `kubectl gs gitops`. Do not edit it by hand.
# It records which version of the repository structure each part of this
# repository was generated with, so that `kubectl gs gitops check` can tell
# you when the repository has fallen behind.
apiVersion: gitops.giantswarm.io/v1alpha1
generatedWith: kubectl-gs/6.0.3
kind: RepositoryMetadata
layers:
- generatedWith: kubectl-gs/6.0.3
  kind: management-cluster
  path: management-clusters/demomc
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: organization
  path: management-clusters/demomc/organizations/demoorg
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: workload-cluster
  path: management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
  structureVersion: 2
structureVersion: 2
```

{{< /tab >}}
{{< tab id="with-definition-config" title="Definition and Configuration" >}}

Cluster definition coming from a base may also be customized with a user configuration passed by the
`--cluster-user-config` flag. The command writes the values to a ConfigMap, and a patch appends that ConfigMap to the
`valuesFrom` of the base's `HelmRelease`. Flux merges `valuesFrom` in order, so these values win over the base's
values. Don't set `global.release.version` in them, because the chart sets it.

**Note:** files referenced by this flag should carry a valid values YAML configuration conforming the values schema of the given cluster chart version.

Below is the example of `values.yaml` setting the service priority of the cluster.

```yaml
global:
  metadata:
    servicePriority: medium
```

After saving this into `/tmp/values.yaml`, it can be referenced when adding a cluster.

```nohighlight
kubectl gs gitops add workload-cluster \
  --local-path /tmp/gitops-demo \
  --name demowc \
  --management-cluster demomc \
  --organization demoorg \
  --repository-name gitops-demo \
  --base bases/clusters/capa/template \
  --release 36.2.0 \
  --cluster-user-config /tmp/values.yaml \
  --dry-run
```

Output:

```nohighlight

## CREATE ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
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
      cluster_description: "demowc managed by GitOps"
      release: 36.2.0
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
resources: []

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
commonLabels:
  giantswarm.io/managed-by: flux
kind: Kustomization
patches:
  - path: patch_cluster_userconfig.yaml
    target:
      group: helm.toolkit.fluxcd.io
      kind: HelmRelease
      # A regular expression matching the name the base gives the HelmRelease
      # before Flux substitutes the variables.
      name: \$\{cluster_name\}
resources:
  - ../../../../../../../../bases/clusters/capa/template
  - cluster_userconfig.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/cluster_userconfig.yaml
apiVersion: v1
data:
  values: |
    global:
      metadata:
        servicePriority: medium
kind: ConfigMap
metadata:
  name: demowc-cluster-userconfig
  namespace: org-demoorg

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi/cluster/patch_cluster_userconfig.yaml
- op: add
  path: /spec/valuesFrom/-
  value:
    kind: ConfigMap
    name: demowc-cluster-userconfig
    valuesKey: values


## MODIFY ##
/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
- demowc.yaml

/tmp/gitops-demo/management-clusters/demomc/organizations/demoorg/workload-clusters/demowc.yaml
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: demomc-clusters-demowc
  namespace: default
spec:
  interval: 1m
  path: ./management-clusters/demomc/organizations/demoorg/workload-clusters/demowc/mapi
  postBuild:
    substitute:
      cluster_description: demowc managed by GitOps
      cluster_name: demowc
      organization: demoorg
      release: 36.2.0
  prune: false
  serviceAccountName: automation
  sourceRef:
    kind: GitRepository
    name: gitops-demo
  timeout: 2m


## METADATA ##
/tmp/gitops-demo/.gitops-metadata.yaml
# This file is managed by `kubectl gs gitops`. Do not edit it by hand.
# It records which version of the repository structure each part of this
# repository was generated with, so that `kubectl gs gitops check` can tell
# you when the repository has fallen behind.
apiVersion: gitops.giantswarm.io/v1alpha1
generatedWith: kubectl-gs/6.0.3
kind: RepositoryMetadata
layers:
- generatedWith: kubectl-gs/6.0.3
  kind: management-cluster
  path: management-clusters/demomc
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: organization
  path: management-clusters/demomc/organizations/demoorg
  structureVersion: 2
- generatedWith: kubectl-gs/6.0.3
  kind: workload-cluster
  path: management-clusters/demomc/organizations/demoorg/workload-clusters/demowc
  structureVersion: 2
structureVersion: 2
```

{{< /tab >}}
{{< /tabs >}}

Remove the `--dry-run` flag and re-run the command it to apply the changes.
