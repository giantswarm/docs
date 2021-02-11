---
linkTitle: list endpoints
title: "'gsctl list endpoints' command reference"
description: The 'gsctl list endpoints' command shows all endpoints you have logged in to so far and tells you which one is currently selected.
weight: 130
menu:
  main:
    parent: uiapi-gsctl
aliases:
  - /reference/gsctl/list-endpoints/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
user_questions:
  - How can I list the API endpoints I have configured in gsctl?
---

# `gsctl list endpoints`

The `gsctl list endpoints` command shows all endpoints you have logged in to so far with additional information.

An endpoint is the Giant Swarm API URL for an installation you access using gsctl.
If you have only one installation, you have only one endpoint.
But if you are using, for example, one installation on-premises and one in the cloud, you have two endpoints.

## Usage and output

The command has no specific flags. Simply run it like this:

```nohighlight
gsctl list endpoints
```

If you have ever logged in to an endpoint before, you will get a table like the one below as a result:

```nohighlight
ALIAS    ENDPOINT URL                                          EMAIL            SELECTED  LOGGED IN
cloudy   https://api.g8s.cloudy.eu-central-1.aws.gigantic.io   me@elsewhere.io  yes       yes
onpremy  https://api.g8s.onpremy.my-datacenter.gigantic.io     me@example.com   no        yes
```

### Output details

- The first column shows the endpoint alias which you can use as a shorthand to
  select this endpoint. See [`gsctl select endpoint`]({{< relref "/ui-api/gsctl/select-endpoint#alias" >}})
  for details.

  **Note:** If the column shows `n/a`, the endpoint has been added with a
  gsctl version before 0.10.0. You can manually edit the configuration file to
  remove the according endpoint and then re-login.

- Column two shows the full endpoint URL.

- The `EMAIL` column shows the email address you have used to log in.

- The `SELECTED` column informs you which one of the endpoints listed is
  currently selected. This means that you will work with this endpoint, unless
  you specify a different endpoint using the `-e`/`--endpoint` command line
  flag.

- The column `LOGGED IN` indicates whether you are currently logged in with the
  endpoint.

## Related

- [`gsctl login`]({{< relref "/ui-api/gsctl/login" >}})
- [`gsctl select endpoint`]({{< relref "/ui-api/gsctl/select-endpoint" >}})
- [`gsctl delete endpoint`]({{< relref "/ui-api/gsctl/delete-endpoint" >}})
