# Getting started - Part 2

This page provides a slighlty more complex example using two components and a custom image. Please make you have `swarm` running. For details see [Getting Started](gettingstarted.md).

*TOC:*

* Example overview
* The currentweather server
* Create and push own images
* Defining dependencies


## Example overview

The example we are using here is very simple:

![](http://yuml.me/diagram/scruffy/class/[%E2%98%BA%20%7Bbg:yellow%7D]-%3E[CurrentWeather],[CurrentWeather]-%3E[Redis],%20[CurrentWeather]-%3E[openweathermap.org%20%7Bbg:white%7D]])

We have Docker container `currentweather` which contains a simple Node.JS script. This provides a http endpoint to see the current weather from Cologne. \* 
To get the data we are calling an external web service: [openweathermap.org](openweathermap.org). Since this is a great open API we want to be good citizens and cache the data locally and only get new data once a minute. The redis lives in a predefined redis container. 

All the sources can be found here: [github.com/luebken/currentweather](github.com/luebken/currentweather)

## The currentweather server

The Node.JS server: server.js

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

Giant Swarm uses Docker images. To create your own image you can use all the tools Docker provides although we recomind to use a [Dockerfile](https://docs.docker.com/reference/builder/)

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



The swarm configuration: *currentweather.json*
```
{
    "app_name": "currentweather",
    "services": [
        {
            "service_name": "currentweather-service",
            "components": [
                {
                    "component_name": "currentweather-component",
                    "image": "luebken/currentweather",
                    "ports": [ "1337/tcp" ],
                    "dependencies": [
                        { "name": "redis", "port": 6379 }
                    ],
                    "domains": { "currentweather.cluster-matthias-02.giantswarm.io": "1337" }
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


\* This example was already finished when Anna noted that there are already some weather website where you can check Colognes weather. Duuh.  