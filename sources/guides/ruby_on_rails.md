# Swarmify Ruby on Rails

The following guide will explain how to configure the [RailsTutorials Sample App](https://github.com/railstutorial/sample_app_rails_4/) to GiantSwarm. In the end we will run one container for Mysql and one container for your Rails application. You should have a basic understanding of Docker and Rails.

The whole diff to the original repository can be found [here](https://git.giantswarm.io/giantswarm/rails-example/merge_requests/1).

## Running rails with docker on localhost

The [Docker-Library Team](https://registry.hub.docker.com/_/rails/) ([Github](https://github.com/docker-library/rails)) already provides a base image for Ruby on Rails, so is easy to run your app with Docker: only a simple `Dockerfile` needs to be written:

```
FROM rails
```

Upon `docker build -t sample_rails_4 .` this image adds your current working directory to the container. If you now run run your build you can access it on the public port for the container port 3000.

## Adding mysql

Next we want to run this app with a mysql database both running in docker containers. As a database we can use the `tutum/mysql` image, which automatically creates an `admin` user with a random password on startup. It also supports reading the initial password from the `MYSQL_PASS` environment variable. So to start our database, we run this:

```bash
PASS=somesecretpassword
docker run -d --name database -e MYSQL_PASS=${PASS} -p 3306 tutum/mysql
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

Since we now use the mysql2 driver, we also need it to our Gemfile for the `production` group:

```ruby
# File Gemfile
+  gem 'mysql2'
```

If we would know start our containers we would have two problems:
1) There is no database `app` in the mysql container
2) Without a database, all the tables are missing too - we need to execute `rake db:migrate`

For now we fix this by writing a custom start script which ensures both points are created:

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

Calling `docker build -t rails_sample_4 .` to build the new image, we can now run everything on the local docker daemon:

```bash
PASS=somesecretpassword
SECRET_KEY=somesecretkeyforrails

# Start the mysql database
docker run -d --name database -e MYSQL_PASS=${PASS} -p 3306 tutum/mysql

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

We also need an application describing our containers:

```json
# File swarm.json
{
  "app_name": "rails-sample-1",
  "services": [{
    "service_name": "web",
    "components": [{
      "component_name": "database",
      "image": "tutum/mysql",
      "ports": ["3306"],
      "env": [
        "MYSQL_PASS=foobar"
      ]
    },
    {
      "component_name": "rails",
      "image": "registry.private.giantswarm.io/zeisss/example-rails",
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

TODO: explain the domain part

As you can see, we are using the image `zeisss/example-rails` for the app. You can replace this with your own `username/imagename` from the docker hub, after you have uploaded it:

```
docker tag sample_rails_4 username/sample_rails_4
docker push username/sample_rails_4
```

Thats it. With the `swarm` command line tool we can now create and start our containers on the GiantSwarm cluster:

```
$ swarm create swarm.json
$ swarm start rails-sample-1
$ swarm status rails-sample-1
```