---
linkTitle: Audit logging
title: Audit logging
description: A guide explaining how to interact with audit logs on Giant Swarm clusters.
weight: 50
menu:
  main:
    identifier: getting-started-observability-logs-auditlogging
    parent: getting-started-observability-logs
user_questions:
  - What are audit logs?
  - What is audit logging?
  - How can I access Kubernetes audit logs?
  - How do I ship audit logs to a remote locations?
aliases:
  - /ui-api/observability/logs/audit-logging
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2023-01-30
---

In this document you will learn what are audit logs, which kind is available on Giant Swarm clusters and how to access / ship them to a remote location.

__Warning:__ This feature and the documentation is quite new, so do not hesitate to ask for support or help us improve this documentation.

## Audit logs

TODO: Brief summary here and then link https://www.datadoghq.com/knowledge-center/audit-logging/

## At Giant Swarm

In all Giant Swarm clusters, two kinds of audit logs are provided:
- Kubernetes audit logs: logging all activity on the Kubernetes API Server
- Machine audit logs: any system calls and file access happening on the host (e.g. login attempts, user commands, file system changes, etc...)

### Kubernetes Audit Logs

The Kubernetes api-server supports audit logging by default. This mechanism log every request made to it by both service accounts and users. Customers can ingest this audit log to detect if any suspicious behavior (internal or by a 3rd party.is made to their kubernetes clusters. 

__Warning:__ This feature is currently unavailable on CAPI clusters.

TODO add sample of logs

For more information on Kubernetes audit logs, we suggest you to read [this](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)

The Kubernetes audit logs can be found on `master/control-plane` nodes only at `/var/log/apiserver/audit*.log

### Virtual Machine Audit Logs

To provide you with a better visibility and security, Giant Swarm gives you the possibility to access the Virtual Machine audit logs.

This solution relies on the [Linux Audit Daemon](https://linux.die.net/man/8/auditd) to collect the logs of any execution happening on the machine.
It is currently configured as such:

```
-a exit,always -F arch=b64 -S execve -k auditing # -k auditing gives those logs a key so we can easily retrieve them
-a exit,always -F arch=b32 -S execve -k auditing
```

TODO add sample of logs

This configuration asks the Linux Audit Daemon to trace any `execve` signal happening on the node.

Beware that the Linux Audit Daemon is quite verbose when it comes to logging so you will need to ensure enough storage and bandwidth for your logs.

The Virtual Machine audit logs can be found in journald.

__Notice:__ The Linux Audit Daemon logs are kernel logs so they need to be accessed as such (e.g. `journalctl -kauditing`)

## How to audit logs ship to a remote location

Giant Swarm offers two tools to allow you to get the audit logs for your workload clusters.

You can also access the access logs for the management clusters but this is not something we provide by default (at least for now). Please contact your Account Engineer to sort out the details.

### Fluent bit

TODO explain what it is and how to configure it
https://github.com/giantswarm/fluent-logshipping-app

### Promtail

TODO explain what it is and how to configure it
https://github.com/giantswarm/promtail-app
