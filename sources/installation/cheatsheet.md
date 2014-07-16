# TL;DR Cheat sheet
This is a very condensed cheat sheet. For more details see [Getting Started](gettingstarted.md).

## Installation

Command      | Purpose
------------ | -------------
`$ swarm`    | test your swarm CLI installation
`$ curl http://cluster-matthias-02.giantswarm.io/v1/` | test your cluster endpoint 
`$ export SWARM_ENDPOINT_URL=http://cluster-matthias-02.giantswarm.io/v1/` | define your swarm endpoint

## Create and run an app

Command                          | Purpose
------------                     | -------------
`$ swarm create helloworld.json` | create an app
`$ swarm status helloworld`      | show status for an app
`$ swarm start helloworld`       | start an app
`$ swarm stop helloworld`        | stop an app
`$ swarm logs helloworld`        | show logs from an app

## helloworld.json

    {
        "app_name": "helloworld",
        "services": [
            {
                "service_name": "helloworld-service",
                "components": [
                    {
                        "component_name": "python",
                        "image": "python:3",
                        "args": ["sh -c 'echo \"Hello Giant Swarm. \\o/\" > index.html && python -m http.server'"],
                        "ports": [ "8000/tcp" ],
                        "domains": { "helloworld.cluster-matthias.giantswarm.io": "8000" }
                    }
                ]
            }
        ]
    }
