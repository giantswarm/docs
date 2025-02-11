---
linkTitle: Authentication
title: Authentication for the platform API
description: Instructions on how to authenticate for the platform API, both as a user and in an automation context. We also provide some technical background information and requirements for new customers. This also includes a guide to debug issues with Giantswarm management API cluster name resolution.
weight: 20
menu:
  principal:
    identifier: tutorials-access-management-authentication
    parent: tutorials-access-management
last_review_date: 2024-10-28
user_questions:
  - How does authentication for the platform API work?
  - What if the Giantswarm administration API doesn't resolve the cluster name properly?
owner:
  - https://github.com/orgs/giantswarm/teams/team-shield
---

## Debugging Giantswarm Management API Cluster Name Resolution

This section outlines a debugging issue where the Giantswarm management API doesn't properly resolve the cluster name. The issue seems to be related to the API permissions. 

### Login Command

Try using the command given below, replacing the placeholders with your actual data.

```shell
kubectl gs login &lt;<https://api>.&lt;YOUR_CLUSTER&gt;.<http://egg.gigantic.io|egg.gigantic.io>&gt; --workload-cluster &lt;YOUR_WORKLOAD_CLUSTER&gt; --organization &lt;YOUR_ORGANIZATION&gt; --certificate-group system:masters --certificate-ttl 8h
```

### Checking RBAC

If the issue persists after the previous step, check if the Role-Based Access Control (RBAC) is present:

```shell
kg rolebinding write-all-customer-group -n &lt;YOUR_ORGANIZATIONAL_NAMESPACE&gt; -o yaml
```

This command should return a YAML output similar to the one shown below:

```yaml
apiVersion: <http://rbac.authorization.k8s.io/v1|rbac.authorization.k8s.io/v1>
kind: RoleBinding
metadata:
  creationTimestamp: "2024-07-10T15:20:16Z"
  labels:
    <http://giantswarm.io/managed-by|giantswarm.io/managed-by>: rbac-operator
  name: write-all-customer-group
  namespace: org-egger
  resourceVersion: "372731412"
  uid: 115e3e43-9c78-4d77-a0c6-85bf4758c772
roleRef:
  apiGroup: <http://rbac.authorization.k8s.io|rbac.authorization.k8s.io>
  kind: ClusterRole
  name: cluster-admin
subjects:
- apiGroup: <http://rbac.authorization.k8s.io|rbac.authorization.k8s.io>
  kind: Group
  name: customer:giantswarm:Employees
- apiGroup: <http://rbac.authorization.k8s.io|rbac.authorization.k8s.io>
  kind: Group
  name: customer:eagle_admin
```

### Changing the OIDC Group ID

If your OIDC group ID has been changed, this could be the source of the problem.

You may need to decrypt the appropriate secret (in this case 'egger dex-app' secret in 'egger-configs') and under `oidc.customer.connectors`, replace `customer-developer` with `customer`.

```shell
#Change this:
id: customer-developers

#To this:
id: customer
```
After making these changes, you might need to create a pull request in your configurations repository and merge the changes.

Finally, you should open an issue to track this hardcoding work if it proves successful. This serves as a record, helping us remember where the hardcoding was implemented.