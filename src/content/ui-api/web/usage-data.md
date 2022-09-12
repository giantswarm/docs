---
linkTitle: Usage data recording
title: Usage data recording in the web interface
description: Our goal is to provide a snappy and bug-free experience to you when using our web interface. To achieve that goal, we collect some usage data. Here we explain in detail what we collect and how.
weight: 1000
menu:
  main:
    parent: uiapi-web
aliases:
   - /reference/web-interface/usage-data/
owner:
  - https://github.com/orgs/giantswarm/teams/team-rainbow
user_questions:
  - What usage data is Giant Swarm recording in the web UI?
  - How is Giant Swarm treating usage data recorded in the web UI?
last_review_date: 2021-01-01
---

In general, when using the Giant Swarm web interface, usage data is collected on these levels:

- The REST API level
- Usage monitoring
- Error data collection

Here we explain the different purposes and what data is recorded.

## REST API level

Each request to our [REST API]({{< relref "/ui-api/rest-api" >}}) is logged for auditing purposes, in case a customer wants to understand modifications made to resources, e. g. the creation or deletion of a cluster.

Note: This is not only the case when using the web interface, but occurs independent of the type of client using the API.

The data stored for each log entry consists of:

- The unique user ID associated with the session token authenticating the request.
- The Path of the API method called (e. g. `/v4/clusters/:clusterID/status/`).
- The HTTP method (e. g. `GET`, `POST`, `DELETE`).
- The date and time when the request has been received.

## Usage monitoring

When using the web interface, some anonymous usage data is collected using a dedicated monitoring service. The recorded data serves several purposes:

- to help Giant Swarm understand how users use the web interface
- to identify performance problems in real world usage

The data recorded consists of:

- Timestamp
- Client data: Browser brand and version, device type, display and viewport size.
- The URL viewed.
- Performance related data related to network transfers, content rendering, application readiness.

The data is submitted to a service in the Giant Swarm Management Cluster.

## Error data collection

We like to learn about any exceptions (unexpected errors) happening during web interface usage, hence we forward information about exceptions to [Sentry](https://sentry.io/welcome/).

Data submitted to sentry includes:

- Timestamp
- Browser brand and version
- Operating system name and version
- The URL visited in the web interface
- Exception description and JavaScript stack trace
- History of requests (timestamp, URL, HTTP method) made prior to the exception
- Information on any interaction prior to the exception, e. g. a button click
