description: A slightly more involved tutorial for those who have tested out our Getting Started guide part 1.

# Getting started - Part 2

<p class="lastmod">Last edited on January 19, 2015 by Marian Steinbach</p>

This tutorial guides you through the creation of a application using two interlinked components and a custom Docker image. The core is a NodeJS server (however you don't need any knowledge of NodeJS, let alone install anything NodeJS-specific). A Redis server is used as a temporary data store and we connect to an external API.

## Prerequisites

* Please make sure you have the `swarm` <abbr title="Command Line Interface">CLI</abbr> installed. Ideally you have followed our [Getting Started Guide - Part 1](gettingstarted.md).

* In addition we assume that you have a basic understanding of Docker. Please make sure that you have Docker installed. Docker provides extensive [installation instructions](https://docs.docker.com/installation/) and [user guides](https://docs.docker.com/userguide/).

* The sources code for this tutorial can be found here: [https://github.com/giantswarm/giantswarm-currentweather](https://github.com/giantswarm/giantswarm-currentweather).

To facilitate following this guide, we recommend you clone the repository:

```
git clone git@github.com:giantswarm/giantswarm-currentweather.git
cd giantswarm-currentweather
```

## Testing Docker and getting some base images

We have a Docker task ahead of us that could be a little time-consuming. The good thing is that we can make things a lot faster with some preparation. As a side effect, you can make sure that `docker` is working as expected on your system.

We need to pull two images from the public Docker library, namely `redis` and `google/nodejs`. Together they can take a few hundret megabyte of data transfer. Start the prefetching using this command:

```
$ docker pull redis && docker pull google/nodejs
```

<i class="fa fa-exclamation-triangle"></i> __Note for Linux users__: You probably have to call the `docker` binary with root privileges, so please use `sudo docker` whenever the docker command is required here. For example, initiatie the prefetching like this:

```
$ sudo docker pull redis && sudo docker pull google/nodejs
```

We won't repeat the `sudo` note for the sake of readability of the rest of this tutorial.

While your terminal and network connection are kept busy with loading Docker images, let's have a look on what exatly it is we are going to build.

## Overview of our application

This diagram depicts how our application components will be set up.

![Application schema diagram](/img/gettingstarted2_appschema.svg)

We have one component which we call `nodejs` as the core piece. It will provide a NodeJS HTTP server. When accessed by a user, it should display the current weather at our home town, Cologne/Germany<sup>1</sup>.

We get the weather data from the [openweathermap.org](openweathermap.org) API. Since we want to be good citizens and not call that API more often than necessary, we cache the API responses locally for a while. For this we use a Redis cache, which is our second component, called `redis` in the diagram above.

## The NodeJS server component

Our NodeJS server consists of only two little files:

* A JavaScript file called `server.js` which contains all our application logic
* A dependencies description file called `package.json`

If you're interested in the internal workings of the server, check their content from the [GitHub](https://github.com/giantswarm/giantswarm-currentweather) repository. For our tutorial, it's not too important, so we cut the details here.

## Building our Docker image

We now create a Docker image for our NodeJS server. Here is the `Dockerfile` we use for that purpose:

```
FROM google/nodejs

WORKDIR /app

ADD package.json /app/
ADD server.js /app/
RUN npm install

EXPOSE 1337
CMD ["/nodejs/bin/node", "server.js"]
``` 

As you can see, we use a [NodeJS image provided by Google](https://registry.hub.docker.com/u/google/nodejs/) as a basis. That means NodeJS is already in place. All we have to do is add the two files we introduced earlier to the container and execute `npm install` inside it.

Assuming that your Giant Swarm username is `yourusername`, to build the image, execute

```
$ docker build -t registry.giantswarm.io/yourusername/currentweather .
```

## Testing locally

To test locally before deploying to Giant Swarm, we also need a redis server. This is very simple, since we can use a standard image here without any modification. Simply run this to start your local Redis server container:

```
$ docker run --name="currentweather-redis" -d redis
```

Now let's start the server container for which we just created the Docker image. Here is the command:

```
$ docker run --link redis:redis -p 1337:1337 -ti --rm registry.giantswarm.io/marian/currentweather
```

Accessing the server in a browser requires knowledge of the IP address your docker host binds to containers. This depends on the operating system.

__Mac/Windows__: with `boot2docker` you can find it out using `boot2docker ip`. The default here is `192.168.59.103`.

__Linux__: the command `ip addr show docker0|grep inet` should print out a line containing the correct address. The default in this case is `172.17.42.1`.

So one of the following two commands will likely work:

```
$ curl 192.168.59.103:1337
$ curl 172.17.42.1:1337
```

Your output should look something like

```
Current weather in Cologne: moderate rain, temperature 10 degrees, wind 42 km/h
```

Try a second request immediately after to test the cache.

In the server console you will see an output like

```
Server running at http://0.0.0.0:1337/
Querying live weather data
Using cached weather data
```

Awesome. Now let's deploy it to the cloud.

## Bringing it to Giant Swarm

### Uploading to a Docker registry

To use this Docker image it has to be built and uploaded to a registry. It's up to you to decide which registry you want to use. Giant Swarm offers you a private registry, so we explain how to upload ("push") to that one here.

For more information on using the Giant Swarm registry, see our [registry reference](../reference/registry.md).

Before pushing to the registry, you have to log in with the `docker` client. Use this command:

```
$ docker login https://registry.giantswarm.io
```

You will be prompted for username and password. Use your Giant Swarm account credentials here.

Still assuming that your username is `yourusername`, you can now push the image like this:

```
$ docker push registry.giantswarm.io/yourusername/currentweather
```

### Configuring your application

Applications in Giant Swarm are [configured using a JSON configuration file](../reference/swarm-json.md) that is usually called `swarm.json`. Four this application, we create a configuration containing one service with two components.

Pay close attention to how we create a link between our two components by defining a dependency in the `nodejs` component pointing to the `redis` component.

```
{
  "app_name": "currentweather-app",
  "services": [
    {
      "service_name": "currentweather-service",
      "components": [
        {
          "component_name": "nodejs",
          "image": "registry.giantswarm.io/$company/currentweather",
          "ports": ["1337/tcp"],
          "dependencies": [
            {
              "name": "redis",
              "port": 6379
            }
          ],
          "domains": {
            "currentweather-$company.gigantic.io": "1337"
          }
        },
        {
          "component_name": "redis",
          "image": "redis",
          "ports": ["6379/tcp"]
        }
      ]
    }
  ]
}
```

With the above configuration saved as `swarm.json` in your current directory you can now create and start the application. Make sure to replace `yourusername` with your actual username.

```
$ swarm up --var=company=yourusername
```

The flag `--var=company=yourusername` will take care of placing your username in the positions where the `$company` variable is used in `swarm.json`.

You will get some progress output like this during creation and startup of your application:

```
Creating 'currentweather-app' in the 'marian/dev' environment...
Application created successfully!
Starting application currentweather-app...
Application currentweather-app is up.
You can see all services and components using this command:

    swarm status currentweather-app

```

Let's do as we are told and check the status of this application.

```
$ swarm status currentweather-app
App currentweather-app is up

service                 component  instanceid                            created              status
currentweather-service  nodejs     1d23c62a-3ebf-4a01-a054-05fbf024eb0a  2015-01-15 15:35:46  up
currentweather-service  redis      04570837-9ac3-4959-bc74-ad49eafaaa3f  2015-01-15 15:35:46  up
```

Here you have them, your two components, running on Giant Swarm. If you want to, you can check the logs using the instance IDs you see in the `swarm status output`. The syntax for the command is `swarm logs <instance-id>`. 

Seeing is believing, they say. So let's do the final test that your application is actually doing what it should.

```
$ curl currentweather-yourusername.gigantic.io
Current weather in Cologne: light rain, temperature 9 degrees, wind 41 km/h
```

## Further reading

* TODO: Where should we link to? swarm.json reference page?

## Remarks

<sup>1</sup> This example was already finished when our team member Anna pointed out that there are already numerous sites on the web allowing us to check Cologne's current weather. Duuh.
