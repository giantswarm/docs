+++
title = "The Giant Swarm App Catalog"
description = "Overview of the Giant Swarm App Catalog, how it works and what to expect."
date = "2019-02-11"
weight = 15
type = "page"
categories = ["basics"]
+++

# The Giant Swarm App Catalog

The _Giant Swarm App Catalog_ refers to a set of features and concepts that allow
you to browse, install and manage the configurations of apps (such as prometheus)
from a single place; the Control Plane.

Through this we are also providing you a list of curated _Managed Apps_.
In the near future you might also see _Apps_ provided by our partners.

These collections of _Apps_ are grouped in _App Catalogs_, which in turn are
browseable through our web interface.

So to clarify a bit: the _Giant Swarm App Catalog_ refers to the whole feature,
and an _App Catalog_ is a collection of _Apps_.

We'll provide some _App Catalogs_, but so will our partners, and you too can set
up your own internal catalog(s) for your whole company to use.

### What makes up the Giant Swarm App Catalog?

Technically the Giant Swarm App Catalog is implemented as a set of operators
running on your Control Plane and tenant clusters. These operators watch various
Custom Resources, some created by us, and others created by you, which make up
the desired state of the Giant Swarm App Catalog.

For example, the "App" Custom Resource indicates that you want an App installed
on a specific tenant cluster.

SNIPPET SHOWING A APP CR

Below you can see a high level overview of the components and resources that work
together to enable the features of the Giant Swarm App Catalog:

SOME KIND OF USEFUL IMAGE SHOWING OPERATORS AND CRS AND SUCH.

### What kind of App Catalogs are there?

By default you will have the Incubator and the Community App Catalogs installed
on your Control Planes.

Some customers might also already have access to the Managed App Catalog, which
contains our selection of Managed Apps.

### The Incubator App Catalog

### The Community App Catalog

### The Managed App Catalog and Managed Apps

Managed Apps are provided by Giant Swarm and have a SLA associated with
them. When you install one of our Managed Apps, we make sure that it stays
running and even get paged if something goes wrong.

Managed Apps can be found in the Managed _App Catalog_. In our web interface
they are indicated by the orange "Managed" badge.

MORE DETAILS ON THE SLA AND EXPECTATION MANAGEMENT

### Installing your own App Catalog

It's possible to install your own App Catalog. This is useful if you want to make
a set of Apps available to your company.

- Explain that an App Catalog is a repo on Github
- Explain some of the automation
- Installing an App Catalog means creating an App Catalog CR

Links to more detailed docs on custom App Catalog creation.

### How can I interact with the Giant Swarm App Catalog?

You can interact with the Giant Swarm App Catalog through our API and
our web interface.

See [this reference page] for more details on how to install and configure apps
using our web interface.

See [link to API docs] for details on API calls related to the Giant Swarm App
Catalog.

Support for the App Catalog is coming to our CLI (gsctl) next.

Lastly, at the end of the day, what our interfaces do, is create (or update)
a set of Custom Resources on your Control Plane.

Our intention is to eventually grant you full access to the Control Plane
API, and all of these resources, so that you can interact with them using
`kubectl`, and automate them just as you have been automating other parts of your
stack.


