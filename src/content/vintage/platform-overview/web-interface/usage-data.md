---
linkTitle: Usage data recording
title: Usage data recording in the web interface
description: Our goal is to provide a snappy and bug-free experience to you when using our web interface. To achieve that goal, we collect some usage data. Here we explain in detail what we collect and how.
weight: 1000
menu:
  main:
    parent: platform-overview-web
aliases:
  - /platform-overview/web-interface
  - /ui-api/web/usage-data
  - /reference/web-interface/usage-data/
owner:
  - https://github.com/orgs/giantswarm/teams/team-honeybadger
user_questions:
  - What usage data is Giant Swarm recording in the web UI?
  - How is Giant Swarm treating usage data recorded in the web UI?
last_review_date: 2023-03-20
---

We like to learn about any exceptions (unexpected errors) happening during web interface usage, hence we forward information about exceptions to [Sentry](https://sentry.io/welcome/).

Data submitted to sentry includes:

- Timestamp
- Browser brand and version
- Operating system name and version
- The URL visited in the web interface
- Exception description and JavaScript stack trace
- History of requests (timestamp, URL, HTTP method) made prior to the exception
- Information on any interaction prior to the exception, e. g. a button click
