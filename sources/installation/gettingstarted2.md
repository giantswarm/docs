# Getting started - Part 2

<p class="lastmod">Last edited on November 14, 2014 by Matthias Lübken</p>

This page provides a slightly more complex example using two components and a custom image. Please make sure you have `swarm` running. For details see [Getting Started](gettingstarted.md).

*TOC:*

* Example overview
* The currentweather server
* Create and push own images
* Define dependency


## Example overview

The example we are using here is very simple:

![](/img/gettingstarted2_appschema.svg)

We have a Docker container `currentweather` which contains a simple NodeJS script. This provides a http endpoint to see the current weather from Cologne. \* 
To get the data we are calling an external web service: [openweathermap.org](openweathermap.org). Since this is a great open API, we want to be good citizens and cache the data locally and only get new data once a minute. For this we use a redis cache. The redis lives in a predefined redis container.

All the sources can be found here: [github.com/luebken/currentweather](http://github.com/luebken/currentweather)

## The currentweather server

The NodeJS server: server.js

```
var http = require('http');
var redis = require('redis');

var addr = process.env.REDIS_PORT_6379_TCP_ADDR;
var port = process.env.REDIS_PORT_6379_TCP_PORT;

client = redis.createClient(port, addr);

http.createServer(function (req, res) {
  client.get("currentweather", function (err, weather) {
    if(weather == null) {
      console.log('querying live weather data');
      var url = "http://api.openweathermap.org/data/2.5/weather?q=Cologne";
      http.get(url, function(res2) {
        var body = '';
        res2.on('data', function(chunk) {
          body += chunk;
        });
        res2.on('end', function() {
          var weatherjson = JSON.parse(body);
          var weather_new = weatherjson.weather[0].description;
          client.set('currentweather', weather_new);
          client.expire('currentweather', 60);
          writeResponse(res, weather_new);
        });
      }).on('error', function(e) {
        console.log("Got error: ", e);
      });
    } else {
      console.log('using cached weather data');
      writeResponse(res, weather);
    }
  })
}).listen(1337, '0.0.0.0');

function writeResponse(res, weather) {
  res.writeHead(200, {'Content-Type': 'text/plain'});
  res.end('Hello World from Cologne: ' + weather + '\n');
}

console.log('Server running at http://0.0.0.0:1337/');
```

and the *package.json*

```
{
  "name": "currentweather",
  "dependencies": {
    "redis": "*"
  }
}
```

## Create and push own images

Giant Swarm uses Docker images from public registries and the private Giant Swarm registry. See the [registry reference](/reference/registry.md) for more information.

For using Giant Swarm's private registry login with Docker: 
```
$ docker login https://registry.giantswarm.io
```

Dockerfile for *currentweather*: Dockerfile

```
FROM dockerfile/nodejs

WORKDIR /root

ADD package.json /root/
RUN npm install

ADD server.js /root/
EXPOSE 1337
CMD ["/usr/local/bin/node", "server.js"]
``` 

To use this Docker image it has to be built and uploaded to a repository. E.g. to push this image to the Giant Swarm registry for the user 'luebken' you would use:

```
$ docker build -t registry.giantswarm.io/luebken/currentweather .
$ docker push registry.giantswarm.io/luebken/currentweather
```

To test this setup locally, you first have to start a container from the official 'redis' image. Afterwards you have to start a container from your currentweather image and link it with the redis container:

```
$ docker run -d --name redis redis
$ docker run  -i -p 1337:1337 --link redis:redis registry.giantswarm.io/luebken/currentweather
```

## Define dependency

In the 'swarm.json' you have these two containers defined as components. The depdency is defined by the container (here the currentweather-service) that uses the other container:

The swarm configuration: *swarm.json*
```
{
    "app_name": "currentweather",
    "services": [
        {
            "service_name": "currentweather-service",
            "components": [
                {
                    "component_name": "currentweather-component",
                    "image": "registry.giantswarm.io/luebken/currentweather",
                    "ports": [ "1337/tcp" ],
                    "dependencies": [
                        { "name": "redis", "port": 6379 }
                    ],
                    "domains": { "currentweather.alpha.giantswarm.io": "1337" }
                },
                {
                    "component_name": "redis",
                    "image": "redis",
                    "ports": [ "6379/tcp" ]
                }
            ]
        }
    ]
}

```

To start this example:
```
$ swarm create swarm.json

$ swarm ls
1 app created so far!

app             env   company    created
currentweather  dev   luebken    2014-09-22 18:53:44

$  swarm status currentweather
App currentweather is down!

service                 component                 instanceid                            status
currentweather-service  currentweather-component  d4664c37-49cb-436b-a2f0-727bb5539538  down
currentweather-service  redis                     02288488-4185-473b-8de1-47f91971bdb2  down

$ swarm start currentweather
Starting app currentweather ...
```

Check the status until all components are *up*:
```
$ swarm status currentweather
App currentweather is starting!

service                 component                 instanceid                            status
currentweather-service  currentweather-component  d4664c37-49cb-436b-a2f0-727bb5539538  starting
currentweather-service  redis                     02288488-4185-473b-8de1-47f91971bdb2  up

$ swarm status currentweather
App currentweather is up!

service                 component                 instanceid                            status
currentweather-service  redis                     02288488-4185-473b-8de1-47f91971bdb2  up
currentweather-service  currentweather-component  d4664c37-49cb-436b-a2f0-727bb5539538  up

$ curl currentweather.alpha.giantswarm.io
Hello World from Cologne: overcast clouds
```

\* This example was already finished when Anna noted that there are already some weather websites, where you can check Cologne's weather. Duuh.  
