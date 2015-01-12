description: Here you can get a quick overview of frequently used commands for the swarm CLI.

# TL;DR Cheat sheet

<p class="lastmod">Last edited on December 3, 2014 by Matthias Lübken</p>


This is a very condensed cheat sheet. For more details see [Getting Started](gettingstarted.md).

## Installation

Mac: `$ brew tap giantswarm/swarm && brew install swarm-client`

Linux: `$ curl -O http://downloads.giantswarm.io/swarm/clients/0.10.1/swarm-0.10.1-linux-amd64.tar.gz`

Command       | Purpose
------------- | -------------
`$ swarm`     | test the swarm CLI and see avaible commands
`$ swarm info` | print current swarm settings
`$ swarm login` | login to your account 
`$ swarm env <username>/dev` | change the environment
`$ swarm ls` | list your apps to check if everything is working
`$ docker login https://registry.giantswarm.io` | login to the private Docker registry

## Create and run an app

Most commands use infos from `swarm.json` in the current path as a default.

Command                          | Purpose
-------------------------------- | -------------
`$ swarm up [swarm.json]`        | create and start an app
`$ swarm create [swarm.json]`    | create an app
`$ swarm start [app name]`       | start an app
`$ swarm stop [app name]`        | stop an app
`$ swarm status [app name]`      | show status for an app
`$ swarm logs <instance-id>`     | show logs from an app

## swarm.json

Example using a predefined python image and exposing a http server:

    {
        "app_name": "helloworld",
        "services": [
            {
                "service_name": "helloworld-service",
                "components": [
                    {
                        "component_name": "python",
                        "image": "python:3",
                        "args": ["sh", "-c", "echo \"Hello Giant Swarm. \\o/\" > index.html && python -m http.server"],
                        "ports": [ "8000/tcp" ],
                        "domains": { "helloworld.gigantic.io": "8000" }
                    }
                ]
            }
        ]
    }
