+++
title = "Swarmify Ruby on Rails"
description = "This guide shows you how to create, deploy, and run a simple Ruby on Rails project on Giant Swarm"
date = "2015-01-13"
type = "page"
weight = 80
categories = ["advanced"]
+++

# Swarmify Ruby on Rails

The following guide will explain how to configure the [RailsTutorials Sample App](https://github.com/railstutorial/sample_app_rails_4/) to GiantSwarm. We will run one container for MySQL and one for your Rails application. You should have a basic understanding of Docker and Rails.

## TL;DR with fig

Before we get into the details, let us first run the setup locally with [fig](http://www.fig.sh/). For this, we clone our repository, switch to the [dockerize branch](https://github.com/giantswarm/sample_app_rails_4/tree/dockerize) and start the setup with `fig up`:

    $ git clone https://github.com/giantswarm/sample_app_rails_4
    $ cd sample_app_rails_4/
    $ git checkout dockerize
    $ fig up

That's it. Two containers are up, linked, and running. You can now access your app on [port 3000](http://localhost:3000/) of your localhost.

## Get up and running with Docker on localhost

Now let's see what needs to get done to manually dockerize the Sample Rails app. 

    $ git clone https://github.com/railstutorial/sample_app_rails_4
    $ cd sample_app_rails_4/

The team behind [Docker-Library](https://registry.hub.docker.com/_/rails/) ([GitHub repository](https://github.com/docker-library/rails)) already provides a base image for Ruby on Rails. We are using the "onbuild" version, which makes it easy to write our own Dockerfile. At the root of the sample rails app, create a new file called `Dockerfile` with the following statement: 

```
FROM rails:onbuild
```

Before you can build the Rails app we need to fix the `Gemfile` and set the Ruby version to `2.1.2`:

```
source 'https://rubygems.org'
ruby '2.1.2'
#ruby-gemset=railstutorial_rails_4_0

gem 'rails', '4.0.8'
gem 'bootstrap-sass', '2.3.2.0'
....
```

Upon `docker build -t sample_rails_4 .` our patched Rails Gemfile is added and the dependencies are installed. Then the Rails sample app is added and Node.JS is installed. See the [Rails Dockerfile](
https://github.com/docker-library/rails/blob/7bb6ade7f97129cc58967d7d0ae17f4b62ae52eb/onbuild/Dockerfile) for details.

If you now run your container with `docker run -p 3000:3000 sample_rails_4` you should get a runtime error message informing you that no database is configured. So let's do that now.

## Adding MySQL

As a database we chose MySQL, which should run in its own container. Fortunatly we can use the predefined [MySQL docker image](https://registry.hub.docker.com/_/mysql/), which automatically creates a `root` user. It also supports reading the initial password from the `MYSQL_ROOT_PASSWORD` environment variable. So to start our database we run this:

```bash
$ PASS=somesecretpassword
$ docker run -d --name database -e MYSQL_ROOT_PASSWORD=${PASS} -p 3306 mysql
```

To hook our Rails app to the database we are using [Docker links](https://docs.docker.com/userguide/dockerlinks/). When linking containers, Docker injects certain environment variables, which can be used to discover the IP and port of the linked container. We need to modify our Rails app to use these variables for connecting to the database:

```yaml
# File config/database.yml - only the production environment is shown
production:
  adapter: mysql2
  pool: 5
  timeout: 5000

  database: app
  username: <%=ENV['MYSQL_USER'] %>
  password: <%=ENV['MYSQL_PASS'] %>
  host: <%=ENV['DATABASE_PORT_3306_TCP_ADDR'] %>
  port: <%=ENV['DATABASE_PORT_3306_TCP_PORT'] %>
```

Since we now use the `mysql2` driver, we also need to add it to our Gemfile for the `production` group (you can also drop `pg` if you want):

```ruby
# File Gemfile
+  gem 'mysql2'
```

Since we have changed the Gemfile, we would normally need to build our application image again. But before we do that, let's fix the next problem. If we start our app and it connects to the database, it encounters two problems:

1. There is no database `app` in the MySQL container
2. Without a database, all the tables are missing, too - we need to execute `rake db:migrate`

We can fix this by writing a custom start script which ensures both points are fixed:

```bash
#!/bin/bash

set -e

cd /usr/src/app

MYSQL_HOST=$DATABASE_PORT_3306_TCP_ADDR
MYSQL_PORT=$DATABASE_PORT_3306_TCP_PORT

MYSQL="mysql -h$MYSQL_HOST -P$MYSQL_PORT -u$MYSQL_USER -p$MYSQL_PASS"

if [ ! $($MYSQL -e 'show databases;'| grep ^app$) ]; then
  $MYSQL -e "create database app;"
fi

rake db:migrate

exec rails s $*
```

To get this running we need to install a MySQL client and register our start script in our `Dockerfile`:

```
FROM rails:onbuild

RUN apt-get update && apt-get install -y mysql-client
RUN chmod +x start

CMD ["./start"]
```

__NOTE__: We realize that this is a non-optimal solution for now, so this will likely change in the future.

One last step: As as we currently do not yet support SSL, we need to disable it for the production environment:

```
# File config/environments/production.rb
-  config.force_ssl = true
+  config.force_ssl = false 
```

Calling `docker build -t sample_rails_4 .` to build the new image, we can now run everything on the local Docker daemon:

```bash
PASS=somesecretpassword
SECRET_KEY=somesecretkeyforrails

# Start the MySQL database
docker run -d --name database -e MYSQL_ROOT_PASSWORD=${PASS} -p 3306 mysql

# Now the Rails app - linked to MySQL
docker run -e RAILS_ENV=production -e SECRET_KEY_BASE=${SECRET_KEY} \
	-e MYSQL_PASS=${PASS} -e MYSQL_USER=root --link database:database \
	-p 3000:3000 sample_rails_4
```

You can now access your app on [port 3000](http://localhost:3000) of localhost again.

## Swarmifying

Now lets port all this to Giant Swarm.

Since Giant Swarm has no access to the images on your host, we also need to publish it. As the docker hub images must all be prefixed with your username we need to rebuild it:

```
$ docker build -t <username>/sample_rails_4 .
$ docker push <username>/sample_rails_4
```

### The swarm.json

Now, we just need to add an application file describing our containers:

```json
{
  "app_name": "rails-sample-1",
  "services": [{
    "service_name": "web",
    "components": [{
      "component_name": "database",
      "image": "mysql",
      "ports": [3306],
      "env": {
        "MYSQL_ROOT_PASSWORD": "somesecretpassword"
      }
    },
    {
      "component_name": "rails",
      "image": "<username>/sample_rails_4",
      "env": {
        "SECRET_KEY_BASE": "somesecretkeyforrails",
        "RAILS_ENV": "production",
        "MYSQL_PASS": "somesecretpassword",
        "MYSQL_USER": "root"
      },
      "dependencies": [
        {"name": "database", "port": 3306}
      ],
      "ports": [3000],
      "domains": {
        "rails-example.gigantic.io": 3000
      }
    }]
  }]
}
```

Here, we define one app `rails-sample-1` with one service `web`. This service comprises two components: `database` and `rails`. We configure each through environment variables. The ports define the accessible interface which can be accessed by two ways:

1. With a `dependency` to access it from another container
2. By adding a `domains` definition, so our load balancer can forward public requests to your container.

You can either use your own domains (which you have to configure to forward to us) or use a subdomain of the cluster you are using. In this example we are using `gigantic.io` - modify this to match your needs.

### Run 

Thats it. With the `swarm` command line tool we can now create and start our containers on the Giant Swarm cluster:

```
$ swarm create
$ swarm start rails-sample-1
$ swarm status rails-sample-1
```

Now open your browser and head to [rails-example.gigantic.io](http://rails-example.gigantic.io)
