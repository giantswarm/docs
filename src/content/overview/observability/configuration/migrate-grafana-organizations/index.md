---
title: Migrate Grafana organizations to v1alpha2
linkTitle: Migrate organizations to v1alpha2
diataxis_content_type: how-to-guide
description: How to migrate GrafanaOrganization resources from the v1alpha1 to the v1alpha2 API version on the Giant Swarm observability platform.
weight: 45
menu:
  principal:
    parent: overview-observability-configuration
    identifier: overview-observability-configuration-migrate-grafana-organizations
last_review_date: 2026-07-08
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I migrate a GrafanaOrganization from v1alpha1 to v1alpha2?
  - What is the difference between v1alpha1 and v1alpha2 tenants?
  - How does automatic conversion of GrafanaOrganization resources work?
  - How do I set granular tenant access when migrating?
---

This guide shows you how to migrate your [`GrafanaOrganization`]({{< relref "/reference/platform-api/crd/grafanaorganizations.observability.giantswarm.io" >}}) resources from the `v1alpha1` to the `v1alpha2` API version. The `v1alpha2` version introduces structured tenant configuration with granular access control. Existing `v1alpha1` resources keep working through automatic conversion, but migrating lets you take advantage of the new features. For creating organizations in the first place, see [creating a Grafana organization]({{< relref "/overview/observability/configuration/creating-grafana-organization" >}}).

## Key differences

| Aspect | v1alpha1 | v1alpha2 |
|--------|----------|----------|
| **Tenant format** | Simple strings | Structured objects with name and types |
| **Access control** | All-or-nothing | Granular (data vs alerting) |
| **Migration** | Manual updates needed | Automatic conversion available |

## Migration examples

**Basic tenant migration:**

```yaml
# v1alpha1 format
spec:
  tenants:
  - "my-app"
  - "production"
  - "staging"

# v1alpha2 equivalent (full access)
spec:
  tenants:
  - name: "my-app"
    types:
    - data
    - alerting
  - name: "production"
    types:
    - data
    - alerting
  - name: "staging"
    types:
    - data
    - alerting
```

**Taking advantage of granular access control:**

```yaml
# v1alpha2 with different access levels
spec:
  tenants:
  # Production: full access (data and alerting)
  - name: "production"
    types:
    - data
    - alerting
  # Development: metrics and logs only (no alerting)
  - name: "dev-metrics"
    types:
    - data
  # Staging: metrics and logs only
  - name: "staging"
    types:
    - data
  # Alert management: alerting functionality only
  - name: "alert-config"
    types:
    - alerting
```

## Access types explained

- **`data`**: Provides access to metrics and logs data sources (Mimir and Loki) in Grafana
- **`alerting`**: Provides access to alerting functionality and alert management (Alertmanager) in Grafana

You can specify both types for full access, or use them separately for restricted access based on your security requirements.

## Automatic migration behavior

When you update existing `v1alpha1` resources, they're automatically converted to `v1alpha2`:

- Each tenant string is converted to a `TenantConfig` object
- The `name` field is set to the original tenant string
- The `types` field defaults to `["data", "alerting"]` (full access)

## Migration best practices

1. **Test first**: Validate your v1alpha2 configuration in a non-production environment
2. **Review access**: Use the migration as an opportunity to review and refine tenant access permissions
3. **Roll out gradually**: Migrate one organization at a time to ensure smooth transitions
4. **Monitor impact**: Verify that users retain appropriate access after migration
5. **Use granular access**: Take advantage of the new access types to implement the principle of least privilege

## See also

- [Creating a Grafana organization]({{< relref "/overview/observability/configuration/creating-grafana-organization" >}}): create and configure organizations
- [GrafanaOrganization CRD reference]({{< relref "/reference/platform-api/crd/grafanaorganizations.observability.giantswarm.io" >}}): the full resource schema
- [Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}}): how tenants isolate observability data
