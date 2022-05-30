---
linkTitle: IAM roles for service accounts
title: AWS IAM roles for service accounts
description: This article describes how to use a new feature that allows binding of specific AWS IAM roles to a service account of a pod.
weight: 60
menu:
  main:
    parent: advanced
user_questions:
 -  How can I use IAM roles for service accounts?
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
last_review_date: 2022-03-04
---

{{< platform_support_table aws="alpha=v17.2.0" >}}

You can associate an IAM role with a Kubernetes service account. This service account can then provide AWS permissions to the containers in any pod that uses that service account. With this feature, you no longer need to provide extended permissions to the Giant Swarm node IAM role so that pods on that node can call AWS APIs.

Applications must sign their AWS API requests with AWS credentials. This feature provides a strategy for managing credentials for your applications, similar to the way that Amazon EC2 instance profiles provide credentials to Amazon EC2 instances. Instead of creating and distributing your AWS credentials to the containers or using the Amazon EC2 instance’s role, you can associate an IAM role with a Kubernetes service account. The applications in the pod’s containers can then use an AWS SDK or the AWS CLI to make API requests to authorized AWS services.

The official documentation from AWS: [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html).

## Additional IAM role permissions on `GiantSwarmAWSOperator` needed

Please first ensure having the following permissions added on the [`GiantSwarmAWSOperator` IAM role]({{< relref "/getting-started/cloud-provider-accounts/aws" >}}):

```json
...
  {
      "Effect": "Allow",
      "Action": [
          "iam:CreateOpenIDConnectProvider",
          "iam:DeleteOpenIDConnectProvider",
          "iam:ListOpenIDConnectProviderTags",
          "iam:TagOpenIDConnectProvider",
          "iam:UntagOpenIDConnectProvider"
      ],
      "Resource": "*"
  },
...
  {
      "Effect": "Allow",
      "Action": [
          "s3:PutObjectAcl"
      ],
      "Resource": "arn:aws:s3:::*-g8s-*"
  },
 ...
```

## Enable the feature on your cluster
This is an alpha feature that has to be enabled by setting an annotation on the  [`AWSCluster`]({{< relref "/ui-api/management-api/crd/awsclusters.infrastructure.giantswarm.io.md" >}}) resource.

Make sure the resource has the `alpha.aws.giantswarm.io/iam-roles-for-service-accounts` annotation **before applying a new cluster or before upgrading to the latest AWS release**. The value can be anything you like, as only the presence of that annotation is checked. Here is an example:

```yaml
apiVersion: infrastructure.giantswarm.io/v1alpha3
kind: AWSCluster
metadata:
  annotations:
    alpha.aws.giantswarm.io/iam-roles-for-service-accounts: ""
  labels:
    ...
  name: abcl0
  namespace: myorg
spec:
  ...
```

Alternatively you can use `kubectl` to annotate the CR like shown below:

```nohighlight
kubectl annotate \
   awsclusters.infrastructure.giantswarm.io \
   abcl0 \
   alpha.aws.giantswarm.io/iam-roles-for-service-accounts=""
```

In order to apply the changes, rolling of the master nodes is required. Rolling of the nodes can be triggered either by an update or manually by terminating each node.

## Using IAM roles for service accounts

### IAM role

To use the IAM role with a service account you need to create new or modify an existing AWS role and configure **trusted entities** with following statement:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::AWS_ACCOUNT:oidc-provider/s3.REGION.amazonaws.com/AWS_ACCOUNT-g8s-CLUSTER_ID-oidc-pod-identity"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "s3.REGION.amazonaws.com/AWS_ACCOUNT-g8s-CLUSTER_ID-oidc-pod-identity:sub": "system:serviceaccount:NAMESPACE:SA_NAME"
                }
            }
        }
    ]
}
```

You need to fill real values for these placeholders:
* `AWS_ACCOUNT` - aws account id, where is the cluster running
* `CLUSTER_ID` - cluster id
* `NAMESPACE` - Kubernetes namespace in cluster, where the pod and service account be used.
* `SA_NAME` - Name of the Kubernetes Service Account which wil be using by the pod.
* `REGION` - AWS region the OIDC provider is located in.

### Service account
The service account has to be annotated with a full ARN of the IAM role. You can get the ARN of the role in the AWS console, when you check role details.
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

## Verify your configuration is correct
Once your pod is running with the configured service account, you should see a file in the pod called `/var/run/secrets/eks.amazonaws.com/serviceaccount/token`, which containts a JWT token with details of the role.

The pod should also have configured enviroment variables `AWS_WEB_IDENTITY_TOKEN_FILE` and `AWS_ROLE_ARN`.

Check the pod using command `kubectl -n NAMESPACE get pod POD_NAME -o yaml` and search for the enviroment variables or for the volume mounts.


## Migration from kiam to IAM roles for service accounts

If you have followed the steps above you can switch from kiam to IAM roles for service accounts by following the steps:

- Remove the all the kiam annotation `iam.amazonaws.com/role` from your deployment and set the `eks.amazonaws.com/role-arn` on the service account. **Important** - you need set the whole ARN of the role, not just the name of the role, see the service account example above.

- Verify that your application is working correctly.

In case your application is not working you can always remove the annotation on the service account and add the kiam annotation on your deployment again.
