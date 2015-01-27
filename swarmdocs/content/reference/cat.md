+++
title = "Getting an application's configuration"
description = "This is the reference page for the 'swarm cat' command, which allows you to fetch the effective configuration of an application."
date = "2014-12-24"
type = "page"
categories = ["Reference", "Swarm CLI Commands"]
tags = ["swarm cat"]
weight = 100
+++

# Getting an application's configuration

The `swarm cat` command allows you to inspect the current effective configuration JSON of an application. This can serve various purposes:

* Quick inspection of a running application. It might have been somone else in your company who has created the application, or some time passed since you created the application and need a quick reminder how it's set up.

* Debugging of variable replacement. Say you have used variables in your `swarm.json` file and want to make sure these have been replaced with the right values, a call to `swarm cat` can help you find out if everything works as expected.

* Reconstruction of a lost configuration file. In case you lost your local version of the application confoguration, this is an easy way to reconstruct the file.

The syntax is simple:

    $ swarm cat [app_name]

The `app_name` argument is optional when there is a proper `swarm.json` file in your current directory, containing the required `app_name` key.

## Further reading

* [Creating an application](../create/)
* [Application configuration (`swarm.json`)](../swarm-json/)
