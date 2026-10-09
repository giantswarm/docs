---
linkTitle: Route requirements
title: Requirements for exposing a service through Gateway API
diataxis_content_type: reference
description: What the default Gateway on Giant Swarm expects from your HTTPRoutes and policies, and how to check that a route is working.
weight: 25
menu:
  principal:
    parent: tutorials-connectivity-gateway-api
    identifier: tutorials-connectivity-gateway-api-route-requirements
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
user_questions:
  - Which Gateway do I attach my HTTPRoute to?
  - Why does my HTTPRoute hostname not get a DNS record or TLS certificate?
  - How do I route to a service in another namespace?
  - How do I attach a SecurityPolicy to my route?
  - How do I check whether my HTTPRoute is accepted?
last_review_date: 2026-10-02
---

This page lists what the default Gateway installed by the [Gateway API bundle]({{< relref "/tutorials/connectivity/gateway-api/installation" >}}) expects from the routes and policies you create for your service. It applies to the default configuration. Your cluster administrator may have changed some of these settings.

## The default Gateway

The bundle creates one Gateway named `giantswarm-default` in the `envoy-gateway-system` namespace. It has two listeners:

| Listener | Port | Hostname | TLS |
|----------|------|----------|-----|
| `http` | 80 | any | none |
| `https` | 443 | `*.BASEDOMAIN` | terminated at the Gateway |

Both listeners accept routes from all namespaces.

Reference the Gateway in `parentRefs`. Without `sectionName`, the route attaches to every listener that accepts it. Because the `http` listener accepts any hostname, a route without `sectionName` whose hostname doesn't match `*.BASEDOMAIN` is still accepted, but only served over plain HTTP. Set `sectionName: https` to serve the route over HTTPS only, and to get an error in the route status when the hostname doesn't match:

```yaml
spec:
  parentRefs:
  - name: giantswarm-default
    namespace: envoy-gateway-system
    sectionName: https
```

The `http` listener doesn't redirect to HTTPS by default. Setting `httpsRedirectEnabled: true` on the `http` listener in the bundle configuration adds a catch-all route that redirects HTTP requests to HTTPS. It only applies to hostnames that have no route of their own on the `http` listener, so a route without `sectionName` is still served over plain HTTP. Routes with `sectionName: https` are redirected as long as no other route on the `http` listener uses the same hostname.

## Hostnames, DNS, and TLS certificates

The `https` listener accepts any hostname under the cluster base domain, but a hostname only works end to end when it has its own DNS record pointing to the Gateway and is covered by the Gateway certificate. Both are only created for subdomains listed in the bundle configuration:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: <CLUSTER_NAME>-gateway-api-bundle
  namespace: org-<ORGANIZATION>
data:
  values: |
    clusterID: <CLUSTER_NAME>
    organization: <ORGANIZATION>
    apps:
      gatewayApiConfig:
        userConfig:
          configMap:
            values: |
              gateways:
                default:
                  listeners:
                    https:
                      subdomains:
                      - myapp
```

With this configuration, `myapp.BASEDOMAIN` gets a CNAME record pointing to the Gateway load balancer and is added to the certificate issued by cert-manager.

A route with a hostname that isn't listed is still accepted by the Gateway, but the Gateway doesn't create a DNS record for it. Whether the hostname resolves depends on the wildcard record `*.BASEDOMAIN` of the cluster, which points to the ingress controller by default, so requests may not reach the Gateway at all. If they do reach the Gateway, clients get the Gateway certificate, which doesn't cover the hostname.

For hostnames outside the cluster base domain, see [Ingress nginx to Gateway API migration guide]({{< relref "/tutorials/connectivity/gateway-api/ingress-nginx-migration" >}}).

## Backends in another namespace

A route can reference a Service in its own namespace without further configuration. To reference a Service in another namespace, the owner of that namespace must allow it with a ReferenceGrant in the namespace of the Service:

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: ReferenceGrant
metadata:
  name: allow-routes-from-team-a
  namespace: team-b
spec:
  from:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    namespace: team-a
  to:
  - group: ""
    kind: Service
```

Without the ReferenceGrant, the route is accepted but its `ResolvedRefs` condition is `False` with reason `RefNotPermitted`, and requests to that backend fail.

## Policies

Envoy Gateway policies such as `SecurityPolicy`, `BackendTrafficPolicy`, and `ClientTrafficPolicy` attach to resources with `spec.targetRefs`, and must be in the same namespace as the resource they target. The single `spec.targetRef` field is deprecated.

```yaml
apiVersion: gateway.envoyproxy.io/v1alpha1
kind: SecurityPolicy
metadata:
  name: myapp-auth
  namespace: team-a
spec:
  targetRefs:
  - group: gateway.networking.k8s.io
    kind: HTTPRoute
    name: myapp
```

A policy whose target doesn't exist has no entries in `status.ancestors`. Check that a policy is applied:

```nohighlight
kubectl get securitypolicy myapp-auth --namespace team-a \
  --output jsonpath='{range .status.ancestors[*]}{.ancestorRef.name}{": "}{.conditions[?(@.type=="Accepted")].status}{"\n"}{end}'
```

## Check the status of a route

The route status has one entry in `status.parents` for each entry in `parentRefs`. Each entry has two conditions:

- `Accepted`: the route is attached to the Gateway. Without `sectionName`, this is `True` as soon as one listener accepts the route.
- `ResolvedRefs`: all backends of the route were found and may be referenced.

```nohighlight
kubectl get httproute myapp --namespace team-a \
  --output jsonpath='{range .status.parents[*]}{.parentRef.sectionName}{": "}{range .conditions[*]}{.type}={.status} ({.reason}) {end}{"\n"}{end}'
```

The output starts with the `sectionName` of each parent, which is empty when the parent reference has no `sectionName`. A route is working when both conditions are `True` for every entry. Common reasons when a condition is `False`:

| Condition | Reason | Meaning |
|-----------|--------|---------|
| `Accepted` | `NoMatchingListenerHostname` | None of the route hostnames match the hostname of the referenced listeners, for example a hostname outside the base domain with `sectionName: https`. |
| `Accepted` | `NotAllowedByListeners` | The listener doesn't accept routes from this namespace or of this kind. |
| `Accepted` | `NoMatchingParent` | The `sectionName` or `port` in `parentRefs` doesn't match a listener. |
| `ResolvedRefs` | `BackendNotFound` | A Service in `backendRefs` doesn't exist. |
| `ResolvedRefs` | `RefNotPermitted` | A backend in another namespace isn't allowed by a ReferenceGrant. |
| `ResolvedRefs` | `InvalidKind` | A `backendRefs` entry references a kind the Gateway can't route to. |

If the route has no entry for the Gateway in `status.parents` at all, check the `name` and `namespace` in `parentRefs`.

## Further reading

- [Using Gateway API with Envoy Gateway]({{< relref "/tutorials/connectivity/gateway-api/usage" >}})
- [Gateway API: route status](https://gateway-api.sigs.k8s.io/reference/api-types/httproute/#status)
- [Envoy Gateway: policy attachment](https://gateway.envoyproxy.io/docs/concepts/gateway_api_extensions/)
