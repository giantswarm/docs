---
linkTitle: Telemetry
title: Usage data collection in 'kubectl gs'
description: kubectl-gs collects anonymous usage data, which helps us to prioritize our further development on the tool.
weight: 1000
menu:
  main:
    identifier: reference-kubectlgs-telemetry
    parent: reference-kubectlgs
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What usage data does kubectl-gs collect?
  - How does Giant Swarm use the usage data collected from kubectl-gs?
  - Where is usage data from kubectl-gs stored?
  - How can I opt out of usage data collection in kubectl-gs?
last_review_date: 2024-10-16
---

Since kubectl-gs version 4.3.0, Giant Swarm collects anonymous usage data about `kubectl gs` command execution. This allows us to understand better which commands are used how widely and how frequently, and to better prioritize our development efforts.

You are free to [opt out](#optout) of this data collection. However, we appreciate your support and ensure that we only collect non-identifyable information and keep data collection to a minimum.

## Details we collect

Whenever a command is executed (this does not include calling a command with `-h` or `--help`), we collect the following details:

- Name of the command executed
- kubectl-gs version
- Name of the operating system
- Processor architecture (e.g. amd64, arm64)
- The [library](https://github.com/giantswarm/telemetrydeck-go) and version used to submit the data (e. g. `telemetrydeck-go/0.0.1`)
- A generated user identifier hash (more details [below](#user-id-hash))
- A random UUID as a session identifier. Currently this is unique per command execution. We may change this in the future to correlate several data submissions to a single session.

## User identifier hash {#user-id-hash}

We submit a hash that is supposed to be distinct to each user using kubectl-gs, to allow counting users. It is generated based on the following data and SHA256-hashed before submission:

- Operating system
- Processor architecture
- Host name
- OS user ID
- OS group ID
- OS user name
- The MAC adresses of network interfaces

For more details, see the [source code](https://github.com/giantswarm/telemetrydeck-go/blob/21f23a6a90f3c1f271b73e5a06b4060daff68083/telemetrydeck.go#L214).

## Disabling usage data collection {#optout}

To disable the data collection, please set the following environment variable to any value:

```nohighlight
KUBECTL_GS_TELEMETRY_OPTOUT
```

For example, in your Bash profile, you might add the following:

```bash
export KUBECTL_GS_TELEMETRY_OPTOUT=1
```

## Data storage

Data is submitted to [TelemetryDeck](https://telemetrydeck.com/), who use Microsoft Azure servers in Amsterdam, Netherlands.

For more information, see the [TelemetryDeck privacy FAQ](https://telemetrydeck.com/docs/guides/privacy-faq/).
