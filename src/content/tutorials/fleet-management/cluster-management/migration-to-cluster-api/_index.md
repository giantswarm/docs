---
title: Migration to Cluster API
description: How the migration from our old AWS vintage management clusters to Cluster API works.
weight: 20
menu:
  principal:
    parent: tutorials-fleet-management-clusters
    identifier: tutorials-fleet-management-migration-to-cluster-api
last_review_date: 2024-05-02
owner:
  - https://github.com/orgs/giantswarm/teams/sig-docs
user_questions:
  - What are the requirements for migrating a cluster to Cluster API?
  - What are the recommendations for a smooth migration?
---

From the outset, Giant Swarm has utilized Kubernetes to build platforms. In the early years, everybody was still figuring out how to manage Kubernetes lifecycle across a fleet of clusters. We built our own tooling, largely based on [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/), which worked well for us and our customers. As the Kubernetes project and the community around it evolved, it became clear that many companies in the ecosystem were trying to solve the same fundamental challenges regarding cluster lifecycle management. With our extensive experience, we saw an opportunity to contribute to a broader solution. We pushed for a joint effort to build a standardized method for cluster lifecycle management. [Cluster API]({{< relref "/overview/fleet-management/cluster-management/introduction-cluster-api" >}}) is backed by the Kubernetes community and covers different providers like AWS, Azure, GCP, and others.

This guide outlines the migration path from our AWS vintage platform to the [Cluster API](https://cluster-api.sigs.k8s.io/) (CAPI) standard, ensuring a seamless transition for customer workload clusters from the previous system to the modern CAPI framework. Within this document, you'll find an overview of the migration procedure in AWS, including its prerequisites and strategic advice, all aimed at facilitating a smooth and successful transition.

## Pre-migration requirements

Before you begin the migration:

1. Your cluster should be at least on a AWS vintage version [`20.0.0`](/changes/workload-cluster-releases-aws/releases/aws-v20.0.0/).
2. The AWS IAM role, with the specific name `giantswarm-{CAPI_MC_NAME}-capa-controller`, must be created for the workload cluster's (WC) AWS account before starting the migration. [For more information please refer to this guide]({{< relref "/vintage/getting-started/cloud-provider-accounts/cluster-api/aws/" >}}).
3. In case of using GitOps, Flux must be turned off during the migration since some of the cluster custom resources will be modified or removed by the migration scripts.

__Note:__ The `CAPI_MC_NAME` is the name of the management cluster (MC) where the Cluster API controllers are installed.

## Recommendations for a smooth migration

We also recommend increasing the size of your "master" node instance type to 2x or 3x its normal size for the duration of the migration (for example `m5.large` to `m5.4xlarge`). This ensures the API server can handle the load during the migration, since there might only be one node to handle the traffic at certain points throughout the process.

## The migration process

The migration process consists of several steps:

0. __New CAPA cluster provision:__ First of all, a new management cluster is created in AWS using the Cluster API flavour (CAPA). This management cluster will have all the necessary controllers to manage the workload clusters once migrated. At the same time a new host zone is created in Route53 for the new management cluster.
1. __Initialization:__ Necessary Kubernetes access credentials and AWS credentials are retrieved. The Vault client is created to interact with the Vault instance containing all security assets of the cluster.
2. __Preparation:__ Migration of secrets to the CAPI management cluster, including CA certs, encryption provider secrets, and service account secrets. Migration scripts are created as secrets in the CAPI management cluster. Additionally, AWS credentials for the cluster are migrated by creating an `AWSClusterRoleIdentity` in the CAPI management cluster. Certain operations are performed to avoid conflicts during migration, such as disabling machine health check on the vintage cluster resources, scaling down the app operator for the migrated workload cluster, or cleaning up certain charts.
3. __Stopping vintage cluster resource reconciliation:__ To avoid conflicts, vintage reconciliation is stopped by removing all `aws-operator` labels from the vintage cluster resource.
4. __Cluster API cluster provisioning:__ Generation and application of CAPI cluster templates. A separate routine runs in the background to ensure the old load balancer remains active. The tool waits until at least one CAPI control-plane node joins the cluster and is in a `Ready` state. Various operations are performed to ensure a smooth transition, such as stopping control-plane components on the vintage cluster, cordoning all vintage control-planes, and deleting certain pods to speed up installation and updates.
5. __Cleaning the vintage cluster:__ All vintage control-plane nodes are drained, vintage auto scaling groups are deleted, and all worker nodes for each node pool are drained and deleted.

__Note:__ The migration process is automated and executed by our engineers. The process is monitored and controlled by a set of scripts and tools to ensure a smooth transition. We don't expect any downtime for the workload clusters during the migration process.

## Post-migration tasks

Our engineers will check that all resources and infrastructure are correctly migrated and that the new cluster is working as expected. There are some remaining tasks that need to be done by the customer:

- The DNS setup changes for the workload clusters. The new management cluster has a new host zone allocated in AWS. In the vintage setup, the host zone contained the management and the workload cluster name in the domain, for API and other components, meanwhile in the CAPI setup the DNS structure is more flexible not containing the management cluster name. Both the old and new host zones will be available for a certain period to ensure a smooth transition, but customers should migrate the DNS records to the new host zone as soon as possible in case they're using cluster wildcard DNS records.

- In case of using GitOps or any other tool pushing the state to the management cluster, the tool should be reconfigured to use the new customer resources used by Cluster API. In order to know which resources need to be updated, created or removed please run `kubectl gs template cluster --provider capa` and compare the output with the current resources in the management cluster. Our account engineers will help with this process providing the exact resources that need to be updated.

- Some customers have been using [k8s-initiator-app](https://github.com/giantswarm/k8s-initiator-app/) to configure some aspects of the workload cluster API.
  In the new Cluster API implementation, [most of the features enabled by the app](https://github.com/giantswarm/capi-migration-cli/tree/main/k8s-initiator-features) are now supported natively by the platform. The app should be removed and moved to the new syntax if our migration CLI doesn't handle your use-case. Giant Swarm account engineers will help you with this process.

- [Service Account issuer switch](#service-account-issuer-switch)

- [Cluster manifest clean-up](#cluster-manifest-clean-up)

### Service Account issuer switch

For context, a cluster's service account issuer is an OIDC provider that signs and issues the tokens for the cluster's Service Accounts. These service accounts can then be used to authenticate workloads against the Kubernetes API and the AWS API via IRSA.

In CAPA, since the cluster domain name changes from vintage, a new service account issuer has also been introduced. To make for a smooth migration though, we support defining multiple issuers in a cluster. This way, service account tokens issued by all the defined issuers will be accepted in the cluster's Kubernetes API. The accepted issuers are defined in `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers` in the cluster app values (order matters as we'll see below).

After a cluster is migrated to CAPI, the vintage service account issuer needs to be phased out, since it's tied to the vintage cluster domain name, which will also be phased out eventually. This is a gradual, multi-step process that will require rolling the master nodes in multiple phases.

1. Update the trust policy for all the AWS IAM Roles used by a `ServiceAccount` via IRSA. The trust policy should allow `sts:AssumeRoleWithWebIdentity` for both Vintage and CAPA issuers during the transition period. As an example, this is how the trust policy of the IAM roles would look like (make sure to use the correct AWS account ID, issuer domains and `ServiceAccount` references):

   ```json
   {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::1234567890:oidc-provider/irsa.foo.k8s.vintage.acme.net"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "ForAnyValue:StringEquals": {
                        "irsa.foo.k8s.vintage.acme.net:sub": [
                            "system:serviceaccount:somenamespace:someserviceaccount"
                        ]
                    }
                }
            },
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "arn:aws:iam::1234567890:oidc-provider/irsa.foo.capi.acme.net"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "ForAnyValue:StringEquals": {
                        "irsa.foo.capi.acme.net:sub": [
                            "system:serviceaccount:somenamespace:someserviceaccount"
                        ]
                    }
                }
            }
        ]
    }
   ```

2. Switch the order of the service account issuers in the cluster values (`cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers`). This will instruct the Kubernetes API to start issuing service account tokens using the CAPI issuer, while still accepting tokens from the vintage issuer. Important notes:
   - This needs to be done __after__ all IAM role trust policies have been updated (step 1.).
   - This will roll the master nodes of the cluster.
   - This could be done as part of a planned major cluster upgrade, to make use of an already planned node roll.
3. Wait until all service account tokens have been renewed
   - For [bound service account tokens](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#bound-service-account-token-volume) this happens either when the Pod gets deleted or after a defined lifespan (1 hour by default). This could be forced by rolling all the worker nodes, which would delete and re-schedule all `Pods`.
   - If [long-lived tokens are in use via `Secret` objects](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/#manual-secret-management-for-serviceaccounts), these will need to be re-created and re-distributed manually.
4. Remove the vintage issuer from the cluster configuration values (`cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers`). Important notes:
   - All Service Account tokens issued by the Vintage issuer will no longer be accepted by the cluster's Kubernetes API, so make sure all tokens are renewed (step 3.).
   - This will roll the master nodes of the cluster.
   - This could be done as part of a planned major cluster upgrade, to make use of an already planned node roll.
5. (Optional) Update all the AWS IAM Roles used by a `ServiceAccount` via IRSA, to remove the Vintage issuer from their trust policy

### Cluster manifest clean-up

There are some fields in the cluster manifest that are only used during the migration, and can be cleaned up afterward. We try to make sure our migration tool cleans up the manifests and removes those fields automatically after a successful migration, but there could be some left-overs, or it could be that a cluster got migrated before that clean-up process got implemented in the tool. Below, you'll find a non-exhaustive list of the fields that can be cleaned up (or modified) after a successful migration:

- `cluster.internal.advancedConfiguration.controlPlane.etcd`: can be completely removed
- `cluster.internal.advancedConfiguration.controlPlane.files`: besides the following files, all other files in the list can be deleted
    - To be kept
        - `/migration/add-vintage-service-account-key.sh`
        - `/etc/kubernetes/pki/sa-old.pem`
- `cluster.internal.advancedConfiguration.controlPlane.preKubeadmCommands`: everything except the following fields can be deleted
    - To be kept
        - the two `iptables` commands
        - `/bin/sh /migration/add-vintage-service-account-key.sh`
- `cluster.internal.advancedConfiguration.controlPlane.postKubeadmCommands`: can be completely removed
- `internal.migration.irsaAdditionalDomain`: starting from release v25.1.1 this domain needs to be appended to `cluster.providerIntegration.controlPlane.kubeadmConfig.clusterConfiguration.apiServer.serviceAccountIssuers`, and the `internal.migration.irsaAdditionalDomain` field can be removed

Here's an example manifest, and a diff with the proposed changes:

```yaml
apiVersion: v1
data:
  values: |
    global:
        metadata:
            name: foo
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
            irsaAdditionalDomain: irsa.foo.k8s.vintage.acme.net
    cluster:
        internal:
            advancedConfiguration:
                controlPlane:
                    apiServer:
                        bindPort: 443
                        etcdPrefix: giantswarm.io
                        extraCertificateSANs:
                            - api.foo.k8s.vintage.acme.net
                    etcd:
                        initialClusterState: existing
                        experimental:
                            peerSkipClientSanVerification: true
                    files:
                        - contentFrom:
                            secret:
                                name: foo-migration-custom-files
                                key: join-etcd-cluster
                          path: /migration/join-existing-cluster.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: foo-migration-custom-files
                                key: move-etcd-leader
                          path: /migration/move-etcd-leader.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: foo-migration-custom-files
                                key: api-healthz-vintage-pod
                          path: /etc/kubernetes/manifests/api-healthz-vintage-pod.yaml
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: foo-migration-custom-files
                                key: add-extra-service-account-key
                          path: /migration/add-vintage-service-account-key.sh
                          permissions: "0644"
                        - contentFrom:
                            secret:
                                name: foo-sa-old
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
    giantswarm.io/cluster: foo
  name: foo-userconfig
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
-            irsaAdditionalDomain: irsa.foo.k8s.vintage.acme.net
     cluster:
         internal:
             advancedConfiguration:
@@ -32,43 +29,23 @@
                         etcdPrefix: giantswarm.io
                         extraCertificateSANs:
                             - api.foo.k8s.vintage.acme.net
-                    etcd:
-                        initialClusterState: existing
-                        experimental:
-                            peerSkipClientSanVerification: true
                     files:
-                        - contentFrom:
-                            secret:
-                                name: foo-migration-custom-files
-                                key: join-etcd-cluster
-                          path: /migration/join-existing-cluster.sh
-                          permissions: "0644"
-                        - contentFrom:
-                            secret:
-                                name: foo-migration-custom-files
-                                key: move-etcd-leader
-                          path: /migration/move-etcd-leader.sh
-                          permissions: "0644"
-                        - contentFrom:
-                            secret:
-                                name: foo-migration-custom-files
-                                key: api-healthz-vintage-pod
-                          path: /etc/kubernetes/manifests/api-healthz-vintage-pod.yaml
-                          permissions: "0644"
                         - contentFrom:
                             secret:
                                 name: foo-migration-custom-files
                                 key: add-extra-service-account-key
                           path: /migration/add-vintage-service-account-key.sh
                           permissions: "0644"
                           - contentFrom:
                            secret:
                                name: foo-sa-old
                                key: tls.key
                          path: /etc/kubernetes/pki/sa-old.pem
                          permissions: "0640"
                     preKubeadmCommands:
                         - 'iptables -A PREROUTING -t nat  -p tcp --dport 6443 -j REDIRECT --to-port 443 # route traffic from 6443 to 443'
                         - 'iptables -t nat -A OUTPUT -p tcp --destination 127.0.0.1 --dport 6443 -j REDIRECT --to-port 443 # include localhost'
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
+                                - url: https://irsa.foo.k8s.vintage.acme.net
+                                - templateName: awsIrsaServiceAccountIssuer
 kind: ConfigMap
 metadata:
   labels:
```
