---
linkTitle: App CR deprecation
title: App CR deprecation and migration to Flux HelmRelease
description: Timeline, reasoning, and migration path for moving from Giant Swarm App custom resources to Flux HelmRelease.
weight: 100
menu:
  principal:
    parent: overview-fleetmanagement-appmanagement
    identifier: overview-fleetmanagement-appmanagement-appcrdeprecation
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - Is the App custom resource being deprecated?
  - When will App CRs stop being supported?
  - How do I migrate from App CRs to Flux HelmRelease?
  - What's the recommended way to deploy apps on Giant Swarm now?
last_review_date: 2026-06-17
---

**Status:** Draft. Timeline to be confirmed.

The Giant Swarm App custom resource (`App`, in the `application.giantswarm.io` API group) is being phased out in favor of upstream [Flux HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/). Every Giant Swarm management cluster already runs Flux, and we're now making it the recommended way for customers to deploy and configure applications.

## Why we're making this change

- **Standard upstream API.** HelmRelease is a widely adopted upstream API. You can use the same tooling on Giant Swarm that you use elsewhere, with no proprietary CRD to learn.
- **More expressive feature set.** HelmRelease offers dependency ordering (`dependsOn`), drift detection, post-renderers, fine-grained install/upgrade/rollback policies, and `valuesFrom` with explicit merge order. These features map onto things we've layered on top of App CRs over the years.
- **Simpler stack.** Collapsing the Giant Swarm app-operator pipeline into one well-understood upstream controller reduces moving parts on the management cluster.

## Notable capabilities HelmRelease adds

These features either have no App CR equivalent or previously required custom tooling to approximate. See the upstream [HelmRelease reference](https://fluxcd.io/flux/components/helm/helmreleases/) for the full specification.

- **Post-renderers.** Apply Kustomize patches to a rendered chart so you can adjust upstream charts (image references, annotations, individual fields) without forking. Patches are persisted to the release, so drift detection accounts for them.
- **Drift detection.** Reverts out-of-band changes (`kubectl edit`, console edits) back to the declared manifest on each reconcile, with ignore rules for fields that legitimately change at runtime.
- **Readiness-gated dependencies.** `dependsOn` blocks a release until other HelmReleases report `Ready`. This solves the common case of installing a controller (and its custom resource definitions) before any custom resources that depend on it.
- **Configurable failure remediation.** Declarative retry counts, choice of rollback or uninstall on failure, and `cleanupOnFail`, all surfaced as spec fields.
- **Flexible chart sources.** Pull charts from `HelmRepository`, `OCIRepository`, `GitRepository`, or `Bucket`, including OCI references with SemVer ranges for controlled auto upgrades.

## Timeline

_Specific dates to be confirmed._ Until the timeline is finalized:

{{%/* steps */%}}

{{% step title="Today" %}}
Both App CRs and HelmRelease are fully supported. New deployments should prefer HelmRelease.
{{% /step %}}

{{% step title="Phase 1 (TBD)" %}}
App CR documentation moved to a legacy section; new tutorials default to HelmRelease.
{{% /step %}}

{{% step title="Phase 2 (TBD)" %}}
Migration CLI available; App CR reconciliation continues unchanged.
{{% /step %}}

{{% step title="Phase 3 (TBD)" %}}
App CR sunset announced with a long deprecation window. Existing deployments continue to work; new App CR creation may be restricted.
{{% /step %}}

{{% step title="Phase 4 (TBD)" %}}
App CR support ends. All workloads expected to run as HelmReleases.
{{% /step %}}

{{% /steps %}}

We'll update this page as the timeline is firmed up. If you're planning a major deployment, contact your account engineer or [support](mailto:support@giantswarm.io) and we'll factor your schedule in.

## What this means for you

- **Existing App CR deployments keep working.** There will be a long, supported overlap period, so don't rush a migration.
- **For new deployments, use Flux HelmRelease.** Start with [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).
- **Plan a migration when it fits your release cadence.** A dedicated CLI is in development to convert App CR bundles into equivalent HelmRelease + OCIRepository bundles. Docs for the CLI will land here once it's ready.

## What's affected

The following resource types in the `application.giantswarm.io` API group are part of the deprecation:

- `App`
- `AppCatalog`
- `AppCatalogEntry`
- `Catalog`
- `Chart`

Their reference documentation remains available but will be marked as deprecated and link back to this page.

## Migration CLI

We're building a CLI tool that converts an existing App CR (along with its associated ConfigMaps and Secrets) into an equivalent Flux HelmRelease and OCIRepository bundle. The tool preserves configuration semantics where the two APIs overlap and flags fields that need manual review.

This page will be updated with installation and usage instructions when the tool is released.

## Where to go next

- [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}): the recommended path for new deployments.
- [App management overview]({{< relref "/overview/fleet-management/app-management" >}}): conceptual overview of how Giant Swarm manages apps.
- [FluxCD]({{< relref "/tutorials/continuous-deployment/flux" >}}): Flux fundamentals on Giant Swarm.

If you have questions about the timeline or migration approach, reach out to your account engineer or to [support](mailto:support@giantswarm.io).
