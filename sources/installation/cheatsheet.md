# TL;DR Cheat sheet
This is a very condensed cheat sheet. For more details see [Getting Started](gettingstarted.md).

## Installation

Command       | Purpose
------------- | -------------
`$ export SWARM_ENDPOINT_URL=http://cluster-XY.giantswarm.io/v1/` | define your swarm endpoint
`$ swarm`     | test the swam cli and see avaible commands
`$ swarm ping` | test your cluster endpoint 

## Create and run an app

Command                          | Purpose
------------                     | -------------
`$ swarm create helloworld.json` | create an app
`$ swarm status helloworld`      | show status for an app
`$ swarm logs <instance-id>`     | show logs from an app
`$ swarm start helloworld`       | start an app
`$ swarm stop helloworld`        | stop an app

## helloworld.json

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
                        "args": ["sh", "-c", "'echo \"Hello Giant Swarm. \\o/\" > index.html && python -m http.server'"],
                        "ports": [ "8000/tcp" ],
                        "domains": { "helloworld.cluster-02.giantswarm.io": "8000" }
                    }
                ]
            }
        ]
    }
