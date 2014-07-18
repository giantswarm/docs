# Getting started - Part 2

This page provides a slighlty more complex example using two components and a custom image. Please make you have `swarm` running. For details see [Getting Started](gettingstarted.md).

*TOC:*

* Example overview
* Create and push own images
* Defining dependencies


## Example overview

The example we are using here is very simple:

![](http://yuml.me/diagram/scruffy/class/[CurrentWeather]-%3E[Redis],%20[CurrentWeather]-%3E[openweathermap.org%20%7Bbg:white%7D]])

We have Docker container `currentweather` which contains a simple Node.JS script. This provides a http endpoint to see the current weather from Cologne. \* 
To get the data we are calling an external web service: [openweathermap.org](openweathermap.org). Since this is a great open API we want to be good citizens and cache the data locally and only get new data once a minute. The redis lives in a predefined redis container. 

## Create and push own images

Giant Swarm uses Docker images. To create your own image you can use all the tools Docker provides although we recomind to use a [Dockerfile](https://docs.docker.com/reference/builder/)

https://github.com/luebken/currentweather

\* This example was already finished when Anna noted that there are already some weather website where you can check Colognes weather. Duuh.  