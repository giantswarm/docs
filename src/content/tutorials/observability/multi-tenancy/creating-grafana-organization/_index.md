---
linkTitle: Creating a Grafana organization
title: Creating a Grafana organization
description: Guide explaining how to manage Grafana organizations in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-multitenancy-create-grafana-organization
    parent: tutorials-observability-multitenancy
weight: 40
last_review_date: 2025-03-05
user_questions:
  - How to create a grafana organization?
  - How to access multi-tenant observability data?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

When you first log in to [your installation's `Grafana`]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}), you see the preselected `Grafana` organization called `_Shared Org_`. This shared organization contains a curated set of managed dashboards accessible to everyone with `Grafana` access. 

If multiple teams access the observability platform, we recommend using multi-tenancy for data and dashboard isolation. The observability platform lets you create new organizations in self-service for this use case.

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

Our operators will create this `Grafana` organization named _MyOnlineShop_. The system equips it with a basic set of data sources for Loki, Mimir and Alertmanager, giving you access to the `myonlineshop` tenant.

## RBAC Configuration

The Role Based Access Control (RBAC) section defines how to assign groups from your configured identity provider to `Grafana` [organization roles](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/#organization-roles) (`Admin`, `Editor`, `Viewer`). 

### Dex Connector Format

Most Giant Swarm installations use Dex as the identity provider. When using Dex, specify groups using the format `{dex-connector-id}:{group-name}`. For example:

- `customer:platform-admin` - Maps the `platform-admin` group from the `customer` Dex connector to Grafana Admin role
- `customer:development-team` - Maps the `development-team` group from the `customer` Dex connector to Grafana Editor role

You can find your Dex connector ID in your cluster's Dex configuration. Only the `admins` field is mandatory in the RBAC section.

For more details about organization mapping, see the official Grafana [OAuth documentation](https://grafana.com/docs/grafana/next/setup-grafana/configure-security/configure-authentication/generic-oauth/#configure-role-mapping).

## Tenant Governance

The tenant field grants access to specified tenants and serves as tenant governance. The system only accepts tenants listed in **at least one** Grafana Organisation CRD as valid targets in the write path. 

Key points about tenant governance:

- Tenants must exist in at least one `GrafanaOrganization` to receive data
- The system drops data sent to tenants not listed in any `GrafanaOrganization` CRD
- Multiple organizations can reference the same tenant for shared access

**Warning:** Removing a tenant from **all** Grafana Organisation CRDs also means you can no longer send data to that tenant!
