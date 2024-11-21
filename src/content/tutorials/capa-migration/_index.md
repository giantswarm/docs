---
title: CAPA migration
description: Learn how the Vintage-to-CAPI migration works, and how to resolve some of the known issues.
weight: 60
menu:
  principal:
    parent: tutorials
    identifier: tutorials-capa-migration
last_review_date: 2024-11-21
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
---

## Post-migration clean-up

There are some fields in the cluster manifest that are only used during the migration, and can be cleaned up afterward. We try to make sure our migration tool cleans up the manifests and removes those fields automatically after a successful migration, but there could be some left-overs, or it could be that a cluster got migrated before that clean-up process got implemented in the tool. Bellow you'll find a non-exhaustive list of the fields that can be cleaned up (or modified) after a successful migration:

- `cluster.internal.advancedConfiguration.controlPlane.etcd`: can be completely removed
- `cluster.internal.advancedConfiguration.controlPlane.files`: everything except the following fields can be deleted
    - To be kept
        - `/migration/add-vintage-service-account-key.sh`
        - `/etc/kubernetes/pki/sa-old.pem`
- `cluster.internal.advancedConfiguration.controlPlane.{preKubeadmCommands,postKubeadmCommands}`: everything except the following fields can be deleted
    - To be kept
        - `/bin/sh /migration/add-vintage-service-account-key.sh`
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
            irsaAdditionalDomain: irsa.foo.k8s.bar.acme.net
    cluster:
        internal:
            advancedConfiguration:
                controlPlane:
                    apiServer:
                        bindPort: 443
                        etcdPrefix: giantswarm.io
                        extraCertificateSANs:
                            - api.foo.k8s.bar.acme.net
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
                                key: add-extra-service-account-issuers
                          path: /migration/add-vintage-service-account-issuers.sh
                          permissions: "0644"
                    preKubeadmCommands:
                        - 'iptables -A PREROUTING -t nat  -p tcp --dport 6443 -j REDIRECT --to-port 443 # route traffic from 6443 to 443'
                        - 'iptables -t nat -A OUTPUT -p tcp --destination 127.0.0.1 --dport 6443 -j REDIRECT --to-port 443 # include localhost'
                        - /bin/sh /migration/join-existing-cluster.sh
                        - /bin/sh /migration/add-vintage-service-account-issuers.sh
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
-            irsaAdditionalDomain: irsa.foo.k8s.bar.acme.net
     cluster:
         internal:
             advancedConfiguration:
@@ -32,43 +29,23 @@
                         etcdPrefix: giantswarm.io
                         extraCertificateSANs:
                             - api.foo.k8s.bar.acme.net
-                    etcd:
-                        initialClusterState: existing
-                        experimental:
-                            peerSkipClientSanVerification: true
                     files:
                         - contentFrom:
                             secret:
                                 name: foo-migration-custom-files
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
-                        - contentFrom:
-                            secret:
-                                name: foo-migration-custom-files
                                 key: add-extra-service-account-issuers
                           path: /migration/add-vintage-service-account-issuers.sh
                           permissions: "0644"
                     preKubeadmCommands:
-                        - 'iptables -A PREROUTING -t nat  -p tcp --dport 6443 -j REDIRECT --to-port 443 # route traffic from 6443 to 443'
-                        - 'iptables -t nat -A OUTPUT -p tcp --destination 127.0.0.1 --dport 6443 -j REDIRECT --to-port 443 # include localhost'
-                        - /bin/sh /migration/join-existing-cluster.sh
                         - /bin/sh /migration/add-vintage-service-account-issuers.sh
-                        - sleep 90
-                    postKubeadmCommands:
-                        - /bin/sh /migration/move-etcd-leader.sh
+        providerIntegration:
+            controlPlane:
+                kubeadmConfig:
+                    clusterConfiguration:
+                        apiServer:
+                            serviceAccountIssuers:
+                                - url: https://irsa.foo.k8s.bar.acme.net
+                                - templateName: awsIrsaServiceAccountIssuer
 kind: ConfigMap
 metadata:
   labels:
```
