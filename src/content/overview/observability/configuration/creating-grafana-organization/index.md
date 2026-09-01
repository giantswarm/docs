---
linkTitle: Creating a Grafana organization
title: Creating a Grafana organization
diataxis_content_type: how-to-guide
description: Step-by-step guide to create and configure Grafana organizations for multi-tenant observability.
menu:
  principal:
    identifier: overview-observability-configuration-grafana-org
    parent: overview-observability-configuration
weight: 40
last_review_date: 2026-07-08
user_questions:
  - How to create a Grafana organization?
  - How to configure RBAC for Grafana organizations?
  - How to assign tenants to organizations?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
aliases:
  - /tutorials/observability/multi-tenancy/creating-grafana-organization/
  - /overview/observability/configuration/multi-tenancy/creating-grafana-organization/
---

This guide walks you through creating and configuring Grafana organizations to implement [multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy" >}}) in your observability platform.

## Prerequisites

Before creating your organization, make sure you have:

- [Access to the management cluster]({{< relref "/tutorials/access-management" >}}), where you can create custom resources
- Identified the [tenant names]({{< relref "/overview/observability/configuration/multi-tenancy#tenant-naming-best-practices" >}}) you want to use
- Configured groups for RBAC in your identity provider

## Understanding default organizations

Before creating your own organizations, it's helpful to know about the two that already exist:

- **Shared Org**: Your starting point with system dashboards and platform metrics (uses `giantswarm` tenant)
- **Giant Swarm**: Internal organization for platform operations (Giant Swarm staff only)

Your organizations will appear alongside the `Shared Org` in the organization dropdown. Learn more about these in our [multi-tenancy overview]({{< relref "/overview/observability/configuration/multi-tenancy#default-organizations" >}}).

## Creating a GrafanaOrganization resource

Create a [`GrafanaOrganization`]({{< relref "/reference/platform-api/crd/grafanaorganizations.observability.giantswarm.io" >}}) custom resource in the management cluster:

### Basic example

This example shows a simple organization for a single application with role-based access for different teams:

{{< tabs >}}
{{< tab title="v1alpha2 (Recommended)" active="true" >}}

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
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
  - name: myonlineshop
    types:
    - data
    - alerting
```

{{< /tab >}}
{{< tab title="v1alpha1" >}}

> **Deprecated**: v1alpha1 is deprecated. Please use v1alpha2 for new resources.

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

{{< /tab >}}
{{< /tabs >}}

### Configuration options

| Field | Description | Required |
|-------|-------------|----------|
| `metadata.name` | Kubernetes resource name (follows DNS naming rules) | Yes |
| `spec.displayName` | Human-readable name shown in Grafana UI | Yes |
| `spec.rbac.admins` | Groups with full organization access | Yes |
| `spec.rbac.editors` | Groups that can create/edit dashboards and alerts | No |
| `spec.rbac.viewers` | Groups with read-only access | No |
| `spec.tenants` | List of tenant configurations this organization can access | Yes |

### Advanced examples

**Multi-environment organization:**

This example demonstrates an organization that manages multiple environments with hierarchical access control:

{{< tabs >}}
{{< tab title="v1alpha2 (Recommended)" active="true" >}}

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: GrafanaOrganization
metadata:
  name: engineering-team
spec:
  displayName: Engineering Team
  rbac:
    admins:
    - customer:engineering-leads
    editors:
    - customer:senior-engineers
    - customer:devops-team
    viewers:
    - customer:junior-engineers
    - customer:qa-team
  tenants:
  - name: prod-frontend
    types:
    - data
    - alerting
  - name: prod-backend
    types:
    - data
    - alerting
  - name: staging-frontend
    types:
    - data
  - name: staging-backend
    types:
    - data
```

{{< /tab >}}
{{< tab title="v1alpha1" >}}

> **Deprecated**: v1alpha1 is deprecated. Please use v1alpha2 for new resources.

```yaml
apiVersion: observability.giantswarm.io/v1alpha1
kind: GrafanaOrganization
metadata:
  name: engineering-team
spec:
  displayName: Engineering Team
  rbac:
    admins:
    - customer:engineering-leads
    editors:
    - customer:senior-engineers
    - customer:devops-team
    viewers:
    - customer:junior-engineers
    - customer:qa-team
  tenants:
  - prod-frontend
  - prod-backend
  - staging-frontend
  - staging-backend
```

{{< /tab >}}
{{< /tabs >}}

**Production-only organization:**

This example shows a restricted organization with access only to production data:

{{< tabs >}}
{{< tab title="v1alpha2 (Recommended)" active="true" >}}

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: GrafanaOrganization
metadata:
  name: production-monitoring
spec:
  displayName: Production Monitoring
  rbac:
    admins:
    - customer:sre-team
    - customer:platform-admin
    viewers:
    - customer:engineering-team
    - customer:support-team
  tenants:
  - name: production
    types:
    - data
    - alerting
```

{{< /tab >}}
{{< tab title="v1alpha1" >}}

> **Deprecated**: v1alpha1 is deprecated. Please use v1alpha2 for new resources.

```yaml
apiVersion: observability.giantswarm.io/v1alpha1
kind: GrafanaOrganization
metadata:
  name: production-monitoring
spec:
  displayName: Production Monitoring
  rbac:
    admins:
    - customer:sre-team
    - customer:platform-admin
    viewers:
    - customer:engineering-team
    - customer:support-team
  tenants:
  - production
```

{{< /tab >}}
{{< /tabs >}}

**Granular access control (v1alpha2 only):**

With `v1alpha2`, you can specify different access types for fine-grained control:

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: GrafanaOrganization
metadata:
  name: mixed-access-org
spec:
  displayName: Mixed Access Organization
  rbac:
    admins:
    - customer:platform-admin
    editors:
    - customer:ops-team
    viewers:
    - customer:read-only-team
  tenants:
  # Full access (data and alerting)
  - name: critical-services
    types:
    - data
    - alerting
  # Data access only (no alerting)
  - name: development-metrics
    types:
    - data
  # Alerting access only
  - name: alerting-management
    types:
    - alerting
```

## RBAC configuration

The RBAC section maps identity provider groups to [Grafana organization roles](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/#organization-roles):

| Role | Permissions |
|------|-------------|
| **Admin** | Full organization access: manage users, datasources, dashboards, and settings |
| **Editor** | Create and edit dashboards, alerts, and folders (can't manage users) |
| **Viewer** | Read-only access to dashboards and data |

### Group format

Most Giant Swarm installations use Dex as the identity provider. Specify groups using the format `{dex-connector-id}:{group-name}`:

```yaml
rbac:
  admins:
  - customer:platform-admin        # Maps 'platform-admin' group from 'customer' connector
  - customer:ops-team
  editors:
  - customer:development-team
  viewers:
  - customer:support-team
```

**Finding your connector ID:** Check your cluster's Dex configuration for the connector ID (usually `customer`).

**Required fields:** `admins` is mandatory. `editors` and `viewers` are optional.

## Migrating from v1alpha1 to v1alpha2

If you have existing `v1alpha1` organizations, see [migrate Grafana organizations to v1alpha2]({{< relref "/overview/observability/configuration/migrate-grafana-organizations" >}}) for the differences between the versions, conversion examples, and migration best practices. New resources should use `v1alpha2` directly.

## What happens when you create an organization

Creating a `GrafanaOrganization` resource automatically provisions:

1. **New Grafana organization** with your specified display name
2. **Tenant-scoped datasources** for Loki, Mimir, and Alertmanager
3. **User role assignments** based on your RBAC configuration
4. **Data collection** of alerts, logs, metrics, and traces

## Verification steps

After creating your organization:

1. **Check organization status:**

   ```bash
   kubectl get grafanaorganization myonlineshop -o yaml
   ```

2. [**Log in to Grafana**]({{< relref "/overview/observability/data-management/data-exploration/" >}}) and verify:

- The organization dropdown menu on the top-left corner shows all expected organizations

![Switching organization](./organization_switching.png)

- You can [explore and query data]({{< relref "/overview/observability/data-management/data-exploration/" >}}) for each of your tenants
- Logged-in users have appropriate role assignments under the `Administration / Users and access / Users` section
