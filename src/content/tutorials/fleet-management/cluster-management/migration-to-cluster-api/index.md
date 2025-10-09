---
title: Post-migration guide for clusters migrated from vintage to Cluster API
linkTitle: Vintage-to-CAPI post-migration guide
description: This only applies to clusters migrated from vintage to Cluster API, not to any newly created clusters. We explain cleanup and migration away from cloud resources previously used in the "vintage" product generation.
weight: 20
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-migration-to-cluster-api
last_review_date: 2025-10-07
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

From the outset, Giant Swarm has utilized Kubernetes to build platforms. In the early years, everybody was still figuring out how to manage Kubernetes lifecycle across a fleet of clusters. We built our own tooling, largely based on [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), which worked well for us and our customers. As the Kubernetes project and the community around it evolved, it became clear that many companies in the ecosystem were trying to solve the same fundamental challenges regarding cluster lifecycle management. With our extensive experience, we saw an opportunity to contribute to a broader solution. We pushed for a joint effort to build a standardized method for cluster lifecycle management. [Cluster API]({{< relref "/overview/fleet-management/cluster-management/introduction-cluster-api" >}}) is backed by the Kubernetes community and covers different providers like AWS, Azure, GCP, and others.

**Giant Swarm has finished the migration from the previous "vintage" product generation to Cluster API based cluster management for all customers in 2025, seamlessly and without downtime. This guide is only relevant for customers with clusters that were migrated to CAPA**, as during migration, certain old cloud resources needed to be kept. Here, we explain the steps to take to switch to new variants and clean up old resources. **If you are not using IRSA for your own applications, or for any managed apps, this guide is not relevant for you.**

For each of the cleanup steps, which can be done independently of each other, feel free to coordinate with Giant Swarm support to ensure a smooth cleanup.

## OIDC providers (service account issuers) and IAM policies

A cluster's service account issuer is an OIDC provider that signs and issues the tokens for the cluster's Service Accounts. These service accounts can then be used to authenticate workloads against the Kubernetes API and the AWS API via [IRSA]({{< relref "/tutorials/access-management/iam-roles-for-service-accounts/" >}}).

In CAPA, since the cluster domain name changes from vintage, a new service account issuer has also been introduced. To make for a smooth migration though, we support defining multiple issuers in a cluster. This way, service account tokens issued by all the defined issuers will be accepted in the cluster's Kubernetes API. The accepted issuers are defined in `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers` ([values documentation](https://github.com/giantswarm/cluster/blob/main/helm/cluster/README.md#provider-integration)) in the cluster-aws app values (order matters as we'll see below).

A migrated cluster, for example, can look like this before cleanup:

- Primary URL/domain, used to issue and validate tokens: `https://irsa.<workload cluster name>.k8s.<management cluster name>.some-subdomain.example.com`
- Secondary URL/domain, only used to validate tokens (but none are issued by this provider yet): `https://irsa.<workload cluster name>.some-subdomain.example.com`
- Note: Clusters in China cannot use a CloudFront deployment with domain `irsa.<cluster domain>`. The S3 buckets storing the key information are used directly as service account issuer URLs, for example `s3.cn-northwest-1.amazonaws.com.cn/123456123456-g8s-mycluster-oidc-pod-identity-v2` for vintage, and `-v3` suffix for CAPI. The instructions below need to be adapted for that special case.

The vintage service account issuer (first in the list above) needs to be phased out, since it's tied to the vintage cluster base domain which will also be phased out eventually (see section [DNS hosted zones](#dns-hosted-zones-and-kubernetes-api-endpoint)).

Two things need to happen to achieve that without downtime:

- You may have applications using the issuers for IRSA, meaning they authenticate to the AWS API through service accounts. In this case, AWS IAM trust relationships may still reference the old domain. You will change them with the below instructions to allow both old and new domains.
- Kubernetes service account tokens must be re-issued by the new issuer domain. Kubernetes does this automatically, but only once a token expires. Therefore, both issuers must be kept for a certain time, but you will turn around their purpose: the vintage issuer will be switched to only validate (old, existing) tokens, while the CAPA issuer will be switched to become primary, meaning it is responsible to issue any new tokens once the old tokens expire, and is also used for validation.

**Let's start. These are the exact steps you need to follow:**

1. Choose one workload cluster for which you want to perform the cleanup. In this example, we'll call the cluster `mycluster`. [Log into]({{< relref "/getting-started/access-to-platform-api/" >}}) the Kubernetes API.
2. Find all the AWS IAM Roles used by a `ServiceAccount` via IRSA:

   ```sh
   kubectl get ServiceAccount -A -o jsonpath='{range .items[?(@.metadata.annotations contains "eks.amazonaws.com/role-arn")]}{ .metadata.annotations.eks\.amazonaws\.com/role-arn }{"\n"}{ end }' | sort | uniq > /tmp/service-accounts.txt
   ```

3. List which AWS accounts you will have to look through:

   ```sh
   echo "### Affected AWS accounts ### "; echo; grep -oE ':[0-9]{12,}:' /tmp/service-accounts.txt | tr -d ':' | sort | uniq > /tmp/affected-accounts.txt; cat /tmp/affected-accounts.txt; echo; echo "### Unknown roles, please manually check to which account each of them belongs ###"; grep -vE ':[0-9]{12,}:' /tmp/service-accounts.txt || echo '(none)'
   ```

4. Find trust policies that only allow the vintage OIDC issuer. You can do this manually using the AWS Console, or somewhat automated using aws-cli. In both cases, if you have roles in multiple accounts, you need to go through all accounts. The file `/tmp/affected-accounts.txt` lists all affected account numbers ‒ **please perform the next steps for each account**. The below instructions are for aws-cli and also require [jq](https://jqlang.org/) to be installed.

   ```sh
   # Use some way to tell aws-cli how to reach an account
   export AWS_PROFILE="FILL_PROFILE_FOR_THE_AWS_ACCOUNT"

   # Specify the base domain of your CAPI MC
   capi_base_domain="capi.acme.net"

   # Copy-paste this full line into your terminal
   (set -eu; account_id="$(aws sts get-caller-identity --query Account --output text)"; echo "Checking AWS account ID ${account_id}"; aws iam list-roles --output json > "/tmp/iam-roles-${account_id}.json"; echo "  Checking $(jq ".Roles | length" "/tmp/iam-roles-${account_id}.json") IAM roles"; jq -c '.Roles[]' "/tmp/iam-roles-${account_id}.json" | grep -F irsa. | grep -vF "${capi_base_domain}:sub" `# filter out roles that already trust the new base domain` | jq -r '.Arn' | sed 's/^/    Affected role: /')
   ```

   With this, you now have a list of affected IAM roles in _one_ account.

5. Update trust policies of the affected IAM roles. They should allow `sts:AssumeRoleWithWebIdentity` for both Vintage and CAPA issuers during the transition period. As an example, the following block shows how the trust policy should look like. The order doesn't matter as long as you trust both the old and new issuer. Make sure to use the correct AWS account ID, issuer domains and `ServiceAccount` references.

   ```json
   {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::1234567890:oidc-provider/irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "ForAnyValue:StringEquals": {
                        "irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net:sub": [
                            "system:serviceaccount:somenamespace:someserviceaccount"
                        ]
                    }
                }
            },
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::1234567890:oidc-provider/irsa.mycluster.capi.acme.net"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "ForAnyValue:StringEquals": {
                        "irsa.mycluster.capi.acme.net:sub": [
                            "system:serviceaccount:somenamespace:someserviceaccount"
                        ]
                    }
                }
            }
        ]
    }
   ```

6. Switch the order of the service account issuers in the cluster values (the values for the cluster-aws chart; specifically `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers`). This will instruct the Kubernetes API to start issuing service account tokens using the CAPI issuer, while still accepting tokens from the vintage issuer. Important notes:
   - This needs to be done **after** all IAM role trust policies have been updated.
   - This will roll the control plane nodes of the cluster.
   - This could be done as part of a planned major cluster upgrade, to make use of an already planned node roll.

   Before:

   ```yaml
   cluster:
     providerIntegration:
         controlPlane:
         kubeadmConfig:
             clusterConfiguration:
             apiServer:
                 serviceAccountIssuers:
                 # Order must be switched from this wrong order...
                 - url: https://irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net # the old one
                 - templateName: awsIrsaServiceAccountIssuer  # the new one (CAPI domain)
   ```

   After applying the new order:

   ```yaml
   cluster:
     providerIntegration:
         controlPlane:
         kubeadmConfig:
             clusterConfiguration:
             apiServer:
                 serviceAccountIssuers:
                 # ... to this correct order:
                 - templateName: awsIrsaServiceAccountIssuer  # the new one (CAPI domain)
                 - url: https://irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net # the old one
   ```

   Make sure you apply the cluster values. To verify that the new values actually arrived on the cluster, you can check if the control plane nodes rolled, or to be very exact, run:

   ```sh
   kubectl get pod -n kube-system -l component=kube-apiserver -o yaml | grep -E 'name: kube-apiserver-|--service-account-issuer'
   ```

7. Wait until all service account tokens have been renewed:
   - For [bound service account tokens](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume) this happens either when the Pod gets deleted or after a defined lifespan (1 hour by default). This could be forced by rolling all the worker nodes, which would delete and re-schedule all `Pods`.
   - If [long-lived tokens are in use via `Secret` objects](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#manual-secret-management-for-serviceaccounts), these will need to be re-created and re-distributed manually.
8. Remove the vintage issuer from the cluster configuration values. Specifically, you want to use the default, so please completely **remove** the whole array `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers` from your cluster values. That means to only use the new issuer. Some clusters may still have the older key name `internal.migration.irsaAdditionalDomain` which you should also remove now. Important notes:
   - All Service Account tokens issued by the vintage issuer will no longer be accepted by the cluster's Kubernetes API, so make sure to wait until all tokens are renewed (see previous step).
   - This will roll the control plane nodes of the cluster.
   - This could be done as part of a planned major cluster upgrade, to make use of an already planned node roll.
9. (Optional) Update all the AWS IAM Roles used by a `ServiceAccount` via IRSA, to remove the vintage issuer from their trust policy.

## DNS hosted zones and Kubernetes API endpoint

The DNS setup changes for the workload clusters. The new management cluster has a new DNS hosted zone allocated in AWS. In the vintage setup, the hosted zone contained the management and the workload cluster name in the domain (example: `irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net`), for API and other components, meanwhile in the CAPI setup the DNS structure is more flexible not containing the management cluster name (example: `irsa.mycluster.capi.acme.net`). Both the old and new hosted zones will be available for a while to ensure a smooth transition, but customers should migrate the DNS records to the new zone.

Examples:

- `api.<cluster domain>` for Kubernetes API access, for example in your existing kubeconfigs (in CI/CD/GitOps pipeline configs, on users' computers, etc.)
- `irsa.<cluster domain>` is covered by the above section
- `*.<cluster domain>` is typically configured as the wildcard domain of the cluster and used for `Ingress` resources. That means any application subdomains could be served in the old hosted zone but should be migrated to the new one. It depends on your applications how that can be done. Feel free to contact Giant Swarm engineers for tips and help.

### Cluster manifest cleanup

There are some fields in the cluster manifest that are only used during the migration, and can be cleaned up afterward. We tried to make sure that our migration tool cleaned up the manifests and removed those fields automatically after a successful migration. But there could be some leftovers, or it could be that a cluster got migrated before that cleanup was implemented in the tool. Below, you'll find a list of the fields that can be cleaned up (or modified) after a successful migration:

- `cluster.internal.advancedConfiguration.controlPlane.etcd`: can be completely removed
- `cluster.internal.advancedConfiguration.controlPlane.files`: besides the following files, all other files in the list can be deleted

    - Keep `/migration/add-vintage-service-account-key.sh` and `/etc/kubernetes/pki/sa-old.pem` until you have complete the section [OIDC providers (service account issuers) and IAM policies](#oidc-providers-service-account-issuers-and-iam-policies)
- `cluster.internal.advancedConfiguration.controlPlane.preKubeadmCommands`: everything except the following fields can be deleted

    - Keep `/bin/sh /migration/add-vintage-service-account-key.sh` until you have completed the section [OIDC providers (service account issuers) and IAM policies](#oidc-providers-service-account-issuers-and-iam-policies)
- `cluster.internal.advancedConfiguration.controlPlane.postKubeadmCommands`: can be completely removed
- `internal.migration.irsaAdditionalDomain`: starting from release v25.1.1 this domain needs to be appended to `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers`, and the `internal.migration.irsaAdditionalDomain` field can be removed

Here's an example manifest, and a diff with the proposed changes:

```yaml
apiVersion: v1
data:
  values: |
    global:
        metadata:
            name: mycluster
            description: example
            organization: acme
            servicePriority: medium
        controlPlane:
            instanceType: m6i.2xlarge
        release:
            version: 25.0.0
        nodePools:
            main:
                availabilityZones:
                    - eu-west-1a
                instanceType: m6a.2xlarge
                minSize: 1
                maxSize: 9
        providerSpecific:
            region: eu-west-1
    internal:
        migration:
            irsaAdditionalDomain: irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net
    cluster:
        internal:
            advancedConfiguration:
                controlPlane:
                    apiServer:
                        bindPort: 443
                        etcdPrefix: giantswarm.io
                        extraCertificateSANs:
                            - api.mycluster.k8s.myoldmanagementcluster.vintage.acme.net
                    etcd:
                        initialClusterState: existing
                        experimental:
                            peerSkipClientSanVerification: true
                    files:
                        - contentFrom:
                            secret:
                                name: mycluster-migration-custom-files
                                key: join-etcd-cluster
                          path: /migration/join-existing-cluster.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: mycluster-migration-custom-files
                                key: move-etcd-leader
                          path: /migration/move-etcd-leader.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: mycluster-migration-custom-files
                                key: api-healthz-vintage-pod
                          path: /etc/kubernetes/manifests/api-healthz-vintage-pod.yaml
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: mycluster-migration-custom-files
                                key: add-extra-service-account-key
                          path: /migration/add-vintage-service-account-key.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: mycluster-sa-old
                                key: tls.key
                          path: /etc/kubernetes/pki/sa-old.pem
                          permissions: "0640"
                    preKubeadmCommands:
                        - 'iptables -A PREROUTING -t nat  -p tcp --dport 6443 -j REDIRECT --to-port 443 # route traffic from 6443 to 443'
                        - 'iptables -t nat -A OUTPUT -p tcp --destination 127.0.0.1 --dport 6443 -j REDIRECT --to-port 443 # include localhost'
                        - /bin/sh /migration/join-existing-cluster.sh
                        - /bin/sh /migration/add-vintage-service-account-key.sh
                        - sleep 90
                    postKubeadmCommands:
                        - /bin/sh /migration/move-etcd-leader.sh
kind: ConfigMap
metadata:
  labels:
    giantswarm.io/cluster: mycluster
  name: mycluster-userconfig
  namespace: org-acme
```

Diff:

```diff
--- one.yaml  2024-11-21 14:20:41
+++ two.yaml  2024-11-21 14:20:53
@@ -20,9 +20,6 @@
                 maxSize: 9
         providerSpecific:
             region: eu-west-1
-    internal:
-        migration:
-            irsaAdditionalDomain: irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net
     cluster:
         internal:
             advancedConfiguration:
@@ -32,43 +29,23 @@
                         etcdPrefix: giantswarm.io
                         extraCertificateSANs:
                             - api.mycluster.k8s.myoldmanagementcluster.vintage.acme.net
-                    etcd:
-                        initialClusterState: existing
-                        experimental:
-                            peerSkipClientSanVerification: true
                     files:
-                        - contentFrom:
-                            secret:
-                                name: mycluster-migration-custom-files
-                                key: join-etcd-cluster
-                          path: /migration/join-existing-cluster.sh
-                          permissions: "0644"
-                        - contentFrom:
-                            secret:
-                                name: mycluster-migration-custom-files
-                                key: move-etcd-leader
-                          path: /migration/move-etcd-leader.sh
-                          permissions: "0644"
-                        - contentFrom:
-                            secret:
-                                name: mycluster-migration-custom-files
-                                key: api-healthz-vintage-pod
-                          path: /etc/kubernetes/manifests/api-healthz-vintage-pod.yaml
-                          permissions: "0644"
                         - contentFrom:
                             secret:
                                 name: mycluster-migration-custom-files
                                 key: add-extra-service-account-key
                           path: /migration/add-vintage-service-account-key.sh
                           permissions: "0644"
                           - contentFrom:
                            secret:
                                name: mycluster-sa-old
                                key: tls.key
                          path: /etc/kubernetes/pki/sa-old.pem
                          permissions: "0640"
                     preKubeadmCommands:
-                        - 'iptables -A PREROUTING -t nat  -p tcp --dport 6443 -j REDIRECT --to-port 443 # route traffic from 6443 to 443'
-                        - 'iptables -t nat -A OUTPUT -p tcp --destination 127.0.0.1 --dport 6443 -j REDIRECT --to-port 443 # include localhost'
-                        - /bin/sh /migration/join-existing-cluster.sh
                         - /bin/sh /migration/add-vintage-service-account-key.sh
-                        - sleep 90
-                    postKubeadmCommands:
-                        - /bin/sh /migration/move-etcd-leader.sh
+        providerIntegration:
+            controlPlane:
+                kubeadmConfig:
+                    clusterConfiguration:
+                        apiServer:
+                            serviceAccountIssuers:
+                                - url: https://irsa.mycluster.k8s.myoldmanagementcluster.vintage.acme.net
+                                - templateName: awsIrsaServiceAccountIssuer
 kind: ConfigMap
 metadata:
   labels:
```
