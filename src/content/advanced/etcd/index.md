---
linkTitle: Etcd Quota Backend Bytes
title: Etcd Quota Backend Bytes
description: Since version 18.3 it's now possible to adjust the Etcd `--quota-backend-bytes` which allows to increase Etcd's keyspace database size.
weight: 140
menu:
  main:
    parent: advanced
user_questions:
  - What is Etcd's keyspace database size?
  - How do I set the quota-backend-bytes?
  - When to change the default value?
  - What are the side effects of setting a large Etcd database?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2023-03-19
---

{{< platform_support_table aws="ga=v18.3" >}}

## Definition

Etcd's keyspace is the set of all keys in an etcd cluster.  
By default Etcd keeps several versions of its keyspace.  
In order to keep Etcd running efficiently it's important to:
1. Assign the right size to the Etcd keyspace database via the `quota-backend-bytes` 
2. Run auto compaction
3. Run defragmentation

From version `>= 18.3` we have improved the Etcd autocompaction and defragmentation to be executed automatically and more frequently.

## How to change the Etcd keyspace size

Since version 18.3 we have introduced a way to configure the `quota-backend-bytes` via the following annotation `etcd.giantswarm.io/quota-backend-bytes` in the `cluster.x-k8s.io/v1beta1/clusters` CRD.  
The value of the annotation is in bytes.  
The default value is: `8589934592`

## When to change the default value

In general the default value is large enough to handle very large clusters.  

Recently, however, more and more technologies, built to run specifically in Kubernetes, tend to abuse Etcd and use it as a database to store reports.  
Kyverno and Trivy are just examples of these kind of technologies.  

Specifically for Kyverno, it's possible to create policies which generate reports very frequently and this can cause the Etcd keyspace to fill up quickly.  

When the Etcd database is full it's a cathastrofic event and the Kubernetes control plane becomes unavailable.  

If the automatic compaction and defragmentation is not enough to prevent the Etcd database from filling up, then it means it's necessary to increase its maximum size via the `etcd.giantswarm.io/quota-backend-bytes` annotation.

## Side effects of a large Etcd database

Etcd recommends to set the `quota-backend-bytes` to a maximum of 8GB.  
It's possible to set even larger values, however it comes at a cost:

- the Etcd process will use much more memory, which in turn will require bigger control plane servers, which means higher running costs.
- the Etcd database can take long to compact and defrag. The defrag is a blocking operation, so it can cause an increase in Etcd leader elections.  
- a large etcd database usually means the k8s control plane runs large range queries which increase the network traffic.
- Etcd appends all key changes to a log file. This log grows forever and is a complete linear history of every change made to the keys. To avoid having a huge log etcd makes periodic snapshots. These snapshots provide a way for etcd to compact the log by saving the current state of the system and removing old logs. If the the snapshot takes too long then it can negatively affect the Etcd availability.

In general, all of the above can cause instability at the Etcd level and by extension Kubernetes control plane.  

Use with care!
