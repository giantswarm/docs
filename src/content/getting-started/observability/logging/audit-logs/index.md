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
last_review_date: 2023-02-01
---

In this document you will learn what are audit logs, which kind is available on Giant Swarm clusters and how to access / ship them to a remote location.

## Audit logging

Audit logging is the process of recording any event happening within or to your system (execution of any network call, security events like logins, payment transactions and so on).
An audit log records any occurrence of an event, i.e. who did what and when with as much detail as possible

For a more in-depth introduction to audit logging, we advise you to read [this](https://www.datadoghq.com/knowledge-center/audit-logging/)

## At Giant Swarm

In all Giant Swarm clusters, two kinds of audit logs are provided:
- __Kubernetes audit logs__: logging all activity on the Kubernetes API Server
- __Machine audit logs__: any system calls and file access happening on the host (e.g. login attempts, user commands, file system changes, etc...)

### Kubernetes audit logs

__Warning:__ This feature is currently unavailable on CAPI clusters.

The Kubernetes api-server supports audit logging by default. This mechanism logs every request made to it by both service accounts and users. Customers can ingest these audit logs to detect if any suspicious behaviour (internal or by a 3rd party) is made to their Kubernetes clusters. 

__Example:__

```json
{
    "kind": "Event",
    "apiVersion": "audit.k8s.io/v1",
    "level": "RequestResponse",
    "auditID": "a6029022-4ff0-4c54-97ed-4099d0ca1923",
    "stage": "RequestReceived",
    "requestURI": "/api/v1/namespaces/default/serviceaccounts?fieldManager=kubectl-create",
    "verb": "create",
    "user": {
        "username": "kubernetes-admin",
        "groups": ["system:masters", "system:authenticated"]
    },
    "sourceIPs": ["172.31.22.88"],
    "userAgent": "kubectl/v1.23.6 (linux/amd64) kubernetes/ad33385",
    "objectRef": {
        "resource": "serviceaccounts",
        "namespace": "default",
        "apiVersion": "v1"
    },
    "requestReceivedTimestamp": "2022-07-31T08:36:48.679291Z",
    "stageTimestamp": "2022-07-31T08:36:48.679291Z"
}
```

For more information on Kubernetes audit logs, we suggest you to read [this](https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/)

At the moment, the Kubernetes audit logs can be found on `control-plane` nodes only at the location `/var/log/apiserver/audit*.log` that you can ship to your <abbr title="Security information and event management">SIEM</abbr> system.

The Kubernetes audit logs will be shipped to our [Managed Loki](https://github.com/giantswarm/roadmap/issues/311) in the future.

### Machine audit logs

To provide you with a better visibility and security, Giant Swarm offers you the possibility to access the Machine audit logs.

This solution relies on the [Linux Audit Daemon](https://linux.die.net/man/8/auditd) to collect the logs of any execution happening on the machine.
It is currently configured as such:

```
-a exit,always -F arch=b64 -S execve -k auditing # -k auditing gives those logs a key so we can easily retrieve them
-a exit,always -F arch=b32 -S execve -k auditing
```

This configuration asks the Linux Audit Daemon to trace any `execve` signal happening on the node and renders logs like:

```sh
Feb 06 09:57:37 ip-10-0-5-34.eu-central-1.compute.internal kernel: audit: type=1300 audit(1675677457.491:6132447): arch=c000003e syscall=59 success=yes exit=0 a0=55a8f8fc7fd0 a1=55a8f947eec0 a2=55a8f9b8fd10 a3=55a8f947eec0 items=2 ppid=1 pid=3659596 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="update-ssh-keys" exe="/usr/bin/update-ssh-keys" subj=system_u:system_r:kernel_t:s0 key="auditing"
```

Beware that the Linux Audit Daemon is quite verbose when it comes to logging so you will need to ensure enough storage and bandwidth for your logs. For this we suggest you use either a SIEM tool, Opensearch or Loki

At the moment, the Machine audit logs can be found in `journald` so you can ship them over to your <abbr title="Security information and event management">SIEM</abbr> system.

__Notice:__ The Linux Audit Daemon logs are kernel logs so they need to be accessed as such (e.g. `journalctl -kauditing`)

The Machine audit logs will be shipped to our [Managed Loki](https://github.com/giantswarm/roadmap/issues/311) in the future.

## How to audit logs ship to a remote location

Giant Swarm offers two tools to allow you to get the audit logs for your workload clusters.

You can also access the access logs for the management clusters but this is not something we provide by default (at least for now). Please contact your Account Engineer to sort out the details.

### Fluent bit

Giant Swarm provides a custom [Fluent-bit](https://fluentbit.io/) configuration packaged as a Managed App named [`fluent-logshipping-app`](https://github.com/giantswarm/fluent-logshipping-app)

Fluent-bit's main advantage is that it can be used for all kinds of cases (shipping to rsyslog, elasticsearch, loki and so on) and provides a lot of configurability with it's plugin system so you can use it if this is what you need.

### Promtail

As we are providing [Loki as Managed app](https://github.com/giantswarm/loki-app), we also provide our customers with [Promtail](https://github.com/giantswarm/promtail-app) for log collection and shipping.

Note that Promtail can only be used with Loki but it provides a better integration with it (targets and labels found using Service Discovery instead of on the node directly).

