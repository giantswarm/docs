---
linkTitle: Audit logs
title: Audit logs
description: A guide explaining how to interact with audit logs on Giant Swarm clusters.
weight: 50
menu:
  main:
    identifier: getting-started-observability-logging-auditlogging
    parent: getting-started-observability-logging
user_questions:
  - What are audit logs?
  - What is audit logging?
  - How can I access Kubernetes audit logs?
aliases:
  - /getting-started/observability/logging/audit-logs
  - /ui-api/observability/logs/audit-logging
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2024-03-21
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

Kubernetes audit logs can be found on `control-plane` nodes at `/var/log/apiserver/audit*.log`.

#### Giant Swarm default audit policy

##### CAPI clusters

In __capi__ clusters, the default kubernetes policy defined on all our clusters is defined [here](https://github.com/giantswarm/cluster/blob/main/helm/cluster/files/etc/kubernetes/policies/audit-policy.yaml) and can be configured by overriding the value of `internal.advancedConfiguration.controlPlane.apiServer.auditPolicy.extraRule` in the cluster helm chart.

##### Vintage clusters

In __vintage__ clusters, the default kubernetes policy defined on all our clusters (management and workload clusters alike) is the following:

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # The following requests were manually identified as high-volume and low-risk,
  # so drop them.
  - level: None
    users: ["system:kube-proxy"]
    verbs: ["watch"]
    resources:
      - group: "" # core
        resources: ["endpoints", "services", "services/status"]
  - level: None
    # Ingress controller reads 'configmaps/ingress-uid' through the unsecured port.
    users: ["system:unsecured"]
    namespaces: ["kube-system"]
    verbs: ["get"]
    resources:
      - group: "" # core
        resources: ["configmaps"]
  - level: None
    users: ["kubelet"] # legacy kubelet identity
    verbs: ["get"]
    resources:
      - group: "" # core
        resources: ["nodes", "nodes/status"]
  - level: None
    userGroups: ["system:nodes"]
    verbs: ["get"]
    resources:
      - group: "" # core
        resources: ["nodes", "nodes/status"]
  - level: None
    users:
      - system:kube-controller-manager
      - system:kube-scheduler
      - system:serviceaccount:kube-system:endpoint-controller
    verbs: ["get", "update"]
    namespaces: ["kube-system"]
    resources:
      - group: "" # core
        resources: ["endpoints"]
  - level: None
    users: ["system:apiserver"]
    verbs: ["get"]
    resources:
      - group: "" # core
        resources: ["namespaces", "namespaces/status", "namespaces/finalize"]
  - level: None
    users: ["system:serviceaccount:kube-system:cluster-autoscaler"]
    verbs: ["get", "update"]
    namespaces: ["kube-system"]
    resources:
      - group: "" # core
        resources: ["configmaps", "endpoints"]
  # Don't log HPA fetching metrics.
  - level: None
    users:
      - system:kube-controller-manager
    verbs: ["get", "list"]
    resources:
      - group: "metrics.k8s.io"
  # Don't log these read-only URLs.
  - level: None
    nonResourceURLs:
      - /healthz*
      - /version
      - /swagger*
  # Don't log events requests.
  - level: None
    resources:
      - group: "" # core
        resources: ["events"]
  # node and pod status calls from nodes are high-volume and can be large, don't log responses for expected updates from nodes
  - level: Request
    users:
      [
        "kubelet",
        "system:node-problem-detector",
        "system:serviceaccount:kube-system:node-problem-detector",
      ]
    verbs: ["update", "patch"]
    resources:
      - group: "" # core
        resources: ["nodes/status", "pods/status"]
    omitStages:
      - "RequestReceived"
  - level: Request
    userGroups: ["system:nodes"]
    verbs: ["update", "patch"]
    resources:
      - group: "" # core
        resources: ["nodes/status", "pods/status"]
    omitStages:
      - "RequestReceived"
  # deletecollection calls can be large, don't log responses for expected namespace deletions
  - level: Request
    users: ["system:serviceaccount:kube-system:namespace-controller"]
    verbs: ["deletecollection"]
    omitStages:
      - "RequestReceived"
  # Secrets, ConfigMaps, and TokenReviews can contain sensitive & binary data,
  # so only log at the Metadata level.
  - level: Metadata
    resources:
      - group: "" # core
        resources: ["secrets", "configmaps"]
      - group: authentication.k8s.io
        resources: ["tokenreviews"]
    omitStages:
      - "RequestReceived"
  # Get repsonses can be large; skip them.
  - level: Request
    verbs: ["get", "list", "watch"]
    resources:
      - group: "" # core
      - group: "admissionregistration.k8s.io"
      - group: "apiextensions.k8s.io"
      - group: "apiregistration.k8s.io"
      - group: "apps"
      - group: "authentication.k8s.io"
      - group: "authorization.k8s.io"
      - group: "autoscaling"
      - group: "batch"
      - group: "certificates.k8s.io"
      - group: "extensions"
      - group: "metrics.k8s.io"
      - group: "networking.k8s.io"
      - group: "policy"
      - group: "rbac.authorization.k8s.io"
      - group: "scheduling.k8s.io"
      - group: "settings.k8s.io"
      - group: "storage.k8s.io"
    omitStages:
      - "RequestReceived"
  # Default level for known APIs
  - level: RequestResponse
    resources:
      - group: "" # core
      - group: "admissionregistration.k8s.io"
      - group: "apiextensions.k8s.io"
      - group: "apiregistration.k8s.io"
      - group: "apps"
      - group: "authentication.k8s.io"
      - group: "authorization.k8s.io"
      - group: "autoscaling"
      - group: "batch"
      - group: "certificates.k8s.io"
      - group: "extensions"
      - group: "metrics.k8s.io"
      - group: "networking.k8s.io"
      - group: "policy"
      - group: "rbac.authorization.k8s.io"
      - group: "scheduling.k8s.io"
      - group: "settings.k8s.io"
      - group: "storage.k8s.io"
    omitStages:
      - "RequestReceived"
  # Default level for all other requests.
  - level: Metadata
    omitStages:
      - "RequestReceived"
```

###### Custom configuration

If the Giant Swarm default Kubernetes Audit Policy is not sufficient for your use case, you can configure it as you want.

To configure the policy for your management cluster, get in touch with your Account engineer and we will help you sort it out.

For your Vintage workload clusters, you can deploy the [k8s-initiator-app](https://github.com/giantswarm/k8s-initiator-app) App to your cluster to deploy the whatever Audit Policy configuration you want.

__Warning:__ Beware that the k8s-initiator-app can change Kubernetes api server settings and any misconfiguration might cause it to go down. We advise you to ask your Account Engineer for help to configure it safely.

### Machine audit logs

To provide you with a better visibility and security, Giant Swarm offers you the possibility to access the Machine audit logs.

This solution relies on the [Linux Audit Daemon](https://linux.die.net/man/8/auditd) to collect the logs of any execution happening on the machine.
It is currently configured as such:

```nohighlight
-a exit,always -F arch=b64 -S execve -k auditing # -k auditing gives those logs a key so we can easily retrieve them
-a exit,always -F arch=b32 -S execve -k auditing
```

This configuration asks the Linux Audit Daemon to trace any `execve` signal happening on the node and renders logs like:

```sh
Feb 06 09:57:37 ip-10-0-5-34.eu-central-1.compute.internal kernel: audit: type=1300 audit(1675677457.491:6132447): arch=c000003e syscall=59 success=yes exit=0 a0=55a8f8fc7fd0 a1=55a8f947eec0 a2=55a8f9b8fd10 a3=55a8f947eec0 items=2 ppid=1 pid=3659596 auid=4294967295 uid=0 gid=0 euid=0 suid=0 fsuid=0 egid=0 sgid=0 fsgid=0 tty=(none) ses=4294967295 comm="update-ssh-keys" exe="/usr/bin/update-ssh-keys" subj=system_u:system_r:kernel_t:s0 key="auditing"
```

The Linux Audit Daemon logs are kernel logs which are stored in `journald` and can be accessed with `journalctl -kauditing`.

__Warning:__ Beware that the Linux Audit Daemon is quite verbose so when shipping those logs you will need to ensure enough storage and bandwidth are available in order to process them.
