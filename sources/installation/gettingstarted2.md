description: A slightly more involved tutorial for those who have tested out our Getting Started guide part 1.

# Getting started - Part 2

<p class="lastmod">Last edited on January 15, 2015 by Marian Steinbach</p>

This page provides a slightly more complex example using two components and a custom Docker image. The core is a NodeJS server. In addition, a Redis cache is used and we connect to an external API.

## Prerequisites

* Please make sure you have the `swarm` <abbr title="Command Line Interface">CLI</abbr> installed. Ideally you have followed our [Getting Started Guide - Part 1](gettingstarted.md).

* In addition we assume that you have a basic understanding of Docker. Please make sure that you have Docker installed. Docker provides extensive [installation instructions](https://docs.docker.com/installation/) and [user guides](https://docs.docker.com/userguide/).

All the sources for this guide can be found here: [https://github.com/giantswarm/giantswarm-currentweather](https://github.com/giantswarm/giantswarm-currentweather)

## Overview of our application

This diagram depicts how our application components will be set up.

![Application schema diagram](/img/gettingstarted2_appschema.svg)

We have one component which we call `nodejs` as the core piece. It will provide a NodeJS HTTP server. When accessed by a user, it should display the current weather at our home town, Cologne/Germany<sup>1</sup>.

We get the weather data from the [openweathermap.org](openweathermap.org) API. Since we want to be good citizens and not call that API more often than necessary, we cache the API responses locally for a while. For this we use a Redis cache, which is our second component, called `redis` in the diagram above.

## The NodeJS server component

Our NodeJS server basically consists of a single JavaScript file we call `server.js`:

```javascript
var http = require("http");
var redis = require("redis");

var redisAddress = process.env.REDIS_PORT_6379_TCP_ADDR,
  redisPort = process.env.REDIS_PORT_6379_TCP_PORT,
  httpAddress = "0.0.0.0",
  httpPort = "1337";

client = redis.createClient(redisPort, redisAddress);

http.createServer(function (request, response) {
  client.get("currentweather", function (err, weatherString) {
    if (weatherString == null) {
      console.log("Querying live weather data");
      var url = "http://api.openweathermap.org/data/2.5/weather?q=Cologne";
      http.get(url, function(apiResponse) {
        var body = "";
        apiResponse.on("data", function(chunk) {
          body += chunk;
        });
        apiResponse.on("end", function() {
          var weather = JSON.parse(body);
          weatherString = weather.weather[0].description;
          weatherString += ", temperature " + Math.round(weather.main.temp - 273);
          weatherString += " degrees, wind " + Math.round(weather.wind.speed * 3.6) +  " km/h"
          client.set("currentweather", weatherString);
          client.expire("currentweather", 60);
          writeResponse(response, weatherString);
        });
      }).on("error", function(e) {
        console.log("Got error: ", e);
      });
    } else {
      console.log("Using cached weather data");
      writeResponse(response, weatherString);
    }
  });
}).listen(httpPort, httpAddress);

function writeResponse(res, weather) {
  res.writeHead(200, {"Content-Type": "text/html"});
  res.end("Current weather in Cologne: " + weather + "\n");
}

console.log("Server running at http://" + httpAddress + ":" + httpPort + "/");
```

To provide NodeJS with the required dependencies, there is also this `package.json` file:

```json
{
  "name": "currentweather",
  "description": "A sample application for Giant Swarm using NodeJS and Redis",
  "repository": {
    "type": "git",
    "url": "https://github.com/giantswarm/giantswarm-currentweather"
  },
  "dependencies": {
    "redis": "*"
  }
}
```

## Building our Docker image

We now create a Docker image for our NodeJS server. Here is the `Dockerfile` we use for that purpose:

```
FROM google/nodejs

WORKDIR /app
ADD package.json /app/
ADD server.js /app/
RUN npm install

EXPOSE 1337
CMD /nodejs/bin/node server.js
``` 

As you can see, we use a [NodeJS image provided by Google](https://registry.hub.docker.com/u/google/nodejs/) as a basis. That means NodeJS is already in place. All we have to do is add the two files we introduced earlier to the container and execute `npm install` inside it.

Assuming that your Giant Swarm username is `yourusername`, to build the image, execute

```
$ docker build -t registry.giantswarm.io/yourusername/currentweather .
```

## Testing locally

To test locally before deploying to Giant Swarm, we also need a redis server. This is very simple, since we can use a standard image here without any modification. Simply run this to start your local Redis server container:

```
$ docker run --name="redis" -p 6379:6379 -d redis
```

Now let's start the server container for which we just created the Docker image. Here is the command:

```
$ docker run --link redis:redis -p 1337:1337 -ti --rm registry.giantswarm.io/marian/currentweather
```

Accessing the server in a browser requires knowledge of the IP address your docker host binds to containers. With `boot2docker` you can find it out using `boot2docker ip`. The default here is `192.168.59.103`. When on Linux, the command `ip addr show docker0|grep inet` should print out a line containing the correct address. The default in this case is `172.17.42.1`.

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

To use this Docker image it has to be built and uploaded to a repository. It's up to you to decide which registry you want to use. Giant Swarm offers you a private registry, so we explain how to upload ("push") to that one here.

Before pushing to the registry, you have to log in with the `docker` client. Use this command:

```
$ docker login https://registry.giantswarm.io
```

You will be prompted for username and password. Use your Giant Swarm account credentials here.

Still assuming that your username is `yourusername`, you can now push the image like this:

```
$ docker push registry.giantswarm.io/yourusername/currentweather
```

For more information on using the Giant Swarm registry, see our [registry reference](../reference/registry.md).

### Configuring your application

As you should already know, applications in Giant Swarm are configured using a JSON configuration file that is usually called `swarm.json`. Four this application, we create a configuration containing one service with two components.

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
