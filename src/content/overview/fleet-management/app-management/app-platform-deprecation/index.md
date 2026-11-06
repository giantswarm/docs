---
linkTitle: App Platform deprecation
title: App Platform deprecation and migration to Flux HelmRelease
diataxis_content_type: explanation
description: Timeline, reasoning, and migration path for moving from the Giant Swarm App Platform to Flux HelmRelease.
weight: 100
menu:
  principal:
    parent: overview-fleetmanagement-appmanagement
    identifier: overview-fleetmanagement-appmanagement-appplatformdeprecation
aliases:
  - /overview/fleet-management/app-management/app-cr-deprecation/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - Is the App custom resource being deprecated?
  - When will App CRs stop being supported?
  - How do I migrate from App CRs to Flux HelmRelease?
  - What's the recommended way to deploy apps on Giant Swarm now?
  - How do I migrate a cluster deployed with an App CR to a HelmRelease?
last_review_date: 2026-11-06
---

The Giant Swarm App custom resource (`App`, in the `application.giantswarm.io` API group) is being phased out in favor of upstream [Flux HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/). Every Giant Swarm management cluster already runs Flux, and we're now making it the recommended way for customers to deploy and configure applications.

## Why we're making this change

- **Standard upstream API.** HelmRelease is a widely adopted upstream API. You can use the same tooling on Giant Swarm that you use elsewhere, with no proprietary CRD to learn.
- **More expressive feature set.** HelmRelease offers dependency ordering (`dependsOn`), drift detection, post-renderers, fine-grained install/upgrade/rollback policies, and `valuesFrom` with explicit merge order. These features map onto things we've layered on top of App CRs over the years.
- **Simpler stack.** Collapsing the Giant Swarm app-operator pipeline into one well-understood upstream controller reduces moving parts on the management cluster.

## HelmRelease capabilities to know

These features either have no App CR equivalent or previously required custom tooling to approximate. See the upstream [HelmRelease reference](https://fluxcd.io/flux/components/helm/helmreleases/) for the full specification.

- **Post-renderers.** Apply Kustomize patches to a rendered chart so you can adjust upstream charts (image references, annotations, individual fields) without forking. Patches are persisted to the release, so drift detection accounts for them.
- **Drift detection.** Opt-in via `spec.driftDetection.mode: enabled` (`warn` only reports). Then Flux reverts out-of-band changes (`kubectl edit`, console edits) back to the declared manifest on each reconcile, with ignore rules for fields that legitimately change at runtime.
- **Readiness-gated dependencies.** `dependsOn` blocks a release until other HelmReleases report `Ready`. This solves the common case of installing a controller (and its custom resource definitions) before any custom resources that depend on it.
- **Configurable failure remediation.** Declarative retry counts, choice of rollback or uninstall on failure, and `cleanupOnFail`, all surfaced as spec fields.
- **Flexible chart sources.** Pull charts from `HelmRepository`, `OCIRepository`, `GitRepository`, or `Bucket`, including OCI references with SemVer ranges for controlled auto upgrades.

## Timeline

_Specific dates to be confirmed._ Until the timeline is finalized:

{{% steps %}}

{{% step title="Phase 1: Communication and docs (completed)" %}}
App Platform sunset announced with a long deprecation window. App Platform documentation moved to a legacy section and new tutorials default to Flux resources.
{{% /step %}}

{{% step title="Phase 2: Flux by default (completed)" %}}
App Platform (`App`, `AppCatalog`, `AppCatalogEntry`, `Catalog`, `Chart`) are fully supported but new deployments should prefer the Flux resources.
{{% /step %}}

{{% step title="Phase 3: Resource migration (today)" %}}
The [migration CLI](#migrating-with-the-cli) is available. App Platform reconciliation continues unchanged, so existing deployments keep working while you migrate them over to Flux.
{{% /step %}}

{{% step title="Phase 4: Sunset (~year)" %}}
App Platform support ends. All workloads expected to run as Flux resources.
{{% /step %}}

{{% /steps %}}

We update this page as the timeline is firmed up. If you're planning a major deployment, contact your account engineer or [support](mailto:support@giantswarm.io) and we'll factor your schedule in.

## What this means for you

- **Existing App Platform resources keep working.** There will be a long, supported overlap period, so don't rush a migration.
- **For new deployments, use Flux resources.** Start with [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).
- **Plan a migration when it fits your release cadence.** The [migration CLI](#migrating-with-the-cli) converts App Platform resources into Flux equivalents, one app at a time.

## What's affected

The following resource types in the `application.giantswarm.io` API group are part of the deprecation:

- `App`
- `AppCatalog`
- `AppCatalogEntry`
- `Catalog`
- `Chart`

Their reference documentation remains available but will be marked as deprecated and link back to this page.

## Migrating with the CLI

The [appcr-to-helmrelease-converter](https://github.com/giantswarm/appcr-to-helmrelease-converter) CLI moves one App CR at a time to Flux. It reads the App CR and its `Catalog` from the management cluster and creates an `OCIRepository` (or a `HelmRepository` for a Helm catalog) and a `HelmRelease` with the same name, namespace and values. Its `ConfigMap` and `Secret` references become `valuesFrom` entries in the same order. Flux then takes over the Helm release the App CR installed, so the app isn't reinstalled.

You need [uv](https://docs.astral.sh/uv/getting-started/installation/) and `kubectl` access to the management cluster. The app must be deployed, as the CLI reads its live state.

First, install the CLI:

```sh
git clone https://github.com/giantswarm/appcr-to-helmrelease-converter
cd appcr-to-helmrelease-converter
uv sync
```

Then preview the Flux resources it generates for the App CR, here `loki` in `org-acme`:

```sh
uv run python main.py migrate --name loki --namespace org-acme --dry-run --output loki-flux.yaml
```

Run it again without `--dry-run` to migrate. The CLI suspends the App CR, applies the Flux resources and waits for the `HelmRelease` to be ready. If it fails, the CLI offers to roll back.

If the App CR comes from a GitOps repository, replace it there with the resources in `loki-flux.yaml` and merge the change.

Finally, delete the App CR and its `Chart` CR from the cluster:

```sh
uv run python main.py cleanup --name loki --namespace org-acme
```

`cleanup` checks that the `HelmRelease` is ready and that Flux manages it before it deletes anything. Note that it can't check your GitOps repository. If the App CR is still there, Flux creates it again.

The [CLI's README](https://github.com/giantswarm/appcr-to-helmrelease-converter#readme) describes every flag, for example for private catalogs and registry mirrors.

### Clusters

Clusters deployed with an App CR of a cluster chart, like `cluster-aws`, migrate the same way. The App CR has the name of the cluster and lives in the organization namespace. The CLI deploys the cluster with the release chart, like `release-aws`, at the cluster's release version. The release chart's version is the release version, so you upgrade the cluster by changing the chart version in the `OCIRepository`.

Before the next upgrade, remove `global.release.version` from the cluster values. `cleanup` refuses to run while it's set.

### GitOps repositories created with kubectl-gs

Since [kubectl-gs v5.13.0](https://github.com/giantswarm/kubectl-gs/releases/tag/v5.13.0), `kubectl gs template cluster` renders clusters as a `HelmRelease` of the release chart. Newer versions of `kubectl gs gitops add base` and `kubectl gs gitops add workload-cluster` do the same and don't support App CRs anymore. To keep using them on a repository created with an older version, upgrade the repository once its App CRs are gone:

1. Migrate every cluster and app in the repository with the CLI.
2. Replace the cluster App CR in each cluster base with the `OCIRepository` and `HelmRelease` that `kubectl gs gitops add base` generates.
3. Check which parts of the repository are outdated, then upgrade them:

   ```sh
   kubectl gs gitops check
   kubectl gs gitops upgrade
   ```

`gitops upgrade` rewrites the files kubectl-gs generated around the App CRs. The patch adding `--cluster-user-config` to the cluster then targets the `HelmRelease`, and the patch pointing App CRs at the workload cluster goes away. It fails on any part of the repository that still deploys an App CR and lists the files.

Giant Swarm also has an internal skill that drives the migration of an app across all your clusters, with the CLI doing each step. It works best on repositories that follow the [gitops-template](https://github.com/giantswarm/gitops-template) structure. If you'd like help with the migration, ask your account engineer.

## Where to go next

- [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}): the recommended path for new deployments.
- [App management overview]({{< relref "/overview/fleet-management/app-management" >}}): conceptual overview of how Giant Swarm manages apps.
- [FluxCD]({{< relref "/tutorials/continuous-deployment/flux" >}}): Flux fundamentals on Giant Swarm.

If you have questions about the timeline or migration approach, reach out to your account engineer or to [support](mailto:support@giantswarm.io).
