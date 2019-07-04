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
from a single place; the control plane.

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
running on your control plane and tenant clusters. These operators watch various
Custom Resources, some created by us, and others created by you, which make up
the desired state of the Giant Swarm App Catalog.

For example, the "App" Custom Resource indicates that you want an App installed
on a specific tenant cluster.

SNIPPET SHOWING A APP CR

Below you can see a high level overview of the components and resources that work
together to enable the features of the Giant Swarm App Catalog:

SOME KIND OF USEFUL IMAGE SHOWING OPERATORS AND CRS AND SUCH.

### What are Managed Apps?

Managed Apps are provided by Giant Swarm and have an SLA associated with
them. When you install one of our Managed Apps, we make sure that it stays
running and even get paged if something goes wrong.

Managed Apps can be found in the Managed _App Catalog_, indicated by the
orange "Managed" badge.

MORE DETAILS ON THE SLA AND EXPECTATION MANAGEMENT

###

### How can I interact with the App Catalog?

Currently only through our web interface. See [this reference page] for more
details on how to install and configure apps using our web interface.

Support for the App Catalog is coming to our CLI (gsctl) next.

Lastly, at the end of the day, the App Catalog is configured through a set of
Custom Resources installed on your Control Plane.

Our intention is to eventually grant you full access to the control plane
API, and all of these resources, so that you can interact with them using
`kubectl` (think `kubectl create app`), and automate them just as you have been automating other parts of your
stack.


