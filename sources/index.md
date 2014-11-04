# Welcome to Giant Swarm

> **Note**:
> We are currently in an early alpha state and lots of things are still in development. Although we do our best, some parts of this documentation might be outdated. If something unexepected happens don't hesitate to contact us: [support@giantswarm.io](mailto:support@giantswarm.io)

![anty](img/ant.png)

## What is Giant Swarm?

Giant Swarm enables you to easily develop, deploy and host your micro-serviced application. We leverage several technologies like Docker and CoreOS and bring them together to a simple yet powerful platform. Besides Docker and your application stack there is not much to know to get started.

## Why Microservices?

The days of big monolith applications are long over. Modularizing your application in services has been the way to go for some time. Each self-contained functionality is developed in a separate service. This makes them independently developable, deployable and scalable. Each with it's own potential database and programming language. The right tool for the job! The [12factor Apps](http://12factor.net/) paradigm goes even further by describing twelve fundamental requirements of modern software-as-a-service. Worth looking at.

At the same time it has always been a hassle to set up a truly service-oriented application. Or the solutions were too cumbersome and stood in the way. Giant Swarm keeps it lean and gets out of the way.

## Overview of the docs

We currently have three sections in our docs:

### <i class="fa fa-cogs"></i> [Installation](installation/cheatsheet.md)
This section gets you started with Giant Swarm: how to install the CLI and get up and running.

 * [Cheat sheet](./installation/cheatsheet.md)
 * [Getting started, part 1](./installation/gettingstarted.md)
 * [Getting started, part 2](./installation/gettingstarted2.md)

### <i class="fa fa-road"></i> [Guides](guides/ruby_on_rails.md) 
This section provides in-depth guides to specific topics:
 
 * [Swarmify Ruby on Rails](./guides/ruby_on_rails.md)
 * [Swarmify PHP and Symfony](./guides/symfony.md)
 * [Swarmify Python](./guides/python.md)

### <i class="fa fa-book"></i> [Reference](reference/)
This section will contain detailed description of the different features Giant Swarm has to offer.

 * [Companies](./reference/companies.md)
 * [Environments](./reference/env.md)
 * [Swarm.json reference](./reference/swarm-json.md)
 * [Shell command completion](./reference/completion.md)
