description: This guide shows how to dockerize a simple Ruby on Rails application and deploy it on Giant Swarm.

# Swarmify Ruby on Rails

<p class="lastmod">Last edited on January 25, 2015 by Marian Steinbach</p>

The following guide will explain how to configure the [RailsTutorials Sample App](https://github.com/railstutorial/sample_app_rails_4/) to GiantSwarm. We will run one container for MySQL and one for your Rails application. You should have a basic understanding of Docker and Rails.

## Prerequisites

In order to follow along this guide you need the following installed and setup on your machine:

* Docker
* Latest `swarm` app
* Ruby 2.2
* Bundler
* MySQL development headers

You can checkout the [dockerize branch](https://github.com/giantswarm/sample_app_rails_4/tree/dockerize) from our fork of the sample app to see the result of the changes.

## Get up and running with Docker on localhost

The get started clone the sample app from GitHub and create a branch to work on:

```shell
$ git clone https://github.com/railstutorial/sample_app_rails_4
$ cd sample_app_rails_4/
$ git checkout -b dockerize
```

First of all we need to create a `Dockerfile`. We could use the [official Rails Docker image](https://registry.hub.docker.com/_/rails/) but we need the `onbuild` image. Using this will make us dependent on their Ruby version updates. Updating the language should be managed by us and not but a third-party. We can still use the [Ruby base image](https://registry.hub.docker.com/_/ruby/) to build our own `Dockerfile`:

```Dockerfile
FROM ruby:2.2.0

RUN apt-get update && apt-get install -y nodejs --no-install-recommends && rm -rf /var/lib/apt/lists/*
RUN apt-get update && apt-get install -y mysql-client --no-install-recommends && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY Gemfile /usr/src/app/
COPY Gemfile.lock /usr/src/app/
RUN bundle install --deployment

COPY . /usr/src/app

EXPOSE 3000

CMD ["rails", "server"]
```

Another advantage of rolling our own `Dockerfile` is we will only install the used database dependency and not all of them. Instead of the global `--freeze` flag for Bundler we will use the `--deployment` flag.

Before we can build our Docker image we need to make sure the `Gemfile.lock` is up to date:

```shell
$ bundle install
```

This step is required every time we change the dependencies in the `Gemfile`. After we done this we can finally build our Docker image:

```shell
$ docker build -t sample_rails_4
```

To start the container we need to specify two essential options: the port we want to be exposed and which Rails environment to be used:

```shell
$ docker run -e RAILS_ENV=production -p 3000:3000 sample_rails_4
```

**NOTE:** The `RAILS_ENV=production` part is important since we're preparing the image to be used in production. Setting this up for local development requires additional steps that will not be covered in this guide.

This will run the sample application in production mode and make it available at <http://localhost:3000>. As soon as you go to the page you will get an error. A look into the log output shows we don't have a database configured yet. Let's do this next.

## Adding MySQL

As a database we chose MySQL, which should run in its own container. Fortunatly we can use the predefined [MySQL docker image](https://registry.hub.docker.com/_/mysql/), which automatically creates a `root` user. It also supports reading the initial password from the `MYSQL_ROOT_PASSWORD` environment variable. So to start our database we run this:

```bash
$ docker run -d --name database -e MYSQL_ROOT_PASSWORD=somesecretpassword -p 3306 mysql
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

The original sample application uses Postgres as database. To use MySQL we need to replace the `pg` gem with the `mysql2` gem in our `Gemfile`:

```ruby
# File Gemfile
-  gem 'pg'
+  gem 'mysql2'
```

Don't forget to run `bundle install` after this change.

While this will allow us to connect to the MySQL database there is not much we can do on it yet. We need to address two issues:

1. There is no database `app` in the MySQL container
2. After creating the database we need to create _and_ maintain the schema in it.

Rails provides Rake tasks for both issues but we still need to execute them at some point. Because we're planning to deploy the app to Giant Swarm we must execute both tasks within a Docker container. There no best practise on how to solve these problems yet, but one way is a custom start script:

```bash
#!/bin/bash

set -e

cd /usr/src/app

rake db:create
rake db:migrate

exec rails s $*
```

Put this file under `script/docker_start` and mark it as executable:

```shell
$ chmod +x script/docker_start
```

To use our custom script instead of the simple `rails server` we must change our `Dockerfile`. Replace the `CMD` with the following:

```Dockerfile
CMD ["./script/docker_start"]
```

**NOTE:** We realize that this is a non-optimal solution for now, so this will likely change in the future.

One last step: As as we currently do not yet support SSL, we need to disable it for the production environment:

```
# File config/environments/production.rb
-  config.force_ssl = true
+  config.force_ssl = false 
```

Now we can build the new image:

```shell
$ docker build -t sample_rails_4
```

At this point we can run both the web app and the database together:

```shell
# Start the MySQL database
$ docker run -d --name database -e MYSQL_ROOT_PASSWORD=somesecretpassword -p 3306 mysql

# Now the Rails app - linked to MySQL
$ docker run -e RAILS_ENV=production -e SECRET_KEY_BASE=somesecretkeyforrails \
  -e MYSQL_PASS=somesecretpassword -e MYSQL_USER=root --link database:database \
  -p 3000:3000 sample_rails_4
```

Visiting the app again on <htt://localhost:3000> should not raise any more errors.

## Swarmifying

Now lets port all this to Giant Swarm.

Since Giant Swarm has no access to the images on your host, we also need to publish it. As the docker hub images must all be prefixed with your username we need to rebuild it:

```
$ docker build -t <username>/sample_rails_4 .
$ docker push <username>/sample_rails_4
```

### The `swarm.json`

Now, we just need to add an application file describing our containers:

```json
{
  "app_name": "rails-sample-1",
  "services": [
    {
      "service_name": "web",
      "components": [
        {
          "component_name": "database",
          "image": "mysql",
          "ports": ["3306"],
          "env": {
            "MYSQL_ROOT_PASSWORD": "$mysqlpass"
          },
          "volumes": [
            {
              "path": "/var/lib/mysql",
              "size": "1 GB"
            } 
          ]
        },
        {
          "component_name": "rails",
          "image": "<username>/sample_rails_4",
          "env": {
            "SECRET_KEY_BASE": "$railssecretkey",
            "RAILS_ENV": "production",
            "MYSQL_PASS": "$mysqlpass",
            "MYSQL_USER": "$mysqluser"
          },
          "dependencies": [
            {
              "name": "database",
              "port": 3306
            }
          ],
          "ports": ["3000"],
          "domains": {
            "rails-example.gigantic.io": "3000"
          }
        }
      ]
    }
  ]
}
```

Here, we define one app `rails-sample-1` with one service `web`. This service comprises two components: `database` and `rails`. We configure each through environment variables. The ports define the accessible interface which can be accessed by two ways:

1. With a `dependency` to access it from another container
2. By adding a `domains` definition, so our load balancer can forward public requests to your container.

You can either use your own domains (which you have to configure to forward to us) or use a subdomain of the cluster you are using. In this example we are using `gigantic.io` - modify this to match your needs.

The last step to make this work is to add the actual environment variables. Since we don't want to write them directly into the `swarm.json` we extract them into the `swarmvars.json`:

```json
{
    "GIANT_SWARM_USER/ENV": {
        "mysqlpass": "somesecretpassword",
        "mysqluser": "root",
        "railssecretkey": "somesecretkeyforrails"
    }
}
```

### Run 

That's it. With the `swarm` command line tool we can now create and start our containers on the Giant Swarm cluster:

```
$ swarm create
$ swarm start rails-sample-1
$ swarm status rails-sample-1
```

Now open your browser and head to [rails-example.gigantic.io](http://rails-example.gigantic.io)

## Further reading

* In our blog: [Getting Started with Microservices using Ruby on Rails and Docker](http://blog.giantswarm.io/getting-started-with-microservices-using-ruby-on-rails-and-docker)
