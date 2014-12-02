# TL;DR Cheat sheet

<p class="lastmod">Last edited on December 1, 2014 by Matthias Lübken</p>


This is a very condensed cheat sheet. For more details see [Getting Started](gettingstarted.md).

## Installation

Command       | Purpose
------------- | -------------
`$ swarm`     | test the swarm CLI and see avaible commands
`$ swarm ping` | test the swarm cluster 
`$ swarm login` | login to your account 
`$ swarm env <username>/dev` | change the environment
`$ swarm ls` | list your apps to check if everything is working
`$ docker login https://registry.giantswarm.io` | login to the private Docker registry

## Create and run an app

Command                          | Purpose
-------------------------------- | -------------
`$ swarm create`                 | create an app from swarm.json
`$ swarm status helloworld`      | show status for an app
`$ swarm logs <instance-id>`     | show logs from an app
`$ swarm start helloworld`       | start an app
`$ swarm stop helloworld`        | stop an app

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
                        "domains": { "helloworld.alpha.giantswarm.io": "8000" }
                    }
                ]
            }
        ]
    }
