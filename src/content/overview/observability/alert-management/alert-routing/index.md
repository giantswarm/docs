---
title: Alert routing
description: Configure how alerts are delivered to different teams and channels through Alertmanager in the Giant Swarm Observability Platform.
weight: 20
menu:
  principal:
    identifier: overview-observability-alert-management-alert-routing
    parent: overview-observability-alert-management
user_questions:
  - How do I configure Alertmanager?
  - How do I route alerts to different teams?
  - How do I visualize the existing alerting configuration?
  - How do I set up notification channels?
  - What are alert routing best practices?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2025-07-07
aliases:
  - /tutorials/observability/alerting/configure-alertmanager/
---

Alert routing determines how alerts flow from your [alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}) to the right teams through the right channels. The Giant Swarm Observability Platform uses Mimir Alertmanager to handle routing, grouping, and delivering notifications.

## How alert routing works

When your alert rules trigger, they send alerts to Mimir Alertmanager. The Alertmanager then:

1. **Groups alerts** based on your configuration to reduce noise
2. **Routes alerts** to appropriate receivers using matching rules  
3. **Delivers notifications** through configured channels like Slack, email, or PagerDuty
4. **Handles silences** and suppression logic

This process is part of the broader [alerting pipeline]({{< relref "/overview/observability/alert-management/" >}}) and supports full [multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}}) isolation.

## Prerequisites

Before configuring alert routing, ensure you have:

- Access to your management cluster
- A tenant defined in a [Grafana Organization]({{< relref "/overview/observability/configuration/multi-tenancy/creating-grafana-organization/" >}})
- [Alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}}) configured for your applications

## Configure Alertmanager

Configure Alertmanager for your tenant by creating a Kubernetes secret on your management cluster with the required labels and configuration data.

### Basic configuration structure

```yaml
apiVersion: v1
kind: Secret
metadata:
  labels:
    # Required: marks this secret as an Alertmanager configuration
    observability.giantswarm.io/kind: alertmanager-config
    # Required: specifies the tenant for this configuration
    observability.giantswarm.io/tenant: my_team
  name: my-alertmanager-config
  namespace: default
stringData:
  # Required: contains the Alertmanager configuration
  alertmanager.yaml: |
    route:
      receiver: "default-receiver"
      group_by: ["alertname", "cluster_id"]
      group_wait: 10s
      group_interval: 10s
      repeat_interval: 1h
      routes:
        - match:
            severity: critical
          receiver: "critical-alerts"
          group_wait: 0s
        - match:
            severity: warning
          receiver: "warning-alerts"
    
    receivers:
      - name: "default-receiver"
        slack_configs:
          - api_url: "YOUR_SLACK_WEBHOOK_URL"
            channel: "#general-alerts"
            title: "Alert: {{ .GroupLabels.alertname }}"
            text: "{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}"
      
      - name: "critical-alerts"
        slack_configs:
          - api_url: "YOUR_SLACK_WEBHOOK_URL"
            channel: "#critical-alerts"
            title: "🚨 Critical Alert: {{ .GroupLabels.alertname }}"
            text: "{{ range .Alerts }}{{ .Annotations.description }}{{ end }}"
        pagerduty_configs:
          - routing_key: "YOUR_PAGERDUTY_INTEGRATION_KEY"
            description: "Critical alert: {{ .GroupLabels.alertname }}"
      
      - name: "warning-alerts"
        slack_configs:
          - api_url: "YOUR_SLACK_WEBHOOK_URL"
            channel: "#warning-alerts"
            title: "⚠️ Warning: {{ .GroupLabels.alertname }}"
type: Opaque
```

### Key configuration components

- **Route**: Defines how alerts are grouped and routed to receivers
- **Receivers**: Configure notification channels (Slack, email, PagerDuty, etc.)
- **Group settings**: Control alert batching to reduce notification noise
- **Match rules**: Route specific alerts based on labels or conditions

### Using notification templates

Create reusable templates for consistent alert formatting across channels:

```yaml
stringData:
  alertmanager.yaml: |
    route:
      receiver: "templated-receiver"
      group_by: ["alertname"]
    
    receivers:
      - name: "templated-receiver"
        slack_configs:
          - api_url: "YOUR_SLACK_WEBHOOK_URL"
            channel: "#alerts"
            title: "{{ template \"alert.title\" . }}"
            text: "{{ template \"alert.description\" . }}"
    
    templates:
      - alert_templates.tmpl
  
  # Template file (must have .tmpl extension)
  alert_templates.tmpl: |
    {{ define "alert.title" }}
    [{{ .CommonLabels.alertname }} | {{ .CommonLabels.cluster_id }}]
    {{ end }}
    
    {{ define "alert.description" }}
    {{ range .Alerts }}
    *Summary:* {{ .Annotations.summary }}
    *Description:* {{ .Annotations.description }}
    *Runbook:* {{ .Annotations.runbook_url }}
    {{ end }}
    {{ end }}
```

## Supported notification channels

The platform supports various notification integrations:

### Slack

```yaml
slack_configs:
  - api_url: "YOUR_WEBHOOK_URL"
    channel: "#alerts"
    username: "alertmanager"
    title: "Alert: {{ .GroupLabels.alertname }}"
    text: "{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}"
```

### Email

```yaml
email_configs:
  - to: "team@company.com"
    from: "alerts@company.com"
    smarthost: "smtp.company.com:587"
    subject: "Alert: {{ .GroupLabels.alertname }}"
    body: "{{ range .Alerts }}{{ .Annotations.description }}{{ end }}"
```

### PagerDuty

```yaml
pagerduty_configs:
  - routing_key: "YOUR_INTEGRATION_KEY"
    description: "{{ .GroupLabels.alertname }}"
    severity: "{{ .CommonLabels.severity }}"
```

### Opsgenie

```yaml
opsgenie_configs:
  - api_key: "YOUR_API_KEY"
    message: "{{ .GroupLabels.alertname }}"
    description: "{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}"
```

For complete configuration options, see the [Alertmanager configuration documentation](https://prometheus.io/docs/alerting/latest/configuration/).

## Validation and testing

### Configuration validation

The platform automatically validates your configuration through a validating webhook that:

- Checks YAML syntax and structure
- Verifies tenant references exist
- Validates Alertmanager configuration format
- Rejects configurations referencing non-existent tenants

### Testing configurations

**Use mimirtool for validation**: Install [`mimirtool`](https://grafana.com/docs/mimir/latest/manage/tools/mimirtool/#validate-alertmanager-configuration) and validate configurations before deployment:

```bash
mimirtool alertmanager verify --address=<your-mimir-url> config.yaml
```

**Test in non-production**: Always test routing configurations in development environments before applying to production clusters.

**Monitor delivery**: Use Grafana's alerting interface to verify alerts reach their intended destinations and troubleshoot delivery issues.

## Configuration best practices

### Alert grouping

- Group related alerts by `alertname` and `cluster_id` to reduce noise
- Use appropriate `group_wait` values to batch related alerts
- Set reasonable `repeat_interval` to avoid notification fatigue

### Routing strategy

- Create specific routes for critical alerts that need immediate attention
- Use default routes for general notifications
- Match on meaningful labels like `severity`, `team`, or `service`

### Template design

- Create reusable templates for consistent formatting
- Include essential context: alert name, affected resources, and remediation links
- Use clear, actionable language in notifications

### Security considerations

- Store sensitive tokens and API keys securely
- Limit access to Alertmanager configuration secrets
- Use separate notification channels for different security levels

## Important limitations

The Observability Platform uses [Mimir Alertmanager](https://grafana.com/docs/mimir/latest/references/architecture/components/alertmanager/), which may not support all features available in upstream Prometheus Alertmanager. Some configuration options might not work as expected.

Key considerations:

- **Feature compatibility**: Not all Alertmanager features are supported in Mimir
- **Template processing**: Only files with `.tmpl` extension are processed as templates
- **Tenant isolation**: Each tenant manages their own routing configuration independently

## Monitoring alert delivery

Access alerting monitoring through your [installation's Grafana]({{< relref "/getting-started/observe-your-clusters-and-apps/" >}}):

1. Navigate to **Alerting** → **Contact points** to view configured receivers
2. Check **Notification policies** to see routing rules and their hierarchy
3. Monitor **Active notifications** for current alert delivery status
4. Review **Silences** to understand suppressed alerts

## Next steps

- Review the complete [alert management]({{< relref "/overview/observability/alert-management/" >}}) workflow
- Set up alert silences for maintenance windows using Grafana's silencing interface
- Explore [data visualization]({{< relref "/overview/observability/data-management/data-exploration/" >}}) to understand alert triggers

## Related observability features

Alert routing works best when integrated with other platform capabilities:

- **[Alert rules]({{< relref "/overview/observability/alert-management/alert-rules/" >}})**: Define the conditions that trigger notifications
- **[Multi-tenancy]({{< relref "/overview/observability/configuration/multi-tenancy/" >}})**: Understand how tenant isolation affects alert routing
- **[Data management]({{< relref "/overview/observability/data-management/" >}})**: Explore the metrics and logs that power your alerts
- **[Logging]({{< relref "/overview/observability/logging/" >}})**: Set up log-based alerts that integrate with your routing configuration
