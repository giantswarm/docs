---
linkTitle: Creating a Grafana organization
title: Creating a Grafana organization
description: Guide explaining how to manage Grafana organizations in the Observability Platform.
menu:
  principal:
    identifier: tutorials-observability-multitenancy-create-grafana-organization
    parent: tutorials-observability-multitenancy
weight: 40
last_review_date: 2024-12-12
user_questions:
  - How to create a grafana organization?
  - How to access multi-tenant observability data?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

When you first access [your installation's `Grafana`]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}), you will be accessing an organization named _Shared Org_, which gives you access to a set of curated dashboards. However, if you want to provide multi-tenancy of your observability data (isolation between tenants), the observability platform allows self-service creation of your own organizations.

## Creating your own organization

To add a new `Grafana` organization, create a [`GrafanaOrganization`](https://raw.githubusercontent.com/giantswarm/observability-operator/refs/heads/main/config/crd/observability.giantswarm.io_grafanaorganizations.yaml) custom resource in the management cluster.

For example:

```yaml
apiVersion: observability.giantswarm.io/v1alpha1
kind: GrafanaOrganization
metadata:
  name: giantswarm
spec:
  displayName: Giant Swarm
  rbac:
    admins:
    - organization-admins
    editors:
    - dashboards-maintainers
    viewers:
    - data-readers
  tenants:
  - giantswarm
```

Our operators will create this `Grafana` organization named _Giant Swarm_. It will be equipped with a basic set of data sources for Loki, Mimir and Alertmanager, giving you access to the `giantswarm` tenant.

The Role Base Access Control (RBAC) section defines how to assign groups from your configured identity provider to `Grafana` [predefined roles](https://grafana.com/docs/grafana/latest/administration/roles-and-permissions/#organization-roles) (`Admin`, `Editor`, `Viewer`). organization mapping, you can read the official Grafana [documentation](https://grafana.com/docs/grafana/next/setup-grafana/configure-security/configure-authentication/generic-oauth/#configure-role-mapping).
Note that only the `admins` field is mandatory in this section.
