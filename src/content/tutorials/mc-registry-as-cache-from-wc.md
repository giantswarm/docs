---
title: Using the registry in the management cluster as a pull-through cache from the workload cluster
description: For faster deployments, higher resilience, and reduced bandwidth usage, you can use the container registry in the management cluster as a pull-through cache from the workload cluster.
weight: 100
last_review_date: 2024-05-24
owner:
  - https://github.com/orgs/giantswarm/teams/team-phoenix
user_questions:
  - How to use the registry in the management cluster as a pull-through cache?
  - How to reduce container registry costs?
  - How to improve deployment speed?
  - How to increase resilience of deployments?
---

TODO: check page slug/URL after finishing the article content!

Outline

- Link to architecture page: {{ relref "/overview/architecture/registry" }} for basic information and benefits.
- Containerd in every node of the workload cluster is configured to use the local registry as a mirror before pulling from any upstream registry. This way, workloads can specify the upstream registry as the image source and the caching is transparent for developers.
- Ideally set the required configuration when creating the workload cluster.
- Alternatively this can also be done after creation. In that case, it will result in nodes being rolled (terminated and replaced) to apply the new configuration.

Workload cluster configuration example:

```yaml
global:
  components:
    containerd:
      localRegistryCache:
        enabled: true
        mirroredRegistries:
          - registry.example.com
          - gsoci.azurecr.io
        port: 32767
      containerRegistries:
        registry.example.com:
          - endpoint: zot.INSTALLATION.gaws.gigantic.io
        gsoci.azurecr.io:
          - endpoint: gsoci.azurecr.io # Why?
```

Explanation:

Say a pod specifies a container image `registry.example.com/my-namespace/my-image:v1.0.0` and an image pull policy of `IfNotAvailable` or `Always`. As this pod gets scheduled to a cluster node, the containerd runtime will find an alternative endpoint for `registry.example.com` which is `zot.INSTALLATION.gaws.gigantic.io` (note that INSTALLATION is a placeholder for an installation name). That's the registry (Zot) in the management cluster.

If Zot is available, it will first check its storage to find the requested image (TODO: will it check the SHA here?). If found there, the image will be served directly. Otherwise Zot will attempt to pull the image from `registry.example.com`, store it for later use, and serve it to cintainerd. The workload deployment will continue.

If Zot on the management cluster isn't available, containerd will try the next alternative endpoint (if available) and, if still not successful, eventually use the original endpoint `registry.example.com` to attempt an image pull.

More details on the configuration block above:

- With `localRegistryCache` you enable the use of the local registry and configure which upstream registries to cache images for.
    - Each upstream registry you want to cache needs to be listed by its fully qualified domain name.
    - Please leave `gsoci.azurecr.io` intact to allow caching of images required by Giant Swarm platform workloads. TODO: Do we really have to ask for this, or can we make sure via the chart?
    - The `port` number in this case must be the exposed Zot port on the management cluster (32767). TODO: link to chart template position of this definition.
- Under `containerRegistries`, you specify alternative alternative endpoint to be used for upstream registry domain names for which requests get redirected to the caching registry first.
    - The key must be the fully qualified domain name of the upstream registry, matching the names given in `mirroredRegistries`.
    - The `endpoint` is the address of the registry in the management cluster.
    - The `registry.example.com` is an example for a registry that is not part of the Giant Swarm platform.