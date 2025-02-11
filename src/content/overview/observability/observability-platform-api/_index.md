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
  - What is the observability-platform API architecture?
  - What is the use of observability-platform API?
  - How may I use the observability-platform API?
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

## Context

The observability platform allows customers to ingest their observability data (metrics and logs) from inside the clusters into our platform by default.

The `observability platform API` is an additional component that is a part of the platform, and it allows customers to ingest their logs (for now) from outside their clusters into our observability platform. Moreover, it also allows them to access our own observability data through their own grafana running on their premises.

Its main objectives are to be able to:

* provide a secure access to our observabily platform and reduce the attack surface.
* allow customers to access our observability data and to send their own.
* sanitize (sampling, relabelling, ...) observability data before it reaches our backends.
* support OTLP (OpenTelemetry).

## Architecture

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

Moreover, the ingressess will verify that the incoming requests are using the `X-Scope-OrgId` http headers (tenant information). If not, the request will be denied.

Upon authentication, the request is then forwarded to either the `loki-gateway` or `mimir-gateway` (depending if the query is looking for logs or metrics) components which are nginx servers respectively fronting the loki and mimir clusters. Those gateway components then finally forward the request to the read components.

That's it, the user now has access to the query's output.

#### Write path

Let's consider the following situation : a customer's logging agent running on his premises want to send its data to the Giant Swarm Observability Platform.

The workflow is quite similar as the one described for the read path. The main difference is in the fact that the requests will go through another ingress in the monitoring namespace which fronts a specifically tuned alloy instance, deployed via the [alloy-gateway-app](https://github.com/giantswarm/alloy-gateway-app).

Once authenticated, the request will thus go through the `alloy-gateway` which will forward it to the `loki-gateway` and then in turn the `loki-write` components.

This additional step was added to ensure that we support OTLP.

## Adding datasources

In order for one to use the observability-platform API's read path, the most straight-forward way is to add a datasource in one's grafana pointing towards it. Here is a step-by-step guide on how to do it :

* in the `Connection` section, write the observability-platform API url which always be `https://observability.<domain_name>`. Replace the `<domain_name>` placeholder with the actual domain name of your installation.

![datasource url](./datasource-url.png)

Please note that if you're adding a Mimir or Prometheus datasource, you will have to add the `/prometheus` suffix to the url (i.e the final url will be of the following form : `https://observability.<domain_name>/prometheus`).

* In the `Authentication` section, select the `Forward OAuth Identity` option.

![datasource authentication](./datasource-authentication.png)

* Sill in the `Authentication` section, add a HTTP header :

![datasource headers](./datasource-headers.png)

The header will always be `X-Scope-OrgID` but the value will differ depending on whether you are adding a Loki or Mimir/Prometheus datasource. The default value to access Giant Swarm managed logs should be `giantswarm` and metrics should be `anynomous`. The value of the header for the data you ingest depends on what you configured as a tenant upon ingestion.

## Limitations

We currently only support logs in the write path.
