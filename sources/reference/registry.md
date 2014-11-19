# Using the registry

<p class="lastmod">Last edited on November 13, 2014 by Marian Steinbach</p>

## TL;DR

Login to the Giant Swarm registry:
```
$ docker login https://registry.giantswarm.io
```

Build your image with the right name:
```
$ docker build -t registry.giantswarm.io/acmecorp/exampleimage:1.4.2 .
```

Upload the image to the registry:
```
$ docker push registry.giantswarm.io/acmecorp/exampleimage:1.4.2
```

Reference the image in your app config:
```
{
    "component_name": "upstream",
    "image": "registry.giantswarm.io/acmecorp/exampleimage:1.4.2",
    ...
}
```

## Intro

Giant Swarm provides you a protected registry to deposit and deploy your [Docker](https://docker.com/) images. Here we give you the information you need to login and push images to our registry and use these images within your applications.

The registry uses software provided by Docker and is accessed via standard Docker tools. If you are familiar with the concept of registries and know how to deal with images there, you can easily transfer that knowledge to our protected registry. In this case, please make sure that you read and understand how we use company names as namespaces, as explained in the section [_company namespaces_](#company-namespaces) below.

In addition to using the Giant Swarm registry, you have the option to use any publicly accessible Docker registry, including the [Docker Hub](https://registry.hub.docker.com/) with lots of readily available Open Source software packages.

## URL and image name format

The URL of our registry is `https://registry.giantswarm.io`.

The full image name format is

    registry.giantswarm.io/<company_namespace>/<image_name>:<tag>

Note that the URL scheme (`https://`) is ommited here.

Example of a full image name:

    registry.giantswarm.io/acmecorp/webserver:1.4.2

## Company namespaces

In our systems, users are associated with [companies](../companies/) to allow for shared resources between multiple users. Docker images are an example of these shared resources.

> Every image you push to the registry has to belong to a certain company. This is expressed by using the company name as the image's namespace.

If, for example, you belong to the company called `acmecorp` and want to create an image, which can be used by all users of that company, the name `acmecorp` has to be used as the name space field within the image name, like here:

    registry.giantswarm.io/acmecorp/exampleimage:1.4.2

We will be using the company name `acmecorp` throughout this page as a placeholder for your respective company name.

## Logging in

Before you can do anything like uploading or downloading images to/from our registry, you first have to log in. Have your Giant Swarm user name and password ready for that purpose. The actual login is performed interactively using the `docker login` command:

    $ docker login https://registry.giantswarm.io

You will be prompted to input your username, then your password, and finally your email address.

As a side note, you can currently enter any email address here. We don't use this piece of information, however the `docker login` command prompts for it, which we cannot influence.

Once you have successfully logged in, you can proceed to the next section.

## Naming and tagging an image

Before uploading ("pushing") a Docker image to any registry, it has to be given the name it will finally have within the registry.

You have several choices on when to name the image with its final name:

* During build time, using the `docker build` command with the `-t` or `--tag` flag
* After building, using the `docker tag` command

Naming the image _during build time_ saves you an extra step but also requires you to plan ahead. When in the directory containg the `Dockerfile` for your `exampleimage` image, any of the following commands would create a named image:

    docker build -t registry.giantswarm.io/acmecorp/exampleimage .
    docker build -t registry.giantswarm.io/acmecorp/exampleimage:latest .
    docker build -t registry.giantswarm.io/acmecorp/exampleimage:1.4.2 .

As for naming _after the build_: If, for example, you have locally created a little image with the simple name `exampleimage`, there are several alternatives how you can give it a name that is valid for the registry:

    docker tag exampleimage registry.giantswarm.io/acmecorp/exampleimage
    docker tag exampleimage registry.giantswarm.io/acmecorp/exampleimage:latest
    docker tag exampleimage registry.giantswarm.io/acmecorp/exampleimage:1.4.2

You might have wondered what the `:latest` or `:1.4.2` suffixes are about. They are called _tags_ and are distinct indicators for different variants of an image. They are frequently used for versioning images.

## Pushing an image

To make use of your images within your Giant Swarm applications, you have to upload or "push" them to our registry. This is done using the `docker push` command.

Above, you learnt that you have to name an image with the appropriate name _before_ pushing it. Now you can use the full image name to push that same image. This is the general command syntax:

    $ docker push registry.giantswarm.io/<company_namespace>/<image_name>:<tag>

There are cases where the `:<tag>` part would be optional. Going into depth here would make this reference a lot longer. For now, we simply recommend to explicitly name the tag. If you like, you can read more about this topic in the Docker documentation (link given [below](#further-reading)). 

So to push our example image to the registry, the command we would use might be:

    $ docker push registry.giantswarm.io/acmecorp/exampleimage:1.4.2

<!-- TODO: show progress output -->

After issuing the push command, you will see some progress information until all layers of your image are completely pushed to the registry.

Once you create newer versions of your images and push them again, you will likely notice the great benefit of the layered nature of docker images: Unchanged layers won't have to be uploaded again, only modified or new layers are transferred over the network.

## Referencing your image in an app

Once an image is pushed to our registry, you can use it in your (or your company's) applications. For general information on this topic, have a look at the [swarm.json reference page](../swarm-json/).

Your application is potentially built of several components with one `"image"` definition each. This is where we expect the full name of your image in our registry.

```json
{
    "component_name": "upstream",
    "image": "registry.giantswarm.io/acmecorp/exampleimage:1.4.2",
    ...
}
```

We _explicitly recommend_ to use the full name including a specific tag here. Do not use the `:latest` alias here, otherwise it will be up the registry endpoint to resolve this to the actual image version.

Be aware that you can use variables in your `swarm.json` file, which can be defined either in another JSON file or as command line parameters. Read more about this on the reference page for [creating apps](../create/).

## Further reading

* [swarm.json reference page](../swarm-json/)
* [Creating an app](../create/)

External resources:

* [Introduction to Docker Images](https://docs.docker.com/terms/image/)
* [Working with Docker Images](https://docs.docker.com/userguide/dockerimages/)
