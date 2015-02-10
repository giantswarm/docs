+++
title = "MySQL with Backups"
description = "This guide shows you how you can create periodic backups of your MySQL database with a very simple, additional service running in your application."
date = "2015-02-10"
type = "page"
weight = 200
categories = ["advanced"]
+++

# MySQL with Backups

<p class="lead">In this guide we show you how a specialized service running inside your Giant Swarm application can be used to create periodic backups of your MySQL database</p>

Setting up a MySQL database on Giant Swarm is simple. The Docker Hub provides a [standard image](https://registry.hub.docker.com/u/library/mysql/) in various flavors. But what happens as soon as your applications creates actual data? Servers can break any time, data can be lost. So you need a backup system.

In this guide we show you how you can add a service to your Giant Swarm application that accomplishes one thing only: Create a database dump and store it to Amazon S3. This way you don't have to touch your existing services. Each function has it's place. Truly microservistic. :-) However, be aware that this is only one possible solution and might not be ideal for you.

This guide proposes Amazon S3 as a means to store backups, because it's well-known. And it has the advantage that it is possble to create user accounts with very specific permission. You might adapt this guide to use different cloud storage services or your own (S)FTP server. If you write this up, let us know. We're happy to learn.

## Prerequisites

To follow this guide, you will need the following:

* The `swarm` and `docker` utilities and some basic knowledge on how to use them. If you followed our [Your first application](/guides/your-first-application/) tutorial, you'll be fine.
* An S3 bucket and a dedicated AWS user account with permission to upload files into the bucket
* The source code used in this guide from [GitHub](https://github.com/giantswarm/giantswarm-mysql-archiver). We recommend to quickly clone it:

```nohighlight
$ git clone git@github.com:giantswarm/giantswarm-mysql-archiver.git
$ cd giantswarm-mysql-archiver
```

A hint for the impatient: There is a `Makefile` in that repository which allows you to call most commands described in this tutorial in a reproducible way.

## AWS S3 setup overview

Setting up everything on AWS involves a few steps which are outlined here. We don't go into all the details, since there should be plenty of tutorials for that elsewhere.

Not that we explicitly recommend to create a dedicated AWS identity exclusively for this backup service. This way you can easily revoke permissions in the case that the according credentials get in the wrong hands. And you can easily restrict the S3 permissions to uploading into a specific bucket.

Here is our recipe for your permission setup:

1. Create an AWS user group
2. Create an S3 bucket
3. Create a policy with write permission for this group and bucket
4. Add the policy to the bucket
5. Create a user
6. Store the credentials for this user, as you will need them in a moment
7. Add the user to the group

Here is the [AWS documentation on identities and bucket policies](http://docs.aws.amazon.com/AmazonS3/latest/dev/using-iam-policies.html). Also very helpful: The [AWS Policy Generator](http://awspolicygen.s3.amazonaws.com/policygen.html).

## A local MySQL database for testing

Before deploying things to Giant Swarm, we want to test our Backup service locally. So we need a MySQL database to backup.

If you don't already have a database available for that purpose, the easiest thing you can do is run one using a standard MySQL docker image.

Here is an example command:

```nohighlight
$ docker run -d --name=mysql \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_ROOT_PASSWORD=some-password \
    mysql:5.5
```

With the command above, you start MySQL in the background with one database called `mydb`. The password for the MySQL user `root` is set to `some-password`. You can change this to whatever you want.

## Building our archiver Docker image

Docker containers are the building blocks of applications on Giant Swarm. We will now build the image for our archiver container.

The image is based on this Dockerfile:

```Dockerfile
FROM debian:wheezy

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -y -q && \
  apt-get install -y mysql-client-5.5 python2.7 python-pip && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

RUN pip install awscli

ADD backup.sh /backup.sh
RUN chmod 0755 /backup.sh

CMD /backup.sh
```

What does it do? The image we build with this Dockerfile will be based on an official Debian image. We install the packages `python2.7` and `python-pip` so we can install and run the AWS command line interface (`awscli`), which is written in Python.

In addition, the `mysql-client-5.5` Debian package is installed, which provides the `mysqldump` command line utility we need to create our SQL dumps.

Last but not least, we add a shell script called `backup.sh` to our image, which is executed by default when the container is started. Let's have a look at that script.

```bash
#!/bin/bash

# interval between backups in seconds
interval=$BACKUP_INTERVAL

# MySQL configuration
dbhost=$MYSQL_PORT_3306_TCP_ADDR
dbport=$MYSQL_PORT_3306_TCP_PORT
dbname=$DB_NAME
dbuser=$DB_USER
dbpass=$DB_PASSWORD

# Amazon S3 target bucket
bucket=$S3_BUCKET

# pattern to create subdirectories from date elements,
# e. g. '%Y/%m/%d' or '%Y/%Y-%m-%d'
pathpattern=$PATH_DATEPATTERN

count=1

while [ 1 ]
do
    # set date-dependent path element
    datepath=`date +"$pathpattern"`
    
    # determine file name
    datetime=`date +"%Y-%m-%d_%H-%M"`
    filename=$dbname_$datetime.sql
    
    echo "Writing backup No. $count for $dbhost:$dbport/$dbname to s3://$bucket/$datepath/$filename.gz"
    
    mysqldump -h $dbhost -P $dbport -u $dbuser --password="$dbpass" $dbname > $filename

    gzip $filename
    aws s3 cp $filename.gz s3://$bucket/$datepath/$filename.gz && echo "Backup No. $count finished"
    rm $filename.gz
    
    # increment counter and for the time to pass by...
    count=`expr $count + 1`
    sleep $interval
done
```

The script provides a generic way to

* Dump a mysql database to an SQL file
* Compress the SQL file using GZip
* Upload the compressed file to some S3 bucket

All configuration is provided via environment variables, which means that the Docker image we create can be used for various databases.

Let's build the Docker image now. Be sure to replace `yourusername` with your actual Giant Swarm username in this command:

```nohighlight
$ docker build -t registry.giantswarm.io/yourusername/mysql-archiver ./
```

When this is done, we can run a container from this image locally to test if things work as they should. As said, all configuration for the `backup.sh` is taken from environment variables, so we have to pass them all to the container. Here is how we do it locally:

```nohighlight
docker run --rm -ti \
  -e "S3_BUCKET=your-bucket-name/your-path-to-mysql-backups/" \
  -e "AWS_ACCESS_KEY_ID=your-aws-access-key-id" \
  -e "AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key" \
  -e "AWS_DEFAULT_REGION=eu-central-1" \
  -e "BACKUP_INTERVAL=3600" \
  -e "DB_NAME=mydb" \
  -e "DB_USER=root" \
  -e "DB_PASSWORD=some-password" \
  -e "PATH_DATEPATTERN=%Y/%m" \
  --link mysql:mysql \
  registry.giantswarm.io/yourusername/mysql-archiver
```

What these environment variables mean:

* `S3_BUCKET`: Name of the bucket you want to put backups in. May include additional path elements. Do not prepend `s3://`!
* `AWS_ACCESS_KEY_ID`: The access key ID of the AWS account you configured to write to your target bucket.
* `AWS_SECRET_ACCESS_KEY`: The secret access key of the AWS account you configured to write to your target bucket.
* `AWS_DEFAULT_REGION` (*optional*): This will be needed in some cases to indicate the location of the S3 bucket. We needed them when testing with buckets created in the Frankfurt location (`eu-central-1`). Might not be required with some other locations.
* `BACKUP_INTERVAL`: Number of seconds to wait between backups. 3600 is one hour.
* `DB_NAME`: Name of the database you want to backup.
* `DB_USER`: Database user to use for the backup.
* `DB_PASSWORD`: Password for the database user to be used.
* `PATH_DATEPATTERN`: To store you backup in a nice folder hierarchy with folders named after the current date, define a date pattern. Unix `date` format placeholders like `%Y` (year), `%m` (month) and `%d` (day) can be used. For example, `%Y/%m` creates one folder per year with one sub folder per month. Note that the backup file itself is also datestamped.

Except for `AWS_DEFAULT_REGION`, all these variables are in fact required.

If you have looked at the `backup.sh` script really closely, you may have noticed that uses two variables which we do not pass here: `MYSQL_PORT_3306_TCP_ADDR` and `MYSQL_PORT_3306_TCP_PORT`. These are automatically set by "container links", which are enabled by naming the MySQL container `mysql` and refering to that name in the `--link` flag when running the `mysql-archiver` container.

Now, adapt the `docker run` command above to match your requirements and give it a try. Hint: Set a low `BACKUP_INTERVAL`, for example `10` seconds, when testing so you don't have to wait too long for a second and third backup to be made.

Execute the adapted `docker run` command. You should see a log output like this:

```nohighlight
Writing backup No. 1 for 192.168.59.103:3306/mysql to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-48.sql.gz
upload: ./2015-01-13_17-48.sql.gz to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-48.sql.gz
Writing backup No. 1 finished.
Writing backup No. 2 for 192.168.59.103:3306/mysql to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-49.sql.gz
upload: ./2015-01-13_17-49.sql.gz to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-49.sql.gz
Writing backup No. 2 finished.
```

When you get this kind of output, congratulations! You have just written database backups to Amazon S3.

You can stop the process using `Ctrl + C`.

## Bringing it to Giant Swarm

After your Docker image is proven locally, let's make it ready for use in the cloud. On Giant Swarm, that is.

### Uploading to the registry

To run your Docker image on Giant Swarm you have to upload it to a Docker registry. Giant Swarm already provides you with a private registry. Your Giant Swarm account is also used to access this registry. So let's use this one.

First, make sure you are logged in with the `docker` command line tool and our registry. Use your Giant Swarm username and the according password when prompted.

```nohighlight
$ docker login https://registry.giantswarm.io
```

Now push your image to the registry.

```nohighlight
$ docker push registry.giantswarm.io/yourusername/mysql-archiver
```

### Configuring your application

You might already have an application with a MySQL component ready. If not, you can easily create one from the example `swarm.json` below. Keep in mind that the example won't do anything meaningful. It only contains an empty database to be backed up.

With an existing application, add a new service with a single component for your MySQL archiver. You can use the `mysql-archiver` service in the example below as a template.

```json
{
  "app_name": "your-app",
  "services": [
    {
      "service_name": "db",
      "components": [
        {
          "component_name": "mysql",
          "image": "mysql:5.5",
          "ports": [3306],
          "env": {
            "MYSQL_ROOT_PASSWORD": "$mysqlpass",
            "MYSQL_DATABASE": "$mysqldb"
          },
          "volumes": [
            {
              "path": "/var/lib/mysql",
              "size": "2 GB"
            }
          ]
        }
      ]
    },
    {
      "service_name": "archiver",
      "components": [
        {
          "component_name": "mysql-archiver",
          "image": "registry.giantswarm.io/yourusername/mysql-archiver:latest",
          "env": {
            "DB_NAME": "$mysqldb",
            "DB_USER": "root",
            "DB_PASSWORD": "$mysqlpass",
            "S3_BUCKET": "your-bucket-name/your-path-to-mysql-backups/",
            "AWS_ACCESS_KEY_ID": "your-aws-access-key-id",
            "AWS_SECRET_ACCESS_KEY": "your-aws-secret-access-key",
            "AWS_DEFAULT_REGION": "eu-central-1",
            "BACKUP_INTERVAL": "3600",
            "PATH_DATEPATTERN": "%Y/%m"
          },
          "dependencies": [
            {
              "name": "db/mysql",
              "port": 3306,
              "alias": "mysql"
            }
          ],
          "ports": [3000]
        }
      ]
    }
  ]
}
```

The example shows how the Docker image you created, tested locally and pushed to the registry is now used as a component inside a service definition. The `service_name` and `component_name` values are only examples, you can chose your own here. The `image` key needs as a value the complete image name you used when pushing your Docker image to the registry.

The `env` key of the component definition gets the familiar environment variable definitions that are needed for the backup script working in the container.

Worth a special note: We use two variables in the configuration file, `$mysqldb` and `$mysqlpass` which you can detect by the `$` prefix. These help you to prevent repeating yourself in the config and also save you from setting a password in a file which you might want to upload into a versionb control system. We show you how to replace these variables in a minute.

Pay special attention to the `dependencies` definition. The `archiver` component is made to depend on the `db/mysql` component, aliased as `mysql`, with exposed port 3306. As a result, the environment variables named `MYSQL_PORT_3306_TCP_ADDR` and `MYSQL_PORT_3306_TCP_PORT`, which we already talked about above, are declared when the component is started.

### Starting your application

If you already had the application created on Giant Swarm and you now modified it to contain the archiver component, you will have to delete this app using `swarm delete <application>`. Note that this results in the __loss of all data__ in your containers and volumes of that application (That's why we do all this in the first place, isn't it?).

If you just created the application configuration for a new application (or you deleted the old one), you can now create and start it on Giant Swarm in one step:


```nohighlight
$ swarm up --var=mysqldb=mydb --var=mysqlpass=rootpasswd
```

This will create the application and start its services. When the application is launched, you can inspect the logs of the archiver component to find out if everything works as expected. Use the `swarm status your-app` command to list all components first. Your output should look similar to this:

```nohighlight
App your-app is up

service   component       instanceid                            created              status
db        mysql           715a3b72-7ab2-4294-8337-bfe4b3758bc1  2015-01-13 18:02:37  up
archiver  mysql-archiver  f8ce5429-74da-4445-acfe-1b84a600c81d  2015-01-13 18:02:37  up

```

Using the instance ID of the `archiver` component, you can now access the logs:

```nohighlight
$ swarm logs f8ce5429-74da-4445-acfe-1b84a600c81d
```

If everything works fine, they look pretty similar to what you saw when running the container locally.

## Running the archiver service on demand

With the archiver running in it's own service, you can stop and start it independently of the database service. To stop it when running, use `swarm stop your-app/archiver`. To start again, use `swarm start your-app/archiver`.

This way you could also use the archiver service as a backup on demand tool. Just start it when you want to create a backup and stop it manually when that backup is finished (checking the logs or looking for the file to appear on S3).

## Further reading

* [Using the registry](../../reference/registry/) - to find out more about using our Docker registry.
* [mysqldump reference](http://dev.mysql.com/doc/refman/5.5/en/mysqldump.html) - to learn about other ways to call `mysqldump` and how this would affect your backup

