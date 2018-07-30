+++
title = "gsctl Command Reference: select endpoint"
description = "The 'gsctl select endpoint' command selects an endpoint for usage in subsequent command executions."
date = "2018-01-26"
type = "page"
weight = 41
+++

# `gsctl select endpoint`

The `gsctl select endpoint` command selects a Giant Swarm API endpoint for
usage in subsequent command executions. This defines which endpoint you use,
unless an endpoint is specified on a per-command basis using the
`-e`/`--endpoint` flag.

This is relevant to you only if you use several installations, e. g. one
on-premises and one in the cloud.

The command works basically as a switch between several available endpoints
that are maintained in your local gsctl configuration file. An endpoint is
added to your configuration whenever you use the [`gsctl login`](../login/)
command with a new endpoint URL. [`gsctl select endpoint`](../select-endpoint/)
helps you switch between several endpoints while staying logged in.
[`gsctl list endpoints`](../list-endpoints/) and [`gsctl info`](../info/) give
you more information on status and which endpoints are available.

## Selection priority

Which endpoint is used is defined in this order:

- The endpoint given via command line flag `-e` or `--endpoint` is used if
  given.
- Otherwise, if given, the endpoint defined via the environment variable
  `GSCTL_ENDPOINT` is used.
- Otherwise the endpoint via `gsctl select endpoint` or `gsctl login` is used.

## Endpoint aliases {#alias}

To simplify the selection of an endpoint, each endpoint URL can have an alias.
When adding a new endpoint to your configuration by the use of
[`gsctl login`](../login/), an alias for the endpoint is automatically set to
the unique name of the according Giant Swarm installation.

You can find out the alias of the currently selected endpoint, if set, using
[`gsctl info`](../info/). The command
[`gsctl list endpoints`](../list-endpoints/) will print all available endpoints
and their aliases.

Aliases can be edited manually by editing your
[gsctl configuration file](../configuration-file/). We
strongly recommend to use the same aliases throughout a team, as that
simplifies communication. Also note that aliases must be unique within your
configuration.

**Note:** Endpoint aliases have been added in gsctl version 0.10.0. Endpoints
added to your configuration by previous version don't have an alias set. A
simple way to add the default alias is to open your gsctl configuraiton in an
editor, then remove the endpoint entry without an alias, then use `gsctl login`
to log in with that endpoint URL again.

## Usage

```nohighlight
gsctl select endpoint <endpoint>
```

Example:

```nohighlight
gsctl select endpoint https://api.g8s.example.eu-central-1.aws.gigantic.io
```

A message will be printed letting you know if the endpoint has been selected.

With the alias `myalias` set for this endpoint, you could alternatively execute
that command:

```nohighlight
gsctl select endpoint myalias
```

## Related

- [`gsctl login`](../login/)
- [`gsctl list endpoints`](../list-endpoints/)
