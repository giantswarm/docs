---
linkTitle: External DNS using static credentials
title: External DNS with AWS Route 53 and static credentials 
description: How to configure the External DNS service to use AWS Route 53 with static credentials.
weight: 25
menu:
  main:
    parent: advanced-external-dns
last_review_date: 2022-12-09
user_questions:
  - How can I customize the External DNS AWS authentication method?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

External DNS in Giant Swarm is configured to authenticate against AWS using the method available on the cluster (KIAM or IRSA). But there are cases where this is no possible, for example, if you try to manage your DNS records in AWS Route 53 from a cluster running on a different provider.

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

### Inject access key as values

__Warning:__ This method is not recommended and will be deprecated in future versions.

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
