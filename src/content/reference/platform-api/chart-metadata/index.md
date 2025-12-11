---
title: Chart metadata reference
linkTitle: Chart metadata
description: Helm charts maintained by Giant Swarm require certain chart metadata. This page explains which fields are requires and recommended, and for what purpose. We also show how chart metadata is represented in OCI registries.
menu:
  principal:
    identifier: reference-platform-api-chartmetadata
    parent: reference-platform-api
last_review_date: 2025-12-09
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What metadata is required in Chart.yaml?
  - How is chart metadata represented in OCI registries?
---

Helm requires certain chart metadata being available in `Chart.yaml`. In addition, for charts published by Giant Swarm, we have certain metadata restrictions.

On this page the goal is to document the requriements for all chart metadata and provide some context for each field, and explain to application users the meaning of metadata properties. We also show how these properties are represented in OCI registries.

## Background

Historically, Giant Swarm distributed charts via HTTP repositories. In addition, we used proprietary top-level keys in `Chart.yaml` (`restrictions`).

Since late 2025, we publish charts in OCI registries, and HTTP based repositories are being phased out. The metadata schema described here is targeting OCI registries and aims to be compliant with the [OpenContainers Annotation Spec](https://specs.opencontainers.org/image-spec/annotations/). Former proprietary top-level keys in `Chart.yaml` are migrated to annotations.

On this page, we mention the old metadata keys as "legacy". Our CI/CD pipeline makes sure to translate between the legacy and the OCI-compliant annotation keys.

## Examples

The following `Chart.yaml` example includes required and recommended properties only:

```yaml
annotations:
  io.giantswarm.application.audience: all
  io.giantswarm.application.managed: "true"
  io.giantswarm.application.team: shield
apiVersion: v2
description: Keeps things secure at runtime
home: https://github.com/giantswarm/security-guard
icon: https://s.giantswarm.io/app-icons/1/png/security-guard-light.svg
name: security-guard
keywords:
  - security
  - containers
version: "3.2.1"
```

A more complex example:

```yaml
annotations:
  io.giantswarm.application.audience: all
  io.giantswarm.application.managed: "true"
  io.giantswarm.application.team: cabbage
  io.giantswarm.application.app-type: cluster
  io.giantswarm.application.upstream-chart-version: "1.1.27"
  io.giantswarm.application.upstream-chart-url: https://example.com/charts/great-connector/
  io.giantswarm.application.restrictions.cluster-singleton: "true"
  io.giantswarm.application.restrictions.fixed-namespace: "false"
  io.giantswarm.application.restrictions.compatible-providers: "aws,azure"
apiVersion: v2
appVersion: "1.26.3"
description: Connects everything with everything else
home: https://github.com/giantswarm/great-connector
icon: https://s.giantswarm.io/app-icons/1/png/great-connector-light.svg
name: great-connector
keywords:
  - networking
version: "2.3.1"
```

## Chart.yaml properties {#properties}

See [the Helm docs](https://helm.sh/docs/topics/charts/#the-chartyaml-file) for any optional properties defined by the Helm project.

Some terminology for this overview:

- **REQUIRED**: Every chart must have this property defined.
- **RECOMMENDED**: For good quality, customer experience etc., this property should be defined.
- **OPTIONAL**: Can be present and might increase the customer experience, to be decided case by case.
- **Legacy Chart.yaml key** key used previously in `Chart.yaml` files authered by Giant Swarm.

### annotations {#annotations}

**REQUIRED** annotations object. See below for required keys and their meaning. Annotation values must be of type string.

All annotations listed here are also represented in OCI repositories where charts get pushed to by the Giant Swarm CI/CD pipeline. In particular, they become part of the "config" manifest, which is a representation of the `Chart.yaml` content. In addition, the annotations are made available in the manifest of each repository.

#### io.giantswarm.application.audience {#io.giantswarm.application.audience}

**REQUIRED** if the chart `type` is not specified or `application`, otherwise (`type: library`) not recommended.

Indicates who is encouraged to deploy and use this application.

The value `all` means that the application is for everyone, including Giant Swarm customers. `giantswarm` means that the app is built for Giant Swarm internal purposes, not to be used by customers.

#### io.giantswarm.application.managed {#io.giantswarm.application.managed}

**REQUIRED** if the chart `type` is not specified or `application`, otherwise (`type: library`) not recommended.

Indicates whether Giant Swarm is responsible for operating the application. The value `true` indicates that Giant Swarm takes responsibility in general. `false` means that customers deploying the application are responsible for operating it.

#### io.giantswarm.application.team {#io.giantswarm.application.team}

**REQUIRED** Short form of the Giant Swarm product team that owns the application. Example: "honeybadger"

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/team`

#### io.giantswarm.application.app-type {#io.giantswarm.application.app-type}

OPTIONAL application type indicator. Value can be `bundle` or `cluster`.

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/app-type`

#### io.giantswarm.application.two-step-install {#io.giantswarm.application.two-step-install}

OPTIONAL Instructs chart-operator to deploy this chart in two steps, if value is "true". This allows for deploying CRDs in the first step, and then CRs using these CRDs in the second step.

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/two-step-install`

#### io.giantswarm.application.readme {#io.giantswarm.application.readme}

URL to the application readme file.

Example: `https://raw.githubusercontent.com/giantswarm/hello-world-app/refs/tags/v1.2.3/examples/README.md`

This annotation is added automatically by the CI/CD pipeline with a value specific for each release. It must not be present in Chart.yaml.

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/readme`

#### io.giantswarm.application.values-schema {#io.giantswarm.application.values-schema}

URL to the application's values.yaml JSON schema.

Example: `https://raw.githubusercontent.com/giantswarm/hello-world-app/refs/tags/v1.2.3/examples/apps/hello-world-app/values.schema.json`

This annotation is added automatically by the CI/CD pipeline with a value specific for each release. It must not be present in Chart.yaml.

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/values-schema`

#### io.giantswarm.application.upstream-chart-version {#io.giantswarm.application.upstream-chart-version}

OPTIONAL if the chart is based on an upstream chart, this shows the original chart version.

Example: `1.2.3`

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/upstream-chart-version`

#### io.giantswarm.application.upstream-chart-url {#io.giantswarm.application.upstream-chart-url}

OPTIONAL if the chart is based on an upstream chart, this shows the original chart URL.

Example: `https://github.com/giantswarm/hello-world-app`

Legacy Chart.yaml key: `annotations` / `application.giantswarm.io/upstream-chart-url`

#### io.giantswarm.application.restrictions.cluster-singleton {#io.giantswarm.application.restrictions.cluster-singleton}

OPTIONAL Indicates that the application can be installed only once per cluster. Can be `true` or `false`.

Legacy Chart.yaml key: `restrictions` / `clusterSingleton`

#### io.giantswarm.application.restrictions.fixed-namespace {#io.giantswarm.application.restrictions.fixed-namespace}

OPTIONAL Namespace the application must be installed into.

Example: `helloworld`

Legacy Chart.yaml key: `restrictions` / `fixedNamespace`

#### io.giantswarm.application.restrictions.gpu-instances {#io.giantswarm.application.restrictions.gpu-instances}

OPTIONAL Indicate whether the application requires GPU nodes. Can be `true` or `false`.

Legacy Chart.yaml key: `restrictions` / `gpuInstances`

#### io.giantswarm.application.restrictions.namespace-singleton {#io.giantswarm.application.restrictions.namespace-singleton}

OPTIONAL Indicates that the application can be installed only once per namespace. Can be `true` or `false`.

Legacy Chart.yaml key: `restrictions` / `namespaceSingleton`

#### io.giantswarm.application.restrictions.compatible-providers {#io.giantswarm.application.restrictions.compatible-providers}

OPTIONAL List of infrastructure providers the application is compatible with. Multiple provider names must be separated with comma.

Example: `azure,aws`

Legacy Chart.yaml key: `restrictions` / `compatibleProviders`

#### io.giantswarm.ui.logo {#io.giantswarm.ui.logo}

OPTIONAL URL of a logo with landscape aspect ratio.

Legacy Chart.yaml key: `annotations` / `ui.giantswarm.io/logo`

### apiVersion

**REQUIRED** Specify the helm chart schema version. The recommended value is `v2`.

### appVersion

**RECOMMENDED** Version of the packaged application. If the chart repository is also the application's source repository, this can be omitted, as it would be identical with `version`.

Example: `0.3.0`

### description

**REQUIRED** A short text that explains the purpose of the application.

Example: `Connects things and keeps things secure`

### home

**REQUIRED** URL of the source repository of this chart.

Example: `https://github.com/giantswarm/hello-world-app`

### icon

**RECOMMENDED** Icon URL.

Example: `https://s.giantswarm.io/app-icons/1/png/hello-world-app-light.svg`

Icons are supposed to get displayed in user interfaces inside square-shaped container, so the aspect ratio is expected to be near a square.

### keywords

**RECOMMENDED** List of keywords to associate with the chart. These are used in user interfaces as search and filter criteria.

Example: `[networking, webapp]`

TODO: Add information about how to align keyword usage throughout applications.

### name

**REQUIRED** Name of the chart.

Example: `hello-world`

Character set: `[a-z0-9-]`. See [chart name best-practices](https://v3.helm.sh/docs/chart_best_practices/conventions#chart-names).

### version

**REQUIRED** Semantic version of the chart.

Example: `2.9.1`

## Additional OCI annotations

The listing above shows which metadata annotations are expected from Chart.yaml. This sections now is for additional annotations we expect in OCI artifact manifests for charts.

### org.opencontainers.image.created {#org.opencontainers.image.created}

Date and time of creation of the artifact. helm push sets this to the current date automatically when pushing.
