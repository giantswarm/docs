# Swarmify Java and JavaSpark

<p class="lastmod">Last edited on December 9, 2014 by Matthias Lübken</p>

There are tons of Java web stacks. For our first example we chose [Spark](http://www.sparkjava.com/) a tiny Sinatra inspired framework in Java 8.

For the simplest helloworld see [https://github.com/giantswarm/sparkexample](https://github.com/giantswarm/sparkexample)

## Dockerfile
A simple Dockerfile using the official Java image, installing maven, compiling and packaging via maven and starting it:
```
FROM dockerfile/java:oracle-java8 

RUN apt-get update
RUN apt-get install -y maven

ADD . /code
WORKDIR /code
RUN ["mvn", "clean", "install"]

EXPOSE 4567
CMD ["java", "-jar", "target/sparkexample-jar-with-dependencies.jar"]
```

## Hello.java

This file resides in `src/main/java/sparkexample/Hello.java`. It's a simple SparkJava class returning a string:

```
package sparkexample;

import static spark.Spark.get;

public class Hello {

    public static void main(String[] args) {
        get("/", (req, res) -> {
            return "hello from sparkjava.com";
        });
    }
}
```

## pom.xml
Java project dependencies and build steps defined in a maven configuration:
```

<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>sparkle</groupId>
    <artifactId>sparkle</artifactId>
    <version>1.0-SNAPSHOT</version>


    <dependencies>
        <dependency>
            <groupId>com.sparkjava</groupId>
            <artifactId>spark-core</artifactId>
            <version>2.0.0</version>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-jar-plugin</artifactId>
                <version>2.4</version>
                <configuration>
                    <finalName>sparkexample</finalName>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>sparkexample.Hello</mainClass>
                            <classpathPrefix>dependency-jars/</classpathPrefix>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-assembly-plugin</artifactId>
                <executions>
                    <execution>
                        <goals>
                            <goal>attached</goal>
                        </goals>
                        <phase>package</phase>
                        <configuration>
                            <finalName>sparkexample</finalName>
                            <descriptorRefs>
                                <descriptorRef>jar-with-dependencies</descriptorRef>
                            </descriptorRefs>
                            <archive>
                                <manifest>
                                    <mainClass>sparkexample.Hello</mainClass>
                                </manifest>
                            </archive>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>
</project>

```

## swarm.json
A simple `swarm.json` using a custom image `giantswarm/sparkexample` and publishing it with the port `4567`:
```
{
    "app_name": "hellospark",
    "services": [
        {
            "service_name": "hellospark-service",
            "components": [
                {
                    "component_name": "sparkexample",
                    "image": "registry.giantswarm.io/giantswarm/sparkexample",
                    "ports": [ "4567/tcp" ],
                    "domains": { "hellospark.gigantic.io": "4567" }
                }
            ]
        }
    ]
}
```

## Commands
```
# Build the image:
$ docker build -t registry.giantswarm.io/giantswarm/sparkexample .
# Test the image locally:
$ docker run -p 4567:4567 registry.giantswarm.io/giantswarm/sparkexample
# Push the image:
$ docker push registry.giantswarm.io/giantswarm/sparkexample
# Start the app:
$ swarm create
```

## Next steps

A slightly more advanced TODO example see [https://github.com/giantswarm/todoapp-spark](https://github.com/giantswarm/todoapp-spark)
