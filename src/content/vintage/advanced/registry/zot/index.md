---
linkTitle: In-cluster image caching with Zot
title: In-cluster image caching with Zot
description: Caching container images close to the cluster and as backup within the cluster. 
weight: 110
menu:
  main:
    parent: advanced-registry
user_questions:
  - How can I cache container images within the cluster?
  - How can I have a backup registry for container images?
last_review_date: 2024-07-11
aliases:
  - /guides/in-cluster-container-image-caching/
  - /advanced/in-cluster-container-image-caching/
owner:
  - https://github.com/orgs/giantswarm/teams/team-bigmac
---

Caching container images close to a Kubernetes cluster has many benefits:

- Availability, in case the upstream registry is experiencing an outage
- Pull limits are enforced by certain upstream registries
- Faster boot times simply because of being closer to the cluster

## Using Zot as a container image cache

[Zot](https://zotregistry.dev/) is an OCI-native container image registry.

The [Giant Swarm packaged version](https://github.com/giantswarm/zot) extends it with opinionated components like
auto-scaling, monitoring, Cilium network policies, etc.

### Zot configuration

The Zot binary itself can be configured via `.configFiles.config.json` Helm value as JSON.
The `.mountConfig` values must be set to `true` to enable mounting the configuration file.

```yaml
configFiles:
  config.json: |-
    {
      # ...
    }
```

The full configuration reference can be found at: https://zotregistry.dev/latest/admin-guide/admin-configuration/.

#### Mirroring

You can configure active or on-demand replication via the Zot configuration file.

The below example configures `docker.io` and `k8s.gcr.io` as on-demand mirrors, meaning when and image is
pulled from these registries through the Zot instance, Zot will cache actually pull and cache them.

For the `my-registry.example.org` registry it is set to actively sync all `6.*` tagged images for `my-organization/my-image`.

```json
{
  "extensions": {
    "sync": {
      "enable": true,
      "registries": [
        {
          "urls": [
            "https://docker.io/library"
          ],
          "onDemand": true,
          "tlsVerify": true,
          "maxRetries": 3,
          "retryDelay": "5m"
        },
        {
          "urls": [
            "https://k8s.gcr.io"
          ],
          "onDemand": true,
          "tlsVerify": true,
          "maxRetries": 3,
          "retryDelay": "5m"
        },
        {
          "urls": [
            "https://my-registry.example.org"
          ],
          "onDemand": false,
          "pollInterval": "5m",
          "tlsVerify": true,
          "maxRetries": 3,
          "retryDelay": "5m",
          "onlySigned": false,
          "content": [
            {
              "prefix": "my-organization/my-image",
              "tags": {
                "regex": "^6.*",
                "semver": true
              }
            }
          ]
        }
      ]
    }
  }
}
```

For Zot to be used on the cluster, you need to for example configure `containerd` on the nodes to use Zot as a mirror
for given upstream registries.

For the full mirroring documentation, see https://zotregistry.dev/latest/articles/mirroring/.

#### Authentication

The `.secretFiles` Helm value can be used as a filename-content map for them to be mounted into the container
when `.mountSecret` is set to `true`.

For one, the Zot users and passwords can be configured here for simple HTTP authentication.

To generate the entries use the `htpasswd` tool like:

```shell
htpasswd -bBn admin password
```

And then store them under `.secretFiles.htpasswd`.

```yaml
mountSecret: true
secretFiles:
  htpasswd: |-
    admin:$2y$05$.fR2nhyzstpecApibWVQDOg12aeXG8I4Zq8fW/ez8VJJ9zSc8zBQi
```

Finally, enable it via the configuration file:

```json
{
  "http": {
    "auth": {
      "htpasswd": {
        "path": "/secret/htpasswd"
      }
    },
    "accessControl": {
      "repositories": {
        "**": {
          "policies": [
            {
              "users": [
                "admin"
              ],
              "actions": [
                "read",
                "create",
                "update",
                "delete"
              ]
            }
          ]
        }
      }
    },
    "address": "0.0.0.0",
    "port": "5000"
  }
}
```

For all the possible authentication methods, see: https://zotregistry.dev/latest/admin-guide/admin-configuration/#authentication.

It is also possible to configure the Prometheus service monitor to be authenticated as well.

```yaml
secretFiles:
  htpasswd: |-
    prom:$2y$05$lvhRlI3YHWbQjlhOMPFwY.vGym0e6dpMpQPyTrwTM5X3OVsTGfUJy

serviceMonitor:
  basicAuth:
    username: prom
    password: example
```

You can also use this to set credentials for the synced registries. To do that, let's add a new entry to `.secretFiles`.

```yaml
secretFiles:
  credentials: |-
    {
      "my-registry.example.org": {
        "username": "my-user",
        "password": "my-token"
      }      
    }
```

Then configure the `sync` extension to use that file as a source to authenticate towards registries via the config file.

```json
{
  "extensions": {
    "sync": {
      "credentialsFile": "/secret/credentials"
    }
  }
}
```

### Use cases

#### Memory constraints

Zot can take up a lot of memory over time. In the Giant Swarm packaged app you you can deploy it with a vertical
pod autoscaler. You can set the resource constraints like:

```yaml
giantswarm:
  verticalPodAutoscaler:
    enabled: true
    maxAllowed:
      cpu: 750m # Set this higher than .resources.limits.cpu to stretch limits in case of higher load
      memory: 2048Mi # Set this higher than .resources.limits.memory to stretch limits in case of higher load

resources:
  requests:
    cpu: 300m # The minimum amount of CPU required for your scenario
    memory: 1024Mi # # The minimum amount of memory required for your scenario
  limits:
    cpu: 500m # The generally maximum amount of CPU required for your scenario
    memory: 1536Mi # The generally maximum amount of CPU required for your scenario
```

In case of an OOM kill, VPA controller will dynamically stretch the limits on the deployment based on Prometheus metrics
up to what is set under `.giantswarm.verticalPodAutoscaler.maxAllowed`.

In certain scenarios - in our experience - it is better, more stable to run with a fix amount of memory. You can
enforce the constraint by fixing the memory request and limit to the same value and configuring the
Go Garbage Collector. Do not forget to disable the VPA in this case!

```yaml
giantswarm:
  verticalPodAutoscaler:
    enabled: false

resources:
  requests:
    cpu: 350m
    memory: 1024Mi
  limits:
    cpu: 500m
    memory: 1024Mi

env:
  - name: "GOGC"
    value: "50"
  - name: "GOMEMLIMIT"
    # Set this to about 80% of the memory limit.
    value: "800MiB"
```

For more details on this approach, see: https://tip.golang.org/doc/gc-guide.

### Deployment strategies

Some extension, like `search` can create file locks on the data volume mount. With the `RollingUpdate` strategy,
this will cause the new pods failing to stand up. In such scenarios it is recommended to set it to `Recreate`.

```yaml
strategy:
  type: Recreate
```
