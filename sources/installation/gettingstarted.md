# Getting started

This page should get you started with Giant Swarm. It will show you how to install the prerequisites tools and get a prefined image running.

## Prerequisites: Install the CLI

We currently don't have an automated sign-up. So for the setup of your cluster and the Commandline interface (CLI) we like to ask you to write an email to support@giantswarm.io. In this Email please include:

  * Full name and Email-Adress
  * If you are working on a Mac or a Linux machine

ASAP we will provide you with:

  * A cluster name and URL: e.g.: http://alpha.giantswarm.io/v1/
  * A `swarm` binary
  * A user and a password

Install the binary on your machine and set the ENV variable `SWARM_ENDPOINT_URL` to the provided cluster URL. e.g. 

    $ export SWARM_ENDPOINT_URL=http://alpha.giantswarm.io/v1/

Check the clusters status and availability:

    $ swarm ping
    $ OK

Login to your account and update your password

    $ swarm login
    $ user or mail: luebken
    $ password:

    $ swarm user -u password
    $ old password:
    $ new password:
    $ confirm new password:

Configure your default environment:

    $ swarm env <username>/dev

See [Working with environments](reference/env/) for further usages.

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
                        "args": ["sh", "-c", "echo \"Hello Giant Swarm. \\o/\" > index.html && python -m http.server"],
                        "ports": [ "8000/tcp" ],
                        "domains": { "helloworld.alpha.giantswarm.io": "8000" }
                    }
                ]
            }
        ]
    }

This configures a simple app with one service. The service consists of one component. The component uses a predefined image and starts a python web http server.

## Run the helloworld application

Before you can run the application it needs to be created. To do so use the `create` command followed by the json file you have just created: 

    $ swarm create helloworld.json

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

On the way you might want to check for the logs by quering against the instanceid:

    $ swarm logs 4cc709fc-5250-4bab-83d3-837cd0f7af36

To stop and delete an app use `swarm stop` and `swarm delete`.

> *Congratulations* you've created and started your first swarm app!

After you have celebrated your success head over to [Part 2](gettingstarted2.md) to see how to define your own images.