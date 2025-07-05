---
title: Multi-tenancy concepts
description: Understand how multi-tenancy works in the Giant Swarm observability platform to isolate data and control access across teams and environments.
weight: 10
menu:
  principal:
    parent: overview-observability-configuration-multi-tenancy
    identifier: overview-observability-configuration-multi-tenancy-concepts
last_review_date: 2025-06-30
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - What is multi-tenancy in the observability platform?
  - How do tenants and organizations work?
  - Why is data isolation important?
  - What are the benefits of multi-tenant observability?
  - How to isolate data in the observability platform?
  - What are tenant separation best practices?
  - How do tenants and organizations work together?
  - What are the tenant naming requirements?
  - How do I create and manage tenants?
---

Multi-tenancy in the Giant Swarm observability platform provides secure data isolation and access controls, enabling multiple teams, environments, or projects to share the same observability infrastructure while maintaining clear boundaries around their data and access permissions.

This architectural approach provides secure data access controls for authorized users. It also delivers the operational efficiency of a shared platform.

## Core concepts

Multi-tenancy works through three key components:

- Tenants
- Grafana organizations
- RBAC groups


### What is a tenant

A **tenant** is a logical namespace that isolates observability data at the storage level in both Mimir (metrics) and Loki (logs). Think of it as a secure container for your data that ensures complete separation from other tenants' information.

Key characteristics of tenants:

- **Data isolation**: Metrics and logs are completely separated at the storage level
- **Independent policies**: Each tenant can have its own retention periods and resource limits
- **Query boundaries**: Dashboards and alerts can only access data within authorized tenants
- **Flexible organization**: Tenants can represent teams, environments, services, or any logical grouping

### What is a Grafana organization

A **Grafana organization** is your workspace within the observability platform that provides access to specific tenants through dedicated datasources. Each organization functions as an independent environment with its own users, dashboards, and configurations.

Key characteristics of organizations:

- **Access control**: Define which users can access which tenants and data
- **User management**: Assign roles and permissions within the organization
- **Resource organization**: Manage dashboards, folders, and datasources independently
- **Multiple tenant access**: One organization can access multiple tenants for cross-team collaboration

### RBAC groups

**RBAC groups** from your identity provider (like Active Directory or OAuth) define which users get access to specific Grafana organizations and their permission levels. These groups bridge your existing organizational structure with observability platform access controls.

### The relationship between tenants and organizations

The multi-tenancy model creates a flexible mapping between data storage (tenants) and access control (organizations):

![Multi-tenancy Architecture](../multi-tenancy-architecture.png)

**Key relationships shown in the diagram:**

- **Organizations** (left) authenticate with the **Data Access Layer** (middle) using their assigned permissions
- **Data Access Layer** enforces RBAC controls and routes queries to authorized **Data Tenants** (right)
- **Platform Team** has admin access through the data access layer to multiple environment tenants (`production`, `staging`, `development`)
- **Frontend Team** has editor access through the data access layer to their specific tenant (`frontend-prod`)
- **Shared Organization** provides read-only access (dashed line) to production data for broader visibility
- **Two-stage security**: Organizations cannot directly access tenants. The Data Access Layer mediates and controls all access

This architecture enables:

- **Flexible access patterns**: Multiple organizations can access the same tenant for collaboration
- **Granular permissions**: Control what data each user can see within and across organizations
- **Scalable administration**: Manage access and data organization independently

## Multi-tenancy benefits

### Security and compliance

- **Data isolation**: Sensitive data remains separate between tenants
- **Access controls**: Fine-grained permissions guarantee users see only authorized data
- **Audit trails**: Clear visibility into who accessed what data and when
- **Compliance support**: Meet regulatory requirements for data separation and access logging

### Operational efficiency

- **Shared infrastructure**: Reduce costs by sharing observability platform components
- **Centralized management**: Single platform for all observability needs across teams
- **Resource optimization**: Efficient use of storage and compute resources across tenants
- **Consistent tooling**: Unified interfaces and workflows for all users

### Team autonomy

- **Self-service monitoring**: Teams can manage their own dashboards and alerts independently
- **Customizable environments**: Teams can tailor each organization to specific needs
- **Independent workflows**: Teams can work without interfering with each other's configurations
- **Collaborative access**: Share data across teams when needed while maintaining boundaries

## Common multi-tenancy patterns

Organizations typically implement multi-tenancy using one or more of these patterns:

### Environment-based separation

Isolate data by deployment environments to prevent cross-environment data leakage and apply different retention policies.

- Examples: `production`, `staging`, `development`
- Use case: Operational separation with different SLAs and access requirements

### Team-based separation

Organize tenants around organizational structure to enable team ownership and self-service monitoring.

- Examples: `platform-team`, `frontend-team`, `backend-team`
- Use case: Independent team operations with clear data ownership

### Service-based separation

Create tenant boundaries at the application or service level for microservices architectures.

- Examples: `user-service`, `payment-service`, `notification-service`
- Use case: Service ownership with independent monitoring and alerting

### Hybrid approaches

Combine multiple patterns for complex organizational needs while maintaining manageable complexity.

- Examples: `prod-frontend`, `staging-backend`, `dev-platform`
- Use case: Balance granular control with operational simplicity

### Finding the right balance

Getting the number of tenants right is tricky:

- Too few and you lose isolation benefits
- Too many and management becomes complex, making it harder to see the full picture (correlation across services becomes difficult)

**Finding balance:**

- Start with broad tenants like `production`, `staging`, `development`
- Split only when teams actually step on each other's toes
- Ask "will this split help solve a real problem we have today?"
- You can always add more tenants later - start simple

## Tenant naming requirements

Tenant names must follow [Grafana Alloy identifier rules](https://github.com/grafana/alloy/blob/main/syntax/scanner/identifier.go):

- Must start with a letter (a-z, A-Z) or underscore (_)
- After the first character, can contain letters (a-z, A-Z), digits (0-9), or underscores (_)
- Cannot contain spaces or special characters (other than underscore)
- Between 1 and 150 characters
- Cannot use `__mimir_cluster` (reserved by the platform)

**Recommended patterns:**

- **Environment-based:** `production`, `staging`, `development`
- **Team-based:** `platform_team`, `frontend_team`, `backend_team`
- **Service-based:** `user_service`, `payment_service`, `notification_service`
- **Hybrid:** `prod_frontend`, `stage_backend`, `dev_notifications`

## Built-in organizations

Every Giant Swarm installation includes two pre-configured organizations:

### Shared organization

Provides immediate access to platform monitoring with curated dashboards and system-wide observability data. All users receive read-only access by default, enabling instant visibility into cluster health and system metrics.

### Giant Swarm organization

Reserved for Giant Swarm operations team to monitor platform health and provide customer support. This organization is not visible to customers and contains internal operational dashboards.

## Data governance and lifecycle

The observability platform automatically enforces data governance to maintain security and operational integrity:

- **Tenant validation**: The platform stores only data sent to explicitly defined tenants; the system rejects invalid tenant data
- **Access enforcement**: Users can only query data from tenants associated with their authorized organizations
- **Retention management**: Each tenant can have independent data retention policies
- **Resource limits**: Platform-level controls prevent any single tenant from overwhelming shared resources

### Tenant governance

The platform automatically enforces tenant governance to control data ingestion:

- **Valid tenants:** Only tenants referenced in at least one `GrafanaOrganization` can receive data
- **Data rejection:** The system automatically drops data sent to unlisted tenants
- **Shared access:** Multiple organizations can reference the same tenant for shared datasets

⚠️ **Important:** Removing a tenant from all organizations immediately stops data ingestion for that tenant. The platform stores data until the retention period expires.

### Tenant lifecycle management

**Creating tenants:**

1. Define the tenant in `GrafanaOrganization` resource
2. Configure data collection to use tenant label (see [Data Ingestion documentation]({{< relref "/tutorials/observability/data-ingestion" >}}))
3. Verify data appears in organization dashboards (see [Data Exploration documentation]({{< relref "/tutorials/observability/data-exploration" >}}))

**Removing tenants:**

1. Stop sending data to the tenant
2. Remove tenant from all `GrafanaOrganization` resources (the platform retains data until the retention period expires)

## Learn more

**Next steps to implement multi-tenancy:**

- **Organization creation**: Create Grafana organizations to implement your tenant strategy
- **Data ingestion**: Configure [data collection]({{< relref "/tutorials/observability/data-ingestion" >}}) to send data to your tenants
- **Data exploration**: [Explore your data]({{< relref "/tutorials/observability/data-exploration" >}}) using Grafana dashboards and queries
- **Alerting**: Set up [tenant-specific alerting]({{< relref "/tutorials/observability/alerting" >}}) rules and notifications

**External resources:**

- **Grafana documentation**: Explore [Grafana's organization management](https://grafana.com/docs/grafana/latest/administration/organization-management/) for additional context

The multi-tenancy design provides a foundation for secure, scalable observability that grows with your organization while maintaining clear boundaries and access controls.
