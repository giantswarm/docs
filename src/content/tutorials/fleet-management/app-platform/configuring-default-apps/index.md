---
linkTitle: Customizing default apps
title: Customizing default apps
description: How to customize default apps configuration using the cluster chart values.
weight: 50
aliases:
  - /getting-started/app-platform/configuring-default-apps
  - /vintage/getting-started/app-platform/configuring-default-apps
menu:
  principal:
    parent: tutorials-fleet-management-app-platform
    identifier: tutorials-fleet-management-app-platform-app-default-apps
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How can I customize preinstalled apps configuration?
  - How can I customize default apps configuration?
  - How can I pass custom values to default apps?
  - How can I configure aws-ebs-csi-driver?
last_review_date: 2026-01-15
---

Every workload cluster has a set of apps installed automatically at creation time, called default apps. Default apps are defined in the [cluster chart](https://github.com/giantswarm/cluster) and provider-specific charts (like [cluster-aws](https://github.com/giantswarm/cluster-aws)). These include essential applications like CoreDNS, Cilium, and cloud provider integrations.

While the default configuration works for most cases, sometimes customization is needed. This guide explains how to customize default apps using the cluster chart values.

## App deployment mechanism

Default applications are deployed using two mechanisms:

- **App CR** - Giant Swarm's in-house app management
- **HelmRelease CR** - Flux CD's Helm controller

## Understanding app keys

Each default app has a `configKey` that identifies it in the values structure. You customize apps under `global.apps.<configKey>`.

### List of default apps

These apps are deployed on all clusters regardless of the infrastructure provider:

| Application                                                                                                 | Config Key | Mechanism |
|-------------------------------------------------------------------------------------------------------------|------------|-----------|
| [Cilium](https://github.com/giantswarm/cilium-app)                                                          | `cilium` | `HelmRelease` |
| [CoreDNS](https://github.com/giantswarm/coredns-app)                                                        | `coreDns` | `HelmRelease` |
| [network-policies-app](https://github.com/giantswarm/network-policies-app)                                      | `networkPolicies` | `HelmRelease` |
| [node-problem-detector-app](https://github.com/giantswarm/node-problem-detector-app)                            | `nodeProblemDetector` | `HelmRelease` |
| [vertical-pod-autoscaler-crd](https://github.com/giantswarm/vertical-pod-autoscaler-crd)                    | `verticalPodAutoscalerCrd` | `HelmRelease` |
| [cert-exporter](https://github.com/giantswarm/cert-exporter)                                                | `certExporter` | `App` |
| [cert-manager](https://github.com/giantswarm/cert-manager-app)                                              | `certManager` | `App` |
| [chart-operator-extensions](https://github.com/giantswarm/chart-operator-extensions)                        | `chartOperatorExtensions` | `App` |
| [cilium-servicemonitors-app](https://github.com/giantswarm/cilium-servicemonitors-app)                          | `ciliumServiceMonitors` | `App` |
| [cluster-autoscaler-app](https://github.com/giantswarm/cluster-autoscaler-app)                                  | `clusterAutoscaler` | `App` |
| [coredns-extensions](https://github.com/giantswarm/coredns-extensions)                                      | `coreDnsExtensions` | `App` |
| [etcd-defrag](https://github.com/giantswarm/etcd-defrag-app)                                                | `etcdDefrag` | `App` |
| [etcd-kubernetes-resources-count-exporter](https://github.com/giantswarm/etcd-kubernetes-resources-count-exporter) | `etcdKubernetesResourcesCountExporter` | `App` |
| [external-dns-app](https://github.com/giantswarm/external-dns-app)                                              | `externalDns` | `App` |
| [k8s-audit-metrics](https://github.com/giantswarm/k8s-audit-metrics)                                        | `k8sAuditMetrics` | `App` |
| [k8s-dns-node-cache-app](https://github.com/giantswarm/k8s-dns-node-cache-app)                                  | `k8sDnsNodeCache` | `App` |
| [metrics-server-app](https://github.com/giantswarm/metrics-server-app)                                          | `metricsServer` | `App` |
| [net-exporter](https://github.com/giantswarm/net-exporter)                                                  | `netExporter` | `App` |
| [node-exporter-app](https://github.com/giantswarm/node-exporter-app)                                            | `nodeExporter` | `App` |
| [observability-bundle](https://github.com/giantswarm/observability-bundle)                                  | `observabilityBundle` | `App` |
| [observability-policies-app](https://github.com/giantswarm/observability-policies-app)                          | `observabilityPolicies` | `App` |
| [prometheus-blackbox-exporter](https://github.com/giantswarm/prometheus-blackbox-exporter)                  | `prometheusBlackboxExporter` | `App` |
| [security-bundle](https://github.com/giantswarm/security-bundle)                                            | `securityBundle` | `App` |
| [teleport-kube-agent-app](https://github.com/giantswarm/teleport-kube-agent-app)                                | `teleportKubeAgent` | `App` |
| [vertical-pod-autoscaler-app](https://github.com/giantswarm/vertical-pod-autoscaler-app)                        | `verticalPodAutoscaler` | `App` |

### AWS provider apps

These apps are specific to clusters running on AWS:

| Application                                                                                            | Config Key | Mechanism |
|--------------------------------------------------------------------------------------------------------|------------|-----------|
| [aws-cloud-controller-manager-app](https://github.com/giantswarm/aws-cloud-controller-manager-app)     | `awsCloudControllerManager` | `HelmRelease` |
| [aws-ebs-csi-driver-app](https://github.com/giantswarm/aws-ebs-csi-driver-app)                         | `awsEbsCsiDriver` | `HelmRelease` |
| [Karpenter](https://github.com/giantswarm/karpenter-app)                                               | `karpenter` | `HelmRelease` |
| [aws-ebs-csi-driver-servicemonitors](https://github.com/giantswarm/aws-ebs-csi-driver-servicemonitors) | `awsEbsCsiDriverServiceMonitors` | `App` |
| [aws-pod-identity-webhook](https://github.com/giantswarm/aws-pod-identity-webhook)                     | `awsPodIdentityWebhook` | `App` |
| [IRSA-servicemonitors](https://github.com/giantswarm/irsa-servicemonitors)                             | `irsaServiceMonitors` | `App` |

### Azure provider apps

These apps are specific to clusters running on Azure:

| Application | Config Key | Mechanism |
|-------------|------------|-----------|
| [azure-cloud-controller-manager-app](https://github.com/giantswarm/azure-cloud-controller-manager-app) | `azureCloudControllerManager` | `HelmRelease` |
| [azure-cloud-node-manager-app](https://github.com/giantswarm/azure-cloud-node-manager-app) | `azureCloudNodeManager` | `HelmRelease` |
| [azuredisk-csi-driver-app](https://github.com/giantswarm/azuredisk-csi-driver-app) | `azureDiskCsiDriver` | `HelmRelease` |
| [azurefile-csi-driver-app](https://github.com/giantswarm/azurefile-csi-driver-app) | `azureFileCsiDriver` | `HelmRelease` |

### vSphere provider apps

These apps are specific to clusters running on vSphere:

| Application | Config Key | Mechanism |
|-------------|------------|-----------|
| [cloud-provider-vsphere-app](https://github.com/giantswarm/cloud-provider-vsphere-app) | `cloudProviderVsphere` | `HelmRelease` |
| [kube-vip](https://github.com/giantswarm/kube-vip-app) | `kubeVip` | `HelmRelease` |
| [kube-vip Cloud Provider](https://github.com/giantswarm/kube-vip-cloud-provider-app) | `kubeVipCloudProvider` | `HelmRelease` |
| [vsphere-csi-driver-app](https://github.com/giantswarm/vsphere-csi-driver-app) | `vsphereCsiDriver` | `HelmRelease` |

### VMware Cloud Director provider apps

These apps are specific to clusters running on VMware Cloud Director:

| Application | Config Key | Mechanism |
|-------------|------------|-----------|
| [cloud-provider-cloud-director-app](https://github.com/giantswarm/cloud-provider-cloud-director-app) | `cloudProviderCloudDirector` | `HelmRelease` |

For a complete and up-to-date list, check the `values.schema.json` in your provider's cluster chart.

## Find out what configuration can be changed

To find available configuration options for each app, refer to the app's default values file in its GitHub repository.

For example, for [CoreDNS](https://github.com/giantswarm/coredns-app), check [helm/coredns-app/values.yaml](https://github.com/giantswarm/coredns-app/blob/main/helm/coredns-app/values.yaml).

If you can't find the values file for an app, reach out to your account engineer.

## Method 1: Inline values

Pass Helm values directly in your cluster values file under `global.apps.<configKey>.values`:

```yaml
global:
  apps:
    coreDns:
      values:
        ConfigMap:
          cache: 15
```

This example reduces the CoreDNS cache lifetime from the default 30 seconds to 15 seconds.

## Method 2: External ConfigMaps or Secrets

For larger configurations or when sharing settings across clusters, reference external ConfigMaps or Secrets using `global.apps.<configKey>.extraConfigs`:

```yaml
global:
  apps:
    awsEbsCsiDriver:
      extraConfigs:
        - kind: ConfigMap
          name: my-ebs-custom-values
          optional: false
```

The referenced resource must:

- Exist in the same namespace as the cluster
- Have values under a key named `values`

### For HelmRelease-based Apps

The `extraConfigs` field uses:

- `kind`: `ConfigMap` or `Secret` (PascalCase)
- `optional`: boolean - if `true`, missing resources are ignored

### For App CR-based Apps

The `extraConfigs` field uses:

- `kind`: `configMap` or `secret` (camelCase)
- `priority`: integer (1-150, default 25) - higher priority values override lower ones

### Creating the ConfigMap

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-ebs-custom-values
  namespace: org-myorg
data:
  values: |
    controller:
      resources:
        limits:
          memory: 512Mi
    node:
      tolerateAllTaints: true
```

Create it with kubectl:

```shell
kubectl apply -f my-ebs-custom-values.yaml
```

### Using Secrets for sensitive data

For confidential configuration, use a Secret instead:

```yaml
global:
  apps:
    certManager:
      extraConfigs:
        - kind: Secret
          name: cert-manager-credentials
          optional: false
```

## Combining both methods

You can use both methods together. Values are merged in this order (later values override earlier):

1. Default provider-independent values (from the chart)
2. Default provider-specific values (from the provider chart)
3. Values from `extraConfigs` (in the order listed)
4. Inline `values` (highest priority)

```yaml
global:
  apps:
    awsEbsCsiDriver:
      extraConfigs:
        - kind: ConfigMap
          name: org-wide-ebs-settings
          optional: true
        - kind: Secret
          name: ebs-sensitive-config
          optional: false
      values:
        # These values override everything above
        controller:
          logLevel: debug
```

## Complete example

Here's a complete cluster values example customizing multiple default apps:

```yaml
global:
  metadata:
    name: my-cluster
    organization: myorg

  apps:
    # Customize CoreDNS
    coreDns:
      values:
        ConfigMap:
          cache: 15

    # Customize Cilium
    cilium:
      values:
        hubble:
          relay:
            enabled: true
          ui:
            enabled: true

    # Customize cert-manager with external config
    certManager:
      extraConfigs:
        - kind: configMap
          name: cert-manager-org-config
          optional: true
      values:
        dns01RecursiveNameserversOnly: true
```

## Troubleshooting

**Values not applied**: Ensure your config key matches exactly (case-sensitive). For example, use `coreDns` not `coredns`.

**ConfigMap not found**: Verify the ConfigMap or Secret exists in the cluster's namespace before creating the cluster.

**Merge conflicts**: Remember that inline `values` always take highest priority over `extraConfigs`.

## Further reading

- [cluster chart repository](https://github.com/giantswarm/cluster) - Provider-independent base chart
- [cluster-aws chart repository](https://github.com/giantswarm/cluster-aws) - AWS provider chart
- [cluster-azure chart repository](https://github.com/giantswarm/cluster-azure) - Azure provider chart
- [cluster-vsphere chart repository](https://github.com/giantswarm/cluster-vsphere) - vSphere provider chart
- [cluster-cloud-director chart repository](https://github.com/giantswarm/cluster-cloud-director) - VMware Cloud Director provider chart
- [App configuration]({{< relref "/tutorials/fleet-management/app-platform/app-configuration" >}}) - General app configuration practices
