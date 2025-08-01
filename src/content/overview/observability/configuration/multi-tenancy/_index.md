---
title: Multi-tenancy
description: Learn how to set up and manage multi-tenancy in the Giant Swarm observability platform.
weight: 10
menu:
  principal:
    parent: overview-observability-configuration
    identifier: overview-observability-configuration-multi-tenancy
last_review_date: 2025-07-17
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is multi-tenancy in observability?
  - How do I create and manage tenants?
  - How does access control work?
  - How do I map Grafana organizations to tenants?
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

## Default organizations

Every Giant Swarm installation comes with two built-in Grafana organizations:

### Shared Org

- **Purpose**: Contains curated dashboards and system-wide observability data
- **Access**: Available to all users with Grafana access in read-only mode
- **Content**: Managed dashboards for platform monitoring, cluster health, and system metrics

When you first log into Grafana, you'll see the Shared Org selected by default. This gives you immediate access to platform monitoring without needing to create your own organization first.

**Need different access?** If you want to restrict Shared Org access to specific groups or give certain users editor permissions, contact your account engineer. They can help configure custom access controls.

### Giant Swarm

- **Purpose**: Internal organization for Giant Swarm operations and platform management
- **Access**: Restricted to Giant Swarm staff only
- **Content**: Operational dashboards and internal monitoring tools

**Note**: You won't see the Giant Swarm organization in the dropdown as a customer - it's only visible to Giant Swarm staff for our internal operations.

## Tenant separation strategies

Choose the right strategy based on your needs:

### By environment

Separate tenants by deployment environment:

```yaml
- production
- staging
- development
```

**Use case:** Keep dev/staging data separate from production, apply different retention policies.

### By team or department

Organize tenants around teams:

```yaml
- platform_team
- frontend_team
- backend_team
- data_team
```

**Use case:** Give teams ownership of their data, enable self-service monitoring.

### By service or application

Create separation at the service level:

```yaml
- user_service
- payment_service
- notification_service
- analytics_service
```

**Use case:** Microservices where each service team manages their own monitoring.

### Hybrid approach

Combine strategies using consistent naming:

```yaml
- prod_frontend
- prod_backend
- staging_frontend
- staging_backend
```

**Use case:** Balance granular control with manageable complexity.

### Finding the right balance

Getting the number of tenants right is tricky:

- too few and you lose isolation benefits.
- too many and management becomes a headache and it is hard to see the full picture (for instance it may be harder to correlation customer requests with CPU usage across services).

**Finding balance:**

- Start with broad tenants like `production`, `staging`, `development`
- Split only when teams actually step on each other's toes
- Ask "will this split help solve a real problem we have today?"
- You can always add more tenants later - start simple

## Tenant naming best practices

Follow these guidelines when choosing tenant names:

### Naming requirements

Tenant names must follow [Grafana Alloy identifier rules](https://github.com/grafana/alloy/blob/main/syntax/scanner/identifier.go):

- Must start with a letter (a-z, A-Z) or underscore (_)
- After the first character, can contain letters (a-z, A-Z), digits (0-9), or underscores (_)
- Cannot contain spaces or special characters (other than underscore)
- Between 1 and 150 characters
- Cannot use `__mimir_cluster` (reserved by the platform)

### Recommended patterns

**Environment-based:** `production`, `staging`, `development`

**Team-based:** `platform_team`, `frontend_team`, `backend_team`

**Service-based:** `user_service`, `payment_service`, `notification_service`

**Hybrid:** `prod_frontend`, `stage_backend`, `dev_notifications`

## Data governance

### Tenant governance

The platform automatically enforces tenant governance to control data ingestion:

- **Valid tenants:** Only tenants referenced in at least one `GrafanaOrganization` can receive data
- **Data rejection:** Data sent to unlisted tenants gets dropped automatically
- **Shared access:** Multiple organizations can reference the same tenant for shared datasets

⚠️ **Important:** Removing a tenant from all organizations immediately stops data ingestion for that tenant. Data is stored until the retention period expires.

### Tenant lifecycle management

**Creating tenants:**

1. Define the tenant in `GrafanaOrganization` resource (see [documentation]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization" >}}))
2. Configure data collection to use tenant label (see [Data Ingestion documentation]({{< relref "/overview/observability/data-management/data-ingestion" >}}))
3. Verify data appears in organization dashboards (see [Data Exploration documentation]({{< relref "/overview/observability/data-management/data-exploration/" >}}))

**Removing tenants:**

1. Stop sending data to the tenant

## Next steps

- [Create a Grafana organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization" >}}) to implement your tenant strategy
- [Configure alert management]({{< relref "/overview/observability/alert-management" >}}) with tenant-specific rules
- [Set up data ingestion]({{< relref "/overview/observability/data-management/data-ingestion" >}}) to send data to your tenants
- [Explore your data]({{< relref "/overview/observability/data-management/data-exploration/" >}}) using Grafana dashboards and queries
