---
title: Chart metadata reference
linkTitle: Chart metadata
description: Helm charts maintained by Giant Swarm require certain chart metadata. This page explains which fields are requires and recommended, and for what purpose. We also show how chart metadadat is represented in OCC registries.
menu:
  principal:
    identifier: reference-platform-api-chartmetadata
    parent: reference-platform-api
last_review_date: 2025-11-28
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What metadata is required in Chart.yaml?
  - How is chart metadata represented in OCI registries?
---

Helm requires certain chart metadata being available in `Chart.yaml`. In addition, for charts published by Giant Swarm, we have certain metadata restrictions.

On this page the goal is to document the requriements for all chart metadata and provide some context for each field, and explain to application users the meaning of metadata properties. We also show how these properties are represented in OCI registries.

## Example {#example}

The following `Chart.yaml` example includes required and recommended properties only.

```yaml
annotations:
  application.giantswarm.io/team: shield
apiVersion: v2
description: Connects things and keeps things secure
home: https://github.com/giantswarm/awesome-application
icon: https://s.giantswarm.io/app-icons/1/png/awesome-application-light.svg
name: awesome-application
keywords:
  - security
  - networking
version: "2.3.1"
```

## Chart.yaml properties {#properties}

See [the Helm docs](https://helm.sh/docs/topics/charts/#the-chartyaml-file) for any optional properties defined by the Helm project.

Some terminology for this overview:

- **REQUIRED**: Every chart must have this property defined.
- **RECOMMENDED**: For good quality, customer experience etc., this property should be defined.
- **OPTIONAL**: Can be present and might increase the customer experience, to be decided case by case.
- **OCI annotation key** when given indicates how the respective field or annotation is represented in an OCI repository annotation.

## annotations {#annotations}

**REQUIRED** annotations object. See below for required keys and their meaning. Annotation values must be strings.

### application.giantswarm.io/audience

**REQUIRED** Indicates who is encouraged to deploy and use this application.

The value `all` means that the application is for everyone, including Giant Swarm customers. `giantswarm` means that the app is built for Giant Swarm internal purposes, not to be used by customers.

### application.giantswarm.io/managed

**REQUIRED** Indicates whether Giant Swarm is responsible for operating the application. The value `true` indicates that Giant Swarm takes responsibility in general. `false` means that customers deploying the application are responsible for operating it.

### application.giantswarm.io/team

**REQUIRED** Short form of the Giant Swarm product team that owns the application. Example: "honeybadger"

OCI annotation key: `io.giantswarm.application.team`

### application.giantswarm.io/app-type

OPTIONAL application type. TODO: Explain. Value can be `bundle` or `cluster`.

### application.giantswarm.io/metadata

Added automatically by the CI/CD pipelinefor compatibility with HTTP registries. Will be removed when they are no longer needed.

Example: `http://example.com/hello-world-app-1.2.3.tgz-meta/main.yaml`

### application.giantswarm.io/readme

URL to the application readme file.

Example: `https://raw.githubusercontent.com/giantswarm/hello-world-app/refs/tags/v1.2.3/examples/README.md`

This annotation is added automatically by the CI/CD pipeline with a value specific for each release. It must not be present in Chart.yaml.

### application.giantswarm.io/values-schema

URL to the application's values.yaml JSON schema.

Example: `https://raw.githubusercontent.com/giantswarm/hello-world-app/refs/tags/v1.2.3/examples/apps/hello-world-app/values.schema.json`

This annotation is added automatically by the CI/CD pipeline with a value specific for each release. It must not be present in Chart.yaml.

### application.giantswarm.io/upstream-chart-version

OPTIONAL if the chart is based on an upstream chart, this shows the original chart version.

Example: `1.2.3`

### application.giantswarm.io/upstream-chart-url

OPTIONAL if the chart is based on an upstream chart, this shows the original chart URL.

Example: `https://github.com/giantswarm/hello-world-app`

### application.giantswarm.io/restrictions/cluster-singleton

OPTIONAL Boolean to indicate that the application can be installed only once per cluster.

Example: `"true"`

### application.giantswarm.io/restrictions/fixed-namespace

OPTIONAL Namespace the application must be installed into.

Example: `helloworld`

### application.giantswarm.io/restrictions/gpu-instances

OPTIONAL Boolean to indicate whether the application requires GPU nodes.

Example: `"false"`

### application.giantswarm.io/restrictions/namespace-singleton

OPTIONAL Boolean to indicate that the application can be installed only once per namespace.

Example: `"true"`

### application.giantswarm.io/restrictions/compatible-providers

OPTIONAL List of infrastructure providers the application is compatible with. Multiple provider names must be separated with comma.

Example: `azure,aws`

### ui.giantswarm.io/logo

OPTIONAL Logo image URL. In contrast to the icon, the logo is meant for display in a larger rectangular space and is displayed larger than the icon, so it can be more details. An example would be the combination of a logo and the wordmark.

We added this annotation specifically for our web UI (happa), which is deprecated, and we currently have no plans to use it in the new UI based on Backstage.

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

## OCI artifact metadata

This sections describes the metadata we expect in manifests of OCI artifacts for charts.

All metadata from the chart as described above is expected to land in the OCI repository as the `config` resource.

In addition, we rely on the following key of the main artifact manifest.

### Annotation org.opencontainers.image.created

Date and time of creation of the artifact. helm push sets this to the current date automatically when pushing.
