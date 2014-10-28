# Valid keys and values for swarm.json

> **Note**:
> This is not valid JSON. It's purely for documentation purpose. 

```
{
    // Name of the application. Type: String
    "app_name":"my app name",

    // Array of contained services. Type: JSON
    "services":[
        {   

            // Name of the service. Type: String.
            "service_name": "api-service",

            // Array of contained components. Type: JSON
            "components": [
                {

                    // Name of the component. Type: String
                    "component_name": "api",

                    // Docker image to be used. Type: String 
                    // Format: <registry>/<image>:<tag>
                    "image":"registry.private.giantswarm.io/redis-example:0.0.2",

                    // TODO
                    "scaling_policy": { "min": 3 },

                    // Array of export ports. Type: Array of strings.
                    // String format: <port>/<protocol>
                    "ports":[ "80/tcp" ],

                    // Array of dependent components. Type: JSON
                    // Format: { "name": <componentname>, "port": <exposed_port> }
                    "dependencies": [
                        { "name": "redis", "port": 6379 }
                    ]
                },
                {
                    "component_name": "redis",
                    "image":"dockerfile/redis",
                    "ports":[ "6379/tcp" ],
                    
                    // Array of mounted volumes. Type: JSON.
                    // Format: { "path": <mount_point>, "size": <nr> GB }
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