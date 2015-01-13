description: This guide shows you how you can create periodic backups of your MySQL database with a very simple, additional service running in your application.

# MySQL with Backups

<p class="lead">In this guide we show you how a specialized service running inside your Giant Swarm application can be used to create periodic backups of your MySQL database</p>

<p class="lastmod">Last edited on January 13, 2014 by Marian Steinbach</p>

Setting up a MySQL database on Giant Swarm is simple. The Docker Hub provides a [standard image](https://registry.hub.docker.com/u/library/mysql/) in various flavors. But what happens as soon as your applications creates actual data? Servers can break any time. Data can be lost. So you need backups.

In this guide we show you how you can add a service to your Giant Swarm application that accomplishes one thing only: Create a database dump and store it to Amazon S3. This way you don't have to touch your existing services. Each function has it's place. Truly microservice-istic. ;-)

This guide proposes Amazon S3 as a means to store backups, because it's well-known. And it has the advantage that it is possble to create user accounts with very specific permission. You might adapt this guide to use different cloud storage services or your own (S)FTP server. If you write this up, let us know. We're happy to learn.

<i class="fa fa-exclamation-triangle"></i> Note that being able to create periodic backups should not drive you to use Giant Swarm in production. We are still in Alpha. Things can and will break, all the time.

## Before you start

To follow this guide, you will need the following:

* The `docker` command line utility. [Get Installation instructions here.](https://docs.docker.com/installation/)
* A dedicated AWS user account with credentials (see below for a quick guide)
* S3 bucket with the correct permissions for the user
* Giant Swarm user account
* Network connection

## Quick guide to AWS setup

If you read this, chances are you already have an Amazon AWS account. If not, got to http://aws.amazon.com/ and create an account now.

* Create a user group
* Create an S3 bucket
* Create a policy with write permission for this group and bucket
* Create a user
* Store the credentials, as you will need them in a moment
* Add the user to the group

## Running MySQL docker container locally

The first thing we need locally is a MySQL database container to test against. Probably the application you are working on already has a MySQL docker image set up. If not, it is very easy to run one using a standard MySQL docker image.

Here is an example command:

```
$ docker run -d -p 3306:3306 \
    -e MYSQL_DATABASE=mydb \
    -e MYSQL_ROOT_PASSWORD=some-password \
    mysql:5.5
```

With the command above, you start MySQL in the background with one database called `mydb`. The password for the MySQL user `root` is set to `some-password`. You can change this to whatever you want.

To create a Docker image for your MySQL archiver service, use this simple `Dockerfile`:

```dockerfile
FROM python:2.7
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -y -q
RUN apt-get install -y mysql-client-5.5
RUN pip install awscli
WORKDIR /
ADD backup.sh /backup.sh
RUN chmod u+x /backup.sh
CMD /backup.sh
```

The image we build with this `Dockerfile` will be based on the official `python` image version 2.7 so we have all the required dependencies in place for installing and running Python programs. So the AWS command line interface (`awscli`), which is written in Python, can be easily installed using `pip install awscli`.

In addition, the `mysql-client-5.5` Debian package is installed, which provides the `mysqldump` command line utility we need to create our SQL dumps.

Last but not least, we add a shell script called `backup.sh` to our image, which is executed by default when the container is started. Let's have a look.

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

# pattern to create subdirectories from dateelements,
# e. g. '%Y/%m/%d' or '%Y/%Y-%m-%d'
pathpattern=$PATH_DATEPATTERN

# initially wait a minute before first backup
#sleep 60
sleep 1

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
    aws s3 cp $filename.gz s3://$bucket/$datepath/$filename.gz
    rm $filename.gz
    
    echo "Writing backup No. $count finished."
    
    # increment counter and for the time to pass by...
    count=`expr $count + 1`
    sleep $interval
done
```

The script provides a generic way to

* Dump a mysql database to an SQL file
* Compress the SQL file using GZip
* Upload the compressed file to some S3 bucket

All configuration is provided via environment variables, which means that the image we create with this script contained can be used for various databases.

But first, let's build the Docker image for our MySQL archiver. It takes not more than this:

```
docker build -t mysql-archiver .
```

Here is a way to run locally for testing purposes and set all the required environment variables for the backup job:

```
docker run --rm -ti \
  -e "S3_BUCKET=your-bucket-name/your-path-to-mysql-backups/" \
  -e "AWS_ACCESS_KEY_ID=your-aws-access-key-id" \
  -e "AWS_SECRET_ACCESS_KEY=your-aws-secret-access-key" \
  -e "AWS_DEFAULT_REGION=eu-central-1" \
  -e "MYSQL_PORT_3306_TCP_ADDR=192.168.59.103" \
  -e "MYSQL_PORT_3306_TCP_PORT=3306" \
  -e "BACKUP_INTERVAL=3600" \
  -e "DB_NAME=mydb" \
  -e "DB_USER=root" \
  -e "DB_PASSWORD=some-password" \
  -e "PATH_DATEPATTERN=%Y/%m" \
  mysql-archiver
```

Let's have a closer look at what these environment variables are doing.

* `S3_BUCKET`: Name of the bucket you want to put backups in. May include additional path elements. Do not prepend `s3://`!
* `AWS_ACCESS_KEY_ID`: The access key ID of the AWS account you configured to write to your target bucket.
* `AWS_SECRET_ACCESS_KEY`: The secret access key of the AWS account you configured to write to your target bucket.
* `AWS_DEFAULT_REGION` (*optional*): This will be needed in some cases to indicate the location of the S3 bucket. We needed them when testing with buckets created in the Frankfurt location (`eu-central-1`). Might not be required with some other locations.
* `MYSQL_PORT_3306_TCP_ADDR`: IP address of the MySQL server. With the MySQL server running on your local docker host, this is your docker IP address.
* `MYSQL_PORT_3306_TCP_PORT`: TCP port the MySQL server is listening on, probably `3306`.
* `BACKUP_INTERVAL`: Number of seconds to wait between backups. 3600 is one hour.
* `DB_NAME`: Name of the database you want to backup.
* `DB_USER`: Database user to use for the backup.
* `DB_PASSWORD`: Password for the database user to be used.
* `PATH_DATEPATTERN`: To store you backup in a nice folder hierarchy with folders named after the current date, define a date pattern. Unix `date` format placeholders like `%Y` (year), `%m` (month) and `%d` (day) can be used. For example, `%Y/%m` creates one folder per year with one sub folder per month. Note that the backup file itself is also datestamped.

Except for `AWS_DEFAULT_REGION`, all these variables are in fact required.

Now, adapt the `docker run` command above to match your requirements and give it a try. Hint: Set a low `BACKUP_INTERVAL`, for example `10` seconds, when testing.

You should see a log output like this:

```
Writing backup No. 1 for 192.168.59.103:3306/mysql to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-48.sql.gz
-- Warning: Skipping the data of table mysql.event. Specify the --events option explicitly.
upload: ./2015-01-13_17-48.sql.gz to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-48.sql.gz
Writing backup No. 1 finished.
Writing backup No. 2 for 192.168.59.103:3306/mysql to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-49.sql.gz
-- Warning: Skipping the data of table mysql.event. Specify the --events option explicitly.
upload: ./2015-01-13_17-49.sql.gz to s3://my-bucket/backup/mysql/2015/01/2015-01-13_17-49.sql.gz
Writing backup No. 2 finished.
```

When you get this kind of output, congratulations! You have just written database backups to Amazon S3.

You can then stop the process using `Ctrl + C`.

## Giant Swarm Application setup

After your Docker image is proven locally, let's make it ready for use in the cloud. On Giant Swarm, that is.

### Uploading to a Docker registry

If you stick close to our example, there should be nothing personal in the `mysql-archiver` Docker image. So actually you can even use the public Docker registry to deploy this image, if you want to.

Depending on what registry you are pushing to, you have to tag your docker image before.

Let's assume you have the Docker registry account `rocker` and plan to use the Docker Hub you could tag the image like this:

```
$ docker tag mysql-archiver docker.
```

Set up your Giant Swarm application to contain the MySQL-Archiver as a service. To have something to backup, you will of course need a MySQL component in some other service.

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
          "ports": ["3306"],
          "env": {
            "MYSQL_ROOT_PASSWORD": "somepassword",
            "MYSQL_DATABASE": "mydb"
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
      "service_name": "db-archiver",
      "components": [
        {
          "component_name": "mysql-archiver",
          "image": "registry.giantswarm.io/<username>/mysql-archiver:latest",
          "env": {
            "BACKUP_INTERVAL": "3600",
            "DB_NAME": "mydb",
            "DB_USER": "root",
            "DB_PASSWORD": "somepassword"
          },
          "dependencies": [
            {
              "name": "db/mysql",
              "port": 3306,
              "alias": "mysql"
            }
          ],
          "ports": ["3000"]
        }
      ]
    }
  ]
}
```

TODO

## Further reading

TODO
