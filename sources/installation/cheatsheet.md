# TL;DR Cheat sheet

<p class="lastmod">Last edited on October 09, 2014 by Matthias Lübken</p>

This is a very condensed cheat sheet. For more details see [Getting Started](gettingstarted.md).

## Installation

Command       | Purpose
------------- | -------------
`$ export SWARM_ENDPOINT_URL=http://alpha.giantswarm.io/v1/` | define your swarm endpoint
`$ swarm`     | test the swam cli and see avaible commands
`$ swarm ping` | test your cluster endpoint 
`$ swarm login` | login to your account 
`$ swarm env <username>/dev` | Use the default environment
`$ swarm ls` | List your apps to check if everything is working

## Create and run an app

Command                          | Purpose
------------                     | -------------
`$ swarm create swarm.json`      | create an app from swarm.json
`$ swarm status helloworld`      | show status for an app
`$ swarm logs <instance-id>`     | show logs from an app
`$ swarm start helloworld`       | start an app
`$ swarm stop helloworld`        | stop an app

## swarm.json

Using a predefined python image and expose a http server:

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
                        "domains": { "helloworld.alpha.giantswarm.io": "8000" }
                    }
                ]
            }
        ]
    }
