description: This guide shows you how to create, deploy, and run a simple PHP/Symfony project on Giant Swarm

# Swarmify PHP and Symfony

<p class="lastmod">Last edited on November 30, 2014 by Matthias Lübken</p>

This page should get you started with PHP, Symfony, and the Swarm. 

__Overview__:

* Swarmify PHP
* Dockerizing Symfony
* Swarmify Symfony

## Swarmify PHP

Getting PHP running on Giant Swarm is rather easy. Use the [official PHP Docker image](https://registry.hub.docker.com/_/php/), build your own image from it, upload and start it.

Start with a simple `Dockerfile`:

```
# from https://registry.hub.docker.com/_/php/	
FROM php:5.6-apache
COPY . /var/www/html
```

If you look at [php:5.6-apache's Dockerfile](https://github.com/docker-library/php/blob/e19f15271b1cbe9d3e5c9f0c552beca9579f0677/5.6/apache/Dockerfile), you will see that port 80 is exposed and the default command to run is `httpd`.

Next, add a simple `index.php` for testing pruposes:
	
	<? echo "<p>Hello from PHP</p>"; ?>

Now build, test, and upload the image:
	
	$ docker build -t registry.giantswarm.io/giantswarm/hellophp .
	$ docker run -d -p 8080:80 registry.giantswarm.io/giantswarm/hellophp
	$ curl localhost:8080
	$ docker push registry.giantswarm.io/giantswarm/hellophp
 
This image can then be referred to in the new `swarm.json` file:

```json
{
  "app_name": "hellophp",
  "services": [
    {
      "service_name": "hellophp-service",
      "components": [
        {
          "component_name": "hellophp-component",
          "image": "registry.giantswarm.io/giantswarm/hellophp",
          "ports": [ "80/tcp" ],
          "domains": { "hellophp.gigantic.io": "80" }
        }
      ]
    }
  ]
}
``

## Swarmify Symfony

Getting Symfony running in Docker and on the Swarm only requires a couple of steps. To get a head start you can just clone our repo and use [fig](http://www.fig.sh/) to get everything up and running.

```
$ git clone git@github.com:giantswarm/symfony-standard.git
$ cd symfony-standard
$ git checkout dockerize
$ fig up
```

	TODO explain the steps

## Run a Symfony app on the Swarm
	
	TODO



