# What is Giant Swarm?

With Giant Swarm you can build and host server-side applications. There are no restrictions concerning programming languages, web frameworks or databases. 

A Swarm application consists of an application description called `swarm.json`and one or more Docker containers. 

## What is Docker

> Self-sufficient linux containers.
 
Docker is the most popular application container format. It let's you package your own Linux in lightweight, portable and self-sufficient manner. Some call it therefor lightweight VM. In contrast to traditional VM's its an order of magnitude faster, lighter and more fun. ;-)

Docker makes a great tool for developer since it allows you to package different parts of your applications in your own containers. These containers can run on different environments like your and your colleagues notebook and different server environments.

Another great aspect of Docker is that there are lots of predefined containers available. From different languages like JavaScript to Golang over different webstacks like Spring to Rails down to databases like Redis or MySQL. In addition defining your own Docker container is very easy. If you follow our `Getting started` you will define your first Docker container within the next half an hour or so.

## What is the swarm.json

> Configuration for describing your Giant Swarm apps

Giant Sarm enables you to easily deploy, orchestrate and operate your Docker based applications. For this means you start describing your application with simple json file. Your application is structured into services and components. The services from logical units and contain one or more components. Components are based on Docker images.

// graphic: app > services > component

## The Swarm CLI

> A simple binary to control your Swarm apps

// describe basic swarm functionality

// In getting started describe docker and dockerregistry.

## Why Microservices?

//TODO

The days of big monolith applications are long over. Modularizing your applications in services has been the way to go for some time. Each self-contained functionality constitutes a separate service. This makes them independently developable, deployable, and scalable. Each with its own potential database and programming language. The right tool for the job! The [12factor Apps](http://12factor.net/) paradigm goes even further by describing twelve fundamental requirements of modern Software-as-a-Service apps - worth looking at.

At the same time it has always been a hassle to set up a truly service-oriented application. Or the solutions were too cumbersome and stood in the way. Giant Swarm keeps it lean and gets out of the way.



   





