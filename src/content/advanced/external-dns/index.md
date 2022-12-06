---
linkTitle: External DNS
title: Advanced External DNS configuration
description: Advanced configuration of the External DNS service in your clusters
weight: 25
menu:
  main:
    parent: advanced
last_review_date: 2022-12-06
user_questions:
  - How can I customize the External DNS service configuration?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

## Integrate External DNS with AWS Route53 with access key

External DNS in Giant Swarm is configured to authenticate against the AWS using the method available on the cluster (KIAM or IRSA). But there are cases where this is no possible, for example, if you try to manage your DNS records in AWS Route53 from a cluster running on a different provider.

There are 2 different possible configurations.

### Use an existing secret (recommended).

This method configures the App to mount the credentials file from an existing `external-dns-route53` secret.

The secret must contain a file with the following format:
```
[default]
aws_access_key_id = _REPLACE_WITH_ACCESS_KEY_ID_
aws_secret_access_key = _REPLACE_WITH_ACCESS_KEY_SECRET_
```

Use the following values to set up the external-dns-app:

```yaml
# values.yaml

aws:
  access: external
  baseDomain: <domain>

env:
- name: AWS_SHARED_CREDENTIALS_FILE
  value: /.aws/credentials

extraVolumeMounts:
- name: aws-credentials
  mountPath: /.aws
  readOnly: true

extraVolumes:
- name: aws-credentials
  secret:
    secretName: external-dns-route53
```

### Inject access key as values.

This configuration directly injects the `aws_access_key_id` and `aws_secret_access_key` into the App.

```yaml

# values.yaml
aws:
  access: external
  baseDomain: <domain>

externalDNS:
  aws_access_key_id: <key_id>
  aws_secret_access_key: <secret>
```

__Warning:__

This method is not recommended and will be deprecated in future versions.

---

## Further reading

- [external-dns-app](https://github.com/giantswarm/external-dns-app)
