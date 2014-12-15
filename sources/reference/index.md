description: This is the table of contents for the Giant Swarm Reference, including an overview of 'swarm' CLI subcommands.

# Reference

The reference area of our documentation is where you get structured information about (eventually) all parts of our client software.

## Contents

 * [Global command line options](global-options/)
 * [Getting basic information](info/)
 * [Companies](companies/)
 * [Environments](env/)
 * [Application configuration (`swarm.json`)](swarm-json/)
 * [Creating an app](create/)
 * [Creating and starting an app](up/)
 * [Starting an application or service](start/)
 * [Getting an app's status](status/)
 * [Getting instance statistics](stats/)
 * [Accessing process logs](logs/)
 * [Modifying user settings](user/)
 * [Using the registry](registry/)


## Command reference

A place to quickly lookup help pages for all `swarm` <abbr title="command line interface">CLI</abbr> commands.

Command                 | Description
----------------------- | -------------------------------
[up](up/)               | Define and start a new app
[info](info/)           | Get basic information on context and environment
[create](create/)       | Define a new app by loading a json file
[status](status/)       | Show current status of an app or service
[start](start/)         | Start an application or service
stop                    | Stop an application or service
delete                  | Delete an app. Note that you lose all contained data by doing so.
update                  | Update a component by changing the docker image to a newer version
[scaleup](scaleup/)     | Increase number of instances running a component
[scaledown](scaledown/) | Reduce number of instances running a component
[logs](logs/)           | Print an app's standard output and error messages
[stats](stats/)         | Print basic statistics of an instance
version                 | Print swarm client version
ls                      | List all apps
[env](env/)             | Handle environments
cat                     | Show the configuration of an application
login                   | Log in to your account
logout                  | Log out from your account
[user](user/)           | Create and modify users
[company](companies/)   | Manage companies
completion              | Setup CLI completion
