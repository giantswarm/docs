+++
title = "Your first application — in Go"
description = "Your first Go application on Giant Swarm, using your own Docker container and connecting multiple components."
date = "2015-02-03"
type = "page"
weight = 50
categories = ["basic"]
+++

# Your first application — in Go on Giant Swarm

This tutorial guides you through the creation of an application using two interlinked components and a custom Docker image. The core is a Golang server. Additionally, a Redis server is used as a temporary data store and we connect to an external API.

## Prerequisites

* You should have done the [Quick Start](/) or the [Annotated Hello World Example](/guides/annotated-helloworld/) and everything should have worked fine.

* We assume that you have a basic understanding of Docker and you have Docker installed. Docker provides extensive [installation instructions](https://docs.docker.com/installation/) and [user guides](https://docs.docker.com/userguide/).


## For the impatient

The sources code for this tutorial can be found [on GitHub](https://github.com/giantswarm/giantswarm-firstapp-go). To facilitate following this guide, we recommend you clone the repository using this command:

```nohighlight
$ git clone https://github.com/giantswarm/giantswarm-firstapp-go.git
$ cd giantswarm-firstapp-go
```


If you're not the type who likes to read a lot, we have a [Makefile](https://github.com/giantswarm/giantswarm-firstapp-go/blob/master/Makefile) in the repository. This file helps you to get everything described below going using these commands:

```nohighlight
$ swarm login <yourusername>
$ make # Build the linux go binary
$ make docker-build # Build the Docker image
$ make docker-run-redis # Run the redis container
$ make docker-run # Run the Go container
$ make docker-push # Push the Go container
$ make swarm-up # Start the application on Giant Swarm
```

Everybody else, follow the path to wisdom and read on.

## Testing Docker and getting some base images

We need to pull two images from the public Docker library, namely `redis` and `busybox`:

```nohighlight
$ docker pull redis:latest && docker pull busybox:ubuntu-14.04
```

__For Linux users__: You probably have to call the `docker` binary with root privileges, so please use `sudo docker` whenever the docker command is required here. For example, initiate the prefetching like this:

```nohighlight
$ docker pull redis:latest && docker pull busybox:ubuntu-14.04
```

We won't repeat the `sudo` note for the sake of readability of the rest of this tutorial. Docker warns you if the priveleges aren't okay, so you'll be remembered anyway.

While your terminal and network connection are kept busy with loading Docker images, let's have a look on what exactly we are going to build.

## Overview of our application

This diagram depicts how our application components will be set up.

![Application schema diagram](/img/your-first-application-schema-nodejs.svg)

We have one component which we call `webserver` as the core piece. It will provide a Go HTTP server. When accessed by a user, it should display the current weather at our home town, Cologne/Germany.

We get the weather data from the [openweathermap.org](http://openweathermap.org/) API. Since we want to be good citizens and not call that API more often than necessary, we cache the API responses locally for a while. For this we use a Redis cache, which is our second component, called `redis` in the diagram above.

## The Go server component

Our Go server consists of one file called [main.go](https://github.com/giantswarm/giantswarm-firstapp-go/blob/master/main.go) which contains all our application logic. There is quite some nice Golang features in file like go functions and channels. For our tutorial, it's not too important, so we cut the details here.

One thing that is important in the Go context is that we build platform specific binaries. Since Docker is based on Linux we need to make sure that we build a Linux binary. Fortunately there is a [Dockerfile](https://github.com/docker-library/golang/blob/acc4ed5ba8dfad17bd484ac858950bc6a6f9acde/1.3/cross/Dockerfile) we can leverage to cross-compile. Please see the [Makefile target](https://github.com/giantswarm/giantswarm-firstapp-go/blob/master/Makefile#L30) to see how to start it.

## Building our Docker image

We now create a Docker image for our Go server. Here is the `Dockerfile` we use for that purpose:

```Dockerfile
FROM busybox:ubuntu-14.04

ADD ./currentweather /usr/bin/

EXPOSE 8080

ENTRYPOINT ["currentweather"]
``` 

We use a tiny [busybox image](https://github.com/jpetazzo/docker-busybox/blob/ca435164f45c40d761fad9ef9b5a76a6ba0d5f1a/Dockerfile) and just need to add our `currentweather` binary. All the beauty of a indpendent binary.

The prefetching of Docker images you started a couple of minutes ago should be finished by now. If not, please wait until it's done.

Assuming that your Giant Swarm username is `yourusername`, to build the image, you  then execute:

```nohighlight
$ docker build -t registry.giantswarm.io/yourusername/currentweather ./
```

## Testing locally

To test locally before deploying to Giant Swarm, we also need a redis server. This is very simple, since we can use a standard image here without any modification. Simply run this to start your local Redis server container:

```nohighlight
$ docker run --name=redis -d redis
```

Now let's start the server container for which we just created the Docker image. Here is the command (replace `yourusername` with your username):

```nohighlight
$ docker run --link redis:redis -p 1337:1337 -ti --rm registry.giantswarm.io/yourusername/currentweather
```

It should be running. But we need proof! Let's issue an HTTP request.

Accessing the server in a browser requires knowledge of the IP address your docker host binds to containers. This depends on the operating system.

__Mac/Windows__: with `boot2docker` you can find it out using `boot2docker ip`. The default here is `192.168.59.103`.

__Linux__: the command `ip addr show docker0|grep inet` should print out a line containing the correct address. The default in this case is `172.17.42.1`.

So one of the following two commands will likely work:

```nohighlight
$ curl 192.168.59.103:1337
$ curl 172.17.42.1:1337
```

Your output should look something like this:

```nohighlight
Current weather in Cologne: moderate rain, temperature 10 degrees, wind 42 km/h
```

Try at least two requests within 60 seconds to verify your cache is working.

In the server console you will see an output like this:

```nohighlight
Server running at http://0.0.0.0:1337/
Querying live weather data
Using cached weather data
```

Awesome. Now let's deploy it to the cloud.

## Bringing it to Giant Swarm

### Uploading to the registry

To use this Docker image on Giant Swarm it has to be uploaded to a Docker registry. Giant Swarm offers you a such a registry. Here we briefly explain how to use it. For more information on using the Giant Swarm registry, see our [registry reference](../reference/registry.md).

Before pushing to the registry, you have to log in with the `docker` client. Use this command:

```nohighlight
$ docker login https://registry.giantswarm.io
```

You will be prompted for username, password and email. Use your Giant Swarm account credentials here.

Still assuming that your username is `yourusername`, you can now push the image like this:

```nohighlight
$ docker push registry.giantswarm.io/yourusername/currentweather
```

### Configuring your application

Applications in Giant Swarm are [configured using a JSON configuration file](../reference/swarm-json.md) that is usually called `swarm.json`. For this application, we create a configuration containing one service with two components.

Pay close attention to how we create a link between our two components by defining a dependency in the `webserver` component pointing to the `redis` component.

```json
{
  "app_name": "currentweather",
  "services": [
    {
      "service_name": "currentweather-service",
      "components": [
        {
          "component_name": "webserver",
          "image": "registry.giantswarm.io/$username/currentweather:latest",
          "ports": ["8080/tcp"],
          "dependencies": [
            {
              "name": "redis",
              "port": 6379
            }
          ],
          "domains": {
            "currentweather-$username.gigantic.io": "8080"
          }
        },
        {
          "component_name": "redis:latest",
          "image": "redis",
          "ports": ["6379/tcp"]
        }
      ]
    }
  ]
}
```

### Starting the application

With the above configuration saved as `swarm.json` in your current directory you can now create and start the application using the `swarm up` command below. As always, replace `yourusername` with your actual username. The flag `--var=company=yourusername` will take care of placing your username in the positions where the `$username` variable is used in `swarm.json`.

```nohighlight
$ swarm up --var=company=yourusername
```

You will see some progress output during creation and startup of your application:

```nohighlight
Creating 'currentweather' in the 'yourusername/dev' environment...
Application created successfully!
Starting application currentweather...
Application currentweather is up.
You can see all services and components using this command:

    swarm status currentweather

```

Seeing is believing, they say. So let's do the final test that your application is actually doing what it should. Open the URL (with your username in the right place) in the browser:

[http://currentweather-yourusername.gigantic.io/](http://currentweather-yourusername.gigantic.io/)

If you watched closely, after starting our app we got the recommendation to check it's status using

```nohighlight
$ swarm status currentweather
```

So here is what we get when doing so (your output will vary slightly):

```nohighlight
App currentweather is up

service                 component  instanceid                            created              status
currentweather-service  redis      7121393e-e649-4f84-9121-9b642c4473bc  2015-02-03 22:17:38  up
currentweather-service  webserver  7e769815-8623-4f5b-8ec6-a2b31d302f24  2015-02-03 22:17:38  up
```

Here you have them, your two components, running on Giant Swarm. If you want to, you can check the logs using the instance IDs you see in the `swarm status output`. The syntax for the command is `swarm logs <instance-id>`. 

Now if you like, you can stop or even delete the application again.

```nohighlight
$ swarm stop currentweather
$ swarm delete currentweather
```

We hope you enjoyed this tutorial. If yes, feel free to tweet and blog it out in the world. If not, please let us know what bugged you (see chat and support info at the bottom of this page).

If you're still hungry, why not continue with a more advanced tutorial?

## Further reading

* [Swarmify Ruby on Rails](../guides/ruby_on_rails.md) - A simple Rails example involving MySQL
* [Swarmify Python](../guides/python.md) - A very simple Flask boilerplate
* [Getting started with Docker and MeanJS](http://blog.giantswarm.io/getting-started-with-docker-and-meanjs) - Easily adaptable to Giant Swarm with the experience you have by now.