---
linkTitle: login
title: "'gsctl login' command reference"
description: "The 'gsctl login' command starts an authenticated session."
weight: 170
menu:
  main:
    parent: uiapi-gsctl
user_questions:
- How can I authenticate against an API endpoint using gsctl?
- How do I login with gsctl manually?
- How do I login with gsctl in a script?
aliases:
  - /reference/gsctl/login/
owner:
  - https://github.com/orgs/giantswarm/teams/sig-ux
---

# `gsctl login`

With `gsctl login` you can authenticate against an API endpoint. Your session will
stay authenticated until you use `gsctl logout`.

## Usage

The standard form of executing a login against an endpoint:

```nohighlight
gsctl login <email> [-e|--endpoint <endpoint>]
```

Example:

```nohighlight
$ gsctl login user@email.com -e https://api.g8s.example.eu-central-1.aws.gigantic.io
Password for user@email.com on https://api.g8s.example.eu-central-1.aws.gigantic.io:
```

The password will _not_ be displayed during input.

The `-e`/`--endpoint` flag is optional. If you have been logged in with the same
endpoint before and it is still the selected one, which you can check using
[`gsctl info`]({{< relref "/ui-api/gsctl/info" >}}), you can omit the endpoint part.

## Non-interactive login

For usage in a script or any other type of information, the password can be
provided as a command line argument using the `-p` or `--password` option. The
syntax is as follows:

```nohighlight
gsctl login <email> -e <endpoint> -p <password>
```

## Related

- [API: Create auth token](/api/#operation/createAuthToken)
