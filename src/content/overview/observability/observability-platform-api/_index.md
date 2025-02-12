---
title: "Observability Platform API"
linkTitle: Observability Platform API
description: Documentation on the observability-platform API architecture deployed and maintained by Giant Swarm.
weight: 80
menu:
  principal:
    identifier: overview-observability-platform-api
    parent: overview-observability
user_questions:
  - What is the observability-platform API?
  - What is the observability-platform API for?
  - How to use the observability-platform API?
owner:
  - https://github.com/orgs/giantswarm/teams/team-atlas
last_review_date: 2025-02-10
---

The following page describes the concept of the Observability Platform API

## Table of contents

* [Context](#context)
* [Architecture](#architecture)
* [Global overview](#global-overview)
  * [How it works](#how-it-works)
    * [Read path](#read-path)
    * [Write path](#write-path)
* [Adding datasources](#adding-datasources)
* [Limitations](#limitations)

## What it is

The observability platform already ingests and allows to explore system and application observability data from inside Giant Swarm managed clusters by default.

The `observability platform API` opens up the observability platform to be used from the outside - which means any resource not managed by Giant Swarm. You can ingest observability data from any source by sending them to the `observability platform API`. Additionally the API allows to query observability data from wherever you want. 

This allows you to for example ingest observability data from a SaaS-Database that might be a dependency of one of your workloads on a Giant Swarm managed cluster. Or you could explore the observability platforms data from your own, remote Grafana instance or any other observability tooling.

**Note:** At this point the `observability platform API` only allows the ingestion of logs and events. The ingestion of metrics will follow in a later release. Keep an eye on our [changes and releases]({{< relref "/changes/observability-platform/" >}}) or this document for updates.

The `observability platform API`s main objectives are to:

* provide a secure access to our observability platform from outside of Giant Swarm managed clusters.
* enable you to ingest and access observability data from anywhere.
* sanitize (sampling, relabelling, ...) observability data to align with our general data standards in the observability platform.
* support for the OpenTelemetry Protocol (OTLP).

## How it works

### Global overview

Here is a graph showing the general architecture for the API :

![api architecture](./observability-platform-api-graph.png)

### How it works

Let's explore the 2 main workflows from the customer's perspective.

#### Read path

Let's consider the following situation : a customer wants to access Giant Swarm observability data from his own Grafana running on his premises.

To do so, the customer will first log into the Grafana instance using the OIDC provider hosted on his premises. Once authenticated, he will perform a query from the "Explore" panel or simply use dashboards which in any case will trigger a request sent to the Observability Platform API url.

There, depending on the path the requests is trying to access (i.e either trying to access logs or metrics) it will go through one of 2 ingresses sharing the same host : one in the loki namespace and the other in the mimir one. Note that we decided to have 2 ingresses sharing the same host instead of having 1 ingress handling all paths because usually, ingresses only forward requests in the same namespace they are deployed in. There are ways to go around this, but those are a bit tricky and definitely not straight forward.

Upon reaching the correct ingress, the request will need to be authenticated before being forwarded. This is done through a nginx annotation : `nginx.ingress.kubernetes.io/auth-url` which value is the customer OIDC provider ingress' url. As the requests coming from Grafana forwards the user's OAuth identity through the use of a token, the Giant Swarm ingress only make sure that the incoming request's token matches an allowed user in the OIDC provider.

Moreover, the ingress will verify that the incoming requests are using the `X-Scope-OrgId` HTTP headers (tenant information). If not, the request will be denied.

Upon authentication, the request is then forwarded to either the `loki-gateway` or `mimir-gateway` (depending if the query is looking for logs or metrics) components which are nginx servers respectively fronting the loki and mimir clusters. Those gateway components then finally forward the request to the read components.

That's it, the user now has access to the query's output.

#### Write path

Let's consider the following situation : a customer's logging agent running on his premises want to send its data to the Giant Swarm Observability Platform.

The workflow is quite similar as the one described for the read path. The main difference is in the fact that the requests will go through another ingress in the monitoring namespace which fronts a specifically tuned alloy instance, deployed via the [alloy-gateway-app](https://github.com/giantswarm/alloy-gateway-app).

Once authenticated, the request will thus go through the `alloy-gateway` which will forward it to the `loki-gateway` and then in turn the `loki-write` components.

This additional step was added to ensure that we support OTLP.

## The observability platform API as Grafana datasource

One use case for the `observability platform API` is to explore the observability platforms data in a self-managed Grafana. Our recommended way of connecting a Grafana instance to the `observability platform API` is to add a datasource in the Grafana instance pointing towards the API.

Here is a step-by-step guide on how to do it :

1. in the `Connection` section, set the `observability-platform API` domain as URL. The API follows the pattern of adding the `observability`-subdomain to your installations base domain. This looks like `https://observability.<domain_name>` while you need to replace the `<domain_name>` placeholder with the actual domain name of your installation. **Please note**: if you're adding a Mimir or Prometheus datasource, you will have to add the `/prometheus` suffix to the url, making it: `https://observability.<domain_name>/prometheus`.

![datasource url](./datasource-url.png)

Please note that if you're adding a Mimir or Prometheus datasource, you will have to add the `/prometheus` suffix to the url (i.e the final url will be of the following form : `https://observability.<domain_name>/prometheus`).

2. In the `Authentication` section, select the `Forward OAuth Identity` option.

![datasource authentication](./datasource-authentication.png)

3. Fill in the `Authentication` section, add the required `X-Scope-OrgID`. Make sure the value of the `X-Scope-OrgID` header is an existing tenant that actually holds the data you're interested in. For example, to access Giant Swarm managed logs the value of this  header should be `giantswarm`, for metrics it should be `anynomous`. You can learn more about our tenant concept in [multi-tenancy in the observability platform.]({{< relref "/tutorials/observability/multi-tenancy/" >}})

![datasource headers](./datasource-headers.png)

The header will always be `X-Scope-OrgID` but the value will differ depending on whether you are adding a Loki or Mimir/Prometheus datasource. The default value to access Giant Swarm managed logs should be `giantswarm` and metrics should be `anynomous`. The value of the header for the data you ingest depends on what you configured as a tenant upon ingestion.

## Limitations

We currently only support logs in the write path.
