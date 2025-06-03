---
linkTitle: Creating a Grafana organization
title: Creating a Grafana organization
description: Guide explaining how to manage Grafana organizations in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-multitenancy-create-grafana-organization
    parent: tutorials-observability-multitenancy
weight: 40
last_review_date: 2025-06-03
user_questions:
  - How to create a grafana organization?
  - How to access multi-tenant observability data?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

When you first log in to [your installation's `Grafana`]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}), you see the preselected `Grafana` organization called `_Shared Org_`. This shared organization contains a curated set of managed dashboards available to everyone with `Grafana` access.

If multiple teams access the observability platform, you should take advantage of multi-tenancy to isolate data and dashboards. The observability platform lets you create new organizations in self-service for this use case.

## Understanding tenants and organizations

Before creating your organization, it's important to understand the relationship between **tenants**, **organizations**, and **RBAC groups**:

- **Tenant**: A logical namespace that isolates observability data (metrics, logs) in the backend storage systems (Mimir and Loki). When applications send data or telemetry agents collect data, they include a tenant label that determines which data partition the information goes to.

- **Grafana Organization**: A Grafana construct that groups users and provides access to specific datasources and dashboards. Each organization acts as a separate workspace within Grafana.

- **RBAC Groups**: Identity provider groups (like those from your company's Active Directory or OAuth provider) that define user permissions and roles.

### How they work together

The data flow works as follows:

1. **Data Collection**: Your clusters collect metrics and logs through applications and telemetry agents. These agents then send data to backend systems (Mimir, Loki) with a specific tenant identifier
2. **Organization Mapping**: Grafana organizations are configured to access specific tenants
3. **User Access**: RBAC groups from your identity provider are mapped to organization roles (Admin, Editor, Viewer)

This architecture does:

- Isolate data between different teams or environments
- Control who can view, edit, or manage specific datasets
- Share data across multiple organizations when needed

## Creating your own organization

To add a new `Grafana` organization, create a [`GrafanaOrganization`](https://raw.githubusercontent.com/giantswarm/observability-operator/refs/heads/main/config/crd/observability.giantswarm.io_grafanaorganizations.yaml) custom resource in the management cluster.

For example:

```yaml
apiVersion: observability.giantswarm.io/v1alpha1
kind: GrafanaOrganization
metadata:
  name: myonlineshop
spec:
  displayName: MyOnlineShop
  rbac:
    admins:
    - customer:platform-admin
    - customer:ops-team
    editors:
    - customer:development-team
    - customer:devops-team
    viewers:
    - customer:marketing-team
    - customer:business-analysts
  tenants:
  - myonlineshop
```

This configuration creates:

- **Grafana Organization**: A new organization named "MyOnlineShop" in Grafana
- **Data Access**: Access to observability data stored within the `myonlineshop` tenant
- **User Permissions**: Role assignments based on your identity provider groups
- **Datasources**: Automatic provisioning of Loki, Mimir, and Alertmanager datasources filtered to the `myonlineshop` tenant

## RBAC configuration

The Role Based Access Control (RBAC) section defines how to assign groups from your configured identity provider to `Grafana` [organization roles](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/#organization-roles) (`Admin`, `Editor`, `Viewer`).

### Dex connector format

Most Giant Swarm installations use Dex as the identity provider. When using Dex, specify groups using the format `{dex-connector-id}:{group-name}`. For example:

- `customer:platform-admin` - Maps the `platform-admin` group from the `customer` Dex connector to Grafana Admin role
- `customer:development-team` - Maps the `development-team` group from the `customer` Dex connector to Grafana Editor role

You can find your Dex connector ID in your cluster's Dex configuration. Only the `admins` field is mandatory in the RBAC section.

For more details about organization mapping, see the official Grafana [OAuth documentation](https://grafana.com/docs/grafana/next/setup-grafana/configure-security/configure-authentication/generic-oauth/#configure-role-mapping).

## Tenant governance

The `tenants` field in your `GrafanaOrganization` serves two purposes:

1. **Access Control**: Grants the organization access to data from the specified tenants
2. **Tenant Governance**: Acts as a safeguard mechanism in the observability platform, preventing collectors from pushing to an invalid tenant.

### How tenant governance works

The observability platform implements tenant governance by only accepting data for tenants that belong to **at least one** `GrafanaOrganization` resource. This means:

- **Valid tenants**: Only tenants referenced in existing `GrafanaOrganization` resources can receive data
- **Data rejection**: The system drops data sent to tenants not listed in any `GrafanaOrganization` resource
- **Shared access**: Multiple organizations can reference the same tenant, allowing shared access to the same dataset

**Warning:** Removing a tenant from **all** `GrafanaOrganization` resources means you can no longer send data to that tenant. Make sure at least one organization references any tenant you want to keep active.
