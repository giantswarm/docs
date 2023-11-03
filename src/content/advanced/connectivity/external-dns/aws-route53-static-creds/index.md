---
linkTitle: AWS Route 53 with static credentials
title: External DNS with AWS Route 53 and static credentials
description: How to configure the External DNS service to use AWS Route 53 with static credentials.
weight: 25
menu:
  main:
    parent: advanced-external-dns
user_questions:
  - How can I customize the External DNS AWS authentication method?
last_review_date: 2023-11-03
aliases:
  - /guides/external-dns/aws-route53-static-creds/
  - /advanced/external-dns/aws-route53-static-creds/
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

External DNS in Giant Swarm is configured to authenticate against AWS using the method available on the cluster (IRSA). But there are cases where this is no possible, for example, if you try to manage your DNS records in AWS Route 53 from a cluster running on a different provider.

## Credentials

This method requires pre-created credentials to authenticate with its respective policy attached.

You can find more information in the [AWS Route 53 - IAM Policy](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#iam-policy) and the [AWS Route 53 - Static Credentials](https://github.com/kubernetes-sigs/external-dns/blob/master/docs/tutorials/aws.md#static-credentials) tutorials.

## Configuration

There are two possible configurations described in this section.

__Important:__ Independent of the cloud provider where the App is running, you must set the `provider` value as `aws`, as shown in the examples.

### Use an existing secret (recommended)

This method configures the App to mount the credentials file from an existing `external-dns-route53` secret.

The secret must contain a file with the following format:

```nohighlight
[default]
aws_access_key_id = _REPLACE_WITH_ACCESS_KEY_ID_
aws_secret_access_key = _REPLACE_WITH_ACCESS_KEY_SECRET_
```

Use the following values to set up the external-dns-app:

```yaml
# values.yaml

provider: aws

aws:
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

### Inject access key as values

Starting from version `2.35.1`, with the addition of the secretConfiguration values, the external-dns-app supports 2 ways to load static credentials:

#### secretConfiguration

This method is flexible as it loads credentias from the chart values and stores them in a `Secret` without making any assumptions about the structure of your data. It can be used in conjunction with `env` values to provide the credentials to the application.

This example is the equivalent configuration to the one outlined in the following section:

```yaml
# values.yaml

provider: aws

domainFilters: <domain>

secretConfiguration:
  enabled: true
  mountPath: /.aws
  data:
    credentials: |
      [default]
      aws_access_key_id = _REPLACE_WITH_ACCESS_KEY_ID_
      aws_secret_access_key = _REPLACE_WITH_ACCESS_KEY_SECRET_
```

#### aws_access_key_id and aws_secret_access_key

__Warning:__ This method will be deprecated in future versions.

This configuration directly injects the `aws_access_key_id` and `aws_secret_access_key` into the App.

```yaml
# values.yaml

provider: aws

aws:
  access: external
  baseDomain: <domain>

externalDNS:
  aws_access_key_id: <key_id>
  aws_secret_access_key: <secret>
```

---

## Further reading

- [external-dns-app](https://github.com/giantswarm/external-dns-app)
