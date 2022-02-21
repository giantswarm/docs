---
linkTitle: Authorization
title: Authorization and RBAC automation in the Management API
description: Granting users specific permission to certain resources is what authorization is all about. The Management API uses Kubernetes' role based access control (RBAC) primitives and provides automation on top of it to make authorization easy for most real-life use cases. Here we explain them in detail.
weight: 20
menu:
  main:
    identifier: uiapi-managementapi-authorization
    parent: uiapi-managementapi
last_review_date: 2022-02-21
user_questions:
  - TODO
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
---

# Authorization and RBAC automation in the Management API

Outline

- Link to ../authorization/ as a prerequisite
- Users will need various levels of access to different resources throughout the management cluster.
  - Examples
    1. Admin needs full permissions for everything
    2. Organization admin needs all permissions for resources of one organization
    3. App developer needs write access to a few apps in clusters, read access to other resources

- RBAC primitives in use
  - Namespaces, with [Organizations]() as a special use case
  - ClusterRoles and Roles
  - ClusterRoleBindings and RoleBindings
  - Subjects: users, groups (from the identity provider) or service accounts

- Resources in the management cluster and where they reside
  - Cluster scope
    - Release
    - Organization
  - default namespace
    - App catalogs by Giant Swarm
  - Organization namespace
    - Resources defining clusters and node pools
    - Provider credentials
  - Cluster namespace
    - Resources for installed apps (App, ConfigMap, Secret)

- Automation grants permissions
  - for 'get' access to an Organization
  - to releases and app catalogs
  - for resources in related (cluster) namespaces (installed apps and their config)
  - mention `rbac-operator`
