# Getting started

This page should get you started with Giant Swarm. 

> **Note**:
> We are currently in an early alpha state and lots of things are still in development. Although we do our best this documentation might be outdated. If something unexepected happens don't hesitate to contact us: [support@giantswarm.io](mailto:support@giantswarm.io)

*TOC:*

* Prerequisites: Install the CLI
* Configure a helloworld application
* Run the helloworld application

## Prerequisites: Install the CLI

We currently don't have an automated sign-up. So for the setup of your cluster and the Commandline interface (CLI) we like to ask you to write an email to support@giantswarm.io. In this Email please include:

  * Full name and Email-Adress
  * If you are working on a Mac or a Linux machine

ASAP we will provide you with:

  * A cluster name and URL: e.g.: http://cluster-matthias.giantswarm.io/v1/
  * A `swarm` binary

Install the binary on your machine and set the ENV variable `SWARM_ENDPOINT_URL` to the provided cluster URL. e.g. 

    $ export SWARM_ENDPOINT_URL=http://cluster-matthias-02.giantswarm.io/v1/

Check the clusters status and availability:

    $ swarm ping
    $ OK

## Configure a helloworld application

Create a file with your favourite editor called `helloworld.json` and fill it with the following json.

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

This configures a simple app with one service. The service consists of one component. The component uses a predefined image and starts a python web http server.

## Run the helloworld application

Before you can run the application it needs to be created. To do so use the `create` command followed by the json file you have just created: 

    $ swarm create helloworld.json
    $ Creating app ...

To start this app use the `start` command followed by the `app_name` specified in the json:

    $ swarm start helloworld

While it's starting (which may take a while) you may check it's status with the `status` command:

    $ swarm status helloworld
    App helloworld is starting!

    service             component  instanceid                            status
    helloworld-service  python     4cc709fc-5250-4bab-83d3-837cd0f7af36  starting

Once it's up you can check by opening the specified domain in a browser or `curl`ing it:
    
    $ curl helloworld.cluster-matthias.giantswarm.io
    Hello Giant Swarm. \o/

On the way you might want to check for the logs:

    $ swarm logs

To stop and delete an app use `swarm stop` and `swarm delete`.

> *Congratulations* you've created and started your first swarm app!