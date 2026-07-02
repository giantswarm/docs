---
linkTitle: Group multiple HelmReleases
title: Group multiple HelmReleases together
diataxis_content_type: how-to-guide
description: Patterns for deploying related HelmReleases as a unit. Covers Helm umbrella charts, Kustomize over multiple releases, and install ordering via `dependsOn`.
weight: 40
menu:
  principal:
    identifier: tutorials-continuous-deployment-helm-releases-multiple
    parent: tutorials-continuous-deployment-helm-releases
user_questions:
  - How do I deploy a set of related apps as one HelmRelease?
  - How do I pin a group of HelmRelease versions together?
  - How do I order HelmRelease installs so one waits for another?
  - What's the HelmRelease equivalent of Giant Swarm App Sets?
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
last_review_date: 2026-06-17
---

There are three idiomatic ways to deploy a related group of HelmReleases together. Pick the one that fits your coupling level:

1. **Helm umbrella chart.** Package the components as sub-charts of one parent chart. Deploy as a single HelmRelease. Strongest coupling: every component upgrades together, on one Helm history.
2. **Kustomize over multiple HelmReleases.** Keep each component as a separate HelmRelease and OCIRepository, then use a Kustomize base to apply shared labels, a common namespace, and version pins. Closest to the [Giant Swarm App Sets pattern]({{< relref "/tutorials/continuous-deployment/apps/app-sets" >}}).
3. **`dependsOn`.** Independent HelmReleases that need to install in a specific order. A native Flux feature with no App CR equivalent.

These three patterns compose. An umbrella chart can be wrapped in a Kustomize base, and a Kustomize-grouped set of releases can use `dependsOn` between members.

## Helm umbrella chart

If the components belong to the same product and ship on the same cadence, package them as a single Helm chart with `dependencies` declared in `Chart.yaml`:

```yaml
# Chart.yaml of the umbrella chart
apiVersion: v2
name: hello-web-app
version: 0.1.0
dependencies:
  - name: hello-world
    version: 0.1.9
    repository: oci://gsoci.azurecr.io/charts/giantswarm
  - name: simple-db
    version: 0.1.1
    repository: oci://gsoci.azurecr.io/charts/giantswarm
```

Publish the umbrella chart to your OCI registry. Then deploy it with one OCIRepository and one HelmRelease, the same way you would any other chart. Shared values and per-`subchart` values both live in the umbrella chart's `values.yaml`, with `subchart` values nested under each dependency name:

```yaml
# values.yaml of the umbrella chart
hello-world:
  replicaCount: 2

simple-db:
  storage:
    size: 5Gi
```

See the upstream [Helm chart dependencies documentation](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/) for the full mechanics, including global values shared across sub-charts.

## Kustomize over multiple HelmReleases

When the components ship independently but still need to be deployed and configured together, keep each one as its own HelmRelease and OCIRepository, then group them with a Kustomize base.

Create a base directory with the per-component manifests (one HelmRelease + one OCIRepository per component), and a `kustomization.yaml` that pulls them together:

```yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
commonLabels:
  gitops.giantswarm.io/releaseGroup: hello-web-app
namespace: hello-web
patches:
  - patch: |-
      - op: replace
        path: /spec/ref/tag
        value: "0.1.9"
    target:
      kind: OCIRepository
      name: hello-world
  - patch: |-
      - op: replace
        path: /spec/ref/tag
        value: "0.1.1"
    target:
      kind: OCIRepository
      name: simple-db
resources:
  - ../../components/hello-world
  - ../../components/simple-db
```

What this base provides:

- **`commonLabels`** stamps a single label across every HelmRelease and OCIRepository in the group, so you can filter the developer portal or `kubectl` queries by that label.
- **`namespace`** enforces the same target namespace for the HelmRelease and OCIRepository resources themselves. The Helm install target namespace is a separate field (`spec.targetNamespace` on the HelmRelease).
- **Inline patches** pin the chart versions on each OCIRepository, so the group uses a known-good combination.
- **`resources`** references the per-component bases. Each component base contains its own HelmRelease, OCIRepository, and optional `ConfigMap` or `Secret`.

Consumers use this base by referencing it from a workload-cluster-level Kustomization, the same way they would a single-component base.

## Ordering with `dependsOn`

If one release must finish installing before another starts (for example, `cert-manager` before anything that needs certificates), use the `dependsOn` field on the dependent HelmRelease:

```yaml
apiVersion: helm.toolkit.fluxcd.io/v2
kind: HelmRelease
metadata:
  name: dev01-hello-world
  namespace: org-acmedev
spec:
  dependsOn:
    - name: dev01-cert-manager
      namespace: org-acmedev
  chartRef:
    kind: OCIRepository
    name: dev01-hello-world
  # ...
```

Flux waits for `dev01-cert-manager` to report `Ready=True` before reconciling `dev01-hello-world`. `dependsOn` supports cross-namespace references and chained dependencies. See the [HelmRelease dependencies reference](https://fluxcd.io/flux/components/helm/helmreleases/#dependencies) for the full semantics, including timeout behavior.
