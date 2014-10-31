# Getting started

<p class="lastmod">Last edited on October 26, 2014 by Marian Steinbach</p>

This page should get you started with Giant Swarm. It will show you how to install the required tools and get a provided Docker image running.

## Installing the swarm CLI

As of now, we don't have an automated sign-up process yet. In order to provide you with access to a Giant Swarm cluster and the required command line interface (CLI) client, please __send us an email__ to [support@giantswarm.io](mailto:support@giantswarm.io). In this email, please include the following details:

 * Your full name and email address
 * The operating system you use on your machine (Linux, Mac OS, ...)

We will then provide you with:

  * a `swarm` binary for your platform
  * a cluster name and URL. Example: http://alpha.giantswarm.io/v1/
  * a user name
  * a password

The first thing you should do then is __install the swarm binary__ somewhere convenient, preferably in a location that's contained in your `PATH` environment variable. For example, `/usr/local/bin/` works fine in many cases.

Next we need to tell the swarm client __what cluster you want to work with__. This is what the cluster URL we sent you is for. Store this URL in the environment variable `SWARM_ENDPOINT_URL` like this: 

    $ export SWARM_ENDPOINT_URL=http://alpha.giantswarm.io/v1/

<i class="fa fa-info-circle"></i> You might want to add this line to your profile file (e. g. `~/.bash_profile`) to have this automatically set for all new terminal sessions.

Once you have this, you can use the swarm client to check your cluster's availability:

    $ swarm ping

You should get an `OK` as a result.

Now that the connection to your cluster is set up, it's time to __log in__ with your user account. That's what the `swarm login` command is for. You will then be prompted for *your* user name or email address and for your password.

    $ swarm login
    user or mail: luebken
    password:

Note that the password won't be displayed while you type.

Since we sent you your password in plain text via email, it is recommended to __change your password__ now. Use `swarm user -u password` for that purpose. You will be prompted to enter the old password and then twice the new one.

    $ swarm user -u password
    old password:
    new password:
    confirm new password:

Very well! The next thing you might want to try is __setting up a specific environment__. Environments allow you to run your apps in specific contexts, for example to distinguish development from production.

TODO: clarify if it's necessary to change the default environment.

Configure your default environment:

    $ swarm env <username>/dev

See [Working with environments](reference/env/) for further details.

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