+++
title = "The Giant Swarm App Catalog in The Web Interface"
description = "What the Giant Swarm App Catalog looks like on our Web Interface and how to use it."
date = "2019-07-05"
layout = "subsection"
weight = 10
+++

# The Giant Swarm App Catalog in the Web Interface

This page will give you an overview of how to do some common tasks related to the
Giant Swarm App Catalog using our Web Interface.

Go here for an [overview of the Giant Swarm App Catalog](/basics/app-catalog/) instead.

### Viewing all App Catalogs

Our web interface lets you browse the App Catalogs installed on your Control Plane.
Click on "App Catalogs" in the navigation menu. The "App Catalogs" link will only
be visible if your Control Plane has at least one App Catalog installed on it.

The screenshot below shows what the "App Catalogs" page looks like with two app catalogs
installed:

![A screenshot of our web interface, showing a list of available app catalogs](../app-catalogs.png)

### Installing an App

Click on the catalog you'd like to install from. Only apps in the Managed catalog
will be monitored and managed by us.

![A screenshot of our web interface, showing a list of apps in an app catalog](../apps.png)

Once you know what app you'd like to install, click on that app, and then on
"Configure & Install"

![A screenshot of our web interface, showing the detail page for a specific app, in this case grafana](../app-detail-page.png)

That'll bring up a modal where you can choose what cluster you want to install
the app on, the version you want install, as well as some further steps allowing you to configure the app.

![A screenshot of the configuration screen when install an app using our web interface](../app-configuration-modal.png#width-60)

Configuration consists of two optional YAML files, one with plaintext values and the other with
base64 encoded secrets.

Configuration values exist at three levels: `catalog`, `app`, and `user`, but the
web interface only allows you to upload configuration files for the final (`user`) configuration level.

The values are merged with values from previous configuration levels and override them
when they contain the same key.

See our [app configuration reference page](/reference/app-configuration) for more details and examples on how this works.