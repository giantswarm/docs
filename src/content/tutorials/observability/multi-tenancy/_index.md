---
title: Multi-tenancy
description: Understanding multi-tenancy concepts and best practices for the Observability Platform.
weight: 20
menu:
  principal:
    parent: tutorials-observability
    identifier: tutorials-observability-multitenancy
last_review_date: 2025-06-11
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How to isolate data in the observability platform?
  - What are tenant separation best practices?
  - How do tenants and organizations work together?
---

The observability platform supports multi-tenancy to help you isolate data and control access across different teams, environments, or projects. This guide explains the core concepts and best practices for implementing tenant separation.

## Understanding multi-tenancy

Multi-tenancy works through three key components:

### Tenants

A **tenant** is a logical namespace that isolates observability data (metrics, logs) in the backend storage systems (Mimir and Loki). When applications send (or retrieve) data, they include a tenant label that determines where the information goes (or is fetched from).

**Key characteristics:**

- Data isolation at the storage level
- Independent retention policies and limits
- Separate query scope for dashboards and alerts

### Grafana organizations

A **Grafana organization** gives you access to specific tenants through dedicated datasources. Each organization is a separate workspace in Grafana with its own:

- User roles and permissions
- Dashboards and folders
- Datasource configurations for alerts, metrics and logs

### RBAC groups

**RBAC groups** from your identity provider (like Active Directory or OAuth) define which users get access to specific Grafana organizations and their permission levels.

## Tenant separation strategies

Choose the right strategy based on your needs:

### By environment

Separate tenants by deployment environment:

```yaml
tenants:
- production
- staging  
- development
```

**Use case:** Keep dev/staging data separate from production, apply different retention policies.

### By team or department

Organize tenants around teams:

```yaml
tenants:
- platform-team
- frontend-team
- backend-team
- data-team
```

**Use case:** Give teams ownership of their data, enable self-service monitoring.

### By service or application

Create separation at the service level:

```yaml
tenants:
- user-service
- payment-service
- notification-service
- analytics-service
```

**Use case:** Microservices where each service team manages their own monitoring.

### Hybrid approach

Combine strategies using consistent naming:

```yaml
tenants:
- prod-frontend
- prod-backend
- staging-frontend
- staging-backend
```

**Use case:** Balance granular control with manageable complexity.

## Tenant naming best practices

Follow these guidelines when choosing tenant names:

### Naming requirements

Tenant names must follow [Grafana Mimir tenant ID restrictions](https://grafana.com/docs/mimir/latest/configure/about-tenant-ids/):

- Alphanumeric characters (a-z, A-Z, 0-9) and special characters (!, -, _, ., *, ', (, ))
- Between 1 and 150 characters
- Can't use: `.`, `..`, `__mimir_cluster`

### Recommended patterns

**Environment-based:** `production`, `staging`, `development`

**Team-based:** `platform-team`, `frontend-team`, `backend-team`

**Service-based:** `user-service`, `payment-service`, `notification-service`

**Hybrid:** `prod-frontend`, `stage-backend`, `dev-notifications`

## Access control patterns

### Organization-to-tenant mapping

Map Grafana organizations to tenants based on your access needs:

#### One-to-one mapping

```yaml
# Platform Team Organization
tenants:
- platform-team
```

**Best for:** Complete team isolation, clear ownership.

#### One-to-many mapping

```yaml
# Engineering Organization
tenants:
- frontend-team
- backend-team
- platform-team
```

**Best for:** Cross-team collaboration, shared dashboards.

### RBAC role assignment

Assign roles based on user needs:

```yaml
rbac:
  admins:
  - customer:platform-admin      # Full access to organization
  editors:
  - customer:senior-engineer     # Can create/edit dashboards and alerts
  viewers:
  - customer:junior-engineer     # Read-only access to dashboards
```

## Data governance

### Tenant governance

The platform automatically enforces tenant governance to control data ingestion:

- **Valid tenants:** Only tenants referenced in at least one `GrafanaOrganization` can receive data
- **Data rejection:** Data sent to unlisted tenants gets dropped automatically
- **Shared access:** Multiple organizations can reference the same tenant for shared datasets

⚠️ **Important:** Removing a tenant from all organizations immediately stops data ingestion for that tenant. Data is stored until it expires.

### Tenant lifecycle management

**Creating tenants:**

1. Define the tenant in `GrafanaOrganization` resource (see [documentation]({{< relref "creating-grafana-organization" >}}))
2. Configure data collection to use tenant label (see [Data Ingestion documentation]({{< relref "/tutorials/observability/data-ingestion" >}}))
3. Verify data appears in organization dashboards (see [Data Exploration documentation]({{< relref "/tutorials/observability/data-exploration" >}}))

**Removing tenants:**

1. Stop sending data to the tenant
2. Wait for retention period to expire
3. Remove tenant from all `GrafanaOrganization` resources

## Next steps

- [Create a Grafana organization]({{< relref "creating-grafana-organization" >}}) to implement your tenant strategy
- [Configure alerting]({{< relref "/tutorials/observability/alerting" >}}) with tenant-specific rules
- [Set up data ingestion]({{< relref "/tutorials/observability/data-ingestion" >}}) to send data to your tenants
- [Explore your data]({{< relref "/tutorials/observability/data-exploration" >}}) using Grafana dashboards and queries
