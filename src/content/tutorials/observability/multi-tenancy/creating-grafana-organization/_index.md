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

At the initial log in to [your installation's `Grafana`]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}) the preselected `Grafana` organization is the so called `_Shared Org_`. This shared organization contains a curated set of managed dashboards that are accessible to everyone with access to `Grafana`. If multiple teams access the observability platform we recommend to work with multi-tenancy and the resulting isolation of data and dashboards. For this use case the observability platform allows you to create new organizations in self-service.

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
    - platform-team
    editors:
    - development-team
    viewers:
    - marketing-team
  tenants:
  - myonlineshop
```

Our operators will create this `Grafana` organization named _Giant Swarm_. It will be equipped with a basic set of data sources for Loki, Mimir and Alertmanager, allowing you access to the `myonlineshop` tenant.

The Role Base Access Control (RBAC) section defines how to assign groups from your configured identity provider to `Grafana` [available roles](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/#organization-roles) (`Admin`, `Editor`, `Viewer`). For organization mapping, you can read the official Grafana [documentation](https://grafana.com/docs/grafana/next/setup-grafana/configure-security/configure-authentication/generic-oauth/#configure-role-mapping).
Note that only the `admins` field is mandatory in this section.

The tenant field is used to grant access to the specified tenants, but also serves as tenant governance. This means that only tenants listed in **at least one** Grafana Organisation CRD are accepted targets in the write path and can receive data. Data sent to a tenant that is not listed in any Grafana Organisation CRDs tenant field will just be dropped. 

**Warning:** Removing a tenant from **all** Grafana Organisation CRDs tenant fields also means, that you can no longer send data to that tenant! 
