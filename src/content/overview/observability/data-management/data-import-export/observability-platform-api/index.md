---
title: Observability Platform API reference
linkTitle: Observability Platform API
diataxis_content_type: reference
description: Reference for the Giant Swarm Observability Platform API, covering import and export endpoints, authentication headers, tenant values, and OIDC provider settings.
weight: 30
menu:
  principal:
    parent: overview-observability-data-management-data-import-export
    identifier: overview-observability-data-management-data-import-export-observability-platform-api
last_review_date: 2025-10-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What endpoints does the Observability Platform API expose?
  - Which authentication headers does the API require?
  - Which tenant value should I use for platform data?
  - What token URL and scopes do common OIDC providers need?
---

This page documents the interface of the Giant Swarm Observability Platform API. It covers the import and export endpoints, the authentication headers, the tenant values you can target, and the settings common OIDC providers need. For task-oriented steps, see [import data]({{< relref "/overview/observability/data-management/data-import-export/import" >}}) and [export data]({{< relref "/overview/observability/data-management/data-import-export/export" >}}).

## Availability

The API must be enabled for your installation before use. Contact your Account Engineer to configure the authentication endpoints. It's reached through a shared host based on your installation's base domain: `https://observability.<domain_name>`.

## Authentication

Every request, in either direction, requires two things:

| Requirement | How to provide it |
|-------------|-------------------|
| **Identity** | A valid OIDC token in the `Authorization: Bearer <token>` header |
| **Tenant scope** | An `X-Scope-OrgID` header naming an existing tenant |

Your identity must have access to the specified tenant, and the tenant must exist in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}). Requests that target a tenant which doesn't exist are rejected.

## Import endpoints

The platform accepts data through these standard observability APIs:

| Signal | Protocol | Endpoint |
|--------|----------|----------|
| Metrics | Prometheus remote write | `https://observability.<domain>/prometheus/api/v1/push` |
| Logs | Loki push API | `https://observability.<domain>/loki/api/v1/push` |
| Traces | OTLP HTTP | `https://observability.<domain>/tempo` (when tracing is enabled) |

## Export endpoints

The platform exposes these query APIs, each compatible with the upstream project's API:

| Signal | Compatible with | Base endpoint |
|--------|-----------------|---------------|
| Logs | Loki query API | `https://observability.<domain>` |
| Metrics | Prometheus query API | `https://observability.<domain>/prometheus` |
| Traces | Tempo query API | `https://observability.<domain>/tempo` (when tracing is enabled) |

## Supported data types

The platform supports importing and exporting all three observability signals:

| Signal | Availability | Examples |
|--------|--------------|----------|
| **Logs and events** | Import and export | Application logs, Kubernetes events, audit logs, external service logs |
| **Traces** | Import and export (when tracing is enabled) | Distributed traces, application spans, external service traces, platform traces |
| **Metrics** | Import and export | Infrastructure metrics, application metrics, platform metrics, external system metrics |

## Tenant values

Choose the tenant value based on the data you want to reach:

| Data type | Tenant value | Description |
|-----------|--------------|-------------|
| Platform logs | `giantswarm` | System and infrastructure logs |
| Platform metrics | `giantswarm` | System and infrastructure metrics |
| Platform traces | `giantswarm` | System and infrastructure traces |
| Custom logs | Your tenant | Logs from your applications |
| Custom metrics | Your tenant | Metrics from your applications |
| Custom traces | Your tenant | Traces from your applications |

## OIDC provider examples

When you configure a client (for example [Grafana Alloy]({{< relref "/overview/observability/data-management/data-import-export/import#grafana-alloy-configuration-recommended" >}})), set the `token_url` and `scopes` to match your OIDC provider:

| Provider | `token_url` | `scopes` |
|----------|-------------|----------|
| Azure AD | `https://login.microsoftonline.com/<tenant>/oauth2/v2.0/token` | `["<client_id>/.default", "openid", "email", "profile"]` |
| Google | `https://oauth2.googleapis.com/token` | `["openid", "email", "profile"]` |
| Okta | `https://<domain>.okta.com/oauth2/default/v1/token` | `["openid", "email", "profile"]` |
| Keycloak | `https://<keycloak-domain>/realms/<realm>/protocol/openid-connect/token` | `["openid", "email", "profile"]` |

The `client_id` and `client_secret` are provided by your Account Engineer.

## See also

- [Import data]({{< relref "/overview/observability/data-management/data-import-export/import" >}}): send external data into the platform.
- [Export data]({{< relref "/overview/observability/data-management/data-import-export/export" >}}): read platform data from external tools.
- [Data import and export]({{< relref "/overview/observability/data-management/data-import-export" >}}): the concepts behind the API.
