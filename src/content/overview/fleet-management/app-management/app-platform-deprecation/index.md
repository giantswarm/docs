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
last_review_date: 2026-06-17
---

The Giant Swarm App custom resource (`App`, in the `application.giantswarm.io` API group) is being phased out in favor of upstream [Flux HelmRelease](https://fluxcd.io/flux/components/helm/helmreleases/). Every Giant Swarm management cluster already runs Flux, and we're now making it the recommended way for customers to deploy and configure applications.

## Why we're making this change

- **Standard upstream API.** HelmRelease is a widely adopted upstream API. You can use the same tooling on Giant Swarm that you use elsewhere, with no proprietary CRD to learn.
- **More expressive feature set.** HelmRelease offers dependency ordering (`dependsOn`), drift detection, post-renderers, fine-grained install/upgrade/rollback policies, and `valuesFrom` with explicit merge order. These features map onto things we've layered on top of App CRs over the years.
- **Simpler stack.** Collapsing the Giant Swarm app-operator pipeline into one well-understood upstream controller reduces moving parts on the management cluster.

## HelmRelease capabilities to know

These features either have no App CR equivalent or previously required custom tooling to approximate. See the upstream [HelmRelease reference](https://fluxcd.io/flux/components/helm/helmreleases/) for the full specification.

- **Post-renderers.** Apply Kustomize patches to a rendered chart so you can adjust upstream charts (image references, annotations, individual fields) without forking. Patches are persisted to the release, so drift detection accounts for them.
- **Drift detection.** Reverts out-of-band changes (`kubectl edit`, console edits) back to the declared manifest on each reconcile, with ignore rules for fields that legitimately change at runtime.
- **Readiness-gated dependencies.** `dependsOn` blocks a release until other HelmReleases report `Ready`. This solves the common case of installing a controller (and its custom resource definitions) before any custom resources that depend on it.
- **Configurable failure remediation.** Declarative retry counts, choice of rollback or uninstall on failure, and `cleanupOnFail`, all surfaced as spec fields.
- **Flexible chart sources.** Pull charts from `HelmRepository`, `OCIRepository`, `GitRepository`, or `Bucket`, including OCI references with SemVer ranges for controlled auto upgrades.

## Timeline

_Specific dates to be confirmed._ Until the timeline is finalized:

{{% steps %}}

{{% step title="Phase 1: Communication and docs (completed)" %}}
App Platform sunset announced with a long deprecation window. App Platform documentation moved to a legacy section and new tutorials default to Flux resources.
{{% /step %}}

{{% step title="Phase 2: Today" %}}
App Platform (`App`, `AppCatalog`, `AppCatalogEntry`, `Catalog`, `Chart`) are fully supported but new deployments should prefer the Flux resources.
{{% /step %}}

{{% step title="Phase 3: Resource migration (soon)" %}}
Migration CLI available. App Platform reconciliation continues unchanged, so existing deployments keep working while you migrate them over to Flux.
{{% /step %}}

{{% step title="Phase 4: Sunset (~year)" %}}
App Platform support ends. All workloads expected to run as Flux resources.
{{% /step %}}

{{% /steps %}}

We'll update this page as the timeline is firmed up. If you're planning a major deployment, contact your account engineer or [support](mailto:support@giantswarm.io) and we'll factor your schedule in.

## What this means for you

- **Existing App Platform resources keep working.** There will be a long, supported overlap period, so don't rush a migration.
- **For new deployments, use Flux resources.** Start with [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}).
- **Plan a migration when it fits your release cadence.** A dedicated CLI is in development to convert App Platform resources into Flux equivalents. Docs for the CLI will land here once it's ready.

## What's affected

The following resource types in the `application.giantswarm.io` API group are part of the deprecation:

- `App`
- `AppCatalog`
- `AppCatalogEntry`
- `Catalog`
- `Chart`

Their reference documentation remains available but will be marked as deprecated and link back to this page.

## Migration CLI

We're building a CLI tool that converts an existing App Platform resources (along with its associated `ConfigMap` and `Secret` resources) into an equivalent Flux resources. The tool preserves configuration semantics where the two APIs overlap and flags fields that need manual review.

This page will be updated with installation and usage instructions when the tool is released.

## Where to go next

- [Deploying an application via a Flux HelmRelease]({{< relref "/tutorials/fleet-management/app-platform/deploy-app-helmrelease" >}}): the recommended path for new deployments.
- [App management overview]({{< relref "/overview/fleet-management/app-management" >}}): conceptual overview of how Giant Swarm manages apps.
- [FluxCD]({{< relref "/tutorials/continuous-deployment/flux" >}}): Flux fundamentals on Giant Swarm.

If you have questions about the timeline or migration approach, reach out to your account engineer or to [support](mailto:support@giantswarm.io).
