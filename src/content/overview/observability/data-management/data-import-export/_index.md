---
title: Data import and export
diataxis_content_type: explanation
description: Understand how the Giant Swarm observability platform lets external systems send data in and read data out through the Observability Platform API.
weight: 50
mermaid: true
menu:
  principal:
    parent: overview-observability-data-management
    identifier: overview-observability-data-management-data-import-export
last_review_date: 2025-10-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How can I access observability data externally?
  - How do I send data from external sources to the platform?
  - How do I connect external tools to the platform?
  - What is the Observability Platform API?
---

Data import and export let you send observability data from external sources into the Giant Swarm platform and read your observability data from external systems and tools. This gives you the flexibility to integrate the platform with your existing monitoring infrastructure, external data sources, and specialized analysis tools.

This page explains the concepts behind import and export. When you're ready to act:

- **[Import data]({{< relref "/overview/observability/data-management/data-import-export/import" >}})**: send metrics, logs, and traces from external sources into the platform.
- **[Export data]({{< relref "/overview/observability/data-management/data-import-export/export" >}})**: connect external Grafana or custom tools to read platform data.
- **[Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api" >}})**: the endpoints, authentication, and tenant values both directions use.

If your data originates inside a Giant Swarm managed cluster, use [data ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}) instead. Import and export cover the case where the data source or consumer lives outside the platform.

## Why import and export data

Import and export open up integration possibilities that a self-contained platform can't offer on its own.

Importing external data lets you:

- **Bring in external sources**: send logs and events from SaaS applications, databases, or other infrastructure that Giant Swarm doesn't manage.
- **Correlate across platforms**: combine data from multiple environments in a single observability stack.
- **Integrate legacy systems**: pull data from existing monitoring tools during migrations or for hybrid deployments.
- **Collect from third parties**: gather observability data from external services, APIs, or cloud providers.

Exporting platform data lets you:

- **Reuse existing tools**: connect your own Grafana instances, dashboards, or business intelligence tools.
- **Run specialized analysis**: feed advanced analytics tools, machine learning platforms, or custom applications with your observability data.
- **Keep extra copies**: archive observability data for compliance or long-term analysis.
- **Support multi-cloud strategies**: centralize observability data from multiple cloud providers.

## How import and export work

The Observability Platform API provides both data import (sending data to the platform) and data export (reading data from the platform) through a unified, secure interface. It's the primary mechanism for both directions, and it works from anywhere, not only from within Giant Swarm managed clusters.

### Architecture overview

The API is reached through a shared host based on your installation's base domain (`https://observability.<domain_name>`). Requests authenticate through your identity provider (OIDC) and carry a tenant scope so that each caller only reaches the data they're allowed to see.

{{< mermaid >}}
graph TB
  subgraph external ["External Systems"]
    A[External Alloy Instance]
    B[External Grafana]
    C[Custom Applications]
  end

  subgraph ingress ["Observability Platform Ingresses"]
    D["nginx-ingress<br/>observability.domain"]
    E["oauth2-proxy<br/>Authentication Handler"]
  end

  subgraph backend ["Backend Services"]
    G["Grafana Mimir<br/>Metrics Storage"]
    H["Grafana Loki<br/>Log Storage"]
    I["Grafana Tempo<br/>Trace Storage"]
  end

  subgraph auth ["Authentication"]
    J["OIDC Provider<br/>Azure AD / Google / Okta"]
  end

  %% Data Import Flow
  A -->|"Metrics: Prometheus Remote Write<br/>Logs: Loki Push API<br/>Traces: OTLP HTTP"| D
  C -->|"Direct API Calls<br/>with OIDC Token"| D

  %% Data Export Flow
  B -->|"Query APIs<br/>Forward OAuth Identity"| D

  %% Internal Flow
  D -->|"Route to auth handler"| E
  E -->|"Validate Token"| J
  E -->|"Authenticated + X-Scope-OrgID"| G
  E -->|"Authenticated + X-Scope-OrgID"| H
  E -->|"Authenticated + X-Scope-OrgID"| I

  %% Styling
  classDef external fill:#e1f5fe
  classDef ingress fill:#fff3e0
  classDef backend fill:#f3e5f5
  classDef auth fill:#e8f5e8

  class A,B,C external
  class D,E ingress
  class G,H,I backend
  class J auth
{{< /mermaid >}}

### Authentication and tenant scoping

Every import and export request combines two things: a valid OIDC token that proves who you are, and an `X-Scope-OrgID` header that names the tenant you want to reach. Your identity must have access to that tenant, and the tenant must exist in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}). Requests for tenants that don't exist are rejected. This is the same multi-tenant isolation the platform applies internally, so external callers never gain broader access than internal ones.

For the exact header names, token format, and the list of tenant values, see the [Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api" >}}).

## Security and compliance

Import and export maintain the same security standards as the internal platform:

- **End-to-end encryption**: all data transfer uses TLS.
- **Identity-based access**: access integrates with your organization's OIDC provider.
- **Tenant isolation**: the multi-tenant architecture keeps data separated.
- **Audit trails**: the platform logs all data access requests for compliance.

## Performance considerations

Both directions consume platform resources, so it helps to understand where the cost sits.

Import volume drives storage and processing needs. High-frequency streams and large payloads consume more ingestion capacity, and every tenant importing data shares the same ingestion resources. Export cost tracks query complexity instead: broad time ranges, intensive filters, and many concurrent exports all compete for the same query capacity.

The import and export how-to guides list concrete best practices (batching, rate limiting, query scoping) for keeping this impact low.

## Next steps

- **[Import data]({{< relref "/overview/observability/data-management/data-import-export/import" >}})**: configure external sources to send data to the platform.
- **[Export data]({{< relref "/overview/observability/data-management/data-import-export/export" >}})**: connect external tools to read platform data.
- **[Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api" >}})**: endpoints, authentication, and tenant values.
- **[Data ingestion]({{< relref "/overview/observability/data-management/data-ingestion/" >}})**: send data from inside a Giant Swarm managed cluster.
- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: understand how tenants isolate observability data.
