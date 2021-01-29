---
linkTitle: Usage data recording
title: Usage data recording in our web interface
description: Details on which data is tracked when using the Giant Swarm web interface
weight: 1000
menu:
  main:
    parent: uiapi-web
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# Usage data recording in our web interface

In general, when using the Giant Swarm web interface, usage data is collected on two different levels:

- The Rest API level
- External usage monitoring

Here we explain the different purposes and what data is recorded.

## Rest API level

Each request to our [Rest API]({{< relref "/ui-api/rest-api" >}}) is logged for auditing purposes, in case a customer wants to understand modifications made to resources, e. g. the creation or deletion of a cluster.

Note: This is not only the case when using the web interface, but occurs independent of the type of client using the API.

The data stored for each log entry consists of:

- The unique user ID associated with the session token authenticating the request.
- The Path of the API method called (e. g. `/v4/clusters/:clusterID/status/`).
- The HTTP method (e. g. `GET`, `POST`, `DELETE`).
- The date and time when the request has been received.

## External usage monitoring

When using the web interface, usage data is collected using a third party monitoring service (Datadog), if this service is enabled for the given installation. The recorded data serves several purposes:

- to help Giant Swarm understand how users use the web interface
- to identify performance problems in real usage
- to identify errors occurring in the field

The data recorded consists of:

- Session/Client parameters:
    - Session start and end timestamp
    - Browser brand and version
    - Operating system name and version
    - Location based on the client IP address
    - Available display size
- For every page view:
    - Timestamp
    - Page URI
    - Performance related metrics
- For every resource request:
    - Timestamp
    - Request URI
    - Performance related metrics
- For every user-initiated action:
    - Timestamp
    - Identifier of the element clicked/used
- For every error occurring in the browser
    - Timestamp
    - Request/page URI
    - Error message reported by the browser

The data is submitted to servers located in the EU. Giant Swarm can gladly provide Datadog's GDPR Data Processing Addendum (DPA) on request.
