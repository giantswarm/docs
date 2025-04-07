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

We are operating a postgresql cluster as a grafana database on which is stored all grafana data. In order to ensure the availability of this stored data, especially in case of disaster, backups need to be created so that the data can be retrieved afterwards. We are already creating backups by default but if you want to add your own, you will find here how to do it.

## Creating grafana backups

There are 2 ways to create backups for the grafana postgresql database :

- __Scheduled backups__ : you can define a `ScheduledBackup` resource in the k8S cluster in which you will define when will backup be created. This is the preferred approach as it allows you to automate backups and have those done on a regular basis. Here is an example of such a resource :

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

The `schedule` field is a cron schedule specification so you can define it the same way you would for a cronjob.
The `cluster.name` field designates the postgresql cluster you want to create a backup from.

- __Manual backups__ : if for any reason you need to create a backup outside of the scheduled time from the ScheduledBackups resources, you can create a `Backup` resource. This will create a backup from the targeted postgresql cluster as soon as it gets deployed and reconciled by the postgresql operator. here is an example of such a resource :

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

The whole disaster recovery process is handled by Giant Swarm engineers as soon as they get notified.
