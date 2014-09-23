# Swarmify Ruby on Rails

The following guide will explain how to configure the [RailsTutorials Sample App](https://github.com/railstutorial/sample_app_rails_4/) to GiantSwarm. In the end we will run one container for Mysql and one container for your Rails application. You should have a basic understanding of Docker and Rails.

    $ git clone https://github.com/railstutorial/sample_app_rails_4.git
    $ cd sample_app_rails_4/

You can also find all changes we do in this guide in the following PR: [here](https://git.giantswarm.io/giantswarm/rails-example/merge_requests/1).

## Running rails with docker on localhost

The [Docker-Library Team](https://registry.hub.docker.com/_/rails/) ([Github](https://github.com/docker-library/rails)) already provides a base image for Ruby on Rails, so is easy to run your app with Docker: only a simple `Dockerfile` needs to be written:

```
FROM rails:onbuild
```

Upon `docker build -t sample_rails_4 .` this image adds your current working directory to the container. 
=> No!

If you now run run your build you can access it on the public port for the container port 3000.
=> No

## Adding mysql

Next we want to run this app with a mysql database both running in docker containers. As a database we can use the [mysql](https://registry.hub.docker.com/_/mysql/) image, which automatically creates an `admin` user with a random password on startup. It also supports reading the initial password from the `MYSQL_ROOT_PASSWORD` environment variable. So to start our database, we run this:

```bash
$ PASS=somesecretpassword
$ docker run -d --name database -e MYSQL_ROOT_PASSWORD=${PASS} -p 3306 mysql
```

When linking containers, docker injects certain environment variables which can be used to discover the IP and port of the linked container. We now need to modify our rails sample app to use these variables for connecting to the database:

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

Since we now use the mysql2 driver, we also need it to our Gemfile for the `production` group (you can also drop `pg` if you want):

```ruby
# File Gemfile
+  gem 'mysql2'
```

If we now start our containers, our app connects to the database, but encounters two problems:

1. There is no database `app` in the mysql container
2. Without a database, all the tables are missing too - we need to execute `rake db:migrate`

We can fix this by writing a custom start script which ensures both points are created:

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

We also need to register this in our `Dockerfile`:

```
FROM rails

RUN apt-get install -y mysql-client
ADD ./start /start

CMD ["/start"]
```

__NOTE__: We realize this is a non-optimal solution for now, so this will change in the future.

Calling `docker build -t rails_sample_4 .` to build the new image, we can now run everything on the local docker daemon:

```bash
PASS=somesecretpassword
SECRET_KEY=somesecretkeyforrails

# Start the mysql database
docker run -d --name database -e MYSQL_ROOT_PASSWORD=${PASS} -p 3306 mysql

# Now the rails app - linked to the mysql
docker run -d -e RAILS_ENV=production -e SECRET_KEY_BASE=${SECRET_KEY} \
	MYSQL_PASS=${PASS} -e MYSQL_USER=admin --link database:database \
	-p 8000:3000 sample_rails_4
```

You can now access your app on [port 8000](http://localhost:8000).

## Swarmifying

Now, lets port all this to GiantSwarm!

First, as we currently do not yet support SSL, we need to disable it for the production environment:

```
# File config/environments/production.rb
-  config.force_ssl = true
+  config.force_ssl = false 
```

Since Giantswarm has no access to the images on your host, we also need to publish it. As the docker hub images must all be prefixed with your username (and we changed a file), we need to rebuild it:

```
$ docker build -t username/sample_rails_4 .
$ docker push username/sample_rails_4
```

If you don't want to share your application publicly with the rest of the world, you can also use our private registry soon.


### The swarm.json

We also need an application file describing our containers:

```json
# File swarm.json
{
  "app_name": "rails-sample-1",
  "services": [{
    "service_name": "web",
    "components": [{
      "component_name": "database",
      "image": "mysql",
      "ports": ["3306"],
      "env": [
        "MYSQL_ROOT_PASSWORD=foobar"
      ]
    },
    {
      "component_name": "rails",
      "image": "zeisss/example-rails",
      "env": [
        "SECRET_KEY_BASE=somemagicsecrethashkeyblablablabla",
        "RAILS_ENV=production",
        "MYSQL_PASS=foobar",
        "MYSQL_USER=admin"
      ],
      "dependencies": [
        {"name": "database", "port": 3306}
      ],
      "ports": ["3000"],
      "domains": {
        "rails-example.cluster-02.giantswarm.io": "3000"
      }
    }]
  }]
}
```

Here, we define one app `rails-sample-1` with one service `web`. This service is build from two components: `database` and `rails`. We configure each through environment variables. The ports define the accessible interface which can be accessed by two ways:

1. With a `dependency` to access it from another container
2. By adding `domains` definition, so our LoadBalancer can forward public requests to your container.

You can either use your own domains (which you have to configure to forward to us) or use a subdomain of the cluster you are using. In the example we are using `cluster-02.giantswarm.io` - modify this to match your needs.

### Run 

Thats it. With the `swarm` command line tool we can now create and start our containers on the GiantSwarm cluster:

```
$ swarm create swarm.json
$ swarm start rails-sample-1
$ swarm status rails-sample-1
```

Now open your browser and head to [rails-example.cluster-02.giantswarm.io](http://rails-example.cluster-02.giantswarm.io)