---
linkTitle: IAM roles for service accounts
title: AWS IAM roles for service accounts (IRSA)
description: This article describes how to use a new feature that allows binding of specific AWS IAM roles to a service account of a pod.
weight: 60
menu:
  principal:
    parent: tutorials-access-management
    identifier: tutorials-access-management-irsa
user_questions:
 -  How can I use IAM roles for service accounts?
last_review_date: 2024-12-03
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
aliases:
  - /vintage/advanced/access-management/iam-roles-for-service-accounts
---

You can associate an IAM role with a `Kubernetes` service account. This service account can then provide AWS permissions to the containers in any pod that uses that service account. With this feature, you no longer need to provide extended permissions to the Giant Swarm node IAM role so that pods on that node can call AWS APIs.

Applications must sign their AWS API requests with AWS credentials. This feature provides a strategy for managing credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Instead of creating and distributing your AWS credentials to the containers or using the Amazon EC2 instance’s role, you can associate an IAM role with a `Kubernetes` service account. The applications in the pod’s containers can then use an AWS SDK or the AWS CLI to make API requests to authorized AWS services.

The official documentation from AWS: [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (`IRSA`).

## IAM role permissions on `capa` controller

The Cluster API for AWS controller comes with an attached policy name `giantswarm-<INSTALLATION>-irsa-controller-policy` that contains permissions like:

```json
  {
      "Effect": "Allow",
      "Action": [
        "iam:CreateOpenIDConnectProvider",
        "...",
        "cloudfront:TagResource",
        "...",
        "acm:RequestCertificate",
        "...",
      ],
      "Resource": "*"
  },
  {
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "...",
      ],
      "Resource": "arn:aws:s3:::*-g8s-*"
  }
```

Thanks to this policy, the controller can create a Cloudfront distribution, ACM certificate, S3 bucket and OpenID Connect provider to enable the usage of the IRSA feature.

## Using IAM roles for service accounts

To use IAM roles for service accounts, you need to create an IAM role, which permissions you want to assign to your application, and a `Kubernetes` service account.

### IAM role

You have to make sure the **trusted entity** of the IAM role contains a condition like the `sub` service account name of a JSON Web token (JWT). You need to ensure one of those conditions match against the `JWT`, which is used by one of your applications.

This is an example of `external-dns` role trust policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::<ACCOUNT_ID>:oidc-provider/irsa.$INSTALLATION.gaws.gigantic.io"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "irsa.golem.gaws.gigantic.io:sub": "system:serviceaccount:kube-system:external-dns"
                }
            }
        }
    ]
}
```

**Note**: In the above example, the federation is set to the `OIDC` provider of the cluster. You can rely on your own OIDC provider making sure the parameter is set correctly.

### Service account

The service account has to be annotated with a full `ARN` of the IAM role. You can get the `ARN` of the role in the AWS console, when you check role details.

The annotation key has to be `eks.amazonaws.com/role-arn`.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  annotations:
    eks.amazonaws.com/role-arn: arn:aws:iam::$AWS_ACCOUNT:role/$IAM_ROLE_NAME
  name: s3-access
  namespace: default
```

## Cross Account Roles {#cross-account}

### IAM role cross account

In order to assume roles cross AWS accounts you will need to create a new AWS Identity Provider (OpenID Connect) in the AWS account where the IAM role is located.

![Creating AWS Identity Provider](identity-provider.png)

Login into the AWS on the account where the cluster is running:

- Grab the address of the `Identity Provider` in your current cluster via [AWS Console > IAM > Identity Providers](https://us-east-1.console.aws.amazon.com/iam/home?#/identity_providers). It will look like `https://irsa.mycluster.<basedomain>`.

Log into the account where the IAM role is located and create an identity provider in `IAM > Identity Providers`:

- Set `Provider URL` to the previously gathered address and click the `Get thumbprint` to import the certificate.
- Set the `audience` to `sts.amazonaws.com` (for China regions: `sts.amazonaws.com.cn`).

## Verify your configuration is correct

Once your pod is running with the configured service account, you should see a file in the pod called `/var/run/secrets/eks.amazonaws.com/serviceaccount/token`, which contains a `JWT` token with details of the role.

The pod should also automatically receive configured environment variables `AWS_WEB_IDENTITY_TOKEN_FILE` and `AWS_ROLE_ARN`.

Check the pod using command `kubectl -n NAMESPACE get pod POD_NAME -o yaml` and search for the environment variables or for the volume mounts.

You can also use this example pod with `aws-cli` to verify the configuration:

```sh
kubectl run aws-cli-test \
  --image=amazon/aws-cli:2.13.17 \
  --restart=Never \
  --namespace=default \
  --command -- sh -c "aws s3 ls" \
  --overrides='{"spec": {"serviceAccountName": "default"}}'
```

**Note**: You may want to adjust the `namespace` and `serviceAccountName` to match your configuration.

Learn more about the [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) in the official AWS documentation.
