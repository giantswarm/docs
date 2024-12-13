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

When you first access [your installations `Grafana`]({{< relref "/tutorials/observability/data-exploration/accessing-grafana" >}}), you will be accessing an organization named _Shared Org_, which gives you access to a set of curated dashboards. However, if you want to provide multi-tenancy of your observability data (isolation between tenants), the observability platform allows you to create your own organizations in self-service.

## Creating your own organization

To create your own Grafana organization, you can create a [`GrafanaOrganization`](https://raw.githubusercontent.com/giantswarm/observability-operator/refs/heads/main/config/crd/observability.giantswarm.io_grafanaorganizations.yaml) custom resource in the management cluster containing the Grafana organization specification.

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
    - giantswarm-admins
    editors:
    - giantswarm-editors
    viewers:
    - giantswarm-viewers
  tenants:
  - giantswarm
```

This Grafana organization will be created by our operators with the name _Giant Swarm_.
It will be equipped with a basic set of datasources for Loki, Mimir and Alertmanager giving you access to the _giantswarm_ tenant.
The RBAC section defines how to map your sso groups to grafana admin roles (Admin, Editor, Viewer). Note that only admins is mandatory in this section.
