# Swarmify PHP and Symfony

This page should get you started with PHP, Symfony and the Swarm. 

*TOC:*

* Swarmify PHP
* Dockerizing Symfony
* Swarmify Symfony

## Swarmify PHP 
To get PHP running in the Swarm is rather easy. Use the [official PHP image](https://registry.hub.docker.com/_/php/) build your own image from it, upload it and start it.

#### Start with a simple `Dockerfile`:

	# from https://registry.hub.docker.com/_/php/	
	FROM php:5.6-apache
	COPY . /var/www/html

See the [php:5.6-apache Dockerfile](https://github.com/docker-library/php/blob/e19f15271b1cbe9d3e5c9f0c552beca9579f0677/5.6/apache/Dockerfile) for details like exported ports and default commands.


#### Add a simple `hello.php`:
	
	<? echo "<p>Hello from PHP</p>"; ?>

#### Build, test and upload the image:
	
	$ docker build -t luebken/hellophp .
	$ docker run -d luebken/hellophp
	$ curl localhost:8000
	$ docker push luebken/hellophp
 
#### Refer to that image in the `swarm.json`:

	{
	    "app_name": "hellophp",
	    "services": [
	        {
	            "service_name": "hellophp-service",
	            "components": [
	                {
	                    "component_name": "hellophp-component",
	                    "image": "luebken/hellophp",
	                    "domains": { "hellophp.cluster-02.giantswarm.io": "80" }
	                }
	            ]
	        }
	    ]
	}

#### Create, start test and upload the image:
	
	$ docker build -t luebken/hellophp .
	$ docker run -d luebken/hellophp .
	$ curl localhost:8000

## Dockerizing Symfony

	TODO

## Run a Symfony app on the Swarm
	
	TODO



