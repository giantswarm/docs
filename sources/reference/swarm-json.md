# Valid keys and values for swarm.json

<p class="lastmod">Last edited on November 25, 2014 by Stephan Zeissler</p>

This page should give a rough overview of possible `swarm.json` keys and their values.

> **Note**:
> This is not valid JSON. It's purely for documentation purposes. 

```
{
    // Name of the application. Type: String
    "app_name":"my app name",

    // Array of contained services. Type: JSON
    "services":[
        {   

            // Name of the service. Type: String
            "service_name": "api-service",

            // Array of contained components. Type: JSON
            "components": [
                {

                    // Name of the component. Type: String
                    "component_name": "api",

                    // Docker image to be used. Type: String 
                    // Format: <registry>/<image>:<tag>
                    "image":"giantswarm/flaskexample:0.0.2",

                    // Docker env to inject into docker containers. Type: Array of strings. Optional.
                    // Format: "<key>=<value>"
                    "env": [
                        "SECRET_KEY_BASE=somesecretkeyforrails",
                        "RAILS_ENV=production"
                    ],

                    // Minimum and maximum instances to launch. Optional.
                    "scaling_policy": { "min": 3, "max" : 10 },

                    // Array of export ports. Type: Array of strings.
                    // String format: <port>/<protocol>
                    // Optional.
                    "ports":[ "80/tcp" ],

                    // Array of dependent components. Type: JSON
                    // Format: { 
                    //    "name": <component_name>, 
                    //    "port": <exposed_required_port>, 
                    //    "same_machine": true | false //optional,
                    //    "alias" : <a_different_name_for_the_dependent_component> //optional
                    // }
                    // Optional.
                    "dependencies": [
                        { "name": "redis", "port": 6379 }
                    ],

                    // Map of public domains. Type: JSON
                    // Format: { <url>: <Port> }
                    // Optional.
                    "domains": {
                        "hello.alpha.giantswarm.io": "80",
                        "hello.alpha.io": "80"
                    }

                },
                {
                    "component_name": "redis",
                    "image":"dockerfile/redis",
                    "ports":[ "6379/tcp" ],

                    // Array of mounted volumes. Type: JSON
                    // Format: { "path": <mount_point>, "size": "<nr>" GB }
                    // Optional.
                    "volumes": [
                        { "path": "/mnt/redis", "size": "5 GB" },
                        { "path": "/var/run/redis", "size": "5 GB" }
                    ]
                }
            ]
        }]
}
```
<!--
see
https://git.giantswarm.io/giantswarm/cli/blob/master/dist/examples/api_0.sample.json
https://git.giantswarm.io/giantswarm/user-config/blob/master/user_config.go
-->