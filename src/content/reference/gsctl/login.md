+++
title = "gsctl Command Reference: login"
description = "The 'gsctl login' command starts an authenticated session."
date = "2017-10-16"
type = "page"
weight = 41
+++

# `gsctl login`

With `gsctl login` you can authenticate against an API endpoint. Your session will
stay authenticated until you use `gsctl logout`.

## Usage

The standard form of executing a login against an endpoint:

```nohighlight
$ gsctl login <email> [-e|--endpoint <endpoint>]
```

Example:

```nohighlight
$ gsctl login user@email.com -e https://api.g8s.example.eu-central-1.aws.gigantic.io
Password for user@email.com on https://api.g8s.example.eu-central-1.aws.gigantic.io:
```

The password will _not_ be displayed during input.

The `-e`/`--endpoint` flag is optional. If you have been logged in with the same
endpoint before and it is still the selected one, which you can check using
[`gsctl info`](../info/), you can omit the endpoint part.

## Non-interactive login

For usage in a script or any other type of information, the password can be
provided as a command line argument using the `-p` or `--password` option. The
syntax is as follows:


```nohighlight
$ gsctl login <email> -e <endpoint> -p <password>
```

## Related

- [`gsctl` reference overview](../)
