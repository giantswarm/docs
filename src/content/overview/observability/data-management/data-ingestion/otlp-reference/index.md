---
title: OTLP ingestion reference
linkTitle: OTLP ingestion reference
diataxis_content_type: reference
description: Reference for OpenTelemetry Protocol (OTLP) ingestion on the Giant Swarm observability platform, covering gateway endpoints, ports, SDK environment variables, and tenant routing.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-ingestion
    identifier: overview-observability-data-management-data-ingestion-otlp-reference
last_review_date: 2026-07-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What OTLP endpoints does the observability platform expose?
  - Which ports does the OTLP gateway use?
  - Which OpenTelemetry SDK environment variables should I set?
  - How is OTLP data routed to a tenant?
  - What is the X-Scope-OrgID header used for in OTLP ingestion?
---

This page describes the OpenTelemetry Protocol (OTLP) ingestion interface of the Giant Swarm Observability Platform. It documents the gateway endpoints and ports, the SDK environment variables the platform recognizes, and how OTLP data is routed to a tenant.

For the task-oriented steps to configure an application to send data, see the [data ingestion guide]({{< relref "/overview/observability/data-management/data-ingestion" >}}).

## Availability

OTLP ingestion is available in alpha from cluster release v31 and fully supported from v33. It must be enabled for your installation before use. Request it through your Account Engineer. Data sent to a tenant that doesn't exist is dropped.

## Gateway endpoints

Each cluster runs a local OTLP gateway (`otlp-gateway.kube-system.svc`) that accepts metrics, logs, and traces and forwards them to central storage.

| Protocol | Endpoint | Port |
|----------|----------|------|
| OTLP/gRPC | `otlp-gateway.kube-system.svc:4317` | `4317` |
| OTLP/HTTP | `http://otlp-gateway.kube-system.svc:4318` | `4318` |

## SDK environment variables

Applications are configured with the [standard OpenTelemetry SDK environment variables](https://opentelemetry.io/docs/specs/otel/configuration/sdk-environment-variables/#general-sdk-configuration). The variables the platform relies on most often:

| Variable | Description |
|----------|-------------|
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP gateway endpoint (for example `http://otlp-gateway.kube-system.svc:4318`) |
| `OTEL_EXPORTER_OTLP_HEADERS` | Additional headers to send with each export; used to set `X-Scope-OrgID` (see [tenant routing](#tenant-routing)) |
| `OTEL_METRICS_EXPORTER` | Set to `otlp` to enable metrics export |
| `OTEL_LOGS_EXPORTER` | Set to `otlp` to enable log export |
| `OTEL_TRACES_EXPORTER` | Set to `otlp` to enable trace export (usually the SDK default) |
| `OTEL_RESOURCE_ATTRIBUTES` | Resource attributes such as `service.name`, `deployment.environment` |
| `OTEL_TRACES_SAMPLER` | Trace sampling strategy (for example `always_on`, `parentbased_always_on`) |
| `OTEL_TRACES_SAMPLER_ARG` | Additional arguments for the sampler |

## Tenant routing

OTLP data is routed to a [tenant]({{< relref "/overview/observability/configuration/multi-tenancy" >}}) using one of two mechanisms:

| Mechanism | Applies to | How to set it |
|-----------|-----------|---------------|
| `X-Scope-OrgID` HTTP header | OTLP/HTTP (port 4318) | Set via the `OTEL_EXPORTER_OTLP_HEADERS` environment variable, for example `X-Scope-OrgID=my_tenant` |
| `observability.giantswarm.io/tenant` pod label | OTLP/gRPC and OTLP/HTTP | Add the label to the pods sending OTLP data |

When both are present, the `X-Scope-OrgID` header takes precedence over the pod label.

## See also

- [Data ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}): how to configure applications to send metrics, logs, and traces
- [Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}}): how tenants isolate observability data
