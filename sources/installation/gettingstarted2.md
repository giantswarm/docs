# Getting started - Part 2

This page provides a slighlty more complex example with using two services and a custom image. Please make you have `swarm` running. For details see [Getting Started](gettingstarted.md).

> TODO put some content in here

Basic idea:

  * One backend service: _weather_
    * a small node service 
    * calling openweathermap.org for current weather in cologne
    * exposing it as simplest service
    * [https://github.com/luebken/currentweather](https://github.com/luebken/currentweather)
    * https://hub.docker.com/u/luebken/currentweather/
  * One frontend service: _nginx_ 
    * a simplest nginx with 
    * using weather as upstream
    * [https://github.com/luebken/hellonginx](https://github.com/luebken/hellonginx)
    * https://hub.docker.com/u/luebken/hellonginx/
  * swarm config:
    * https://github.com/luebken/hellonginx/blob/master/hellonginx.json


