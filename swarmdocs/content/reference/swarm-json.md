+++
title = "Application configuration (swarm.json)"
description = "This is the reference page for the application configuration file, usually called 'swarm.json'."
date = "2015-02-10"
type = "page"
weight = 40
+++

# Application configuration (`swarm.json`)

Giant Swarm applications are defined using a JSON configuration file format. The configuration file is ususlly called `swarm.json`.

This page explains in detail which configuration directives are available and how they work.

## Basic structure

The basic structure of the configuration file is:

* Definition of exactly one application
* Definition of one or multiple services
* Within each service, one or multiple components

## Minimal example

The following example illustrates the basic structure by defining an application called `simple_app`. This application consists of only one service named `service_one`, which contains only one component `component_one`.

```json
{
  "app_name": "simple_app",
  "services": [
    {
      "service_name": "service_one",
      "components": [
        {
          "component_name": "component_one",
          "image": "ubuntu",
          "args": [
            "/usr/bin/some_process"
          ]
        }
      ]
    }
  ]
}
```

## Complete example

This example makes use of all possible keys to illustrate their use.

```json
{
  "app_name": "less_simple_app",
  "services": [
    {
      "service_name": "service_one",
      "components": [
        {
          "component_name": "appserver",
          "image": "registry.giantswarm.io/mycorp/mycomponent:latest",
          "args": [
            "/usr/bin/some_process"
          ],
          "volumes": [
            {
              "path": "/var/data",
              "size": "10 GB"
            }
          ],
          "ports": [ 8080 ],
          "env": {
            "MODE": "development"
          },
          "dependencies": [
            {
              "name": "redis",
              "port": 6379
            }
          ],
          "scaling_policy": {
            "min": 3,
            "max" : 10
          },
          "domains": {
            "myexample.gigantic.io": 8080
          }
        },
        {
          "component_name": "redis",
          "image": "dockerfile/redis",
          "ports": [ 6379 ]
        }
      ]
    }
  ]
}
```

## Application level keys

On the application level, both the `app_name` and the `services` keys are required.

### `app_name`

The name of the application. You can refer to this name when controlling the application, for example when starting or stopping the application.

The application name has to be unique within the [environment](../env/) you're deploying it to. An attempt to create an application with the same name twice within one environment will result in an error message.

### `services`

This key is used to hold the array of service definitions.

## Service level keys

On this level, both the `service_name` and the `components` keys are required.

### `service_name`

The name of the service.

### `components`

The list of components contained in this service.

## Component level keys

On this level, the keys `component_name` and `image` are required.

### `component_name`

The name of the component.

### `image`

The name of a docker image. This can be a name like `ubuntu` or `redis` when using "standard" images from the public Docker registry. In order to address images from the Giant Swarm registry, a fully qualified image name in the form `registry.giantswarm.io/<company_namespace>/<image_name>[:<tag>]` is required.

Find out more on the [registry reference page](../registry/).

### `args`

The `args` key is optional and, if present, expects as value an array of strings. These strings will be passed as arguments when your container is started, just like the arguments you can pass to `docker run`. The effect of these arguments depends on how the container is set up. Please refer to the [Dockerfile documentation](https://docs.docker.com/reference/builder/), especially on the `CMD` and `ENTRYPOINT` directives.

As already shown in our [minimal example](#minimal-example) above, when using a simple Linux image, the `args` key can be used to define which process is to be called.

    "image": "ubuntu",
    "args": ["/usr/bin/some_process"]

With this setup, further argument array entries could be used to pass arguments to the call of a binary. Example:

    "image": "ubuntu",
    "args": ["ps", "aux"]

This provides for some convenience, since it potentially allows you to use container images in a flexible way for more than a single purpose. So it might save you from building and pushing multiple almost identical images.

### `dependencies`

Array of dependency objects, which are used to define dependencies between components. Defining a dependency object within _component A_ pointing to _component B_ indicates that _component A_ requires _component B_ to be running. Dependencies can refer to components within the same service or within different services.

Besides making sure that the components are started in the appropriate order, dependencies also enable network communication between components (called "container linking" in the Docker terminology).

The keys of a dependency object are as follows:

* `name`: Either the name of a required component within the same service or, if the required component is defined in a different service, the service name and component name in the format `<service_name>/<component_name>`. This key is required. A string is expected as value.
* `port`: An exposed port of the required component. This key is required. An integer or string is expected as a value.
* `alias`: An optional alias name to be used instead of the actual component name when automatically generating environment variables for host and port of the required component. Read on for more information on that.

Let's review the dependencies key in our full-fledged example above, specifically in the `appserver` component:

```json
"dependencies": [
  {
    "name": "redis",
    "port": 6379
  }
]
```

The name `redis` points to the `component_name` of the component in the same service. This dependency enforces the `redis` component to be started before the `appserver component`. 

In addition, this dependency definition results in a network link between the `appserver` component and port 6379 of the `redis` component being set up. To make use of this link, the `appserver` component needs to know the IP address of the running `redis` component. This information will be made available automatically in an environment variable called

    REDIS_PORT_6379_TCP_ADDR

from two required keys from our example dependency definition above. The variable name schema, which you might have guessed by now, is:

    <NAME_or_ALIAS>_PORT_<PORT>_ADDR

In addition to that environment variable, an entry in `/etc/hosts` is generated with the name of the required component and it's ip address. Example:

    redis 123.123.123.123

Be aware that this example variable and host name is directly derived The `alias` key (mentioned above), if used, takes precedence over the `name` when it comes to variable generation. So if there is an `alias`, it defines how the environment variable for linking will be called.

Suppose we would change the dependency configuration above to this instead:

```json
"dependencies": [
  {
    "name": "redis",
    "port": 6379,
    "alias": "db"
  }
]
```

As a result, our component would now provide an environment variable with the name `DB_PORT_6379_TCP_ADDR`. The according `/etc/hosts` would now be named `db`.

As a third and last example, imagine we had an additional service in our application configuration called `payment` with a component called `restapi` and port 8000 exposed. To make our current component depend on that component, the dependency configuration would have to look like this:

```json
"dependencies": [
  {
    "name": "payment/restapi",
    "port": 8000
  }
]
```

As a result, our current component would provide the environment variable `RESTAPI_PORT_800_TCP_ADDR` and an `/etc/hosts` entry `restapi`. As you can see, while contained in the `name` key, the service name (`payment`) is not used in the environment variable name nor in the `/etc/hosts` entry. In order to make these names more explicit, you could of course set an alias as explained above.

### `domains`

The `domains` key allows you to make components of your application available via HTTP under one or several domain names.

The example below makes the given component's exposed port 8080 available under TCP port 80 (the HTTP default port) using the domain name `myexample.gigantic.io`:

```json
"domains": {
  "myexample.gigantic.io": 8080
}
```

The `domains` key can be used in any number of components. In a real life scenario, this means that a web application could have one component acting as a public entry point. A different component could serve as an admin interface, using a different `domains` key.

When deciding on what domain name to use, you have two general options available:

* Use a subdomain of the `gigantic.io` domain
* Use your own domain name

Both options are explained in detail below.

__Using the gigantic.io domain for your app__

This option is the easiest, especially for applications in their early stage.

If you want to make your application available as `my-super-app.gigantic.io`, fine. Simply enter that string as a key in the `domains` setting and make it point to the correct port. There is nothing else you have to take care of. (You might want to test before if that subdomain is already in use by someone.)

<i class="fa fa-exclamation-triangle"></i> As of now we do not yet have checks in place to ensure a `gigantic.io` subdomain is used only by one application. This could theoretically result in another user's application grabbing a name you want for yourself. This is clearly to be solved and we will come up with a solution rather sooner than later.

__Using your own domain name__

If you plan to use your own domain name in your configuration, there is one configuration step to take care of on your side: please set up a CNAME entry for the desired subdomain pointing to `loadbalancer.giantswarm.io`. This can usually be done wherever the DNS settings for that domain are administered.

### `env`

Environment variables definitions. These variables will be available within the running docker containers. Entries _must_ be of type string. Example:

```json
"env": {
  "FIRST_VARIABLE": "foo",
  "SECOND_VARIABLE": "bar",
  "NUMERIC_VARIABLE": "123"
}
```

### `ports`

This key expects as value an array of one or more port numbers to be exposed for this component. If, for example, a component should expose TCP port 80, the according value would be:

    "ports": [80]

### `scaling_policy`

This key can hold an object which defines the number of minimum and maximum instances of this component to be allowed.

If this is ommitted, exactly one instance of the according component is started during application startup.

The Object given with this key can have two optional keys:

* `min`: The minimum number of instances to run for this component
* `max`: The maximum number of instances to run for this component

Note that there currently is a hard [limit](https://giantswarm.io/limits/) of 10 instances per component.

### `volumes`

When you stop an application component, all data written to the file system in the docker container representing this component is lost. With volumes you can preserve your data to survive stops and starts. The volumes you define will be created when the application is created and will be deleted upon application deletion.

The `volumes` key expects an array of simple objects as value, one object for each volume you want to define. Each of these objects must have the following keys:

* `path`: The path in which the volume will be mounted, as a string
* `size`: A string defining the volume size in gigabytes in a format like `<n> GB`.

<i class="fa fa-exclamation-triangle"></i> Please note that we currently do not provide a backup mechanism. If you need to preserve the data on your volumes, please think about a solution using for example an FTP server or cloud storage like Amazon S3 from within your component.

## Making use of configuration variables

Imagine you would like to run an almost identical application in two different [environments](../env/), say each one with only a different version of an image.

To prevent you from having to copy your entire configuration file and make those tiny changes, our application configuration supports the use of variables.

The use of variables is explained in more detail in the documentation of the [`swarm create`](../create/) command.

## Further reading

* More application configuration examples can be found in our [Guides](../)
* [Creating an application](../create/)
* [Handling environments](../env/)

<!--
see
https://git.giantswarm.io/giantswarm/cli/blob/master/dist/examples/api_0.sample.json
https://git.giantswarm.io/giantswarm/user-config/blob/master/user_config.go
-->
