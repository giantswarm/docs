# Swarmify Ruby on Rails

The following guide will explain how to configure the [RailsTutorials Sample App](https://github.com/railstutorial/sample_app_rails_4/) to GiantSwarm. In the end we will run one container for Mysql and one container for your Rails application. You should have a basic understanding of Docker and Rails.

    $ git clone https://github.com/railstutorial/sample_app_rails_4.git
    $ cd sample_app_rails_4/

You can also find all changes we do in this guide in a [dockerize branch](https://github.com/giantswarm/sample_app_rails_4/tree/dockerize).

## Running rails with docker on localhost

The [Docker-Library Team](https://registry.hub.docker.com/_/rails/) ([Github](https://github.com/docker-library/rails)) already provides a base image for Ruby on Rails. We are using the onbuild version which makes it easy to write our own `Dockerfile`. At the root of the sample rails app create a new file called `Dockerfile` with the following statement: 

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

Upon `docker build -t sample_rails_4 .` our patched Rails Gemfile is added and the dependencies are installed. Then the Rails app is added and NodeJS is installed. See the [Rails Dockerfile](
https://github.com/docker-library/rails/blob/7bb6ade7f97129cc58967d7d0ae17f4b62ae52eb/onbuild/Dockerfile) for details.

If you now run your container with `docker run -p 3000:3000 sample_rails_4` you can access the rails app on port 3000. But hold on we need to configure our databse.

## Adding mysql

Next we want to run this app with a mysql database in it's own container. As a database we can use the [mysql](https://registry.hub.docker.com/_/mysql/) image, which automatically creates an `admin` user with a random password on startup. It also supports reading the initial password from the `MYSQL_ROOT_PASSWORD` environment variable. So to start our database, we run this:

```bash
$ PASS=somesecretpassword
$ docker run -d --name database -e MYSQL_ROOT_PASSWORD=${PASS} -p 3306 mysql
```

To hook our Rails app to the database we are using [Docker links](https://docs.docker.com/userguide/dockerlinks/). When linking containers Docker injects certain environment variables which can be used to discover the IP and port of the linked container. We need to modify our Rails app to use these variables for connecting to the database:

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

Since we have changed the Gemfile we would need to build our application image again. But before we do that lets fix the last little problem.

If start our app and it connects to the database it encounters two problems:

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

To get this running we need to install an mysql client and register our start script in our `Dockerfile`:

```
FROM rails:onbuild

RUN apt-get update && apt-get install -y mysql-client
RUN chmod +x start

CMD ["./start"]
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
	-e MYSQL_PASS=${PASS} -e MYSQL_USER=admin --link database:database \
	-p 3000:3000 sample_rails_4
```

You can now access your app on [port 3000](http://localhost:3000).

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