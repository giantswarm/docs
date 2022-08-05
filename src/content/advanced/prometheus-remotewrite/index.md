---
linkTitle: Prometheus RemoteWrite
title: Prometheus RemoteWrite
description: A guide that explains Prometheus RemoteWrite, and how we do it at Giant Swarm.
weight: 50
menu:
  main:
    parent: advanced
user_questions:
  - What is a Prometheus RemoteWrite?
  - How Prometheus RemoteWrite work?
aliases:
  - /advanced/remotewrite/
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2022-07-19
---

In this document you will learn how to use Prometheus RemoteWrite feature provided out of the box by Giant Swarm.

## What is Prometheus RemoteWrite

Prometheus allows integration with remote storage systems.
Prometheus has [remote_write config](https://prometheus.io/docs/prometheus/latest/configuration/configuration/#remote_write) that allows you to configure `remote_write` targets.

Prometheus `RemoteWrite` is a new approach of managing `remote_write` targets using an opinionated K8s API.

Giant Swarm offers `RemoteWrite` Custom resource, in order to configure `remote_write` in the according Prometheus instance.


