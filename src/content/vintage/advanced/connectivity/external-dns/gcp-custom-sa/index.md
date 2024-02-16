---
linkTitle: Using a dedicated GCP service account
title: External DNS using a dedicated GCP service account
description: This document describes how to configure External DNS to use a dedicated GCP service account.
weight: 25
menu:
  main:
    parent: advanced-external-dns
user_questions:
  - How can I override GCP service account used by External DNS?
last_review_date: 2023-11-07
aliases:
  - /advanced/connectivity/external-dns/gcp-custom-sa
  - /guides/external-dns/gcp-custom-sa/
  - /advanced/external-dns/gcp-custom-sa/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

## Overview

By default, our External DNS App uses the `gcpProject` value to compose the right annotation for the `ServiceAccount` to correctly authenticate against GCP.

## Configuration

To override the default configuration, use the following values with the `external-dns-app`:

```yaml
# values.yaml

serviceAccount:
  annotations:
    giantswarm.io/gcp-service-account: _REPLACE_WITH_GCP_SA_ID_
```

---

## Further reading

- [external-dns-app](https://github.com/giantswarm/external-dns-app)
- [workload-identity-operator-gcp](https://github.com/giantswarm/workload-identity-operator-gcp)
