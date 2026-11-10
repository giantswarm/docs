---
linkTitle: Clusterwide deny
title: Deny network traffic in all namespaces by default
diataxis_content_type: how-to-guide
description: Turn on the clusterwide deny for a workload cluster, keep your workloads reachable with allow labels and a Same-namespace policy, and roll back if something breaks.
weight: 38
menu:
  principal:
    parent: tutorials-connectivity
    identifier: tutorials-connectivity-network-policies
user_questions:
  - How do I deny all network traffic in every namespace by default?
  - How do I exclude a namespace from the clusterwide deny?
  - Which allow labels can I set on a namespace?
  - How do I allow traffic between pods in the same namespace under the clusterwide deny?
  - How do I keep DNS working when I turn on the clusterwide deny?
  - How do I roll back the clusterwide deny?
last_review_date: 2026-11-10
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
---

Every workload cluster runs the `network-policies` app. By default it only denies traffic in the `kube-system` and `giantswarm` namespaces, and your own namespaces are open. The **clusterwide deny** extends this to every namespace: once it's on, a pod can only send or receive traffic that a network policy allows.

This guide explains how to turn the clusterwide deny on, how to keep your workloads working with allow labels and a Same-namespace policy, and how to roll it back.

## Before you start

- The cluster needs a release with `network-policies` v0.6.0 or newer. Check the version in the release notes of your cluster's release.
- Turn the clusterwide deny on only for a running cluster whose default apps are all ready. Never set it in the values you create a cluster with: some default apps can't finish installing under the deny. For the same reason, an app's install or upgrade jobs can fail under the deny if the app doesn't carry its own policies yet.
- Not every Giant Swarm managed app carries its own network policies yet. Check with your account engineer which apps on your cluster are covered before you turn it on.
- The clusterwide deny enforces immediately. There's no audit or dry-run mode. Find out which traffic each of your namespaces needs, and set the allow labels and policies for it first.
- Start on a non-production cluster, see [Rolling it out](#rolling-it-out).

## How the clusterwide deny works

The clusterwide deny is a `CiliumClusterwideNetworkPolicy` named `default-deny-all-namespaces`. It denies all ingress and egress traffic of every pod in every namespace, `kube-system` and `giantswarm` included. Only namespaces with the namespace opt-out label are left out. It replaces the per-namespace `default-deny-all` policies in `kube-system` and `giantswarm`.

For your own namespaces, three things open traffic again:

- **Allow labels** on a namespace put it under a standard allow that Giant Swarm ships, for example for DNS or for the Kubernetes API server.
- A **Same-namespace policy** that you apply lets the pods of a namespace talk to each other.
- Your own network policies, as before, for everything else.

All of these only add allowed traffic. In a namespace without any deny policy they change nothing until the clusterwide deny is on, so you can prepare those namespaces ahead of time. In a namespace that already has its own deny policy, they open that traffic within about a minute.

Any namespace you create after turning on the clusterwide deny is denied from the start. Add its allow labels and Same-namespace policy when you create it.

## Turn on the clusterwide deny

Add the `network-policies` app values to the user configuration of your cluster, under `global.apps.networkPolicies.values`. Merge them into the `values` of the existing `<cluster>-userconfig` ConfigMap instead of replacing it:

```yaml
global:
  apps:
    networkPolicies:
      values:
        denyByDefault:
          clusterWide:
            enabled: true
            # Optional if every namespace carries the allow-dns label, see the warning below.
            allowDNS:
              enabled: true
```

{{% notice warning %}}
Turning on the clusterwide deny cuts DNS in every namespace that has no DNS allow. In the same change, either set `allowDNS.enabled: true` as in the example, or first add the `policy.giantswarm.io/allow-dns` label to every one of your namespaces. Otherwise DNS lookups fail in all your namespaces. If a namespace limits DNS with `rules.dns`, see [Allow DNS for all namespaces](#allow-dns-for-all-namespaces).
{{% /notice %}}

If your cluster reaches the internet through an HTTP proxy, your namespaces also need their own policy for egress to the proxy. If that policy uses `toFQDNs` for the proxy's hostname, it also needs a `rules.dns` rule matching that name, because the `allow-dns` label and the DNS switch don't send lookups through Cilium's DNS proxy.

The deny takes effect as soon as the app is reconciled. To check that it's active:

```nohighlight
kubectl get ciliumclusterwidenetworkpolicies default-deny-all-namespaces
```

Read more about [customizing default apps]({{< relref "/tutorials/fleet-management/app-platform/configuring-default-apps/" >}}).

## Allow DNS for all namespaces

`denyByDefault.clusterWide.allowDNS.enabled` (default `false`) adds a second clusterwide policy, `allow-dns-all-namespaces`. It allows egress to the cluster DNS (CoreDNS, the node-local DNS cache, and `kube-dns` on AKS, the same targets as the `allow-dns` label) for every namespace the clusterwide deny covers. It only has an effect while the clusterwide deny is on.

With `allowDNS` off, which is the more restrictive setting, a namespace only gets DNS through the `policy.giantswarm.io/allow-dns` label or its own policies. `kube-system` and `giantswarm` keep their DNS either way.

{{% notice warning %}}
Both the DNS switch and the `allow-dns` label allow DNS for every name. If a namespace limits DNS to some domains with a Cilium `rules.dns` allow-list, for example to use `toFQDNs`, these allows defeat that list, because any name can then be resolved. If any namespace on the cluster does this, leave `allowDNS` off for the whole cluster, set the `allow-dns` label only on the namespaces that need it, and write the DNS rule of the restricted namespaces in their own policy.
{{% /notice %}}

## Exclude a namespace with the namespace opt-out

Label a namespace with `policy.giantswarm.io/default-deny: "false"` to take it out of the clusterwide deny:

```nohighlight
kubectl label namespace my-namespace policy.giantswarm.io/default-deny=false --overwrite
```

The namespace is then open again, as it was before the clusterwide deny, unless your own policies restrict it. The change takes effect without restarting pods. Remove the label to put the namespace back under the clusterwide deny:

```nohighlight
kubectl label namespace my-namespace policy.giantswarm.io/default-deny-
```

Never set the namespace opt-out on `kube-system` or `giantswarm`. Nothing prevents it, but it removes the deny from Giant Swarm components.

## Open traffic with allow labels

Each allow label puts a namespace under one standard allow. Set the label to `"true"`:

```nohighlight
kubectl label namespace my-namespace policy.giantswarm.io/allow-dns=true policy.giantswarm.io/allow-kube-apiserver=true --overwrite
```

The allow labels and the traffic they open:

| Allow label | Opens | Details |
|---|---|---|
| `policy.giantswarm.io/allow-dns` | Egress to the cluster DNS | CoreDNS, the node-local DNS cache, and `kube-dns` on AKS, ports 53 and 1053, UDP and TCP |
| `policy.giantswarm.io/allow-kube-apiserver` | Egress to the Kubernetes API server | Any port |
| `policy.giantswarm.io/allow-webhook-ingress` | Ingress to admission and conversion webhooks | Ports 443, 4443, 8443, 9443, and 10250, from the API server and from the host network of other nodes, which the API server's calls can arrive through. Webhooks on other ports need your own policy. Not on AKS yet: write your own webhook ingress policy there |
| `policy.giantswarm.io/allow-ingress-controller` | Ingress from Envoy Gateway | Any pod in the `envoy-gateway-system` namespace, any port. Other ingress controllers need your own policy |
| `policy.giantswarm.io/allow-metrics-scraping` | Ingress from the Giant Swarm metrics agent | The `alloy-metrics` pods in `kube-system`, any port |

The standard allows are `CiliumClusterwideNetworkPolicy` objects named `standard-allow-<name>`, for example `standard-allow-dns`. They only use the namespace label, so you can't narrow them to some pods. For anything narrower, write your own policy instead of setting the label.

A label change takes effect within about a minute, because Cilium has to recompute the identities of the namespace's pods. Removing a label removes the allow just as reliably.

Anyone who may label a namespace may set these labels. This is the same permission that already allows setting the namespace opt-out.

## Allow traffic inside a namespace

Under the clusterwide deny, pods in the same namespace can't reach each other either. Cilium can't express "same namespace" in a clusterwide policy, so there's no allow label for it. Apply this Same-namespace policy to every namespace whose pods talk to each other:

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: same-namespace
  namespace: my-namespace
spec:
  endpointSelector: {}
  enableDefaultDeny:
    ingress: false
    egress: false
  ingress:
    - fromEndpoints:
        - {}
  egress:
    - toEndpoints:
        - {}
```

`enableDefaultDeny: false` keeps the policy purely additive. Without it, Cilium would put every pod the policy selects into default-deny mode, and the policy would lock the namespace down even without the clusterwide deny.

## Roll back

Use the levers in this order:

1. **Set the namespace opt-out** on the namespace that broke. It takes effect within about a minute, without restarting pods, and leaves the rest of the cluster under the deny. If the broken workload is in `kube-system` or `giantswarm`, go straight to the next step.
2. **Turn the clusterwide deny off** for the whole cluster with `denyByDefault.clusterWide.enabled: false` in the cluster's user configuration. This restores the per-namespace denies in `kube-system` and `giantswarm` and leaves your namespaces open, as before.

Allow labels and Same-namespace policies can stay in place after a rollback. They only add allowed traffic.

Also turn the clusterwide deny off before you delete a cluster, so that apps can still reach the API server while they're uninstalled. Wait until `kubectl get ciliumclusterwidenetworkpolicies default-deny-all-namespaces` returns `NotFound` before you delete the cluster.

## Rolling it out

Giant Swarm tests the clusterwide deny on every change of the `network-policies` app in ephemeral test clusters on AWS (CAPA), Azure (CAPZ), vSphere, and VMware Cloud Director. The `allow-ingress-controller` and `allow-metrics-scraping` labels aren't covered by these tests yet, and AKS and EKS aren't tested yet. For your clusters, the recommended order is:

1. Turn it on for one non-production cluster at a time. Leave each running for two weeks without incidents caused by the deny before you move on.
2. Turn it on for production clusters, one at a time.

Before each step, make sure every namespace on that cluster has the allow labels and policies it needs. Contact your account engineer if you want to plan the rollout together.
