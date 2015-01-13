description: This is the table of contents for the Giant Swarm Reference, including an overview of 'swarm' CLI subcommands.

# Reference

The reference area of our documentation is where you get structured information about (eventually) all parts of our client software.

## Contents

#### [Release notes](release-notes/)

Check this page for news on the latest release of our command line interface (CLI).

#### [Global command line options](global-options/)

Options and argument to change the bahaviour of almost all CLI commands.

#### [Getting basic information](info/)

How to get basic information on your login status and environment.

#### [Companies](companies/)

How to deal with companies, adding and removing users.

#### [Environments](env/)

Managing environments for different purposes like e. g. development, staging or production.

#### [Application configuration (`swarm.json`)](swarm-json/)

Configuring applications for Giant Swarm using our JSON format. Comprehensive documentation of all possible keys. Also a good entry point to learn about some advanced features.

#### [Creating an app](create/)

Deploying a readily configered app to giant swarm. Also gives information on how to use variables in the application configuration to treat different environments differently.

#### [Creating and starting an app](up/)

How to create and start an application in only one command.

#### [Starting an application or service](start/)

Starting an application or some part of it.

#### [Stopping an application or service](stop/)

Stopping an application or some part of it.

#### [Listing applications](ls/)

Getting an overview of all applications available in an environment.

#### [Getting an application's status](status/)

Finding out which parts of an application are running, how many instances there are per component and how to get details about component instances.

#### [Getting instance statistics](stats/)

Accessing basic statistics about a component instance, like memory and CPU usage.

#### [Accessing process logs](logs/)

Accessing logs of components to debug process details.

#### [Modifying user settings](user/)

Setting a user's email and password

#### [Using the registry](registry/)

How to tag Docker images and upload them to the Giant Swarm registry for use in applications.



## Command reference

A place to quickly lookup help pages for all `swarm` <abbr title="command line interface">CLI</abbr> commands.

Command                 | Description
----------------------- | -------------------------------
[up](up/)               | Define and start a new app
[info](info/)           | Get basic information on context and environment
[create](create/)       | Define a new app by loading a json file
[status](status/)       | Show current status of an app or service
[start](start/)         | Start an application or service
[stop](stop/)           | Stop an application or service
delete                  | Delete an app. Note that you lose all contained data by doing so.
[scaleup](scaleup/)     | Increase number of instances running a component
[scaledown](scaledown/) | Reduce number of instances running a component
[logs](logs/)           | Print an app's standard output and error messages
[stats](stats/)         | Print basic statistics of an instance
version                 | Print swarm client version
[ls](ls/)               | List all apps
[env](env/)             | Handle environments
[cat](cat/)             | Show the configuration of an application
login                   | Log in to your account
logout                  | Log out from your account
[user](user/)           | Create and modify users
[company](companies/)   | Manage companies
completion              | Setup CLI completion

<!-- Command is deactivated
update                  | Update a component by changing the docker image to a newer version
-->
