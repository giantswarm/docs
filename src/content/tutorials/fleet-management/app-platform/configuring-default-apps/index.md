---
linkTitle: Customizing default apps
title: Customizing default apps
description: How to customize preinstalled apps configuration using the cluster chart values.
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
last_review_date: 2025-11-28
---

Every workload cluster has a set of apps installed automatically at creation time, called default apps. Default apps are defined in the [cluster chart](https://github.com/giantswarm/cluster) and provider-specific charts (like [cluster-aws](https://github.com/giantswarm/cluster-aws)). These include essential applications like CoreDNS, Cilium, and cloud provider integrations.

While the default configuration works for most cases, sometimes customization is needed. This guide explains how to customize default apps using the cluster chart values.

## Understanding app keys

Each default app has a `configKey` that identifies it in the values structure. You customize apps under `global.apps.<configKey>`.

Common apps and their keys:

| Application | Config Key | Description |
|-------------|------------|-------------|
| AWS EBS CSI Driver | `awsEbsCsiDriver` | EBS volume provisioning (AWS) |
| Cilium | `cilium` | CNI networking |
| CoreDNS | `coreDns` | Cluster DNS |
| cert-manager | `certManager` | Certificate management |
| External DNS | `externalDns` | External DNS integration |
| Cluster Autoscaler | `clusterAutoscaler` | Node autoscaling |
| Vertical Pod Autoscaler | `verticalPodAutoscaler` | Pod resource recommendations |

For a complete list, check the `values.schema.json` in your provider's cluster chart.

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
        configmap:
          cache: 15
```

This example reduces the CoreDNS cache lifetime from the default 30 seconds to 15 seconds.

### AWS EBS CSI Driver example

```yaml
global:
  apps:
    awsEbsCsiDriver:
      values:
        controller:
          resources:
            limits:
              memory: 256Mi
        node:
          tolerateAllTaints: true
```

### Cilium example

```yaml
global:
  apps:
    cilium:
      values:
        hubble:
          relay:
            enabled: true
          ui:
            enabled: true
```

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
        configmap:
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
        - kind: ConfigMap
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
