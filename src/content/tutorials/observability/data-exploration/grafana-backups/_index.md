---
linkTitle: Grafana backups
title: Creating and using grafana backups
description: Guide explaining how to create and use grafana backups in the Observability Platform for disaster recovery.
menu:
  principal:
    identifier: tutorials-observability-data-exploration-grafana-backups
    parent: tutorials-observability-data-exploration
weight: 40
last_review_date: 2025-04-07
user_questions:
  - How to create grafana backups?
  - How to recover grafana data after a disater?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
---

We operate a PostgreSQL cluster as a Grafana database storing your data. To ensure the availability of this stored data, especially in a disaster, backups need to be created to retrieve the data afterward. We are already creating backups by default, but if you want to add your own, you will find here how to do it.

## Creating grafana backups

There are two ways to create backups for the PostgreSQL database :

- __Scheduled backups__ : You can define a `ScheduledBackup` resource in the management cluster. This is the preferred approach as it allows you to automate backups and have those done regularly. Here is an example of such a resource :

```yaml
apiVersion: postgresql.cnpg.io/v1
kind: ScheduledBackup
metadata:
  name: scheduled-backup-example
spec:
  schedule: "0 0 0 * * *"
  backupOwnerReference: self
  cluster:
    name: my-pg-cluster
```

The `schedule` field is a cron schedule specification, so you can define it the same way you would for a cronjob. The `cluster.name` field designates the PostgreSQL cluster from which you want to create a backup.

- __Manual backups__ : If you need to create a backup outside of the scheduled time from the `ScheduledBackup` resources, you can create a `Backup` resource. This will create a backup from the targeted PostgreSQL cluster as soon as it gets deployed and reconciled by the PostgreSQL operator. Check the example of such a resource :

```yaml
apiVersion: postgresql.cnpg.io/v1
kind: Backup
metadata:
  name: backup-example
spec:
  cluster:
    name: my-pg-cluster
```

## Disaster recovery

Our engineers handle the disaster recovery process as soon as they are notified.
