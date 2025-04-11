---
title: Using your own URL for the developer portal
linkTitle: URL
description: How to set up a custom URL for your Giant Swarm developer portal.
weight: 10
menu:
  principal:
    parent: overview-developer-portal-customizing
    identifier: overview-developer-portal-customizing-url
last_review_date: 2025-04-01
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - How can I configure and customize the developer portal?
---

The URL of the developer portal is set to `https://backstage.BASE_DOMAIN/` by default, where `BASE_DOMAIN` is the base domain of the management cluster is deployed in.

We are happy to customize the URL according to your needs. All we need is a CNAME record pointing to the current portal host name. Once you have this CNAME configured, please inform your account engineer so we can update your portal configuration.

## Example

Your management cluster's base domain is `k8s.example.com`, so the default URL of the developer portal is `https://backstage.k8s.example.com/`.

If you want to change the URL to `https://portal.example.com/`, create a CNAME record for `portal.example.com` pointing to `backstage.k8s.example.com`.

As a result, the portal will be available under the URL `https://portal.example.com/` in addition to the default one.
