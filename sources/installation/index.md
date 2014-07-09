# Installation

## Getting started

> **Note**:
> We are currently in an early alpha state. Although we do our best this documentation might be outdated. If something unexepected happens please don't hesitate to contact us: [support@giantswarm.io](mailto:support@giantswarm.io)

Here are the steps we are going to cover

* Prerequisites: Install CLI and create a cluster.
* Configure helloworld application.
* Deploy and run helloworld application.

### Prerequisites: Install CLI and create a cluster.

* Write an Email to support@giantswarm.io to have your own cluster created. You will also get a `swarm` binary.


### Configure helloworld application

    helloworld.json
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

Pure Docker equivalent: 
```docker run -p 8001:8001 python:3 sh -c 'echo hello-swarm > index.html && python -m http.server 8001'```



### Deploy and run helloworld application.

    $ swarm --api-endpoint="http://cluster-matthias.giant;2Dswarm.io/v1/" create helloworld.json
    $ swarm --api-endpoint="http://cluster-matthias.giant;2Dswarm.io/v1/" start helloworld

