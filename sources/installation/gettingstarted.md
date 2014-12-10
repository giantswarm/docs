description: A first practical introduction into using Giant Swarm. This will take you to a simple Hello World example.

# Getting started

<p class="lastmod">Last edited on December 1, 2014 by Matthias Lübken</p>


This page gets you started with Giant Swarm. It will show you how to install the required tools and get a provided Docker image running.

## Prerequisites

This section assumes that you have an account with Giant Swarm. If not please sign up at [giantswarm.io](http://giantswarm.io). Please note that we currently have a waiting list. It may take a while before you get an invite.

## Installing the CLI

The current CLI is v0.8.0.

If you are on Mac OS X and have [homebrew](http://brew.sh/) installed, you can just tap it:

```
$ brew tap giantswarm/swarm
$ brew install swarm-client
```

### Manual install the swarm CLI

For manual installation, download a tarball from here:

  * [Mac](http://downloads.giantswarm.io/swarm/clients/0.8.0/swarm-0.8.0-darwin-amd64.tar.gz)
  * [Linux](http://downloads.giantswarm.io/swarm/clients/0.8.0/swarm-0.8.0-linux-amd64.tar.gz)

You can place the __swarm binary__ somewhere convenient, preferably in a location that's contained in your `PATH` environment variable. For example, `/usr/local/bin/` works fine in many cases.

## Say hi to the swarm

Now that you have the `swarm` command available, you can use check the cluster's availability:

    $ swarm ping

You should get an `OK` as a result.

Now that the connection to your cluster is set up, it's time to __log in__ with your user account. That's what the `swarm login` command is for. You will then be prompted for your user name or email address and for your password.

    $ swarm login
    user or mail: luebken
    password:

Note that the password won't be displayed while you type.

Since we sent you your password in plain text via email, it is recommended to __change your password__ now. Use `swarm user -u password` for that purpose. You will be prompted to enter the old password, and then the new one twice.

    $ swarm user -u password
    old password:
    new password:
    confirm new password:

The next thing you might want to try is setting up a specific environment. See [Working with environments](/reference/env/) for further details.

## Configure a helloworld application

Create a file called `swarm.json` with your favourite editor and fill it with the following JSON code.

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

Before you can run the application it needs to be created. To do so, use the `create` command in the directory where your `swarm.json` file resides: 

    $ swarm create

To start this app use the `start` command followed by the `app_name` specified in the JSON:

    $ swarm start helloworld

While it's starting (which may take a while) you may check its status with the `status` command:

    $ swarm status helloworld
    App helloworld is starting!

    service             component  instanceid                            status
    helloworld-service  python     4cc709fc-5250-4bab-83d3-837cd0f7af36  starting

Once it's up, you can check it by opening the specified domain in a browser or `curl`ing it:
    
    $ curl helloworld.alpha.giantswarm.io
    Hello Giant Swarm. \o/

On the way you might want to check for the logs by querying against the instanceid:

    $ swarm logs 4cc709fc-5250-4bab-83d3-837cd0f7af36

To stop and delete an app use `swarm stop` and `swarm delete`.

> *Congratulations* you've created and started your first swarm app!

After you have celebrated your success head over to [Part 2](gettingstarted2.md) to see how to define your own images.
