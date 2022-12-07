---
linkTitle: API Gateway
title: Kong API Gateway
description: An overview of how and what Giant Swarm offers with the Kong API Gateway.
weight: 20
menu:
  main:
    parent: platform-overview-connectivity
aliases:
  - /developer-platform/connectivity/api-gateway
  - /app-platform/apps/kong
user_questions:
  - What is tested for Kong?
owner:
  - https://github.com/orgs/giantswarm/teams/team-cabbage
last_review_date: 2022-02-23
---

Kong is an API gateway that Giant Swarm provides as part of the developer platform.

Kong provides API microservice management features, as well as other API gateway functionality such as OIDC or caching.

See [the Kong website](https://konghq.com/) for further details.

## Testing

Our overall strategy with testing Kong is to primarily test the integration between Kong and our clusters, via integration and smoke tests, to assert that Kong operates correctly.

Where possible, we will also submit fixes or improvements to testing upstream, so that the entire community can benefit from our experience.

### Test Plan

Our current automated test plan can be summarised as follows:

- Deploy Kong to a CI test cluster, using real-world configuration values
- Install all relevant plugins (i.e: those in use by our users)
- Apply our test ingress and backend deployment
- Test that we can access our backend deployment via Kong
- Test plugins
    - (including but not limited to: basic auth, cache, cors, key-auth, and response-transformer)
- Cleanup, tear down

Our aim is to constantly improve this test suite over time, as we discover more relevant integration tests to add.

See [our test suite itself](https://github.com/giantswarm/kong-app/tree/master/tests) for specific details.
