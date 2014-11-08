# Global command line options

<p class="lastmod">Last edited on November 8, 2014 by Marian Steinbach</p>

This page describes options available with all commands of the `swarm` command line tool.

## General format

Note that the global options are placed __before__ any other command name.

    $ swarm [options] <command>

## Available options

### `-v, --verbose`

This switch allows to enable or suppress detailed output.

### `-h, --help`

Show help for command.

### `--api-endpoint`

Explicitly sets the API endpoint for the command call. If used, this overrides the `SWARM_ENDPOINT_URL` environment variable.

Example:

    --api-endpoint="https://cluster-01.giantswarm.io/v1/"

### `--debug`

Enable debugging output. This usually contains API calls.

### `--env`

Explicitly sets the [environment](../env/) used. If set, this overrides the current default environment, but only for this very command.

Example:

    --env="mycompany/production"
