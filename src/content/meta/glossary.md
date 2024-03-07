---
title: Glossary
description: A page with the term definitions Giant Swarm uses in the documentation.
search: false
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
---

We used a set of terms across our documentation that could be no clear to readers. In the following article we define of those terms to clarify the complexity that could carry.

## Cloud Native Developer Platform

A Cloud Native Developer Platform is an integrated collection of capabilities exposed by intuitive interface that facilitates the application development lifecycle. It offers a flexible configuration to build a system that encodes your company practices. It integrates with different open source solutions to enable automation, observability and security for your workloads.

## Smart Platform Engineering

Smart Platform Engineering refers to the design and development of intelligent platforms that help you to create the desired Developer Platform for your teams in a quick fashion. Instead of starting from scratch to build piece by piece an entire platform meanwhile you operate it 24/7, leverage in our knowledge, product and support to reach your goals in a decent amount of time.

## Platform API

Is the entrypoint of the Cloud Native Developer Platform. Everything in the platform is exposed via the API, allowing the automation of processes and fostering standardization. The Platform API is a fully compliant Kubernetes API extended with some custom resources to enable a variety of use cases.

## Management Cluster

It is a Kubernetes cluster that acts a central point of the platform. It is in charge of host platform wide services like observability or security to ensure visualization and compliance over all the workloads in all clusters.

## Workload Cluster

The customer platform teams can define several clusters where the developers can run their applications based on different requirements like location, stage or isolation.
