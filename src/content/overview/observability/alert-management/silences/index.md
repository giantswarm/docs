---
title: Silences
diataxis_content_type: how-to-guide
description: Learn how to manage alert silences in the Giant Swarm observability platform.
weight: 30
menu:
  principal:
    parent: overview-observability-alert-management
    identifier: overview-observability-alert-management-silences
last_review_date: 2026-10-06
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
user_questions:
  - How do I silence alerts?
  - How do I schedule maintenance windows?
  - How do I use silences in Alertmanager?
  - How do I manage silences via CRDs and the UI?
  - How do I automate silence management?
  - How do silences interact with alert rules and routing?
---

This guide shows you how to create and manage alert silences to temporarily suppress notifications during planned maintenance or while investigating issues. For what silences are, when to use them, and how they fit into the alerting pipeline, see [understanding alert silences]({{< relref "/overview/observability/alert-management/understanding-silences" >}}).

The platform supports two approaches to managing silences, both tenant-scoped and requiring proper tenant labeling:

- **CRD-based (GitOps)** ✅ **Recommended**: Kubernetes resources using the v1alpha2 Silence API for version-controlled, automated management. Best for planned silences.
- **Grafana UI**: interactive silences through the Grafana interface for immediate, ad-hoc needs. Best for emergencies.

The following sections cover each approach in turn.

## CRD-based silence management

Use the v1alpha2 Silence API (`observability.giantswarm.io/v1alpha2`) for GitOps-style silence management. This approach provides version control, automated deployment, and better integration with your infrastructure-as-code workflows.

**Important:** Silence CRDs can only be created in management clusters. The silence-operator runs on management clusters and manages silences for the entire observability platform.

The v1alpha2 API is namespace-scoped and supports explicit timing through `spec.startsAt`, `spec.endsAt`, and `spec.duration`. Without them, silences start immediately and end at the `valid-until` annotation. For the complete `Silence` field schema, see the [Silence CRD reference]({{< relref "/reference/platform-api/crd/silences.observability.giantswarm.io" >}}).

### Required tenant labeling

**Important:** All silences must include the `observability.giantswarm.io/tenant` label that references an existing tenant defined in a [Grafana Organization]({{< relref "/overview/observability/configuration/creating-grafana-organization/" >}}). The system ignores any silence that references a non-existing tenant.

Get familiar with tenant management in our [multi-tenancy documentation]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}).

### Basic silence example

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    # Required: specifies which tenant this silence belongs to
    observability.giantswarm.io/tenant: my_tenant
  annotations:
    # When the silence expires (yyyy-mm-dd or RFC3339 format)
    valid-until: "2025-07-20T06:00:00Z"
  name: maintenance-window
  namespace: my-namespace
spec:
  # Alert matching criteria
  matchers:
    - name: alertname
      matchType: "="
      value: DatabaseDown
    - name: cluster_id
      matchType: "="
      value: prod-cluster-01
```

### Advanced matching patterns

The v1alpha2 API supports different matching types for flexible alert targeting:

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    observability.giantswarm.io/tenant: my_tenant
  annotations:
    # Silence expires at end of load testing
    valid-until: "2025-07-20T18:00:00Z"
  name: regex-silence-example
  namespace: my-namespace
spec:
  matchers:
    # Exact match
    - name: severity
      matchType: "="
      value: warning
    # Negative match (not equal)
    - name: alertname
      matchType: "!="
      value: CriticalSystemDown
    # Regular expression match
    - name: alertname
      matchType: "=~"
      value: "CPU.*"
    # Negative regex match
    - name: instance
      matchType: "!~"
      value: "prod-db-.*"
```

### Match types

The v1alpha2 API supports four match types using Alertmanager operator symbols:

- **`"="`**: Exact string match
- **`"!="`**: String doesn't match exactly
- **`"=~"`**: Regular expression match
- **`"!~"`**: Regular expression doesn't match

### Silence timing

Silences in the v1alpha2 API resolve their time window as follows:

- **Start time**: `spec.startsAt` (RFC3339). Defaults to the creation timestamp, so set a future value to schedule a silence.
- **End time**: The first of these that is set wins:
  1. `spec.endsAt` (RFC3339).
  2. `spec.duration`, counted from the start time, for example `7d`, `2w`, `1d12h`, `30m` (units `w`, `d`, `h`, `m`, `s`).
  3. The `valid-until` annotation in `yyyy-mm-dd` or RFC3339 format.
  4. A 100-year default.
- `spec.endsAt` and `spec.duration` are mutually exclusive, and `spec.startsAt` must be before `spec.endsAt`.

```yaml
spec:
  startsAt: "2026-10-20T22:00:00Z"
  duration: 4h
  matchers:
    - name: alertname
      matchType: "="
      value: DatabaseDown
```

### Forcing complete silence

By default, the platform protects your most important notifications from being suppressed by mistake. Every silence automatically excludes alerts that target all notification pipelines (the most critical, system-wide alerts) and the `Heartbeat` alert. This means a broad silence won't take down the alerts you most need to keep flowing.

If you need a silence to suppress **everything** it matches, including critical alerts, add the `silence.application.giantswarm.io/force-all` annotation:

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    observability.giantswarm.io/tenant: my_tenant
  annotations:
    valid-until: "2025-07-20T06:00:00Z"
    # Suppress every matching alert, including critical ones
    silence.application.giantswarm.io/force-all: "true"
  name: full-maintenance
  namespace: my-namespace
spec:
  matchers:
    - name: cluster_id
      matchType: "="
      value: prod-cluster-01
```

With this annotation, the all-pipelines protection is skipped, so critical alerts matching the silence are suppressed too. The `Heartbeat` alert is always preserved, even in this mode.

**Warning:** Forcing complete silence removes the safety net that would normally page you when something goes wrong. Before using `force-all`, make sure nothing in the silenced scope can cause real harm while unobserved. For example, a component stuck in a crash loop might re-read large amounts of data from object storage (such as S3) on every restart. Those reads can generate significant cloud costs that no alert will warn you about. Keep `force-all` silences as narrowly scoped and short-lived as possible.

### Deployment patterns

**Important:** Silences can only be created in management clusters. Deploy silence CRDs to your management cluster to create silences that apply across your entire installation:

```yaml
# Silence example (deploy to management cluster only)
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    observability.giantswarm.io/tenant: platform_team
  annotations:
    # Maintenance window ends in 2 hours
    valid-until: "2025-07-20T03:00:00Z"
  name: global-maintenance
  namespace: monitoring
spec:
  matchers:
    - name: alertname
      matchType: "=~"
      value: "Infrastructure.*"
```

## Grafana UI silence management

For immediate silence needs or interactive troubleshooting, use the Grafana Alerting interface. This approach is ideal for:

- Emergency silences during active incidents
- Temporary silences while developing alert rules
- Quick silences for investigation purposes

### Creating silences in Grafana

1. **Access Grafana**: Navigate to your [installation's Grafana]({{< relref "/getting-started/observe-your-clusters-and-apps/" >}}) interface
2. **Go to Alerting**: Click the Alerting (bell) icon in the left sidebar
3. **Select Silences**: Choose "Silences" from the alerting menu
4. **Create New Silence**: Click the "New Silence" button
5. **Configure Matchers**: Add label matchers to specify which alerts to silence
6. **Set Duration**: Define start and end times for the silence
7. **Add Comments**: Provide context about why the silence is needed
8. **Save**: Create the silence

### Grafana silence best practices

- **Use descriptive comments**: Explain the reason and expected duration
- **Set appropriate end times**: Don't create indefinite silences
- **Use specific matchers**: Target specific alerts rather than broad patterns
- **Monitor active silences**: Review and clean up expired silences

### Viewing active silences

In Grafana:

1. Navigate to **Alerting > Silences**
2. View active, pending, and expired silences
3. Filter by state, matchers, or creator
4. Edit or expire silences as needed

## Silence lifecycle management

### Checking silence status

Monitor your silences using kubectl:

```bash
# List all silences in a namespace
kubectl get silences -n my-namespace

# Get detailed information about a specific silence
kubectl describe silence maintenance-window -n my-namespace

# Check silence status across all namespaces
kubectl get silences --all-namespaces
```

### Updating silences

Modify existing silences by updating the CRD:

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    observability.giantswarm.io/tenant: my_tenant
  annotations:
    # Extended end time for longer maintenance
    valid-until: "2025-07-20T08:00:00Z"
  name: maintenance-window
  namespace: my-namespace
spec:
  matchers:
    - name: alertname
      matchType: "="
      value: DatabaseDown
```

### Removing silences

Delete silences before their expiration time:

```bash
# Remove a specific silence
kubectl delete silence maintenance-window -n my-namespace

# Remove all silences for a tenant (be careful!)
kubectl delete silences -l observability.giantswarm.io/tenant=my_tenant -n my-namespace
```

## Troubleshooting silences

### Common issues

**Silence not working:**

- Verify tenant labeling matches an existing Grafana organization
- Check matcher values exactly match alert labels
- Confirm the silence hasn't expired (check the `valid-until` annotation)
- Validate namespace and RBAC permissions
- Check `spec.startsAt` isn't in the future

**Can't create silences:**

- Ensure proper RBAC permissions for Silence CRDs
- Verify the silence-operator is running in your cluster
- Check tenant exists in Grafana organizations

**Grafana UI silences not appearing:**

- Confirm you're viewing the correct tenant's alerts
- Check Grafana organization membership
- Verify Alertmanager connectivity in Grafana

### Debugging commands

```bash
# Check silence operator status
kubectl get pods -l app.kubernetes.io/name=silence-operator -A

# View silence operator logs
kubectl logs -l app.kubernetes.io/name=silence-operator -A

# Check Alertmanager configuration
kubectl get configmap alertmanager-config -n monitoring -o yaml
```

## Best practices

### Silence management guidelines

- **Prefer CRDs for most use cases**: The GitOps approach with CRDs is recommended for better version control, audit trails, and team collaboration
- **Use CRDs for planned silences**: Leverage GitOps for predictable maintenance windows
- **Use Grafana UI for emergencies**: Quick silences during active incidents when immediate action is needed
- **Time creation**: Without `spec.startsAt`, silences start when created. Set `spec.startsAt` to schedule one ahead of time
- **Set reasonable durations**: Use appropriate `valid-until` times to avoid indefinite silences
- **Use meaningful names**: Choose descriptive silence names for easy identification
- **Regular cleanup**: Remove expired silences and review long-running ones

### Security considerations

- **Tenant isolation**: Silences only affect alerts within the same tenant
- **RBAC controls**: Use Kubernetes RBAC to control who can create silences
- **Audit trail**: CRD-based silences provide better audit trails than UI-created ones
- **Review access**: Audit who has silence creation permissions

## Next steps

- Learn about [alert routing]({{< relref "/overview/observability/alert-management/alert-routing/" >}}) to understand how silences integrate with notification workflows
- Review [alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}) to understand what you're silencing
- Explore the [alert management overview]({{< relref "/overview/observability/alert-management/" >}}) for the complete alerting pipeline

## Related observability features

Silence management works best when integrated with other platform capabilities:

- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: Essential for understanding tenant labeling requirements and secure silence isolation
- **[Alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}})**: Understanding your alert rules helps create effective silences
- **[Data exploration]({{< relref "/overview/observability/data-management/data-exploration/" >}})**: Use Grafana Explore to test alert matchers before creating silences
