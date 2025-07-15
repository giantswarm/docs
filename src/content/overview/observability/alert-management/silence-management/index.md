---
title: Silence management
description: Learn how to create and manage alert silences using both Kubernetes CRDs and the Grafana UI in the Giant Swarm Observability Platform.
weight: 30
menu:
  principal:
    identifier: overview-observability-alert-management-silence-management
    parent: overview-observability-alert-management
user_questions:
  - How do I create alert silences?
  - How do I silence alerts temporarily?
  - What's the difference between CRD and Grafana UI silences?
  - How do I use tenant labeling for silences?
  - How do I manage silences with GitOps?
  - How do I check active silences?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2025-07-15
---

This guide shows you how to create and manage alert silences to temporarily suppress notifications during planned maintenance or while investigating issues. For an overview of how silences fit into the alerting pipeline, see the [alert management overview]({{< relref "/overview/observability/alert-management/" >}}).

## What are silences?

Silences temporarily prevent alerts from generating notifications without stopping alert evaluation. When an alert matches an active silence, Alertmanager suppresses notifications but continues evaluating the alert rule. This is essential for:

- **Planned maintenance**: Prevent noise during scheduled downtime
- **Investigation periods**: Focus on troubleshooting without constant notifications  
- **Known issues**: Temporarily suppress alerts for acknowledged problems

## Silence management approaches

The Giant Swarm Observability Platform supports two approaches for managing silences:

- **CRD-based (GitOps)**: Use Kubernetes resources with the v1alpha2 Silence API for version-controlled, automated silence management
- **Grafana UI**: Create silences interactively through the Grafana interface for immediate, ad-hoc needs

Both approaches integrate with the platform's multi-tenancy model and require proper tenant labeling.

## CRD-based silence management

Use the v1alpha2 Silence API (`observability.giantswarm.io/v1alpha2`) for GitOps-style silence management. This approach provides version control, automated deployment, and better integration with your infrastructure-as-code workflows.

**Important:** Silence CRDs can only be created in management clusters. The silence-operator runs on management clusters and manages silences for the entire observability platform.

The v1alpha2 API is namespace-scoped and uses a simplified timing model where silences start immediately when created and end at the time specified in the `valid-until` annotation.

### Required tenant labeling

**Important:** All silences must include the `observability.giantswarm.io/tenant` label that references an existing tenant defined in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization/" >}}). The system ignores any silence that references a non-existing tenant.

Get familiar with tenant management in our [multi-tenancy documentation]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}).

### Basic silence example

```yaml
apiVersion: observability.giantswarm.io/v1alpha2
kind: Silence
metadata:
  labels:
    # Required: specifies which tenant this silence belongs to
    observability.giantswarm.io/tenant: my_team
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
    observability.giantswarm.io/tenant: my_team
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

Silences in the v1alpha2 API use a simple timing model:

- **Start time**: Silences become active immediately when created in the cluster
- **End time**: Set using the `valid-until` annotation in either `yyyy-mm-dd` or RFC3339 format
- **No scheduling**: You can't schedule silences for future activation - they start when you create them

This design keeps the API simple while supporting the most common use cases. For precise timing, create the silence CRD exactly when you want it to start.

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
- **Monitor active silences**: Regularly review and clean up expired silences

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
    observability.giantswarm.io/tenant: my_team
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
kubectl delete silences -l observability.giantswarm.io/tenant=my_team -n my-namespace
```

## Integration with alert routing

Silences work at the Alertmanager level, after alert rules evaluation but before [alert routing]({{< relref "/overview/observability/alert-management/alert-routing/" >}}). This means:

- **Alert rules continue evaluating**: Silences don't affect rule evaluation
- **Metrics remain available**: Silenced alerts still appear in Grafana with suppressed state
- **Routing is bypassed**: Silenced alerts don't trigger notifications to receivers

### Silence priority

When multiple silences could match an alert:
- **Most specific wins**: Silences with more matchers take precedence
- **Newest wins**: Among equally specific silences, the most recently created applies
- **All must match**: An alert must match ALL matchers in a silence to be suppressed

## Troubleshooting silences

### Common issues

**Silence not working:**

- Verify tenant labeling matches an existing Grafana organization
- Check matcher values exactly match alert labels
- Confirm the silence hasn't expired (check the `valid-until` annotation)
- Validate namespace and RBAC permissions
- Ensure the silence was created when you wanted it to start (no future scheduling)

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

- **Use CRDs for planned silences**: Leverage GitOps for predictable maintenance windows
- **Use Grafana UI for emergencies**: Quick silences during active incidents
- **Time creation carefully**: Since v1alpha2 silences start immediately, create them exactly when needed
- **Set reasonable durations**: Use appropriate `valid-until` times to avoid indefinite silences
- **Use meaningful names**: Choose descriptive silence names for easy identification
- **Regular cleanup**: Remove expired silences and review long-running ones

### Security considerations

- **Tenant isolation**: Silences only affect alerts within the same tenant
- **RBAC controls**: Use Kubernetes RBAC to control who can create silences
- **Audit trail**: CRD-based silences provide better audit trails than UI-created ones
- **Review access**: Regularly audit who has silence creation permissions

## Next steps

- Learn about [alert routing]({{< relref "/overview/observability/alert-management/alert-routing/" >}}) to understand how silences integrate with notification workflows
- Review [alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}) to understand what you're silencing
- Explore the [alert management overview]({{< relref "/overview/observability/alert-management/" >}}) for the complete alerting pipeline

## Related observability features

Silence management works best when integrated with other platform capabilities:

- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: Essential for understanding tenant labeling requirements and secure silence isolation
- **[Alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}})**: Understanding your alert rules helps create effective silences
- **[Data exploration]({{< relref "/overview/observability/data-management/data-exploration/" >}})**: Use Grafana Explore to test alert matchers before creating silences
