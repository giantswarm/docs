---
title: Import data into the observability platform
linkTitle: Import data
diataxis_content_type: how-to-guide
description: Send metrics, logs, and traces from external sources into the Giant Swarm observability platform using Grafana Alloy or the platform's HTTP APIs.
weight: 10
menu:
  principal:
    parent: overview-observability-data-management-data-import-export
    identifier: overview-observability-data-management-data-import-export-import
last_review_date: 2025-10-20
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I import data into the observability platform?
  - How do I send data from external sources to the platform?
  - How do I configure Grafana Alloy to forward data to the platform?
  - How do I configure OAuth2 authentication for external data import?
---

This guide shows you how to send metrics, logs, and traces from external sources into the Giant Swarm observability platform. Use it when the data originates outside a Giant Swarm managed cluster, for example from a SaaS application, an external database, or another cloud environment. For the concepts behind import, see [data import and export]({{< relref "/overview/observability/data-management/data-import-export" >}}). To send data from inside a managed cluster, use [data ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}) instead.

## Prerequisites

Before you import data, make sure you have:

1. **OIDC provider configured**: work with Giant Swarm to set up identity provider integration.
2. **A tenant**: create or identify the tenant where your external data should be stored. The tenant must exist in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}).
3. **Network access**: your external systems must be able to reach `https://observability.<domain_name>`.
4. **The API enabled**: the Observability Platform API must be enabled for your installation. Contact your Account Engineer to configure the authentication endpoints.

The platform accepts data through standard observability APIs. For the full list of endpoints and the authentication headers they expect, see the [Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api" >}}).

## Grafana Alloy configuration (recommended)

You can send data directly through API calls, but we recommend using [Grafana Alloy](https://grafana.com/oss/alloy-opentelemetry-collector/). It gives you a robust, configurable way to collect and forward data with built-in authentication and error handling.

The following configuration handles metrics, logs, and traces, with shared OAuth2 credentials across all three:

```alloy
// ============================================================================
// OAuth2 Authentication (shared across all components)
// ============================================================================

// Shared OAuth2 configuration for metrics
prometheus.remote_write "to_observability_platform" {
  endpoint {
    url = "https://observability.<your-domain>/prometheus/api/v1/push"
    oauth2 {
      client_id     = "<client_id>"
      client_secret = "<client_secret>"
      scopes        = ["<required_scopes>"]
      token_url     = "<oidc_provider_token_url>"
    }
    headers = {
      "X-Scope-OrgID" = "<tenant_id>"
    }
  }
}

// Shared OAuth2 configuration for logs
loki.write "to_observability_platform" {
  endpoint {
    url = "https://observability.<your-domain>/loki/api/v1/push"
    oauth2 {
      client_id     = "<client_id>"
      client_secret = "<client_secret>"
      scopes        = ["<required_scopes>"]
      token_url     = "<oidc_provider_token_url>"
    }
    headers = {
      "X-Scope-OrgID" = "<tenant_id>"
    }
  }
}

// Shared OAuth2 configuration for traces
otelcol.auth.oauth2 "observability_platform" {
  client_id     = "<client_id>"
  client_secret = "<client_secret>"
  token_url     = "<oidc_provider_token_url>"
  scopes        = ["<required_scopes>"]
}


// Export traces to observability platform
otelcol.exporter.otlphttp "observability_platform" {
  client {
    endpoint = "https://observability.<your-domain>/tempo"
    auth     = otelcol.auth.oauth2.observability_platform.handler
    headers = {
      "X-Scope-OrgID" = "<tenant_id>"
    }
  }
}
```

Replace the placeholders with your own values:

- `<your-domain>`: your observability platform domain.
- `<client_id>`, `<client_secret>`: OAuth2 credentials provided by your Account Engineer.
- `<oidc_provider_token_url>`: your OIDC provider's token endpoint URL.
- `<required_scopes>`: OAuth2 scopes required by your OIDC provider.
- `<tenant_id>`: target tenant for data routing. It must exist in a Grafana Organization.

The [Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api#oidc-provider-examples" >}}) lists the `token_url` and `scopes` values for common OIDC providers such as Azure AD, Google, Okta, and Keycloak.

## Setup process

Roll out import in stages so you can catch configuration problems early:

1. **Plan your data sources**: identify which external systems will send data to the platform.
2. **Configure authentication**: work with Giant Swarm to set up OIDC integration for your data sources.
3. **(Optional) Enable tracing**: for trace import, ensure tracing is enabled for your cluster.
4. **Set up tenants**: create the [Grafana Organizations]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}) for your external data.
5. **Test ingestion**: send sample data to verify connectivity and formatting.
6. **Deploy at scale**: run your chosen import method in production.
7. **Monitor ingestion**: track data volume and verify data is being processed correctly.

## Best practices

Keep the platform's ingestion load manageable:

- **Batch events**: send data in appropriately sized batches rather than individual events.
- **Rate-limit the client**: apply client-side rate limiting so you don't overwhelm the platform.
- **Filter early**: send only relevant data and pre-filter unnecessary logs or events.
- **Compress payloads**: use compressed payloads where supported to reduce transfer time.

## Next steps

- **[Export data]({{< relref "/overview/observability/data-management/data-import-export/export" >}})**: read platform data from external tools.
- **[Observability Platform API reference]({{< relref "/overview/observability/data-management/data-import-export/observability-platform-api" >}})**: endpoints, authentication, and tenant values.
- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: set up the tenants your imported data routes to.
