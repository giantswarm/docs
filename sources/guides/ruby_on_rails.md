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

```
PASS=somesecretpassword
docker run -d --name database -e MYSQL_PASS=${PASS} -p 3306 tutum/mysql
```

When linking containers, docker injects certain environment variables which can be used to discover the IP and port of the linked container. We now need to modify our rails samle app to use these variables for connecting to the database:

```
# File config/database.yml

```

1) Configure app to use env db
2) create app database in mysql
3) run db:migrate rake task

To runs everything on your local docker daemon:

```
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


