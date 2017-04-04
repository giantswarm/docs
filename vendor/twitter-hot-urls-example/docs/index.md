+++
title = "Microservices & Custom Metrics Example"
description = "Here we show how to build microservices and offer Prometheus custom metrics in your application."
date = "2016-10-27"
type = "page"
weight = 100
tags = ["tutorial"]
+++

# Microservices & Custom Metrics Example

In this example we show how to build a simpe Microservice application that offer custom Prometheus metrics.

The multiple components work hand in hand to collect URLs mentioned on Twitter and create a hotlist of popular URLs. We call this example internally Twitter Hot URLs Example - short THUX.

Contents:

- [Component Overview](#component-overview)
- [Getting Credentials to Access Twitter API](#twitter-api)
- [Deploying the Application](#deploy)

## Component Overview

![Component Overview](components-overview.png)

### tracker

This component consumes the Twitter Stream API, looking for tweets containing the strings `http` or `https` to fetch all tweets with links. The tweets are then parsed for contained URLs.

The URLs found are stored in the `inbox` redis database.

### inbox-redis

This component is a simple Redis database that receives all found URLs from the `tracker` component. It makes use of the official Redis Docker image.

This component consciously does not provide a volume, which means that whenever this component is restarted, the database content is lost.

### resolver

The script inside this component reads URLs from the `inbox` Redis database and creates requests to those URLs in order to resolve redirects, to reveal the actual target URL. The resulting URL is stored in the `hotlist` Redis database.

To prevent accessing the same URL several times, a cache is maintained in the `hotlist` Redis.

The `resolver` component can be thought of as a worker, processing jobs from a queue. Since resolving URLs is in many cases a time-consuming job, there can be multiple instances of this component working in parallel.

### hotlist-redis

This second Redis database component stores all resolved URLs together with scoring information. It also contains the cache for the `resolver`. Just like the `inbox` component, we use the official Redis Docker image here.

In contrast to the `inbox` component, the `hotlist` provides a volume to persist the database throughout restarts.

### cleaner

This component contains a little helper that periodically removes outdated information from the `hotlist` Redis database.

### frontend

This is a Python/Flask web application that offers a JSON API to fetch the resulting URL hotlist.

### rebrow

The `rebrow` component offers a web-based user interface ("rebrow" stands for "redis browser") to debug the content of both Redis databases. It makes use of a third party Docker image.

## Getting Credentials to Access Twitter API {#twitter-api}

To access the [streaming API](https://dev.twitter.com/streaming/overview/connecting) of Twitter an personalized [account](https://twitter.com/signup) is needed and some app specific credentials created at [Twitter Application Management](https://apps.twitter.com/).

For example:

    Name: thux
    Description: Tracks URLs mentioned on Twitter and creates a ranked list
    Website: https://github.com/giantswarm/twitter-hot-urls-example
    Callback URL: <leave this field blank>

After that also create an Access Token under "Keys and Access Tokens". Edit `secrets/twitter-api-secret.yaml` and fill all four data fields with the corresponding [`base64` encoded values]((http://kubernetes.io/docs/user-guide/secrets/#creating-a-secret-manually)).

```nohighlight
printf "exampletokenxyz" | base64
```

## Deploying the Application {#deploy}

__Note:__ To get custom metrics you need to have our [Monitoring recipe](/guides/kubernetes-prometheus/) deployed.

Then, you can deploy the app by running:

```nohighlight
kubectl apply --filename https://raw.githubusercontent.com/giantswarm/twitter-hot-urls-example/master/manifests-all.yaml
kubectl apply --filename secrets/twitter-api-secret.yaml
```

After a while you should be able to see the custom metrics appearing in Grafana.
